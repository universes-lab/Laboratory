# HONC / Qf / R1 / КТ-1 — А-5 rev8: материалы к поручению (ответ на `STOP → REPORT GAP`)

**ОТ:** Клод, руководитель отдела · **КОМУ:** DeepSeek · **КОПИЯ:** Грок · **ЧЕРЕЗ:** Автора · **Дата:** 11.11.2026

> Значений ядра здесь нет. Ниже — источники дословно и твой код rev7 целиком. Всё это было в ZOV поручения, но в твой чат не попало — мой недосмотр.

## 0. Ответы на твои вопросы — по источникам (полный текст в §§ 1–3)

| Вопрос | Ответ | Где |
|---|---|---|
| Что такое ρ | Угол в направлении навеса: **e = s·e_x·cos ρ + (−e_z·cos ψ + e_y·sin ψ)·sin ρ** в рамке узла хозяина. ρ — отклонение от поперечного направления s·e_x; ψ = 0 — назад, к предыдущему тору | интерфейс § 2, «Навес» |
| Что такое u в T′ = T_h − 2(T_h·u)·u | **u = e** — единичное направление навеса (звена) от центра хозяина. Поворот на δ — вокруг **n = нормировка(u × T_h)**, по правилу правой руки | интерфейс § 2, «Звено k» и «Навес» |
| Где центр H1 | **A_H1 = A_h + d·e**, где d — корень «зазор G-4(H1, хозяин) = 0» вдоль e (незеркальное звено, δ ≠ 0); при δ = 0 (зеркальное звено, как в К3) — закрытая форма G-3: d = 2(½·√(1 − (T_h·e)²) + ½) | интерфейс § 2; спецификация G-3 |
| Что такое ρ-корень | ρ задаётся уравнением «зазор G-4(H1, T1) = 0» (`fix`, `with: "T1"`) в вилке `bracket` | интерфейс § 4.1–4.2 |
| Зазор тор–тор | **g = min_φ dist(C₁(φ), C₂) − 1**: C₁(φ) — точка средней окружности первого тора (радиус 0,5), C₂ — средняя окружность второго; расстояние от точки до окружности — закрытая форма; константа Липшица по φ ≤ 0,5 | спецификация G-4 |
| `dist` в проверке 2 | Кольцо и чужой тор: **f(t) = dist(E(t), средняя окружность) − 0,5**; f < 0 — точка кольца внутри тела тора (прокол) | спецификация G-5а |
| Зависит ли кольцо 1→2 от ρ | **Нет.** Это кольцо R1 нити (тора T1), через A₁ и A₂. В прямой нити (все звенья θ = φ = δ = 0) A_k = (0, 0, 2k), кольцо R1 — окружность радиуса 1 в плоскости yz с центром (0, 0, 3): **E(θ) = (0, sin θ, 3 − cos θ)**. От ρ зависит только H1 | интерфейс § 2; спецификация А-1, G-2 |
| Рамка узла хозяина T2 в прямой нити | e_z = +ẑ (входящее звено), T₂ = +ŷ, e_y = +ŷ, e_x = e_y × e_z = +x̂; A₂ = (0, 0, 4), T₁: A₁ = (0, 0, 2), ось +ŷ | интерфейс § 2, «Начало», «Рамка узла» |
| Конфигурация К3 / К4 / А-5 | Нить n = 5, все звенья (0, 0, 0); навес H1 на T2 (`host: 2`), `side: 1`, `coords: "rho-psi"`; ψ и δ — из команды; `fix: contact, free: rho, with: T1, bracket` — из команды | интерфейс § 4.1 (пример — ровно К4) |

**Что изменить в поручении — ничего.** Двухэтапную сдачу не ввожу: присылай части по мере готовности по правилу 12 КБ, а принимаю я полный пакет по трём случаям § 5 поручения.

## 1. Интерфейс v6 — §§ 1, 2, 4.1, 4.2 дословно

Источник: `HONC_Qf_R1_KT1_Interface_2026-11-01.md`, sha256 `84b28b3a02c34c84367087f6ad54949afd3c9bfe3a637d7a32cf1bc5f0e861c6`.

#### 1. Единицы и соглашения

- **Длины** — в единицах R, где длина кольца 2πR, то есть R = 1. Тор: a = b = ½.
- **Углы на входе и в протоколе** — в градусах, десятичной записью.
- **Координаты** — правая тройка (x, y, z).
- **Вилка** — пара чисел `[lo, hi]` с lo ≤ hi. Каждое число — точное двоичное значение с плавающей точкой, записанное в JSON без потери (кратчайшая точная запись). Вилка гарантированно содержит истинное значение — если полнота `EXACT` или `CERTIFIED`.
- **Вектор-вилка** — три вилки.

#### 2. Построение (G-7): точные определения

Каждый Qf — тор со своим кольцом. Кольцо тора k продевает тор k и следующий тор нити. Кольцо последнего тора свободно: строится тем же правилом звена, но в его второй точке тора нет.

**Начало.** Тор T0: центр A₀ = (0, 0, 0), ось T₀ = +ŷ; начальное направление нити e_z = +ẑ.

**Рамка узла k** — для тора k с осью T_k и входящим направлением e_z (направление звена, пришедшего в тор k; для k = 0 — +ẑ):
- e_y = нормированная часть T_k, перпендикулярная e_z. Если она вырождена — e_y = нормировка (e_z × x̂);
- e_x = e_y × e_z.

**Звено k** из тора k, параметры (θ, φ, δ):
- направление: u = e_z·cos θ + (e_x·cos φ + e_y·sin φ)·sin θ;
- зеркальная ось: T′ = T_k − 2(T_k·u)·u;
- ось следующего тора: T_{k+1} = поворот T′ на угол δ вокруг n = нормировка(u × T_k), по правилу правой руки;
- δ = 0 — зеркальное звено;
- расстояние d:
  - зеркальное звено: d = 2(½·√(1 − (T_k·u)²) + ½);
  - незеркальное: d — корень уравнения «зазор G-4 = 0» вдоль u, с вилкой и проверкой единственности;
- центр следующего тора: A_{k+1} = A_k + d·u;
- кольцо k — плоский эллипс длины 2π через A_k и A_{k+1}, касательный к T_k в A_k и к T_{k+1} в A_{k+1} (G-2). Как кольцо записывается в протоколе и с какой точностью — § 6.5;
- последнее звено строится по тому же правилу с явно заданными (θ, φ, δ). Его кольцо свободно: тора в точке A_n нет;
- **зеркальное звено** (δ = 0) — конвенция модели [Г] (Раунд 3а, § 1). Ядро её не подставляет: δ всегда приходит из входа, а протокол помечает каждое зеркальное звено (§ 6, `conventions`).

**Навес** — на торе-хозяине h нити, сторона s ∈ {+1, −1}, рамка узла h:
- в координатах (ρ, ψ, δ): e = s·e_x·cos ρ + (−e_z·cos ψ + e_y·sin ψ)·sin ρ.
  - ρ — отклонение от поперечного направления s·e_x.
  - ψ = 0 — отклонение назад, к предыдущему тору (−e_z); ψ = 180° — вперёд; ψ = 90° — вдоль оси хозяина.
- в координатах сцены захвата (α, λ, δ): e = cos λ·(s·cos α·e_x + sin α·e_y) − sin λ·e_z.
  - α — азимут от экватора хозяина к его оси; λ — отклонение назад.
  - Перевод: cos ρ = cos λ·cos α; ψ = atan2(cos λ·sin α, sin λ). При ρ = 0 угол ψ не определён — тогда перевод не выполняется, и навес задаётся напрямую в (ρ, ψ, δ).
- тор навеса и его кольцо строятся по правилу звена из хозяина с u = e и данным δ.

  Кольцо навеса продевает навес и хозяина.

**Имена объектов:**
- торы нити — `T0`…`T{n−1}`; навесы — `H1`, `H2`, …;
- кольцо тора нити k — `R{k}`; кольцо навеса j — `RH{j}`.

**Ориентация осей.** Ось T каждого тора — ровно тот вектор, который дало построение. Знак J5 на отдельном ребре, sign(v_A·v_B) с v = T × (c − A), зависит от этой ориентации. Произведение знаков по циклу и итоги K-6 от неё не зависят.

##### 4.1. Конфигурация нити с навесами

```json
{
  "id": "K4",
  "thread": { "n": 5, "links": [
    { "theta": 0, "phi": 0, "delta": 0 }, { "theta": 0, "phi": 0, "delta": 0 },
    { "theta": 0, "phi": 0, "delta": 0 }, { "theta": 0, "phi": 0, "delta": 0 },
    { "theta": 0, "phi": 0, "delta": 0 } ] },
  "hangs": [
    { "host": 2, "side": 1,
      "coords": "rho-psi", "rho": null, "psi": 54, "delta": 10,
      "fix": { "kind": "contact", "free": "rho", "with": "T1", "bracket": [57.0, 57.5] } }
  ]
}
```

- `thread.n` — число торов нити.
- `thread.links` — ровно n записей (θ, φ, δ) для звеньев 0…n−1, включая последнее, со свободным кольцом.
- `hangs[]` — навесы:
  - `coords`: `"rho-psi"` или `"alpha-lambda"`;
  - параметры `rho`, `psi`, `delta` или `alpha`, `lambda`, `delta`.
- **Значений по умолчанию нет.** Отсутствующий параметр — `input_error`. Исключение — свободный параметр уравнения касания: он равен `null` (§ 4.2).
- Числа входа понимаются как точные десятичные значения. Ядро заключает их перевод в радианы в вилку.

##### 4.2. Конфигурация, заданная уравнением касания

Поле `fix` задаёт один параметр навеса уравнением «зазор G-4 между навесом и тором `with` равен нулю»:
- `free` — свободный параметр: `rho`, `psi`, `lambda` или `alpha`; во входе он равен `null`;
- `bracket` — вилка поиска корня, в градусах.

**Обязательства ядра:**
- доказать существование и единственность корня в вилке. Не удалось — конфигурация не строится, протокол содержит `UNRESOLVED` с причиной;
- касание с `with` получает `IMPOSED` по П-8(б); основание: уравнение, вилка, вилка корня, способ доказательства единственности;
- все остальные проверки выполнить на всей вилке корня, а не в её середине.

**Ограничение.** «Первое касание вдоль пути» этим не удостоверяется: доказывается лишь, что корень в вилке единствен. Нет ли касания раньше, по параметру пути, — вопрос пути (TB-1), в КТ-1 не решается.

**Без `fix`** все параметры берутся как числа. Касание с зазором, вилка которого содержит 0, тогда получает `CANDIDATE` (K-1). Так задаётся испытание Б-8.

## 2. Спецификация v0.3 — строки § 2.1 и § 2.11 дословно

Источник: `HONC_Qf_Tool_Spec_2026-11-01.md`, sha256 `1f443e6f4c67b31a89c52270206eb4890f69ac9132ba5fb116958247ce3d4577`.

**§ 2.1, строки G-1…G-5а, G-7:**

| ID | Требование | Кат. | Приёмка |
|---|---|---|---|
| G-1 | Тор: рогатый, центр A, единичная ось T; средняя окружность радиуса 0,5, трубка 0,5 | R1 | А-1 |
| G-2 | Кольцо — плоский эллипс через центры A и B, касательный к T_A в A и к T_B в B; T_B лежит в плоскости кольца. Построение — пучок коник. Длина 2π: периметр через полный эллиптический интеграл второго рода методом AGM; уравнение длины решается с гарантированной вилкой. Точность *(поправка 1, 02.11)*: примитив периметра при точных полуосях и кольцо по точному тождеству — ошибка ≤ 10⁻¹²; кольцо общего вида — сертифицированная вилка переменной ширины, ширина обязательно выводится в протокол. Последующие проверки учитывают полную вилку построения; если её недостаточно — `UNRESOLVED` | R1 | А-1: при u = 0 — окружность радиуса 1; совпадение с прежним ядром в зеркальном случае |
| G-3 | Расстояние звена d. Зеркальное — закрытая форма d = 2(½√(1 − u²) + ½). Незеркальное — корень зазора G-4 вдоль направления звена: вилка, проверка единственности, интервал ошибки | R1 (вилка и единственность); R2 (перенос ошибки в G-2) | А-1, А-4 |
| G-4 | Зазор тор–тор: g = minφ dist(C₁(φ), C₂) − 1. Расстояние от точки до окружности — закрытая форма. Глобальный минимум — ветвями и границами (константа Липшица ≤ 0,5). На выходе — интервал [g_lo, g_hi] и все минимумы | R1 | А-2, А-3, А-6 |
| G-5а | Кольцо и чужой тор (кольцо его не продевает): f(t) = dist(E(t), средняя окружность) − 0,5; ветви и границы (константа Липшица ≤ большой полуоси); интервал | R1 | А-4: граница окна, прокол кольцом 1→2 |
| G-7 | Параметризации навеса (ρ, ψ, δ) и (α, λ, δ) с точным переводом; звено хозяина (θ, φ, δ) | R1 | А-4: две параметризации дают одну конфигурацию |

**§ 2.11, группа А, строки А-1, А-2, А-4, А-5:**

| ID | Случай | Ожидаемое | Допуск |
|---|---|---|---|
| А-1 | К1 | d = 2; кольцо — окружность радиуса 1; вердикт `PASSED` (§ 2.10) | 10⁻¹² |
| А-2 | К2 | Полуплоскости −90° / 0° / +90°; тройка = 1; первое касание при отклонении в плоскости — 30,0000° назад и вперёд; на границе — `IMPOSED` | 10⁻⁶ ° |
| А-4 | К4, ψ = 54°, δ = 10° (и ψ = 306°, δ = −10°) | ρ = 57,261°; геометрия `PASSED`; запасы ≈ 0,078 (кольцо–тело) и ≈ 0,006 (касп); κ_r = 1,366. Эталон — прежнее выборочное ядро: расхождение докладывается, а не подгоняется | 0,001° / 0,0005 |
| А-5 | Окно, граница прокола (ψ = 56°, δ = 10°) | Кольцо 1→2 в торе навеса — `FORBIDDEN` (G-5а) | — |

## 3. Твой код rev7 целиком

Источник: `DEEPSEEK_KT1_A5_SCRIPTS_2026-11-03_rev7.md`, sha256 `08ed14a3a65946584d5b9aa497ab4749b71c65764bb9ed72effe1c722ef067bb`; архив `HONC_Qf_KT1_A5_DeepSeek_2026-11-03_rev7.zip`, sha256 `166a2d30…237c`. Ниже — текст сдачи rev7 без изменений, начиная с первого файла.

### FILE: a5/lib/ia.js
```js
'use strict';
const F64 = new Float64Array(1);
const I64 = new BigInt64Array(F64.buffer);
function nextUp(x) {
  if (x !== x) return x;
  if (x === Infinity) return x;
  if (x === 0) return Number.MIN_VALUE;
  F64[0] = x;
  const bits = I64[0];
  I64[0] = x > 0 ? bits + 1n : bits - 1n;
  return F64[0];
}
function nextDown(x) { return -nextUp(-x); }
class I {
  constructor(lo, hi) { this.lo = lo; this.hi = hi; }
  static of(v) { return new I(v, v); }
  add(o) { return new I(nextDown(this.lo + o.lo), nextUp(this.hi + o.hi)); }
  sub(o) { return new I(nextDown(this.lo - o.hi), nextUp(this.hi - o.lo)); }
  mul(o) {
    const p = [this.lo*o.lo, this.lo*o.hi, this.hi*o.lo, this.hi*o.hi];
    return new I(nextDown(Math.min(...p)), nextUp(Math.max(...p)));
  }
  div(o) {
    if (o.lo <= 0 && o.hi >= 0) throw new Error('div by interval containing 0');
    const p = [this.lo/o.lo, this.lo/o.hi, this.hi/o.lo, this.hi/o.hi];
    return new I(nextDown(Math.min(...p)), nextUp(Math.max(...p)));
  }
  neg() { return new I(-this.hi, -this.lo); }
  abs() { return new I(this.lo < 0 && this.hi > 0 ? 0 : Math.min(Math.abs(this.lo), Math.abs(this.hi)), Math.max(Math.abs(this.lo), Math.abs(this.hi))); }
  sqrt() {
    const lo = this.lo < 0 ? 0 : this.lo;
    if (this.hi < 0) throw new Error('sqrt of negative interval');
    return new I(nextDown(Math.sqrt(lo)), nextUp(Math.sqrt(this.hi)));
  }
  sin() {
    if (this.hi - this.lo > 2*Math.PI) return new I(-1, 1);
    let hasPeak = false, hasTrough = false;
    const kpLo = Math.floor((this.lo - Math.PI/2) / (2*Math.PI));
    const kpHi = Math.ceil((this.hi - Math.PI/2) / (2*Math.PI));
    for (let k = kpLo; k <= kpHi; k++) {
      const p = Math.PI/2 + 2*Math.PI*k;
      if (p >= this.lo && p <= this.hi) hasPeak = true;
    }
    const ktLo = Math.floor((this.lo + Math.PI/2) / (2*Math.PI));
    const ktHi = Math.ceil((this.hi + Math.PI/2) / (2*Math.PI));
    for (let k = ktLo; k <= ktHi; k++) {
      const p = -Math.PI/2 + 2*Math.PI*k;
      if (p >= this.lo && p <= this.hi) hasTrough = true;
    }
    let lo = Math.min(Math.sin(this.lo), Math.sin(this.hi));
    let hi = Math.max(Math.sin(this.lo), Math.sin(this.hi));
    if (hasPeak) hi = 1;
    if (hasTrough) lo = -1;
    const E = 1e-12;
    return new I(nextDown(lo - E), nextUp(hi + E));
  }
  cos() { return new I(this.lo + Math.PI/2, this.hi + Math.PI/2).sin(); }
  hasZero() { return this.lo <= 0 && this.hi >= 0; }
  isPos() { return this.lo > 0; }
  isNeg() { return this.hi < 0; }
  mid() { return (this.lo + this.hi) / 2; }
  width() { return this.hi - this.lo; }
}
module.exports = { I, nextUp, nextDown };
```

### FILE: a5/lib/vec.js
```js
'use strict';
const { I } = require('./ia');
class V {
  constructor(x, y, z) { this.x = x; this.y = y; this.z = z; }
  static of(a) { return new V(I.of(a[0]), I.of(a[1]), I.of(a[2])); }
  add(o) { return new V(this.x.add(o.x), this.y.add(o.y), this.z.add(o.z)); }
  sub(o) { return new V(this.x.sub(o.x), this.y.sub(o.y), this.z.sub(o.z)); }
  scale(k) {
    const K = (k instanceof I) ? k : I.of(k);
    return new V(this.x.mul(K), this.y.mul(K), this.z.mul(K));
  }
  neg() { return new V(this.x.neg(), this.y.neg(), this.z.neg()); }
  dot(o) { return this.x.mul(o.x).add(this.y.mul(o.y)).add(this.z.mul(o.z)); }
  cross(o) {
    return new V(
      this.y.mul(o.z).sub(this.z.mul(o.y)),
      this.z.mul(o.x).sub(this.x.mul(o.z)),
      this.x.mul(o.y).sub(this.y.mul(o.x))
    );
  }
  norm() { return this.dot(this).sqrt(); }
  unit() {
    const n = this.norm();
    if (n.hasZero()) throw new Error('normalize near-zero vector');
    return new V(this.x.div(n), this.y.div(n), this.z.div(n));
  }
}
module.exports = { V };
```

### FILE: a5/lib/geom.js
```js
'use strict';
const { I } = require('./ia');
const { V } = require('./vec');
function orthonormalBasis(T) {
  const zhat = V.of([0, 0, 1]);
  const xhat = V.of([1, 0, 0]);
  let u;
  try {
    u = T.cross(zhat).unit();
    u.norm();
  } catch (e) {
    u = xhat;
  }
  const v = T.cross(u);
  return { u, v };
}
function distPointToMidCircle(P, A, T) {
  const dPA = P.sub(A);
  const axial = dPA.dot(T);
  const P_rad = new V(
    dPA.x.sub(axial.mul(T.x)),
    dPA.y.sub(axial.mul(T.y)),
    dPA.z.sub(axial.mul(T.z))
  );
  const radial = P_rad.norm();
  const r = I.of(0.5);
  const dr = radial.sub(r);
  return axial.mul(axial).add(dr.mul(dr)).sqrt();
}
function gapTorusTorus(A, T, A2, T2, N_phi, L_phi) {
  const { u, v } = orthonormalBasis(T);
  const one = I.of(1);
  const half = I.of(0.5);
  let minAdjLo = Infinity;
  let minHi = Infinity;
  const h = 2 * Math.PI / N_phi;
  for (let j = 0; j < N_phi; j++) {
    const phi = j * h;
    const cosphi = I.of(Math.cos(phi));
    const sinphi = I.of(Math.sin(phi));
    const C = A.add(u.scale(cosphi).add(v.scale(sinphi)).scale(half));
    const d = distPointToMidCircle(C, A2, T2);
    const gap_at = d.sub(one);
    const adj_lo = gap_at.lo - L_phi * h / 2;
    if (adj_lo < minAdjLo) minAdjLo = adj_lo;
    if (gap_at.hi < minHi) minHi = gap_at.hi;
  }
  return new I(minAdjLo, minHi);
}
module.exports = { orthonormalBasis, distPointToMidCircle, gapTorusTorus };
```

### FILE: a5/lib/frame.js
```js
'use strict';
const { I } = require('./ia');
const { V } = require('./vec');
function hangDirection(rho, psi, ex, ey, ez, side) {
  const cr = rho.cos();
  const sr = rho.sin();
  const cp = I.of(Math.cos(psi));
  const sp = I.of(Math.sin(psi));
  const s = side === 1 ? 1 : -1;
  const term1 = ex.scale(cr).scale(s);
  const vec_part = ez.scale(cp).neg().add(ey.scale(sp));
  const term2 = vec_part.scale(sr);
  return term1.add(term2);
}
function rodrigues(v, k, alpha) {
  const ca = I.of(Math.cos(alpha));
  const sa = I.of(Math.sin(alpha));
  const kv = k.dot(v);
  const kxv = k.cross(v);
  const one_minus_ca = new I(1, 1).sub(ca);
  return v.scale(ca).add(kxv.scale(sa)).add(k.scale(kv.mul(one_minus_ca)));
}
module.exports = { hangDirection, rodrigues };
```

### FILE: a5/check1_root.js
```js
'use strict';
const { I } = require('./lib/ia');
const { V } = require('./lib/vec');
const { gapTorusTorus } = require('./lib/geom');
const { hangDirection, rodrigues } = require('./lib/frame');

const A_T1 = V.of([0, 0, 2]);
const A_T2 = V.of([0, 0, 4]);
const Y_HAT = V.of([0, 1, 0]);
const X_HAT = V.of([1, 0, 0]);
const Z_HAT = V.of([0, 0, 1]);

const EX = X_HAT, EY = Y_HAT, EZ = Z_HAT;
const SIDE = 1;

// Build H1 torus per §2 interface v6, link rule with u = e:
//   mirror T' = T_h − 2(T_h·u)·u; n = norm(u × T_h); T_{k+1} = rodrigues(T', n, δ)
function buildH1(rho_I, d_I, psi, delta) {
  const e = hangDirection(rho_I, psi, EX, EY, EZ, SIDE);
  const u_dot_T = e.dot(Y_HAT);
  const T_prime = Y_HAT.sub(e.scale(u_dot_T.mul(I.of(2))));
  const n_raw = e.cross(Y_HAT);
  let n;
  try {
    n = n_raw.unit();
  } catch (err) {
    throw new Error('n degenerate at ρ=' + (rho_I.mid() * 180 / Math.PI));
  }
  const T_H1 = rodrigues(T_prime, n, delta);
  const A_H1 = A_T2.add(e.scale(d_I));
  return { A_H1, T_H1 };
}

function evaluateGapH1T2(rho_I, d_mid, psi, delta) {
  const { A_H1, T_H1 } = buildH1(rho_I, I.of(d_mid), psi, delta);
  return gapTorusTorus(A_H1, T_H1, A_T2, Y_HAT, 180, 1.0);
}

// Solve d_H1(ρ): root of gap(H1, T2) = 0 in d ∈ [dLo, dHi].
// Expanded range [0.3, 3.5] vs rev6 [0.5, 3.0].
// Returns { lo, hi, uncertain, multiplicity }.
//   multiplicity = number of sign-change sub-intervals found.
//   If multiple, take the smallest (first from dLo) — first contact H1 with T2.
//   If none, uncertain = true, bracket = [dLo, dHi] (whole range).
function solveD(rho_I, psi, delta) {
  const dLo = 0.3, dHi = 3.5;
  const N_scan = 40;
  const scanH = (dHi - dLo) / N_scan;
  const straddles = [];
  let prevSign = null;
  let prev_d = dLo;
  for (let j = 0; j <= N_scan; j++) {
    const d = dLo + j * scanH;
    const g = evaluateGapH1T2(rho_I, d, psi, delta);
    const sign = g.isPos() ? '+' : (g.isNeg() ? '-' : '0');
    if (prevSign !== null && prevSign !== '0' && sign !== '0' && prevSign !== sign) {
      straddles.push([prev_d, d]);
    }
    if (sign !== '0') prevSign = sign;
    prev_d = d;
  }
  if (straddles.length === 0) {
    return { lo: dLo, hi: dHi, uncertain: true, multiplicity: 0 };
  }
  // use first (smallest d) straddle — H1 first encounters T2
  const [a0, b0] = straddles[0];
  let a = a0, b = b0;
  const ga = evaluateGapH1T2(rho_I, a, psi, delta);
  let sign_a = ga.isPos() ? '+' : '-';
  for (let iter = 0; iter < 40 && (b - a) > 1e-6; iter++) {
    const m = (a + b) / 2;
    const g = evaluateGapH1T2(rho_I, m, psi, delta);
    const s = g.isPos() ? '+' : (g.isNeg() ? '-' : '0');
    if (s === sign_a) a = m;
    else b = m;
  }
  return { lo: a, hi: b, uncertain: false, multiplicity: straddles.length };
}

// gap(H1, T1) at given ρ.
// Does NOT fall back to [-1, 1] on d.uncertain — instead computes gap on the
// full d-bracket [d.lo, d.hi]. The result is '?' (hasZero) only if the gap
// interval straddles zero, not because d is uncertain.
function gapH1T1(rho_I, psi, delta) {
  const d = solveD(rho_I, psi, delta);
  const d_I = new I(d.lo, d.hi);
  const { A_H1, T_H1 } = buildH1(rho_I, d_I, psi, delta);
  const gap = gapTorusTorus(A_H1, T_H1, A_T1, Y_HAT, 360, 1.0);
  return { gap, d, uncertain: gap.hasZero() };
}

// Sign classification per node:
//   '+' — gap_lo > 0 (definitely positive)
//   '-' — gap_hi < 0 (definitely negative)
//   '?' — gap interval contains 0 (could be root at this node, or uncertain d)
function classify(gap) {
  if (gap.isPos()) return '+';
  if (gap.isNeg()) return '-';
  return '?';
}

function check1_root(psi_deg, delta_deg, rho_lo_deg, rho_hi_deg) {
  const psi = psi_deg * Math.PI / 180;
  const delta = delta_deg * Math.PI / 180;
  const N = 80;
  const step = (rho_hi_deg - rho_lo_deg) / N;
  const grid = [];
  for (let j = 0; j <= N; j++) {
    const rhoDeg = rho_lo_deg + j * step;
    const rho = I.of(rhoDeg * Math.PI / 180);
    const { gap, d, uncertain } = gapH1T1(rho, psi, delta);
    const sign = uncertain ? '?' : classify(gap);
    grid.push({
      rho_deg: rhoDeg, gap_lo: gap.lo, gap_hi: gap.hi,
      d_lo: d.lo, d_hi: d.hi,
      d_multiplicity: d.multiplicity,
      d_widened: d.uncertain,
      sign, uncertain
    });
  }
  // Collect sign changes, allowing '?' as separator between '+' and '-'.
  // A "W candidate" spans from the last definite '+' to the first definite '-'
  // (or reverse), even if intermediate nodes are '?'.
  const changes = [];
  let i = 0;
  while (i < N) {
    const a = grid[i];
    if (a.sign !== '+' && a.sign !== '-') { i++; continue; }
    // look ahead for next definite-sign node of opposite sign
    let j = i + 1;
    let sawUncertain = false;
    while (j <= N && grid[j].sign === '?') { sawUncertain = true; j++; }
    if (j <= N && grid[j].sign !== a.sign) {
      changes.push({
        rho_a_deg: a.rho_deg,
        rho_b_deg: grid[j].rho_deg,
        sign_a: a.sign,
        sign_b: grid[j].sign,
        through_uncertain: sawUncertain,
        uncertain_count: j - i - 1
      });
      i = j;
    } else {
      i++;
    }
  }
  const hasUncertain = grid.some(g => g.uncertain || g.sign === '?');
  const hasWidened = grid.some(g => g.d_widened);
  let W = null, existence, uniqueness;
  if (changes.length === 1) {
    W = [changes[0].rho_a_deg, changes[0].rho_b_deg];
    if (changes[0].through_uncertain || hasWidened) {
      existence = 'undetermined_with_W';
      uniqueness = 'practical_with_uncertain_nodes';
    } else {
      existence = 'yes';
      uniqueness = 'practical_one_change';
    }
  } else if (changes.length === 0 && !hasUncertain && !hasWidened) {
    existence = 'no';
    uniqueness = 'no_change';
  } else if (changes.length === 0) {
    existence = 'undetermined';
    uniqueness = 'undetermined_grid';
  } else {
    existence = 'undetermined';
    uniqueness = 'multiple_sign_changes';
  }
  let minGapLo = Infinity, minGapLoRho = null;
  let maxGapHi = -Infinity, maxGapHiRho = null;
  let countUncertain = 0, countWidened = 0, maxMultiplicity = 0;
  for (const g of grid) {
    if (g.gap_lo < minGapLo) { minGapLo = g.gap_lo; minGapLoRho = g.rho_deg; }
    if (g.gap_hi > maxGapHi) { maxGapHi = g.gap_hi; maxGapHiRho = g.rho_deg; }
    if (g.uncertain) countUncertain++;
    if (g.d_widened) countWidened++;
    if (g.d_multiplicity > maxMultiplicity) maxMultiplicity = g.d_multiplicity;
  }
  return {
    check: 'check1_root',
    config: { psi_deg, delta_deg, rho_bracket_deg: [rho_lo_deg, rho_hi_deg], with: 'T1', side: 1 },
    grid_points: N + 1,
    grid_step_deg: step,
    grid: grid,
    grid_summary: {
      min_gap_lo: minGapLo, min_gap_lo_rho_deg: minGapLoRho,
      max_gap_hi: maxGapHi, max_gap_hi_rho_deg: maxGapHiRho,
      count_uncertain: countUncertain,
      count_widened: countWidened,
      max_d_multiplicity: maxMultiplicity
    },
    sign_changes: changes,
    W_deg: W,
    existence,
    uniqueness,
    notes: 'Existence via IVT on gap_H1_T1(ρ) = 0; sign-changes may pass through "?" nodes. gapH1T1 computes gap on full [d.lo, d.hi] bracket — does not fall back to [-1,1] on d uncertainty. solveD scans d ∈ [0.3, 3.5]; if multiple straddles, uses the smallest (first contact with T2) and sets multiplicity > 1 (open question for review). sin/cos via Math.* with field 1e-12 — practical envelope. buildH1 applies full §2 link rule (mirror axis then rotate).'
  };
}

module.exports = { check1_root };
```

### FILE: a5/check2_penetration.js
```js
'use strict';
const { I } = require('./lib/ia');
const { V } = require('./lib/vec');
const { distPointToMidCircle } = require('./lib/geom');
const { hangDirection, rodrigues } = require('./lib/frame');

const A_T2 = V.of([0, 0, 4]);
const Y_HAT = V.of([0, 1, 0]);
const EX = V.of([1, 0, 0]), EY = Y_HAT, EZ = V.of([0, 0, 1]);
const SIDE = 1;

function buildH1(rho_I, d_I, psi, delta) {
  const e = hangDirection(rho_I, psi, EX, EY, EZ, SIDE);
  const u_dot_T = e.dot(Y_HAT);
  const T_prime = Y_HAT.sub(e.scale(u_dot_T.mul(I.of(2))));
  const n_raw = e.cross(Y_HAT);
  let n;
  try {
    n = n_raw.unit();
  } catch (err) {
    throw new Error('n degenerate at ρ=' + (rho_I.mid() * 180 / Math.PI));
  }
  const T_H1 = rodrigues(T_prime, n, delta);
  const A_H1 = A_T2.add(e.scale(d_I));
  return { A_H1, T_H1 };
}

function checkTheta(theta, W_deg, N_rho, dMid, dPad, psi, delta) {
  const P = V.of([0, Math.sin(theta), 3 - Math.cos(theta)]);
  let distMax = -Infinity;
  let distMin = Infinity;
  let hitCount = 0;
  for (let j = 0; j <= N_rho; j++) {
    const rhoDeg = W_deg[0] + j * (W_deg[1] - W_deg[0]) / N_rho;
    const rho = I.of(rhoDeg * Math.PI / 180);
    const d_I = new I(dMid - dPad, dMid + dPad);
    let H;
    try { H = buildH1(rho, d_I, psi, delta); } catch (e) { continue; }
    hitCount++;
    const dist = distPointToMidCircle(P, H.A_H1, H.T_H1);
    if (dist.hi > distMax) distMax = dist.hi;
    if (dist.lo < distMin) distMin = dist.lo;
  }
  if (hitCount === 0) return null;
  return { distMax, distMin, body_bound: 0.5 };
}

function check2_penetration(W_deg, d_lo, d_hi, psi_deg, delta_deg) {
  if (!W_deg) {
    return {
      check: 'check2_penetration',
      found: false,
      error: 'no_W_from_check1',
      coverage: 'NONE — no single-interval W from check1.',
      notes: 'Cannot run: check1 returned no single-interval W.'
    };
  }
  const psi = psi_deg * Math.PI / 180;
  const delta = delta_deg * Math.PI / 180;
  const N_theta = 720;
  const N_rho = 50;
  const dMid = (d_lo + d_hi) / 2;
  const dPad = (d_hi - d_lo) / 2 + 0.01;
  let best = null;
  for (let j = 0; j < N_theta; j++) {
    const thetaDeg = j * 360 / N_theta;
    const theta = thetaDeg * Math.PI / 180;
    const r = checkTheta(theta, W_deg, N_rho, dMid, dPad, psi, delta);
    if (r && r.distMax < 0.5) {
      if (!best || r.distMax < best.distMax) {
        best = { theta_deg: thetaDeg, distMax: r.distMax, distMin: r.distMin };
      }
    }
  }
  const found = !!best;
  return {
    check: 'check2_penetration',
    config: { psi_deg, delta_deg, side: 1 },
    W_deg,
    theta_grid_points: N_theta,
    rho_grid_points: N_rho + 1,
    found,
    theta_deg: found ? best.theta_deg : null,
    dist_H1_body_hi: found ? best.distMax : null,
    body_bound: 0.5,
    coverage: found
      ? 'PARTIAL — W is a union of undetermined boxes; uniqueness of the root is not proven. Penetration shown for sampled ρ ∈ W and all θ in a 720-point grid.'
      : 'NOT_FOUND — no θ in the grid gave strict penetration for all sampled ρ ∈ W.',
    notes: 'If found=true: point on R1 is strictly inside H1 body. Per Integrator 03.11: PARTIAL coverage — uniqueness of the root not proven. buildH1 applies full §2 link rule (mirror axis then rotate).'
  };
}

module.exports = { check2_penetration };
```

### FILE: a5/run.js
```js
'use strict';
const fs = require('fs');
const path = require('path');
const { check1_root } = require('./check1_root');
const { check2_penetration } = require('./check2_penetration');

function parseArgs(argv) {
  const args = { psi: 56, delta: 10, rho_lo: 45, rho_hi: 65 };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    const take = (key) => { if (i + 1 >= argv.length) { console.error('missing value for ' + key); process.exit(2); } return parseFloat(argv[++i]); };
    if (a === '--psi') args.psi = take(a);
    else if (a === '--delta') args.delta = take(a);
    else if (a === '--rho-lo') args.rho_lo = take(a);
    else if (a === '--rho-hi') args.rho_hi = take(a);
    else if (a.startsWith('--psi=')) args.psi = parseFloat(a.slice(6));
    else if (a.startsWith('--delta=')) args.delta = parseFloat(a.slice(8));
    else if (a.startsWith('--rho-lo=')) args.rho_lo = parseFloat(a.slice(9));
    else if (a.startsWith('--rho-hi=')) args.rho_hi = parseFloat(a.slice(9));
    else { console.error('unknown arg: ' + a); process.exit(2); }
  }
  for (const k of ['psi', 'delta', 'rho_lo', 'rho_hi']) {
    if (!isFinite(args[k])) { console.error('invalid --' + k.replace('_', '-') + ': ' + args[k]); process.exit(2); }
  }
  if (args.rho_lo >= args.rho_hi) { console.error('rho-lo must be < rho-hi'); process.exit(2); }
  return args;
}

function main() {
  const outDir = process.env.KT1_OUT;
  if (!outDir) { console.error('KT1_OUT not set'); process.exit(2); }
  const { psi, delta, rho_lo, rho_hi } = parseArgs(process.argv);
  console.log(`a5/run.js: psi=${psi} delta=${delta} rho=[${rho_lo}, ${rho_hi}]`);
  console.log('a5/run.js: starting check1_root...');
  const c1 = check1_root(psi, delta, rho_lo, rho_hi);
  const gs = c1.grid_summary;
  console.log(`  existence=${c1.existence} uniqueness=${c1.uniqueness} W_deg=${JSON.stringify(c1.W_deg)}`);
  console.log(`  grid_summary: min_gap_lo=${gs.min_gap_lo.toFixed(6)}@rho=${gs.min_gap_lo_rho_deg.toFixed(2)}deg max_gap_hi=${gs.max_gap_hi.toFixed(6)}@rho=${gs.max_gap_hi_rho_deg.toFixed(2)}deg uncertain=${gs.count_uncertain} widened=${gs.count_widened} max_mult=${gs.max_d_multiplicity}`);
  console.log(`  sign_changes: ${c1.sign_changes.length}`);
  for (const ch of c1.sign_changes) {
    console.log(`    ${ch.sign_a}→${ch.sign_b} at rho∈[${ch.rho_a_deg}, ${ch.rho_b_deg}], through_uncertain=${ch.through_uncertain}, uncertain_count=${ch.uncertain_count}`);
  }
  fs.writeFileSync(path.join(outDir, 'a5.check1.root.json'), JSON.stringify(c1, null, 2));

  let c2;
  if (c1.W_deg) {
    const W = c1.W_deg;
    let d_lo = Infinity, d_hi = -Infinity;
    for (const g of c1.grid) {
      if (g.rho_deg >= W[0] && g.rho_deg <= W[1]) {
        if (g.d_lo < d_lo) d_lo = g.d_lo;
        if (g.d_hi > d_hi) d_hi = g.d_hi;
      }
    }
    if (d_lo === Infinity) { d_lo = 1.5; d_hi = 2.0; }
    console.log(`a5/run.js: starting check2_penetration W_deg=${JSON.stringify(W)} d∈[${d_lo.toFixed(4)}, ${d_hi.toFixed(4)}]...`);
    c2 = check2_penetration(W, d_lo, d_hi, psi, delta);
    console.log(`  found=${c2.found} theta_deg=${c2.theta_deg} dist_hi=${c2.dist_H1_body_hi}`);
  } else {
    c2 = {
      check: 'check2_penetration',
      found: false,
      error: 'no_W_from_check1',
      coverage: 'NONE',
      notes: 'check1 returned no single-interval W; check2 cannot run.'
    };
    console.log('a5/run.js: no W from check1, check2 skipped.');
  }
  fs.writeFileSync(path.join(outDir, 'a5.check2.result.json'), JSON.stringify(c2, null, 2));

  console.log('a5/run.js: done. Wrote a5.check1.root.json, a5.check2.result.json to KT1_OUT.');
}

main();
```

---

#### Что изменилось в rev7 (от rev6)

**Только `a5/check1_root.js`.** Изменения:

1. **`solveD`:** диапазон `d` расширен `[0.5, 3.0] → [0.3, 3.5]`. При multiplicity > 1 берётся **наименьший** straddle (первый контакт H1 с T2); `multiplicity` сохраняется в выводе. Если straddle нет — `uncertain = true`, но bracket = весь `[0.3, 3.5]`, а не искусственный `[dLo, dLo + 0.01]`.
2. **`gapH1T1`:** больше **не** возвращает `[-1, 1]` при `d.uncertain`. Считает `gap(H1, T1)` на широкой вилке `[d.lo, d.hi]` (которая уже есть). Узел `uncertain` — только если `gap.lo <= 0 <= gap.hi`, а не из-за d.
3. **`check1_root`:** sign-change ищется сквозь `?`-узлы. Между определённым `+` и определённым `−` через несколько `?` — это sign-change с флагом `through_uncertain: true`. W строится из последнего `+` и первого `−` (или наоборот). `existence` в этом случае `'undetermined_with_W'` (не `'yes'`, не `'no'`).
4. **`run.js`** — доработан вывод: добавлен `sign_changes: N` и разбивка по каждому `+→−` с указанием `through_uncertain`.

#### Ожидаемое от rev7-прогона

- **k4cal:** `sign_changes: 1` (через `?`), `W_deg` внутри `[57.0, 57.5]`, `existence: 'undetermined_with_W'`, `min_gap_lo < 0`.
- **a5pre:** `sign_changes: 1` (через `?`), `W_deg` внутри `[45, 65]`, `existence: 'undetermined_with_W'`, `min_gap_lo < 0`. Затем check2 запустится и найдёт/не найдёт penetration.

Если `sign_changes: 0` — значит multiplicity = 0 в узлах с `?` и нет straddle в диапазоне `[0.3, 3.5]`. Тогда причина не в W, а в `solveD`/`gap(H1, T2)` при ψ=54°, δ=10° — и это уже другой класс проблемы. Тогда нужен `a5.check1.root.json` rev7 для диагностики.

#### Что остаётся оговоркой (к рецензии Грока)

- **`sin/cos` через `Math.*` с полем 1e-12** — practical envelope, не строгая граница libm.
- **Единственность** — practical_one_change на сетке 0,25°, не формальный Lipschitz по ρ.
- **check2 по точкам ρ ∈ W**, не по всей вилке.
- **`existence: 'undetermined_with_W'`** — честный промежуточный статус: W есть, но покрытие через `?`-узлы. Для окончательного сертификата нужен sign-change без `?`, что требует B1–B3 (строгие `sin/cos`, ящики по ρ, вся вилка W в check2).

#### Состояние

`A-5 = REV7 TEXT SUBMITTED (7 files)`
`run: node a5/run.js [--psi 54] [--delta 10] [--rho-lo 57.0 --rho-hi 57.5]`
`A-5 INDEPENDENT COVERAGE = OPEN`

**Представление Клоду.** Rev7 — исправление логической ошибки в сборке W (пункт 1, 2 выше), плюс расширение диапазона `d` (пункт 3). Изменён **только `check1_root.js`**. Прошу собрать rev7 и прогнать оба случая. Если `sign_changes: 1` (или больше) — W есть, check2 запустится. Если `sign_changes: 0` — проблема глубже, нужен полный `a5.check1.root.json` для диагностики.

STOP.

`A-5 REV8 — MATERIALS (spec §2.1/§2.11 rows, interface §§1–2, 4.1–4.2, rev7 code)` · `ORDER UNCHANGED` · `A5.json — HELD` · `KT-1 KERNEL — FROZEN` · значений ядра нет
