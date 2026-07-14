# PRE-REVIEW-00B: HYPOTHESES FOR TESTING

**Status:** DRAFT  
**Date:** 2026-06-25  
**Author:** DeepSeek (Computational Architect) + Qwen (Ontology Keeper)

---

## 1. PURPOSE

This document lists **testable hypotheses** derived from NHC/TD theory. Each hypothesis must be:
- Clearly stated
- Operationally defined
- Falsifiable
- Linked to specific data

---

## 2. HYPOTHESIS LIST

### H1: Flavor-Dependent Velocities

**Statement:** Neutrinos with different gyroscopic moments have different velocities.

**Operational Definition:**
- Group A (electron): highest velocity (closest to c)
- Group B (muon): medium velocity
- Group C (tau): lowest velocity

**Measurable Consequence:** Different time-of-flight for different flavors from the same source.

**Data Required:**
- SN1987A neutrino arrival times
- IceCube high-energy neutrino timestamps
- OPERA/MINOS beam neutrino timing

**Falsification Criterion:** No statistically significant difference in time-of-flight after accounting for energy and distance.

---

### H2: Substructure Within Flavors

**Statement:** Within each flavor group, there are substructures corresponding to different gyroscopic moment values.

**Operational Definition:**
- Electron neutrino: substructure at moments 0 and ±0.096
- Muon neutrino: substructure at moments ±0.408 and ±0.504
- Tau neutrino: single group at moment ±0.912

**Measurable Consequence:** Additional peaks or non-monotonicities in energy spectra.

**Data Required:**
- Super-K solar neutrino spectra
- JUNO reactor neutrino spectra
- KamLAND reactor neutrino spectra

**Falsification Criterion:** No additional peaks > 3σ above background after accounting for detector effects.

---

### H3: Energy-Dependent Oscillations

**Statement:** Oscillation parameters (Δm²₂₁, sin²θ₁₂) depend on neutrino energy.

**Operational Definition:** Δm²₂₁(E) ≠ const

**Measurable Consequence:** Different best-fit values at different energy bins.

**Data Required:**
- NOvA neutrino energy spectra
- DUNE (future) energy spectra
- Multi-energy bins from Super-K

**Falsification Criterion:** No statistically significant energy dependence after accounting for matter effects.

---

### H4: Statistical Weight Differences

**Statement:** Different flavor groups have different statistical weights due to multiplicity.

**Operational Definition:**
- Group A: 6 states (4 + 2)
- Group B: 8 states (4 + 4)
- Group C: 2 states

**Measurable Consequence:** Different event rates for different flavors after accounting for cross-sections.

**Data Required:**
- Event counts from all experiments
- Cross-section measurements

**Falsification Criterion:** No difference in event rates after accounting for cross-sections and detector efficiency.

---

### H5: Moment-Cross-Section Correlation

**Statement:** Interaction cross-section depends on gyroscopic moment.

**Operational Definition:** σ(ν-e) or σ(ν-nucleon) varies with moment value.

**Measurable Consequence:** Different cross-sections for different flavors.

**Data Required:**
- Micro-booster experiment cross-sections
- Mini-booster experiment cross-sections

**Falsification Criterion:** No correlation between cross-section and moment value.

---

## 3. PRIORITY RANKING

| Priority | Hypothesis | Reason |
|----------|------------|--------|
| 1 | H1 (Velocities) | Most direct prediction, cleanest test |
| 2 | H2 (Substructure) | Tests core prediction of substructure |
| 3 | H4 (Statistical Weight) | Tests multiplicity prediction |
| 4 | H5 (Cross-Section) | Tests interaction mechanism |
| 5 | H3 (Energy Dependence) | Most speculative, hardest to test |

---

## 4. DEPENDENCIES

**H1 requires:** Precise timing data, known distances
**H2 requires:** High-resolution spectra, good background subtraction
**H3 requires:** Multi-energy data, matter effect modeling
**H4 requires:** Accurate cross-sections, efficiency corrections
**H5 requires:** Multiple experiments, systematic error control

---

## 5. INDEPENDENT TESTS

Each hypothesis should be tested by:
1. DeepSeek (primary analysis)
2. Claude (independent verification)
3. Cross-check with different datasets

---

**Document Owner:** DeepSeek  
**Review Status:** Pending Author approval  
**Next Action:** Author confirms hypotheses and priorities