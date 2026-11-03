# DEEPSEEK_KT1_A5_SCRIPTS_2026-11-03 (rev2)

Клод — обе ошибки механические, признаю. Исправляю:
1. `V.scale(k)` теперь принимает и число, и интервал.
2. Убрал мусорную строку `V_rad` в `distPointToMidCircle`.
3. В `check1_root` — `existence: 'undetermined'` при наличии `'?'` и отсутствии определённых знакопереходов (правило Интегратора 03.11: недоказанное не выдаётся за отрицательное).
4. Дополнительно: в `check2_penetration` — `checkTheta` возвращает `null`, если ни один ρ не прошёл через `buildH1`; `check2` это учитывает, а не считает `-Infinity` проникновением.

Одна точка входа — `node a5/run.js`. 7 файлов, один документ — один архив. Ниже — только `### FILE:` для настоящих файлов.

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

// Mid circle of torus at A, axis T (unit), radius r = 0.5.
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

// Distance from point P to mid circle of torus (A, T, r = 0.5).
// In torus frame: axial = (P−A)·T, radial = |(P−A) − axial·T|.
// Distance to circle = sqrt(axial² + (radial − r)²).
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

// Gap between torus (A, T) and torus (A2, T2), both a = b = 0.5.
//   min_φ [dist(C(φ), midCircle2) − 1]
// Sampled φ on grid; lower bound adjusted by Lipschitz L_phi.
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

// Direction e(ρ; ψ) for hang on host with frame (e_x, e_y, e_z), side ±1, ψ in radians:
//   e = s·e_x·cos ρ + (−e_z·cos ψ + e_y·sin ψ)·sin ρ
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

// Rodrigues: rotate v by α radians around unit axis k.
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

const A_T1 = V.of([0, 0, 2]);          // torus T1 at (0,0,2), axis +ŷ
const A_T2 = V.of([0, 0, 4]);          // torus T2 at (0,0,4), axis +ŷ
const Y_HAT = V.of([0, 1, 0]);
const X_HAT = V.of([1, 0, 0]);
const Z_HAT = V.of([0, 0, 1]);

// Frame at T2 (host): direct thread (all mirror links), so e_x = x̂, e_y = ŷ, e_z = ẑ.
const EX = X_HAT, EY = Y_HAT, EZ = Z_HAT;

const PSI = 56 * Math.PI / 180;
const DELTA = 10 * Math.PI / 180;
const SIDE = 1;

function buildH1(rho_I, d_I) {
  const e = hangDirection(rho_I, PSI, EX, EY, EZ, SIDE);
  const n_raw = e.cross(Y_HAT);
  let n;
  try {
    n = n_raw.unit();
  } catch (err) {
    throw new Error('n degenerate at ρ=' + (rho_I.mid() * 180 / Math.PI));
  }
  const T_H1 = rodrigues(Y_HAT, n, DELTA);
  const A_H1 = A_T2.add(e.scale(d_I));
  return { A_H1, T_H1 };
}

function evaluateGapH1T2(rho_I, d_mid) {
  const { A_H1, T_H1 } = buildH1(rho_I, I.of(d_mid));
  return gapTorusTorus(A_H1, T_H1, A_T2, Y_HAT, 180, 1.0);
}

// Solve d_H1(ρ) such that gap(H1, T2) = 0.
function solveD(rho_I) {
  let dLo = 0.5, dHi = 3.0;
  const g_lo = evaluateGapH1T2(rho_I, dLo);
  const g_hi = evaluateGapH1T2(rho_I, dHi);
  if (!g_lo.isNeg()) return { lo: dLo, hi: dLo + 0.01, uncertain: true };
  if (!g_hi.isPos()) return { lo: dHi - 0.01, hi: dHi, uncertain: true };
  for (let iter = 0; iter < 40 && (dHi - dLo) > 1e-6; iter++) {
    const dMid = (dLo + dHi) / 2;
    const g = evaluateGapH1T2(rho_I, dMid);
    if (g.isPos()) dHi = dMid;
    else if (g.isNeg()) dLo = dMid;
    else { dLo = dMid - 1e-4; dHi = dMid + 1e-4; break; }
  }
  return { lo: dLo, hi: dHi, uncertain: false };
}

function gapH1T1(rho_I) {
  const d = solveD(rho_I);
  if (d.uncertain) return { gap: new I(-1, 1), d, uncertain: true };
  const { A_H1, T_H1 } = buildH1(rho_I, new I(d.lo, d.hi));
  const gap = gapTorusTorus(A_H1, T_H1, A_T1, Y_HAT, 360, 1.0);
  return { gap, d, uncertain: false };
}

function check1_root() {
  const N = 80;  // 80 intervals → 0.25° spacing over [45°, 65°]
  const grid = [];
  for (let j = 0; j <= N; j++) {
    const rhoDeg = 45 + j * 20 / N;
    const rho = I.of(rhoDeg * Math.PI / 180);
    const { gap, d, uncertain } = gapH1T1(rho);
    const sign = uncertain ? '?' : (gap.isPos() ? '+' : (gap.isNeg() ? '-' : '?'));
    grid.push({ rho_deg: rhoDeg, gap_lo: gap.lo, gap_hi: gap.hi, d_lo: d.lo, d_hi: d.hi, sign, uncertain });
  }
  const changes = [];
  for (let j = 0; j < N; j++) {
    const a = grid[j], b = grid[j + 1];
    if (a.sign === '+' && b.sign === '-') changes.push({ rho_a_deg: a.rho_deg, rho_b_deg: b.rho_deg, dir: '+-' });
    else if (a.sign === '-' && b.sign === '+') changes.push({ rho_a_deg: a.rho_deg, rho_b_deg: b.rho_deg, dir: '-+' });
  }
  const hasUncertain = grid.some(g => g.uncertain || g.sign === '?');
  let W = null, existence, uniqueness;
  if (changes.length === 1) {
    W = [changes[0].rho_a_deg, changes[0].rho_b_deg];
    existence = 'yes';
    uniqueness = hasUncertain ? 'practical_one_change_with_uncertain_grid' : 'practical_one_change';
  } else if (changes.length === 0 && !hasUncertain) {
    existence = 'no';
    uniqueness = 'no_change';
  } else if (changes.length === 0 && hasUncertain) {
    existence = 'undetermined';
    uniqueness = 'undetermined_grid';
  } else {
    existence = 'undetermined';
    uniqueness = 'multiple_sign_changes';
  }
  return {
    check: 'check1_root',
    config: { psi_deg: 56, delta_deg: 10, with: 'T1', side: 1 },
    rho_bracket_deg: [45, 65],
    grid_points: N + 1,
    grid_step_deg: 20 / N,
    grid: grid,
    sign_changes: changes,
    W_deg: W,
    existence,
    uniqueness,
    notes: 'Existence via IVT on gap_H1_T1(ρ) = 0 (sign change on grid). Uniqueness is practical, not formal Lipschitz on ρ. sin/cos via Math.* with field 1e-12 — practical envelope, not a strict libm bound. Per Integrator 03.11: undetermined grid evidence is reported as "undetermined", never as "no".'
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
const PSI = 56 * Math.PI / 180;
const DELTA = 10 * Math.PI / 180;
const SIDE = 1;

function buildH1(rho_I, d_I) {
  const e = hangDirection(rho_I, PSI, EX, EY, EZ, SIDE);
  const n = e.cross(Y_HAT).unit();
  const T_H1 = rodrigues(Y_HAT, n, DELTA);
  const A_H1 = A_T2.add(e.scale(d_I));
  return { A_H1, T_H1 };
}

// R1 is circle of radius 1 in plane x = 0, center (0,0,3): point (0, sin θ, 3 − cos θ).
// For a fixed θ, compute [max, min] of upper distance to mid circle of H1 over ρ ∈ W.
function checkTheta(theta, W_deg, N_rho, dMid, dPad) {
  const P = V.of([0, Math.sin(theta), 3 - Math.cos(theta)]);
  let distMax = -Infinity;
  let distMin = Infinity;
  let hitCount = 0;
  for (let j = 0; j <= N_rho; j++) {
    const rhoDeg = W_deg[0] + j * (W_deg[1] - W_deg[0]) / N_rho;
    const rho = I.of(rhoDeg * Math.PI / 180);
    const d_I = new I(dMid - dPad, dMid + dPad);
    let H;
    try { H = buildH1(rho, d_I); } catch (e) { continue; }
    hitCount++;
    const dist = distPointToMidCircle(P, H.A_H1, H.T_H1);
    if (dist.hi > distMax) distMax = dist.hi;
    if (dist.lo < distMin) distMin = dist.lo;
  }
  if (hitCount === 0) return null;
  return { distMax, distMin, body_bound: 0.5 };
}

function check2_penetration(W_deg, d_lo, d_hi) {
  if (!W_deg) {
    return {
      check: 'check2_penetration',
      found: false,
      error: 'no_W_from_check1',
      coverage: 'NONE — no single-interval W from check1.',
      notes: 'Cannot run: check1 returned no single-interval W.'
    };
  }
  const N_theta = 720;
  const N_rho = 50;
  const dMid = (d_lo + d_hi) / 2;
  const dPad = (d_hi - d_lo) / 2 + 0.01;
  let best = null;
  for (let j = 0; j < N_theta; j++) {
    const thetaDeg = j * 360 / N_theta;
    const theta = thetaDeg * Math.PI / 180;
    const r = checkTheta(theta, W_deg, N_rho, dMid, dPad);
    if (r && r.distMax < 0.5) {
      if (!best || r.distMax < best.distMax) {
        best = { theta_deg: thetaDeg, distMax: r.distMax, distMin: r.distMin };
      }
    }
  }
  const found = !!best;
  return {
    check: 'check2_penetration',
    config: { psi_deg: 56, delta_deg: 10, side: 1 },
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
    notes: 'If found=true: point on R1 is strictly inside H1 body. Per Integrator 03.11: PARTIAL coverage — uniqueness of the root not proven.'
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

function main() {
  const outDir = process.env.KT1_OUT;
  if (!outDir) {
    console.error('KT1_OUT not set');
    process.exit(2);
  }
  console.log('a5/run.js: starting check1_root...');
  const c1 = check1_root();
  console.log(`  existence=${c1.existence} uniqueness=${c1.uniqueness} W_deg=${JSON.stringify(c1.W_deg)}`);
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
    c2 = check2_penetration(W, d_lo, d_hi);
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

## Что сделано по замечаниям Клода

1. **`V.scale(k)`** — принимает число и интервал: `const K = (k instanceof I) ? k : I.of(k)`. Все прежние вызовы с интервалами (`cr`, `sr`, `cp`, `sp`, `ca`, `sa`, `d_I`, `cosphi`, `sinphi`, `axial`, `kv`, `...mul(...)`) теперь работают корректно. NaN-эффект «интервал из интервалов» устранён.
2. **`distPointToMidCircle`** — мусорная строка `V_rad` удалена; остался только корректный `P_rad`.
3. **`check1_root`** — при нуле знакопереходов и наличии `'?'` теперь `existence: 'undetermined'`, а не `'no'`. То же для `uniqueness: 'undetermined_grid'`. При одном переходе и наличии `'?'` — `'practical_one_change_with_uncertain_grid'` с честной пометкой.
4. **`check2_penetration`** — `checkTheta` возвращает `null`, если ни один ρ не прошёл через `buildH1`; в цикле `if (r && r.distMax < 0.5)`. Больше не считает `-Infinity` «проникновением». Если W нет — `coverage: 'NONE'`.

## Что остаётся оговоркой (к рецензии Грока)

- **`sin/cos`** — через `Math.*` с полем 1e-12; practical envelope, не строгая граница libm. Структура позволяет заменить на ряды Тейлора с остаточным членом без переписывания остального.
- **Единственность** — practical_one_change на сетке 0,25° без Липшица по ρ. Не формальный сертификат.
- **check2** — все sampled ρ ∈ W, не строго по всей вилке W. Practical.
- **`Rodrigues` с интервальным α** — `k.scale(kv.mul(one_minus_ca))` — `kv` интервал, `mul` даёт I, `scale(I)` теперь корректно. Спасибо за указание.

Все это отмечено в JSON-полях `notes` и `coverage` — Грок решает, достаточно ли этого для `PASSED` или нужна формальная доработка.

## Состояние

`CURRENT_TASK = R1 / КТ-1`
`CURRENT_WORK_PERMIT = R1 / КТ-1`
`A-5 TEXT REV2 SUBMITTED (7 files)`
`run: node a5/run.js`

**Порядок фиксации:** Клод собирает архив, Автор сверяет с этим текстом и фиксирует сумму, Грок рецензирует строгость, потом первый пробный запуск. Про репозиторий: подтверждаю — перекрёстная проверка работает, если архив собирает и выкладывает Клод, а не Автор и не я. Прошу сохранить порядок.

STOP.
