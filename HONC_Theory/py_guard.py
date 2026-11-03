# Дополнительный слой для Python внутри песочницы bubblewrap (не единственная защита): audit hook разрешает
# чтение только в KT1_READ (папка прогона внутри песочницы) и в стандартной библиотеке, запись — только в KT1_WRITE;
# запуск процессов и сокеты запрещены. Audit hook не ловит всё (ctypes, C-расширения) — поэтому основная граница —
# пространства имён bubblewrap. Скрипт не меняется: он выполняется через runpy как __main__.
import os, sys, runpy
READ = os.path.realpath(os.environ.get('KT1_READ', '/sandbox'))
WRITE = os.path.realpath(os.environ.get('KT1_WRITE', '/sandbox/work'))
READ_OK = [READ] + sorted({os.path.realpath(p) for p in (sys.base_prefix, sys.prefix, sys.exec_prefix)}) + ['/dev/null', '/dev/urandom', '/proc/self']
WRITE_OK = [WRITE, '/dev/null']
inside = lambda p, roots: any(p == r or p.startswith(r + os.sep) for r in roots)
def hook(event, args):
    if event == 'open':
        path, mode, flags = (list(args) + [None, None])[:3]
        if isinstance(path, int) or path is None: return
        p = os.path.realpath(os.fsdecode(path))
        w = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT))
        if not inside(p, WRITE_OK if w else READ_OK): raise PermissionError(f'kt1-guard: доступ запрещён: {p}')
    elif event.startswith(('subprocess.', 'os.system', 'os.exec', 'os.spawn', 'os.posix_spawn', 'os.fork', 'socket.', 'ctypes.')):
        raise PermissionError(f'kt1-guard: запрещено: {event}')
script = os.path.realpath(sys.argv[1])
sys.argv = sys.argv[1:]
sys.path[:] = [os.path.dirname(script)] + [p for p in sys.path if p and inside(os.path.realpath(p), READ_OK[1:])]
sys.addaudithook(hook)
runpy.run_path(script, run_name='__main__')
