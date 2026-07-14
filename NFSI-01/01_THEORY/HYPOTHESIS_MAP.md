# HYPOTHESIS MAP: NFSI-01

**Status:** DRAFT  
**Date:** 2026-06-25  
**Author:** DeepSeek + Qwen

---

## 1. PURPOSE

This is the **master table** linking hypotheses to data, tests, and falsification criteria.

---

## 2. HYPOTHESIS MAP

| Hypothesis | Consequence | What is Measured | Data Required | Falsification Criterion |
|------------|-------------|------------------|---------------|-------------------------|
| **H1:** 5 groups with different moments | Different velocities | Time-of-flight | SN1987A, IceCube, OPERA | No correlation moment-velocity |
| **H2:** Substructure within flavors | Additional peaks in spectra | Energy spectra | Super-K, JUNO, KamLAND | No peaks > 3σ |
| **H3:** Energy dependence | Δm²(E) ≠ const | Oscillations at different E | NOvA, DUNE | No energy dependence |
| **H4:** Statistical weight | Different event rates | Statistics by flavor | All experiments | No difference after cross-section correction |
| **H5:** Moment-cross-section correlation | Cross-section depends on moment | ν-e, ν-nucleon cross-sections | Micro/mini-booster experiments | No correlation |

---

## 3. DATA AVAILABILITY

| Hypothesis | Data Available? | Quality | Priority |
|------------|-----------------|---------|----------|
| H1 | Partial (SN1987A, OPERA) | Medium | 1 |
| H2 | Yes (Super-K, JUNO, KamLAND) | High | 2 |
| H3 | Partial (NOvA) | Medium | 5 |
| H4 | Yes (all experiments) | High | 3 |
| H5 | Yes (cross-section measurements) | Medium | 4 |

---

## 4. TESTING STRATEGY

**Phase 1:** H1 (velocities) — cleanest test  
**Phase 2:** H2 (substructure) — core prediction  
**Phase 3:** H4 (statistical weight) — multiplicity test  
**Phase 4:** H5 (cross-section) — interaction test  
**Phase 5:** H3 (energy dependence) — speculative test

---

## 5. DECISION TREE

START
  │
  ├─→ Test H1 (velocities)
  │     │
  │     ├─→ Significant difference? → SUPPORT H1
  │     │
  │     └─→ No difference? → REJECT H1 → Test H2
  │
  ├─→ Test H2 (substructure)
  │     │
  │     ├─→ Additional peaks? → SUPPORT H2
  │     │
  │     └─→ No peaks? → REJECT H2 → Test H4
  │
  ├─→ Test H4 (statistical weight)
  │     │
  │     ├─→ Different rates? → SUPPORT H4
  │     │
  │     └─→ No difference? → REJECT H4 → Test H5
  │
  └─→ Test H5 (cross-section)
        │
        ├─→ Correlation? → SUPPORT H5
        │
        └─→ No correlation? → REJECT H5 → Test H3


---

## 6. SUCCESS CRITERIA

**Strong Support:** BF > 10 or p < 0.001 for any hypothesis  
**Weak Support:** BF > 3 or p < 0.05 for any hypothesis  
**No Support:** All BF < 3, all p > 0.05  
**Rejection:** Explicit falsification of all hypotheses

---

**Document Owner:** DeepSeek  
**Review Status:** Pending Author approval  
**Next Action:** Author approves hypothesis map
