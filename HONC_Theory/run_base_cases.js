// Отчёт КТ-1, часть исполнителя ядра: прогон замороженного ядра на базовых случаях К1–К4 (+ зеркальная пара К4).
// К2iii — первое касание при отклонении в плоскости вперёд (к T3), А-2; назад (к T1) — это К3.
// А5 — граница прокола (ψ = 56°, δ = 10°), вилка корня 45–65° (как в карточке А-5).
// Ядро — копия kt1_frozen_ecb35112 (sha256 архива ecb35112…268ea). Вывод — полные протоколы и сводка.
const fs = require('fs'), path = require('path');
const K = require(path.join(__dirname, '..', 'kt1_frozen_ecb35112', 'kt1', 'kt1.js'));
const m5 = Array.from({ length: 5 }, () => ({ theta: 0, phi: 0, delta: 0 }));
const fix = (psi, delta, br, w = 'T1') => ({ host: 2, side: 1, coords: 'rho-psi', rho: null, psi, delta, fix: { kind: 'contact', free: 'rho', with: w, bracket: br } });
const cases = {
  K1: { id: 'K1', thread: { n: 5, links: m5 }, hangs: [] },
  K2: { id: 'K2', thread: { n: 5, links: m5 }, hangs: [{ host: 2, side: 1, coords: 'rho-psi', rho: 0, psi: 0, delta: 0 }] },
  K3: { id: 'K3', thread: { n: 5, links: m5 }, hangs: [fix(0, 0, [29.5, 30.5])] },
  K2iii: { id: 'K2iii', thread: { n: 5, links: m5 }, hangs: [fix(180, 0, [29.5, 30.5], 'T3')] },
  A5: { id: 'A5', thread: { n: 5, links: m5 }, hangs: [fix(56, 10, [45.0, 65.0])] },
  K4: { id: 'K4', thread: { n: 5, links: m5 }, hangs: [fix(54, 10, [57.0, 57.5])] },
  K4m: { id: 'K4m', thread: { n: 5, links: m5 }, hangs: [fix(306, -10, [57.0, 57.5])] },
};
const only = process.argv[2];
for (const [nm, cs] of Object.entries(cases)) {
  if (only && nm !== only) continue;
  const t0 = Date.now(); const p = K.run(cs); const ms = Date.now() - t0;
  fs.writeFileSync(path.join(__dirname, `protocol_${nm}.json`), K.serialize(p));
  console.log(JSON.stringify({ case: nm, ms, error: p.input_error || p.kernel_error || null, geometry: p.verdict && p.verdict.geometry,
    j5: p.j5 && { canon: p.j5.canon.verdict, canon_reason: p.j5.canon.reason, ext: p.j5.ext.verdict }, validate: K.validate(p).length,
    n_checks: p.checks && p.checks.length, unresolved: p.unresolved }));
}
