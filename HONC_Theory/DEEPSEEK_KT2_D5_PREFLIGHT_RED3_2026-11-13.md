# Д-5 ред. 3 — карточки эталонов КТ-2 (текст Дипсика_А, 13.11.2026)

> Архивная копия: три части сдачи Дипсика_А от 13.11.2026, как переслал Автор. Текст между заголовками частей не изменён. Зафиксировано 13.11 как спецификация ожиданий отдела (не слепой сертификат).

### FILE: d5/DEEPSEEK_KT2_D5_CARDS.md (редакция 3, часть 1/3)

```markdown
# Д-5 — карточки эталонов КТ-2 (редакция 3)

**Задание:** `DEEPSEEK_KT2_D5_ORDER_2026-11-12.md`
**Материалы:** `DEEPSEEK_KT2_D5_MATERIALS_2026-11-12.md`
**Решения по пробелам:** `DEEPSEEK_KT2_D5_GAPS_DECISIONS_2026-11-12.md`
**Preflight ч.1–2 ред.2:** `DEEPSEEK_KT2_D5_PREFLIGHT_FINAL_PARTS1-2_2026-11-12.md`
**Preflight ч.3 ред.2:** `DEEPSEEK_KT2_D5_PREFLIGHT_FINAL_PART3_2026-11-12.md`
**Preflight ред. 2:** `DEEPSEEK_KT2_D5_PREFLIGHT_RED2_2026-11-13.md`
**Интерфейс:** `HONC_Qf_R1_KT2_Interface_v7.1_2026-11-13.md` (FIXED 13.11) — изменения к `HONC_Qf_R1_KT2_Interface_v7_2026-11-12.md` (FIXED 12.11)
**Рамка:** `HONC_Qf_R1_KT2_TASK_FRAME_2026-11-12.md`
**Дата:** 13.11.2026

## Соглашения

- `ref` — дословная цитата источника; `src` — файл, раздел, строка.
- `tol_src` — откуда допуск; без допуска — правило округления (полуоткрытый до последнего разряда).
- **Классы — по плану § 6.1:** Э-А (закрытая форма, тождество, симметрия); Э-Н (независимый метод); Э-М (метаморфный); Э-С (синтетический с известным ответом); Э-П (прежнее ядро). Для А-6, А-7, Б-4, Б-6, Б-7 — по плану § 6.2 (М-11).
- **Научный статус** ([Д]/[Д-Кл]/[Г]) — из источника. Правила интерфейса — не научный статус, метка «—».
- **Направление навеса** — интерфейс v6, § 2 (М-14); в v7 и v7.1 не менялось: `e = s·e_x·cos ρ + (−e_z·cos ψ + e_y·sin ψ)·sin ρ`. При прямой нити (e_x = x̂, e_y = ŷ, e_z = ẑ), ψ = 0: e = s·cos ρ·x̂ − sin ρ·ẑ; T_h·e = 0; d = 2 по G-3.
- **Геометрия и J5 — раздельно.** J5 в `verdict.geometry` не входит.
- **Цикл J5 ≠ цепь латчеров** (состояние § 3.11). `CONTACT-ONLY` = только условие J5.
- **Итоги раздельно:** (1) геометрия; (2) J5-CANON/EXT; (3) топология — LINK/CONTACT-ONLY; (4) касания — существование и метка.
- **ρ = 0** — валидный вход (v7.1 § 2), `psi_ignored: true`.
- **Синтетика** (v6, § 4.3; v7, § 1, п. 6): `tori` непусто; оси `sameAs`/`oppositeOf`; `declare type`; E1/E2 ортонормированы; координаты 17 значащих.
- Ссылки на правила — «интерфейс v7.1» (пункты v7 сохранены).
- Значений ядра нет.

---

## К5 — гребёнка

### K5-POS-transverse

**1.** Гребёнка поперечно, стороны +,+. Требования: G-4, G-5, R-3, K-6, А-6.

**2. Построение.**

```json
{"id":"K5-POS-transverse","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0},{"host":2,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0},{"host":3,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0}]}
```

H_k = (2, 0, 2k); d(H1,H2) = d(H2,H3) = 2.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| d_H–H = 2 | М-6 (§2.10 К5): «Касания навес–навес на расстоянии 2» | 10⁻⁹ / §2.11 А-6 | Э-А | [Д] |
| IMPOSED (H–H) | М-6: «при поперечной гребёнке — `IMPOSED` по симметрии переноса»; П-8(г), v7.1 § 3 | — | Э-А | [Д] |
| R-3 EXACT | М-6: «R-3 `EXACT`» | — | Э-А | [Д] |
| J5-CANON: PASSED | М-6: «Лестница: `J5-CANON: PASSED`» | — | Э-С | [Д] |
| J5-EXT: PASSED-EXT | спец. K-6 (М-2) | — | Э-А | [Г, мост] |

**4. Итоги.**

- **Геометрия:** `PASSED`.
- **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`.
- **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k); H_k–H_{k+1} — CONTACT-ONLY.
- **Касания:** все IMPOSED (П-8(а)/П-8(г)).

**5. Контроль.** Ложный `UNRESOLVED`: H–H без П-8(г) — CANDIDATE.

---

### K5-POS-uniform-shift

**1.** Равномерный сдвиг: ρ = 5° у всех трёх навесов. Требования: G-4, K-6.

**2. Построение.**

```json
{"id":"K5-POS-uniform-shift","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":5,"psi":0,"delta":0},{"host":2,"side":1,"coords":"rho-psi","rho":5,"psi":0,"delta":0},{"host":3,"side":1,"coords":"rho-psi","rho":5,"psi":0,"delta":0}]}
```

e = cos5°·x̂ − sin5°·ẑ; d = 2; H_k = A_k + 2e; ΔH = (0,0,2) ⊥ оси ŷ; зазор H–H = 0.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| касания сохраняются | М-8 (§7.1): «Равномерный сдвиг сохраняет касания» | — | Э-М | [Д-Кл] |
| d_H–H = 2 | то же | 10⁻⁹ | Э-А | [Д] |
| IMPOSED | v7.1 § 3, П-8(г) | — | Э-А | — |

**4.** Геометрия PASSED; J5 PASSED/PASSED-EXT; топология и касания — как transverse.

**5.** Ложный `UNRESOLVED`: если П-8(г) требует строго ρ = 0.

---

### K5-POS-K4-node

**1.** Узел К4 на хозяевах 1, 2, 3, «все вверх и через один». Требования: G-4, K-6, B-4.

**2. Построение.**

```json
{"id":"K5-POS-K4-node","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":null,"psi":54,"delta":10,"fix":{"kind":"contact","free":"rho","with":"T0","bracket":[57.0,57.5]}},{"host":2,"side":1,"coords":"rho-psi","rho":null,"psi":306,"delta":-10,"fix":{"kind":"contact","free":"rho","with":"T1","bracket":[57.0,57.5]}},{"host":3,"side":1,"coords":"rho-psi","rho":null,"psi":54,"delta":10,"fix":{"kind":"contact","free":"rho","with":"T2","bracket":[57.0,57.5]}}]}
```

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| статически допустим, касаний H–H нет | М-8 (§7.1 К5): «Узел К4 на всех хозяевах … статически допустим, касаний навес–навес нет» | — | Э-А | [Д-Кл] |
| J5-CANON: UNRESOLVED | М-6 (§2.10 К4); М-7 (§2.11 Б-2) | — | Э-С | [Д] |
| J5-EXT: PASSED-EXT | спец. K-6 (М-2) | — | Э-А | [Г, мост] |

**Геометрия по интерфейсу v7.1 — для каждой пары RH.**

- **RH1–RH2** (hosts 1, 2; ψ = 54, 306; δ = 10, −10; ρ один через `fix` с T0, T1, одна вилка). Проверка П-9(в):
  - В1: hosts 1, 2 в цепочке θ=0, δ=0; T0, T1 — в цепочке. ✓
  - В2: s = +1, +1. ✓
  - В3: coords rho-psi, `fix` на ρ. ✓
  - В4: ψ + ψ′ = 54 + 306 = 360 ≡ 0 (mod 360°) точно. ✓
  - В5: δ′ = −δ = −10. ✓
  - В6: `fix` с T0, T1 при одной вилке. ✓
  - **Применимо.** ρ ≈ 57,26° ≠ 90° → `parallel-distinct`, R-3 EXACT.
  - **Ожидаемая запись:** `case: "parallel-distinct"`, `plane_relation_basis {rule: "П-9в", premises}`, R-3, EXACT, PASSED.
- **RH2–RH3** (hosts 2, 3; ψ = 306, 54; δ = −10, 10; `fix` с T1, T2). Симметрично RH1–RH2. **П-9(в) применимо.** R-3 EXACT.
- **RH1–RH3** (hosts 1, 3; ψ = 54, 54; δ = 10, 10; `fix` с T0, T2, одна вилка). Проверка П-9(а):
  - hosts 1, 3 связаны цепочкой θ=0, δ=0; T0, T2 — в цепочке. ✓
  - сторона, coords, параметры (ρ, ψ, δ) одинаковые: s=1, rho-psi, ψ=54, δ=10. ✓
  - `fix` с T0, T2, одна вилка. ✓
  - **Применимо.** R-3, EXACT, PASSED.

**Все пары RH → R-3 EXACT. Ожидаемая геометрия: `PASSED`.** Совпадает с источником — REFERENCE NOTE не требуется.

**4. Итоги.**

- **Геометрия:** `PASSED`.
- **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: PASSED-EXT`.
- **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k, IMPOSED через `fix`, П-8(б)); T_{k−1}–H_k — CONTACT-ONLY; H–H рёбер нет.
- **Касания:** T_k–T_{k+1} IMPOSED (П-8(а)); T_k–H_k — LINK, IMPOSED (П-8(а)); T_{k−1}–H_k — CONTACT-ONLY, IMPOSED через `fix` (П-8(б)); H–H SEPARATED.

**5. Контроль.** Ложный `PASSED` по J5: если рёбра T_{k−1}–H_k и T_k–H_k считать каноническими — у них оси непараллельны, их чтение только расширение (K-3). Ложный `FORBIDDEN`: если ∏g ошибочно −1.

---

### K5-NEG-single-deviation

**1.** Одиночное отклонение в плоскости. Требования: G-5а, А-6.

**2. Построение.**

```json
{"id":"K5-NEG-single-deviation","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0},{"host":2,"side":1,"coords":"rho-psi","rho":5,"psi":0,"delta":0},{"host":3,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0}]}
```

H2 = (2cos5°, 0, 4 − 2sin5°) ≈ (1.99239, 0, 3.82569). |H2−H1| ≈ 1.825 < 2 (PENETRATION); |H2−H3| ≈ 2.173 > 2.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| FORBIDDEN (геометрия) | М-7 (А-6): «одиночное отклонение в плоскости — `FORBIDDEN`» | — | Э-А (G-4 PENETRATION) | [Д] |
| PENETRATION H1–H2; SEPARATED H2–H3 | М-8: «сразу входит в соседний навес» | — | Э-А | [Д-Кл] |

**4. Итоги.**

- **Геометрия:** `FORBIDDEN` (PENETRATION H1–H2).
- **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`. Запрет геометрический, не J5: H1–H2 не касание (проникновение) — ребра в графе нет; граф — дерево.
- **Топология:** LINK T_k–T_{k+1}, T_1–H_1, T_2–H_2, T_3–H_3; H1–H2, H2–H3 рёбер нет.
- **Касания:** H1–H2 PENETRATION; H2–H3 SEPARATED; остальные IMPOSED.

**5. Контроль.** Ложный `PASSED`: если PENETRATION H1–H2 не найден.

---

### K5-NEG-band-30

**1.** Треугольная лента при 30° — гребёнка при ρ = 30°. Требования: K-6, B-4.

**2. Построение.**

```json
{"id":"K5-NEG-band-30","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":null,"psi":0,"delta":0,"fix":{"kind":"contact","free":"rho","with":"T0","bracket":[29.5,30.5]}},{"host":2,"side":1,"coords":"rho-psi","rho":null,"psi":0,"delta":0,"fix":{"kind":"contact","free":"rho","with":"T1","bracket":[29.5,30.5]}},{"host":3,"side":1,"coords":"rho-psi","rho":null,"psi":0,"delta":0,"fix":{"kind":"contact","free":"rho","with":"T2","bracket":[29.5,30.5]}}]}
```

При ρ = 30°: e = (√3/2, 0, −1/2); H_k = A_k + (√3, 0, −1).

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| геометрия `PASSED` | спец. §2.10 К3: «структура: касание с предыдущим тором — `IMPOSED`, статически допустимо» | — | Э-А | [Д] |
| J5-CANON: FORBIDDEN | М-6 (§2.10 К5): «лента при 30°: `FORBIDDEN`»; М-7 (Б-4) | — | Э-С | [Д] |

**4. Итоги.**

- **Геометрия:** `PASSED`.
- **J5:** `J5-CANON: FORBIDDEN`; `J5-EXT: FORBIDDEN-EXT`.
- **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k); T_{k−1}–H_k — CONTACT-ONLY; H_k–H_{k+1} — CONTACT-ONLY.
- **Касания:** T_{k−1}–H_k IMPOSED (П-8(б)); H_k–H_{k+1} IMPOSED (П-8(г)).

**5. Контроль.** Ложный `PASSED` по J5: ∏g ошибочно +1. Ложный `FORBIDDEN` по геометрии: касание H_k–H_{k+1} ошибочно классифицировано как PENETRATION.

---

### K5-UNRESOLVED-B8

**1.** Аналог Б-8 — гребёнка при ρ = 30° числом, без `fix`. Требования: K-1, Б-8.

**2. Построение.**

```json
{"id":"K5-UNRESOLVED-B8","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":30,"psi":0,"delta":0},{"host":2,"side":1,"coords":"rho-psi","rho":30,"psi":0,"delta":0},{"host":3,"side":1,"coords":"rho-psi","rho":30,"psi":0,"delta":0}]}
```

H_k = A_k + (√3, 0, −1); |H_k − A_{k−1}| = |(√3, 0, 1)| = 2 — аналитический ноль, но не установлен (без `fix`).

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| геометрия `UNRESOLVED` | М-1 (K-1): «разошлись — `UNRESOLVED`» | — | Э-С | [Д] |
| CANDIDATE (T_{k−1}–H_k) | М-1: «`CANDIDATE` в него автоматически не входит»; v6 § 4.2 | — | Э-С | [Д] |
| J5-CANON: UNRESOLVED | М-1 | — | Э-С | [Д] |

**4. Итоги.**

- **Геометрия:** `UNRESOLVED`.
- **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: UNRESOLVED`.
- **Топология:** LINK T_k–T_{k+1}, T_k–H_k; H_k–H_{k+1} — CONTACT-ONLY, IMPOSED (П-8(г)); T_{k−1}–H_k CANDIDATE (k=1..3).
- **Касания:** T_{k−1}–H_k CANDIDATE; остальные IMPOSED.

**5. Контроль.** Ложный `PASSED`/`FORBIDDEN`: если CANDIDATE свёрнут в одну ветвь.

---

**Конец части 1/3.**
```

**Следующая — часть 2/3: К6 (4 карточки) и Кλ5 (4 карточки).**
---
### FILE: d5/DEEPSEEK_KT2_D5_CARDS.md (редакция 3, часть 2/3)

```markdown
## К6 — чередование

### K6-POS-alternating

**1.** Чередование, стороны +,−,+. Требования: G-4, G-5, K-6, А-7.

**2. Построение.**

```json
{"id":"K6-POS-alternating","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0},{"host":2,"side":-1,"coords":"rho-psi","rho":0,"psi":0,"delta":0},{"host":3,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0}]}
```

H1 = (2, 0, 2); H2 = (−2, 0, 4); H3 = (2, 0, 6). d(H1,H2) = √20 ≈ 4.472136; d(H2,H3) = √20; d(H1,H3) = 4.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| d(H1,H2) = √20 ≈ 4.472136 | М-7 (А-7): «Касаний навес–навес нет (≈ 4,47)» | 10⁻⁹ / §2.11 А-7 | Э-А | [Д] |
| SEPARATED | М-6 (К6): «`SEPARATED` (≈ 4,47) — `CERTIFIED`» | — | Э-А | [Д] |
| граф — дерево | М-8 (§7.1 К6): «граф — дерево; отклонения независимы» | — | Э-С | [Д-Кл] |
| J5-CANON: PASSED | М-6 (К6): «Дерево: `J5-CANON: PASSED`» | — | Э-С | [Д] |
| J5-EXT: PASSED-EXT | спец. K-6 (М-2) | — | Э-А | [Г, мост] |
| пары колец навесов RH1–RH2, RH2–RH3, RH1–RH3 — R-3 `EXACT` | интерфейс v7, § 7, п. 4 — чтение строки § 2.10 К6 | — | Э-А | — |

**4. Итоги.**

- **Геометрия:** `PASSED`; пары колец навесов — R-3 EXACT по П-9(б) (все ρ=0, плоскости z=2,4,6 попарно параллельны, расстояния 2, 2, 4).
- **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`.
- **Топология:** LINK T_k–T_{k+1}, T_k–H_k; H–H рёбер нет.
- **Касания:** T_k–T_{k+1}, T_k–H_k IMPOSED; H–H SEPARATED.

**5. Контроль.** Ложный `FORBIDDEN`: если sides не учтены — H1–H2 касание, 4-цикл.

---

### K6-NEG-synthetic-odd

**1.** Синтетический нечётный 3-цикл. Требования: K-6, B-4.

**2. Построение.**

```json
{"id":"K6-NEG-synthetic-odd","tori":[{"name":"Ta","A":[0,0,0],"T":[0,1,0]},{"name":"Tb","A":[2,0,0],"T":{"sameAs":"Ta"}},{"name":"Tc","A":[1,0,1.7320508075688772],"T":{"sameAs":"Ta"}}],"declare":[{"kind":"symmetry","pair":["Ta","Tb"],"contact":"IMPOSED","basis":"triangle-17digits"},{"kind":"symmetry","pair":["Tb","Tc"],"contact":"IMPOSED","basis":"triangle-17digits"},{"kind":"symmetry","pair":["Tc","Ta"],"contact":"IMPOSED","basis":"triangle-17digits"},{"kind":"type","pair":["Ta","Tb"],"type":"SIDE","basis":"triangle-declared"},{"kind":"type","pair":["Tb","Tc"],"type":"SIDE","basis":"triangle-declared"},{"kind":"type","pair":["Tc","Ta"],"type":"SIDE","basis":"triangle-declared"}]}
```

|Ta−Tb| = 2; |Tb−Tc| = |(−1,0,1.73205…)| = 2; |Tc−Ta| = 2.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| знак каждого ребра −1 | Э-А: при одинаковых осях и боковом касании v_B = −v_A | — | Э-А | [Д] |
| ∏g = −1 (3-цикл) | М-9 (Кλ5): «синтетический нечётный цикл … даёт −1» | — | Э-С | [Д] |
| J5-CANON: FORBIDDEN | М-7 (Б-4): «синтетический нечётный цикл — `FORBIDDEN`» | — | Э-С | [Д] |

**4. Итоги.**

- **Геометрия:** `PASSED`.
- **J5:** `J5-CANON: FORBIDDEN`; `J5-EXT: FORBIDDEN-EXT`.
- **Топология:** 3 CONTACT-ONLY ребра в 3-цикле.
- **Касания:** 3 IMPOSED (declare).

**5. Контроль.** Ложный `PASSED`: если 3-цикл не замечен как цикл.

---

### K6-UNRESOLVED

**1.** Аналог Б-8: чередование с ρ = 30° числом, без `fix`. Требования: K-1, K-6.

**2. Построение.**

```json
{"id":"K6-UNRESOLVED","thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":30,"psi":0,"delta":0},{"host":2,"side":-1,"coords":"rho-psi","rho":30,"psi":0,"delta":0},{"host":3,"side":1,"coords":"rho-psi","rho":30,"psi":0,"delta":0}]}
```

По М-14 (ρ = 30°, ψ = 0):
- host 1 (s=+1): e = (√3/2, 0, −1/2); A_H1 = (√3, 0, 1).
- host 2 (s=−1): e = (−√3/2, 0, −1/2); A_H2 = (−√3, 0, 3).
- host 3 (s=+1): e = (√3/2, 0, −1/2); A_H3 = (√3, 0, 5).

**Проверка касания с предыдущим тором:**
- H1–T0: |(√3, 0, 1) − (0, 0, 0)| = |(√3, 0, 1)| = 2.
- H2–T1: |(−√3, 0, 3) − (0, 0, 2)| = |(−√3, 0, 1)| = 2.
- H3–T2: |(√3, 0, 5) − (0, 0, 4)| = |(√3, 0, 1)| = 2.

У всех трёх — аналитический ноль, но без `fix` не установлен (П-7 не применим) → `CANDIDATE`.

**Расстояния навес–навес:**
- |H1−H2| = |(2√3, 0, −2)| = 4. SEPARATED.
- |H2−H3| = |(−2√3, 0, −2)| = 4. SEPARATED.
- |H1−H3| = |(0, 0, −4)| = 4. SEPARATED.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| CANDIDATE (T_{k−1}–H_k) | М-1 (K-1): «`CANDIDATE` в него автоматически не входит»; v6 §4.2 | — | Э-С | [Д] |
| J5-CANON: UNRESOLVED | М-1: «разошлись — `UNRESOLVED`» | — | Э-С | [Д] |

**4. Итоги.**

- **Геометрия:** `UNRESOLVED`.
- **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: UNRESOLVED`.
- **Топология:** LINK T_k–T_{k+1}, T_k–H_k; T_{k−1}–H_k CANDIDATE; H–H рёбер нет.
- **Касания:** T_{k−1}–H_k CANDIDATE (k=1..3); T_k–T_{k+1}, T_k–H_k IMPOSED (П-8(а)); H–H SEPARATED.

**5. Контроль.** Ложный `PASSED`/`FORBIDDEN`: если CANDIDATE свёрнут в одну ветвь.

---

## Кλ5 — плоские замкнутые цепи (β = 0), без колец

### Kλ5-W-even

**1.** W, N = 4. Требования: K-6, B-4, М-9.

**2. Построение.**

```json
{"id":"Kλ5-W-even","tori":[{"name":"T1","A":[0,0,0],"T":[0,1,0]},{"name":"T2","A":[2,0,0],"T":{"sameAs":"T1"}},{"name":"T3","A":[2,0,2],"T":{"sameAs":"T1"}},{"name":"T4","A":[0,0,2],"T":{"sameAs":"T1"}}],"declare":[{"kind":"symmetry","pair":["T1","T2"],"contact":"IMPOSED","basis":"square-side-2"},{"kind":"symmetry","pair":["T2","T3"],"contact":"IMPOSED","basis":"square-side-2"},{"kind":"symmetry","pair":["T3","T4"],"contact":"IMPOSED","basis":"square-side-2"},{"kind":"symmetry","pair":["T4","T1"],"contact":"IMPOSED","basis":"square-side-2"},{"kind":"type","pair":["T1","T2"],"type":"SIDE","basis":"square-declared"},{"kind":"type","pair":["T2","T3"],"type":"SIDE","basis":"square-declared"},{"kind":"type","pair":["T3","T4"],"type":"SIDE","basis":"square-declared"},{"kind":"type","pair":["T4","T1"],"type":"SIDE","basis":"square-declared"}]}
```

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| ∏g = +1 (N = 4) | М-9 (Кλ5): «∏g = +1 на цикле» | — | Э-С + Э-П | [Д] |
| J5-CANON: PASSED | М-7 (Б-4): «чётные циклы — `J5-CANON: PASSED`» | — | Э-С + Э-П | [Д] |

**4.** Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 4 CONTACT-ONLY; касания 4 IMPOSED.

**5.** Ложный `FORBIDDEN`: ∏g ошибочно −1.

---

### Kλ5-Gluon-even

**1.** Глюон, N = 8. Требования: K-6, B-4, М-9.

**2. Построение.**

```json
{"id":"Kλ5-Gluon-even","tori":[{"name":"T0","A":[2.6131259297527530,0,0],"T":[0,1,0]},{"name":"T1","A":[1.8477590650225735,0,1.8477590650225735],"T":{"sameAs":"T0"}},{"name":"T2","A":[0,0,2.6131259297527530],"T":{"sameAs":"T0"}},{"name":"T3","A":[-1.8477590650225735,0,1.8477590650225735],"T":{"sameAs":"T0"}},{"name":"T4","A":[-2.6131259297527530,0,0],"T":{"sameAs":"T0"}},{"name":"T5","A":[-1.8477590650225735,0,-1.8477590650225735],"T":{"sameAs":"T0"}},{"name":"T6","A":[0,0,-2.6131259297527530],"T":{"sameAs":"T0"}},{"name":"T7","A":[1.8477590650225735,0,-1.8477590650225735],"T":{"sameAs":"T0"}}],"declare":[{"kind":"symmetry","pair":["T0","T1"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"symmetry","pair":["T1","T2"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"symmetry","pair":["T2","T3"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"symmetry","pair":["T3","T4"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"symmetry","pair":["T4","T5"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"symmetry","pair":["T5","T6"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"symmetry","pair":["T6","T7"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"symmetry","pair":["T7","T0"],"contact":"IMPOSED","basis":"octagon-side-2"},{"kind":"type","pair":["T0","T1"],"type":"SIDE","basis":"octagon-declared"},{"kind":"type","pair":["T1","T2"],"type":"SIDE","basis":"octagon-declared"},{"kind":"type","pair":["T2","T3"],"type":"SIDE","basis":"octagon-declared"},{"kind":"type","pair":["T3","T4"],"type":"SIDE","basis":"octagon-declared"},{"kind":"type","pair":["T4","T5"],"type":"SIDE","basis":"octagon-declared"},{"kind":"type","pair":["T5","T6"],"type":"SIDE","basis":"octagon-declared"},{"kind":"type","pair":["T6","T7"],"type":"SIDE","basis":"octagon-declared"},{"kind":"type","pair":["T7","T0"],"type":"SIDE","basis":"octagon-declared"}]}
```

**3. Ожидаемое.** Как W-even, но N = 8:
- ∏g = (+1)^8 = +1 → J5-CANON: PASSED;
- геометрия `PASSED`; топология 8 CONTACT-ONLY; касания 8 IMPOSED.

**4–5.** Как W-even.

---

### Kλ5-Synthetic-odd

**1.** 3-цикл — синтетический нечётный. Требования: K-6, B-4.

**2. Построение.** Вход: тот же JSON, что в `K6-NEG-synthetic-odd`, поле `id` = `Kλ5-Synthetic-odd`.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| ∏g = −1 | М-9 (Кλ5): «синтетический нечётный цикл … даёт −1» | — | Э-С | [Д] |
| J5-CANON: FORBIDDEN | М-7 (Б-4): «синтетический нечётный цикл — `FORBIDDEN`» | — | Э-С | [Д] |

**4.** Геометрия `PASSED`; J5 `FORBIDDEN`/`FORBIDDEN-EXT`; топология 3 CONTACT-ONLY; касания 3 IMPOSED.

**5.** Как в K6-NEG-synthetic-odd.

---

### Kλ5-Z-notapplicable

**1.** Z, N = 2 — документирующая. Требование: терминология §3.

**2. Построение.**

```json
{"id":"Kλ5-Z-notapplicable","tori":[{"name":"Za","A":[0,0,0],"T":[0,1,0]},{"name":"Zb","A":[2,0,0],"T":{"sameAs":"Za"}}],"rings":[{"name":"Q","C":[1,0,0],"E1":[0,1,0],"E2":[1,0,0],"s1":1,"s2":1,"threads":["Za","Zb"]}],"declare":[{"kind":"symmetry","pair":["Za","Zb"],"contact":"IMPOSED","basis":"Z-pair"},{"kind":"type","pair":["Za","Zb"],"type":"SIDE","basis":"Z-pair"}]}
```

Кольцо в плоскости z = 0 (span(ŷ, x̂)), касается ŷ в Za=(0,0,0) и в Zb=(2,0,0) (проверено: Q(3π/2) = (0,0,0), Q(π/2) = (2,0,0); касательные ∥ ŷ).

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| J5-CANON: PASSED (циклов нет) | интерфейс v7.1 (K-6); у Z одно ребро | — | Э-А | [Д] |
| Z — не Кλ5 (нет цикла J5) | Клод, ред.7 §1; терминология §3 | — | — | [Д] |

**4.** Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 1 LINK; касания IMPOSED.

**5.** Ложный `UNRESOLVED`: если ошибочно ищется цикл длины 2.

---

**Конец части 2/3.**
```

**Следующая — часть 3/3: A6, A7, B4, B6a/b/c, B7, m7, REFERENCE GAP (№7, №8 закрыты), «Нужно в интерфейсе», След источника.**
---
### FILE: d5/DEEPSEEK_KT2_D5_CARDS.md (редакция 3, часть 3/3)

```markdown
## Испытания — А-6, А-7, Б-4, Б-6, Б-7, м7

### A6-K5

**1.** Испытание А-6. Требования: G-4, G-5, R-3, A-6. Опирается на `K5-POS-transverse` и `K5-NEG-single-deviation` — часть 1.

**2. Построение.** См. `K5-POS-transverse` (положительная) и `K5-NEG-single-deviation` (запрещённая).

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| d_H–H = 2 | М-7 (А-6): «Расстояние навес–навес = 2» | 10⁻⁹ / §2.11 А-6 | Э-А | [Д] |
| R-3 EXACT | М-7 (А-6): «R-3 `EXACT`» | — | Э-А | [Д] |
| одиночное отклонение — FORBIDDEN | М-7 (А-6): «одиночное отклонение в плоскости — `FORBIDDEN`» | — | Э-А | [Д] |

**4. Итоги.**

- **Геометрия:** положительная — `PASSED`; одиночное — `FORBIDDEN`.
- **J5:** положительная — `J5-CANON: PASSED`; одиночное — `J5-CANON: PASSED` (проникновение не ребро; граф — дерево).
- **Топология:** положительная — LINK T_k–T_{k+1}, T_k–H_k; H–H CONTACT-ONLY; одиночное — H1–H2, H2–H3 рёбер нет.
- **Касания:** положительная — H–H IMPOSED (П-8(г)); одиночное — H1–H2 PENETRATION, H2–H3 SEPARATED.

**5. Контроль.** Ложный `FORBIDDEN` положительной: если H–H не IMPOSED → CANDIDATE → UNRESOLVED. Ложный `PASSED` одиночного: если PENETRATION H1–H2 не найден.

---

### A7-K6

**1.** Испытание А-7. Требования: G-4, K-6, A-7. Опирается на `K6-POS-alternating` — часть 2.

**2. Построение.** См. `K6-POS-alternating`.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| H–H касаний нет | М-7 (А-7): «Касаний навес–навес нет (≈ 4,47)» | 10⁻⁹ / §2.11 А-7 | Э-А (закрытая форма √20) | [Д] |

**4. Итоги.**

- **Геометрия:** `PASSED`.
- **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT` (спец. K-6, М-2).
- **Топология:** LINK T_k–T_{k+1}, T_k–H_k; H–H рёбер нет.
- **Касания:** H–H SEPARATED.

**5. Контроль.** Ложный `FORBIDDEN`: если sides не учтены.

---

### B4-Kλ5

**1.** Испытание Б-4: чётность J5 на циклах. Требования: K-6, B-4. Опирается на `Kλ5-W-even`, `Kλ5-Gluon-even`, `Kλ5-Synthetic-odd` — часть 2.

**2. Построение.** См. соответствующие карточки (плоские цепи β = 0, без колец).

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| чётные циклы — `J5-CANON: PASSED` | М-7 (Б-4): «чётные циклы — `J5-CANON: PASSED`» | — | Э-С + Э-П | [Д] |
| нечётный цикл — `J5-CANON: FORBIDDEN` | М-7 (Б-4): «синтетический нечётный цикл — `FORBIDDEN`» | — | Э-С + Э-П | [Д] |
| ∏g на цикле | М-9 (Кλ5): «∏g = +1 на цикле»; «…нечётный … даёт −1» | — | Э-С | [Д] |

**4. Итоги.**

- **Геометрия:** во всех трёх — `PASSED`.
- **J5:** W, глюон — `PASSED`/`PASSED-EXT`; синтетический нечётный — `FORBIDDEN`/`FORBIDDEN-EXT`.
- **Топология:** W — 4 CONTACT-ONLY; глюон — 8 CONTACT-ONLY; нечётный — 3 CONTACT-ONLY.
- **Касания:** все IMPOSED через `declare`.

**5. Контроль.** Ложный `FORBIDDEN` на чётном: ∏g ошибочно −1. Ложный `PASSED` на нечётном: 3-цикл не замечен.

---

### B6a-R2-static-meeting

**1.** Статическая встреча по R-2. Требование: R-2, Б-6.

**2. Построение.**

```json
{"id":"B6a-R2-static-meeting","tori":[{"name":"S1","A":[10,10,10],"T":[0,1,0]}],"rings":[{"name":"Q1","C":[0,0,0],"E1":[1,0,0],"E2":[0,0,1],"s1":1,"s2":1},{"name":"Q2","C":[1,1,0],"E1":[0,1,0],"E2":[0,0,1],"s1":1,"s2":1}]}
```

**Проверка:** Q1(0) = (1,0,0), Q2(π) = (1,0,0); других общих точек нет: Q1 пересекает плоскость x = 1 только в (1,0,0). Плоскости: Q1 нормаль ŷ, Q2 нормаль x̂; угол 90° > θ_min.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| contact_class = `UNRESOLVED CONTACT` | М-7 (Б-6): «Статическая встреча — `UNRESOLVED CONTACT` с локальным типом» | — | Э-С | [Д] |
| локальный тип встречи | М-3 (R-2): «с локальным типом встречи и индикаторами исходного класса пары» | — | Э-С | [Д] |

**4. Итоги.**

- **Геометрия:** R-2, `UNRESOLVED CONTACT`.
- **J5:** вне графа (синтетика без declare касания).
- **Топология:** нет рёбер.
- **Касания:** не IMPOSED — статика.

**5. Контроль.** Ложный `ALLOWED CONTACT` / `FORBIDDEN CROSSING`: источник явно различает статику (`UNRESOLVED CONTACT`) и событие пути (P-5).

---

### B6b-R5-near-parallel

**1.** Почти параллельные плоскости (угол < θ_min). Требование: R-5, Б-6.

**2. Построение.**

```json
{"id":"B6b-R5-near-parallel","tori":[{"name":"S1","A":[10,10,10],"T":[0,1,0]}],"rings":[{"name":"Q1","C":[0,0,0],"E1":[1,0,0],"E2":[0,0,1],"s1":1,"s2":1},{"name":"Q2","C":[0,0.1,0],"E1":[1,0,0],"E2":[0,0.008726535498373935,0.9999619230641713],"s1":1,"s2":1}]}
```

Угол между нормалями 0.5° < θ_min = 1°.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| UNRESOLVED (R-5) | М-7 (Б-6): «почти параллельные плоскости — `UNRESOLVED`» | — | Э-С | [Д] |

**4.** Геометрия — R-5 `UNRESOLVED`; остальное вне графа.

**5. Контроль.** Ложный `UNRESOLVED CONTACT`: если θ_min не проверяется, пара уходит в R-2.

---

### B6c-R6-three-rings

**1.** Три кольца в одной точке вне каспа (R-6). Требование: R-6, Б-6.

**2. Построение.**

```json
{"id":"B6c-R6-three-rings","tori":[{"name":"S1","A":[10,10,10],"T":[0,1,0]}],"rings":[{"name":"Q1","C":[0,0,0],"E1":[1,0,0],"E2":[0,0,1],"s1":1,"s2":1},{"name":"Q2","C":[1,1,0],"E1":[0,1,0],"E2":[0,0,1],"s1":1,"s2":1},{"name":"Q3","C":[2,0,0],"E1":[1,0,0],"E2":[0,1,0],"s1":1,"s2":1}]}
```

**Проверка:** Q1(0) = Q2(π) = Q3(π) = (1,0,0); плоскости y = 0, x = 1, z = 0 попарно перпендикулярны; каждая пара колец имеет одну общую точку — (1,0,0).

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| DEGENERATE MEETING | М-7 (Б-6): «три кольца в точке — `DEGENERATE MEETING`» | — | Э-С | [Д] |

**4.** Геометрия — R-6 `DEGENERATE MEETING`; J5 вне графа.

**5. Контроль.** Ложный `ALLOWED CONTACT`: источник явно «за событие защёлки не считать».

---

### B7-B1-property

**1.** Б-7 — свойство B-1 через `family`. Требование: B-1, Б-7.

**2. Построение.**

```json
{"id":"B7-B1-property","family":{"param":"hangs[1].rho","values":[0,5,10,15,20]},"thread":{"n":5,"links":[{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0},{"theta":0,"phi":0,"delta":0}]},"hangs":[{"host":1,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0},{"host":2,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0},{"host":3,"side":1,"coords":"rho-psi","rho":0,"psi":0,"delta":0}]}
```

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| `output.geometry: null` для FORBIDDEN | М-4 (B-1): «Запрещённая конфигурация не рисуется как геометрия» | — | Э-С (свойство) | [Д] |
| `output.family.first_stop` — ρ = 5° | интерфейс v7.1 §5 | — | Э-С | — |
| `output.family.last_admissible` — ρ = 0° (PASSED) | интерфейс v7.1 §5 | — | Э-С | — |
| ни одна конфигурация в `output.geometry` и `last_admissible` не имеет FORBIDDEN | М-4 | — | Э-С (свойство) | [Д] |

**4. Итоги.**

- **Геометрия (свойство):** `output.geometry = null` для FORBIDDEN; `last_admissible` = ρ = 0° (PASSED).
- **J5:** вне области.
- **Топология:** вне области.
- **Касания:** вне области.

**5. Контроль.** Ложный `PASSED`: если `output.geometry` не null для FORBIDDEN. `family` проверяет только перечисленные члены; о допустимости между ними ничего не утверждается (интерфейс v7.1, § 5: «это не путь»).

---

### m7-mutant

**1.** Мутант м7 (план §6.3): статическая встреча колец классифицируется как `ALLOWED CONTACT` вместо `UNRESOLVED CONTACT`. Ловится `B6a-R2-static-meeting`.

**2.** Не карточка; ссылка на B6a.

**3. Ожидаемое.**

| Метрика | src / ref | tol / tol_src | класс | статус |
|---|---|---|---|---|
| м7 ловится B6a | М-12 (м7): «Статическая встреча колец как `ALLOWED` … ловится Б-6» | — | — | [Д] |

**4.** На правильном ядре B6a — `UNRESOLVED CONTACT` (PASSED по ожиданию). На мутанте — `ALLOWED` (FAIL).

---

## REFERENCE GAP — итог

| № | Проблема | Статус |
|---|---|---|
| 1 | Основание касания навесов | Закрыт: П-8(г) (v7.1 § 3) |
| 2 | «Все вверх и через один» | Закрыт: hosts 1, 2, 3; К4, зеркальная пара, К4 — см. `K5-POS-K4-node` |
| 3 | Лента при 30° | Закрыт: `K5-NEG-band-30` — гребёнка при ρ = 30° через `fix` |
| 4 | Синтетический нечётный цикл | Закрыт: 17 значащих, `sameAs`, IMPOSED при вилке с 0 |
| 5 | W, глюон | Закрыт: β = 0, плоские цепи, без колец (CONTACT-ONLY) |
| 6 | Z как Кλ5 | Закрыт: документирующая карточка |
| 7 | Б-7 при N > 8 | Закрыт: свойство через `family` (`hangs[1].rho`) |
| 8 | «Узел К4 на всех хозяевах» | Закрыт чтением: hosts 1, 2, 3; К4, зеркальная пара, К4; геометрия по v7.1 — `PASSED` (совпадает с источником) |

---

## Нужно в интерфейсе

| № | Что | Статус |
|---|---|---|
| 1 | ρ = 0 с `psi_ignored: true` | есть (v7.1 § 2) |
| 2 | П-8(г) — касание навесов по переносу | есть (v7.1 § 3) |
| 3 | П-9(а) — перенос (v7.1, § 1); П-9(б) — общая рамка при ρ = 0 (v7, § 3) | есть |
| 4 | `output.geometry` / `output.admissible` / `output.family` | есть (v7.1 § 5) |
| 5 | `declare: type SIDE/AXIAL` | есть (v6 § 4.3) |
| 6 | `crosschecks[]` (R-7) | есть (v7.1 § 4) |
| 7 | `family` | есть (v7.1 § 5) |
| 8 | П-9(в) — зеркальный перенос | есть (v7.1, § 2) |

---

## След источника (preflight)

| Карточка | src (дословно) |
|---|---|
| K5-POS-transverse | М-6 §2.10 К5; М-7 §2.11 А-6 |
| K5-POS-uniform-shift | М-8 §7.1 |
| K5-POS-K4-node | М-8 §7.1; М-6 §2.10 К4; М-7 §2.11 Б-2; спец. А-4 (зерк. ψ=306°, δ=−10°); интерфейс v7.1 §1, §2 |
| K5-NEG-single-deviation | М-7 §2.11 А-6; М-8 §7.1 |
| K5-NEG-band-30 | М-6 §2.10 К5; М-7 §2.11 Б-4; М-8 §7.1; спец. §2.10 К3 |
| K5-UNRESOLVED-B8 | М-1 §2.2 K-1; v6 §4.2 |
| K6-POS-alternating | М-6 §2.10 К6; М-7 §2.11 А-7; М-8 §7.1; v7 §7 п.4 |
| K6-NEG-synthetic-odd | М-7 §2.11 Б-4; М-9 §7.2 |
| K6-UNRESOLVED | М-1 §2.2 K-1; v6 §4.2 |
| Kλ5-W-even | М-9 §7.2; М-7 §2.11 Б-4 |
| Kλ5-Gluon-even | М-9 §7.2; М-7 §2.11 Б-4 |
| Kλ5-Synthetic-odd | М-9 §7.2; М-7 §2.11 Б-4 |
| Kλ5-Z-notapplicable | М-17 [Д] + G10; терминология §3; Клод ред.7 §1 |
| A6-K5 | М-7 §2.11 А-6 |
| A7-K6 | М-7 §2.11 А-7 |
| B4-Kλ5 | М-7 §2.11 Б-4; М-9 §7.2; М-11 §6.2 |
| B6a-R2-static-meeting | М-7 §2.11 Б-6; М-3 §2.3 R-2 |
| B6b-R5-near-parallel | М-7 §2.11 Б-6; М-3 §2.3 R-5; М-13 θ_min |
| B6c-R6-three-rings | М-7 §2.11 Б-6; М-3 §2.3 R-6 |
| B7-B1-property | М-4 §2.6 B-1; М-7 §2.11 Б-7; М-8 §7.1 К7в; v7.1 §5 |
| m7-mutant | М-12 §6.3 м7; М-3 §2.3 R-2 |

---

`D-5 — RED.3 SUBMITTED` · `20 EDITS APPLIED` · `NO KERNEL VALUES` · `KT-1 KERNEL — FROZEN`
```

**Конец части 3/3. Редакция 3 полная — три части.**
