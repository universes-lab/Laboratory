'use strict';
// HONC / Qf / R1 / КТ-1 — WP-0: гарантированные процедуры.
//  minimize — глобальный минимум функции одной переменной ветвями и границами по константе Липшица;
//  root     — вилка корня с проверкой существования и единственности;
//  perimeter — периметр эллипса через полный эллиптический интеграл второго рода (AGM) с вилкой.
// Обоснования границ — WP0_Error_Bounds.md.
const iv = require('./wp0_interval');

// ---------------- minimize ----------------
// f(x) -> вилка [lo, hi] значения в точке x (предоставляется вызывающим; за её верность отвечает он).
// L — константа Липшица на [a, b] (за её верность отвечает вызывающий; ядро её не проверяет).
// Нижняя граница на отрезке [l, r] с точкой m внутри: f(m).lo − L·max(m − l, r − m).
function minimize({ f, a, b, L, tol = 1e-12, maxEval = 200000, keepTol }) {
  if (!(a < b) || !(L >= 0)) throw new Error('minimize: bad arguments');
  const evalAt = x => { const v = iv.check(f(x)); return v; };
  const box = (l, r) => {
    const m = l + (r - l) / 2;
    const fm = evalAt(m);
    const hw = Math.max(iv.nextUp(m - l), iv.nextUp(r - m));
    const lb = iv.sub(I0(fm[0]), iv.mul(iv.I(L), iv.I(hw)))[0];
    return { l, r, m, fm, lb };
  };
  const I0 = x => [x, x];
  // двоичная куча по lb
  const heap = [];
  const push = x => { heap.push(x); let i = heap.length - 1; while (i > 0) { const p = (i - 1) >> 1; if (heap[p].lb <= heap[i].lb) break; [heap[p], heap[i]] = [heap[i], heap[p]]; i = p; } };
  const pop = () => { const top = heap[0], last = heap.pop(); if (heap.length) { heap[0] = last; let i = 0; for (;;) { const l = 2 * i + 1, r = l + 1; let s = i; if (l < heap.length && heap[l].lb < heap[s].lb) s = l; if (r < heap.length && heap[r].lb < heap[s].lb) s = r; if (s === i) break; [heap[s], heap[i]] = [heap[i], heap[s]]; i = s; } } return top; };
  let evals = 0;
  const first = box(a, b); evals++;
  let U = first.fm[1], Uat = first.m;
  push(first);
  let converged = false;
  while (heap.length) {
    const top = heap[0];
    if (iv.nextUp(U - top.lb) <= tol) { converged = true; break; }
    if (evals + 2 > maxEval) break;
    pop();
    if (top.lb > U) continue;
    const parts = [box(top.l, top.m), box(top.m, top.r)]; evals += 2;
    for (const p of parts) { if (p.fm[1] < U) { U = p.fm[1]; Uat = p.m; } }
    for (const p of parts) if (p.lb <= U) push(p);
  }
  const lbMin = heap.length ? Math.min(heap[0].lb, U) : U;
  // Кандидаты в точки минимума: все отрезки, где нижняя граница не выше U + keepTol.
  const kt = keepTol === undefined ? tol : keepTol;
  const cand = heap.filter(x => x.lb <= U + kt).map(x => [x.l, x.r]).sort((p, q) => p[0] - q[0]);
  const argmin = [];
  for (const c of cand) { const last = argmin[argmin.length - 1]; if (last && c[0] <= last[1]) last[1] = Math.max(last[1], c[1]); else argmin.push([c[0], c[1]]); }
  if (!argmin.length) argmin.push([Uat, Uat]);
  return { min: [lbMin, U], argmin, evals, converged, completeness: 'CERTIFIED' };
}

// ---------------- root ----------------
// F(lo, hi) -> вилка значений F на [lo, hi]; dF(lo, hi) -> вилка производной. F непрерывна.
// Корень существует, если знаки F на концах отрезка строго различны; единствен на отрезке,
// где вилка производной не содержит 0. Весь [a, b] разбивается, пока каждый кусок не станет
// либо без корня (вилка F не содержит 0), либо монотонным (вилка dF не содержит 0).
function root({ F, dF, a, b, tol = 1e-14, maxDepth = 40 }) {
  const pieces = [];
  let ambiguous = 0;
  const sgn = v => (v[0] > 0 ? 1 : v[1] < 0 ? -1 : 0);
  function classify(l, r, depth) {
    const Fv = iv.check(F(l, r));
    if (!iv.containsZero(Fv)) return;                         // корней нет
    const D = iv.check(dF(l, r));
    if (!iv.containsZero(D)) {
      const sl = sgn(F(l, l)), sr = sgn(F(r, r));
      if (sl !== 0 && sr !== 0) { if (sl !== sr) pieces.push([l, r]); return; }  // ровно один или ни одного
    }
    if (depth >= maxDepth) { ambiguous++; return; }
    const m = l + (r - l) / 2;
    if (!(m > l && m < r)) { ambiguous++; return; }
    classify(l, m, depth + 1); classify(m, r, depth + 1);
  }
  classify(a, b, 0);
  const exists = pieces.length >= 1;
  const unique = pieces.length === 1 && ambiguous === 0;
  if (!exists) return { exists: false, unique: false, root: null, completeness: 'UNRESOLVED', reason: ambiguous ? 'корень не отделён' : 'корня нет на отрезке' };
  // сужение первого куска делением пополам по знаку
  let [l, r] = pieces[0];
  const sl0 = sgn(F(l, l));
  for (let k = 0; k < 200 && iv.nextUp(r - l) > tol; k++) {
    const m = l + (r - l) / 2;
    if (!(m > l && m < r)) break;
    const sm = sgn(F(m, m));
    if (sm === 0) break;               // знак в середине не определён: корень по-прежнему в [l, r]
    if (sm === sl0) l = m; else r = m;
  }
  return {
    exists, unique, root: [l, r], pieces: pieces.length, ambiguous,
    completeness: unique ? 'CERTIFIED' : 'UNRESOLVED',
    reason: unique ? null : (pieces.length > 1 ? 'на отрезке больше одного корня' : 'единственность не доказана'),
  };
}

// ---------------- perimeter ----------------
// Периметр эллипса с полуосями s1, s2 (числа или вилки), формула через AGM:
//   a0 = max, b0 = min, c0^2 = a0^2 − b0^2;  a_{n+1} = (a_n + b_n)/2, b_{n+1} = sqrt(a_n b_n), c_{n+1} = (a_n − b_n)/2;
//   P = 2π · (a0^2 − Σ_{n>=0} 2^{n−1} c_n^2) / M,  M = AGM(a0, b0) ∈ [b_n, a_n] при любом n.
// Хвост суммы после шага N: Σ_{m>N} 2^{m−1} c_m^2 <= 2^{N+1} c_{N+1}^2, пока c_m <= 2·b0 (WP0_Error_Bounds.md, § 4).
function perimeter(s1, s2) {
  const A = Array.isArray(s1) ? s1 : iv.I(s1), B = Array.isArray(s2) ? s2 : iv.I(s2);
  if (A[0] <= 0 || B[0] <= 0) throw new Error('perimeter: semi-axes must be positive');
  // Член n = 0 объединён с a0^2: a0^2 − ½·c0^2 = ½(a0^2 + b0^2). Так формула симметрична по
  // полуосям и не требует знать, какая из них больше (вилки могут перекрываться).
  let a = A, b = B;
  const b0lo = Math.min(A[0], B[0]);
  const base = iv.mul(iv.I(0.5), iv.add(iv.sqr(A), iv.sqr(B)));
  let S = iv.I(0);
  let pow2 = 0.5;
  for (let n = 0; n < 60; n++) {
    const an1 = iv.mul(iv.I(0.5), iv.add(a, b));
    const bn1 = iv.sqrt(iv.mul(a, b));
    let cn1 = iv.mul(iv.I(0.5), iv.sub(a, b)); cn1 = iv.abs(cn1);
    pow2 *= 2;                          // 2^{(n+1)-1}
    S = iv.add(S, iv.mul(iv.I(pow2), iv.sqr(cn1)));
    a = an1; b = bn1;
    // остановка: вклад члена пренебрежимо мал, а хвост оценивается ниже строго
    if (pow2 * cn1[1] * cn1[1] <= 1e-22 * base[0] && cn1[1] <= 2 * b0lo) break;
  }
  // хвост: c_{N+2} <= c_{N+1}^2/(4 b0); оцениваем следующий член и удваиваем
  const cNext = (() => { const c = iv.mul(iv.I(0.5), iv.sub(a, b)); return iv.absMax(c); })();
  if (!(cNext <= 2 * b0lo)) throw new Error('perimeter: tail bound precondition failed');
  const tail = iv.mul(iv.I(2 * pow2 * 2), iv.sqr(iv.I(cNext)));
  S = iv.add(S, [0, tail[1]]);
  const M = [Math.min(a[0], b[0]), Math.max(a[1], b[1])];   // AGM ∈ [b_n, a_n]
  const num = iv.sub(base, S);
  const P = iv.mul(iv.TWO_PI, iv.div(num, M));
  return { value: P, completeness: 'CERTIFIED' };
}

module.exports = { minimize, root, perimeter };
