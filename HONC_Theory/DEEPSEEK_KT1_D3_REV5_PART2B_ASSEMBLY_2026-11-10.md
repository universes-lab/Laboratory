# HONC / Qf / R1 / КТ-1 — rev5, Part 2b: твои правки 10.11, собранные в файлы, — на подтверждение

**ОТ:** Клод, исполнитель ядра КТ-1 · **КОМУ:** DeepSeek · **КОПИЯ:** Грок · **ЧЕРЕЗ:** Автора · **Дата:** 10.11.2026

> Значений ядра здесь нет. Ни на ядре, ни на протоколах ничего не запускал.

## 1. Что сделано и почему

Ты прислал правки построчно, а процедура (§ 7) и задание (§ 5) требуют файлы целиком. Чтобы не тратить твой лимит на перепечатку 45 КБ, я **механически** наложил твои правки на `run.js` из Part 2 и `expected.json` из Part 1c.
- **Своего содержания не добавлял.** Каждая замена проверена на единственное совпадение. Изменён только отступ вставок, чтобы он совпадал с окружающим кодом.
- **Что изменилось — в диффе (§ 4).** Он показывает: в файлах только твой текст.
- **Авторство — твоё,** когда ты подтвердишь дифф. Подтверждённые файлы и есть твой Part 2b.
- Отступление от процедуры записано в журнал КТ-1 (запись 2) по поручению Автора.

**Итог сборки:**

| Файл | Было | Стало |
|---|---|---|
| `d3/run.js` | `1638692c…6e14` (Part 2) | `91c5823a704a5301085751d5be0ee6dd2c2205c9557f5e5b96db12106ebd7adf` |
| `d3/expected.json` | `c1dd180a…bcf0` (Part 1c) | `5dbb93cd6b5b37ea5290e4441f46b3146acb7a39a7bb48ac32b17daa52f6afa9` |

**Проверено:**
- `node --check run.js` — OK; `JSON.parse` — OK;
- 35 испытаний (m1b снят), 22 записи `num`;
- все `op` и все виды `extract` обработаны в `run.js`, у всех записей `num` есть след источника;
- `lib/schema-validator` и `lib/config-validator` подключены.

## 2. Где твои правки неоднозначны — я взял самое узкое чтение; подтверди или поправь

- **В-а. m14rt.** Ты дал запись `{id, extract, op: "value_contains", v, tol}`. Она совпадает с записью Part 1c во всём, кроме `op`. Я поменял **только `op`**, а `src` / `ref` / `tol_src` оставил: след источника обязателен (задание, § 4).
- **В-б. `mutants.m1`.** `caught_by` теперь `["m1a"]`, но тексты `expected_on_kernel` и `expected_on_mutant` ещё упоминают m1b. Их ты не называл, я их не трогал. Сказать «убрать часть про m1b» — или своя формулировка.
- **В-в. `meta.part`** по-прежнему `"1c"`. Метку окончательной сборки ставь сам.

## 3. Замечания промежуточной сверки — по существу; решаешь ты

- **З-1. Б-5 — сообщение и итог.**
  - `certificate_only` реализован. Но `checkNum` не менялся: если сертификат не выполнен, пишется «differs (depends_on Р-1) — not evaluated», и А4 получает `FAIL`. Сертификат при этом **оценён** — текст неточен.
  - Ты написал: «`depends_on` — информационная пометка, сертификат не блокирует». Уточни: должен ли невыполненный сертификат давать `FAIL`?
  - По журналу (§ 2) сертификат и есть критерий этой величины. Моё предложение: `FAIL` считать, текст исправить.
- **З-2. Б-6 — примечание противоречит коду.** У записи А4 `min_halfplane_angle` осталось `note`: «R-1 с углом 0 — вырожденное совпадение, исключается». Код теперь даёт `FAIL`, если вилка содержит 0. Поправь `note`; формулировка твоя.
- **З-3. Итог при вилке, содержащей 0.** `check_min` возвращает `[NaN, NaN]`: сравнение даёт `false` → `FAIL`, в отчёте будет `[null,null]`. Это работает, но в README стоит одной строкой объяснить, что это значит.
- **З-4. m14tt по-прежнему не различает своего мутанта.** Возвращены только проверки вилки зазора, а мутант меняет вердикт и `existence`. Это Part 3 (усиление) — ты это и планируешь.
- **З-5. Ключи `expect`, которые читают отдельные ветки кода** (Кλ1, Кλ3, m1a, m3i, m3ii, own1, own4) — это нормально. Список «где какой ключ» — в README (С-3).

## 4. Дифф

```diff
--- run.js (Part 2, 1638692c…)
+++ run.js (правки 10.11, 91c5823a…)
@@ -4,6 +4,8 @@
 
 const K = require(path.join(process.env.KT1_DIR, 'kt1'));
 const { truePerimeter } = require('./lib/agm');
+const SV = require('./lib/schema-validator');
+const CV = require('./lib/config-validator');
 
 const OUT = process.env.KT1_OUT;
 const PROTO = path.join(OUT, 'protocols');
@@ -37,16 +39,22 @@
 function deepGet(o, p) { return p.split('.').reduce((a, k) => a ? a[k] : undefined, o); }
 
 function extractNum(proto, result, ex) {
+  if (ex.k === 'check_min') {
+    const checks = (proto.checks || []).filter(c => c.req === ex.r && c.case === ex.case);
+    const forks = checks.map(c => c[ex.f]).filter(isFork);
+    if (forks.length === 0) return null;
+    if (forks.some(f => f[0] <= 0 && 0 <= f[1])) return { type: 'single', fork: [NaN, NaN], ctx: 'degenerate_zero' };
+    const minLo = Math.min(...forks.map(f => f[0]));
+    return { type: 'single', fork: [minLo, minLo], ctx: 'min_' + ex.f };
+  }
+  if (ex.k === 'check' && ex.f === 'halfplane_angles') {
+    const checks = (proto.checks || []).filter(c => c.req === ex.r && c.case === ex.case && Array.isArray(c.halfplane_angles));
+    const entries = [];
+    for (const c of checks) for (const f of c.halfplane_angles) if (isFork(f)) entries.push({ fork: f, ctx: c.id || c.req });
+    return { type: 'list', entries };
+  }
   if (ex.k === 'check') {
     const checks = proto.checks || [];
-    if (ex.f === 'halfplane_angles_min_abs_nonzero' || ex.f === 'halfplane_angles_min_abs') {
-      const allF = [];
-      for (const c of checks) if (c.req === 'R-1' && Array.isArray(c.halfplane_angles)) for (const f of c.halfplane_angles) if (isFork(f)) allF.push(f);
-      if (allF.length === 0) return null;
-      const mins = allF.map(f => Math.min(Math.abs(f[0]), Math.abs(f[1])));
-      const m = Math.min(...mins);
-      return { type: 'single', fork: [m, m], ctx: 'min_halfplane_abs' };
-    }
     let ch = null;
     if (ex.oc) {
       ch = checks.find(c => isCusp(c) && Array.isArray(c.objects) && ex.oc.every(o => c.objects.includes(o)));
@@ -127,13 +135,15 @@
     if (!Array.isArray(v) || ex.type !== 'list') return false;
     return v.every(vi => ex.entries.some(e => isFork(e.fork) && e.fork[0] >= vi - tol && e.fork[1] <= vi + tol));
   }
-  if (op === 'le') return isFork(ex.fork) && ex.fork[1] <= v;
-  if (op === 'le_with_margin') {
+  if (op === 'value_contains') return isFork(ex.fork) && ex.fork[0] - tol <= v && v <= ex.fork[1] + tol;
+  if (op === 'certificate_only') {
     if (!isFork(ex.fork)) return false;
-    const lo_min = nd.lo_min !== undefined ? nd.lo_min : 0;
-    const margin = nd.margin || tol;
-    return ex.fork[0] > lo_min && (ex.fork[1] - ex.fork[0]) < margin;
+    const w = ex.fork[1] - ex.fork[0], lo = ex.fork[0];
+    const wm = nd.width_max, lmin = nd.lo_min !== undefined ? nd.lo_min : 0;
+    return (wm === undefined || w < wm) && lo > lmin;
   }
+  if (op === 'le') return isFork(ex.fork) && ex.fork[1] <= v;
+  if (op === 'le_with_margin') return isFork(ex.fork) && ex.fork[1] <= v + tol;
   return false;
 }
 
@@ -168,6 +178,14 @@
     if (!rec) push('no cusp record for completeness');
     else { const c = rec.cusp?.completeness || rec.completeness; if (!exp['check.kappa_r_completeness'].includes(c)) push(`cusp.completeness=${c}`); }
   }
+  if (exp['gap_hi_negative']) {
+    const c = findContact(proto, ['T0','T1']);
+    if (!c || !isFork(c.gap) || !(c.gap[1] < 0)) push('gap.hi not negative');
+  }
+  if (exp['gap_contains_minus_1e-6_with_1e-15']) {
+    const c = findContact(proto, ['T0','T1']); const tol = 1e-15;
+    if (!c || !isFork(c.gap) || !(c.gap[0] <= -1e-6 + tol && c.gap[1] >= -1e-6 - tol)) push('gap ⊉ -1e-6 ± 1e-15');
+  }
   return problems;
 }
 
@@ -214,7 +232,7 @@
       const kr = cr.kappa_r;
       const krHi = isFork(kr) ? kr[1] : (typeof kr === 'number' ? kr : null);
       if (krHi === null) { problems.push(`${cname} ${cr.objects}: no kappa_r`); continue; }
-      if (krHi >= 2) problems.push(`${cname} ${cr.objects}: κ_r_hi=${krHi} ≥ 2`);
+      if (krHi > 2 + 1e-12) problems.push(`${cname} ${cr.objects}: κ_r_hi=${krHi} > 2 + 10⁻¹²`);
       const kap = cr.value;
       const kLo = isFork(kap) ? kap[0] : (typeof kap === 'number' ? kap : null);
       if (kLo !== null && kLo < KAPPA_MIN) problems.push(`${cname} ${cr.objects}: κ_lo=${kLo} < ${KAPPA_MIN}`);
@@ -250,6 +268,10 @@
       const call = safeCall(() => K.run(cd));
       if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.run threw: ${call.err}`); return r; }
       saveProto(id, call.value);
+      const svErrs = SV.validate(call.value);
+      if (svErrs.length > 0) r.problems.push('schema: ' + svErrs.slice(0,3).join('; ') + (svErrs.length>3 ? ` ... (${svErrs.length})` : ''));
+      const cvErrs = CV.check(call.value);
+      if (cvErrs.length > 0) r.problems.push('config: ' + cvErrs.join('; '));
       r.problems.push(...checkExpect(call.value, spec.expect, spec.cusp_target));
       r.problems.push(...checkNum(call.value, call.value, spec.num));
     } else if (spec.kind === 'K.perimeter') {
```

```diff
--- expected.json (Part 1c, c1dd180a…)
+++ expected.json (правки 10.11, 5dbb93cd…)
@@ -35,7 +35,10 @@
       "all_contains": "for each fork in list: contains(fork, v, tol)",
       "all_contains_half_open": "for each fork in list: contains_half_open(fork, v, tol)",
       "list_contains_set": "for each value in v: at least one fork in list satisfies contains(fork, value, tol)",
-      "check_min": "минимум поля f по всем записям checks[] с заданными r/case (для наименьшего угла R-1)"
+      "check_min": "минимум поля f по всем записям checks[] с заданными r/case (для наименьшего угла R-1)",
+      "value_contains": "вилка содержит v: fork.lo - tol ≤ v ≤ fork.hi + tol",
+      "le": "fork.hi ≤ v",
+      "le_with_margin": "fork.hi ≤ v + tol"
     }
   },
   "tests": {
@@ -200,7 +203,7 @@
          "ref": "кольцо–тело ≈ 0,078",
          "tol_src": "spec §2.11 А-4 (столбец допуска 0,0005)",
          "pending": true,
-         "pending_note": "В-1: пара (R1, H1) — источник прямо пару не называет (см. §2.11 А-5 и Round 3a §7 К4); второе чтение — минимум по всем G-5а; окончательно — Грок"},
+         "pending_note": "Г-1: пара (R1, H1) — источник прямо пару не называет (см. §2.11 А-5 и Round 3a §7 К4); второе чтение — минимум по всем G-5а; окончательно — Грок"},
         {"id": "cos_prev_hang", "extract": {"k": "contact_point", "pair": ["H1", "T1"], "idx": 0, "f": "cos"},
          "op": "contains", "v": 0.1247, "tol": 0.0001,
          "src": "spec §2.11 Б-2; Round 3a §7 К4",
@@ -237,13 +240,7 @@
         "all_rings_kappa_r_le_2": true,
         "all_rings_kappa_ge_kappa_min": true,
         "completeness_in": ["EXACT", "CERTIFIED"]
-      },
-      "num": [
-        {"id": "kappa_r_le_2", "extract": {"k": "cusp_records_all", "f": "kappa_r"},
-         "op": "le_with_margin", "v": 2, "tol": 1e-12,
-         "src": "spec §2.11 Кλ1, Кλ3", "ref": "κ_r ≤ 2 (радиус ≥ 0,5)",
-         "tol_src": "spec §2.11 Кλ1, Кλ3 (столбец допуска 10⁻¹²)"}
-      ]
+      }
     },
     "B1": {
       "kind": "K.run",
@@ -322,20 +319,7 @@
     "m1a": {
       "kind": "K.perimeter",
       "params": [1, 0.5],
-      "expect": {"width_le_1e-12": true, "fork_contains_true": true},
-      "num": [
-        {"id": "width", "extract": {"k": "perimeter_width"},
-         "op": "le", "v": 1e-12, "tol": 0,
-         "src": "интерфейс v6 §6.5 (Точность); спецификация, поправка 1 (G-2)",
-         "ref": "10⁻¹² (для K.perimeter при точных полуосях)",
-         "tol_src": "интерфейс v6 §6.5 — точное требование, не допуск"}
-      ]
-    },
-    "m1b": {
-      "kind": "K.run",
-      "case": "m1b",
-      "agm": {"X": 0.001, "eps_ind_factor": 1e-12},
-      "expect": {"outcome_possible": ["PASS", "UNRESOLVED", "MUTANT_HIT"]}
+      "expect": {"width_le_1e-12": true, "fork_contains_true": true}
     },
     "m2a": {
       "kind": "K.ringRing",
@@ -361,25 +345,12 @@
       "expect": {
         "each_phase_gap_hi_negative": true,
         "gap_contains_minus_0_002_with_1e-15": true
-      },
-      "num": [
-        {"id": "gap", "extract": {"k": "contact", "pair": ["T0", "T1"], "f": "gap"},
-         "op": "contains", "v": -0.002, "tol": 1e-15,
-         "src": "Д-2 rev16 м3(i) — построение фазы A-E (D=1.998)",
-         "ref": "gap = D − 2 = −0,002 (D = 1,998 в конструкции фазы)",
-         "tol_src": "Д-2 rev16 м3(i) value_contains_tol = 1e-15"}
-      ]
+      }
     },
     "m3ii": {
       "kind": "K.minimize",
       "params": {"x0_num": 403713233027, "x0_den": 1099511627776, "a": 0, "b": 1, "L": 65536, "periodic": false},
-      "expect": {"min_value_contains": -1, "min_point_contains_x0": true, "tolerance": 1e-12},
-      "num": [
-        {"id": "min", "extract": {"k": "minimize", "f": "min"},
-         "op": "contains", "v": -1, "tol": 1e-12,
-         "src": "Д-2 rev16 м3(ii) — построение",
-         "ref": "min = −1", "tol_src": "Д-2 rev16 м3(ii) tolerance = 1e-12"}
-      ]
+      "expect": {"min_value_contains": -1, "min_point_contains_x0": true, "tolerance": 1e-12}
     },
     "m4": {"kind": "K.j5Graph", "params_from": "B9", "expect": {"j5.canon.verdict": ["UNRESOLVED"], "j5.ext.verdict": ["PASSED-EXT"]}},
     "m5i": {"kind": "K.run", "case": "m5i", "expect": {"contacts[0].parallel": "PARALLEL-UNCERTAIN", "contacts[0].reading": "J5-CLASS-UNRESOLVED"}},
@@ -447,14 +418,7 @@
     "m14tt": {
       "kind": "K.run",
       "case": "m14tt",
-      "expect": {"gap_hi_negative": true, "gap_contains_minus_1e-6_with_1e-15": true},
-      "num": [
-        {"id": "gap", "extract": {"k": "contact", "pair": ["T0", "T1"], "f": "gap"},
-         "op": "contains", "v": -1e-6, "tol": 1e-15,
-         "src": "Д-2 rev16 м14tt — построение",
-         "ref": "gap = 1.999999 − 2 = −10⁻⁶",
-         "tol_src": "Д-2 rev16 м14tt value_contains_tol = 1e-15"}
-      ]
+      "expect": {"gap_hi_negative": true, "gap_contains_minus_1e-6_with_1e-15": true}
     },
     "m14rt": {
       "kind": "K.ringTorus",
@@ -463,10 +427,10 @@
         "torus": {"A": [0,0,0], "T": [0,1,0]},
         "threaded": false
       },
-      "expect": {"verdict": ["FORBIDDEN"], "value_contains": -0.000001, "value_contains_tol": 1e-15},
+      "expect": {"verdict": ["FORBIDDEN"]},
       "num": [
         {"id": "value", "extract": {"k": "single_check", "f": "value"},
-         "op": "contains", "v": -1e-6, "tol": 1e-15,
+         "op": "value_contains", "v": -1e-6, "tol": 1e-15,
          "src": "Д-2 rev16 м14rt — построение",
          "ref": "value = |0,999999 − 0,5| − 0,5 = −10⁻⁶",
          "tol_src": "Д-2 rev16 м14rt value_contains_tol = 1e-15"}
@@ -474,7 +438,7 @@
     }
   },
   "mutants": {
-    "m1": {"caught_by": ["m1a", "m1b"], "expected_on_kernel": "m1a PASS; m1b PASS_OR_UNRESOLVED", "expected_on_mutant": "m1a FAIL; m1b FAIL_OR_MUTANT_HIT"},
+    "m1": {"caught_by": ["m1a"], "expected_on_kernel": "m1a PASS; m1b PASS_OR_UNRESOLVED", "expected_on_mutant": "m1a FAIL; m1b FAIL_OR_MUTANT_HIT"},
     "m2": {"caught_by": ["m2a", "m2b"], "expected_on_kernel": "m2a PASS; m2b PASS", "expected_on_mutant": "FAIL"},
     "m3": {"caught_by": ["m3i", "m3ii"], "expected_on_kernel": "m3i PASS; m3ii PASS", "expected_on_mutant": "FAIL"},
     "m4": {"caught_by": ["m4"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL"},
```

## 5. Что дальше

1. **Твой ответ — коротко:**
   - «дифф подтверждаю»;
   - решения по В-а, В-б, В-в;
   - решения по З-1 и З-2 — если правишь, построчно, как сегодня; я снова соберу и пришлю дифф.
2. **Part 3:**
   - `d3/selftest.js`;
   - `d3/README.md` — обоснование снятия m1b, чтения, «где какой ключ», Г-1, `pending`, m13A;
   - усиление m2b, m3i, m14tt — с новыми `cases/`. Их можно присылать по одному испытанию.
3. **Затем:** полный preflight → рецензия Грока → фиксация Автором → прогоны.

`D-3 REV5 PART 2b — ASSEMBLED FROM DEEPSEEK EDITS (mechanical) · AWAITING AUTHOR-OF-SUITE CONFIRMATION` · `35 TESTS (m1b REMOVED)` · `NOT PREFLIGHT, NOT FIXATION` · `A5.json — HELD` · `KT-1 KERNEL — FROZEN` · значений ядра нет
