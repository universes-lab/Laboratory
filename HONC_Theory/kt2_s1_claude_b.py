#!/usr/bin/env python3
# KT2-S1 Stage 1 — independent computation by Claude_B. Python 3 + numpy only.
# Usage:  python3 kt2_s1_claude_b.py S1_node_research_input.json
# Construction follows interface v6 § 2 (G-7), gap G-4 (spec § 2.1), ring G-2 (pencil of conics, length 2*pi).
# Numerics are floating-point (no interval arithmetic): results are DERIVED, not certified.
import sys, json
import numpy as np

DEG = np.pi / 180.0
R_MID = 0.5                      # torus: a = b = 1/2 (interface v6 § 1)

def unit(v):
    return v / np.linalg.norm(v)

def rot(v, axis, ang):           # right-hand rotation of v about unit axis by ang (rad)
    k = unit(axis)
    return v*np.cos(ang) + np.cross(k, v)*np.sin(ang) + k*(k @ v)*(1-np.cos(ang))

def perp_basis(T):
    a = np.array([1.0, 0, 0]) if abs(T[0]) < 0.9 else np.array([0, 1.0, 0])
    U = unit(np.cross(T, a)); V = np.cross(T, U)
    return U, V

def pt_circle_dist(P, A, T, r=R_MID):   # P: (N,3); distance to circle (centre A, axis T, radius r)
    w = P - A
    h = w @ T
    q = np.linalg.norm(w - np.outer(h, T), axis=1)
    return np.sqrt(h*h + (q - r)**2)

def golden_min(f, a, b, tol=1e-15, it=200):
    g = (np.sqrt(5)-1)/2
    c = b - g*(b-a); d = a + g*(b-a); fc = f(c); fd = f(d)
    for _ in range(it):
        if fc < fd: b, d, fd = d, c, fc; c = b - g*(b-a); fc = f(c)
        else:       a, c, fc = c, d, fd; d = a + g*(b-a); fd = f(d)
        if b - a < tol: break
    x = (a+b)/2
    return x, f(x)

def torus_gap(A1, T1, A2, T2, N=4096, refine=True):
    """G-4: g = min_phi dist(C1(phi), C2) - 1. Returns (g, [minima phi], sample_min, lipschitz_slack)."""
    U, V = perp_basis(T1)
    phi = np.linspace(0, 2*np.pi, N, endpoint=False)
    C1 = A1 + R_MID*(np.outer(np.cos(phi), U) + np.outer(np.sin(phi), V))
    f = pt_circle_dist(C1, A2, T2) - 1.0
    slack = 0.5 * (2*np.pi/N) / 2          # Lipschitz const <= 0.5 (spec G-4) times half-step
    if not refine:
        return f.min(), [], f.min(), slack
    idx = [i for i in range(N) if f[i] <= f[i-1] and f[i] <= f[(i+1) % N]]
    best = []
    for i in idx:
        if f[i] > f.min() + 4*slack + 1e-9:
            continue
        fun = lambda t: (pt_circle_dist((A1 + R_MID*(np.cos(t)*U + np.sin(t)*V))[None, :], A2, T2) - 1.0)[0]
        x, v = golden_min(fun, phi[i] - 2*np.pi/N, phi[i] + 2*np.pi/N)
        best.append((v, x))
    best.sort()
    g = best[0][0]
    minima = [x for v, x in best if v < g + 1e-9]
    return g, minima, f.min(), slack

def bisect(F, a, b, tol=1e-14, it=200):
    fa, fb = F(a), F(b)
    assert fa*fb < 0, ("no sign change", a, b, fa, fb)
    for _ in range(it):
        m = 0.5*(a+b); fm = F(m)
        if fa*fm <= 0: b, fb = m, fm
        else: a, fa = m, fm
        if b-a < tol: break
    return 0.5*(a+b)

# ---------------- construction (interface v6 § 2) ----------------
def frame(Tk, ez):
    p = Tk - (Tk @ ez)*ez
    ey = unit(p) if np.linalg.norm(p) > 1e-14 else unit(np.cross(ez, [1.0, 0, 0]))
    ex = np.cross(ey, ez)
    return ex, ey, ez

def link_step(A, T, u, delta_deg):
    """Link from torus (A,T) along unit u with delta: returns (A_next, T_next, d, mirror)."""
    Tp = T - 2*(T @ u)*u
    if delta_deg == 0:
        Tn = Tp
        d = 2*(0.5*np.sqrt(max(0.0, 1-(T @ u)**2)) + 0.5)
        return A + d*u, unit(Tn), d, True
    n = unit(np.cross(u, T))
    Tn = unit(rot(Tp, n, delta_deg*DEG))
    F = lambda d: torus_gap(A, T, A + d*u, Tn)[0]
    d = bisect(F, 1.0, 2.5)
    return A + d*u, Tn, d, False

def build_thread(case):
    A = [np.zeros(3)]; T = [np.array([0, 1.0, 0])]; ez_in = [np.array([0, 0, 1.0])]
    links = case["thread"]["links"]; n = case["thread"]["n"]
    U = []
    for k in range(n):
        ex, ey, ez = frame(T[k], ez_in[k])
        L = links[k]
        th, ph = L["theta"]*DEG, L["phi"]*DEG
        u = unit(ez*np.cos(th) + (ex*np.cos(ph) + ey*np.sin(ph))*np.sin(th))
        An, Tn, d, mir = link_step(A[k], T[k], u, L["delta"])
        U.append(u)
        if k < n-1:
            A.append(An); T.append(Tn); ez_in.append(u)
        else:
            A_free = An
    return A, T, ez_in, U, A_free

def hang_geom(A, T, ez_in, h, side, rho, psi, delta):
    ex, ey, ez = frame(T[h], ez_in[h])
    e = unit(side*ex*np.cos(rho*DEG) + (-ez*np.cos(psi*DEG) + ey*np.sin(psi*DEG))*np.sin(rho*DEG))
    AH, TH, d, mir = link_step(A[h], T[h], e, delta)
    return AH, TH, d, e

# ---------------- ring G-2: pencil of conics, length 2*pi ----------------
def ellipse_perimeter(a, b):
    if a < b: a, b = b, a
    a0, b0 = 1.0, b/a
    c2 = 1 - b0*b0
    s = 0.5*c2; p = 0.5
    for _ in range(60):
        a1 = 0.5*(a0+b0); b1 = np.sqrt(a0*b0); c = 0.5*(a0-b0)
        p *= 2; s += p*c*c
        a0, b0 = a1, b1
        if c < 1e-17: break
    K = np.pi/(2*a0)
    return 4*a*K*(1 - s)

def conic_ellipse(P0, t0, P1, t1, k):
    """Conic L0*L1 - k*M^2 = 0 in 2D. Returns (center, axes(2x2 cols), semiaxes) or None."""
    n0 = np.array([-t0[1], t0[0]]); n1 = np.array([-t1[1], t1[0]])
    ch = P1 - P0; m = np.array([-ch[1], ch[0]])
    # L(x) = n.x - n.P ; quadratic form pieces
    def lin(nv, P): return nv, -(nv @ P)
    a0_, c0_ = lin(n0, P0); a1_, c1_ = lin(n1, P1); am, cm = lin(m, P0)
    Aq = 0.5*(np.outer(a0_, a1_) + np.outer(a1_, a0_)) - k*np.outer(am, am)
    bq = a0_*c1_ + a1_*c0_ - 2*k*am*cm
    cq = c0_*c1_ - k*cm*cm
    if np.linalg.det(Aq) <= 0: return None
    xc = -0.5*np.linalg.solve(Aq, bq)
    cp = cq + 0.5*(bq @ xc)
    M = Aq/(-cp)
    w, vec = np.linalg.eigh(M)
    if np.any(w <= 0): return None
    return xc, vec, 1/np.sqrt(w)

def build_ring(A, TA, B, TB):
    """Plane ellipse through A,B tangent to TA at A and TB at B, perimeter 2*pi (G-2)."""
    e1 = unit(B - A); nrm = unit(np.cross(e1, TA)); e2 = np.cross(nrm, e1)
    to2 = lambda v: np.array([v @ e1, v @ e2])
    P0 = np.zeros(2); P1 = to2(B - A); t0 = unit(to2(TA)); t1 = unit(to2(TB))
    assert abs(TB @ nrm) < 1e-9, "TB not in ring plane"
    ks = np.concatenate([-np.logspace(-6, 6, 4000)[::-1], np.logspace(-6, 6, 4000)])
    vals = []
    for k in ks:
        r = conic_ellipse(P0, t0, P1, t1, k)
        if r is not None:
            vals.append((k, ellipse_perimeter(*r[2])))
    vals = np.array(vals)
    target = 2*np.pi
    sols = []
    for i in range(len(vals)-1):
        (k1, p1), (k2, p2) = vals[i], vals[i+1]
        if (p1-target)*(p2-target) < 0:
            F = lambda kk: ellipse_perimeter(*conic_ellipse(P0, t0, P1, t1, kk)[2]) - target
            sols.append(bisect(F, k1, k2, tol=1e-15*max(1, abs(k1))))
    assert len(sols) == 1, ("ring length root count", len(sols))
    xc, vec, sa = conic_ellipse(P0, t0, P1, t1, sols[0])
    C = A + xc[0]*e1 + xc[1]*e2
    E1 = vec[0, 0]*e1 + vec[1, 0]*e2; E2 = vec[0, 1]*e1 + vec[1, 1]*e2
    return dict(C=C, E1=E1, E2=E2, s1=sa[0], s2=sa[1], n=nrm, k=sols[0])

def ring_pts(R, t):
    return R["C"] + np.outer(R["s1"]*np.cos(t), R["E1"]) + np.outer(R["s2"]*np.sin(t), R["E2"])

def ring_param_of(R, P):
    w = P - R["C"]
    return np.arctan2((w @ R["E2"])/R["s2"], (w @ R["E1"])/R["s1"])

def curvature_at(R, t):
    a, b = R["s1"], R["s2"]
    return a*b / (a*a*np.sin(t)**2 + b*b*np.cos(t)**2)**1.5

# ---------------- main ----------------
def main(path):
    case = json.load(open(path))
    A, T, ez_in, U, A_free = build_thread(case)
    n = case["thread"]["n"]
    out = {}
    print("THREAD")
    for k in range(n):
        print(f"  T{k}: A={A[k].round(15).tolist()} T={T[k].round(15).tolist()}")

    # ---- item 1: rho* for each hang ----
    hangs = case["hangs"]
    def g_fix(j, rho):
        hg = hangs[j]; h = hg["host"]; w = int(hg["fix"]["with"][1:])
        AH, TH, d, e = hang_geom(A, T, ez_in, h, hg["side"], rho, hg["psi"], hg["delta"])
        return torus_gap(AH, TH, A[w], T[w])[0]
    roots = []
    for j, hg in enumerate(hangs):
        grid = np.arange(1.0, 180.0, 1.0)
        gv = []
        for r in grid:
            try: gv.append(g_fix(j, r))
            except AssertionError: gv.append(np.nan)
        gv = np.array(gv)
        ok = ~np.isnan(gv)
        sc = [i for i in range(len(grid)-1) if ok[i] and ok[i+1] and gv[i]*gv[i+1] < 0]
        print(f"H{j+1}: scan rho = 1..179 step 1: hang-link root found at {int(ok.sum())} of {len(grid)} points; "
              f"min g = {np.nanmin(gv):+.4f}; sign changes of g_fix at {[(float(grid[i]), float(grid[i+1])) for i in sc]}")
        rr = [bisect(lambda r: g_fix(j, r), grid[i], grid[i+1], tol=1e-12) for i in sc]
        roots.append(rr)
        print(f"   roots (deg): {[f'{r:.9f}' for r in rr]}")
    out["roots"] = roots

    # ---- item 1 (uniqueness): monotonicity of g on the proposed common bracket ----
    BR = (57.2, 57.3)
    hstep = 0.002; hd = 1e-5
    grid = np.arange(BR[0], BR[1] + hstep/2, hstep)
    for j in range(len(hangs)):
        gv = np.array([g_fix(j, r) for r in grid])
        dg = np.array([(g_fix(j, r+hd) - g_fix(j, r-hd))/(2*hd) for r in grid])
        M2 = np.max(np.abs(np.diff(dg)))/hstep
        print(f"H{j+1}: bracket {list(BR)}: g(lo)={gv[0]:+.6e} g(hi)={gv[-1]:+.6e}; "
              f"dg/drho in [{dg.min():+.6e},{dg.max():+.6e}] per deg; |g''| est <= {M2:.3e} per deg^2; "
              f"max dg + M2*h/2 = {dg.max() + M2*hstep/2:+.6e}; sign changes on grid: "
              f"{int(np.sum(np.sign(gv[:-1]) != np.sign(gv[1:])))}")
    rho_star = roots[0][0]
    return A, T, ez_in, U, A_free, hangs, g_fix, rho_star, out

def full_checks(A, T, ez_in, U, A_free, hangs, rho_star):
    n = len(A)
    tori = {f"T{k}": (A[k], T[k]) for k in range(n)}
    rings = {}
    owner = {}; threads = {}
    for k in range(n-1):
        rings[f"R{k}"] = build_ring(A[k], T[k], A[k+1], T[k+1]); threads[f"R{k}"] = [f"T{k}", f"T{k+1}"]
    # free ring of last torus: same link rule, no torus at the second point (mirror link, T_next = T reflected)
    u = U[n-1]; Tn = unit(T[n-1] - 2*(T[n-1] @ u)*u)
    rings[f"R{n-1}"] = build_ring(A[n-1], T[n-1], A_free, Tn); threads[f"R{n-1}"] = [f"T{n-1}"]
    hinfo = {}
    for j, hg in enumerate(hangs):
        h = hg["host"]
        AH, TH, d, e = hang_geom(A, T, ez_in, h, hg["side"], rho_star, hg["psi"], hg["delta"])
        nm = f"H{j+1}"; tori[nm] = (AH, TH)
        rings[f"RH{j+1}"] = build_ring(A[h], T[h], AH, TH); threads[f"RH{j+1}"] = [nm, f"T{h}"]
        hinfo[nm] = dict(host=h, d=d, e=e, AH=AH, TH=TH, with_=hg["fix"]["with"])
        print(f"{nm}: host T{h}, d={d:.12f}, A_H={AH.round(9).tolist()}, T_H={TH.round(9).tolist()}")
    # ---- tori pairs G-4 ----
    names = list(tori)
    structural = set((f"T{k}", f"T{k+1}") for k in range(n-1)) | set((f"T{v['host']}", nm) for nm, v in hinfo.items())
    fixpairs = set((v["with_"], nm) for nm, v in hinfo.items())
    print("\nG-4 torus pairs")
    contacts = []
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            a, b = names[i], names[j]
            (A1, T1), (A2, T2) = tori[a], tori[b]
            dc = np.linalg.norm(A1 - A2)
            key = (a, b) if (a, b) in structural | fixpairs else (b, a)
            if dc > 2 + 1e-9 and key not in structural and key not in fixpairs:
                print(f"  {a}-{b}: centres {dc:.6f} > 2  -> SEPARATED (exact cut-off)")
                continue
            g, mins, smin, slack = torus_gap(A1, T1, A2, T2)
            tag = "STRUCTURAL/IMPOSED" if key in structural else ("FIX/IMPOSED" if key in fixpairs else "")
            if not tag:
                tag = "SEPARATED" if smin - slack > 0 else ("CANDIDATE" if g > -1e-12 else "PENETRATION")
            print(f"  {a}-{b}: centres {dc:.6f}, gap {g:+.3e}, minima {len(mins)}, sample-min {smin:+.3e}, slack {slack:.2e} -> {tag}")
            if tag.endswith("IMPOSED"):
                contacts.append((a, b, mins, tag))
    # ---- J5 on contacts ----
    print("\nJ5 on contacts (v = T x (c - A), g = sign(vA.vB))")
    edges = []
    for a, b, mins, tag in contacts:
        (A1, T1), (A2, T2) = tori[a], tori[b]
        U1, V1 = perp_basis(T1)
        for ph in mins:
            P1 = A1 + R_MID*(np.cos(ph)*U1 + np.sin(ph)*V1)
            w = P1 - A2; hh = w @ T2; radial = unit(w - hh*T2); P2 = A2 + R_MID*radial
            c = 0.5*(P1 + P2); nvec = unit(P2 - P1)
            vA = np.cross(T1, c - A1); vB = np.cross(T2, c - A2)
            cos = (vA @ vB)/np.linalg.norm(vA)/np.linalg.norm(vB)
            par = np.linalg.norm(np.cross(T1, T2))
            print(f"  {a}-{b} [{tag}]: |TAxTB|={par:.6e}, |n.TA|={abs(nvec@T1):.4f}, |n.TB|={abs(nvec@T2):.4f}, cos={cos:+.6f}, g={int(np.sign(cos)):+d}")
            edges.append((a, b, int(np.sign(cos)), par, tag))
    # ---- rings ----
    print("\nRINGS")
    for nm, R in rings.items():
        print(f"  {nm}: threads {threads[nm]}, s1={R['s1']:.9f}, s2={R['s2']:.9f}, perim={ellipse_perimeter(R['s1'],R['s2']):.12f}, normal={R['n'].round(9).tolist()}")
    # G-5b-d: ring vs threaded torus, planar reduction
    print("\nG-5b-d ring vs threaded torus (planar reduction: ellipse vs two circles r=0.5 at A +- 0.5 w)")
    t = np.linspace(-np.pi, np.pi, 400001)
    for nm, R in rings.items():
        P = ring_pts(R, t)
        for tn in threads[nm]:
            At, Tt = tori[tn]
            wv = unit(np.cross(R["n"], Tt))
            tc = ring_param_of(R, At)
            kap = curvature_at(R, tc)
            f = np.minimum(np.linalg.norm(P - (At + 0.5*wv), axis=1), np.linalg.norm(P - (At - 0.5*wv), axis=1)) - 0.5
            dt = np.angle(np.exp(1j*(t - tc)))
            o = np.argsort(dt); dts, fs = dt[o], f[o]
            plus, minus = fs[dts > 0], fs[dts < 0][::-1]
            def mono_until(v):
                dv = np.diff(v); i = np.where(dv < -1e-15)[0]
                return (v[i[0]] if len(i) else np.inf)
            w = [float(fs[np.abs(dts) >= L].min()) for L in (0.05, 0.1, 0.2)]
            print(f"  {nm} vs {tn}: kappa_r = {kap:.6f} (radius {1/kap:.6f}), margin 2-kappa = {2-kap:.6f}; "
                  f"f>0 off cusp: {bool(np.all(fs[np.abs(dts) > 1e-4] > 0))}; f increases from cusp until f >= "
                  f"{min(mono_until(plus), mono_until(minus)):.4f}; min f for |t-tc|>=0.05/0.1/0.2: "
                  f"{w[0]:.5f}/{w[1]:.5f}/{w[2]:.5f}")
    # G-5a: ring vs foreign tori
    print("\nG-5a ring vs non-threaded tori: min_t dist(E(t), mid-circle) - 0.5")
    t2 = np.linspace(-np.pi, np.pi, 20001)
    worst = (np.inf, None)
    for nm, R in rings.items():
        P = ring_pts(R, t2)
        row = []
        for tn, (At, Tt) in tori.items():
            if tn in threads[nm]: continue
            f = pt_circle_dist(P, At, Tt) - R_MID
            i = int(np.argmin(f))
            fun = lambda tt: (pt_circle_dist(ring_pts(R, np.array([tt])), At, Tt) - R_MID)[0]
            x, v = golden_min(fun, t2[i] - 2*np.pi/20000, t2[i] + 2*np.pi/20000)
            row.append(f"{tn}:{v:+.4f}")
            if v < worst[0]: worst = (v, f"{nm} vs {tn}")
        print(f"  {nm}: " + "  ".join(row))
    print(f"  smallest G-5a margin: {worst[0]:+.6f} ({worst[1]})")
    # A-15
    print("\nA-15 rings per hole")
    for tn in tori:
        cnt = [nm for nm in rings if tn in threads[nm]]
        print(f"  {tn}: {len(cnt)} {cnt}")
    # ring pairs
    print("\nRING PAIRS")
    rn = list(rings)
    for i in range(len(rn)):
        for j in range(i+1, len(rn)):
            a, b = rn[i], rn[j]; Ra, Rb = rings[a], rings[b]
            shared = set(threads[a]) & set(threads[b])
            cr = np.linalg.norm(np.cross(Ra["n"], Rb["n"]))
            if shared:
                tn = shared.pop(); At, Tt = tori[tn]
                ang = []
                for R in (Ra, Rb):
                    tc = ring_param_of(R, At); P = ring_pts(R, np.array([tc + 0.3, tc - 0.3]))
                    mid = P.mean(axis=0) - At; mid = mid - (mid @ Tt)*Tt
                    ang.append(mid)
                U1, V1 = perp_basis(Tt)
                angs = [np.degrees(np.arctan2(m @ V1, m @ U1)) for m in ang]
                diff = abs((angs[0] - angs[1] + 180) % 360 - 180)
                print(f"  {a}-{b}: R-1 shared cusp {tn}, half-plane angle difference {diff:.4f} deg")
                continue
            if cr < 1e-12:
                dist = abs(Ra["n"] @ (Rb["C"] - Ra["C"]))
                if dist < 1e-12:
                    # R-4 coplanar: separating direction along centre line (support functions)
                    dvec = unit(Rb["C"] - Ra["C"])
                    def h(R, dv): 
                        a1 = R["s1"]*(dv @ R["E1"]); a2 = R["s2"]*(dv @ R["E2"]); return dv @ R["C"] + np.hypot(a1, a2)
                    sep = -h(Rb, -dvec) - h(Ra, dvec)
                    print(f"  {a}-{b}: R-4 coplanar, separation along centre line = {sep:.6f}")
                else:
                    print(f"  {a}-{b}: R-3 parallel distinct planes, distance = {dist:.9f}")
                continue
            # R-2: line l = plane intersection; chords
            na, nb = Ra["n"], Rb["n"]
            dl = unit(np.cross(na, nb))
            M = np.array([na, nb, dl]); rhs = np.array([na @ Ra["C"], nb @ Rb["C"], 0.0])
            p0 = np.linalg.solve(M, rhs)
            def chord(R):
                q = p0 - R["C"]
                x0, x1 = q @ R["E1"]/R["s1"], dl @ R["E1"]/R["s1"]
                y0, y1 = q @ R["E2"]/R["s2"], dl @ R["E2"]/R["s2"]
                aa = x1*x1 + y1*y1; bb = 2*(x0*x1 + y0*y1); cc = x0*x0 + y0*y0 - 1
                disc = bb*bb - 4*aa*cc
                if disc < 0: return None
                r = np.sqrt(disc); return sorted([(-bb - r)/(2*aa), (-bb + r)/(2*aa)])
            ca, cb = chord(Ra), chord(Rb)
            Pa = ring_pts(Ra, t2); Pb = ring_pts(Rb, np.linspace(-np.pi, np.pi, 4001))
            dmin = min(np.min(np.linalg.norm(Pa - q, axis=1)) for q in Pb)
            if ca is None or cb is None:
                print(f"  {a}-{b}: R-2, chord {'none' if ca is None else 'ok'}/{'none' if cb is None else 'ok'} -> no meeting, Lk=0; sampled min distance {dmin:.4f}")
                continue
            ends = sorted([(ca[0], 'a'), (ca[1], 'a'), (cb[0], 'b'), (cb[1], 'b')])
            pattern = ''.join(x[1] for x in ends)
            gapmin = min(abs(x - y) for x in ca for y in cb)
            lk = 1 if pattern in ('abab', 'baba') else 0
            print(f"  {a}-{b}: R-2, chords a={np.round(ca,6).tolist()} b={np.round(cb,6).tolist()}, order {pattern}, min |end-end| {gapmin:.6f}, Lk={lk}; sampled min distance {dmin:.4f}")
    return edges

if __name__ == "__main__":
    A, T, ez_in, U, A_free, hangs, g_fix, rho_star, out = main(sys.argv[1])
    print(f"\nrho* used for the configuration: {rho_star:.12f} deg")
    full_checks(A, T, ez_in, U, A_free, hangs, rho_star)
