// Собственный разбор Клода: замороженное ядро (копия kt1_frozen_ecb35112) на семействе навесов H1 с касанием T1, ψ — по аргументам.
// Ядро не менялось; это прогоны ядра на новых входах для анализа, не эталоны и не приёмка.
const path = require('path');
const K = require(path.join(__dirname, '..', 'kt1_frozen_ecb35112', 'kt1', 'kt1.js'));
const m5 = Array.from({ length: 5 }, () => ({ theta: 0, phi: 0, delta: 0 }));
const psi = parseFloat(process.argv[2]), lo = parseFloat(process.argv[3]), hi = parseFloat(process.argv[4]);
const delta = process.argv[5] !== undefined ? parseFloat(process.argv[5]) : 10, side = process.argv[6] !== undefined ? parseInt(process.argv[6]) : 1;
const t0 = Date.now();
const p = K.run({ id: `scan-psi-${psi}-d${delta}-s${side}`, thread: { n: 5, links: m5 }, hangs: [{ host: 2, side, coords: 'rho-psi', rho: null, psi, delta, fix: { kind: 'contact', free: 'rho', with: 'T1', bracket: [lo, hi] } }] });
const h = p.configuration && p.configuration.tori && p.configuration.tori.find(t => t.name === 'H1');
const bad = (p.checks || []).filter(c => c.verdict !== 'PASSED').map(c => `${c.id} ${c.verdict}: ${c.reason}`);
console.log(JSON.stringify({ psi, delta, side, bracket: [lo, hi], ms: Date.now() - t0, kernel: p.kernel && p.kernel.version, error: p.input_error || p.kernel_error || null,
  geometry: p.verdict && p.verdict.geometry, root_deg: h && h.fix && h.fix.root_deg, not_passed: bad, unresolved: p.unresolved }));
