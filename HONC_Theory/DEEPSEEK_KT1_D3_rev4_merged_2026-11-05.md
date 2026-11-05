# Сборка: DEEPSEEK_KT1_D3_rev3_merged_2026-11-05.md + патч DEEPSEEK_KT1_D3_SUBMISSION_2026-11-05_rev4_patch.md (механически, без правок)

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
```
{
  "meta": {
    "source": "Д-1 rev16 + Д-2 rev16 fix, спецификация v0.3+поправка1, Round 3a §7, интерфейс v6",
    "kappa_min": 0.05,
    "theta_min_deg": 1
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
      }
    },
    "A2i": {"kind": "K.run", "case": "A2i", "expect": {"verdict.geometry": ["PASSED"], "j5.canon.verdict": ["PASSED"]}},
    "A2ii": {"kind": "K.run", "case": "A2ii", "expect": {"verdict.geometry": ["PASSED"], "j5.canon.verdict": ["FORBIDDEN"]}},
    "A2iii": {"kind": "K.run", "case": "A2iii", "expect": {"verdict.geometry": ["PASSED"], "j5.canon.verdict": ["FORBIDDEN"]}},
    "A2iv": {"kind": "K.run", "case": "A2iv", "expect": {"verdict.geometry": ["FORBIDDEN"]}},
    "A3": {"kind": "K.run", "case": "A3", "expect": {"verdict.geometry": ["PASSED"], "j5.canon.verdict": ["FORBIDDEN"]}},
    "A4": {
      "kind": "K.run",
      "case": "A4",
      "cusp_target": {"ring": "RH1", "torus": "T2"},
      "expect": {
        "verdict.geometry": ["PASSED"],
        "j5.canon.verdict": ["UNRESOLVED"],
        "j5.ext.verdict": ["PASSED-EXT"],
        "check.kappa_r_in_range": [1.3655, 1.3665],
        "check.kappa_r_completeness": ["EXACT"]
      }
    },
    "A5": {
      "kind": "K.run",
      "case": "A5",
      "expect": {
        "verdict.geometry": ["FORBIDDEN", "UNRESOLVED"],
        "_note": "A-5 INDEPENDENT COVERAGE = OPEN; UNRESOLVED допустим по §4.2, но не засчитывается как успешная проверка проникновения"
      }
    },
    "Kλ1": {
      "kind": "K.run",
      "cases": ["Kλ1_0", "Kλ1_30", "Kλ1_60", "Kλ1_75", "Kλ1_85"],
      "expect": {
        "d_by_theta": {"0": 2.0, "30": 1.8660254, "60": 1.5, "75": 1.2588190, "85": 1.0871557},
        "tolerance": 1e-9
      }
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
      }
    },
    "B2": {"kind": "K.run", "case": "B2", "expect": {"j5.canon.verdict": ["UNRESOLVED"], "j5.ext.verdict": ["PASSED-EXT"]}},
    "B3": {"kind": "K.run", "case": "B3", "expect": {"j5.canon.verdict": ["UNRESOLVED"], "j5.ext.verdict": ["PASSED-EXT", "UNRESOLVED"]}},
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
    "m1a": {"kind": "K.perimeter", "params": [1, 0.5], "expect": {"width_le_1e-12": true, "fork_contains_true": true}},
    "m1b": {
      "kind": "K.run",
      "case": "m1b",
      "agm": {"X": 0.001, "eps_ind_factor": 1e-12},
      "expect": {"outcome_possible": ["PASS", "UNRESOLVED", "MUTANT_HIT"]}
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
      "kind": "MY_CONFIG_VALIDATOR",
      "params": {
        "constructed": {
          "checks": [{"id":"x","req":"G-4","objects":["Q0"],"quantity":"gap","value":[-0.001,0.001],"completeness":"SAMPLED","verdict":"PASSED","reason":null,"where":null,"level":"L2","layer":"CARRIER","status":null}],
          "verdict": {"geometry": "PASSED"}
        }
      },
      "expect": {"violations_non_empty": true}
    },
    "m13A": {
      "kind": "K.ringTorus",
      "params": {
        "ring": {"C": [-2, 0, 0], "E1": [1,0,0], "E2": [0,1,0], "s1": 2, "s2": 1},
        "torus": {"A": [0,0,0], "T": [0,1,0]},
        "threaded": true
      },
      "expect": {"verdict": ["UNRESOLVED"]}
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
      "expect": {"verdict": ["FORBIDDEN"], "value_contains": -0.000001, "value_contains_tol": 1e-15}
    }
  },
  "mutants": {
    "m1": {"caught_by": ["m1a", "m1b"], "expected_on_kernel": "m1a PASS; m1b PASS_OR_UNRESOLVED", "expected_on_mutant": "m1a FAIL; m1b FAIL_OR_MUTANT_HIT", "reason": "Приближённая формула периметра"},
    "m2": {"caught_by": ["m2a", "m2b"], "expected_on_kernel": "m2a PASS (UNRESOLVED CONTACT); m2b PASS (FORBIDDEN)", "expected_on_mutant": "FAIL", "reason": "Слепая зона у каспа"},
    "m3": {"caught_by": ["m3i", "m3ii"], "expected_on_kernel": "m3i PASS; m3ii PASS", "expected_on_mutant": "FAIL", "reason": "PASSED по выборке"},
    "m4": {"caught_by": ["m4"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL", "reason": "K-6 только по циклам"},
    "m5": {"caught_by": ["m5i", "m5ii"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL", "reason": "Параллельность по допуску"},
    "m8": {"caught_by": ["m8"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL", "reason": "Кандидат как IMPOSED"},
    "m12": {"caught_by": ["m12"], "expected_on_kernel": "PASS", "expected_on_mutant": "FAIL", "reason": "Граф без CONTACT-ONLY"},
    "m13": {"caught_by": ["m13A", "m13B"], "expected_on_kernel": "m13A PASS; m13B PASS", "expected_on_mutant": "FAIL", "reason": "Допуск на κ_r=2"},
    "m14": {"caught_by": ["m14tt", "m14rt"], "expected_on_kernel": "m14tt PASS; m14rt PASS", "expected_on_mutant": "FAIL", "reason": "Допуск на проникновение"}
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
```
'use strict';
const fs = require('fs');
const path = require('path');
const K = require(path.join(process.env.KT1_DIR, 'kt1'));
const SV = require('./lib/schema-validator');
const CV = require('./lib/config-validator');
const { truePerimeter, perimeterFork } = require('./lib/agm');
const { get, findCheck } = require('./lib/compare');

const OUT = process.env.KT1_OUT;
const PROTO_DIR = path.join(OUT, 'protocols');
if (!fs.existsSync(PROTO_DIR)) fs.mkdirSync(PROTO_DIR, { recursive: true });

const expected = JSON.parse(fs.readFileSync(path.join(__dirname, 'expected.json'), 'utf8'));

function loadCase(name) {
  const raw = JSON.parse(fs.readFileSync(path.join(__dirname, 'cases', name + '.json'), 'utf8'));
  if (raw.same_as) return loadCase(raw.same_as);
  return raw;
}

function safeCall(fn) {
  try { return { ok: true, value: fn() }; }
  catch (e) { return { ok: false, err: String(e && e.stack || e) }; }
}

function saveProto(id, proto) {
  fs.writeFileSync(path.join(PROTO_DIR, id + '.json'), JSON.stringify(proto, null, 2));
}

function j5Record(container) {
  if (!container) return null;
  if (container.canon && container.ext) return container;
  if (container.j5 && container.j5.canon) return container.j5;
  return null;
}

// Per interface §6.3, j5.edges[] has pair, cls, reading, sign, on_cycle, bridge.
// "IMPOSED" is a field of contacts[] (§6.2), NOT of edges[]. Match by pair.
function imposedEdges(proto) {
  const j5 = j5Record(proto.j5) || (proto.edges && proto.edges.length ? proto : null);
  if (!j5) return { edges: [], reason: 'no j5 record' };
  const contacts = (proto.contacts || []);
  const impPairs = new Set();
  for (const c of contacts) {
    if (c.existence === 'IMPOSED' && Array.isArray(c.pair)) {
      const [a, b] = c.pair;
      impPairs.add(a + '|' + b);
      impPairs.add(b + '|' + a);
    }
  }
  const edges = (j5.edges || []).filter(e => {
    let pair = e.pair;
    if (!Array.isArray(pair)) {
      if (e.a && e.b) pair = [e.a, e.b];
      else return false;
    }
    return impPairs.has(pair[0] + '|' + pair[1]);
  });
  return { edges, reason: null };
}

function getGapFork(proto) {
  const contacts = proto.contacts || [];
  if (contacts.length > 0 && Array.isArray(contacts[0].gap)) return contacts[0].gap;
  const g4 = findCheck(proto.checks, { req: 'G-4' });
  if (g4 && Array.isArray(g4.value)) return g4.value;
  return null;
}

function isCuspCheck(c) {
  return c.req === 'G-5б–г' || c.quantity === 'kappa_margin';
}

// Select the cusp record for a specific (ring, torus) pair.
// Per §2 interface: RH{j} for hang ring; T{k} for thread torus, H{j} for hang torus.
// diag (optional) collects all cusp objects for diagnosis when no strict match found.
function getCuspRecordFor(proto, ringName, torusName, diag) {
  const checks = proto.checks || [];
  for (const c of checks) {
    if (!isCuspCheck(c)) continue;
    const objs = c.objects || [];
    if (objs.indexOf(ringName) >= 0 && objs.indexOf(torusName) >= 0) return c;
  }
  if (diag) diag.allCuspObjects = checks.filter(isCuspCheck).map(c => c.objects || []);
  // Fallback: ring only (some kernels may name check objects differently)
  for (const c of checks) {
    if (!isCuspCheck(c)) continue;
    const objs = c.objects || [];
    if (objs.indexOf(ringName) >= 0) {
      if (diag) diag.fallback = true;
      return c;
    }
  }
  return null;
}

function compareRun(id, spec, proto) {
  const problems = [];
  const exp = spec.expect || {};
  const svErrs = SV.validate(proto);
  if (svErrs.length) problems.push('schema: ' + svErrs.join('; '));
  const cvErrs = CV.check(proto);
  if (cvErrs.length) problems.push('config-rule: ' + cvErrs.join('; '));

  if (exp['verdict.geometry']) {
    const v = get(proto, 'verdict.geometry');
    if (exp['verdict.geometry'].indexOf(v) < 0) problems.push('verdict.geometry=' + v);
  }
  if (exp['j5.canon.verdict']) {
    const v = get(proto, 'j5.canon.verdict');
    if (exp['j5.canon.verdict'].indexOf(v) < 0) problems.push('j5.canon.verdict=' + v);
  }
  if (exp['j5.ext.verdict']) {
    const v = get(proto, 'j5.ext.verdict');
    if (exp['j5.ext.verdict'].indexOf(v) < 0) problems.push('j5.ext.verdict=' + v);
  }
  for (const key of ['contacts[0].existence', 'contacts[0].parallel', 'contacts[0].type', 'contacts[0].reading']) {
    if (exp[key]) {
      const v = get(proto, 'contacts.0.' + key.split('.')[1]);
      if (v !== exp[key]) problems.push(key + '=' + v);
    }
  }
  if (exp['contacts.count_imposed'] !== undefined) {
    const contacts = proto.contacts || [];
    const n = contacts.filter(c => c.existence === 'IMPOSED').length;
    if (n !== exp['contacts.count_imposed']) problems.push('IMPOSED count=' + n);
  }
  if (exp['contacts.all_imposed_side']) {
    const contacts = (proto.contacts || []).filter(c => c.existence === 'IMPOSED');
    const bad = contacts.find(c => c.type !== 'SIDE');
    if (bad) problems.push('IMPOSED contact type=' + bad.type + ' not SIDE');
  }
  if (exp['contacts.all_imposed_sign_minus_1']) {
    const contacts = (proto.contacts || []).filter(c => c.existence === 'IMPOSED');
    const bad = contacts.find(c => c.sign !== -1);
    if (bad) problems.push('IMPOSED contact sign=' + bad.sign + ' not -1');
  }
  if (exp['j5.edges.all_imposed_sign_minus_1']) {
    const r = imposedEdges(proto);
    if (r.edges.length === 0) problems.push('no IMPOSED edges in j5 (' + (r.reason || 'contacts[] empty or pair mismatch') + ')');
    for (const e of r.edges) {
      if (e.sign !== -1) problems.push('j5 IMPOSED edge pair=' + JSON.stringify(e.pair || [e.a, e.b]) + ' sign=' + e.sign);
    }
  }
  if (exp['rings.count'] !== undefined) {
    const rings = get(proto, 'configuration.rings') || [];
    if (rings.length !== exp['rings.count']) problems.push('rings.count=' + rings.length);
  }
  if (exp['rings.length_all_close_2pi']) {
    const rings = get(proto, 'configuration.rings') || [];
    const tol = 1e-6;
    for (const r of rings) {
      if (r.length && Array.isArray(r.length)) {
        const inside = 2 * Math.PI >= r.length[0] - tol && 2 * Math.PI <= r.length[1] + tol;
        if (!inside) problems.push('ring ' + r.name + ' length fork ' + JSON.stringify(r.length));
      }
    }
  }
  // A4: κ_r range and cusp.completeness — using cusp_target to select correct record
  if (exp['check.kappa_r_in_range'] || exp['check.kappa_r_completeness']) {
    const target = spec.cusp_target || { ring: 'RH1', torus: 'T2' };
    const diag = {};
    const rec = getCuspRecordFor(proto, target.ring, target.torus, diag);
    if (!rec) {
      problems.push('no kappa_margin record for ' + target.ring + ' in ' + target.torus +
                    '; available cusp objects: ' + JSON.stringify(diag.allCuspObjects || []));
    } else {
      if (exp['check.kappa_r_in_range']) {
        const range = exp['check.kappa_r_in_range'];
        const kr = rec.kappa_r !== undefined ? rec.kappa_r :
                   (Array.isArray(rec.value) ? rec.value : (rec.value !== undefined ? [rec.value, rec.value] : null));
        if (kr === null) {
          problems.push('no kappa_r in G-5б–г record; keys=' + Object.keys(rec).join(',') +
                        (diag.fallback ? ' [FALLBACK to ring-only match]' : ''));
        } else if (Array.isArray(kr)) {
          if (kr[0] > range[1] || kr[1] < range[0]) problems.push('kappa_r fork ' + JSON.stringify(kr) + ' outside [' + range[0] + ',' + range[1] + '] for ' + target.ring + '↔' + target.torus);
        } else if (kr < range[0] || kr > range[1]) {
          problems.push('kappa_r=' + kr + ' for ' + target.ring + '↔' + target.torus);
        }
      }
      if (exp['check.kappa_r_completeness']) {
        const cuspComp = get(rec, 'cusp.completeness');
        if (!cuspComp) {
          problems.push('no cusp.completeness in G-5б–г record; keys=' + Object.keys(rec).join(','));
        } else if (exp['check.kappa_r_completeness'].indexOf(cuspComp) < 0) {
          problems.push('cusp.completeness=' + cuspComp + ' for ' + target.ring + '↔' + target.torus);
        }
      }
    }
  }
  // m14tt: gap fork
  if (exp['gap_hi_negative'] || exp['gap_contains_minus_1e-6_with_1e-15']) {
    const gap = getGapFork(proto);
    if (!Array.isArray(gap)) {
      problems.push('no contacts[0].gap / G-4 value fork');
    } else {
      if (exp['gap_hi_negative'] && !(gap[1] < 0)) problems.push('gap.hi=' + gap[1] + ' not negative');
      if (exp['gap_contains_minus_1e-6_with_1e-15']) {
        const tol = 1e-15;
        const tgt = -1e-6;
        const c = (gap[0] - tol) <= tgt && tgt <= (gap[1] + tol);
        if (!c) problems.push('gap [' + gap[0] + ',' + gap[1] + '] does not contain -1e-6 ±' + tol);
      }
    }
  }
  // m1b: outcome via perimeterFork on R0's s1/s2 from protocol
  if (exp['outcome_possible']) {
    const cfg = spec.agm || {};
    const X = cfg.X !== undefined ? cfg.X : 0.001;
    const epsFactor = cfg.eps_ind_factor !== undefined ? cfg.eps_ind_factor : 1e-12;
    const rings = get(proto, 'configuration.rings') || [];
    const r0 = rings.find(r => r.name === 'R0');
    if (!r0 || !Array.isArray(r0.s1) || !Array.isArray(r0.s2)) {
      problems.push('m1b: no R0.s1/s2 fork in configuration.rings[]');
    } else {
      const pf = perimeterFork(r0.s1, r0.s2);
      const W = pf[1] - pf[0];
      const epsInd = epsFactor * pf[0];
      const twoPi = 2 * Math.PI;
      let outcome;
      if (twoPi < pf[0] - epsInd || twoPi > pf[1] + epsInd) outcome = 'MUTANT_HIT';
      else if (W < X) outcome = 'PASS';
      else outcome = 'UNRESOLVED';
      if (exp['outcome_possible'].indexOf(outcome) < 0) {
        problems.push('m1b outcome=' + outcome + ' P=' + JSON.stringify(pf) + ' W=' + W + ' X=' + X);
      }
    }
  }
  return problems;
}

function runTest(id, spec) {
  const r = { id, kind: spec.kind, status: 'PASS', problems: [] };
  try {
    if (spec.kind === 'K.run') {
      const caseData = loadCase(spec.case);
      const call = safeCall(() => K.run(caseData));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.run threw: ' + call.err); return r; }
      saveProto(id, call.value);
      const probs = compareRun(id, spec, call.value);
      if (probs.length) { r.status = 'FAIL'; r.problems.push(...probs); }
    } else if (spec.kind === 'K.perimeter') {
      const [s1, s2] = spec.params;
      const call = safeCall(() => K.perimeter(s1, s2));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.perimeter threw: ' + call.err); return r; }
      const raw = call.value;
      const v = Array.isArray(raw) ? raw : (raw && raw.value);
      if (!Array.isArray(v)) { r.status = 'FAIL'; r.problems.push('perimeter not fork: ' + JSON.stringify(raw)); return r; }
      if (v[1] - v[0] > 1e-12) r.problems.push('fork width ' + (v[1] - v[0]) + ' > 1e-12');
      const pTrue = truePerimeter(s1, s2);
      if (pTrue < v[0] - 1e-10 || pTrue > v[1] + 1e-10) r.problems.push('fork [' + v[0] + ',' + v[1] + '] does not contain true perimeter ' + pTrue);
      if (r.problems.length) r.status = 'FAIL';
    } else if (spec.kind === 'K.ringRing') {
      const p = spec.params;
      const call = safeCall(() => K.ringRing(p.r1, p.r2, p.sharedCusp));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.ringRing threw: ' + call.err); return r; }
      saveProto(id, call.value);
      const exp = spec.expect.contact_class;
      const actual = get(call.value, 'contact_class');
      if (actual !== exp) { r.status = 'FAIL'; r.problems.push('contact_class=' + actual + ' expected ' + exp); }
    } else if (spec.kind === 'K.ringTorus') {
      const p = spec.params;
      const call = safeCall(() => K.ringTorus(p.ring, p.torus, p.threaded));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.ringTorus threw: ' + call.err); return r; }
      saveProto(id, call.value);
      const expectV = spec.expect.verdict;
      const actual = get(call.value, 'verdict');
      if (Array.isArray(expectV)) {
        if (expectV.indexOf(actual) < 0) r.problems.push('verdict=' + actual + ' expected ' + expectV.join('/'));
      } else if (actual !== expectV) {
        r.problems.push('verdict=' + actual + ' expected ' + expectV);
      }
      if (spec.expect.value_contains !== undefined) {
        const v = get(call.value, 'value');
        const tgt = spec.expect.value_contains;
        const tol = spec.expect.value_contains_tol || 1e-15;
        if (!Array.isArray(v)) r.problems.push('value not fork');
        else if (!((v[0] - tol) <= tgt && tgt <= (v[1] + tol))) r.problems.push('value fork [' + v[0] + ',' + v[1] + '] does not contain ' + tgt + ' ±' + tol);
      }
      if (r.problems.length) r.status = 'FAIL';
    } else if (spec.kind === 'K.j5Reading') {
      const p = spec.params;
      const call = safeCall(() => K.j5Reading(p));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.j5Reading threw: ' + call.err); return r; }
      saveProto(id, call.value);
      const exp = spec.expect;
      if (call.value.reading !== exp.reading) r.problems.push('reading=' + call.value.reading);
      if (call.value.sign !== exp.sign) r.problems.push('sign=' + call.value.sign);
      if (exp.contact_class && call.value.contact_class !== exp.contact_class) r.problems.push('contact_class=' + call.value.contact_class);
      if (exp.epsilon_range) {
        const e = call.value.epsilon;
        if (!(e >= exp.epsilon_range[0] && e <= exp.epsilon_range[1])) r.problems.push('epsilon=' + e);
      }
      if (r.problems.length) r.status = 'FAIL';
    } else if (spec.kind === 'K.j5Graph') {
      const p = spec.params_from ? expected.tests[spec.params_from].params : spec.params;
      const call = safeCall(() => K.j5Graph(p));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.j5Graph threw: ' + call.err); return r; }
      saveProto(id, call.value);
      const exp = spec.expect;
      const j5 = j5Record(call.value) || call.value;
      const canon = get(j5, 'canon.verdict');
      const ext = get(j5, 'ext.verdict');
      if (exp['j5.canon.verdict'] && exp['j5.canon.verdict'].indexOf(canon) < 0)
        r.problems.push('canon=' + canon + ' expected ' + exp['j5.canon.verdict'].join('/'));
      if (exp['j5.ext.verdict'] && exp['j5.ext.verdict'].indexOf(ext) < 0)
        r.problems.push('ext=' + ext + ' expected ' + exp['j5.ext.verdict'].join('/'));
      if (r.problems.length) r.status = 'FAIL';
    } else if (spec.kind === 'K.validate') {
      const call = safeCall(() => K.validate(spec.params.constructed));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.validate threw: ' + call.err); return r; }
      if (!Array.isArray(call.value) || call.value.length === 0) {
        r.status = 'FAIL'; r.problems.push('K.validate returned empty on PASSED+SAMPLED');
      }
    } else if (spec.kind === 'MY_CONFIG_VALIDATOR') {
      const errs = CV.check(spec.params.constructed);
      if (errs.length === 0) { r.status = 'FAIL'; r.problems.push('my config-validator missed PASSED+SAMPLED'); }
    } else if (spec.kind === 'K.minimize') {
      const p = spec.params;
      const x0 = p.x0_num / p.x0_den;
      const f = (x) => {
        const dx = x - x0;
        if (Math.abs(dx) > 1 / 65536) return [0, 0];
        const v = -1 + Math.abs(dx) * 65536;
        return [v, v];
      };
      const call = safeCall(() => K.minimize({ f, a: p.a, b: p.b, L: p.L, periodic: p.periodic }));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.minimize threw: ' + call.err); return r; }
      saveProto(id, call.value);
      const minv = call.value.min !== undefined ? call.value.min :
                   (call.value.min_value !== undefined ? call.value.min_value : call.value.value);
      if (!Array.isArray(minv) || !(minv[0] <= -1 + 1e-12 && minv[1] >= -1 - 1e-12))
        r.problems.push('min fork ' + JSON.stringify(minv) + ' does not contain -1');
      const argmin = call.value.argmin || call.value.min_points || call.value.points;
      let x0Found = false;
      if (Array.isArray(argmin)) {
        for (const pnt of argmin) if (Array.isArray(pnt) && pnt[0] - 1e-12 <= x0 && x0 <= pnt[1] + 1e-12) { x0Found = true; break; }
      } else if (argmin && typeof argmin === 'object') {
        for (const k of Object.keys(argmin)) {
          const pnt = argmin[k];
          if (Array.isArray(pnt) && pnt[0] - 1e-12 <= x0 && x0 <= pnt[1] + 1e-12) { x0Found = true; break; }
        }
      }
      if (!x0Found) r.problems.push('argmin/min_points do not contain x0=' + x0);
      if (r.problems.length) r.status = 'FAIL';
    } else {
      r.status = 'ERROR'; r.problems.push('unknown kind ' + spec.kind);
    }
  } catch (e) {
    r.status = 'ERROR'; r.problems.push(String(e && e.stack || e));
  }
  return r;
}

function runComposite(id) {
  const r = { id, status: 'PASS', problems: [], sub: [] };
  if (id === 'Kλ1') {
    const expectD = {0: 2.0, 30: 1.8660254, 60: 1.5, 75: 1.2588190, 85: 1.0871557};
    for (const th of [0, 30, 60, 75, 85]) {
      const c = { id: 'Kλ1_' + th, thread: { n: 2, links: [{theta: th, phi: 90, delta: 0}, {theta: 0, phi: 0, delta: 0}] }, hangs: [] };
      const call = safeCall(() => K.run(c));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.run threw θ=' + th + ': ' + call.err); continue; }
      const dCheck = findCheck(call.value.checks, {req: 'G-3'}) || findCheck(call.value.checks, {quantity: 'd'});
      if (!dCheck || !Array.isArray(dCheck.value)) {
        r.sub.push({ theta: th, status: 'FAIL', reason: 'no G-3/d check' });
        r.status = 'FAIL';
        continue;
      }
      const inside = expectD[th] >= dCheck.value[0] - 1e-9 && expectD[th] <= dCheck.value[1] + 1e-9;
      r.sub.push({ theta: th, expected_d: expectD[th], d_fork: dCheck.value, inside });
      if (!inside) r.status = 'FAIL';
    }
    return r;
  }
  if (id === 'Kλ3') {
    // Per D-2 rev16 — check ALL cusp records across ALL rings in each case, not one per case.
    for (const cname of ['A1','A2i','A2ii','A2iii','A3','A4']) {
      const caseData = loadCase(cname);
      const call = safeCall(() => K.run(caseData));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.run threw ' + cname + ': ' + call.err); continue; }
      const allCusp = (call.value.checks || []).filter(isCuspCheck);
      if (allCusp.length === 0) {
        r.sub.push({ case: cname, status: 'FAIL', reason: 'no kappa_margin records in checks[]' });
        r.status = 'FAIL';
        continue;
      }
      for (const rec of allCusp) {
        const recInfo = { case: cname, objects: rec.objects || [] };
        const v = rec.kappa_r !== undefined ? rec.kappa_r : rec.value;
        let krHi;
        if (Array.isArray(v)) krHi = v[1];
        else if (typeof v === 'number') krHi = v;
        else { r.sub.push(Object.assign({}, recInfo, { status: 'FAIL', reason: 'kappa_r not number/fork' })); r.status = 'FAIL'; continue; }
        const kappa = 2 - krHi;
        if (krHi >= 2) { r.sub.push(Object.assign({}, recInfo, { kappa_r: v, status: 'FAIL', reason: 'κ_r ≥ 2' })); r.status = 'FAIL'; continue; }
        if (kappa < 0.05) { r.sub.push(Object.assign({}, recInfo, { kappa_r: v, status: 'FAIL', reason: 'κ < κ_min' })); r.status = 'FAIL'; continue; }
        const cuspComp = get(rec, 'cusp.completeness') || rec.completeness;
        if (!['EXACT', 'CERTIFIED'].includes(cuspComp)) {
          r.sub.push(Object.assign({}, recInfo, { kappa_r: v, completeness: cuspComp, status: 'FAIL' }));
          r.status = 'FAIL';
          continue;
        }
        r.sub.push(Object.assign({}, recInfo, { kappa_r: v, completeness: cuspComp, status: 'PASS' }));
      }
    }
    return r;
  }
  if (id === 'm3i') {
    for (const p of ['m3i-A','m3i-B','m3i-C','m3i-D','m3i-E']) {
      const caseData = loadCase(p);
      const call = safeCall(() => K.run(caseData));
      if (!call.ok) { r.status = 'ERROR'; r.problems.push('K.run threw ' + p + ': ' + call.err); continue; }
      const contacts = call.value.contacts || [];
      const gap = contacts[0] && contacts[0].gap;
      if (!Array.isArray(gap)) { r.sub.push({ phase: p, status: 'FAIL', reason: 'no gap' }); r.status = 'FAIL'; continue; }
      const contains = gap[0] - 1e-15 <= -0.002 && gap[1] + 1e-15 >= -0.002;
      const hiNeg = gap[1] < 0;
      r.sub.push({ phase: p, gap, hi_negative: hiNeg, contains_minus_0_002: contains });
      if (!hiNeg || !contains) r.status = 'FAIL';
    }
    return r;
  }
  r.status = 'ERROR'; r.problems.push('unknown composite ' + id);
  return r;
}

function main() {
  const results = [];
  for (const id of Object.keys(expected.tests)) {
    if (id === 'm3i' || id === 'Kλ1' || id === 'Kλ3') results.push(runComposite(id));
    else results.push(runTest(id, expected.tests[id]));
  }
  fs.writeFileSync(path.join(OUT, 'd3_results.json'), JSON.stringify({
    meta: expected.meta, results, mutants: expected.mutants, run_date: new Date().toISOString()
  }, null, 2));
  const n = results.length;
  const passed = results.filter(r => r.status === 'PASS').length;
  const failed = results.filter(r => r.status === 'FAIL').length;
  const errors = results.filter(r => r.status === 'ERROR').length;
  console.log('d3_results: ' + n + '; PASS=' + passed + ' FAIL=' + failed + ' ERROR=' + errors);
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

