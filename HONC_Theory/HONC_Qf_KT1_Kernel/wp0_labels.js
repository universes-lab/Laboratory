'use strict';
// HONC / Qf / R1 / КТ-1 — WP-0: словарь меток (спецификация § 1), правило вердикта, валидатор протокола.
const fs = require('fs');
const path = require('path');

const COMPLETENESS = ['EXACT', 'CERTIFIED', 'SAMPLED', 'UNRESOLVED'];
const VERDICT = ['PASSED', 'FORBIDDEN', 'UNRESOLVED'];
const LEVEL_KT1 = ['L1', 'L2', 'L3'];          // L4 в КТ-1 не выдаётся, L5 — никогда
const LAYER = ['CARRIER'];                      // в КТ-1 других слоёв нет
const EXISTENCE = ['IMPOSED', 'CANDIDATE', 'SEPARATED', 'PENETRATION'];
const PARALLEL = ['PARALLEL-ESTABLISHED', 'PARALLEL-UNCERTAIN', 'NON-PARALLEL'];
const TYPE = ['SIDE', 'AXIAL', 'MIXED', 'UNDETERMINED'];
const READING = ['J5-CANON', 'J5-EXT', 'J5-DEGENERATE', 'J5-CLASS-UNRESOLVED'];
const CONTACT_CLASS = ['STRUCTURAL', 'ALLOWED CONTACT', 'UNRESOLVED CONTACT', 'DEGENERATE MEETING'];
const J5_CANON = ['PASSED', 'FORBIDDEN', 'UNRESOLVED'];
const J5_EXT = ['PASSED-EXT', 'FORBIDDEN-EXT', 'UNRESOLVED'];

const REGISTRY = JSON.parse(fs.readFileSync(path.join(__dirname, 'registry_S3.json'), 'utf8'));
const REG_IDS = new Set(REGISTRY.rows.map(r => r.id));

function oneOf(name, v, set) { if (!set.includes(v)) throw new Error(`${name}: недопустимое значение ${JSON.stringify(v)}`); }

// Запись проверки (интерфейс § 6.1). Инвариант: PASSED только при EXACT / CERTIFIED.
function makeCheck(c) {
  for (const k of ['id', 'req', 'objects', 'quantity', 'value', 'completeness', 'verdict', 'level']) {
    if (c[k] === undefined) throw new Error(`check: нет поля ${k}`);
  }
  oneOf('completeness', c.completeness, COMPLETENESS);
  oneOf('verdict', c.verdict, VERDICT);
  oneOf('level', c.level, LEVEL_KT1);
  if (c.verdict === 'PASSED' && !(c.completeness === 'EXACT' || c.completeness === 'CERTIFIED')) {
    throw new Error(`check ${c.id}: PASSED при полноте ${c.completeness} недопустим`);
  }
  if ((c.verdict === 'FORBIDDEN' || c.verdict === 'UNRESOLVED') && !c.reason) {
    throw new Error(`check ${c.id}: ${c.verdict} без причины`);
  }
  if (c.status !== undefined && c.status !== null && !REG_IDS.has(c.status)) throw new Error(`check ${c.id}: нет строки реестра ${c.status}`);
  return Object.freeze({ layer: 'CARRIER', status: null, reason: null, where: null, ...c });
}

// Правило § 1: PASSED ⇔ все PASSED; хотя бы одна FORBIDDEN ⇒ FORBIDDEN; иначе UNRESOLVED.
function configVerdict(checks) {
  if (checks.some(c => c.verdict === 'FORBIDDEN')) return 'FORBIDDEN';
  if (checks.length > 0 && checks.every(c => c.verdict === 'PASSED')) return 'PASSED';
  return 'UNRESOLVED';
}

// Вердикт по вилке запаса: запас > 0 — PASSED, < 0 — FORBIDDEN, иначе UNRESOLVED.
function verdictFromMargin(v) { return v[0] > 0 ? 'PASSED' : v[1] < 0 ? 'FORBIDDEN' : 'UNRESOLVED'; }

// Валидатор протокола (K.validate): возвращает список нарушений, пустой — если нарушений нет.
function validate(p) {
  const out = [];
  const bad = m => out.push(m);
  if (!p || typeof p !== 'object') return ['протокол: не объект'];
  if (p.input_error || p.kernel_error) {
    if (p.verdict) bad('протокол с ошибкой входа или ядра не должен содержать вердикта');
    return out;
  }
  if (p.protocol !== 'honc-qf-r1-kt1') bad('protocol: неверное имя');
  if (p.interface !== 4) bad('interface: ожидается 4');
  const checks = Array.isArray(p.checks) ? p.checks : (bad('checks: нет массива'), []);
  for (const c of checks) {
    const id = c && c.id;
    if (!COMPLETENESS.includes(c.completeness)) bad(`${id}: completeness ${c.completeness}`);
    if (!VERDICT.includes(c.verdict)) bad(`${id}: verdict ${c.verdict}`);
    if (c.verdict === 'PASSED' && !(c.completeness === 'EXACT' || c.completeness === 'CERTIFIED')) bad(`${id}: PASSED при полноте ${c.completeness}`);
    if ((c.verdict === 'FORBIDDEN' || c.verdict === 'UNRESOLVED') && !c.reason) bad(`${id}: ${c.verdict} без причины`);
    if (!LEVEL_KT1.includes(c.level)) bad(`${id}: level ${c.level} недопустим в КТ-1`);
    if (c.layer !== undefined && !LAYER.includes(c.layer)) bad(`${id}: layer ${c.layer}`);
    if (c.status && !REG_IDS.has(c.status)) bad(`${id}: нет строки реестра ${c.status}`);
    if (!Array.isArray(c.value) || c.value.length !== 2 || !(c.value[0] <= c.value[1])) bad(`${id}: value — не вилка`);
  }
  if (p.verdict) {
    const g = p.verdict.geometry;
    if (!VERDICT.includes(g)) bad(`verdict.geometry ${g}`);
    else if (g !== configVerdict(checks)) bad(`verdict.geometry ${g} не следует из проверок по правилу § 1 (${configVerdict(checks)})`);
  } else bad('verdict: нет');
  if (p.j5) {
    if (p.j5.canon && !J5_CANON.includes(p.j5.canon.verdict)) bad(`j5.canon.verdict ${p.j5.canon.verdict}`);
    if (p.j5.ext) {
      if (!J5_EXT.includes(p.j5.ext.verdict)) bad(`j5.ext.verdict ${p.j5.ext.verdict}`);
      if (p.j5.ext.label !== '[Г, мост]') bad('j5.ext.label должен быть «[Г, мост]»');
    }
  }
  for (const ct of p.contacts || []) {
    if (!EXISTENCE.includes(ct.existence)) bad(`contact ${ct.pair}: existence ${ct.existence}`);
    if (!PARALLEL.includes(ct.parallel)) bad(`contact ${ct.pair}: parallel ${ct.parallel}`);
    if (!TYPE.includes(ct.type)) bad(`contact ${ct.pair}: type ${ct.type}`);
    if (!READING.includes(ct.reading)) bad(`contact ${ct.pair}: reading ${ct.reading}`);
    if (ct.reading === 'J5-CANON' && !(ct.parallel === 'PARALLEL-ESTABLISHED' && (ct.type === 'SIDE' || ct.type === 'AXIAL'))) bad(`contact ${ct.pair}: J5-CANON без установленной параллельности и типа (K-3)`);
    if (ct.existence === 'IMPOSED' && !ct.basis) bad(`contact ${ct.pair}: IMPOSED без основания`);
    if (ct.parallel === 'PARALLEL-ESTABLISHED' && !ct.parallel_basis) bad(`contact ${ct.pair}: PARALLEL-ESTABLISHED без тождества`);
    if (ct.contact_class !== undefined && !CONTACT_CLASS.includes(ct.contact_class)) bad(`contact ${ct.pair}: contact_class ${ct.contact_class}`);
  }
  return out;
}

module.exports = {
  COMPLETENESS, VERDICT, LEVEL_KT1, EXISTENCE, PARALLEL, TYPE, READING, CONTACT_CLASS, J5_CANON, J5_EXT,
  REGISTRY, makeCheck, configVerdict, verdictFromMargin, validate,
};
