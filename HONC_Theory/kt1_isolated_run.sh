#!/usr/bin/env bash
# СНЯТ С ПРИМЕНЕНИЯ 03.11.2026 (Интегратор: «ISOLATED RUN PROCEDURE v2 — CORRECTIONS REQUIRED»). Замена — kt1_sandbox_run.py (редакция 3).
echo "kt1_isolated_run.sh (редакция 2) снят с применения; используйте kt1_sandbox_run.py" >&2; exit 2
# Изолированный прогон чужого кода без изменений (Интегратор 03.11: А-5 и приёмочный прогон Д-3).
#   kt1_isolated_run.sh <метка> <архив.zip> <sha256 архива> <node|python|node-check> <входной файл> [аргументы…]
# node-check — только проверка синтаксиса всех .js архива (пробный прогон Д-3 без ядра); входной файл тогда — «-».
# Необязательно (только для Д-3): KERNEL_ZIP, KERNEL_SHA, KERNEL_DEST — замороженное ядро кладётся в src/$KERNEL_DEST.
# Без KERNEL_ZIP скрипт, упоминающий ядро, не запускается. Node — с моделью разрешений (чтение и запись только в папке
# прогона, без дочерних процессов); Python — через py_guard.py (то же правило через audit hook).
set -u
LABEL="$1"; ARCH="$(realpath "$2")"; WANT="$3"; LANGX="$4"; ENTRY="$5"; shift 5
[ -n "${KERNEL_ZIP:-}" ] && KERNEL_ZIP="$(realpath "$KERNEL_ZIP")"
HERE="$(cd "$(dirname "$0")" && pwd)"
TS="$(date -u +%Y%m%dT%H%M%SZ)"
RUN="$(dirname "$HERE")/runs/${LABEL}-${TS}"
mkdir -p "$RUN/src" "$RUN/out"
OUT="$RUN/out"
log() { echo "$*" | tee -a "$OUT/summary.txt"; }
log "Прогон: $LABEL ($TS UTC)"
GOT="$(sha256sum "$ARCH" | cut -c1-64)"
log "Архив: $(basename "$ARCH"); sha256 $GOT"
if [ "$GOT" != "$WANT" ]; then log "ОТКАЗ: контрольная сумма архива не совпадает с зафиксированной ($WANT)"; exit 10; fi
(cd "$RUN/src" && unzip -q "$ARCH") || { log "ОТКАЗ: архив не распакован"; exit 11; }
(cd "$RUN/src" && find . -type f | sort | xargs -d '\n' sha256sum) > "$OUT/manifest_files.txt"
grep -rnE "kt1|wp[0-4]_|HONC_Qf_KT1_Kernel|/tmp/|/home/|\.\./" "$RUN/src" > "$OUT/scan.txt" 2>/dev/null
if [ -n "${KERNEL_ZIP:-}" ]; then
  KGOT="$(sha256sum "$KERNEL_ZIP" | cut -c1-64)"
  log "Ядро: $(basename "$KERNEL_ZIP"); sha256 $KGOT"
  if [ "$KGOT" != "${KERNEL_SHA:-}" ]; then log "ОТКАЗ: контрольная сумма ядра не совпадает с замороженной (${KERNEL_SHA:-})"; exit 12; fi
  mkdir -p "$RUN/src/${KERNEL_DEST:-.}" && (cd "$RUN/src/${KERNEL_DEST:-.}" && unzip -q "$KERNEL_ZIP")
  export KT1_DIR="$RUN/src/${KERNEL_DEST:-.}/kt1"
else
  if [ -s "$OUT/scan.txt" ]; then log "ВНИМАНИЕ: в исходниках есть упоминания ядра или внешних путей — см. scan.txt; запуск без ядра, доступ вне папки прогона запрещён"; fi
fi
{ echo "date_utc: $TS"; echo "node: $(node --version)"; echo "python: $(python3 --version 2>&1)"; echo "uname: $(uname -srm)"; } > "$OUT/env.txt"
log "Среда: $(tr '\n' ';' < "$OUT/env.txt")"
# Чистое окружение: без прокси, NODE_OPTIONS, NODE_PATH, PYTHONPATH и прочих переменных сессии; HOME — папка прогона.
CLEAN=(env -i PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 HOME="$RUN" KT1_OUT="$OUT" KT1_RUN="$RUN")
[ -n "${KT1_DIR:-}" ] && CLEAN+=(KT1_DIR="$KT1_DIR")
cp "$HERE/py_guard.py" "$RUN/py_guard.py"
cd "$RUN/src"
T0=$(date +%s.%N)
if [ "$LANGX" = node-check ]; then
  # Только синтаксис: node --check по каждому .js архива (код не исполняется). ENTRY не используется.
  CODE=0; : > "$OUT/stdout.txt"; : > "$OUT/stderr.txt"
  while IFS= read -r f; do
    log "Команда: ${CLEAN[*]} node --check $f"
    if "${CLEAN[@]}" node --check "$f" >> "$OUT/stdout.txt" 2>> "$OUT/stderr.txt"; then echo "OK $f" >> "$OUT/stdout.txt"; else echo "FAIL $f" >> "$OUT/stdout.txt"; CODE=1; fi
  done < <(find . -name '*.js' -type f | sort)
else
  if [ "$LANGX" = node ]; then CMD=(node --permission --allow-fs-read="$RUN" --allow-fs-write="$RUN" "$ENTRY" "$@")
  else CMD=(python3 -I "$RUN/py_guard.py" "$ENTRY" "$@"); fi
  log "Команда: ${CLEAN[*]} ${CMD[*]}"
  "${CLEAN[@]}" "${CMD[@]}" > "$OUT/stdout.txt" 2> "$OUT/stderr.txt"; CODE=$?
fi
T1=$(date +%s.%N)
log "Код выхода $CODE; время $(echo "$T1 - $T0" | bc) с"
(cd "$RUN" && zip -qr "${RUN}-out.zip" out)
sha256sum "${RUN}-out.zip" | cut -c1-64 > "${RUN}-out.zip.sha256"
echo "Вывод: $(basename "$RUN")-out.zip; sha256 $(cat "${RUN}-out.zip.sha256")"
echo "$RUN"
