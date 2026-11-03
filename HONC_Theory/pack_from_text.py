#!/usr/bin/env python3
# Механическая сборка архива из исходников, сданных текстом (Интегратор 03.11, п. 2: упаковка — без изменения логики).
#   python3 -I pack_from_text.py <текст.md> <архив.zip>
# Формат сдачи: для каждого файла — строка «### FILE: относительный/путь» и сразу за ней блок кода в тройных
# обратных кавычках (язык после кавычек допускается). Содержимое блока пишется в файл дословно, с переводом строки
# в конце. Архив воспроизводим: порядок файлов — по пути, время — фиксированное, без сжатия (ZIP_STORED), поэтому
# любой участник, собрав тот же текст этим же правилом, получит ту же контрольную сумму.
import hashlib, re, sys, zipfile

src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding='utf-8').read().split('\n')
files, i = {}, 0
head = re.compile(r'^#{1,6}\s*FILE:\s*(\S+)\s*$')
while i < len(lines):
    m = head.match(lines[i])
    if not m:
        i += 1; continue
    path = m.group(1)
    if path.startswith('/') or '..' in path.split('/'): sys.exit(f'ОТКАЗ: недопустимый путь {path}')
    if path in files: sys.exit(f'ОТКАЗ: файл {path} указан дважды')
    j = i + 1
    while j < len(lines) and lines[j].strip() == '': j += 1
    if j >= len(lines) or not lines[j].startswith('```'): sys.exit(f'ОТКАЗ: за заголовком {path} нет блока кода')
    fence = re.match(r'^(`{3,})', lines[j]).group(1)
    k = j + 1
    while k < len(lines) and not (lines[k].startswith(fence) and lines[k].strip() == fence): k += 1
    if k >= len(lines): sys.exit(f'ОТКАЗ: блок кода {path} не закрыт')
    files[path] = '\n'.join(lines[j + 1:k]) + '\n'
    i = k + 1
if not files: sys.exit('ОТКАЗ: в тексте нет ни одного файла')
with zipfile.ZipFile(dst, 'w', compression=zipfile.ZIP_STORED) as z:
    for path in sorted(files):
        zi = zipfile.ZipInfo(path, date_time=(2026, 1, 1, 0, 0, 0))
        zi.external_attr = 0o644 << 16
        z.writestr(zi, files[path].encode('utf-8'))
print(f'Источник: {src}; sha256 {hashlib.sha256(open(src, "rb").read()).hexdigest()}')
print(f'Файлов: {len(files)}')
for path in sorted(files):
    b = files[path].encode('utf-8')
    print(f'{hashlib.sha256(b).hexdigest()}  {path}  ({len(b)} байт)')
print(f'Архив: {dst}; sha256 {hashlib.sha256(open(dst, "rb").read()).hexdigest()}')
