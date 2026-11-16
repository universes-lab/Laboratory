#!/usr/bin/env python3
# q1_01.py — Q1-01 static geometry, single Q1
# Run: python3 q1_01.py > q1_01_out.txt
import numpy as np
import itertools
from collections import Counter

KZ = np.array([0., 0., 1.]); KX = np.array([1., 0., 0.]); KY = np.array([0., 1., 0.])

def runit(rng, N):
    V = rng.normal(size=(N, 3))
    return V / np.linalg.norm(V, axis=1, keepdims=True)

def basis(n):
    n = n / np.linalg.norm(n)
    a = np.array([1., 0., 0.]) if abs(n[0]) < 0.9 else np.array([0., 1., 0.])
    u = np.cross(n, a); u /= np.linalg.norm(u); v = np.cross(n, u)
    return u, v

def basis_b(nn):
    a = np.where(np.abs(nn[:, 0:1]) < 0.9,
                 np.tile([1., 0., 0.], (len(nn), 1)),
                 np.tile([0., 1., 0.], (len(nn), 1)))
    u = np.cross(nn, a); u /= np.linalg.norm(u, axis=1, keepdims=True)
    v = np.cross(nn, u); return u, v

def ring_pt(n, c, r, N=3600):
    u, v = basis(n); t = np.linspace(0, 2*np.pi, N, endpoint=False)
    return c + r*(np.cos(t)[:, None]*u + np.sin(t)[:, None]*v)

def ring_pt_b(nn, c, r, N=3600):
    u, v = basis_b(nn); t = np.linspace(0, 2*np.pi, N, endpoint=False)
    return c + r*(np.cos(t)[None, :, None]*u[:, None, :] + np.sin(t)[None, :, None]*v[:, None, :])

def F_tor(P, k):
    h = P @ k
    return (np.linalg.norm(P - h[..., None]*k, axis=-1) - 0.5)**2 + h**2 - 0.25

def G_sph(P): return np.linalg.norm(P, axis=-1) - 1.

def cls_F(m):
    if m < -1e-9: return 'проникновение'
    if m <= 1e-6: return 'касание'
    return 'свободно'

def cls_G(G):
    if np.all(np.abs(G) <= 1e-9): return 'на оболочке'
    if G.min() < -1e-9 and G.max() > 1e-9: return 'пересекает'
    if np.abs(G).min() <= 1e-6: return 'касание'
    if G.max() < -1e-6: return 'внутри'
    return 'снаружи'

def cnt(F, thr=1e-6):
    if np.all(F <= thr): return -1
    return int(((F < np.roll(F, 1)) & (F < np.roll(F, -1)) & (F <= thr)).sum())

def sp_mats():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([-1, 1], repeat=3):
            M = np.zeros((3, 3))
            for i, j in enumerate(p): M[i, j] = s[i]
            out.append(M)
    return out
SPM = sp_mats()

def mpm(M, v):
    Mv = M @ v
    return np.allclose(Mv, v, atol=1e-9) or np.allclose(Mv, -v, atol=1e-9)

def dsym(cond):
    return [M for M in SPM if all(c is None or mpm(M, c) for c in cond)]

def mstr(M): return '[' + ';'.join(''.join(f'{int(round(x)):2d}' for x in r) for r in M) + ']'

def axial(N=2000):
    t = np.linspace(0, 2*np.pi, N, endpoint=False)
    return 0.5*np.stack([np.cos(t), np.sin(t), np.zeros(N)], axis=1)

def glink(g1, g2):
    d1 = np.roll(g1, -1, axis=0) - g1
    d2 = np.roll(g2, -1, axis=0) - g2
    diff = g1[:, None, :] - g2[None, :, :]
    r = np.linalg.norm(diff, axis=-1)
    if r.min() < 1e-8: return None
    cr = np.cross(d1[:, None, :], d2[None, :, :])
    return (np.einsum('ijk,ijk->ij', diff, cr) / r**3).sum() / (4*np.pi)

def arc(n1, n2, steps=200):
    n1 = n1/np.linalg.norm(n1); n2 = n2/np.linalg.norm(n2)
    c = np.clip(np.dot(n1, n2), -1, 1); om = np.arccos(c)
    if om < 1e-12: return [n1]*(steps+1)
    ax = np.cross(n1, n2)
    if np.linalg.norm(ax) < 1e-12:
        ax = np.array([0., 0., 1.]) if abs(n1[2]) < 0.9 else np.array([1., 0., 0.])
    ax /= np.linalg.norm(ax)
    return [n1*np.cos(om*k/steps) + np.cross(ax, n1)*np.sin(om*k/steps) for k in range(steps+1)]

def analyze(n, c, r, k, N=3600):
    P = ring_pt(n, c, r, N); F = F_tor(P, k)
    return F.min(), cls_F(F.min()), cnt(F)

def main():
    rng = np.random.default_rng(20261116)

    # A1
    print("=== A1. Размеры и центр ===")
    print("внешний радиус тора (a+b) = 1  (П1)")
    print("радиус кольца = 1  (П1)")
    print("радиус сферы = 1  (П1)")
    print("центр тора = (0,0,0)  (П3)")
    print("центр кольца = (0,0,0)  (П3)")
    print("три радиуса равны: 1 = 1 = 1")

    # A2
    print("\n=== A2. У-1 (аналитика) ===")
    print("Для p∈K(n): |p|=1, ρ²+h²=1 ⇒ F(p)=(ρ−½)²+h²−¼ = 1−ρ ≥ 0.")
    print("Точки касания: при |n_z|=1 — вся окружность; при |n_z|<1 — p_±=±(e_z×n)/|e_z×n|.")

    # A3
    print("\n=== A3. У-2 (аналитика) ===")
    print("K(n)⊂{p:|p|=1}=S по определению.")

    # A4
    print("\n=== A4. Численная проверка (100000 нормалей × 3600 точек) ===")
    ns = runit(rng, 100000); B = 500; N = 3600
    mins = np.zeros(len(ns)); cc = np.zeros(len(ns), dtype=int)
    for i0 in range(0, len(ns), B):
        b = ns[i0:i0+B]
        Fs = F_tor(ring_pt_b(b, np.zeros(3), 1.0, N), KZ)
        for j in range(len(b)):
            fj = Fs[j]; mins[i0+j] = fj.min(); cc[i0+j] = cnt(fj)
    print(f"min F по всем точкам всех колец: {mins.min():.3e}")
    print(f"число колец с проникновением: {int((mins < -1e-9).sum())}")
    msk = np.abs(ns[:, 2]) < 1 - 1e-6
    dist = Counter(cc[msk].tolist())
    print(f"распределение точек касания (|n_z|<1−10⁻⁶): {dict(sorted(dist.items()))}")
    nzr = analyze(KZ, np.zeros(3), 1.0, KZ)
    print(f"n=e_z: класс={nzr[1]}, число={nzr[2]}")

    # A5(а)
    print("\n=== A5(а). Радиус кольца ===")
    ns2 = runit(rng, 2000)
    for r in [0.90, 0.99, 1.00, 1.01, 1.10]:
        best = 1e9; worst = -1e9; wcls = 'свободно'
        for n in list(ns2) + [KZ, -KZ, KX, -KX]:
            P = ring_pt(n, np.zeros(3), r, N); F = F_tor(P, KZ)
            if F.min() < best: best = F.min()
            if F.min() < -1e-9 and wcls != 'проникновение': wcls = 'проникновение'
            elif F.min() <= 1e-6 and wcls == 'свободно': wcls = 'касание'
        G = G_sph(ring_pt(KZ, np.zeros(3), r, N))
        print(f"r={r:.2f}: min F={best:.4e}, худший класс={wcls}, при n=e_z: {cls_G(G)}")

    # A5(б)
    print("\n=== A5(б). Смещение центра, тор ===")
    dvals = [0, 0.25, 0.5, 0.75, 0.99, 1.00, 1.01, 1.5, 1.99, 2.00, 2.5]
    ax = axial()
    for n, nl in [(KZ, 'e_z'), (KY, 'e_y'), (KX, 'e_x')]:
        for e, el in [(KX, 'e_x'), (KY, 'e_y'), (KZ, 'e_z')]:
            for d in dvals:
                c = d * e
                P = ring_pt(n, c, 1.0, N); F = F_tor(P, KZ)
                m = F.min(); k = cls_F(m); cc2 = cnt(F)
                tag = ''
                if k == 'касание' and cc2 > 0:
                    prev = np.roll(F, 1); nxt = np.roll(F, -1)
                    idx = np.where((F < prev) & (F < nxt) & (F <= 1e-6))[0]
                    pts = ' '.join(f'({P[i,0]:.4f},{P[i,1]:.4f},{P[i,2]:.4f})' for i in idx[:4])
                    tag = f' точки: {pts}'
                L_s = '—'
                if k != 'проникновение':
                    Lg = glink(P, ax)
                    L_s = f'{Lg:.6f} (≈{round(Lg)})' if Lg is not None else '—'
                print(f"n={nl}, e={el}, d={d:5.2f}: min F={m:+.4e} класс={k} контактов={cc2} L={L_s}{tag}")

    # A5(в)
    print("\n=== A5(в). Смещение центра, сфера ===")
    for n, nl in [(KZ, 'e_z'), (KX, 'e_x')]:
        for e, el in [(KX, 'e_x'), (KZ, 'e_z')]:
            for d in dvals:
                P = ring_pt(n, d*e, 1.0, N); G = G_sph(P)
                print(f"n={nl}, e={el}, d={d:5.2f}: min G={G.min():+.4e}, max G={G.max():+.4e}, {cls_G(G)}")

    # B1
    print("\n=== B1. Наклон кольца у тора ===")
    for th_deg in [0, 1, 5, 15, 30, 45, 60, 75, 85, 89, 90]:
        th = np.radians(th_deg); n = np.array([np.sin(th), 0., np.cos(th)])
        P = ring_pt(n, np.zeros(3), 1.0, N); F = F_tor(P, KZ)
        cc2 = cnt(F)
        if cc2 == -1: cps = 'окружность'
        elif cc2 > 0:
            prev = np.roll(F,1); nxt = np.roll(F,-1)
            idx = np.where((F < prev) & (F < nxt) & (F <= 1e-6))[0]
            cps = ' '.join(f'({P[i,0]:+.3f},{P[i,1]:+.3f},{P[i,2]:+.3f})' for i in idx)
        else: cps = '—'
        ds = dsym([KZ, n])
        # continuous around KZ?
        cont = np.allclose(np.abs(np.dot(KZ, n)), 1)
        print(f"θ={th_deg:3d}°: min F={F.min():.2e}, касание={cps}, |sym|={len(ds)}, непрерывная={cont}")
        for M in ds: print(f"   {mstr(M)}")

    # B2
    print("\n=== B2. Сфера + K(e_z) ===")
    ds = dsym([KZ])
    print(f"|sym|={len(ds)}, непрерывная=True (вокруг e_z)")
    for M in ds: print(f"   {mstr(M)}")

    # B3
    print("\n=== B3. Кандидаты ===")
    th = np.radians(45); nn = np.array([np.sin(th), 0., np.cos(th)])
    cands = [
        ('С', 'sph', KZ, KZ), ('С', 'sph', KZ, KX),
        ('Э', KZ, KZ, KZ), ('Э', KZ, KZ, KX),
        ('М', KZ, KX, KZ), ('М', KZ, KX, KX), ('М', KZ, KX, KY),
        ('Н', KZ, nn, KZ), ('Н', KZ, nn, nn), ('Н', KZ, nn, KY),
    ]
    def bl(bt, k, v):
        if isinstance(bt, str) and bt == 'sph': return 'сфера'
        t = float(np.dot(v, k))
        if abs(abs(t) - 1) < 1e-9: return 'вдоль'
        if abs(t) < 1e-9: return 'поперёк'
        return 'наклон'
    def rl(n, v):
        t = float(np.dot(v, n))
        if abs(abs(t) - 1) < 1e-9: return 'вдоль'
        if abs(t) < 1e-9: return 'поперёк'
        return 'наклон'
    def vm(v):
        for nm, x in [('e_z', KZ), ('e_x', KX), ('e_y', KY), ('n', nn)]:
            if np.allclose(v, x, atol=1e-9): return nm
        return '?'
    for cls, body, n, V in cands:
        b = bl(body, body if not isinstance(body, str) else None, V) if not isinstance(body, str) else 'сфера'
        if isinstance(body, str): b = 'сфера'
        else: b = bl('tor', body, V)
        r = rl(n, V)
        cond = [] if isinstance(body, str) else [body]
        cond.append(n); cond.append(V)
        ds = dsym(cond)
        cont = False
        if isinstance(body, str):
            if np.allclose(np.abs(np.dot(V, n)), 1): cont = True
        else:
            if np.allclose(np.abs(np.dot(V, body)), 1) and np.allclose(np.abs(np.dot(V, n)), 1): cont = True
        print(f"класс={cls}, тело={body if isinstance(body, str) else 'T('+vm(body)+')'}, n={vm(n)}, V={vm(V)}: тело={b}, кольцо={r}, |sym|={len(ds)}, непр={cont}")

    # B4(а)
    print("\n=== B4(а). Пути поворота ===")
    for name, n1, n2, body in [('Э→М T(e_z)', KZ, KX, 'tor'), ('М→М T(e_z)', KX, KY, 'tor'), ('С→С S', KZ, KX, 'sph')]:
        path = arc(n1, n2, 200)
        print(f"{name}:")
        if body == 'tor':
            Fmin_all = 1e9; stats = Counter()
            for n in path:
                P = ring_pt(n, np.zeros(3), 1.0, 3600); F = F_tor(P, KZ)
                Fmin_all = min(Fmin_all, F.min())
                c = cnt(F); stats['окр' if c == -1 else c] += 1
            print(f"  min F по всему пути={Fmin_all:.3e}, шагов с окр/2/иное: {dict(stats)}")
        else:
            Gmin = 1e9; Gmax = -1e9
            for n in path:
                P = ring_pt(n, np.zeros(3), 1.0, 3600); G = G_sph(P)
                Gmin = min(Gmin, G.min()); Gmax = max(Gmax, G.max())
            print(f"  min G={Gmin:.3e}, max G={Gmax:.3e}")

    # B4(в)
    print("\n=== B4(в). Класс М, k и n ===")
    print("Три кандидата М: k=e_z, n=e_x у всех — k и n одинаковы. Различие: 'одинаково'.")

    # C
    print("\n=== C. Скорости в точках касания ===")
    def vcross(u, p): return np.cross(u, p)
    def cosang(a, b):
        na = np.linalg.norm(a); nb = np.linalg.norm(b)
        if na < 1e-12 or nb < 1e-12: return 0.0, True
        return float(np.dot(a, b)/(na*nb)), False
    rows = [
        ('Qd', 'sph', KZ, KZ, [(KZ, 'e_z')], [(KZ, 'e_z')]),
        ('Qu', 'sph', KX, KX, [(KZ, 'e_z')], [(KX, 'e_x'), (KZ, 'e_z-мер')]),
        ('Qs', 'tor', KZ, KZ, [(KZ, 'e_z')], [(KZ, 'e_z')]),
        ('Qc', 'tor', KZ, KX, [(KZ, 'e_z')], [(KX, 'e_x'), (KZ, 'e_z-мер')]),
        ('Qt', 'tor', KX, KZ, [(KX, 'e_x'), (KZ, 'e_z-мер')], [(KZ, 'e_z')]),
        ('Qb-A', 'tor', KX, KY, [(KX, 'e_x'), (KZ, 'e_z-мер')], [(KX, 'e_x-диам'), (KZ, 'e_z-мер')]),
        ('Qb-B', 'tor', KX, KY, [(KX, 'e_x'), (KZ, 'e_z-мер')], [(KY, 'e_y'), (KX, 'e_x-диам')]),
        ('Э-x', 'tor', KX, KX, [(KX, 'e_x'), (KZ, 'e_z-мер')], [(KX, 'e_x'), (KZ, 'e_z-мер')]),
    ]
    for cid, bt, k, n, r2d, r1d in rows:
        if abs(abs(np.dot(n, k)) - 1) < 1e-9:
            # circumference contact
            u, v = basis(n)
            pts = [u*np.cos(a) + v*np.sin(a) for a in np.linspace(0, 2*np.pi, 8, endpoint=False)]
            tag = 'окр'
        else:
            pc = np.cross(k, n); pc /= np.linalg.norm(pc)
            pts = [pc, -pc]
            tag = '2т'
        summary = []
        for ud, un in r2d:
            for ue, uen in r1d:
                co = []
                for p in pts:
                    v2d = vcross(ud, p); v1d = vcross(ue, p)
                    cc, deg = cosang(v2d, v1d)
                    co.append(cc)
                nz = [x for x in co if abs(x) > 1e-12]
                if not nz: sm = '0'
                elif all(abs(abs(x) - 1) < 1e-9 for x in nz): sm = 'коллинеарны'
                elif all(abs(x) < 1e-9 for x in nz): sm = 'ортогональны'
                else: sm = 'прочие'
                summary.append((un, uen, sm, co))
        print(f"{cid} (k={'e_x' if np.allclose(k,KX) else 'e_z'}, n={'e_y' if np.allclose(n,KY) else ('e_x' if np.allclose(n,KX) else 'e_z')}, {tag}):")
        for un, uen, sm, co in summary:
            cos_str = ', '.join(f'{x:+.3f}' for x in co)
            print(f"  ({un}, {uen}): cos=[{cos_str}] → {sm}")

if __name__ == '__main__':
    main()
