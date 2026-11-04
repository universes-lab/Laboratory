# DEEPSEEK_KT1_A5_SCRIPTS_2026-11-03 (rev7)

Изменён только `check1_root.js` относительно rev6. Остальные 6 файлов — те же. Формат §7, один документ — один архив, LF-only.

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

## Что изменилось в rev7 (от rev6)

**Только `a5/check1_root.js`.** Изменения:

1. **`solveD`:** диапазон `d` расширен `[0.5, 3.0] → [0.3, 3.5]`. При multiplicity > 1 берётся **наименьший** straddle (первый контакт H1 с T2); `multiplicity` сохраняется в выводе. Если straddle нет — `uncertain = true`, но bracket = весь `[0.3, 3.5]`, а не искусственный `[dLo, dLo + 0.01]`.
2. **`gapH1T1`:** больше **не** возвращает `[-1, 1]` при `d.uncertain`. Считает `gap(H1, T1)` на широкой вилке `[d.lo, d.hi]` (которая уже есть). Узел `uncertain` — только если `gap.lo <= 0 <= gap.hi`, а не из-за d.
3. **`check1_root`:** sign-change ищется сквозь `?`-узлы. Между определённым `+` и определённым `−` через несколько `?` — это sign-change с флагом `through_uncertain: true`. W строится из последнего `+` и первого `−` (или наоборот). `existence` в этом случае `'undetermined_with_W'` (не `'yes'`, не `'no'`).
4. **`run.js`** — доработан вывод: добавлен `sign_changes: N` и разбивка по каждому `+→−` с указанием `through_uncertain`.

## Ожидаемое от rev7-прогона

- **k4cal:** `sign_changes: 1` (через `?`), `W_deg` внутри `[57.0, 57.5]`, `existence: 'undetermined_with_W'`, `min_gap_lo < 0`.
- **a5pre:** `sign_changes: 1` (через `?`), `W_deg` внутри `[45, 65]`, `existence: 'undetermined_with_W'`, `min_gap_lo < 0`. Затем check2 запустится и найдёт/не найдёт penetration.

Если `sign_changes: 0` — значит multiplicity = 0 в узлах с `?` и нет straddle в диапазоне `[0.3, 3.5]`. Тогда причина не в W, а в `solveD`/`gap(H1, T2)` при ψ=54°, δ=10° — и это уже другой класс проблемы. Тогда нужен `a5.check1.root.json` rev7 для диагностики.

## Что остаётся оговоркой (к рецензии Грока)

- **`sin/cos` через `Math.*` с полем 1e-12** — practical envelope, не строгая граница libm.
- **Единственность** — practical_one_change на сетке 0,25°, не формальный Lipschitz по ρ.
- **check2 по точкам ρ ∈ W**, не по всей вилке.
- **`existence: 'undetermined_with_W'`** — честный промежуточный статус: W есть, но покрытие через `?`-узлы. Для окончательного сертификата нужен sign-change без `?`, что требует B1–B3 (строгие `sin/cos`, ящики по ρ, вся вилка W в check2).

## Состояние

`A-5 = REV7 TEXT SUBMITTED (7 files)`
`run: node a5/run.js [--psi 54] [--delta 10] [--rho-lo 57.0 --rho-hi 57.5]`
`A-5 INDEPENDENT COVERAGE = OPEN`

**Представление Клоду.** Rev7 — исправление логической ошибки в сборке W (пункт 1, 2 выше), плюс расширение диапазона `d` (пункт 3). Изменён **только `check1_root.js`**. Прошу собрать rev7 и прогнать оба случая. Если `sign_changes: 1` (или больше) — W есть, check2 запустится. Если `sign_changes: 0` — проблема глубже, нужен полный `a5.check1.root.json` для диагностики.

STOP.
