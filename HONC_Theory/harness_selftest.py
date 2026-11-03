#!/usr/bin/env python3
# Самопроверка среды исполнения (процедура, редакция 3). Опровергающие пробы: что песочница отвергает и что пропускает.
#   python3 -I harness_selftest.py <замороженный архив ядра>
# Пробы пишутся во временную папку; ядро подключается только в пробе d3-run.
import hashlib, json, os, shutil, subprocess, sys, tempfile, zipfile
HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, HERE)
import kt1_sandbox_run as R

KZIP = os.path.realpath(sys.argv[1])
KJS = os.path.join(os.path.dirname(os.path.dirname(KZIP)), 'kt1', 'kt1.js')   # файл ядра на хозяине — для проб чтения
T = tempfile.mkdtemp(prefix='kt1-selftest-')
res, fails = [], []
def ok(cond, msg): (res if cond else fails).append(msg)
def mkzip(name, entries, symlink=None):
    p = os.path.join(T, name)
    with zipfile.ZipFile(p, 'w') as z:
        for n, d in entries:
            zi = zipfile.ZipInfo(n, (2026, 1, 1, 0, 0, 0)); zi.external_attr = 0o100644 << 16; z.writestr(zi, d)
        if symlink:
            zi = zipfile.ZipInfo(symlink[0], (2026, 1, 1, 0, 0, 0)); zi.external_attr = 0o120777 << 16; z.writestr(zi, symlink[1])
    return p
def run(*args):
    p = subprocess.run([sys.executable, '-I', os.path.join(HERE, 'kt1_sandbox_run.py'), *args], capture_output=True, text=True)
    return json.loads(p.stdout), p.returncode
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def out(r, k=0): return open(os.path.join(r['run_dir'], 'log', f'stdout_{k:03d}.txt')).read()
def outer(label, files, lang, inner):
    """Только внешний слой: та же песочница, что у прогона, но без Node --permission и без py_guard."""
    d, _ = R.new_run_dir(label); os.makedirs(os.path.join(d, 'src'))
    for n, data in files.items(): open(os.path.join(d, 'src', n), 'w').write(data); os.chmod(os.path.join(d, 'src', n), 0o444)
    os.chmod(os.path.join(d, 'src'), 0o555)
    env = {'PATH': f'{R.NODE_ROOT}/bin:/usr/bin:/bin', 'KT1_OUT': '/sandbox/work'}
    p = subprocess.run(R.bwrap(d, lang, [], env, inner, 8, 60), capture_output=True, text=True)
    return p, d

probe_js = f"""const fs=require('fs'),path=require('path');const o={{}};
const t=f=>{{try{{f();return 'ALLOWED'}}catch(e){{return 'blocked '+(e.code||e.name)}}}};
o.kernel=t(()=>fs.readFileSync({json.dumps(KJS)}));o.srcWrite=t(()=>fs.writeFileSync(path.join(__dirname,'p.js'),'x'));
o.child=t(()=>require('child_process').execSync('id'));o.work=t(()=>fs.writeFileSync(path.join(process.env.KT1_OUT,'w.txt'),'1'));
require('net').connect(443,'1.1.1.1').on('error',e=>{{o.net='blocked '+e.code;console.log(JSON.stringify(o))}}).on('connect',()=>{{o.net='ALLOWED';console.log(JSON.stringify(o));process.exit(0)}});"""
# 1. Полный режим а-5 (оба слоя)
z = mkzip('a5.zip', [('a5/p.js', probe_js)])
r, _ = run('--mode', 'a5', '--label', 'st-a5', '--archive', z, '--sha', sha(z), '--entry', 'a5/p.js')
o = json.loads(out(r))
ok(all(o[k].startswith('blocked') for k in ('kernel', 'srcWrite', 'child', 'net')) and o['work'] == 'ALLOWED' and r['src_unchanged'], f'а-5, оба слоя: {o}')
# 2. Только внешний слой (bubblewrap без --permission) — граница держится сама
p, d = outer('st-outer-node', {'p.js': probe_js}, 'node', ['node', 'p.js'])
o2 = json.loads(p.stdout)
ok(o2['kernel'] == 'blocked ENOENT' and o2['srcWrite'] == 'blocked EROFS' and o2['net'] == 'blocked ENETUNREACH' and o2['work'] == 'ALLOWED', f'только bubblewrap: {o2}')
# 2а. Пользователь хозяина: файл, созданный в песочнице, принадлежит nobody (65534) и снаружи, а не root
st = os.stat(os.path.join(d, 'work', 'w.txt'))
ok(st.st_uid == 65534 and st.st_gid == 65534, f'пользователь хозяина для процесса в песочнице: uid {st.st_uid}, gid {st.st_gid}')
# 2б. Предел числа процессов (nproc 256) действует: 400 фоновых процессов не создаются
fb = 'n=0; for i in $(seq 1 400); do sleep 30 2>/dev/null & done; echo "процессов: $(ls /proc | grep -c \'^[0-9]\')"\n'
p, d = outer('st-outer-fork', {'fb.sh': fb}, 'python', ['/bin/sh', 'fb.sh'])
ok('Cannot fork' in p.stderr, f'предел процессов: {(p.stderr.strip().splitlines() or ["—"])[-1]} {p.stdout.strip()}')
# 2г. Файловые системы в памяти ограничены (/tmp и /dev/shm — по 256 МиБ), /dev и корень — только чтение, /etc нет
fs_sh = ('for f in /tmp/x /dev/shm/x; do dd if=/dev/zero of=$f bs=1M count=400 2>/dev/null; echo "$f $(stat -c %s $f)"; rm -f $f; done; '
         'echo 1 > /dev/x 2>/dev/null && echo "/dev ALLOWED" || echo "/dev blocked"; echo 1 > /x 2>/dev/null && echo "/ ALLOWED" || echo "/ blocked"; '
         '[ -e /etc ] && echo "/etc видна" || echo "/etc нет"\n')
p, d = outer('st-outer-fs', {'fs.sh': fs_sh}, 'python', ['/bin/sh', 'fs.sh'])
lim = str(R.TMPFS)
ok(p.stdout.split() == ['/tmp/x', lim, '/dev/shm/x', lim, '/dev', 'blocked', '/', 'blocked', '/etc', 'нет'], f'память и корень: {" ".join(p.stdout.split())}')
# 2в. Журнал прогона недоступен процессу в песочнице (log не монтируется; на хозяине — 0700 root)
ok(oct(os.stat(os.path.join(r['run_dir'], 'log')).st_mode & 0o777) == '0o700' and os.stat(os.path.join(r['run_dir'], 'log')).st_uid == 0,
   'доверенный журнал: 0700, владелец root, в песочницу не монтируется')
# 3. Отказы до распаковки
bad = {
    'обход пути': mkzip('b1.zip', [('../x.js', '1')]),
    'абсолютный путь': mkzip('b2.zip', [('/etc/x.js', '1')]),
    'символическая ссылка': mkzip('b3.zip', [('a.js', '1')], symlink=('l.js', '/etc/passwd')),
    'дубликат': mkzip('b4.zip', [('a.js', '1'), ('A.js', '2')]),
    'файл ядра в режиме а-5': mkzip('b5.zip', [('x/kt1.js', '1')]),
    'вложенный архив': mkzip('b6.zip', [('k.zip', '1')]),
}
for nm, p in bad.items():
    r, code = run('--mode', 'a5', '--label', 'st-bad', '--archive', p, '--sha', sha(p), '--entry', 'a.js')
    ok(code == 2 and 'refused' in r, f'отказ — {nm}: {r.get("refused")}')
r, code = run('--mode', 'a5', '--label', 'st-bad', '--archive', z, '--sha', '0' * 64, '--entry', 'a5/p.js')
ok(code == 2 and 'не совпадает' in r.get('refused', ''), f'отказ — сумма архива: {r.get("refused")}')
r, code = run('--mode', 'a5', '--label', 'st-bad', '--archive', z, '--sha', sha(z), '--entry', 'a5/p.js', '--kernel', KZIP)
ok(code == 2 and 'запрещено' in r.get('refused', ''), f'отказ — ядро в режиме а-5: {r.get("refused")}')
fake = mkzip('fake_kernel.zip', [('kt1/kt1.js', 'module.exports={}')])
s3 = mkzip('s.zip', [('run.js', "console.log(1)")])
r, code = run('--mode', 'd3-run', '--label', 'st-bad', '--archive', s3, '--sha', sha(s3), '--entry', 'run.js', '--kernel', fake)
ok(code == 2 and 'не замороженная' in r.get('refused', ''), f'отказ — чужое ядро в d3-run: {r.get("refused")}')
# 4. d3-run на замороженном ядре: случай К1 через KT1_DIR; печатается только версия ядра и наличие протокола (значений ядра в журнале нет)
suite = mkzip('suite.zip', [('run.js', "const path=require('path');const K=require(path.join(process.env.KT1_DIR,'kt1'));"
    "const m=Array.from({length:5},()=>({theta:0,phi:0,delta:0}));const p=K.run({id:'K1',thread:{n:5,links:m},hangs:[]});"
    "console.log('protocol', p.kernel.version, typeof p.verdict); require('fs').writeFileSync(path.join(process.env.KT1_OUT,'K1.json'),K.serialize(p));")])
r, code = run('--mode', 'd3-run', '--label', 'st-d3', '--archive', suite, '--sha', sha(suite), '--entry', 'run.js', '--kernel', KZIP)
ok(code == 0 and out(r).startswith('protocol kt1-2026-11-02-wp4 object') and r['kernel_sha256'] == R.FROZEN_KERNEL_SHA and 'K1.json' in r['work_files']
   and r['kernel_unchanged'] and r['src_unchanged'], f'd3-run, замороженное ядро: {out(r).strip()}')
# 4а. d3-run: набор пытается изменить ядро — только чтение
tamper = mkzip('tamper.zip', [('t.js', "const fs=require('fs'),path=require('path');let s;try{fs.appendFileSync(path.join(process.env.KT1_DIR,'kt1.js'),'//x');s='ALLOWED'}catch(e){s='blocked '+e.code}console.log(s)")])
r, code = run('--mode', 'd3-run', '--label', 'st-tamper', '--archive', tamper, '--sha', sha(tamper), '--entry', 't.js', '--kernel', KZIP)
ok(out(r).startswith('blocked') and r['kernel_unchanged'], f'd3-run, запись в ядро: {out(r).strip()}')
# 5. d3-check: синтаксис, без ядра
chk = mkzip('chk.zip', [('ok.js', 'console.log(1)\n'), ('bad.js', 'console.log(;\n')])
r, code = run('--mode', 'd3-check', '--label', 'st-chk', '--archive', chk, '--sha', sha(chk))
ok([x['exit_code'] for x in r['runs']] == [1, 0] and 'kernel_sha256' not in r, f'd3-check: коды {[x["exit_code"] for x in r["runs"]]}')
# 6. Пределы времени и памяти
loop = mkzip('loop.zip', [('l.js', 'for(;;){}\n')])
r, code = run('--mode', 'a5', '--label', 'st-time', '--archive', loop, '--sha', sha(loop), '--entry', 'l.js', '--timeout', '3')
ok(r['runs'][0]['exit_code'] in (124, 137) and r['runs'][0]['seconds'] < 15, f'предел времени: код {r["runs"][0]["exit_code"]}, {r["runs"][0]["seconds"]} с')
mem = mkzip('mem.zip', [('m.js', 'const a=[];for(;;)a.push(new Float64Array(1e7));\n')])
r, code = run('--mode', 'a5', '--label', 'st-mem', '--archive', mem, '--sha', sha(mem), '--entry', 'm.js', '--mem', '2', '--timeout', '60')
se = open(os.path.join(r['run_dir'], 'log', 'stderr_000.txt')).read()
ok(r['runs'][0]['exit_code'] != 0 and 'allocation failed' in se, f'предел памяти: код {r["runs"][0]["exit_code"]}, {se.splitlines()[4] if len(se.splitlines()) > 4 else se.strip()}')
# 7. Python: оба слоя
probe_py = f"""import os, json, socket, subprocess
def t(f):
    try: f(); return 'ALLOWED'
    except Exception as e: return 'blocked ' + type(e).__name__
o = {{'kernel': t(lambda: open({KJS!r}).read()), 'srcWrite': t(lambda: open(__file__, 'w').write('x')),
      'child': t(lambda: subprocess.run(['id'])), 'net': t(lambda: socket.create_connection(('1.1.1.1', 443), 3)),
      'work': t(lambda: open(os.path.join(os.environ['KT1_OUT'], 'w.txt'), 'w').write('1'))}}
print(json.dumps(o))"""
pz = mkzip('py.zip', [('a5/p.py', probe_py)])
r, code = run('--mode', 'a5', '--label', 'st-py', '--archive', pz, '--sha', sha(pz), '--lang', 'python', '--entry', 'a5/p.py')
o3 = json.loads(out(r))
ok(all(o3[k].startswith('blocked') for k in ('kernel', 'srcWrite', 'child', 'net')) and o3['work'] == 'ALLOWED' and r.get('guard_sha256') == sha(os.path.join(HERE, 'py_guard.py')), f'Python, оба слоя: {o3}')
# 8. Python — только внешний слой (без py_guard): граница держится без audit hook
probe_py2 = probe_py.replace("open(__file__, 'w')", "open('/sandbox/src/p.py', 'w')").replace("subprocess.run(['id'])", "subprocess.run(['id'], capture_output=True)").replace("'blocked ' + type(e).__name__", "'blocked ' + type(e).__name__ + ' ' + str(getattr(e, 'errno', ''))")
p, d = outer('st-outer-py', {'p.py': probe_py2}, 'python', [R.PYTHON, '-I', 'p.py'])
o4 = json.loads(p.stdout)
ok(o4['kernel'].startswith('blocked FileNotFoundError') and o4['srcWrite'].startswith('blocked OSError 30') and o4['net'].startswith('blocked OSError 101') and o4['work'] == 'ALLOWED',
   f'Python, только bubblewrap: {o4}')
shutil.rmtree(T, ignore_errors=True)
for m in res: print('OK  ', m)
for m in fails: print('FAIL', m)
print(f'Самопроверка: {len(res)} прошло, {len(fails)} не прошло')
sys.exit(1 if fails else 0)
