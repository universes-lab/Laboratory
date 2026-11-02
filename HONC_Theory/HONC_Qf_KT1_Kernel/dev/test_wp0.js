'use strict';
// Рабочие проверки исполнителя по WP-0 (не приёмочный набор: он независимо пишется в Д-3).
// Каждая проверка вложения сравнивает вилку ядра с эталоном высокой точности ref_bigint.js.
const iv = require('../wp0_interval');
const { minimize, root, perimeter } = require('../wp0_cert');
const L = require('../wp0_labels');
const R = require('./ref_bigint');

let pass = 0, fail = 0; const fails = [];
const ok = (c, msg) => { if (c) pass++; else { fail++; fails.push(msg); } };
// вилка [lo, hi] содержит эталон ref (фиксированная точка): lo <= ref <= hi с учётом усечения на 2^-256
const inside = (v, ref) => R.fromDouble(v[0]) <= ref + 1n && ref - 1n <= R.fromDouble(v[1]) + 1n;

// детерминированный генератор
let seed = 12345; const rnd = () => { seed = (seed * 1103515245 + 12345) % 2147483648; return seed / 2147483648; };

// 1. sin / cos в точках
let maxW = 0;
const pts = [0, 1e-300, -1e-300, 1e-8, Math.PI / 2, Math.PI, -Math.PI, 3 * Math.PI / 2, 2 * Math.PI, 100, -100, 1e5];
for (let i = 0; i < 3000; i++) pts.push((rnd() * 2 - 1) * 40);
for (const x of pts) {
  const { s, c } = iv.sinCosPoint(x); const ref = R.sinCosF(R.fromDouble(x));
  ok(inside(s, ref.s), `sin(${x})`); ok(inside(c, ref.c), `cos(${x})`);
  maxW = Math.max(maxW, s[1] - s[0], c[1] - c[0]);
}
console.log(`sin/cos в точках: ${pts.length} точек, наибольшая ширина вилки ${maxW.toExponential(2)}`);

// 2. sin / cos на отрезках: экстремумы внутри
ok(iv.sin([1.5, 1.7])[1] === 1, 'sin [1.5,1.7] включает 1');
ok(iv.cos([3.1, 3.2])[0] === -1, 'cos [3.1,3.2] включает -1');
ok(iv.cos([-0.1, 0.1])[1] === 1, 'cos [-0.1,0.1] включает 1');
for (let i = 0; i < 500; i++) {
  const a = (rnd() * 2 - 1) * 20, w = rnd() * 3, v = iv.sin([a, a + w]), u = iv.cos([a, a + w]);
  for (let j = 0; j <= 8; j++) { const t = a + w * j / 8; const ref = R.sinCosF(R.fromDouble(t)); ok(inside(v, ref.s) && inside(u, ref.c), `sin/cos на [${a}, ${a + w}] в ${t}`); }
}

// 3. arctg
maxW = 0;
const apts = [0, 1e-20, 1, -1, 0.5, 2, 1e10, -1e10];
for (let i = 0; i < 3000; i++) apts.push((rnd() * 2 - 1) * (rnd() < 0.5 ? 2 : 200));
for (const x of apts) { const v = iv.atanPoint(x); ok(inside(v, R.atanF(R.fromDouble(x))), `atan(${x})`); maxW = Math.max(maxW, v[1] - v[0]); }
console.log(`atan в точках: ${apts.length} точек, наибольшая ширина ${maxW.toExponential(2)}`);
// atan2 по четвертям
for (const [y, x] of [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, -1], [1, 0], [-1, 0]]) {
  const v = iv.atan2(iv.I(y), iv.I(x)).v; ok(v[0] <= Math.atan2(y, x) + 1e-15 && Math.atan2(y, x) - 1e-15 <= v[1], `atan2(${y},${x})`);
}

// 4. корень
for (let i = 0; i < 3000; i++) { const x = rnd() * 1e3; const v = iv.sqrt(iv.I(x)); ok(inside(v, R.sqrtF(R.fromDouble(x))), `sqrt(${x})`); }

// 5. π, перевод градусов
ok(inside(iv.PI, R.PI), 'вилка π содержит π');
ok(inside(iv.deg2rad(iv.I(180)), R.PI), '180° = π');

// 6. периметр (AGM) против ряда Гаусса — Куммера
for (const [a, b] of [[1, 1], [1, 0.5], [1, 0.9], [1, 0.3], [2, 1.999], [1.3, 0.7], [0.5, 0.25]]) {
  const P = perimeter(a, b).value; const ref = R.perimeterF(R.fromDouble(a), R.fromDouble(b));
  ok(inside(P, ref), `perimeter(${a},${b})`);
  ok(P[1] - P[0] <= 1e-12, `perimeter(${a},${b}): ширина ${P[1] - P[0]}`);
  console.log(`периметр (${a}, ${b}) = [${P[0]}, ${P[1]}], ширина ${(P[1] - P[0]).toExponential(2)}`);
}
// приближение Рамануджана (мутант м1) — для окружности точно, для вытянутого эллипса выходит из вилки
const raman = (a, b) => { const h = ((a - b) / (a + b)) ** 2; return Math.PI * (a + b) * (1 + 3 * h / (10 + Math.sqrt(4 - 3 * h))); };
{ const P = perimeter(1, 0.5).value; const r = raman(1, 0.5); ok(r < P[0] || r > P[1], 'Рамануджан (1, 0.5) вне вилки AGM — мутант м1 различим'); console.log(`Рамануджан (1, 0.5) − середина вилки = ${(r - iv.mid(P)).toExponential(2)}`); }

// 7. минимум: узкий провал между узлами сетки
{
  const x0 = 0.3141592653589793, K = 100, D = 0.01;
  const f = x => { const d = iv.abs(iv.sub(iv.I(x), iv.I(x0))); const v = iv.mul(iv.I(K), d); return [Math.min(v[0], D), Math.min(v[1], D)]; };
  const r = minimize({ f, a: 0, b: 1, L: K, tol: 1e-9 });
  ok(r.min[0] <= 0 && r.min[1] < 1e-8, `провал: вилка минимума ${r.min}`);
  ok(r.argmin.some(s => s[0] <= x0 && x0 <= s[1]), 'провал: вилка точки минимума содержит x0');
  let gridMin = Infinity; for (let i = 0; i <= 1000; i++) gridMin = Math.min(gridMin, f(i / 1000)[0]);
  ok(gridMin >= D - 1e-12, 'сетка 0,001 провал пропускает (контроль постановки)');
  console.log(`минимум: вилка [${r.min[0].toExponential(2)}, ${r.min[1].toExponential(2)}], вычислений ${r.evals}, сетка 0,001 даёт ${gridMin}`);
}
{ // cos на [0, 7]: минимум −1 в π
  const r = minimize({ f: x => iv.sinCosPoint(x).c, a: 0, b: 7, L: 1, tol: 1e-10 });
  ok(r.min[0] <= -1 && r.min[1] >= -1 && r.min[1] < -1 + 1e-9, `cos min ${r.min}`);
  ok(r.argmin.some(s => s[0] <= Math.PI + 1e-9 && Math.PI - 1e-9 <= s[1]), 'cos argmin содержит π');
}

// 8. корень
{
  const r = root({ F: (l, h) => iv.sub(iv.sqr([l, h]), iv.I(2)), dF: (l, h) => iv.mul(iv.I(2), [l, h]), a: 1, b: 2 });
  ok(r.unique && inside(r.root, R.sqrtF(2n * R.ONE)), `корень √2: ${r.root}`);
  const r2 = root({ F: (l, h) => iv.mul(iv.sub([l, h], iv.I(1)), iv.sub([l, h], iv.I(2))), dF: (l, h) => iv.sub(iv.mul(iv.I(2), [l, h]), iv.I(3)), a: 0, b: 3 });
  ok(!r2.unique && r2.completeness === 'UNRESOLVED', 'два корня: единственность не подтверждена');
  const r3 = root({ F: (l, h) => iv.sin([l, h]), dF: (l, h) => iv.cos([l, h]), a: 3, b: 3.3 });
  ok(r3.unique && inside(r3.root, R.PI), `корень sin около π: ${r3.root}`);
  const r4 = root({ F: (l, h) => { const x = [l, h]; return iv.mul(iv.sqr(x), x); }, dF: (l, h) => iv.mul(iv.I(3), iv.sqr([l, h])), a: -1, b: 1 });
  ok(!r4.unique, 'кратный корень x^3: единственность честно не доказана');
}

// 9. метки и правило вердикта
let threw = false; try { L.makeCheck({ id: 'c', req: 'G-4', objects: [], quantity: 'gap', value: [1, 2], completeness: 'SAMPLED', verdict: 'PASSED', level: 'L2' }); } catch (e) { threw = true; }
ok(threw, 'PASSED при SAMPLED отвергается');
threw = false; try { L.makeCheck({ id: 'c', req: 'G-4', objects: [], quantity: 'gap', value: [-1, 2], completeness: 'CERTIFIED', verdict: 'UNRESOLVED', level: 'L2' }); } catch (e) { threw = true; }
ok(threw, 'UNRESOLVED без причины отвергается');
const P = v => ({ verdict: v });
ok(L.configVerdict([P('PASSED'), P('PASSED')]) === 'PASSED', '§1: все PASSED');
ok(L.configVerdict([P('PASSED'), P('UNRESOLVED')]) === 'UNRESOLVED', '§1: UNRESOLVED');
ok(L.configVerdict([P('UNRESOLVED'), P('FORBIDDEN')]) === 'FORBIDDEN', '§1: FORBIDDEN');
ok(L.configVerdict([]) === 'UNRESOLVED', '§1: без проверок — UNRESOLVED');
const proto = (checks, g) => ({ protocol: 'honc-qf-r1-kt1', interface: 4, checks, verdict: { geometry: g } });
const ch = (v, c, r) => ({ id: 'x', req: 'G-4', objects: [], quantity: 'gap', value: [0, 1], completeness: c, verdict: v, level: 'L2', reason: r });
ok(L.validate(proto([ch('PASSED', 'SAMPLED')], 'PASSED')).length > 0, 'validate: PASSED при SAMPLED');
ok(L.validate(proto([ch('PASSED', 'CERTIFIED'), ch('UNRESOLVED', 'CERTIFIED', 'r')], 'PASSED')).length > 0, 'validate: вердикт конфигурации против § 1');
ok(L.validate(proto([ch('PASSED', 'CERTIFIED')], 'PASSED')).length === 0, 'validate: правильный протокол чист');

console.log(`\nИтого: ${pass} прошло, ${fail} не прошло`);
if (fail) { console.log(fails.slice(0, 20).join('\n')); process.exit(1); }
