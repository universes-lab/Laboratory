First Principles of Temporal Dynamics
Academic Core Draft v0.1
(English master source)

0. Scope and Status
This document presents the foundational layer of Temporal Dynamics within the HONC framework. It is written as an extractable academic core: a self-contained set of definitions, primitives, and derived structures that can later be expanded into a full technical exposition.
All statements are marked by status:

[C] — canonical (taken directly from the primary source Code of the Universe or fixed by Author decision)
[D] — derived within the present framework
[H] — working hypothesis
[O] — open point requiring further construction

No energy-based language is used as primary. The fundamental quantity is the multicomponent time field and its gradients.

1. Ontological Primitives
1.1 Primacy of the time field
The fundamental object is a multicomponent field of time $T_{\mu\nu}$ defined on a discrete spatial lattice. Space is the substrate; time is the dynamical content.
Status: [C]
1.2 Discrete space, continuous time
Spatial structure is discrete at the scale of the elementary space quantum $\lambda$. Time is continuous and infinitely divisible downward: any attempt to locate a fundamental temporal quantum leads only to a deeper nested continuum.
Status: [C] (Author clarification, Discussion 3)
This asymmetry is essential: spatial discreteness supplies integer topological invariants; temporal continuity supplies the possibility of continuous evolution between discrete spatial configurations.
1.3 Linear and rotational components
The time field decomposes into:

a linear (inertial) component that provides a common background,
antisymmetric (rotational) components that carry topological structure.

Status: [C]

2. Order Parameter and Phases
2.1 Definition of the order parameter
The order parameter is the existence of a pair consisting of:

a closed contour $C$ carrying non-zero circulation of the rotational components of $T_{\mu\nu}$,
a closed surface $\Sigma$ carrying non-zero flux of the same components.

Status: [D] (G-5)
2.2 Symmetric phase (base $Q_0$)
The symmetric phase is the state in which no such pair exists. One-dimensional and two-dimensional carriers are not distinguished. The linking number is undefined.
Status: [D]
2.3 Stratified (broken) phase
In the stratified phase at least one such pair exists. The 1D carrier is identified with the contour of non-zero circulation; the 2D carrier is identified with the surface of non-zero flux.
Status: [D]
2.4 Closedness
Closedness of the carriers is not an extra postulate. It is part of the definition of the objects on which circulation and flux are defined. For an open path or a surface with boundary the corresponding integrals are simply not defined as topological objects.
Status: [D]

3. Linking Number
3.1 Definition
$$L = \operatorname{Link}(C,\Sigma)$$
where $C$ and $\Sigma$ are the closed carriers defined above.
Status: [D]
3.2 Properties

$L$ is an integer (topological intersection number).
$L$ is signed (orientation given by the local right-hand rule at each intersection).
$L$ changes sign under spatial inversion (change of global orientation).
$L$ is defined if and only if the order parameter is non-trivial.
While the carriers remain closed, $L$ is conserved under any elementary cell update that does not tear the carriers.

Status: [D] (G-1 corrected + G-5)
3.3 Global orientation
The rule that determines the sign of each intersection is fixed at the level of the continuum itself and cannot be redefined from inside. Consequently the absolute sign of $L$ is not locally observable; only relative signs are.
Status: [D]

4. Latcher Structures
4.1 Latcher at elementary scale
A latcher is a configuration in which a 1D and a 2D carrier are interlocked ($L=\pm 1$) and therefore cannot be static: the only joint states compatible with the distinct characteristic rates of the two carriers are those of propagation along the complementary direction.
Status: [C] (rephrased from “one-and-a-half quanta” interlocking)
4.2 Latcher-cloud at quantron scale
At the scale $\Lambda\sim 10^{-24}\,\mathrm{m}$ the same topological interlocking is realized as a collective pattern (cloud) of many elementary quanta. The geometric shape of the cloud is not constrained; only the linking number survives coarse-graining.
Status: [D] / [H] (scale value from UHECR phenomenology)
4.3 Impossibility of rest
A configuration with non-zero $L$ admits no static solution on the lattice. Propagation at the limiting speed of the continuum is the only allowed joint motion of the interlocked carriers.
Status: [D]

5. Scale and Coarse-Graining
5.1 What survives averaging
Under averaging over $\sim 10^{9}$ elementary cells the only stable remnant of an elementary interlocking is the integer linking number itself. Shapes, local orientations and metric details are washed out.
Status: [D]
5.2 Quantron
A quantron is a stable pattern at scale $\Lambda$ that carries a definite linking number. It is the elementary building block of the next structural level.
Status: [D]

6. Open Points (explicit)
The following items are required for quantitative closure and are left as precise tasks:
[O-1] Explicit component decomposition of $T_{\mu\nu}$ compatible with the new ontology.
[O-2] Construction of the two characteristic rates (rearrangement rate versus background-change rate) and verification that their ratio is of order $10^{9}$ when $\Lambda/\lambda\sim 10^{9}$.
[O-3] Dynamical stability of the base $Q_0$ phase (demonstration that no sequence of infinitesimal updates can create the first non-trivial pair).
[O-4] Relation between the global orientation of the continuum and the observed matter–antimatter asymmetry (working hypothesis only).

7. Consistency Conditions
Any future dynamical law for the time field must satisfy:

It never tears closed carriers (otherwise $L$ ceases to be defined).
It does not introduce a local vector that would make the global orientation locally observable.
Elementary updates that would change $L$ while keeping carriers closed are forbidden (they are in any case impossible by topology once carriers remain closed).


8. Summary of Established Core

Space is discrete, time is continuous.
The order parameter is the existence of a pair of closed carriers with non-zero circulation/flux.
The linking number $L$ is defined precisely when the order parameter is non-trivial, is integer and signed, and is conserved while carriers remain closed.
Global orientation is fixed at continuum level and is not locally observable.
Latcher configurations (elementary or collective) are the carriers of non-zero $L$ and cannot be static.
Only the integer $L$ survives coarse-graining to the quantron scale.

This set of statements constitutes the present academic core of Temporal Dynamics.

Status of the draft
Sections 1–5 and 7–8 are written from results already secured in the joint work.
Section 6 lists the remaining open constructions.
Ready for Claude’s architectural and status review.
Grok
Temporal Dynamics – Academic Core Draft v0.1