# Д-3 rev5 — рабочий текст набора после Part 2b (10.11.2026; НЕ сборка, НЕ фиксация)

Набор rev4 (зафиксирован, 5cc71cc7…071a) + d3/expected.json и d3/run.js в редакции Part 2b (автор — DeepSeek; дифф подтверждён им 10.11; сборка механическая, журнал КТ-1, запись 2). Остальные 32 файла — как в rev4. Part 3 сдаётся поверх этого текста файлами целиком. Значений ядра нет.

### FILE: d3/README.md
```
# d3 — исполняемый набор КТ-1 (R1 / D-3), rev4

Задание: `DEEPSEEK_KT1_D3_TASK_2026-11-05.md`.
Формат сдачи: процедура изолированного исполнения ред. 3.2, § 6–7.
Все файлы — LF (без CR).

## Что изменилось в rev4 (относительно rev3)

Четыре файла: `d3/run.js`, `d3/expected.json` (A-4 cusp_target), `d3/README.md`, `d3/selftest.js`. Остальные 30 — побайтно как в rev3.

Исправления по preflight rev3:

1. **Самопроверка 16/17.** В `testPerimeterFork` передавался boolean в `record(id, status, details)`; статус был `true`, а не `'PASS'`; в подсчёт PASS не попадал. Сама проверка верна; статус теперь явно `'PASS'`/`'FAIL'`.
2. **A-4 — выбор правильного кольцевого record.** В каспе несколько `kappa_margin` записей (по одной на каждую пару кольцо–тор в свой тор и в тор-хозяин). Эталон `κ_r = 1,366` относится к **`RH1` в `T2`** (кольцо навеса в торе-хозяине). Добавлено поле `cusp_target: {ring: "RH1", torus: "T2"}` в expected; в `run.js` — выборка по `objects`; при отсутствии strict match — fallback на «ring-only» с пометкой в problem при провале.
3. **Кλ3 — все кольца, не одно.** Composite теперь итерирует по всем `kappa_margin` записям каждого случая. Если хотя бы одно кольцо даёт `κ_r ≥ 2`, `κ < κ_min` или completeness вне `{EXACT, CERTIFIED}` — FAIL.
4. **README.** Убраны две неверные строки: `B1` (описывал `e.existence` в edges — в коде используется `contacts[]` и `pair`) и `m14tt` (описывал `quantity === 'gap'` — в коде `req: 'G-4'`). Актуальное описание — ниже.

## Что изменилось в rev3 (относительно rev2)

Исправления по preflight rev2 (сохранены в rev4):
- `K.j5Graph` возвращает `canon`/`ext` без обёртки `j5`; допускается fallback.
- B1 фильтрует IMPOSED-рёбра через `contacts[].existence`, а не `e.existence`; сравнивается `pair`.
- A4 и Кλ3 ищут касп по `req: 'G-5б–г'` / `quantity: 'kappa_margin'`.
- m14tt: gap из `contacts[0].gap` (fallback `checks[]` с `req: 'G-4'`).
- m14rt: `threaded: false` ⇒ проверка G-5а — только `verdict` и вилка `value`.
- m1b: независимый `perimeterFork(r0.s1, r0.s2)`.
- A4 `check.kappa_r_completeness`: строго `["EXACT"]`.

## Строки запуска

- С ядром (`d3-run`): `KT1_DIR=/sandbox/kernel/kt1 KT1_OUT=/sandbox/work node d3/run.js`
- Без ядра (`d3-selftest`): `KT1_OUT=/sandbox/work node d3/selftest.js`

## Что делает run.js

Читает `expected.json`. Для каждого испытания — вызов библиотечной точки §7, сохранение сырого протокола в `KT1_OUT/protocols/<id>.json`, сравнение с ожиданием, запись `KT1_OUT/d3_results.json`.

Если поле не найдено — `FAIL` с причиной и `Object.keys` / `objects` для диагностики.

**Актуальные проверки по ключевым ожиданиям:**

- **B1** (`j5.edges.all_imposed_sign_minus_1`): из `j5.edges[]` выбираются рёбра, чей `pair` встречается в `contacts[]` с `existence === 'IMPOSED'`; каждое такое ребро должно иметь `sign === -1`. Поля `existence` у рёбер нет (§6.3); IMPOSED — у касаний (§6.2).
- **A-4** (`check.kappa_r_in_range`, `check.kappa_r_completeness`): среди `checks[]` с `req === 'G-5б–г'` или `quantity === 'kappa_margin'` выбирается запись, в `objects` которой есть и целевое кольцо, и целевой тор (`cusp_target: {ring: "RH1", torus: "T2"}`). Fallback: запись с нужным кольцом (без тора) — с пометкой в problem при провале.
- **m14tt** (`gap_hi_negative`, `gap_contains_minus_1e-6_with_1e-15`): gap берётся из `contacts[0].gap`; если отсутствует — из `checks[]` с `req === 'G-4'` (поле `value`).
- **m1b** (`outcome_possible`): вилка `perimeterFork(r0.s1, r0.s2)` из `configuration.rings[]`; три исхода (`PASS` / `UNRESOLVED` / `MUTANT_HIT`) по `X = 1e-3`, `ε_ind = 1e-12 · P`.
- **m3ii** (`min_value_contains`, `min_point_contains_x0`): вилка минимума содержит −1; вилка точки минимума содержит `x0 = x0_num / x0_den` (403713233027 / 2⁴⁰).

## Что делает selftest.js

- `lib/k6-enumerator.js` — B9, B1, CLASS-UNRESOLVED, пустой граф.
- `lib/schema-validator.js` — PASSED+SAMPLED, кольцо без `widths`, `lo > hi`.
- `lib/config-validator.js` — правило §1.
- `lib/agm.js` — три известных периметра (2π, π, эллипс 1×0,5); `perimeterFork` на точных полуосях.
- `lib/compare.js::findCheck` — по `req` и по `quantity`.

Пишет `KT1_OUT/d3_selftest.json`, код выхода 0.

## Оговорки (к рецензии Грока)

- `sin/cos` в `lib/agm.js` — через `Math.*`, шаг N = 20000, ~1e-6; достаточно для X = 1e-3, не строгий сертификат.
- Единственность корня в m1b — practical, не Липшиц по ρ.
- B1 — `sign === -1` независимо от `points[].cos`.
- A-5 `INDEPENDENT COVERAGE = OPEN`: `UNRESOLVED` в A-5 по §4.2 допустим, но не засчитывается как успешная проверка проникновения.

## Статус

`D-3 rev4` — к упаковке.
`A-5 rev7` — submitted; rev8 — после D-3.
```

### FILE: d3/cases/A1.json
```
{"id":"A1","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[]}
```

### FILE: d3/cases/A2i.json
```
{"id":"A2i","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0}]}
```

### FILE: d3/cases/A2ii.json
```
{"id":"A2ii","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":null,"psi":0,"delta":0,"fix":{"kind":"contact","free":"rho","with":"T1","bracket":[29.5,30.5]}}]}
```

### FILE: d3/cases/A2iii.json
```
{"id":"A2iii","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":null,"psi":180,"delta":0,"fix":{"kind":"contact","free":"rho","with":"T3","bracket":[29.5,30.5]}}]}
```

### FILE: d3/cases/A2iv.json
```
{"id":"A2iv","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":31,"psi":0,"delta":0}]}
```

### FILE: d3/cases/A3.json
```
{"id":"A3","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":null,"psi":0,"delta":0,"fix":{"kind":"contact","free":"rho","with":"T1","bracket":[29.5,30.5]}}]}
```

### FILE: d3/cases/A4.json
```
{"id":"A4","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":null,"psi":54,"delta":10,"fix":{"kind":"contact","free":"rho","with":"T1","bracket":[56.0,58.5]}}]}
```

### FILE: d3/cases/A5.json
```
{"id":"A5","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":null,"psi":56,"delta":10,"fix":{"kind":"contact","free":"rho","with":"T1","bracket":[45.0,65.0]}}]}
```

### FILE: d3/cases/B1.json
```
{"id":"B1","same_as":"A3"}
```

### FILE: d3/cases/B10.json
```
{"id":"B10","tori":[{"name":"S1","A":[0,0,0],"T":[0,1,0]},{"name":"S2","A":[2,0,0],"T":[0,2,0]}],"rings":[{"name":"Q1","C":[1,0,0],"E1":[1,0,0],"E2":[0,1,0],"s1":1,"s2":1,"threads":["S1","S2"]}],"declare":[{"kind":"symmetry","pair":["S1","S2"],"contact":"IMPOSED","basis":"synthetic"}]}
```

### FILE: d3/cases/B2.json
```
{"id":"B2","same_as":"A4"}
```

### FILE: d3/cases/B3.json
```
{"id":"B3","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"alpha-lambda","alpha":52,"lambda":null,"delta":0,"fix":{"kind":"contact","free":"lambda","with":"T1","bracket":[20.0,35.0]}}]}
```

### FILE: d3/cases/B8.json
```
{"id":"B8","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":2,"side":1,"coords":"rho-psi","rho":30,"psi":0,"delta":0}]}
```

### FILE: d3/cases/KL1.json
```
{"id":"Kλ1","kind":"multi_theta","thetas":[0,30,60,75,85]}
```

### FILE: d3/cases/KL3.json
```
{"id":"Kλ3","kind":"collection","cases":["A1","A2i","A2ii","A2iii","A3","A4"]}
```

### FILE: d3/cases/m14tt.json
```
{"id":"m14tt","tori":[{"name":"T0","A":[0,0,0],"T":[0,1,0]},{"name":"T1","A":[1.999999,0,0],"T":[0,1,0]}]}
```

### FILE: d3/cases/m1b.json
```
{"id":"m1b","thread":{"n":2,"links":[{"theta":85,"phi":90,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[]}
```

### FILE: d3/cases/m3i-A.json
```
{"id":"m3i-A","tori":[{"name":"T0","A":[0,0,0],"T":[0,1,0]},{"name":"T1","A":[1.998,0,0],"T":[0,1,0]}]}
```

### FILE: d3/cases/m3i-B.json
```
{"id":"m3i-B","tori":[{"name":"T0","A":[0,0,0],"T":[0,1,0]},{"name":"T1","A":[1.91808,0,0.55944],"T":[0,1,0]}]}
```

### FILE: d3/cases/m3i-C.json
```
{"id":"m3i-C","tori":[{"name":"T0","A":[0,0,0],"T":[0,1,0]},{"name":"T1","A":[1.1988,0,1.5984],"T":[0,1,0]}]}
```

### FILE: d3/cases/m3i-D.json
```
{"id":"m3i-D","tori":[{"name":"T0","A":[0,0,0],"T":[0,1,0]},{"name":"T1","A":[1.5984,0,1.1988],"T":[0,1,0]}]}
```

### FILE: d3/cases/m3i-E.json
```
{"id":"m3i-E","tori":[{"name":"T0","A":[0,0,0],"T":[0,1,0]},{"name":"T1","A":[0.55944,0,1.91808],"T":[0,1,0]}]}
```

### FILE: d3/cases/m5i.json
```
{"id":"m5i","tori":[{"name":"S1","A":[0,0,0],"T":[0,1,0]},{"name":"S2","A":[2,0,0],"T":[0,2,0]}],"rings":[{"name":"Q1","C":[1,0,0],"E1":[1,0,0],"E2":[0,1,0],"s1":1,"s2":1,"threads":["S1","S2"]}],"declare":[{"kind":"symmetry","pair":["S1","S2"],"contact":"IMPOSED","basis":"synthetic"}]}
```

### FILE: d3/cases/m5ii.json
```
{"id":"m5ii","tori":[{"name":"S1","A":[0,0,0],"T":[0,1,0]},{"name":"S2","A":[2,0,0],"T":[0,1,0.1]}],"declare":[{"kind":"symmetry","pair":["S1","S2"],"contact":"IMPOSED","basis":"synthetic"}]}
```

### FILE: d3/cases/own3.json
```
{"id":"own3","tori":[{"name":"S1","A":[0,0,0],"T":[0,1,0]},{"name":"S2","A":[2,0,0],"T":{"sameAs":"S1"}}],"rings":[{"name":"Q1","C":[1,0,0],"E1":[1,0,0],"E2":[0,1,0],"s1":1,"s2":1,"threads":["S1","S2"]}],"declare":[{"kind":"symmetry","pair":["S1","S2"],"contact":"IMPOSED","basis":"synthetic"}]}
```

### FILE: d3/expected.json
```json
{
  "meta": {
    "rev": 5,
    "part": "2b",
    "status": "preparation",
    "source": "Д-1 rev16 + Д-2 rev16 fix + спецификация v0.3+поправка1 + Round 3a §7 + журнал эталонов ред.3 + интерфейс v6",
    "kappa_min": 0.05,
    "theta_min_deg": 1,
    "p2_note": "Р-2 — величина Round 3a §7 К4 ('кольцо–кольцо 0,0325'). В §2.10/§2.11 спецификации её нет; решение Интегратора 'исключить или дать определение' — не принято. В num не включена.",
    "open_questions_for_integrator": {
      "В-1": "применим ли допуск строки А-2 к тройке A-2 (источник допуска — в градусах, не в безразмерном значении тройки)",
      "В-2": "точные целые §2.10 (К1: κ_r = 1, 'запас 1'): правило округления (0.5) или иной критерий"
    },
    "field_names_confirmed_by_executor": {
      "d": "checks[] req='G-3', quantity='link_distance', value",
      "rho_fix": "contacts[].basis.root_deg (для пары навес — тор with)",
      "det_triple": "configuration.triples[] req='G-8', quantity='abs_det_T_n1_n2', value",
      "cusp_record_fields": "req='G-5б–г': kappa_r, value(=kappa_margin), outside_margin, cusp.completeness, outside.completeness, r0, objects",
      "ring_body_margin": "checks[] req='G-5а', quantity='margin', objects=[ring, torus]",
      "contacts_pair_order": "по построению (напр. ['T1','H1']); сравнивать как неупорядоченную",
      "halfplane_angles": "checks[] req='R-1', case='shared-cusp', halfplane_angles"
    },
    "field_debts_v7": [
      "checks[].quantity = 'link_distance' — не в §6.1",
      "configuration.triples[] — не в §6; поля: req, quantity, torus, rings, value, optional",
      "configuration.tori[].fix.root_deg — не в §6",
      "contacts[].type = null, reading = null для existence ∈ {SEPARATED, PENETRATION} (Интегратор 03.11)",
      "halfplane_angles — массив из двух вилок; интерфейс v6 не определяет, что они означают"
    ],
    "op_definitions": {
      "contains": "замкнутый интервал: fork.lo >= v−tol AND fork.hi <= v+tol (вилка ядра лежит внутри интервала допуска)",
      "contains_half_open": "полуоткрытый интервал: fork.lo >= v−tol AND fork.hi < v+tol (правило округления; правая граница не включена)",
      "certificate_only": "проверяются только критерии сертификата (width_max, lo_min); значение v не сравнивается (предмет Р-1)",
      "certificate_plus_contains_half_open": "сначала certificate_only, затем contains_half_open",
      "all_contains": "for each fork in list: contains(fork, v, tol)",
      "all_contains_half_open": "for each fork in list: contains_half_open(fork, v, tol)",
      "list_contains_set": "for each value in v: at least one fork in list satisfies contains(fork, value, tol)",
      "check_min": "минимум поля f по всем записям checks[] с заданными r/case (для наименьшего угла R-1)",
      "value_contains": "вилка содержит v: fork.lo - tol ≤ v ≤ fork.hi + tol",
      "le": "fork.hi ≤ v",
      "le_with_margin": "fork.hi ≤ v + tol"
    }
  },
  "tests": {
    "A1": {
      "kind": "K.run",
      "case": "A1",
      "expect": {
        "verdict.geometry": ["PASSED"],
        "j5.canon.verdict": ["PASSED"],
        "j5.ext.verdict": ["PASSED-EXT"],
        "contacts.all_imposed_side": true,
        "contacts.all_imposed_sign_minus_1": true,
        "contacts.count_imposed": 4,
        "rings.count": 5,
        "rings.length_all_close_2pi": true
      },
      "num": [
        {"id": "d", "extract": {"k": "check", "r": "G-3", "q": "link_distance", "f": "value"},
         "op": "contains", "v": 2, "tol": 1e-12,
         "src": "spec §2.11 А-1",
         "ref": "d = 2",
         "tol_src": "spec §2.11 А-1 (столбец допуска 10⁻¹²)"},
        {"id": "s1_all", "extract": {"k": "rings_all", "f": "s1"},
         "op": "all_contains", "v": 1, "tol": 1e-12,
         "src": "spec §2.11 А-1", "ref": "кольцо — окружность радиуса 1",
         "tol_src": "spec §2.11 А-1 (столбец допуска 10⁻¹²)"},
        {"id": "s2_all", "extract": {"k": "rings_all", "f": "s2"},
         "op": "all_contains", "v": 1, "tol": 1e-12,
         "src": "spec §2.11 А-1", "ref": "кольцо — окружность радиуса 1",
         "tol_src": "spec §2.11 А-1 (столбец допуска 10⁻¹²)"},
        {"id": "kappa_r", "extract": {"k": "cusp_records_all", "f": "kappa_r"},
         "op": "all_contains_half_open", "v": 1, "tol": 0.5,
         "src": "spec §2.10 К1",
         "ref": "κ_r = 1, запас 1",
         "tol_src": "journal ред.3 §2 — округление до целого разряда (консервативно)",
         "pending": true,
         "pending_note": "В-2: прямого допуска в источнике нет; слабый допуск; передано Интегратору"},
        {"id": "kappa_margin", "extract": {"k": "cusp_records_all", "f": "value"},
         "op": "all_contains_half_open", "v": 1, "tol": 0.5,
         "src": "spec §2.10 К1",
         "ref": "запас 1",
         "tol_src": "journal ред.3 §2 — округление до целого разряда (консервативно)",
         "pending": true,
         "pending_note": "В-2: то же, что kappa_r"}
      ]
    },
    "A2i": {
      "kind": "K.run",
      "case": "A2i",
      "expect": {
        "verdict.geometry": ["PASSED"],
        "j5.canon.verdict": ["PASSED"]
      },
      "num": [
        {"id": "halfplanes_set", "extract": {"k": "check", "r": "R-1", "case": "shared-cusp", "f": "halfplane_angles"},
         "op": "list_contains_set", "v": [-90, 0, 90], "tol": 1e-6,
         "src": "spec §2.11 А-2",
         "ref": "Полуплоскости −90° / 0° / +90°",
         "tol_src": "spec §2.11 А-2 (столбец допуска 10⁻⁶°)"},
        {"id": "det_triple", "extract": {"k": "triple", "r": "G-8", "q": "abs_det_T_n1_n2", "f": "value"},
         "op": "contains_half_open", "v": 1, "tol": 0.5,
         "src": "spec §2.11 А-2",
         "ref": "тройка = 1",
         "tol_src": "journal ред.3 §2 — округление до целого (консервативно)",
         "pending": true,
         "pending_note": "В-1: применим ли допуск строки А-2 (10⁻⁶°, в градусах) к тройке — передано Интегратору; пока правило округления до целого"}
      ]
    },
    "A2ii": {
      "kind": "K.run",
      "case": "A2ii",
      "expect": {
        "verdict.geometry": ["PASSED"],
        "j5.canon.verdict": ["FORBIDDEN"]
      },
      "num": [
        {"id": "rho_fix", "extract": {"k": "contact", "pair": ["H1", "T1"], "f": "basis.root_deg"},
         "op": "contains", "v": 30.0, "tol": 1e-6,
         "src": "spec §2.10 К2; §2.11 А-2",
         "ref": "первое касание при отклонении в плоскости — 30,0000° назад и вперёд",
         "tol_src": "spec §2.11 А-2 (столбец допуска 10⁻⁶°)"}
      ]
    },
    "A2iii": {
      "kind": "K.run",
      "case": "A2iii",
      "expect": {
        "verdict.geometry": ["PASSED"],
        "j5.canon.verdict": ["FORBIDDEN"]
      },
      "num": [
        {"id": "rho_fix", "extract": {"k": "contact", "pair": ["H1", "T3"], "f": "basis.root_deg"},
         "op": "contains", "v": 30.0, "tol": 1e-6,
         "src": "spec §2.10 К2; §2.11 А-2",
         "ref": "первое касание при отклонении в плоскости — 30,0000° назад и вперёд",
         "tol_src": "spec §2.11 А-2 (столбец допуска 10⁻⁶°)"}
      ]
    },
    "A2iv": {
      "kind": "K.run",
      "case": "A2iv",
      "expect": {
        "verdict.geometry": ["FORBIDDEN"]
      }
    },
    "A3": {
      "kind": "K.run",
      "case": "A3",
      "expect": {
        "verdict.geometry": ["PASSED"],
        "j5.canon.verdict": ["FORBIDDEN"]
      },
      "num": [
        {"id": "cos_all_canon_edges", "extract": {"k": "j5_edges_canon", "f": "cos_from_contacts"},
         "op": "all_contains_half_open", "v": -1.0, "tol": 0.0005,
         "src": "spec §2.11 Б-1", "ref": "cos = −1,000 на трёх рёбрах",
         "tol_src": "journal ред.3 §2 — округление до последнего разряда (три знака после запятой)"}
      ]
    },
    "A4": {
      "kind": "K.run",
      "case": "A4",
      "cusp_target": {"ring": "RH1", "torus": "T2"},
      "expect": {
        "verdict.geometry": ["PASSED"],
        "j5.canon.verdict": ["UNRESOLVED"],
        "j5.ext.verdict": ["PASSED-EXT"],
        "check.kappa_r_completeness": ["EXACT"]
      },
      "num": [
        {"id": "rho_fix", "extract": {"k": "contact", "pair": ["H1", "T1"], "f": "basis.root_deg"},
         "op": "contains", "v": 57.261, "tol": 0.001,
         "src": "spec §2.11 А-4; Round 3a §7 К4",
         "ref": "ρ = 57,261°",
         "tol_src": "spec §2.11 А-4 (столбец допуска 0,001°)"},
        {"id": "kappa_r", "extract": {"k": "check", "r": "G-5б–г", "oc": ["RH1", "T2"], "fb_oc": ["RH1"], "f": "kappa_r"},
         "op": "contains_half_open", "v": 1.366, "tol": 0.0005,
         "src": "spec §2.10 К4; §2.11 А-4",
         "ref": "κ_r = 1,366",
         "tol_src": "journal ред.3 §2 — округление до последнего разряда (три знака после запятой)"},
        {"id": "kappa_margin", "extract": {"k": "check", "r": "G-5б–г", "oc": ["RH1", "T2"], "fb_oc": ["RH1"], "f": "value"},
         "op": "contains_half_open", "v": 0.63, "tol": 0.005,
         "src": "spec §2.10 К4",
         "ref": "запас 0,63",
         "tol_src": "journal ред.3 §2 — округление до последнего записанного знака (два знака после запятой); §2.10 К4 говорит 'CERTIFIED', критерий ширины не приписан к этой строке"},
        {"id": "outside_margin", "extract": {"k": "check", "r": "G-5б–г", "oc": ["RH1", "T2"], "fb_oc": ["RH1"], "f": "outside_margin"},
         "op": "certificate_only", "width_max": 0.005, "lo_min": 0,
         "src": "spec §2.10 К4; §2.11 А-4",
         "ref": "запас вне каспа ≈ 0,006 (касп)",
         "tol_src": "journal ред.3 §2 — запас у каспа К4: критерий сертификата (ширина < 0,005, нижняя граница > 0); допуска по значению в источнике нет",
         "depends_on": "Р-1",
         "pending": true,
         "pending_note": "Р-1 не решён Интегратором; сравнение по значению 0,006 не делается; проверяется только критерий сертификата"},
        {"id": "min_halfplane_angle", "extract": {"k": "check_min", "r": "R-1", "case": "shared-cusp", "f": "value"},
         "op": "contains_half_open", "v": 47.6, "tol": 0.05,
         "src": "spec §2.10 К4", "ref": "R-1 (наименьший угол 47,6°)",
         "tol_src": "journal ред.3 §2 — округление до последнего записанного знака (один знак после запятой)",
         "note": "минимум по всем R-1 в case='shared-cusp'; R-1 с вилкой, содержащей 0, — вырожденное совпадение, даёт FAIL (см. README)"},
        {"id": "ring_body_margin_R1_H1", "extract": {"k": "check", "r": "G-5а", "objs": ["R1", "H1"], "f": "value"},
         "op": "contains", "v": 0.078, "tol": 0.0005,
         "src": "spec §2.11 А-4",
         "ref": "кольцо–тело ≈ 0,078",
         "tol_src": "spec §2.11 А-4 (столбец допуска 0,0005)",
         "pending": true,
         "pending_note": "Г-1: пара (R1, H1) — источник прямо пару не называет (см. §2.11 А-5 и Round 3a §7 К4); второе чтение — минимум по всем G-5а; окончательно — Грок"},
        {"id": "cos_prev_hang", "extract": {"k": "contact_point", "pair": ["H1", "T1"], "idx": 0, "f": "cos"},
         "op": "contains", "v": 0.1247, "tol": 0.0001,
         "src": "spec §2.11 Б-2; Round 3a §7 К4",
         "ref": "cos = +0,1247 на ребре предыдущий–навес",
         "tol_src": "journal ред.3 §2 — карточка Б-2 (допуск 10⁻⁴ задан)"},
        {"id": "cos_hang_host", "extract": {"k": "contact_point", "pair": ["H1", "T2"], "idx": 0, "f": "cos"},
         "op": "contains_half_open", "v": -1.0, "tol": 0.0005,
         "src": "Round 3a §7 К4", "ref": "cos хозяин–навес = −1,000",
         "tol_src": "journal ред.3 §2 — округление до последнего разряда (три знака)"}
      ]
    },
    "A5": {
      "kind": "K.run",
      "case": "A5",
      "expect": {
        "verdict.geometry": ["FORBIDDEN", "UNRESOLVED"],
        "_note": "A-5 INDEPENDENT COVERAGE = OPEN; UNRESOLVED допустим по §4.2, но не засчитывается как успешная проверка проникновения. Числовой эталон −0,063 не добавлен до A-5 rev8."
      }
    },
    "Kλ1": {
      "kind": "K.run",
      "case": "Kλ1",
      "expect": {
        "d_formula": "1 + Math.cos(theta_rad)",
        "theta_list_deg": [0, 30, 60, 75, 85],
        "tolerance": 1e-12
      },
      "num_note": "d(θ) вычисляется формулой в run.js по θ; эталон — формула + допуск, без предвычисленной таблицы. Источник: spec §2.11 Кλ1 + карточка Д-1 rev16 Kλ1."
    },
    "Kλ3": {
      "kind": "K.run",
      "cases": ["A1", "A2i", "A2ii", "A2iii", "A3", "A4"],
      "expect": {
        "all_rings_kappa_r_le_2": true,
        "all_rings_kappa_ge_kappa_min": true,
        "completeness_in": ["EXACT", "CERTIFIED"]
      }
    },
    "B1": {
      "kind": "K.run",
      "case": "B1",
      "expect": {
        "j5.canon.verdict": ["FORBIDDEN"],
        "j5.edges.all_imposed_sign_minus_1": true
      },
      "num": [
        {"id": "cos_all_canon_edges", "extract": {"k": "j5_edges_canon", "f": "cos_from_contacts"},
         "op": "all_contains_half_open", "v": -1.0, "tol": 0.0005,
         "src": "spec §2.11 Б-1", "ref": "cos = −1,000 на трёх рёбрах",
         "tol_src": "journal ред.3 §2 — округление до последнего разряда (три знака)"}
      ]
    },
    "B2": {
      "kind": "K.run",
      "case": "B2",
      "expect": {
        "j5.canon.verdict": ["UNRESOLVED"],
        "j5.ext.verdict": ["PASSED-EXT"]
      },
      "num": [
        {"id": "cos_prev_hang", "extract": {"k": "contact_point", "pair": ["H1", "T1"], "idx": 0, "f": "cos"},
         "op": "contains", "v": 0.1247, "tol": 0.0001,
         "src": "spec §2.11 Б-2; Round 3a §7 К4",
         "ref": "cos = +0,1247 на ребре предыдущий–навес",
         "tol_src": "journal ред.3 §2 — карточка Б-2 (допуск 10⁻⁴ задан)"}
      ]
    },
    "B3": {
      "kind": "K.run",
      "case": "B3",
      "expect": {
        "j5.canon.verdict": ["UNRESOLVED"],
        "j5.ext.verdict": ["PASSED-EXT", "UNRESOLVED"]
      },
      "num": [
        {"id": "cos_prev_hang", "extract": {"k": "contact_point", "pair": ["H1", "T1"], "idx": 0, "f": "cos"},
         "op": "contains_half_open", "v": 0.051, "tol": 0.0005,
         "src": "spec §2.11 Б-3", "ref": "cos = +0,051",
         "tol_src": "journal ред.3 §2 — округление до последнего записанного знака (три знака); в журнале — 'порог протокола', не обычный допуск; используется как полуоткрытый интервал для сравнения значения",
         "note": "семантика также: при ε < 0,051 знак определён, иначе J5-DEGENERATE"}
      ]
    },
    "B5": {
      "kind": "K.j5Reading",
      "params": {"parallel": "NON-PARALLEL", "type": "UNDETERMINED", "cos": [[-0.8, -0.6], [0.6, 0.8]]},
      "expect": {"reading": "J5-EXT", "sign": null, "epsilon_range": [0.099999999, 0.100000001], "contact_class": "UNRESOLVED CONTACT"}
    },
    "B8": {"kind": "K.run", "case": "B8", "expect": {"verdict.geometry": ["UNRESOLVED"]}},
    "B9": {
      "kind": "K.j5Graph",
      "params": {
        "vertices": ["T1", "T2", "T3", "T4"],
        "edges": [
          {"a": "T1", "b": "T2", "cls": "LINK", "existence": "IMPOSED", "reading": "J5-CANON", "sign": 1},
          {"a": "T2", "b": "T3", "cls": "LINK", "existence": "IMPOSED", "reading": "J5-CANON", "sign": 1},
          {"a": "T3", "b": "T1", "cls": "LINK", "existence": "IMPOSED", "reading": "J5-CANON", "sign": 1},
          {"a": "T3", "b": "T4", "cls": "CONTACT-ONLY", "existence": "IMPOSED", "reading": "J5-EXT", "sign": 1}
        ]
      },
      "expect": {"j5.canon.verdict": ["UNRESOLVED"], "j5.ext.verdict": ["PASSED-EXT"]}
    },
    "B10": {
      "kind": "K.run",
      "case": "B10",
      "expect": {
        "contacts[0].existence": "IMPOSED",
        "contacts[0].parallel": "PARALLEL-UNCERTAIN",
        "contacts[0].reading": "J5-CLASS-UNRESOLVED",
        "j5.ext.verdict": ["PASSED-EXT"],
        "j5.canon.verdict": ["UNRESOLVED"]
      }
    },
    "m1a": {
      "kind": "K.perimeter",
      "params": [1, 0.5],
      "expect": {"width_le_1e-12": true, "fork_contains_true": true}
    },
    "m2a": {
      "kind": "K.ringRing",
      "params": {
        "r1": {"C": [0,0,-1], "E1": [0,0,1], "E2": [0,1,0], "s1": 1, "s2": 1},
        "r2": {"C": [0,0,-0.01], "E1": [0,0,1], "E2": [0,1,0], "s1": 0.01, "s2": 1.5},
        "sharedCusp": {"A": [0,0,0], "T": [0,1,0]}
      },
      "expect": {"contact_class": "UNRESOLVED CONTACT"}
    },
    "m2b": {
      "kind": "K.ringTorus",
      "params": {
        "ring": {"C": [0,0,-0.2], "E1": [0,0,1], "E2": [0,1,0], "s1": 0.2, "s2": 0.1},
        "torus": {"A": [0,0,0], "T": [0,1,0]},
        "threaded": true
      },
      "expect": {"verdict": ["FORBIDDEN"]}
    },
    "m3i": {
      "kind": "K.run",
      "cases": ["m3i-A", "m3i-B", "m3i-C", "m3i-D", "m3i-E"],
      "expect": {
        "each_phase_gap_hi_negative": true,
        "gap_contains_minus_0_002_with_1e-15": true
      }
    },
    "m3ii": {
      "kind": "K.minimize",
      "params": {"x0_num": 403713233027, "x0_den": 1099511627776, "a": 0, "b": 1, "L": 65536, "periodic": false},
      "expect": {"min_value_contains": -1, "min_point_contains_x0": true, "tolerance": 1e-12}
    },
    "m4": {"kind": "K.j5Graph", "params_from": "B9", "expect": {"j5.canon.verdict": ["UNRESOLVED"], "j5.ext.verdict": ["PASSED-EXT"]}},
    "m5i": {"kind": "K.run", "case": "m5i", "expect": {"contacts[0].parallel": "PARALLEL-UNCERTAIN", "contacts[0].reading": "J5-CLASS-UNRESOLVED"}},
    "m5ii": {"kind": "K.run", "case": "m5ii", "expect": {"contacts[0].parallel": "NON-PARALLEL", "contacts[0].reading": "J5-EXT"}},
    "m8": {"kind": "K.run", "case": "B8", "expect": {"verdict.geometry": ["UNRESOLVED"]}},
    "m12": {"kind": "K.run", "case": "A3", "expect": {"j5.canon.verdict": ["FORBIDDEN"]}},
    "own1": {
      "kind": "K.validate",
      "params": {
        "constructed": {
          "checks": [{"id":"synthetic","req":"G-5a","objects":["Q0","T0"],"quantity":"gap","value":[-0.001,0.001],"completeness":"SAMPLED","verdict":"PASSED","reason":null,"where":null,"level":"L2","layer":"CARRIER","status":null}],
          "configuration": {"rings":[]}, "verdict": {"geometry": "PASSED"}
        }
      },
      "expect": {"violations_non_empty": true}
    },
    "own2": {
      "kind": "K.ringTorus",
      "params": {
        "ring": {"C": [0, 0.3, 0], "E1": [1,0,0], "E2": [0,0,1], "s1": 0.5, "s2": 0.5},
        "torus": {"A": [0,0,0], "T": [0,1,0]},
        "threaded": false
      },
      "expect": {"verdict": ["FORBIDDEN"]}
    },
    "own3": {
      "kind": "K.run",
      "case": "own3",
      "expect": {
        "contacts[0].parallel": "PARALLEL-ESTABLISHED",
        "contacts[0].type": "UNDETERMINED",
        "contacts[0].reading": "J5-CLASS-UNRESOLVED"
      }
    },
    "own4": {
      "kind": "K.validate",
      "params": {
        "constructed": {
          "checks": [{"id":"own4-check","req":"G-4","objects":["Q0"],"quantity":"gap","value":[-0.001,0.001],"completeness":"CERTIFIED","verdict":"FORBIDDEN","reason":null,"where":null,"level":"L2","layer":"CARRIER","status":null}],
          "configuration": {"rings": []}, "verdict": {"geometry": "FORBIDDEN"}
        }
      },
      "expect": {"violations_non_empty": true},
      "note": "rev5: redirected from MY_CONFIG_VALIDATOR to K.validate with FORBIDDEN without reason (schema-validator must reject per §6.1). Rule §1 coverage remains in selftest."
    },
    "m13A": {
      "kind": "K.ringTorus",
      "params": {
        "ring": {"C": [-2, 0, 0], "E1": [1,0,0], "E2": [0,1,0], "s1": 2, "s2": 1},
        "torus": {"A": [0,0,0], "T": [0,1,0]},
        "threaded": true
      },
      "expect": {"verdict": ["UNRESOLVED"]},
      "note": "маскируется κ_min = 0.05: при κ_r = 2 запас κ = 0 < κ_min, итог UNRESOLVED по ветви κ < κ_min. Оставляю; оговорка в README (Part 3)."
    },
    "m13B": {
      "kind": "K.ringTorus",
      "params": {
        "ring": {"C": [-2.0000001, 0, 0], "E1": [1,0,0], "E2": [0,1,0], "s1": 2.0000001, "s2": 1},
        "torus": {"A": [0,0,0], "T": [0,1,0]},
        "threaded": true
      },
      "expect": {"verdict": ["FORBIDDEN"]}
    },
    "m14tt": {
      "kind": "K.run",
      "case": "m14tt",
      "expect": {"gap_hi_negative": true, "gap_contains_minus_1e-6_with_1e-15": true}
    },
    "m14rt": {
      "kind": "K.ringTorus",
      "params": {
        "ring": {"C": [0,0,0], "E1": [1,0,0], "E2": [0,0,1], "s1": 0.999999, "s2": 0.999999},
        "torus": {"A": [0,0,0], "T": [0,1,0]},
        "threaded": false
      },
      "expect": {"verdict": ["FORBIDDEN"]},
      "num": [
        {"id": "value", "extract": {"k": "single_check", "f": "value"},
         "op": "value_contains", "v": -1e-6, "tol": 1e-15,
         "src": "Д-2 rev16 м14rt — построение",
         "ref": "value = |0,999999 − 0,5| − 0,5 = −10⁻⁶",
         "tol_src": "Д-2 rev16 м14rt value_contains_tol = 1e-15"}
      ]
    }
  },
  "mutants": {
    "m1": {"caught_by": ["m1a"], "expected_on_kernel": "m1a PASS", "expected_on_mutant": "m1a FAIL"},
    "m2": {"caught_by": ["m2a", "m2b"], "expected_on_kernel": "m2a PASS; m2b PASS", "expected_on_mutant": "FAIL"},
    "m3": {"caught_by": ["m3i", "m3ii"], "expected_on_kernel": "m3i PASS; m3ii PASS", "expected_on_mutant": "FAIL"},
    "m4": {"caught_by": ["m4"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL"},
    "m5": {"caught_by": ["m5i", "m5ii"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL"},
    "m8": {"caught_by": ["m8", "B8"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL"},
    "m12": {"caught_by": ["m12"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL"},
    "m13": {"caught_by": ["m13A", "m13B"], "expected_on_kernel": "m13A PASS; m13B PASS", "expected_on_mutant": "FAIL"},
    "m14": {"caught_by": ["m14tt", "m14rt"], "expected_on_kernel": "m14tt PASS; m14rt PASS", "expected_on_mutant": "FAIL"}
  }
}
```

### FILE: d3/lib/agm.js
```
'use strict';

// Независимый периметр эллипса — численное интегрирование полного эллиптического
// интеграла второго рода. В run.js/selftest.js — только этот метод. Не использует K.*.

function truePerimeter(a, b) {
  if (a <= 0 || b <= 0) return NaN;
  const N = 20000;
  const h = 2 * Math.PI / N;
  let s = 0;
  for (let i = 0; i < N; i++) {
    const t = i * h;
    s += Math.sqrt(a * a * Math.sin(t) * Math.sin(t) + b * b * Math.cos(t) * Math.cos(t));
  }
  return s * h;
}

// Вилка: периметр монотонно растёт по каждой полуоси; на вилках [s1_lo, s1_hi] × [s2_lo, s2_hi]
//   P_lo = truePerimeter(s1_lo, s2_lo)
//   P_hi = truePerimeter(s1_hi, s2_hi)
function perimeterFork(s1Fork, s2Fork) {
  const pLo = truePerimeter(s1Fork[0], s2Fork[0]);
  const pHi = truePerimeter(s1Fork[1], s2Fork[1]);
  return [pLo, pHi];
}

module.exports = { truePerimeter, perimeterFork };
```

### FILE: d3/lib/compare.js
```
'use strict';

function numInFork(x, fork) {
  return Array.isArray(fork) && typeof x === 'number' && x >= fork[0] && x <= fork[1];
}

function checkContains(actual, expected_num, eps) {
  eps = eps || 1e-15;
  if (!Array.isArray(actual)) return false;
  return actual[0] - eps <= expected_num && expected_num <= actual[1] + eps;
}

function get(obj, path) {
  const parts = path.split('.');
  let cur = obj;
  for (const p of parts) {
    if (cur === null || cur === undefined) return undefined;
    if (Array.isArray(cur) && /^\d+$/.test(p)) cur = cur[parseInt(p, 10)];
    else cur = cur[p];
  }
  return cur;
}

// Поиск проверки по любому из признаков id / req / quantity.
function findCheck(checks, want) {
  if (!Array.isArray(checks)) return null;
  for (const c of checks) {
    let ok = true;
    for (const k of Object.keys(want)) {
      if (c[k] !== want[k]) { ok = false; break; }
    }
    if (ok) return c;
  }
  return null;
}

module.exports = { numInFork, checkContains, get, findCheck };
```

### FILE: d3/lib/config-validator.js
```
'use strict';

function derive(checks) {
  if (!Array.isArray(checks) || checks.length === 0) return 'UNRESOLVED';
  let anyForbidden = false, allPassed = true;
  for (const c of checks) {
    if (c.verdict === 'FORBIDDEN') anyForbidden = true;
    if (c.verdict !== 'PASSED') allPassed = false;
  }
  if (anyForbidden) return 'FORBIDDEN';
  if (allPassed) return 'PASSED';
  return 'UNRESOLVED';
}

function check(protocol) {
  if (!protocol || !protocol.checks || !protocol.verdict) return ['no checks/verdict'];
  const derived = derive(protocol.checks);
  const claimed = protocol.verdict.geometry;
  if (derived !== claimed) return ['derived ' + derived + ' != claimed ' + claimed];
  return [];
}

module.exports = { derive, check };
```

### FILE: d3/lib/k6-enumerator.js
```
'use strict';

const N_MAX = 6;
const N_MAX_CANDIDATES = 8;

function enumerateCycles(vertices, edges) {
  const adj = new Map();
  for (const v of vertices) adj.set(v, []);
  for (const e of edges) { adj.get(e.a).push(e); adj.get(e.b).push(e); }
  const cycles = [];
  const seen = new Set();
  for (const start of vertices) {
    const path = [start];
    const inPath = new Set([start]);
    function dfs(v) {
      for (const e of adj.get(v)) {
        const w = e.a === v ? e.b : e.a;
        if (w === start && path.length >= 3) {
          const key = canonicalKey(path);
          if (!seen.has(key)) {
            seen.add(key);
            const edgesInCycle = [];
            for (let i = 0; i < path.length; i++) {
              const u = path[i], x = path[(i + 1) % path.length];
              edgesInCycle.push(edges.find(ee => (ee.a === u && ee.b === x) || (ee.a === x && ee.b === u)));
            }
            cycles.push({ vertices: path.slice(), edges: edgesInCycle });
          }
        } else if (path.length < N_MAX && !inPath.has(w)) {
          path.push(w); inPath.add(w); dfs(w); path.pop(); inPath.delete(w);
        }
      }
    }
    dfs(start);
  }
  return cycles;
}

function canonicalKey(path) {
  const minIdx = path.indexOf(Math.min(...path));
  const rotated = path.slice(minIdx).concat(path.slice(0, minIdx));
  const reversed = [rotated[0]].concat(rotated.slice(1).reverse());
  return rotated.join(',') < reversed.join(',') ? rotated.join(',') : reversed.join(',');
}

function judgeCanon(edges, cycles) {
  const bad = cycles.filter(c =>
    c.edges.every(e => e.reading === 'J5-CANON') &&
    c.edges.reduce((p, e) => p * (e.sign === null ? 0 : e.sign), 1) < 0
  );
  if (bad.length > 0) return { verdict: 'FORBIDDEN', reason: 'inconsistent CANON cycle' };
  const nonCanon = edges.filter(e => e.reading !== 'J5-CANON');
  if (nonCanon.length > 0) return { verdict: 'UNRESOLVED', reason: 'non-CANON edges present' };
  return { verdict: 'PASSED' };
}

function judgeExt(edges, cycles) {
  const signed = edges.filter(e => e.reading !== 'J5-DEGENERATE' && e.sign !== null);
  const unsigned = edges.filter(e => e.reading === 'J5-DEGENERATE' || e.sign === null);
  const bad = cycles.filter(c =>
    c.edges.every(e => signed.indexOf(e) >= 0) &&
    c.edges.reduce((p, e) => p * e.sign, 1) < 0
  );
  if (bad.length > 0) return { verdict: 'FORBIDDEN-EXT', reason: 'inconsistent EXT cycle' };
  if (unsigned.length > 0) return { verdict: 'UNRESOLVED', reason: 'unsigned edges present' };
  return { verdict: 'PASSED-EXT', label: '[Г, мост]' };
}

function enumerateBranches(graph) {
  const cand = graph.edges.filter(e => e.existence === 'CANDIDATE');
  if (cand.length > N_MAX_CANDIDATES) return { tooMany: true, branches: [] };
  if (cand.length === 0) return { tooMany: false, branches: [graph] };
  const branches = [];
  for (let mask = 0; mask < (1 << cand.length); mask++) {
    const edges = graph.edges.map(e => {
      if (e.existence !== 'CANDIDATE') return e;
      const ci = cand.indexOf(e);
      if ((mask >> ci) & 1) return { ...e, existence: 'IMPOSED' };
      return { ...e, existence: 'EXCLUDED' };
    }).filter(e => e.existence !== 'EXCLUDED');
    branches.push({ ...graph, edges });
  }
  return { tooMany: false, branches };
}

function evaluate(graph) {
  const { tooMany, branches } = enumerateBranches(graph);
  if (tooMany) {
    return { j5: {
      canon: { verdict: 'UNRESOLVED', reason: 'n_max_candidates exceeded' },
      ext: { verdict: 'UNRESOLVED', reason: 'n_max_candidates exceeded' }
    } };
  }
  const results = branches.map(b => {
    const cycles = enumerateCycles(b.vertices, b.edges);
    return { canon: judgeCanon(b.edges, cycles), ext: judgeExt(b.edges, cycles) };
  });
  const canonAgree = results.every(r => r.canon.verdict === results[0].canon.verdict);
  const extAgree = results.every(r => r.ext.verdict === results[0].ext.verdict);
  const out = { j5: {} };
  out.j5.canon = canonAgree ? results[0].canon : { verdict: 'UNRESOLVED', reason: 'branch disagreement' };
  out.j5.ext = extAgree ? results[0].ext : { verdict: 'UNRESOLVED', reason: 'branch disagreement' };
  if (branches.length > 1) out.j5.branches = results;
  return out;
}

module.exports = { evaluate, enumerateCycles };
```

### FILE: d3/lib/schema-validator.js
```
'use strict';

function validateFork(f) {
  if (!Array.isArray(f) || f.length !== 2) return 'fork must be [lo, hi]';
  if (typeof f[0] !== 'number' || typeof f[1] !== 'number') return 'fork must be two numbers';
  if (!isFinite(f[0]) || !isFinite(f[1])) return 'fork must be finite';
  if (f[0] > f[1]) return 'fork lo > hi: [' + f[0] + ', ' + f[1] + ']';
  return null;
}

function checkCheck(rec, errs, prefix) {
  const need = ['id', 'req', 'objects', 'quantity', 'value', 'completeness', 'verdict', 'level', 'layer'];
  for (const f of need) if (!(f in rec)) errs.push(prefix + ': missing field ' + f);
  if ('value' in rec) {
    const e = validateFork(rec.value);
    if (e) errs.push(prefix + ': value ' + e);
  }
  if (!['EXACT','CERTIFIED','SAMPLED','UNRESOLVED'].includes(rec.completeness)) {
    errs.push(prefix + ': unknown completeness ' + rec.completeness);
  }
  if (rec.verdict === 'PASSED') {
    if (rec.completeness !== 'EXACT' && rec.completeness !== 'CERTIFIED') {
      errs.push(prefix + ': PASSED with completeness ' + rec.completeness + ' forbidden');
    }
  } else if (rec.verdict === 'FORBIDDEN' || rec.verdict === 'UNRESOLVED') {
    if (typeof rec.reason !== 'string' || rec.reason.length === 0) {
      errs.push(prefix + ': ' + rec.verdict + ' without reason');
    }
  } else {
    errs.push(prefix + ': unknown verdict ' + rec.verdict);
  }
  if ('where' in rec) {
    if (rec.where !== null && typeof rec.where !== 'object') errs.push(prefix + ': where must be object or null');
  }
  if (!['L1','L2','L3'].includes(rec.level)) errs.push(prefix + ': level ' + rec.level + ' not allowed in KT-1');
  if (rec.layer !== 'CARRIER') errs.push(prefix + ': layer must be CARRIER in KT-1');
}

function checkRing(rec, errs, prefix) {
  const need = ['name', 'source', 'C', 'E1', 'E2', 's1', 's2', 'widths', 'width_max'];
  for (const f of need) if (!(f in rec)) errs.push(prefix + ': missing field ' + f);
  for (const f of ['s1', 's2']) {
    if (f in rec) { const e = validateFork(rec[f]); if (e) errs.push(prefix + '.' + f + ': ' + e); }
  }
  for (const f of ['C', 'E1', 'E2']) {
    if (f in rec && Array.isArray(rec[f])) {
      for (let i = 0; i < rec[f].length; i++) {
        const e = validateFork(rec[f][i]);
        if (e) errs.push(prefix + '.' + f + '[' + i + ']: ' + e);
      }
    }
  }
  if ('widths' in rec && (typeof rec.widths !== 'object' || rec.widths === null)) {
    errs.push(prefix + ': widths must be object');
  }
  if ('width_max' in rec && typeof rec.width_max !== 'number') {
    errs.push(prefix + ': width_max must be number');
  }
}

function validate(protocol) {
  const errs = [];
  if (!protocol || typeof protocol !== 'object') return ['protocol is not an object'];
  if (!protocol.configuration) errs.push('missing configuration');
  if (!protocol.checks) errs.push('missing checks[]');
  if (!protocol.verdict) errs.push('missing verdict');
  if (protocol.checks) {
    for (let i = 0; i < protocol.checks.length; i++) checkCheck(protocol.checks[i], errs, 'checks[' + i + ']');
  }
  if (protocol.configuration && protocol.configuration.rings) {
    for (let i = 0; i < protocol.configuration.rings.length; i++) checkRing(protocol.configuration.rings[i], errs, 'rings[' + i + ']');
  }
  return errs;
}

module.exports = { validate };
```

### FILE: d3/run.js
```js
'use strict';
const fs = require('fs');
const path = require('path');

const K = require(path.join(process.env.KT1_DIR, 'kt1'));
const { truePerimeter } = require('./lib/agm');
const SV = require('./lib/schema-validator');
const CV = require('./lib/config-validator');

const OUT = process.env.KT1_OUT;
const PROTO = path.join(OUT, 'protocols');
if (!fs.existsSync(PROTO)) fs.mkdirSync(PROTO, { recursive: true });

const expected = JSON.parse(fs.readFileSync(path.join(__dirname, 'expected.json'), 'utf8'));
const KAPPA_MIN = expected.meta.kappa_min || 0.05;

function loadCase(name) {
  const p = path.join(__dirname, 'cases', name + '.json');
  if (!fs.existsSync(p)) return null;
  const raw = JSON.parse(fs.readFileSync(p, 'utf8'));
  if (raw.same_as) return loadCase(raw.same_as);
  return raw;
}
function safeCall(fn) { try { return { ok: true, value: fn() }; } catch (e) { return { ok: false, err: String(e && e.stack || e) }; } }
function saveProto(id, v) { try { fs.writeFileSync(path.join(PROTO, id + '.json'), JSON.stringify(v, null, 2)); } catch (e) {} }
function isFork(x) { return Array.isArray(x) && x.length === 2 && typeof x[0] === 'number' && typeof x[1] === 'number'; }
function pairEq(a, b) { return Array.isArray(a) && Array.isArray(b) && a.length === 2 && b.length === 2 && ((a[0]===b[0]&&a[1]===b[1]) || (a[0]===b[1]&&a[1]===b[0])); }
function findCheck(checks, q) { return (checks || []).find(c => { if (q.req && c.req !== q.req) return false; if (q.quantity && c.quantity !== q.quantity) return false; if (q.case && c.case !== q.case) return false; return true; }) || null; }
function isCusp(c) { return c && (c.req === 'G-5б–г' || c.quantity === 'kappa_margin'); }
function getCusps(proto) { return (proto.checks || []).filter(isCusp); }
function findCusp(proto, ring, torus) {
  const cs = getCusps(proto);
  const strict = cs.find(c => Array.isArray(c.objects) && c.objects.includes(ring) && c.objects.includes(torus));
  if (strict) return { record: strict, fallback: false };
  const fb = cs.find(c => Array.isArray(c.objects) && c.objects.includes(ring));
  return { record: fb || null, fallback: !!fb, available: cs.map(c => c.objects) };
}
function findContact(proto, pair) { return (proto.contacts || []).find(c => pairEq(c.pair, pair)) || null; }
function deepGet(o, p) { return p.split('.').reduce((a, k) => a ? a[k] : undefined, o); }

function extractNum(proto, result, ex) {
  if (ex.k === 'check_min') {
    const checks = (proto.checks || []).filter(c => c.req === ex.r && c.case === ex.case);
    const forks = checks.map(c => c[ex.f]).filter(isFork);
    if (forks.length === 0) return null;
    if (forks.some(f => f[0] <= 0 && 0 <= f[1])) return { type: 'single', fork: [NaN, NaN], ctx: 'degenerate_zero' };
    const minLo = Math.min(...forks.map(f => f[0]));
    return { type: 'single', fork: [minLo, minLo], ctx: 'min_' + ex.f };
  }
  if (ex.k === 'check' && ex.f === 'halfplane_angles') {
    const checks = (proto.checks || []).filter(c => c.req === ex.r && c.case === ex.case && Array.isArray(c.halfplane_angles));
    const entries = [];
    for (const c of checks) for (const f of c.halfplane_angles) if (isFork(f)) entries.push({ fork: f, ctx: c.id || c.req });
    return { type: 'list', entries };
  }
  if (ex.k === 'check') {
    const checks = proto.checks || [];
    let ch = null;
    if (ex.oc) {
      ch = checks.find(c => isCusp(c) && Array.isArray(c.objects) && ex.oc.every(o => c.objects.includes(o)));
      if (!ch && ex.fb_oc) ch = checks.find(c => isCusp(c) && Array.isArray(c.objects) && ex.fb_oc.every(o => c.objects.includes(o)));
    } else if (ex.objs) {
      ch = checks.find(c => c.req === ex.r && Array.isArray(c.objects) && ex.objs.every(o => c.objects.includes(o)));
    } else {
      ch = findCheck(checks, { req: ex.r, quantity: ex.q, case: ex.case });
    }
    if (!ch) return null;
    const val = ex.f ? deepGet(ch, ex.f) : ch;
    return { type: 'single', fork: val, ctx: ch.id || ch.req || 'check' };
  }
  if (ex.k === 'rings_all') {
    const rings = (proto.configuration && proto.configuration.rings) || [];
    return { type: 'list', entries: rings.map(r => ({ fork: r[ex.f], ctx: r.name })) };
  }
  if (ex.k === 'cusp_records_all') {
    const cs = getCusps(proto);
    return { type: 'list', entries: cs.map(c => ({ fork: c[ex.f], ctx: c.objects })) };
  }
  if (ex.k === 'contact') {
    const c = findContact(proto, ex.pair || [ex.pair_ring, ex.pair_torus]);
    if (!c) return null;
    const val = ex.f.split('.').reduce((a, k) => a ? a[k] : undefined, c);
    return { type: 'single', fork: val, ctx: c.pair };
  }
  if (ex.k === 'contact_point') {
    const c = findContact(proto, ex.pair);
    if (!c || !Array.isArray(c.points)) return null;
    const pt = c.points[ex.idx || 0];
    if (!pt) return null;
    return { type: 'single', fork: pt[ex.f], ctx: c.pair };
  }
  if (ex.k === 'j5_edges_canon') {
    const j5 = proto.j5 || ((proto.edges && proto.canon) ? proto : null);
    if (!j5) return null;
    const entries = [];
    for (const e of (j5.edges || [])) {
      if (e.reading !== 'J5-CANON') continue;
      const c = findContact(proto, e.pair || [e.a, e.b]);
      if (!c || !Array.isArray(c.points) || !c.points[0]) continue;
      entries.push({ fork: c.points[0].cos, ctx: e.pair });
    }
    return { type: 'list', entries };
  }
  if (ex.k === 'triple') {
    const tr = (proto.configuration && proto.configuration.triples) || [];
    const t = tr.find(x => x.req === ex.r && (!ex.q || x.quantity === ex.q));
    if (!t) return null;
    return { type: 'single', fork: t[ex.f], ctx: t.torus };
  }
  if (ex.k === 'perimeter_width') {
    let fork = result;
    if (result && typeof result === 'object' && !Array.isArray(result)) fork = result.value;
    if (!isFork(fork)) return null;
    const w = fork[1] - fork[0];
    return { type: 'single', fork: [w, w], ctx: 'width' };
  }
  if (ex.k === 'minimize') {
    let val = result[ex.f];
    if (val === undefined && ex.f === 'min') val = result.min_value || result.value;
    return { type: 'single', fork: val, ctx: ex.f };
  }
  if (ex.k === 'single_check') return { type: 'single', fork: result[ex.f], ctx: result.id || 'ring_torus' };
  return null;
}

function applyOp(nd, ex) {
  const v = nd.v, tol = nd.tol || 0, op = nd.op;
  const inF = (f) => isFork(f) && f[0] >= v - tol && f[1] <= v + tol;
  const inH = (f) => isFork(f) && f[0] >= v - tol && f[1] < v + tol;
  if (op === 'contains' || op === 'within') return inF(ex.fork);
  if (op === 'contains_half_open' || op === 'within_half_open') return inH(ex.fork);
  if (op === 'all_contains' || op === 'all_within') return ex.type === 'list' && ex.entries.every(e => inF(e.fork));
  if (op === 'all_contains_half_open' || op === 'all_within_half_open') return ex.type === 'list' && ex.entries.every(e => inH(e.fork));
  if (op === 'list_contains_set') {
    if (!Array.isArray(v) || ex.type !== 'list') return false;
    return v.every(vi => ex.entries.some(e => isFork(e.fork) && e.fork[0] >= vi - tol && e.fork[1] <= vi + tol));
  }
  if (op === 'value_contains') return isFork(ex.fork) && ex.fork[0] - tol <= v && v <= ex.fork[1] + tol;
  if (op === 'certificate_only') {
    if (!isFork(ex.fork)) return false;
    const w = ex.fork[1] - ex.fork[0], lo = ex.fork[0];
    const wm = nd.width_max, lmin = nd.lo_min !== undefined ? nd.lo_min : 0;
    return (wm === undefined || w < wm) && lo > lmin;
  }
  if (op === 'le') return isFork(ex.fork) && ex.fork[1] <= v;
  if (op === 'le_with_margin') return isFork(ex.fork) && ex.fork[1] <= v + tol;
  return false;
}

function checkExpect(proto, exp, target) {
  const problems = [];
  const g = (p) => deepGet(proto, p);
  const push = (s) => problems.push(s);
  if (exp['verdict.geometry'] && !exp['verdict.geometry'].includes(g('verdict.geometry'))) push(`verdict.geometry=${g('verdict.geometry')}`);
  if (exp['j5.canon.verdict'] && !exp['j5.canon.verdict'].includes(g('j5.canon.verdict'))) push(`j5.canon.verdict=${g('j5.canon.verdict')}`);
  if (exp['j5.ext.verdict'] && !exp['j5.ext.verdict'].includes(g('j5.ext.verdict'))) push(`j5.ext.verdict=${g('j5.ext.verdict')}`);
  for (const k of ['contacts[0].existence','contacts[0].parallel','contacts[0].type','contacts[0].reading'])
    if (exp[k] && g(k) !== exp[k]) push(`${k}=${g(k)}`);
  if (exp['contacts.count_imposed'] !== undefined) { const n = (proto.contacts||[]).filter(c=>c.existence==='IMPOSED').length; if (n !== exp['contacts.count_imposed']) push(`IMPOSED count=${n}`); }
  if (exp['contacts.all_imposed_side']) { const b = (proto.contacts||[]).filter(c=>c.existence==='IMPOSED'&&c.type!=='SIDE'); if (b.length) push(`IMPOSED type≠SIDE: ${b.map(c=>c.pair).join(',')}`); }
  if (exp['contacts.all_imposed_sign_minus_1']) { const b = (proto.contacts||[]).filter(c=>c.existence==='IMPOSED'&&c.sign!==-1); if (b.length) push(`IMPOSED sign≠-1: ${b.map(c=>c.pair).join(',')}`); }
  if (exp['j5.edges.all_imposed_sign_minus_1']) {
    const impPairs = (proto.contacts||[]).filter(c=>c.existence==='IMPOSED').map(c=>c.pair);
    const edges = (proto.j5?.edges)||[];
    const imp = edges.filter(e => impPairs.some(p => pairEq(p, e.pair||[e.a,e.b])));
    if (imp.length === 0) push('no IMPOSED edges in j5');
    for (const e of imp) if (e.sign !== -1) push(`j5 edge ${JSON.stringify(e.pair)} sign=${e.sign}`);
  }
  if (exp['rings.count'] !== undefined) { const n = (proto.configuration?.rings||[]).length; if (n !== exp['rings.count']) push(`rings.count=${n}`); }
  if (exp['rings.length_all_close_2pi']) {
    const tol = 1e-6;
    for (const r of (proto.configuration?.rings||[])) if (isFork(r.length) && !(2*Math.PI >= r.length[0]-tol && 2*Math.PI <= r.length[1]+tol)) push(`ring ${r.name} length fork ${r.length}`);
  }
  if (exp['check.kappa_r_completeness']) {
    let rec = null;
    if (target) rec = findCusp(proto, target.ring, target.torus).record;
    else rec = getCusps(proto)[0] || null;
    if (!rec) push('no cusp record for completeness');
    else { const c = rec.cusp?.completeness || rec.completeness; if (!exp['check.kappa_r_completeness'].includes(c)) push(`cusp.completeness=${c}`); }
  }
  if (exp['gap_hi_negative']) {
    const c = findContact(proto, ['T0','T1']);
    if (!c || !isFork(c.gap) || !(c.gap[1] < 0)) push('gap.hi not negative');
  }
  if (exp['gap_contains_minus_1e-6_with_1e-15']) {
    const c = findContact(proto, ['T0','T1']); const tol = 1e-15;
    if (!c || !isFork(c.gap) || !(c.gap[0] <= -1e-6 + tol && c.gap[1] >= -1e-6 - tol)) push('gap ⊉ -1e-6 ± 1e-15');
  }
  return problems;
}

function checkNum(proto, result, nums) {
  const problems = [];
  for (const nd of nums || []) {
    const ex = extractNum(proto, result, nd.extract);
    if (!ex) { problems.push(`${nd.id}: field-not-found`); continue; }
    if (!applyOp(nd, ex)) {
      if (nd.op === 'certificate_only') problems.push(`${nd.id}: certificate criteria not satisfied — fork ${JSON.stringify(ex.fork)}`);
      else if (nd.depends_on) problems.push(`${nd.id}: differs (depends_on ${nd.depends_on}) — not evaluated`);
      else problems.push(`${nd.id}: FAIL — ${JSON.stringify(ex.fork)} not in [${nd.v - (nd.tol||0)}, ${nd.v + (nd.tol||0)}]`);
    }
  }
  return problems;
}

function runKλ1(spec) {
  const problems = [];
  const thetas = spec.expect.theta_list_deg;
  const tol = spec.expect.tolerance;
  for (const th of thetas) {
    const c = { id: `Kλ1_${th}`, thread: { n: 2, links: [{ theta: th, phi: 90, delta: 0 }, { theta: 0, phi: 0, delta: 0 }] }, hangs: [] };
    const call = safeCall(() => K.run(c));
    if (!call.ok) { problems.push(`θ=${th}: K.run threw`); continue; }
    const dCheck = (call.value.checks||[]).find(ch => ch.req === 'G-3' && (ch.quantity === 'link_distance' || ch.quantity === 'd'));
    if (!dCheck || !isFork(dCheck.value)) { problems.push(`θ=${th}: no d fork`); continue; }
    const dExp = 1 + Math.cos(th * Math.PI / 180);
    const [lo, hi] = dCheck.value;
    if (!(lo >= dExp - tol && hi <= dExp + tol)) problems.push(`θ=${th}: d=[${lo},${hi}] not within [${dExp-tol},${dExp+tol}]`);
  }
  return { id: 'Kλ1', status: problems.length ? 'FAIL' : 'PASS', problems };
}

function runKλ3(spec) {
  const problems = [];
  for (const cname of spec.cases || []) {
    const cd = loadCase(cname);
    if (!cd) { problems.push(`${cname}: no case`); continue; }
    const call = safeCall(() => K.run(cd));
    if (!call.ok) { problems.push(`${cname}: K.run threw`); continue; }
    const cs = getCusps(call.value);
    if (cs.length === 0) { problems.push(`${cname}: no cusp records`); continue; }
    for (const cr of cs) {
      const kr = cr.kappa_r;
      const krHi = isFork(kr) ? kr[1] : (typeof kr === 'number' ? kr : null);
      if (krHi === null) { problems.push(`${cname} ${cr.objects}: no kappa_r`); continue; }
      if (krHi > 2 + 1e-12) problems.push(`${cname} ${cr.objects}: κ_r_hi=${krHi} > 2 + 10⁻¹²`);
      const kap = cr.value;
      const kLo = isFork(kap) ? kap[0] : (typeof kap === 'number' ? kap : null);
      if (kLo !== null && kLo < KAPPA_MIN) problems.push(`${cname} ${cr.objects}: κ_lo=${kLo} < ${KAPPA_MIN}`);
      const comp = cr.cusp?.completeness || cr.completeness;
      if (!['EXACT','CERTIFIED'].includes(comp)) problems.push(`${cname} ${cr.objects}: completeness=${comp}`);
    }
  }
  return { id: 'Kλ3', status: problems.length ? 'FAIL' : 'PASS', problems };
}

function runM3i(spec) {
  const problems = [];
  for (const p of spec.cases || []) {
    const cd = loadCase(p);
    if (!cd) { problems.push(`${p}: no case`); continue; }
    const call = safeCall(() => K.run(cd));
    if (!call.ok) { problems.push(`${p}: K.run threw`); continue; }
    const c = findContact(call.value, ['T0', 'T1']);
    if (!c || !isFork(c.gap)) { problems.push(`${p}: no T0-T1 gap`); continue; }
    const [lo, hi] = c.gap;
    if (!(hi < 0)) problems.push(`${p}: gap.hi=${hi} not negative`);
    if (!(lo <= -0.002 + 1e-15 && hi >= -0.002 - 1e-15)) problems.push(`${p}: gap=${JSON.stringify(c.gap)} not ⊇ -0.002 ± 1e-15`);
  }
  return { id: 'm3i', status: problems.length ? 'FAIL' : 'PASS', problems };
}

function runTest(id, spec) {
  const r = { id, kind: spec.kind, status: 'PASS', problems: [] };
  try {
    if (spec.kind === 'K.run') {
      const cd = loadCase(spec.case);
      if (!cd) { r.status = 'ERROR'; r.problems.push(`case not found: ${spec.case}`); return r; }
      const call = safeCall(() => K.run(cd));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.run threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      const svErrs = SV.validate(call.value);
      if (svErrs.length > 0) r.problems.push('schema: ' + svErrs.slice(0,3).join('; ') + (svErrs.length>3 ? ` ... (${svErrs.length})` : ''));
      const cvErrs = CV.check(call.value);
      if (cvErrs.length > 0) r.problems.push('config: ' + cvErrs.join('; '));
      r.problems.push(...checkExpect(call.value, spec.expect, spec.cusp_target));
      r.problems.push(...checkNum(call.value, call.value, spec.num));
    } else if (spec.kind === 'K.perimeter') {
      const [s1, s2] = spec.params;
      const call = safeCall(() => K.perimeter(s1, s2));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.perimeter threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      let fork = Array.isArray(call.value) ? call.value : call.value.value;
      if (!isFork(fork)) { r.status = 'FAIL'; r.problems.push('perimeter not fork'); return r; }
      if (fork[1] - fork[0] > 1e-12) r.problems.push(`width=${fork[1]-fork[0]} > 1e-12`);
      const pTrue = truePerimeter(s1, s2);
      if (!(fork[0] - 1e-10 <= pTrue && pTrue <= fork[1] + 1e-10)) r.problems.push(`perimeter fork ${fork} not ⊇ ${pTrue}`);
    } else if (spec.kind === 'K.ringRing') {
      const p = spec.params;
      const call = safeCall(() => K.ringRing(p.r1, p.r2, p.sharedCusp));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.ringRing threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      if (spec.expect.contact_class && call.value.contact_class !== spec.expect.contact_class) r.problems.push(`contact_class=${call.value.contact_class}`);
    } else if (spec.kind === 'K.ringTorus') {
      const p = spec.params;
      const call = safeCall(() => K.ringTorus(p.ring, p.torus, p.threaded));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.ringTorus threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      const expV = spec.expect.verdict;
      const av = call.value.verdict;
      if (Array.isArray(expV)) { if (!expV.includes(av)) r.problems.push(`verdict=${av}`); }
      else if (av !== expV) r.problems.push(`verdict=${av}`);
      if (spec.expect.value_contains !== undefined) {
        const tol = spec.expect.value_contains_tol || 1e-15;
        const v = call.value.value;
        if (!isFork(v) || !(v[0] <= spec.expect.value_contains + tol && v[1] >= spec.expect.value_contains - tol)) r.problems.push(`value fork ${v} ⊉ ${spec.expect.value_contains}`);
      }
      r.problems.push(...checkNum(null, call.value, spec.num));
    } else if (spec.kind === 'K.j5Reading') {
      const call = safeCall(() => K.j5Reading(spec.params));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.j5Reading threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      const e = spec.expect;
      if (call.value.reading !== e.reading) r.problems.push(`reading=${call.value.reading}`);
      if (call.value.sign !== e.sign) r.problems.push(`sign=${call.value.sign}`);
      if (e.contact_class && call.value.contact_class !== e.contact_class) r.problems.push(`contact_class=${call.value.contact_class}`);
      if (e.epsilon_range && !(call.value.epsilon >= e.epsilon_range[0] && call.value.epsilon <= e.epsilon_range[1])) r.problems.push(`epsilon=${call.value.epsilon}`);
    } else if (spec.kind === 'K.j5Graph') {
      const p = spec.params_from ? expected.tests[spec.params_from].params : spec.params;
      const call = safeCall(() => K.j5Graph(p));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.j5Graph threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      const j5 = (call.value.canon && call.value.ext) ? call.value : (call.value.j5 || call.value);
      if (spec.expect['j5.canon.verdict'] && !spec.expect['j5.canon.verdict'].includes(j5.canon?.verdict)) r.problems.push(`canon.verdict=${j5.canon?.verdict}`);
      if (spec.expect['j5.ext.verdict'] && !spec.expect['j5.ext.verdict'].includes(j5.ext?.verdict)) r.problems.push(`ext.verdict=${j5.ext?.verdict}`);
    } else if (spec.kind === 'K.validate') {
      const call = safeCall(() => K.validate(spec.params.constructed));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.validate threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      if (!Array.isArray(call.value) || call.value.length === 0) r.problems.push('K.validate empty');
    } else if (spec.kind === 'K.minimize') {
      const p = spec.params;
      const x0 = p.x0_num / p.x0_den;
      const tol = spec.expect.tolerance || 1e-12;
      const f = (x) => { const dx = x - x0; if (Math.abs(dx) > 1/65536) return [0, 0]; const v = -1 + Math.abs(dx) * 65536; return [v, v]; };
      const call = safeCall(() => K.minimize({ f, a: p.a, b: p.b, L: p.L, periodic: p.periodic }));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push(`K.minimize threw: ${call.err}`); return r; }
      saveProto(id, call.value);
      const minv = call.value.min || call.value.min_value || call.value.value;
      if (!isFork(minv) || !(minv[0] <= -1 + tol && minv[1] >= -1 - tol)) r.problems.push(`min fork ${JSON.stringify(minv)} ⊉ -1`);
      const arg = call.value.argmin || call.value.min_points || [];
      const found = Array.isArray(arg) && arg.some(pt => isFork(pt) && pt[0] - tol <= x0 && x0 <= pt[1] + tol);
      if (!found) r.problems.push(`argmin ∌ x0=${x0}`);
    } else {
      r.status = 'ERROR'; r.problems.push(`unknown kind: ${spec.kind}`);
    }
  } catch (e) { r.status = 'ERROR'; r.problems.push(String(e && e.stack || e)); }
  if (r.problems.length && r.status === 'PASS') r.status = 'FAIL';
  return r;
}

function main() {
  const results = [];
  for (const id of Object.keys(expected.tests)) {
    const s = expected.tests[id];
    if (id === 'Kλ1') results.push(runKλ1(s));
    else if (id === 'Kλ3') results.push(runKλ3(s));
    else if (id === 'm3i') results.push(runM3i(s));
    else results.push(runTest(id, s));
  }
  fs.writeFileSync(path.join(OUT, 'd3_results.json'), JSON.stringify({ meta: expected.meta, results, mutants: expected.mutants, run_date: new Date().toISOString() }, null, 2));
  const p = results.filter(r => r.status === 'PASS').length;
  const f = results.filter(r => r.status === 'FAIL').length;
  const e = results.filter(r => r.status === 'ERROR').length;
  console.log(`d3 rev5: ${results.length} tests; PASS=${p} FAIL=${f} ERROR=${e}`);
  process.exit(0);
}

main();
```

### FILE: d3/selftest.js
```
'use strict';
const fs = require('fs');
const path = require('path');
const SV = require('./lib/schema-validator');
const CV = require('./lib/config-validator');
const K6 = require('./lib/k6-enumerator');
const { truePerimeter, perimeterFork } = require('./lib/agm');

const OUT = process.env.KT1_OUT;
const results = [];
function record(id, status, details) { results.push({ id, status, details: details || null }); }

function testK6_B9() {
  const g = {
    vertices: ['T1','T2','T3','T4'],
    edges: [
      {a:'T1',b:'T2',cls:'LINK',existence:'IMPOSED',reading:'J5-CANON',sign:1},
      {a:'T2',b:'T3',cls:'LINK',existence:'IMPOSED',reading:'J5-CANON',sign:1},
      {a:'T3',b:'T1',cls:'LINK',existence:'IMPOSED',reading:'J5-CANON',sign:1},
      {a:'T3',b:'T4',cls:'CONTACT-ONLY',existence:'IMPOSED',reading:'J5-EXT',sign:1}
    ]
  };
  const r = K6.evaluate(g);
  record('k6_B9', (r.j5.canon.verdict === 'UNRESOLVED' && r.j5.ext.verdict === 'PASSED-EXT') ? 'PASS' : 'FAIL', r.j5);
}

function testK6_B1() {
  const g = {
    vertices: ['T1','T2','T3'],
    edges: [
      {a:'T1',b:'T2',cls:'LINK',existence:'IMPOSED',reading:'J5-CANON',sign:-1},
      {a:'T2',b:'T3',cls:'LINK',existence:'IMPOSED',reading:'J5-CANON',sign:-1},
      {a:'T3',b:'T1',cls:'LINK',existence:'IMPOSED',reading:'J5-CANON',sign:-1}
    ]
  };
  const r = K6.evaluate(g);
  record('k6_B1', r.j5.canon.verdict === 'FORBIDDEN' ? 'PASS' : 'FAIL', r.j5);
}

function testK6_B10() {
  const g = {
    vertices: ['S1','S2'],
    edges: [{a:'S1',b:'S2',cls:'LINK',existence:'IMPOSED',reading:'J5-CLASS-UNRESOLVED',sign:1}]
  };
  const r = K6.evaluate(g);
  record('k6_B10_single', (r.j5.canon.verdict === 'UNRESOLVED' && r.j5.ext.verdict === 'PASSED-EXT') ? 'PASS' : 'FAIL', r.j5);
}

function testK6_empty() {
  const g = { vertices: ['T1'], edges: [] };
  const r = K6.evaluate(g);
  record('k6_empty', (r.j5.canon.verdict === 'PASSED' && r.j5.ext.verdict === 'PASSED-EXT') ? 'PASS' : 'FAIL', r.j5);
}

function testSV() {
  const bad = {
    checks: [{ id:'x', req:'G-4', objects:[], quantity:'gap', value:[-0.001,0.001], completeness:'SAMPLED', verdict:'PASSED', where:null, level:'L2', layer:'CARRIER' }],
    configuration: { rings: [] }, verdict: { geometry: 'PASSED' }
  };
  const errs = SV.validate(bad);
  record('sv_PASSED_with_SAMPLED', errs.some(e => e.indexOf('SAMPLED') >= 0) ? 'PASS' : 'FAIL', errs);

  const ringNoWidths = {
    checks: [],
    configuration: { rings: [{ name: 'R0', source: 'construction', C:[[0,0],[0,0],[0,0]], E1:[[1,1],[0,0],[0,0]], E2:[[0,0],[1,1],[0,0]], s1:[0.5,0.5], s2:[0.5,0.5] }] },
    verdict: { geometry: 'PASSED' }
  };
  const errs2 = SV.validate(ringNoWidths);
  record('sv_ring_missing_widths', errs2.some(e => e.indexOf('widths') >= 0) ? 'PASS' : 'FAIL', errs2);

  const forkBad = {
    checks: [{ id:'x', req:'G-4', objects:[], quantity:'gap', value:[0.5,0.1], completeness:'CERTIFIED', verdict:'PASSED', where:null, level:'L2', layer:'CARRIER' }],
    configuration: { rings: [] }, verdict: { geometry: 'PASSED' }
  };
  const errs3 = SV.validate(forkBad);
  record('sv_lo_gt_hi', errs3.some(e => e.indexOf('lo > hi') >= 0) ? 'PASS' : 'FAIL', errs3);
}

function testCV() {
  const ok = CV.check({ checks: [{verdict:'PASSED'},{verdict:'PASSED'}], verdict: { geometry: 'PASSED' } });
  record('cv_all_passed_ok', ok.length === 0 ? 'PASS' : 'FAIL', ok);
  const bad = CV.check({ checks: [{verdict:'PASSED'},{verdict:'FORBIDDEN'}], verdict: { geometry: 'PASSED' } });
  record('cv_one_forbidden_flagged', bad.length > 0 ? 'PASS' : 'FAIL', bad);
  const unsolved = CV.check({ checks: [{verdict:'PASSED'},{verdict:'UNRESOLVED'}], verdict: { geometry: 'PASSED' } });
  record('cv_unsolved_flagged', unsolved.length > 0 ? 'PASS' : 'FAIL', unsolved);
  const badC = CV.check({ checks: [{verdict:'UNRESOLVED'},{verdict:'UNRESOLVED'}], verdict: { geometry: 'UNRESOLVED' } });
  record('cv_all_unsolved_ok', badC.length === 0 ? 'PASS' : 'FAIL', badC);
}

function testTruePerimeter() {
  const p1 = truePerimeter(1, 1);
  record('perimeter_circle_r1', Math.abs(p1 - 2 * Math.PI) < 1e-9 ? 'PASS' : 'FAIL', { computed: p1, expected: 2 * Math.PI });

  const p2 = truePerimeter(0.5, 0.5);
  record('perimeter_circle_r05', Math.abs(p2 - Math.PI) < 1e-9 ? 'PASS' : 'FAIL', { computed: p2, expected: Math.PI });

  const p3 = truePerimeter(1, 0.5);
  const p3_known = 4.84422411;
  record('perimeter_ellipse_1_05', Math.abs(p3 - p3_known) < 1e-6 ? 'PASS' : 'FAIL', { computed: p3, expected: p3_known });
}

function testPerimeterFork() {
  const f = perimeterFork([1, 1], [0.5, 0.5]);
  const expected = 4.84422411;
  // FIX (rev4): статус должен быть 'PASS'/'FAIL', не boolean.
  const ok = Math.abs(f[0] - expected) < 1e-6 && Math.abs(f[1] - expected) < 1e-6;
  record('perimeterFork_exact_1_05', ok ? 'PASS' : 'FAIL', { fork: f, expected });
}

function testFindCheck() {
  const { findCheck } = require('./lib/compare');
  const recs = [
    { id: 'x', req: 'G-5а', quantity: 'gap', value: [-0.01, -0.001] },
    { id: 'y', req: 'G-5б–г', quantity: 'kappa_margin', value: [0.5, 0.6] },
    { id: 'z', req: 'G-4', quantity: 'gap', value: [0.5, 1.0] }
  ];
  const byReq = findCheck(recs, { req: 'G-5б–г' });
  const byQ = findCheck(recs, { quantity: 'kappa_margin' });
  record('findCheck_by_req', byReq && byReq.id === 'y' ? 'PASS' : 'FAIL', byReq && byReq.id);
  record('findCheck_by_quantity', byQ && byQ.id === 'y' ? 'PASS' : 'FAIL', byQ && byQ.id);
}

function main() {
  testK6_B9(); testK6_B1(); testK6_B10(); testK6_empty();
  testSV(); testCV(); testTruePerimeter(); testPerimeterFork(); testFindCheck();
  fs.writeFileSync(path.join(OUT, 'd3_selftest.json'), JSON.stringify({
    results, run_date: new Date().toISOString()
  }, null, 2));
  const passed = results.filter(r => r.status === 'PASS').length;
  const failed = results.filter(r => r.status === 'FAIL').length;
  console.log('d3_selftest: ' + results.length + '; PASS=' + passed + ' FAIL=' + failed);
  process.exit(0);
}

main();
```
