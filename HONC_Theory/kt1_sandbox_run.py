#!/usr/bin/env python3
# HONC / Qf / R1 / КТ-1 — изолированный запуск чужих скриптов без изменений (процедура, редакция 3).
# Поправки Интегратора 03.11 («ISOLATED RUN PROCEDURE v2 — CORRECTIONS REQUIRED»):
#  1. системная песочница: bubblewrap — отдельные пространства имён (файлы, сеть, процессы, IPC, UTS, пользователь,
#     cgroup), без сети, без файловой системы хозяина (видны только /usr, интерпретатор и папки прогона);
#     bubblewrap запускается от непривилегированного пользователя хозяина nobody (65534) через setpriv — внутри и
#     снаружи один и тот же uid 65534, без возможностей (cap-drop ALL, пустой bounding set), no_new_privs; пределы
#     времени, памяти, процессов, файлов. Node --permission и py_guard — дополнительные слои, не единственная защита;
#  2. исходники — только для чтения; запись — только в work/; доверенные журналы (log/) в песочницу не монтируются;
#  3. ZIP проверяется до распаковки: пути, символические ссылки, дубликаты, размеры, сжатие; в режимах без ядра
#     подключение ядра отвергается;
#  4. Д-3: sha256 ядра сравнивается с зашитым эталоном замороженной сборки;
#  5. node-check — без ядра;
#  6. полные stdout / stderr, код выхода, точная команда, версии среды, суммы исходников до и после.
# Адресные поправки Интегратора 03.11 («SANDBOX REV3 — ACCEPTED WITH TWO TARGETED CORRECTIONS»):
#  7. статус оболочки (runner_status) и статус испытуемого скрипта (test_status) разделены; код выхода оболочки
#     сообщает о провале испытания (таблица EXIT ниже);
#  8. stdout + stderr пишутся в журнал потоком, общий предел объёма; work/ — отдельная tmpfs с квотой байт и файлов;
#     при превышении прогон прерывается, статус OUTPUT_LIMIT / WORK_LIMIT, протокол помечен неполным, усечённый
#     файл вывода получает в имени .TRUNCATED.
#
#   kt1_sandbox_run.py --mode {a5,d3-check,d3-selftest,d3-run} --label L --archive A.zip --sha SHA
#                      [--lang node|python] [--entry путь] [--kernel K.zip] [--timeout с] [--mem ГиБ]
#                      [--max-output МиБ] [--work-quota МиБ] [--work-files N] [-- аргументы…]
import argparse, datetime, hashlib, io, json, os, re, shutil, signal, stat, subprocess, sys, threading, time, zipfile

FROZEN_KERNEL_SHA = 'ecb35112d85911c810d70942f3655ddc25ed19c9047befff2cb7dfbf6ea268ea'   # запись заморозки 03.11
KERNEL_NAMES = re.compile(r'(^|/)(kt1\.js|wp[0-4]_[a-z0-9_]+\.js|registry_S3\.json|WP[0-4]_[A-Za-z_]+\.md)$|HONC_Qf_KT1_Kernel', re.I)
LIMITS = dict(max_files=2000, max_file=20 << 20, max_total=100 << 20, max_ratio=100)
HERE = os.path.dirname(os.path.realpath(__file__))
RUNS_ROOT = '/var/tmp/kt1-runs'        # вне папок сессии (те закрыты 0700 для root): nobody должен пройти к src и work
NOBODY = 65534
TMPFS = 256 << 20                      # предел /tmp и /dev/shm внутри песочницы
# Код выхода оболочки: 0 — испытание завершилось с кодом 0; 1 — испытуемый скрипт завершился с ненулевым кодом;
# 2 — отказ до запуска; 3 — превышен предел (время, вывод, work/) — протокол неполный; 4 — ошибка самой оболочки.
EXIT = {'EXIT_0': 0, 'EXIT_NONZERO': 1, 'REFUSED': 2, 'TIMEOUT': 3, 'OUTPUT_LIMIT': 3, 'WORK_LIMIT': 3, 'RUNNER_ERROR': 4}
SEVERITY = ['EXIT_0', 'EXIT_NONZERO', 'TIMEOUT', 'WORK_LIMIT', 'OUTPUT_LIMIT']        # итог по нескольким запускам — худший
FULL_BYTES, FULL_FILES = 1 << 20, 16   # work/ считается исчерпанной, если свободно меньше 1 МиБ или меньше 16 файлов
NODE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(shutil.which('node'))))      # /opt/node22
PYTHON = os.path.realpath('/usr/bin/python3')                                              # без /etc/alternatives
SAFE = re.compile(r'^[A-Za-z0-9._-]+$')

def sha(b): return hashlib.sha256(b).hexdigest()
def fsha(p):
    with open(p, 'rb') as f: return sha(f.read())

class Refuse(Exception): pass

def check_zip(path, allow_kernel_names):
    """Проверка содержимого архива до распаковки. Возвращает список (имя, данные)."""
    try: z = zipfile.ZipFile(path)
    except zipfile.BadZipFile as e: raise Refuse(f'не ZIP: {e}')
    infos, seen, total, out = z.infolist(), set(), 0, []
    if len(infos) > LIMITS['max_files']: raise Refuse(f'файлов {len(infos)} > {LIMITS["max_files"]}')
    for zi in infos:
        n = zi.filename
        if zi.is_dir(): continue
        segs = n.split('/')
        if n.startswith('/') or '\\' in n or ':' in n or any(s in ('', '.', '..') for s in segs) or not all(SAFE.match(s) for s in segs):
            raise Refuse(f'недопустимый путь в архиве: {n!r}')
        mode = zi.external_attr >> 16
        if mode and not stat.S_ISREG(mode): raise Refuse(f'не обычный файл (символическая ссылка или иное): {n}')
        key = n.lower()
        if key in seen: raise Refuse(f'дубликат пути: {n}')
        seen.add(key)
        if zi.file_size > LIMITS['max_file']: raise Refuse(f'файл больше предела: {n} ({zi.file_size} байт)')
        if zi.compress_size and zi.file_size / zi.compress_size > LIMITS['max_ratio']: raise Refuse(f'подозрительное сжатие: {n}')
        total += zi.file_size
        if total > LIMITS['max_total']: raise Refuse('суммарный размер больше предела')
        if not allow_kernel_names and (KERNEL_NAMES.search(n) or n.lower().endswith('.zip')):
            raise Refuse(f'файл ядра или вложенный архив в режиме без ядра: {n}')
        data = z.read(zi)
        if len(data) != zi.file_size: raise Refuse(f'распаковано не полностью: {n}')
        out.append((n, data))
    return out

def extract(files, root):
    os.makedirs(root, exist_ok=True)
    for n, data in files:
        p = os.path.join(root, n)
        assert os.path.realpath(p).startswith(os.path.realpath(root) + os.sep)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'xb') as f: f.write(data)
    # только чтение: файлы 0444, папки 0555
    for d, ds, fs in os.walk(root):
        for f in fs: os.chmod(os.path.join(d, f), 0o444)
        os.chmod(d, 0o555)

def tree(root):
    res = {}
    for d, ds, fs in os.walk(root):
        for f in sorted(fs):
            p = os.path.join(d, f)
            if os.path.islink(p): res[os.path.relpath(p, root)] = 'SYMLINK'; continue
            res[os.path.relpath(p, root)] = fsha(p)
    return dict(sorted(res.items()))

def new_run_dir(label):
    """Новая пустая папка прогона, без перезаписи прежних. Владелец root; nobody может только пройти (0711)."""
    os.makedirs(RUNS_ROOT, exist_ok=True); os.chmod(RUNS_ROOT, 0o711)
    ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    base = os.path.join(RUNS_ROOT, f'{label}-{ts}'); run, k = base, 1
    while True:
        try: os.makedirs(run); break
        except FileExistsError: k += 1; run = f'{base}-{k}'
    os.chmod(run, 0o711)
    log = os.path.join(run, 'log'); os.makedirs(log); os.chmod(log, 0o700)      # доверенный журнал: nobody не читает и не пишет
    work = os.path.join(run, 'work'); os.makedirs(work); os.chown(work, NOBODY, NOBODY); os.chmod(work, 0o700)
    return run, ts

def mount_work(work, quota_bytes, max_files):
    """work/ — отдельная tmpfs с жёсткой квотой байт и файлов (inode), владелец nobody."""
    subprocess.run(['mount', '-t', 'tmpfs', '-o', f'size={quota_bytes},nr_inodes={max_files},mode=0700,uid={NOBODY},gid={NOBODY},nosuid,nodev',
                    'tmpfs', work], check=True, capture_output=True)

def work_full(work):
    s = os.statvfs(work)
    return s.f_bavail * s.f_frsize < FULL_BYTES or s.f_favail < FULL_FILES

def nobody_procs():
    """Процессы пользователя nobody (65534) в контейнере — только из песочниц этой оболочки."""
    n = 0
    for d in os.listdir('/proc'):
        if d.isdigit():
            try:
                with open(f'/proc/{d}/status') as f:
                    if any(l.startswith('Uid:') and l.split()[1] == str(NOBODY) for l in f): n += 1
            except OSError: pass
    return n

def wait_nobody(seconds=10):
    """Дождаться, пока ядро снимет пространства PID прежних песочниц; вернуть остаток."""
    for _ in range(int(seconds * 10)):
        if nobody_procs() == 0: return 0
        time.sleep(0.1)
    return nobody_procs()

def execute(cmd, so, se, work, timeout, max_output):
    """Запуск: stdout и stderr — потоком в файлы журнала, общий предел объёма; сторож квоты work/ и срока.
    Превышение — немедленное прерывание всей песочницы (SIGKILL группе bubblewrap; --die-with-parent добивает остальное)."""
    p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
    st = {'written': 0, 'reason': None, 'dropped': {'stdout': 0, 'stderr': 0}}
    lock = threading.Lock()
    def kill(reason):
        with lock:
            if st['reason'] is None: st['reason'] = reason
        try: os.killpg(p.pid, signal.SIGKILL)
        except ProcessLookupError: pass
    def pump(pipe, path, name):
        with open(path, 'wb') as f:
            while True:
                chunk = pipe.read1(1 << 16)
                if not chunk: break
                with lock:
                    take = max(0, min(len(chunk), max_output - st['written']))
                    st['written'] += take; st['dropped'][name] += len(chunk) - take
                if take: f.write(chunk[:take])
                if take < len(chunk): kill('OUTPUT_LIMIT')
    th = [threading.Thread(target=pump, args=(p.stdout, so, 'stdout')), threading.Thread(target=pump, args=(p.stderr, se, 'stderr'))]
    for t in th: t.start()
    t0 = time.time()
    while p.poll() is None:
        if work_full(work): kill('WORK_LIMIT')
        if time.time() - t0 > timeout + 30: kill('TIMEOUT')     # запасной срок снаружи песочницы, сверх timeout внутри
        time.sleep(0.05)
    for t in th: t.join(60)
    dt = time.time() - t0
    st['leftover'] = wait_nobody()
    if st['reason'] is None and work_full(work): st['reason'] = 'WORK_LIMIT'
    if st['reason'] is None and p.returncode in (124, 137) and dt >= timeout: st['reason'] = 'TIMEOUT'
    status = st['reason'] or ('EXIT_0' if p.returncode == 0 else 'EXIT_NONZERO')
    return p.returncode, dt, status, st['dropped'], st['leftover']

def bwrap(run, lang, extra_binds, env, inner, mem_gib, timeout):
    cmd = ['setpriv', f'--reuid={NOBODY}', f'--regid={NOBODY}', '--clear-groups', '--no-new-privs', '--bounding-set=-all',
           'bwrap', '--unshare-all', '--die-with-parent', '--new-session', '--cap-drop', 'ALL', '--clearenv']
    for k, v in env.items(): cmd += ['--setenv', k, v]
    cmd += ['--ro-bind', '/usr', '/usr', '--symlink', 'usr/bin', '/bin', '--symlink', 'usr/lib', '/lib', '--symlink', 'usr/lib64', '/lib64',
            '--proc', '/proc', '--dev', '/dev', '--size', str(TMPFS), '--tmpfs', '/dev/shm', '--remount-ro', '/dev',
            '--size', str(TMPFS), '--tmpfs', '/tmp']                     # /tmp и /dev/shm — в памяти, по 256 МиБ; /dev — только чтение
    if lang in ('node', 'node-check'): cmd += ['--ro-bind', NODE_ROOT, NODE_ROOT]
    cmd += ['--ro-bind', os.path.join(run, 'src'), '/sandbox/src', '--bind', os.path.join(run, 'work'), '/sandbox/work']
    for a, b in extra_binds: cmd += ['--ro-bind', a, b]
    cmd += ['--remount-ro', '/']                                          # корень песочницы (tmpfs bubblewrap) — только чтение
    cmd += ['--chdir', '/sandbox/src', '--uid', '65534', '--gid', '65534']
    lim = ['prlimit', '--nproc=256', '--nofile=512', f'--fsize={256 << 20}', f'--cpu={timeout + 5}', f'--as={mem_gib << 30}', '--',
           'timeout', '--kill-after=5', str(timeout)]
    return cmd + lim + inner

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', required=True, choices=['a5', 'd3-check', 'd3-selftest', 'd3-run'])
    ap.add_argument('--label', required=True); ap.add_argument('--archive', required=True); ap.add_argument('--sha', required=True)
    ap.add_argument('--lang', choices=['node', 'python'], default='node'); ap.add_argument('--entry')
    ap.add_argument('--kernel'); ap.add_argument('--timeout', type=int, default=1800); ap.add_argument('--mem', type=int, default=8)
    ap.add_argument('--max-output', type=int, default=64, help='МиБ: общий предел stdout + stderr на весь прогон (все запуски)')
    ap.add_argument('--work-quota', type=int, default=512, help='МиБ: квота work/')
    ap.add_argument('--work-files', type=int, default=20000, help='квота числа файлов и папок в work/')
    ap.add_argument('args', nargs='*')
    a = ap.parse_args()
    if not SAFE.match(a.label): sys.exit('ОТКАЗ: метка прогона — только [A-Za-z0-9._-]')
    run, ts = new_run_dir(a.label)
    log, work = os.path.join(run, 'log'), os.path.join(run, 'work')
    rec = {'label': a.label, 'mode': a.mode, 'date_utc': ts, 'archive': os.path.basename(a.archive),
           'runner_sha256': fsha(os.path.realpath(__file__)), 'argv': sys.argv[1:],
           'limits': {'timeout_s': a.timeout, 'address_space_gib': a.mem, 'output_bytes': a.max_output << 20,
                      'work_bytes': a.work_quota << 20, 'work_files': a.work_files, 'nproc': 256, 'nofile': 512,
                      'file_bytes': 256 << 20, 'tmp_bytes': TMPFS, 'dev_shm_bytes': TMPFS}}
    mounted = False
    def finish(runner_status, test_status, why=None):
        rec['runner_status'] = runner_status; rec['test_status'] = test_status
        rec['protocol_complete'] = runner_status == 'COMPLETED' and test_status in ('EXIT_0', 'EXIT_NONZERO')
        if why: rec['refused' if runner_status == 'REFUSED' else 'runner_error'] = why
        code = EXIT[test_status] if runner_status == 'COMPLETED' else EXIT[runner_status]
        rec['runner_exit_code'] = code
        with open(os.path.join(log, 'summary.json'), 'w') as f: json.dump(rec, f, ensure_ascii=False, indent=1)
        outzip = run + '-out.zip'
        with zipfile.ZipFile(outzip, 'w', zipfile.ZIP_DEFLATED) as z:
            for base in ('log', 'work'):
                for d, ds, fs in os.walk(os.path.join(run, base)):
                    for fn in sorted(fs): p = os.path.join(d, fn); z.write(p, os.path.relpath(p, run))
        if mounted:                                     # копия work/ на диск рядом, затем tmpfs снимается
            shutil.copytree(work, os.path.join(run, 'work.saved'), symlinks=True)
            subprocess.run(['umount', work], check=False)
        print(json.dumps({**rec, 'run_dir': run, 'out_zip': outzip, 'out_zip_sha256': fsha(outzip)}, ensure_ascii=False, indent=1))
        sys.exit(code)
    try:
        for f in [a.archive] + ([a.kernel] if a.kernel else []):
            if not os.path.isfile(f): raise Refuse(f'файл не найден: {f}')
        got = fsha(a.archive); rec['archive_sha256'] = got
        if got != a.sha: raise Refuse(f'контрольная сумма архива {got} не совпадает с зафиксированной {a.sha}')
        files = check_zip(a.archive, allow_kernel_names=False)
        extract(files, os.path.join(run, 'src'))
        rec['src_before'] = tree(os.path.join(run, 'src'))
        binds, env = [], {'PATH': f'{NODE_ROOT}/bin:/usr/bin:/bin', 'LANG': 'C.UTF-8', 'HOME': '/sandbox/work', 'KT1_OUT': '/sandbox/work', 'KT1_RUN': '/sandbox'}
        if a.mode == 'd3-run':
            if not a.kernel: raise Refuse('d3-run: нужен --kernel')
            ks = fsha(a.kernel); rec['kernel_sha256'] = ks
            if ks != FROZEN_KERNEL_SHA: raise Refuse(f'ядро {ks} — не замороженная сборка {FROZEN_KERNEL_SHA}')
            extract(check_zip(a.kernel, allow_kernel_names=True), os.path.join(run, 'kernel'))
            rec['kernel_before'] = tree(os.path.join(run, 'kernel'))
            binds.append((os.path.join(run, 'kernel'), '/sandbox/kernel')); env['KT1_DIR'] = '/sandbox/kernel/kt1'
        elif a.kernel: raise Refuse(f'режим {a.mode}: подключение ядра запрещено')
        if a.lang == 'python':
            gdir = os.path.join(run, 'guard'); os.makedirs(gdir); shutil.copy(os.path.join(HERE, 'py_guard.py'), gdir)
            os.chmod(os.path.join(gdir, 'py_guard.py'), 0o444); os.chmod(gdir, 0o555)
            rec['guard_sha256'] = fsha(os.path.join(gdir, 'py_guard.py'))   # копия в папке прогона, в песочнице — только чтение
            binds.append((gdir, '/sandbox/guard'))
        def ver(cmd):
            try: return subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip() or '—'
            except Exception as e: return f'нет ({e})'
        rec['env'] = {'node': ver(['node', '--version']), 'python': ver([PYTHON, '--version']), 'bwrap': ver(['bwrap', '--version']),
                      'uname': ' '.join(os.uname()[i] for i in (0, 2, 4)), 'sandbox': 'setpriv nobody (65534) → bubblewrap: unshare-all, cap-drop ALL, без сети; /usr и интерпретатор — только чтение'}
        jobs = []
        if a.mode == 'd3-check':
            for n in sorted(k for k in rec['src_before'] if k.endswith('.js')): jobs.append(('node-check', ['node', '--check', n]))
        else:
            if not a.entry: raise Refuse('нужен --entry')
            if a.entry not in rec['src_before']: raise Refuse(f'входного файла {a.entry} нет в архиве')
            if a.lang == 'node': inner = ['node', '--permission', '--allow-fs-read=/sandbox', '--allow-fs-write=/sandbox/work', a.entry, *a.args]
            else:
                env['KT1_READ'] = '/sandbox'; env['KT1_WRITE'] = '/sandbox/work'
                inner = [PYTHON, '-I', '/sandbox/guard/py_guard.py', a.entry, *a.args]
            jobs.append((a.lang, inner))
        mount_work(work, a.work_quota << 20, a.work_files); mounted = True
        rec['runs'] = []; budget = a.max_output << 20         # предел вывода — общий на весь прогон
        for k, (lang, inner) in enumerate(jobs):
            cmd = bwrap(run, lang, binds, env, inner, a.mem, a.timeout)
            so, se = os.path.join(log, f'stdout_{k:03d}.txt'), os.path.join(log, f'stderr_{k:03d}.txt')
            if wait_nobody(): raise RuntimeError('перед запуском уже есть процессы nobody — песочница не изолирована от прежних прогонов')
            rc, dt, status, dropped, left = execute(cmd, so, se, work, a.timeout, budget)
            r = {'command': cmd, 'exit_code': rc, 'seconds': round(dt, 3), 'test_status': status, 'leftover_processes': left}
            for name, path in (('stdout', so), ('stderr', se)):
                if dropped[name]:                         # усечённый вывод не выдаётся за полный: метка в имени файла и в журнале
                    cut = path[:-4] + '.TRUNCATED.txt'; os.rename(path, cut); path = cut
                r[name] = os.path.basename(path); r[f'{name}_sha256'] = fsha(path); r[f'{name}_bytes'] = os.path.getsize(path)
                r[f'{name}_truncated'] = bool(dropped[name]); r[f'{name}_bytes_dropped_at_least'] = dropped[name]
            rec['runs'].append(r); budget -= r['stdout_bytes'] + r['stderr_bytes']
            if status in ('TIMEOUT', 'OUTPUT_LIMIT', 'WORK_LIMIT'): break   # прогон прерван; дальнейшие запуски не делаются
        rec['jobs_planned'] = len(jobs); rec['jobs_run'] = len(rec['runs'])
        rec['src_after'] = tree(os.path.join(run, 'src'))
        rec['src_unchanged'] = rec['src_after'] == rec['src_before']
        if 'kernel_before' in rec: rec['kernel_unchanged'] = tree(os.path.join(run, 'kernel')) == rec['kernel_before']
        rec['work_files'] = tree(work)
        rec['work_bytes'] = sum(os.path.getsize(os.path.join(d, f)) for d, ds, fs in os.walk(work) for f in fs)
        worst = max((r['test_status'] for r in rec['runs']), key=SEVERITY.index, default='EXIT_0')
        finish('COMPLETED', worst)
    except Refuse as e:
        finish('REFUSED', 'NOT_RUN', str(e))
    except Exception as e:                                # ошибка самой оболочки: журнал пишется, код 4
        finish('RUNNER_ERROR', 'NOT_RUN', f'{type(e).__name__}: {e}')

if __name__ == '__main__':
    main()
