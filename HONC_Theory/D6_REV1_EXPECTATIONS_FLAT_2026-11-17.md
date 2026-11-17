# Д-6 rev1 — ожидания построчно, для рецензии Грока

**ОТ:** Клод_А · **КОМУ:** Грок · **Дата:** 17.11.2026

> Не для DeepSeek и не для кандидатов триады Б. Механическая развёртка `d6/expected.json` (`c68cba6a…`) из архива `079dc3a7…6657` в таблицу — без комментариев и оценок. Классы — из матрицы происхождения, § 2; составные тесты — GUIDED по матрице. Если строка таблицы расходится с JSON, верен JSON.

| № | тест / вход | класс (матрица) | что проверяется | ожидание | источник | цитата (дословно; «¦» = «\|» в оригинале) |
|---|---|---|---|---|---|---|
| 1 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | `verdict.geometry` | ["PASSED"] | K5-POS-transverse § 4, «Итоги. Геометрия» | **Геометрия:** `PASSED`. |
| 2 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | `j5.canon.verdict` | ["PASSED"] | K5-POS-transverse § 4, «Итоги. J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`. |
| 3 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | `j5.ext.verdict` | ["PASSED-EXT"] | K5-POS-transverse § 4, «Итоги. J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`. |
| 4 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | contacts: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3, H1–H2, H2–H3 · `existence` | "IMPOSED" | K5-POS-transverse § 4, «Итоги. Касания» | **Касания:** все IMPOSED (П-8(а)/П-8(г)). |
| 5 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | j5_edges: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `cls` | "LINK" | K5-POS-transverse § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k); H_k–H_{k+1} — CONTACT-ONLY. |
| 6 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | j5_edges: H1–H2, H2–H3 · `cls` | "CONTACT-ONLY" | K5-POS-transverse § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k); H_k–H_{k+1} — CONTACT-ONLY. |
| 7 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | число `gap_H1_H2`: {"k": "contact", "pair": ["H1", "H2"], "f": "gap"} | contains v=0 tol=1e-09 | K5-POS-transverse § 3, «d_H–H = 2»; G-4: d=2 → g=0 | Касания навес–навес на расстоянии 2 |
| 8 | `K5-POS-transverse` | BLIND-SOURCE (prov.) | число `gap_H2_H3`: {"k": "contact", "pair": ["H2", "H3"], "f": "gap"} | contains v=0 tol=1e-09 | K5-POS-transverse § 3, «d_H–H = 2»; G-4: d=2 → g=0 | Касания навес–навес на расстоянии 2 |
| 9 | `K5-POS-uniform-shift` | BLIND-SOURCE (prov.) | `verdict.geometry` | ["PASSED"] | K5-POS-uniform-shift § 4 | Геометрия PASSED; J5 PASSED/PASSED-EXT; топология и касания — как transverse. |
| 10 | `K5-POS-uniform-shift` | BLIND-SOURCE (prov.) | `j5.canon.verdict` | ["PASSED"] | K5-POS-uniform-shift § 4 | Геометрия PASSED; J5 PASSED/PASSED-EXT; топология и касания — как transverse. |
| 11 | `K5-POS-uniform-shift` | BLIND-SOURCE (prov.) | `j5.ext.verdict` | ["PASSED-EXT"] | K5-POS-uniform-shift § 4 | Геометрия PASSED; J5 PASSED/PASSED-EXT; топология и касания — как transverse. |
| 12 | `K5-POS-uniform-shift` | BLIND-SOURCE (prov.) | число `gap_H1_H2`: {"k": "contact", "pair": ["H1", "H2"], "f": "gap"} | contains v=0 tol=1e-09 | K5-POS-uniform-shift § 3, «d_H–H = 2»; G-4: d=2 → g=0 | касания сохраняются |
| 13 | `K5-POS-uniform-shift` | BLIND-SOURCE (prov.) | число `gap_H2_H3`: {"k": "contact", "pair": ["H2", "H3"], "f": "gap"} | contains v=0 tol=1e-09 | K5-POS-uniform-shift § 3, «d_H–H = 2»; G-4: d=2 → g=0 | касания сохраняются |
| 14 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | `verdict.geometry` | ["PASSED"] | K5-POS-K4-node § 4, «Итоги. Геометрия» | **Геометрия:** `PASSED`. |
| 15 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | `j5.canon.verdict` | ["UNRESOLVED"] | K5-POS-K4-node § 4, «Итоги. J5» | **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: PASSED-EXT`. |
| 16 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | `j5.ext.verdict` | ["PASSED-EXT"] | K5-POS-K4-node § 4, «Итоги. J5» | **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: PASSED-EXT`. |
| 17 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | contacts: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3, T0–H1, T1–H2, T2–H3 · `existence` | "IMPOSED" | K5-POS-K4-node § 4, «Итоги. Касания» | **Касания:** T_k–T_{k+1} IMPOSED (П-8(а)); T_k–H_k — LINK, IMPOSED (П-8(а)); T_{k−1}–H_k — CONTACT-ONLY, IMPOSED через `fix` (П-8(б)); H–H SEPARATED. |
| 18 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | contacts: H1–H2, H2–H3, H1–H3 · `existence` | "SEPARATED" | K5-POS-K4-node § 4, «Итоги. Касания» | **Касания:** T_k–T_{k+1} IMPOSED (П-8(а)); T_k–H_k — LINK, IMPOSED (П-8(а)); T_{k−1}–H_k — CONTACT-ONLY, IMPOSED через `fix` (П-8(б)); H–H SEPARATED. |
| 19 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | j5_edges: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `cls` | "LINK" | K5-POS-K4-node § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k, IMPOSED через `fix`, П-8(б)); T_{k−1}–H_k — CONTACT-ONLY; H–H рёбер нет. |
| 20 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | j5_edges: T0–H1, T1–H2, T2–H3 · `cls` | "CONTACT-ONLY" | K5-POS-K4-node § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k, IMPOSED через `fix`, П-8(б)); T_{k−1}–H_k — CONTACT-ONLY; H–H рёбер нет. |
| 21 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | checks R-3: RH1–RH2, RH2–RH3 · `completeness` | "EXACT" | K5-POS-K4-node § 3, «RH1–RH2» | **Применимо.** ρ ≈ 57,26° ≠ 90° → `parallel-distinct`, R-3 EXACT. |
| 22 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | checks R-3: RH1–RH2, RH2–RH3 · `plane_relation_basis.rule` | "П-9в" | K5-POS-K4-node § 3, «RH1–RH2»; интерфейс v7.1, поправка 1 | **Применимо.** ρ ≈ 57,26° ≠ 90° → `parallel-distinct`, R-3 EXACT. |
| 23 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | checks R-3: RH1–RH3 · `completeness` | "EXACT" | K5-POS-K4-node § 3, «RH1–RH3» | **Применимо.** R-3, EXACT, PASSED. |
| 24 | `K5-POS-K4-node` | CONTAMINATED (вне счёта) | checks R-3: RH1–RH3 · `plane_relation_basis.rule` | "П-9а" | K5-POS-K4-node § 3, «RH1–RH3»; интерфейс v7.1, поправка 1 | **Применимо.** R-3, EXACT, PASSED. |
| 25 | `K5-NEG-single-deviation` | GUIDED | `verdict.geometry` | ["FORBIDDEN"] | K5-NEG-single-deviation § 4, «Итоги. Геометрия» | **Геометрия:** `FORBIDDEN` (PENETRATION H1–H2). |
| 26 | `K5-NEG-single-deviation` | GUIDED | `j5.canon.verdict` | ["PASSED"] | K5-NEG-single-deviation § 4, «Итоги. J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`. Запрет геометрический, не J5: H1–H2 не касание (проникновение) — ребра в графе нет; граф — дерево. |
| 27 | `K5-NEG-single-deviation` | GUIDED | `j5.ext.verdict` | ["PASSED-EXT"] | K5-NEG-single-deviation § 4, «Итоги. J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`. Запрет геометрический, не J5: H1–H2 не касание (проникновение) — ребра в графе нет; граф — дерево. |
| 28 | `K5-NEG-single-deviation` | GUIDED | contacts: H1–H2 · `existence` | "PENETRATION" | K5-NEG-single-deviation § 4, «Итоги. Касания» | **Касания:** H1–H2 PENETRATION; H2–H3 SEPARATED; остальные IMPOSED. |
| 29 | `K5-NEG-single-deviation` | GUIDED | contacts: H2–H3 · `existence` | "SEPARATED" | K5-NEG-single-deviation § 4, «Итоги. Касания» | **Касания:** H1–H2 PENETRATION; H2–H3 SEPARATED; остальные IMPOSED. |
| 30 | `K5-NEG-single-deviation` | GUIDED | j5_edges: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `cls` | "LINK" | K5-NEG-single-deviation § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1}, T_1–H_1, T_2–H_2, T_3–H_3; H1–H2, H2–H3 рёбер нет. |
| 31 | `K5-NEG-band-30` | GUIDED | `verdict.geometry` | ["PASSED"] | K5-NEG-band-30 § 3, строка «геометрия `PASSED`» | геометрия `PASSED` |
| 32 | `K5-NEG-band-30` | GUIDED | `j5.canon.verdict` | ["FORBIDDEN"] | K5-NEG-band-30 § 4, «Итоги. J5» | **J5:** `J5-CANON: FORBIDDEN`; `J5-EXT: FORBIDDEN-EXT`. |
| 33 | `K5-NEG-band-30` | GUIDED | `j5.ext.verdict` | ["FORBIDDEN-EXT"] | K5-NEG-band-30 § 4, «Итоги. J5» | **J5:** `J5-CANON: FORBIDDEN`; `J5-EXT: FORBIDDEN-EXT`. |
| 34 | `K5-NEG-band-30` | GUIDED | contacts: T0–H1, T1–H2, T2–H3 · `existence` | "IMPOSED" | K5-NEG-band-30 § 4, «Итоги. Касания» | **Касания:** T_{k−1}–H_k IMPOSED (П-8(б)); H_k–H_{k+1} IMPOSED (П-8(г)). |
| 35 | `K5-NEG-band-30` | GUIDED | contacts: H1–H2, H2–H3 · `existence` | "IMPOSED" | K5-NEG-band-30 § 4, «Итоги. Касания» | **Касания:** T_{k−1}–H_k IMPOSED (П-8(б)); H_k–H_{k+1} IMPOSED (П-8(г)). |
| 36 | `K5-NEG-band-30` | GUIDED | j5_edges: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `cls` | "LINK" | K5-NEG-band-30 § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k); T_{k−1}–H_k — CONTACT-ONLY; H_k–H_{k+1} — CONTACT-ONLY. |
| 37 | `K5-NEG-band-30` | GUIDED | j5_edges: T0–H1, T1–H2, T2–H3, H1–H2, H2–H3 · `cls` | "CONTACT-ONLY" | K5-NEG-band-30 § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1} (R_k); LINK T_k–H_k (RH_k); T_{k−1}–H_k — CONTACT-ONLY; H_k–H_{k+1} — CONTACT-ONLY. |
| 38 | `K5-UNRESOLVED-B8` | GUIDED | `verdict.geometry` | ["UNRESOLVED"] | спецификация § 2.2, K-1 | Ветви совпали — вердикт выдаётся с пометкой; разошлись — `UNRESOLVED`. |
| 39 | `K5-UNRESOLVED-B8` | GUIDED | `j5.canon.verdict` | ["UNRESOLVED"] | K5-UNRESOLVED-B8 § 4, «Итоги. J5» | **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: UNRESOLVED`. |
| 40 | `K5-UNRESOLVED-B8` | GUIDED | `j5.ext.verdict` | ["UNRESOLVED"] | K5-UNRESOLVED-B8 § 4, «Итоги. J5» | **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: UNRESOLVED`. |
| 41 | `K5-UNRESOLVED-B8` | GUIDED | contacts: T0–H1, T1–H2, T2–H3 · `existence` | "CANDIDATE" | K5-UNRESOLVED-B8 § 4, «Итоги. Касания» | **Касания:** T_{k−1}–H_k CANDIDATE; остальные IMPOSED. |
| 42 | `K5-UNRESOLVED-B8` | GUIDED | contacts: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `existence` | "IMPOSED" | K5-UNRESOLVED-B8 § 4, «Итоги. Касания» | **Касания:** T_{k−1}–H_k CANDIDATE; остальные IMPOSED. |
| 43 | `K5-UNRESOLVED-B8` | GUIDED | j5_edges: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `cls` | "LINK" | K5-UNRESOLVED-B8 § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1}, T_k–H_k; H_k–H_{k+1} — CONTACT-ONLY, IMPOSED (П-8(г)); T_{k−1}–H_k CANDIDATE (k=1..3). |
| 44 | `K5-UNRESOLVED-B8` | GUIDED | j5_edges: H1–H2, H2–H3 · `cls` | "CONTACT-ONLY" | K5-UNRESOLVED-B8 § 4, «Итоги. Топология» | **Топология:** LINK T_k–T_{k+1}, T_k–H_k; H_k–H_{k+1} — CONTACT-ONLY, IMPOSED (П-8(г)); T_{k−1}–H_k CANDIDATE (k=1..3). |
| 45 | `K6-POS-alternating` | GUIDED | `verdict.geometry` | ["PASSED"] | K6-POS-alternating § 4, «Геометрия» | **Геометрия:** `PASSED` |
| 46 | `K6-POS-alternating` | GUIDED | `j5.canon.verdict` | ["PASSED"] | K6-POS-alternating § 4, «J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`. |
| 47 | `K6-POS-alternating` | GUIDED | `j5.ext.verdict` | ["PASSED-EXT"] | K6-POS-alternating § 4, «J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT`. |
| 48 | `K6-POS-alternating` | GUIDED | contacts: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `existence` | "IMPOSED" | K6-POS-alternating § 4, «Касания» | **Касания:** T_k–T_{k+1}, T_k–H_k IMPOSED; H–H SEPARATED. |
| 49 | `K6-POS-alternating` | GUIDED | contacts: H1–H2, H2–H3 · `existence` | "SEPARATED" | K6-POS-alternating § 4, «Касания» | **Касания:** T_k–T_{k+1}, T_k–H_k IMPOSED; H–H SEPARATED. |
| 50 | `K6-POS-alternating` | GUIDED | checks R-3: RH1–RH2, RH2–RH3, RH1–RH3 · `completeness` | "EXACT" | K6-POS-alternating § 4, «Геометрия» | **Геометрия:** `PASSED`; пары колец навесов — R-3 EXACT по П-9(б) |
| 51 | `K6-POS-alternating` | GUIDED | checks R-3: RH1–RH2, RH2–RH3, RH1–RH3 · `plane_relation_basis.rule` | "П-9б" | K6-POS-alternating § 4, «Геометрия»; интерфейс v7.1, поправка 1 | **Геометрия:** `PASSED`; пары колец навесов — R-3 EXACT по П-9(б) |
| 52 | `K6-POS-alternating` | GUIDED | число `gap_H1_H2`: {"k": "contact", "pair": ["H1", "H2"], "f": "gap"} | value_contains v=2.4721359549995796 tol=1e-09 | K6-POS-alternating § 3, «d(H1,H2) = √20 ≈ 4.472136»; G-4: d=√20 → g=√20 − 2 | Касаний навес–навес нет (≈ 4,47) |
| 53 | `K6-POS-alternating` | GUIDED | число `gap_H2_H3`: {"k": "contact", "pair": ["H2", "H3"], "f": "gap"} | value_contains v=2.4721359549995796 tol=1e-09 | K6-POS-alternating § 3, «d(H2,H3) = √20»; G-4 | Касаний навес–навес нет (≈ 4,47) |
| 54 | `K6-NEG-synthetic-odd` | GUIDED | `verdict.geometry` | ["PASSED"] | K6-NEG-synthetic-odd § 4, «Геометрия» | **Геометрия:** `PASSED`. |
| 55 | `K6-NEG-synthetic-odd` | GUIDED | `j5.canon.verdict` | ["FORBIDDEN"] | K6-NEG-synthetic-odd § 4, «J5» | **J5:** `J5-CANON: FORBIDDEN`; `J5-EXT: FORBIDDEN-EXT`. |
| 56 | `K6-NEG-synthetic-odd` | GUIDED | `j5.ext.verdict` | ["FORBIDDEN-EXT"] | K6-NEG-synthetic-odd § 4, «J5» | **J5:** `J5-CANON: FORBIDDEN`; `J5-EXT: FORBIDDEN-EXT`. |
| 57 | `K6-NEG-synthetic-odd` | GUIDED | contacts: Ta–Tb, Tb–Tc, Tc–Ta · `existence` | "IMPOSED" | K6-NEG-synthetic-odd § 4, «Касания» | **Касания:** 3 IMPOSED (declare). |
| 58 | `K6-NEG-synthetic-odd` | GUIDED | j5_edges: Ta–Tb, Tb–Tc, Tc–Ta · `cls` | "CONTACT-ONLY" | K6-NEG-synthetic-odd § 4, «Топология» | **Топология:** 3 CONTACT-ONLY ребра в 3-цикле. |
| 59 | `K6-UNRESOLVED` | GUIDED | `verdict.geometry` | ["UNRESOLVED"] | K6-UNRESOLVED § 4, «Геометрия» | **Геометрия:** `UNRESOLVED`. |
| 60 | `K6-UNRESOLVED` | GUIDED | `j5.canon.verdict` | ["UNRESOLVED"] | K6-UNRESOLVED § 4, «J5» | **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: UNRESOLVED`. |
| 61 | `K6-UNRESOLVED` | GUIDED | `j5.ext.verdict` | ["UNRESOLVED"] | K6-UNRESOLVED § 4, «J5» | **J5:** `J5-CANON: UNRESOLVED`; `J5-EXT: UNRESOLVED`. |
| 62 | `K6-UNRESOLVED` | GUIDED | contacts: T0–H1, T1–H2, T2–H3 · `existence` | "CANDIDATE" | K6-UNRESOLVED § 4, «Касания» | **Касания:** T_{k−1}–H_k CANDIDATE (k=1..3); T_k–T_{k+1}, T_k–H_k IMPOSED (П-8(а)); H–H SEPARATED. |
| 63 | `K6-UNRESOLVED` | GUIDED | contacts: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `existence` | "IMPOSED" | K6-UNRESOLVED § 4, «Касания» | **Касания:** T_{k−1}–H_k CANDIDATE (k=1..3); T_k–T_{k+1}, T_k–H_k IMPOSED (П-8(а)); H–H SEPARATED. |
| 64 | `K6-UNRESOLVED` | GUIDED | contacts: H1–H2, H2–H3, H1–H3 · `existence` | "SEPARATED" | K6-UNRESOLVED § 4, «Касания» | **Касания:** T_{k−1}–H_k CANDIDATE (k=1..3); T_k–T_{k+1}, T_k–H_k IMPOSED (П-8(а)); H–H SEPARATED. |
| 65 | `K6-UNRESOLVED` | GUIDED | j5_edges: T0–T1, T1–T2, T2–T3, T3–T4, T1–H1, T2–H2, T3–H3 · `cls` | "LINK" | K6-UNRESOLVED § 4, «Топология» | **Топология:** LINK T_k–T_{k+1}, T_k–H_k; T_{k−1}–H_k CANDIDATE; H–H рёбер нет. |
| 66 | `Kλ5-W-even` | GUIDED | `verdict.geometry` | ["PASSED"] | Kλ5-W-even § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 4 CONTACT-ONLY; касания 4 IMPOSED. |
| 67 | `Kλ5-W-even` | GUIDED | `j5.canon.verdict` | ["PASSED"] | Kλ5-W-even § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 4 CONTACT-ONLY; касания 4 IMPOSED. |
| 68 | `Kλ5-W-even` | GUIDED | `j5.ext.verdict` | ["PASSED-EXT"] | Kλ5-W-even § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 4 CONTACT-ONLY; касания 4 IMPOSED. |
| 69 | `Kλ5-W-even` | GUIDED | contacts: T1–T2, T2–T3, T3–T4, T4–T1 · `existence` | "IMPOSED" | Kλ5-W-even § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 4 CONTACT-ONLY; касания 4 IMPOSED. |
| 70 | `Kλ5-W-even` | GUIDED | j5_edges: T1–T2, T2–T3, T3–T4, T4–T1 · `cls` | "CONTACT-ONLY" | Kλ5-W-even § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 4 CONTACT-ONLY; касания 4 IMPOSED. |
| 71 | `Kλ5-Gluon-even` | GUIDED | `verdict.geometry` | ["PASSED"] | Kλ5-Gluon-even § 3, «Ожидаемое» | геометрия `PASSED`; топология 8 CONTACT-ONLY; касания 8 IMPOSED. |
| 72 | `Kλ5-Gluon-even` | GUIDED | `j5.canon.verdict` | ["PASSED"] | Kλ5-Gluon-even § 3, «Ожидаемое» | ∏g = (+1)^8 = +1 → J5-CANON: PASSED |
| 73 | `Kλ5-Gluon-even` | GUIDED | contacts: T0–T1, T1–T2, T2–T3, T3–T4, T4–T5, T5–T6, T6–T7, T7–T0 · `existence` | "IMPOSED" | Kλ5-Gluon-even § 3, «Ожидаемое» | геометрия `PASSED`; топология 8 CONTACT-ONLY; касания 8 IMPOSED. |
| 74 | `Kλ5-Gluon-even` | GUIDED | j5_edges: T0–T1, T1–T2, T2–T3, T3–T4, T4–T5, T5–T6, T6–T7, T7–T0 · `cls` | "CONTACT-ONLY" | Kλ5-Gluon-even § 3, «Ожидаемое» | геометрия `PASSED`; топология 8 CONTACT-ONLY; касания 8 IMPOSED. |
| 75 | `Kλ5-Synthetic-odd` | GUIDED | `verdict.geometry` | ["PASSED"] | Kλ5-Synthetic-odd § 4 | Геометрия `PASSED`; J5 `FORBIDDEN`/`FORBIDDEN-EXT`; топология 3 CONTACT-ONLY; касания 3 IMPOSED. |
| 76 | `Kλ5-Synthetic-odd` | GUIDED | `j5.canon.verdict` | ["FORBIDDEN"] | Kλ5-Synthetic-odd § 4 | Геометрия `PASSED`; J5 `FORBIDDEN`/`FORBIDDEN-EXT`; топология 3 CONTACT-ONLY; касания 3 IMPOSED. |
| 77 | `Kλ5-Synthetic-odd` | GUIDED | `j5.ext.verdict` | ["FORBIDDEN-EXT"] | Kλ5-Synthetic-odd § 4 | Геометрия `PASSED`; J5 `FORBIDDEN`/`FORBIDDEN-EXT`; топология 3 CONTACT-ONLY; касания 3 IMPOSED. |
| 78 | `Kλ5-Synthetic-odd` | GUIDED | contacts: Ta–Tb, Tb–Tc, Tc–Ta · `existence` | "IMPOSED" | Kλ5-Synthetic-odd § 4 | Геометрия `PASSED`; J5 `FORBIDDEN`/`FORBIDDEN-EXT`; топология 3 CONTACT-ONLY; касания 3 IMPOSED. |
| 79 | `Kλ5-Synthetic-odd` | GUIDED | j5_edges: Ta–Tb, Tb–Tc, Tc–Ta · `cls` | "CONTACT-ONLY" | Kλ5-Synthetic-odd § 4 | Геометрия `PASSED`; J5 `FORBIDDEN`/`FORBIDDEN-EXT`; топология 3 CONTACT-ONLY; касания 3 IMPOSED. |
| 80 | `Kλ5-Z-notapplicable` | GUIDED | `verdict.geometry` | ["PASSED"] | Kλ5-Z-notapplicable § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 1 LINK; касания IMPOSED. |
| 81 | `Kλ5-Z-notapplicable` | GUIDED | `j5.canon.verdict` | ["PASSED"] | Kλ5-Z-notapplicable § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 1 LINK; касания IMPOSED. |
| 82 | `Kλ5-Z-notapplicable` | GUIDED | `j5.ext.verdict` | ["PASSED-EXT"] | Kλ5-Z-notapplicable § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 1 LINK; касания IMPOSED. |
| 83 | `Kλ5-Z-notapplicable` | GUIDED | contacts: Za–Zb · `existence` | "IMPOSED" | Kλ5-Z-notapplicable § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 1 LINK; касания IMPOSED. |
| 84 | `Kλ5-Z-notapplicable` | GUIDED | j5_edges: Za–Zb · `cls` | "LINK" | Kλ5-Z-notapplicable § 4, «Итоги» | Геометрия `PASSED`; J5 `PASSED`/`PASSED-EXT`; топология 1 LINK; касания IMPOSED. |
| 85 | `A6-K5` / K5-POS-transverse | GUIDED | `verdict.geometry` | ["PASSED"] | A6-K5 § 4, «Итоги. Геометрия» | **Геометрия:** положительная — `PASSED`; одиночное — `FORBIDDEN`. |
| 86 | `A6-K5` / K5-POS-transverse | GUIDED | `j5.canon.verdict` | ["PASSED"] | A6-K5 § 4, «Итоги. J5» | **J5:** положительная — `J5-CANON: PASSED`; одиночное — `J5-CANON: PASSED` (проникновение не ребро; граф — дерево). |
| 87 | `A6-K5` / K5-POS-transverse | GUIDED | contacts: H1–H2, H2–H3 · `existence` | "IMPOSED" | A6-K5 § 4, «Итоги. Касания» | **Касания:** положительная — H–H IMPOSED (П-8(г)); одиночное — H1–H2 PENETRATION, H2–H3 SEPARATED. |
| 88 | `A6-K5` / K5-NEG-single-deviation | GUIDED | `verdict.geometry` | ["FORBIDDEN"] | A6-K5 § 4, «Итоги. Геометрия» | **Геометрия:** положительная — `PASSED`; одиночное — `FORBIDDEN`. |
| 89 | `A6-K5` / K5-NEG-single-deviation | GUIDED | `j5.canon.verdict` | ["PASSED"] | A6-K5 § 4, «Итоги. J5» | **J5:** положительная — `J5-CANON: PASSED`; одиночное — `J5-CANON: PASSED` (проникновение не ребро; граф — дерево). |
| 90 | `A6-K5` / K5-NEG-single-deviation | GUIDED | contacts: H1–H2 · `existence` | "PENETRATION" | A6-K5 § 4, «Итоги. Касания» | **Касания:** положительная — H–H IMPOSED (П-8(г)); одиночное — H1–H2 PENETRATION, H2–H3 SEPARATED. |
| 91 | `A6-K5` / K5-NEG-single-deviation | GUIDED | contacts: H2–H3 · `existence` | "SEPARATED" | A6-K5 § 4, «Итоги. Касания» | **Касания:** положительная — H–H IMPOSED (П-8(г)); одиночное — H1–H2 PENETRATION, H2–H3 SEPARATED. |
| 92 | `A6-K5` / K5-POS-transverse | GUIDED | число `gap_H1_H2`: {"k": "contact", "pair": ["H1", "H2"], "f": "gap"} | contains v=0 tol=1e-09 | A6-K5 § 3, строка «d_H–H = 2»; G-4: d=2 → g=0 | Расстояние навес–навес = 2 |
| 93 | `A6-K5` / K5-POS-transverse | GUIDED | число `gap_H2_H3`: {"k": "contact", "pair": ["H2", "H3"], "f": "gap"} | contains v=0 tol=1e-09 | A6-K5 § 3, строка «d_H–H = 2»; G-4: d=2 → g=0 | Расстояние навес–навес = 2 |
| 94 | `A7-K6` / K6-POS-alternating | GUIDED | `verdict.geometry` | ["PASSED"] | A7-K6 § 4, «Итоги. Геометрия» | **Геометрия:** `PASSED`. |
| 95 | `A7-K6` / K6-POS-alternating | GUIDED | `j5.canon.verdict` | ["PASSED"] | A7-K6 § 4, «Итоги. J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT` (спец. K-6, М-2). |
| 96 | `A7-K6` / K6-POS-alternating | GUIDED | `j5.ext.verdict` | ["PASSED-EXT"] | A7-K6 § 4, «Итоги. J5» | **J5:** `J5-CANON: PASSED`; `J5-EXT: PASSED-EXT` (спец. K-6, М-2). |
| 97 | `A7-K6` / K6-POS-alternating | GUIDED | contacts: H1–H2, H2–H3 · `existence` | "SEPARATED" | A7-K6 § 4, «Итоги. Касания» | **Касания:** H–H SEPARATED. |
| 98 | `A7-K6` / K6-POS-alternating | GUIDED | число `gap_H1_H2`: {"k": "contact", "pair": ["H1", "H2"], "f": "gap"} | value_contains v=2.4721359549995796 tol=1e-09 | A7-K6 § 3, «d(H1,H2) = √20 ≈ 4.472136»; G-4: d=√20 → g=√20 − 2 | Касаний навес–навес нет (≈ 4,47) |
| 99 | `A7-K6` / K6-POS-alternating | GUIDED | число `gap_H2_H3`: {"k": "contact", "pair": ["H2", "H3"], "f": "gap"} | value_contains v=2.4721359549995796 tol=1e-09 | A7-K6 § 3, «d(H2,H3) = √20»; G-4 | Касаний навес–навес нет (≈ 4,47) |
| 100 | `B4-Kλ5` / Kλ5-W-even | GUIDED | `verdict.geometry` | ["PASSED"] | B4-Kλ5 § 4, «Итоги. Геометрия» | **Геометрия:** во всех трёх — `PASSED`. |
| 101 | `B4-Kλ5` / Kλ5-W-even | GUIDED | `j5.canon.verdict` | ["PASSED"] | B4-Kλ5 § 3, «чётные циклы» | **J5:** W, глюон — `PASSED`/`PASSED-EXT`; синтетический нечётный — `FORBIDDEN`/`FORBIDDEN-EXT`. |
| 102 | `B4-Kλ5` / Kλ5-Gluon-even | GUIDED | `verdict.geometry` | ["PASSED"] | B4-Kλ5 § 4, «Итоги. Геометрия» | **Геометрия:** во всех трёх — `PASSED`. |
| 103 | `B4-Kλ5` / Kλ5-Gluon-even | GUIDED | `j5.canon.verdict` | ["PASSED"] | B4-Kλ5 § 3, «чётные циклы» | **J5:** W, глюон — `PASSED`/`PASSED-EXT`; синтетический нечётный — `FORBIDDEN`/`FORBIDDEN-EXT`. |
| 104 | `B4-Kλ5` / Kλ5-Synthetic-odd | GUIDED | `verdict.geometry` | ["PASSED"] | B4-Kλ5 § 4, «Итоги. Геометрия» | **Геометрия:** во всех трёх — `PASSED`. |
| 105 | `B4-Kλ5` / Kλ5-Synthetic-odd | GUIDED | `j5.canon.verdict` | ["FORBIDDEN"] | B4-Kλ5 § 3, «нечётный цикл» | **J5:** W, глюон — `PASSED`/`PASSED-EXT`; синтетический нечётный — `FORBIDDEN`/`FORBIDDEN-EXT`. |
| 106 | `B6a-R2-static-meeting` | GUIDED | checks R-2: Q1–Q2 · `contact_class` | "UNRESOLVED CONTACT" | B6a-R2-static-meeting § 4, «Итоги» | **Геометрия:** R-2, `UNRESOLVED CONTACT`. |
| 107 | `B6b-R5-near-parallel` | BLIND-SOURCE (prov.) | `verdict.geometry` | ["UNRESOLVED"] | B6b-R5-near-parallel § 4, «Итоги» | Геометрия — R-5 `UNRESOLVED`; остальное вне графа. |
| 108 | `B6c-R6-three-rings` | GUIDED | checks R-6: Q1–Q2–Q3 · `contact_class` | "DEGENERATE MEETING" | B6c-R6-three-rings § 4, «Итоги» | Геометрия — R-6 `DEGENERATE MEETING`; J5 вне графа. |
| 109 | `B7-B1-property` | GUIDED | `output.family.first_stop.value` | [5] | B7-B1-property § 3, «output.family.first_stop — ρ = 5°» | `output.family.first_stop` — ρ = 5° |
| 110 | `B7-B1-property` | GUIDED | `output.family.last_admissible.value` | [0] | B7-B1-property § 3, «output.family.last_admissible — ρ = 0°» | `output.family.last_admissible` — ρ = 0° (PASSED) |
| 111 | мутант `m7` | BLIND-SOURCE (prov.) | ловится: B6a-R2-static-meeting | на ядре PASS, на мутанте FAIL | D-5 ред. 3, m7-mutant § 3 | м7 ловится B6a |

Всего строк: 111.
