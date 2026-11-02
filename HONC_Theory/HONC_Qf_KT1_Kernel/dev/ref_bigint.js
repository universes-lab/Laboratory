'use strict';
// Независимый эталон высокой точности для рабочих проверок WP-0 (не приёмочный набор).
// Фиксированная точка: значение = N / 2^S, S = 256. Алгоритмы намеренно другие, чем в ядре:
// π — формула Мэчина; sin/cos — ряд после сведения по π/2 в фиксированной точке;
// atan — трёхкратное удвоение угла; периметр — ряд Гаусса — Куммера (не AGM).
const S = 256n;
const ONE = 1n << S;

const fbuf = new Float64Array(1), ubuf = new BigUint64Array(fbuf.buffer);
function fromDouble(x) {           // точное значение double, усечённое вниз до 2^-S
  if (x === 0) return 0n;
  fbuf[0] = Math.abs(x);
  const u = ubuf[0];
  const e = Number((u >> 52n) & 0x7ffn), frac = u & ((1n << 52n) - 1n);
  const m = e === 0 ? frac : frac | (1n << 52n);
  const sh = BigInt((e === 0 ? 1 : e) - 1075) + S;
  const v = sh >= 0n ? m << sh : m >> -sh;
  return x < 0 ? -v : v;
}
const mulF = (a, b) => (a * b) >> S;
const divF = (a, b) => (a << S) / b;
function isqrt(n) { if (n < 0n) throw new Error('isqrt'); if (n < 2n) return n; let x = 1n << (BigInt(n.toString(2).length) / 2n + 1n); for (;;) { const y = (x + n / x) >> 1n; if (y >= x) return x; x = y; } }
const sqrtF = a => isqrt(a << S);
function atanInv(n) { const N = BigInt(n), N2 = N * N; let term = ONE / N, sum = term, k = 1n, sign = -1n; for (;;) { term = term / N2; const t = term / (2n * k + 1n); if (t === 0n) break; sum += sign * t; sign = -sign; k++; } return sum; }
const PI = 16n * atanInv(5) - 4n * atanInv(239);
const HALF = PI / 2n;
function sinCosF(x) {
  const k = (x + (x >= 0n ? HALF / 2n : -HALF / 2n)) / HALF;     // ближайшее целое
  const r = x - k * HALF;
  const r2 = mulF(r, r);
  let ts = r, s = r, tc = ONE, c = ONE;
  for (let i = 1n; ; i++) {
    ts = -mulF(ts, r2) / ((2n * i) * (2n * i + 1n)); tc = -mulF(tc, r2) / ((2n * i - 1n) * (2n * i));
    if (ts === 0n && tc === 0n) break; s += ts; c += tc;
  }
  const q = Number(((k % 4n) + 4n) % 4n);
  return { s: [s, c, -s, -c][q], c: [c, -s, -c, s][q] };
}
function atanF(x) {
  if (x < 0n) return -atanF(-x);
  if (x > ONE) return HALF - atanF(divF(ONE, x));
  let y = x;
  for (let k = 0; k < 3; k++) y = divF(y, ONE + sqrtF(ONE + mulF(y, y)));
  const y2 = mulF(y, y);
  let t = y, sum = y;
  for (let i = 1n; ; i++) { t = -mulF(t, y2); const d = t / (2n * i + 1n); if (d === 0n) break; sum += d; }
  return 8n * sum;
}
// Периметр по ряду Гаусса — Куммера: P = π(a+b) Σ [C(1/2,n)]^2 h^n, h = ((a−b)/(a+b))^2.
function perimeterF(a, b) {
  const h = mulF(divF(a - b, a + b), divF(a - b, a + b));
  let t = ONE, sum = ONE;
  for (let n = 1n; n < 100000n; n++) {
    t = (mulF(t, h) * (2n * n - 3n) * (2n * n - 3n)) / ((2n * n) * (2n * n));
    if (t === 0n) break; sum += t;
  }
  return mulF(mulF(PI, a + b), sum);
}
const toNum = v => Number(v) / 2 ** 256;
module.exports = { S, ONE, fromDouble, mulF, divF, sqrtF, PI, sinCosF, atanF, perimeterF, toNum };
