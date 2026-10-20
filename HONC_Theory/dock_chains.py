"""Причал прямых латчерных цепочек длины L к λ-молекуле (вариант (а)), геометрия без закона контакта.

Цепочка: от тора-хозяина по направлению u строятся L звеньев по правилу ЛМ1 (зеркальный тор + кольцо через
центры двух соседних торов). Направление u одно для всех звеньев — прямая цепочка (оси торов чередуются
зеркально, кольца в одной плоскости). Проверки: торы цепочки не пересекают торы сборки и друг друга; кольца
цепочки проходят вне чужих торов; кольца сборки — вне торов цепочки; в глюоне с квантроном — вне шара радиуса 1.

Для каждой длины L печатает:
  - сколько направлений свободно для одной цепочки на одном хозяине (сетка 10°);
  - сколько цепочек на тор помещается одновременно, если все торы сборки несут один узор
    (жадный поиск, нижняя оценка; образы по симметрии сборки).

Запуск: python3 dock_chains.py N beta [quantron] [Lmax]
"""
import numpy as np, sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import docking as D

N = int(sys.argv[1]); beta = float(sys.argv[2]); quantron = 'quantron' in sys.argv
Lmax = int([a for a in sys.argv[3:] if a.isdigit()][0]) if any(a.isdigit() for a in sys.argv[3:]) else 5
g, tori, rings = D.assembly(N, beta)
T0, eo, et = D.frame(0, tori)
TOL = D.TOL
ASM_SURF = [D.torus_surface(A, T, 30) for A, T in tori]


def Ry(th):
    c, s = np.cos(th), np.sin(th)
    return np.array([[c, 0, -s], [0, 1, 0], [s, 0, c]])


REF = np.diag([1.0, -1.0, 1.0])
def M(i):
    m = Ry(i * 2 * np.pi / N)
    return m @ REF if (i % 2 and N > 2) else m


def build_chain(uh, L):
    links = []; A, T = tori[0]
    for k in range(L):
        lk = D.dock_link(A, T, uh)
        if lk is None or lk['Rcurv'] < D.a - 1e-6:
            return None
        R = D.ring_points(lk['C'], lk['u'], lk['W'], lk['p'], lk['q'], 300)
        links.append(dict(A=lk['A2'], T=lk['T2'], S=D.torus_surface(lk['A2'], lk['T2'], 30), R=R))
        A, T = lk['A2'], lk['T2']
    return links


def chain_ok(ch):
    """Цепочка против сборки и против самой себя."""
    for k, lk in enumerate(ch):
        for j, (A, T) in enumerate(tori):
            if np.linalg.norm(lk['A'] - A) < 0.05:
                return False
            if (j != 0 or k > 0) and (D.memb(lk['S'], A, T).min() < 1 - TOL or D.memb(ASM_SURF[j], lk['A'], lk['T']).min() < 1 - TOL):
                return False
            if D.memb(lk['R'], A, T).min() < 1 - TOL:
                return False
        for rp in rings:
            if D.memb(rp, lk['A'], lk['T']).min() < 1 - TOL:
                return False
        for m, ll in enumerate(ch):
            if abs(m - k) > 1 and D.memb(lk['S'], ll['A'], ll['T']).min() < 1 - TOL:
                return False
            if m != k and m != k + 1 and D.memb(lk['R'], ll['A'], ll['T']).min() < 1 - TOL:
                return False
        if quantron and (np.linalg.norm(lk['S'], axis=1).min() < 1 - TOL or np.linalg.norm(lk['R'], axis=1).min() < 1 - TOL):
            return False
    return True


def image(ch, i):
    m = M(i)
    return [dict(A=m @ lk['A'], T=m @ lk['T'], S=lk['S'] @ m.T, R=lk['R'] @ m.T) for lk in ch]


def chains_compatible(c1, c2):
    for a in c1:
        for b in c2:
            if np.linalg.norm(a['A'] - b['A']) < 0.05:
                return False
            if D.memb(a['S'], b['A'], b['T']).min() < 1 - TOL or D.memb(b['S'], a['A'], a['T']).min() < 1 - TOL:
                return False
            if D.memb(a['R'], b['A'], b['T']).min() < 1 - TOL or D.memb(b['R'], a['A'], a['T']).min() < 1 - TOL:
                return False
    return True


dirs = []
for al in range(10, 180, 10):
    for ps in range(0, 360, 10):
        ar, pr = np.radians(al), np.radians(ps)
        dirs.append((al, ps, np.cos(ar) * T0 + np.sin(ar) * (np.cos(pr) * eo + np.sin(pr) * et)))
rng = np.random.default_rng(3)
print(f"N={N} beta={beta} quantron={quantron}")
alive = dirs
for L in range(1, Lmax + 1):
    cands = []
    for al, ps, uh in alive:
        ch = build_chain(uh, L)
        if ch is not None and chain_ok(ch):
            cands.append((al, ps, uh, ch))
    alive = [(al, ps, uh) for al, ps, uh, ch in cands]
    best = []
    for trial in range(25):
        order = rng.permutation(len(cands)); chosen = []; allimgs = []
        for k in order:
            ch = cands[k][3]
            imgs = [image(ch, i) for i in range(N)]
            if not all(chains_compatible(imgs[i], imgs[j]) for i in range(N) for j in range(i + 1, N)):
                continue
            if all(chains_compatible(u, v) for u in imgs for v in allimgs):
                chosen.append(cands[k]); allimgs += imgs
        if len(chosen) > len(best):
            best = chosen
    print(f"   L={L}: свободных направлений для одной цепочки {len(cands)}; на всех торах сразу — не меньше {len(best)} цепочек на тор; "
          f"направления (alpha, psi): {[(c[0], c[1]) for c in best]}", flush=True)
    if not cands:
        break
