'use strict';
// HONC / Qf / R1 / КТ-1 — WP-0: интервальная арифметика с округлением наружу.
// Опора: ECMAScript задаёт Number::add/subtract/multiply/divide как операции IEEE 754-2019
// binary64 с округлением к ближайшему. Поэтому точный результат лежит в пределах половины
// единицы последнего разряда от вычисленного, и расширение на один шаг вниз и вверх
// (nextDown / nextUp) даёт гарантированную вилку. Math.sqrt, Math.sin и др. НЕ используются
// как источник гарантии: корень проверяется умножением, тригонометрия и арктангенс —
// собственные ряды с остаточным членом. Обоснования — WP0_Error_Bounds.md.

const buf = new Float64Array(1);
const bits = new BigInt64Array(buf.buffer);

function nextUp(x) {
  if (Number.isNaN(x) || x === Infinity) return x;
  if (x === 0) return Number.MIN_VALUE;
  buf[0] = x;
  bits[0] += x > 0 ? 1n : -1n;
  return buf[0];
}
function nextDown(x) { return -nextUp(-x); }

// Вилка — массив [lo, hi]. NaN в любом конце — ошибка вычисления.
function check(v) { if (Number.isNaN(v[0]) || Number.isNaN(v[1]) || v[0] > v[1]) throw new Error('interval: invalid ' + v); return v; }
const I = x => [x, x];
// Десятичное значение входа: целое (|x| < 2^53) точно; иначе — вилка вокруг ближайшего double.
function fromInput(x) {
  if (typeof x !== 'number' || !Number.isFinite(x)) throw new Error('input: not a finite number');
  return Number.isInteger(x) && Math.abs(x) < 2 ** 53 ? [x, x] : [nextDown(x), nextUp(x)];
}

const add = (a, b) => [nextDown(a[0] + b[0]), nextUp(a[1] + b[1])];
const sub = (a, b) => [nextDown(a[0] - b[1]), nextUp(a[1] - b[0])];
const neg = a => [-a[1], -a[0]];
function mul(a, b) {
  const p = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]];
  // 0 * Infinity не встречается в пределах ядра; NaN ловит check.
  return check([nextDown(Math.min(...p)), nextUp(Math.max(...p))]);
}
function div(a, b) {
  if (b[0] <= 0 && b[1] >= 0) return [-Infinity, Infinity];
  const q = [a[0] / b[0], a[0] / b[1], a[1] / b[0], a[1] / b[1]];
  return check([nextDown(Math.min(...q)), nextUp(Math.max(...q))]);
}
function sqr(a) {
  if (a[0] >= 0) return [nextDown(a[0] * a[0]), nextUp(a[1] * a[1])];
  if (a[1] <= 0) return [nextDown(a[1] * a[1]), nextUp(a[0] * a[0])];
  return [0, nextUp(Math.max(a[0] * a[0], a[1] * a[1]))];
}
const hull = (a, b) => [Math.min(a[0], b[0]), Math.max(a[1], b[1])];
const intersect = (a, b) => { const r = [Math.max(a[0], b[0]), Math.min(a[1], b[1])]; return r[0] <= r[1] ? r : null; };
const contains = (a, x) => a[0] <= x && x <= a[1];
const containsZero = a => a[0] <= 0 && a[1] >= 0;
const width = a => nextUp(a[1] - a[0]);
const mid = a => a[0] + (a[1] - a[0]) / 2;
const absMax = a => Math.max(Math.abs(a[0]), Math.abs(a[1]));
function abs(a) { if (a[0] >= 0) return a; if (a[1] <= 0) return neg(a); return [0, absMax(a)]; }

// --- Корень: Math.sqrt — только приближение; граница проверяется умножением.
// lo годится, если nextUp(fl(lo*lo)) <= x (тогда точное lo^2 <= x); hi — если nextDown(fl(hi*hi)) >= x.
function sqrtLo(x) {
  if (x <= 0) return 0;
  let s = Math.sqrt(x);
  for (let k = 0; k < 8 && nextUp(s * s) > x; k++) s = nextDown(s);
  if (nextUp(s * s) > x) throw new Error('sqrtLo: no certified bound');
  return s;
}
function sqrtHi(x) {
  if (x <= 0) return 0;
  let s = Math.sqrt(x);
  for (let k = 0; k < 8 && nextDown(s * s) < x; k++) s = nextUp(s);
  if (nextDown(s * s) < x) throw new Error('sqrtHi: no certified bound');
  return s;
}
function sqrt(a) {
  if (a[1] < 0) throw new Error('sqrt: negative interval');
  return [sqrtLo(Math.max(a[0], 0)), sqrtHi(a[1])];
}

// --- π: Math.PI — ближайший к π double, он меньше π; следующий double больше π.
const PI = [Math.PI, nextUp(Math.PI)];
const HALF_PI = [Math.PI / 2, nextUp(Math.PI) / 2];   // деление на 2 точно
const TWO_PI = [2 * Math.PI, 2 * nextUp(Math.PI)];
const deg2rad = d => mul(d, div(PI, I(180)));
const rad2deg = r => mul(r, div(I(180), PI));

// --- Ряды Тейлора на вилке r (|r| <= ~0.8), с остаточным членом Лагранжа.
const NT = 16;
function sinSeries(r) {
  const r2 = sqr(r);
  let term = r, sum = r;
  for (let i = 1; i <= NT; i++) { term = neg(div(mul(term, r2), I((2 * i) * (2 * i + 1)))); sum = add(sum, term); }
  // |остаток| <= |r|^(2NT+3)/(2NT+3)!
  let R = I(absMax(r));
  let rem = R; for (let k = 2; k <= 2 * NT + 3; k++) rem = div(mul(rem, R), I(k));
  return add(sum, [-rem[1], rem[1]]);
}
function cosSeries(r) {
  const r2 = sqr(r);
  let term = I(1), sum = I(1);
  for (let i = 1; i <= NT; i++) { term = neg(div(mul(term, r2), I((2 * i - 1) * (2 * i)))); sum = add(sum, term); }
  let R = I(absMax(r));
  let rem = I(1); for (let k = 1; k <= 2 * NT + 2; k++) rem = div(mul(rem, R), I(k));
  return add(sum, [-rem[1], rem[1]]);
}
const clampUnit = a => [Math.max(a[0], -1), Math.min(a[1], 1)];

// sin и cos точки x (double): x = k·π/2 + r, вилка r строится через вилку π/2 — тождество верно
// при любом целом k, поэтому выбор k приближённым делением гарантии не портит.
function sinCosPoint(x) {
  if (!Number.isFinite(x)) throw new Error('sinCos: non-finite');
  if (Math.abs(x) > 1e6) return { s: [-1, 1], c: [-1, 1] };
  const k = Math.round(x / (Math.PI / 2));
  const r = sub(I(x), mul(I(k), HALF_PI));
  const s = sinSeries(r), c = cosSeries(r);
  const q = ((k % 4) + 4) % 4;
  const S = [s, c, neg(s), neg(c)][q], C = [c, neg(s), neg(c), s][q];
  return { s: clampUnit(S), c: clampUnit(C) };
}
// Есть ли (возможно) в [lo,hi] точка вида base + 2πm; base — вилка.
function maybeContains(lo, hi, base) {
  const m0 = Math.floor((lo - base[1]) / (2 * Math.PI)) - 1, m1 = Math.ceil((hi - base[0]) / (2 * Math.PI)) + 1;
  for (let m = m0; m <= m1; m++) {
    const p = add(base, mul(I(m), TWO_PI));
    if (p[1] >= lo && p[0] <= hi) return true;
  }
  return false;
}
function sin(a) {
  if (a[1] - a[0] >= 6.3) return [-1, 1];
  let r = hull(sinCosPoint(a[0]).s, sinCosPoint(a[1]).s);
  if (maybeContains(a[0], a[1], HALF_PI)) r = [r[0], 1];
  if (maybeContains(a[0], a[1], neg(HALF_PI))) r = [-1, r[1]];
  return r;
}
function cos(a) {
  if (a[1] - a[0] >= 6.3) return [-1, 1];
  let r = hull(sinCosPoint(a[0]).c, sinCosPoint(a[1]).c);
  if (maybeContains(a[0], a[1], I(0))) r = [r[0], 1];
  if (maybeContains(a[0], a[1], PI)) r = [-1, r[1]];
  return r;
}

// --- Арктангенс: монотонен, вилка — по концам. Точка: сведение к |y| <= tan(π/16)
// двойным удвоением угла atan(y) = 2·atan(y / (1 + sqrt(1 + y^2))), затем знакочередующийся ряд.
const NA = 24;
function atanSmall(y) { // y — вилка в [0, 0.21]
  const y2 = sqr(y);
  let term = y, sum = y;
  for (let i = 1; i <= NA; i++) { term = neg(mul(term, y2)); sum = add(sum, div(term, I(2 * i + 1))); }
  // |остаток| <= |y|^(2NA+3)/(2NA+3)
  let rem = I(absMax(y)); for (let k = 1; k < 2 * NA + 3; k++) rem = mul(rem, I(absMax(y)));
  rem = div(rem, I(2 * NA + 3));
  return add(sum, [-rem[1], rem[1]]);
}
function halveTan(y) { return div(y, add(I(1), sqrt(add(I(1), sqr(y))))); }
function atanUnit(y) { // y — вилка в [0, 1]
  const y2 = halveTan(halveTan(y));
  return mul(I(4), atanSmall(y2));
}
function atanPoint(x) {
  if (x === 0) return [0, 0];
  if (x < 0) return neg(atanPoint(-x));
  if (x <= 1) return atanUnit(I(x));
  return sub(HALF_PI, atanUnit(div(I(1), I(x))));
}
function atan(a) { return [atanPoint(a[0])[0], atanPoint(a[1])[1]]; }

// atan2 для вилок; угол в (−π, π]. При рамке, задевающей начало координат или ветвь разреза,
// возвращается широкая, но верная вилка и флаг.
function atan2(y, x) {
  if (x[0] > 0) return { v: atan(div(y, x)), cut: false };
  if (y[0] > 0) return { v: sub(HALF_PI, atan(div(x, y))), cut: false };
  if (y[1] < 0) return { v: sub(neg(HALF_PI), atan(div(x, y))), cut: false };
  if (x[1] < 0) {
    if (y[0] >= 0) return { v: add(PI, atan(div(y, x))), cut: false };
    if (y[1] <= 0) return { v: sub(atan(div(y, x)), PI), cut: false };
    return { v: [-PI[1], PI[1]], cut: true };
  }
  return { v: [-PI[1], PI[1]], cut: true };
}

module.exports = {
  nextUp, nextDown, I, fromInput, add, sub, neg, mul, div, sqr, sqrt, abs, hull, intersect, contains,
  containsZero, width, mid, absMax, PI, HALF_PI, TWO_PI, deg2rad, rad2deg, sin, cos, sinCosPoint,
  atan, atanPoint, atan2, check,
};
