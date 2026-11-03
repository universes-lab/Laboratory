#!/usr/bin/env python3
# HONC / Qf / R1 / КТ-1 — упаковка work/ ВНУТРИ песочницы, от nobody (процедура 3.2; исправление безопасности
# Интегратора 03.11: «SANDBOX REV3.1 — TWO CORRECTIONS ACCEPTED; ONE SECURITY FIX REQUIRED»).
# Запускается оболочкой kt1_sandbox_run.py в отдельной песочнице bubblewrap: work/ смонтирована только для чтения,
# исходников, ядра и журналов нет. Поэтому даже ошибка здесь не дотянется до файлов хозяина.
# Обход — без следования по ссылкам: os.fwalk(follow_symlinks=False); каждый элемент — lstat относительно дескриптора
# каталога; файл открывается с O_NOFOLLOW | O_NONBLOCK, тип перепроверяется через fstat.
# В архив (stdout, ZIP_STORED, фиксированное время) идут только обычные файлы с именами из [A-Za-z0-9._-].
# Всё прочее — символические ссылки, FIFO, сокеты, устройства, недоступные для чтения файлы и каталоги, недопустимые
# имена — не читается и не упаковывается, а перечисляется в отчёте (stderr, JSON).
import json, os, re, stat, sys, zipfile

ROOT = '/sandbox/work'
SAFE = re.compile(r'^[A-Za-z0-9._-]+$')
KIND = {stat.S_IFLNK: 'symlink', stat.S_IFIFO: 'fifo', stat.S_IFSOCK: 'socket', stat.S_IFCHR: 'char-device', stat.S_IFBLK: 'block-device'}
rejected = []
def reject(path, kind): rejected.append({'path': path, 'type': kind})
def onerror(e):
    n = os.fsdecode(e.filename) if e.filename else '?'
    reject(os.path.relpath(n, ROOT) if os.path.isabs(n) else n, f'unreadable-dir ({e.strerror})')

out = zipfile.ZipFile(sys.stdout.buffer, 'w', zipfile.ZIP_STORED)
for top, dirs, files, dfd in os.fwalk(ROOT, follow_symlinks=False, onerror=onerror):
    rel = os.path.relpath(top, ROOT)
    for name in sorted(dirs + files):
        path = name if rel == '.' else f'{rel}/{name}'
        try: st = os.stat(name, dir_fd=dfd, follow_symlinks=False)
        except OSError as e: reject(path, f'unreadable ({e.strerror})'); continue
        fmt = stat.S_IFMT(st.st_mode)
        if fmt == stat.S_IFDIR:
            if not SAFE.match(name): reject(path, 'name'); dirs.remove(name)      # внутрь каталога с таким именем не входим
            continue
        if name in dirs: dirs.remove(name)                                       # ссылка на каталог: не входим
        if fmt != stat.S_IFREG: reject(path, KIND.get(fmt, 'other')); continue
        if not SAFE.match(name): reject(path, 'name'); continue
        try:
            fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=dfd)
        except OSError as e: reject(path, f'unreadable ({e.strerror})'); continue
        with os.fdopen(fd, 'rb') as f:
            if not stat.S_ISREG(os.fstat(f.fileno()).st_mode): reject(path, 'changed'); continue
            data = f.read()
        zi = zipfile.ZipInfo(path, (2026, 1, 1, 0, 0, 0)); zi.external_attr = 0o100644 << 16
        out.writestr(zi, data)
out.close()
sys.stderr.write(json.dumps({'rejected': rejected}, ensure_ascii=False))
