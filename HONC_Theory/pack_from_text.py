#!/usr/bin/env python3
# Механическая сборка архива из исходников, сданных текстом (Интегратор 03.11, п. 2: упаковка — без изменения логики).
#   python3 -I pack_from_text.py <текст.md> <архив.zip>
# Формат сдачи: для каждого файла — строка «### FILE: относительный/путь» и сразу за ней блок кода в тройных (или более)
# обратных кавычках; язык после кавычек допускается. Содержимое блока пишется в файл дословно, с переводом строки в конце.
# Требования (редакция 3): только LF — текст с CR отвергается, а не исправляется; путь — из сегментов [A-Za-z0-9._-],
# без «.», «..», пустых сегментов, обратных косых и ведущего «/»; не больше 2000 файлов и 20 МиБ на файл.
# Архив воспроизводим: порядок файлов — по пути, время фиксированное, без сжатия (ZIP_STORED). После сборки архив
# перечитывается и сверяется с текстом побайтно (полнота упаковки).
import hashlib, re, sys, zipfile

SAFE = re.compile(r'^[A-Za-z0-9._-]+$')
src, dst = sys.argv[1], sys.argv[2]
raw = open(src, 'rb').read()
if b'\r' in raw: sys.exit('ОТКАЗ: в тексте есть CR (окончания строк CRLF); нужен только LF — текст не исправляется')
lines = raw.decode('utf-8').split('\n')
files, i = {}, 0
head = re.compile(r'^#{1,6}\s*FILE:\s*(\S+)\s*$')
while i < len(lines):
    m = head.match(lines[i])
    if not m:
        i += 1; continue
    path = m.group(1)
    segs = path.split('/')
    if path.startswith('/') or '\\' in path or any(s in ('', '.', '..') for s in segs) or not all(SAFE.match(s) for s in segs) or len(path) > 200:
        sys.exit(f'ОТКАЗ: недопустимый путь {path!r}')
    if path.lower() in {p.lower() for p in files}: sys.exit(f'ОТКАЗ: файл {path} указан дважды')
    j = i + 1
    while j < len(lines) and lines[j].strip() == '': j += 1
    if j >= len(lines) or not lines[j].startswith('```'): sys.exit(f'ОТКАЗ: за заголовком {path} нет блока кода')
    fence = re.match(r'^(`{3,})', lines[j]).group(1)
    k = j + 1
    while k < len(lines) and not (lines[k].startswith(fence) and lines[k].strip() == fence): k += 1
    if k >= len(lines): sys.exit(f'ОТКАЗ: блок кода {path} не закрыт')
    files[path] = ('\n'.join(lines[j + 1:k]) + '\n').encode('utf-8')
    if len(files[path]) > 20 << 20: sys.exit(f'ОТКАЗ: файл {path} больше 20 МиБ')
    i = k + 1
if not files: sys.exit('ОТКАЗ: в тексте нет ни одного файла')
if len(files) > 2000: sys.exit('ОТКАЗ: больше 2000 файлов')
with zipfile.ZipFile(dst, 'w', compression=zipfile.ZIP_STORED) as z:
    for path in sorted(files):
        zi = zipfile.ZipInfo(path, date_time=(2026, 1, 1, 0, 0, 0))
        zi.external_attr = 0o100644 << 16          # обычный файл, rw-r--r--
        z.writestr(zi, files[path])
# Полнота упаковки: архив перечитывается и сверяется с текстом.
with zipfile.ZipFile(dst) as z:
    names = [zi.filename for zi in z.infolist()]
    if names != sorted(files) or any(z.read(n) != files[n] for n in names): sys.exit('ОТКАЗ: архив не совпал с текстом при проверке')
print(f'Источник: {src}; sha256 {hashlib.sha256(raw).hexdigest()}')
print(f'Файлов: {len(files)} (сверены с текстом побайтно)')
for path in sorted(files):
    print(f'{hashlib.sha256(files[path]).hexdigest()}  {path}  ({len(files[path])} байт)')
print(f'Архив: {dst}; sha256 {hashlib.sha256(open(dst, "rb").read()).hexdigest()}')
