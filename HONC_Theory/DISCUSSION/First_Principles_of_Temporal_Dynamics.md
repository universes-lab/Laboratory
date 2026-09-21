# First Principles of Temporal Dynamics

## Academic Core — final text
### English master source

---

## 0. Scope and Status

This document constitutes the foundational academic core of Temporal Dynamics within the HONC framework. It is written as an extractable, self-contained manuscript core suitable for later expansion into a full technical exposition or preprint.

Status labels used throughout:

- **[C]** — canonical (primary source *Code of the Universe*, or explicit Author decision)
- **[D]** — derived inside the present framework
- **[H]** — working hypothesis
- **[O]** — open construction task
- **[def]** — definitional

The fundamental object is the multicomponent time field. No energy, mass, force or ℏ is employed as a primary quantity. Wherever a bridge to conventional observables is required, it is explicitly marked.

---

# 1. Ontological Primitives

## 1.1 Primacy of the time field

The fundamental object is a multicomponent field of time \(T_{\mu\nu}\) defined on a discrete spatial lattice. Space functions as substrate; the dynamical content resides in the time field.

**Status: [C]**

## 1.2 Discrete space, continuous time

Spatial structure is discrete at the elementary scale \(\lambda\). Time is continuous and admits no fundamental quantum: any search for a minimal temporal interval leads only to a deeper nested continuum.

**Status: [C]**

The asymmetry is essential. Spatial discreteness supplies integer topological invariants. Temporal continuity orders elementary cell updates, so that the displacement of a large-scale pattern proceeds as a front of successive intermediate configurations rather than as a single discontinuous jump.

## 1.3 Linear and rotational components

The time field decomposes into a linear (inertial) component that furnishes a common background, and antisymmetric (rotational) components that support topological structure.

**Status: [C]**

---

# 2. Order Parameter and Phases

## 2.1 Definition of the order parameter

The order parameter is the existence of a pair consisting of

- a closed contour \(C\) that carries non-zero circulation of the rotational components of \(T_{\mu\nu}\), and
- a closed surface \(\Sigma\) that carries non-zero flux of the same components.

**Status: [def]**

## 2.2 Base symmetric phase \(Q_0\)

By definition, the base symmetric phase \(Q_0\) is the state in which no such pair exists. The one-dimensional and two-dimensional carriers remain undistinguished and the linking number is undefined.

Whether this state is dynamically realizable and stable remains an open question (see [O-3]).

**Status: [def]; realizability [O-3]**

## 2.3 Transitional state \(Q_0^*\)

During a quantron-scale transition the carriers may dissolve inside a limited spatial region. Inside that region the order-parameter pair ceases to exist and the linking number loses definition. This transitional state \(Q_0^*\) is distinct from the global base \(Q_0\).

A working requirement of the framework is that a bounded \(Q_0^*\) transition must not destroy the topological information associated with the surrounding configuration. However, the identity of the quantity preserved through this transition has not yet been derived. It may be \(L\) itself, a latent boundary winding, or another invariant from which \(L\) is recovered after the transition.

Determination of that conserved quantity and the mechanism of its recovery is therefore an open construction task (see [O-7]).

**Status of the \(Q_0^*\) distinction: [D]**  
**Status of conservation through \(Q_0^*\): [H] / [O-7]**

## 2.4 Stratified phase

In the stratified phase at least one order-parameter pair exists. The 1D carrier is identified with the contour of non-zero circulation; the 2D carrier is identified with the surface of non-zero flux.

**Status: [D]**

## 2.5 Closedness

Closedness belongs to the definition of the carriers. Circulation on an open path, and flux through a surface with boundary, are not defined as topological objects.

**Status: [D]**

---

# 3. Linking Number

## 3.1 Definition

\[
L = \operatorname{Link}(C,\Sigma)
\]

**Status: [D]**

## 3.2 Properties

The following properties are established:

- \(L\) is an integer.
- \(L\) is signed by the local orientation at each intersection.
- \(L\) changes sign under spatial inversion.
- \(L\) is defined if and only if the order parameter exists.

**Status: [D]**

A further dynamical requirement remains open:

For an admissible evolution law, \(L\) is expected to remain invariant under elementary cell updates for which the order-parameter pair remains defined. This update-by-update invariance has not yet been demonstrated.

It remains to be established whether invariance follows automatically from topology once the carriers remain closed, or whether the admissible shift law must explicitly exclude link-altering elementary transitions.

See [O-6].

**Status of update-by-update conservation: [H] / [O-6]**

## 3.3 Global orientation and non-observability of absolute sign

The sign rule is fixed at the level of the continuum and cannot be redefined from within. Absolute sign is therefore not locally observable; only relative signs are.

This agrees with the empirical fact that there is no intrinsic, absolute criterion for declaring our matter to be “matter” rather than “antimatter”; one can only establish that the two are opposite.

**Status: [D]**

---

# 4. Latcher Structures

## 4.1 Interlocking (canonical)

A latcher is a configuration in which a 1D carrier and a 2D carrier are interlocked \((L=\pm1)\). The canonical reason such a configuration cannot remain static is the impossibility of tearing one dimension out of space: the carriers can neither separate nor coincide.

**Status: [C]**

## 4.2 Rate-mismatch argument

A derived argument notes that the two carriers are characterized by distinct rates. In the \(\lambda\)-scale geometry these rates appear as approximately \(0.58c\) and \(0.82c\) (diagonal-of-the-cube figures).

Because the figures themselves require re-attestation in the new ontology, the rate-mismatch mechanism is carried as a working hypothesis pending that re-derivation.

**Status: [H] — re-attestation pending**

## 4.3 Latcher-cloud

The same topological interlocking can be realized as a collective pattern spanning many elementary spatial quanta. Geometric shape is not constrained; only the linking number survives coarse-graining.

Because time is continuous, displacement of such a pattern is a front of successive elementary updates ordered in time, generating a continuous family of intermediate configurations.

**Status of the topological realization: [D]**  
**Status of any specific numerical scale: [H]**

## 4.4 Propagation at limiting speed

A configuration with non-zero \(L\) admits no static solution. The joint kinematics of the two carriers are consistent only along the complementary direction.

The conclusion that this motion occurs at the limiting speed of the continuum rests solely on the existence of a single common rate supplied by the linear component and available to both carriers. It does not depend on the specific numerical values of the carrier rates discussed in §4.2, and is therefore independent of the provisional status of that subsection.

**Status: [D]**

---

# 5. Scale and Coarse-Graining

## 5.1 Three distinct scales

The framework requires three scales to be kept separate:

| Symbol / term | Meaning |
|---|---|
| \(\lambda\) | elementary lattice scale — the spatial quantum |
| \(\Lambda\) | characteristic reference scale of quantron patterns |
| extent | actual spatial extent of an individual quantron pattern |

\(\Lambda\) is a reference value, not an outer radius. The extent of an individual pattern is state-dependent and is not fixed by \(\Lambda\). No universal pattern size is asserted.

**Status: [def]**

## 5.2 Survival under averaging

Under averaging over a large number of elementary cells, the only stable remnant of an elementary interlocking is the integer linking number. Shapes, local orientations and metric details are eliminated. State-dependence of extent reinforces this: a quantity that varies between states cannot be the surviving invariant.

Circulation and flux are integral quantities. Integrals survive averaging by construction; consequently the carriers themselves remain identifiable after coarse-graining as the supports of the surviving non-zero integrals.

**Status: [D]**

## 5.3 Quantron

A quantron is a stable collective pattern that carries a definite linking number and serves as a building block of the next structural level.

The UHECR-derived value

\[
\Lambda \sim 2\times10^{-24}\,\mathrm m
\]

is at present only a candidate characteristic, correlation, or reference scale. It is not established as a sharp universal outer radius of every quantron pattern. The actual spatial extent of a quantron pattern may in principle be state-dependent.

**Status: [D] — existence of the pattern**  
**Status: [H] — any specific numerical scale**

---

# 6. Open Tasks — to be constructed

### [O-1]
Explicit component decomposition of \(T_{\mu\nu}\) compatible with the present ontology.

### [O-2]
Independent construction, from the components of \(T_{\mu\nu}\), of two rates:

- the local rearrangement rate of carriers;
- the rate of change of the background field.

Their ratio is then to be compared with the external characteristic target \(\sim10^9\).

The value of the ratio must not be used as an input, and the comparison is against a characteristic value, not a universal one.

**Bridge declaration:** the numerical target associated with

\[
\Lambda \sim 2\times10^{-24}\,\mathrm m
\]

originates from UHECR phenomenology via the conventional relation

\[
E=\hbar c/\lambda .
\]

This is an observational bridge to laboratory units, not a statement internal to Temporal Dynamics.

### [O-3]
Demonstration that the base phase \(Q_0\) is dynamically stable: no sequence of infinitesimal updates creates the first order-parameter pair.

### [O-4]
Relation between the global orientation of the continuum and the observed matter–antimatter asymmetry.

**Status: hypothesis only.**

### [O-5]
Determination of what fixes the actual spatial extent of a quantron-scale pattern, and whether that extent is state-dependent.

**Route: Discussion 2.**

### [O-6]
Construction of an admissible elementary shift/update law and demonstration — by induction over elementary switchings ordered in continuous time, or by an equivalent argument — of whether \(L\) remains invariant under every elementary update for which the order-parameter pair remains defined.

The construction must determine whether this invariance follows from topology alone or requires an explicit dynamical restriction excluding link-altering updates.

**Route: resumed Discussion 2 / Temporal Dynamics construction.**

### [O-7]
Determination of the quantity preserved through a bounded transitional \(Q_0^*\) region.

Candidates include:

- the linking number \(L\) itself;
- latent boundary winding;
- another topological invariant from which \(L\) is recovered.

The mechanism by which the pre-transition value is related to the post-transition value must be explicitly derived rather than assumed.

**Route: separate transition/invariant round within resumed Discussion 2.**

---

# 7. Constraints — to be satisfied by any construction

Any admissible evolution law for the time field must satisfy:

1. Closed carriers are never permanently torn where the topological description is required to remain defined.

2. Bounded, temporary dissolution of a carrier pair inside a limited region is permitted, provided the enclosing configuration remains intact. This is the transitional state \(Q_0^*\) of §2.3.

3. No local vector is introduced that would render the global orientation locally observable. A vector carries direction and therefore appears in local observables; a pure sign carries only two values and no direction, and can therefore differ globally without differing locally.

4. The elementary shift/update law must be compatible with preservation of the relevant topological invariant during evolution. Whether this invariant is \(L\) itself under every elementary update is the subject of [O-6].

5. A bounded \(Q_0^*\) transition must preserve sufficient enclosing topological information for the post-transition configuration to remain related to the pre-transition configuration. The identity of that conserved quantity is the subject of [O-7].

---

# 8. Established Core

Space is discrete and time is continuous.

The order parameter is the existence of a pair of closed carriers with non-zero circulation and flux.

Base \(Q_0\) is the global symmetric phase; transitional \(Q_0^*\) is a localized temporary loss of that pair.

The linking number \(L\) is defined when the order-parameter pair exists, is integer, and is signed.

Global orientation is fixed at continuum level, while absolute sign is not locally observable.

Configurations carrying non-zero \(L\) cannot be static.

Under coarse-graining, the integer linking number and the integral supports associated with its carriers survive while local shape and metric detail are eliminated.

Any specific numerical scale associated with quantron patterns remains provisional.

**No general conservation law for \(L\) under elementary updates, and no conservation mechanism through \(Q_0^*\), is claimed as derived at this stage. These are explicit open construction tasks [O-6] and [O-7].**

---

## Status of this text

The foundational architecture established in Discussion 3 is retained.

The two conservation questions identified by the Ontology Keeper are explicitly returned to open status rather than silently closed:

- update-by-update invariance of \(L\);
- conservation through transitional \(Q_0^*\).

No derivation has been invented to close either question.

The remaining construction work is routed back into the continuing Temporal Dynamics programme.

---

**APPENDIX / DISCUSSION 3 CLOSED → RETURN TO DISCUSSION 2**