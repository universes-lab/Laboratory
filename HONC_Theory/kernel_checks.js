// Собственный разбор Клода: замороженное ядро (копия kt1_frozen_ecb35112) на одной точке семейства H1 —
// общий вердикт и состояние каждой проверки, с сертифицированными запасами.
//   node kernel_checks.js <ψ> <ρ_lo> <ρ_hi> <δ> <сторона>
const path = require('path');
const K = require(path.join(__dirname, '..', 'kt1_frozen_ecb35112', 'kt1', 'kt1.js'));
const [psi, lo, hi, delta] = process.argv.slice(2, 6).map(Number), side = parseInt(process.argv[6] || '1');
const m5 = Array.from({ length: 5 }, () => ({ theta: 0, phi: 0, delta: 0 }));
const t0 = Date.now();
const p = K.run({ id: `pt-${psi}-${delta}-${side}`, thread: { n: 5, links: m5 }, hangs: [{ host: 2, side, coords: 'rho-psi', rho: null, psi, delta, fix: { kind: 'contact', free: 'rho', with: 'T1', bracket: [lo, hi] } }] });
const h = p.configuration && p.configuration.tori && p.configuration.tori.find(t => t.name === 'H1');
const pick = id => { const c = (p.checks || []).find(c => c.id === id); return c ? { verdict: c.verdict, value: c.value, outside_margin: c.outside_margin, kappa_margin: c.kappa_margin, reason: c.reason } : null; };
console.log(JSON.stringify({ psi, delta, side, bracket: [lo, hi], ms: Date.now() - t0, geometry: p.verdict && p.verdict.geometry, root_deg: h && h.fix && h.fix.root_deg,
  not_passed: (p.checks || []).filter(c => c.verdict !== 'PASSED').map(c => c.id), n_checks: (p.checks || []).length, unresolved: p.unresolved,
  R1_H1: pick('G5a:R1:H1'), RH1_T2: pick('G5bg:RH1:T2'), RH1_T1: pick('G5a:RH1:T1') }));
