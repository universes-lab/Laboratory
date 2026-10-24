"""Этап Б, первая задача (Интегратор, 24.10): межсборочный контакт кольцо — кольцо двух глюонов (N = 8, β = 65°, «вместе»).
Одним участником; кольца — провода толщины a = 0,015 (касание при зазоре 2a), ЛМ1.
1. Устойчивость касаний к возмущениям: поворот φ около 45°, наклон β обеих сборок, наклон оси B на ε, сдвиг B вбок на δ.
   Для нарушающих симметрию возмущений — разброс ΔD: насколько ещё надо сблизить пару после первого касания, чтобы коснулись все четыре.
2. Топология: гауссовы числа зацепления Lk(A_i, B_j) до касания и после взаимного прохождения проводов (модель без стенок).
3. Маршруты состояния (чтение R1 «прохождение на касании», [Г]): кольца режутся точками каспов (центры торов) и касаний;
   в каспе состояние идёт с входящего кольца на исходящее (узел защёлки), на касании — на кольцо другой сборки вперёд.
   Число замкнутых маршрутов, их длина (в длинах кольца 2π) и число переходов между сборками; для пары и для цепочки из трёх.
Запуск: python3 contact_pair.py"""
import numpy as np, sys, os, io, contextlib
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import importlib.util
from scipy.spatial import cKDTree
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
a = 0.015; y = np.array([0, 1.0, 0]); NP = 1200
def Rot(axis, ang):
    axis = np.asarray(axis, float); axis = axis / np.linalg.norm(axis)
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
def assembly(beta):
    g = h.build(8, beta); t = np.linspace(0, 2 * np.pi, NP, endpoint=False); R = []
    for r in g['rings']:
        P = r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])
        R.append(P if r['Om'] > 0 else P[::-1])
    return R, [np.array(A) for A in g['A']]
def place(R, A, M, shift): return [P @ M.T + shift for P in R], [M @ x + shift for x in A]
def pairdist(P, Q):
    d, j = cKDTree(Q).query(P); i = int(np.argmin(d)); return d[i], (i, int(j[i]))
def tang(P, i): t = P[(i + 1) % len(P)] - P[i - 1]; return t / np.linalg.norm(t)
RA, AA = assembly(65.0)
def contacts(RA, RB, tol=1e-3):
    out = []
    for i, P in enumerate(RA):
        for j, Q in enumerate(RB):
            d, k = pairdist(P, Q)
            if d < 2 * a + tol: out.append((i, j, d, k, float(tang(P, k[0]) @ tang(Q, k[1]))))
    return out
def first_contact(RA, RB_of_D, lo=1.8, hi=2.6):
    tA = cKDTree(np.vstack(RA)); gmin = lambda D: tA.query(np.vstack(RB_of_D(D)[0]))[0].min()
    # подход издалека: шаг вниз до первого касания, потом бисекция
    D = hi
    while D > lo and gmin(D) >= 2 * a: D -= 0.01
    lo2, hi2 = D, D + 0.01
    for _ in range(25):
        m = (lo2 + hi2) / 2; lo2, hi2 = (lo2, m) if gmin(m) >= 2 * a else (m, hi2)
    return hi2
print("1. Устойчивость касаний")
print("1а. Поворот φ (ось общая, β = 65°):")
for ph in (40, 42.5, 44, 45, 46, 47.5, 50):
    M = Rot(y, np.radians(ph)); RBf = lambda D, M=M: place(RA, AA, M, D * y)
    Dc = first_contact(RA, RBf); c = contacts(RA, RBf(Dc)[0])
    print(f"   φ={ph:5.1f}°: D_c={Dc:.4f}; касаний {len(c)}; угол касательных {np.degrees(np.arccos(min(1, abs(c[0][4])))):.1f}°; "
          f"обход {'сонаправленный' if all(x[4] > 0 for x in c) else 'смешанный'}", flush=True)
print("1б. Наклон β обеих сборок (φ = 45°):")
for b in (64.0, 64.5, 65.5, 66.0):
    RAb, AAb = assembly(b); M = Rot(y, np.pi / 4); RBf = lambda D, M=M, RAb=RAb, AAb=AAb: place(RAb, AAb, M, D * y)
    Dc = first_contact(RAb, RBf); c = contacts(RAb, RBf(Dc)[0])
    print(f"   β={b}: D_c={Dc:.4f}; касаний {len(c)}; угол {np.degrees(np.arccos(min(1, abs(c[0][4])))):.2f}°", flush=True)
print("1в. Нарушение симметрии (φ = 45°, β = 65°): ΔD — сколько ещё сблизить после первого касания, чтобы коснулись все четыре")
pairs45 = [(1, 2), (3, 4), (5, 6), (7, 0)]
def pair_D(i, j, RBf, lo=1.9, hi=2.6):
    f = lambda D: pairdist(RA[i], RBf(D)[0][j])[0] - 2 * a
    for _ in range(30):
        m = (lo + hi) / 2; lo, hi = (lo, m) if f(m) >= 0 else (m, hi)
    return hi
for kind, vals in (('наклон оси ε', (0.25, 0.5, 1.0, 2.0)), ('сдвиг вбок δ', (0.005, 0.02, 0.05))):
    for v in vals:
        if kind.startswith('наклон'):
            M = Rot(np.array([1.0, 0, 0]), np.radians(v)) @ Rot(y, np.pi / 4); RBf = lambda D, M=M: place(RA, AA, M, D * y)
        else:
            M = Rot(y, np.pi / 4); RBf = lambda D, M=M, v=v: place(RA, AA, M, D * y + np.array([v, 0, 0]))
        Ds = [pair_D(i, j, RBf) for i, j in pairs45]
        print(f"   {kind} = {v}: D касания по парам " + ", ".join(f"{d:.4f}" for d in Ds) + f"; ΔD = {max(Ds) - min(Ds):.4f}", flush=True)
print("\n2. Гауссовы числа зацепления Lk(A_i, B_j), φ = 45°")
def Lk(P, Q):
    dP = np.roll(P, -1, 0) - P; dQ = np.roll(Q, -1, 0) - Q; mP = P + dP / 2; mQ = Q + dQ / 2
    R = mP[:, None] - mQ[None]; num = np.einsum('ijk,ijk->ij', R, np.cross(dP[:, None], dQ[None]))
    return (num / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)
M45 = Rot(y, np.pi / 4)
for D in (2.6, 2.3, 2.2, 2.0):
    RB, _ = place(RA, AA, M45, D * y)
    L = np.array([[Lk(RA[i][::4], RB[j][::4]) for j in range(8)] for i in range(8)])
    nz = [(i, j, round(L[i, j])) for i in range(8) for j in range(8) if abs(L[i, j]) > 0.5]
    print(f"   D={D}: max|Lk| = {np.abs(L).max():.3f}; ненулевые: {nz if nz else 'нет'}", flush=True)
print("\n3. Маршруты состояния при чтении R1 (прохождение на касании вперёд по другому кольцу)")
def segments(rings, tori, contacts_by_ring):
    """Для каждого кольца: точки по ходу обхода (вход-касп, касания, выход-касп) и продолжения."""
    info = []
    for r, P in enumerate(rings):
        cs = np.array([np.argmin(np.linalg.norm(P - T, axis=1)) for T in tori]); dmin = np.array([np.linalg.norm(P - T, axis=1).min() for T in tori])
        two = np.argsort(dmin)[:2]; idx = cs[two]
        # вход — касп, после которого по ходу обхода идёт касание (между двумя каспами по короткой дуге через вершину)
        info.append(dict(tori=two, idx=idx))
    return info
ARC = {}
def routes(rings_by_tool, tori_by_tool, contact_list):
    # узлы: (tool, ring, позиция); отрезок = (tool, ring, k) между последовательными метками по ходу обхода
    marks = {}
    for t, (R, T) in enumerate(zip(rings_by_tool, tori_by_tool)):
        for r, P in enumerate(R):
            d = np.array([np.linalg.norm(P - x, axis=1).min() for x in T]); tw = np.argsort(d)[:2]
            ii = [int(np.argmin(np.linalg.norm(P - T[k], axis=1))) for k in tw]
            marks[(t, r)] = [('cusp', ii[0], int(tw[0])), ('cusp', ii[1], int(tw[1]))]
    for (t1, r1, i1, t2, r2, i2) in contact_list:
        marks[(t1, r1)].append(('ct', i1, (t2, r2, i2))); marks[(t2, r2)].append(('ct', i2, (t1, r1, i1)))
    n = NP
    # порядок меток по ходу обхода; отрезок начинается в метке и кончается в следующей
    order = {k: sorted(v, key=lambda m: m[1]) for k, v in marks.items()}
    def next_seg(t, r, mark):
        """Состояние пришло по кольцу (t, r) в метку mark; куда дальше."""
        if mark[0] == 'cusp':
            torus = mark[2]   # на какое кольцо той же сборки уходит из этого каспа
            for r2 in range(8):
                if r2 == r: continue
                for m in order[(t, r2)]:
                    if m[0] == 'cusp' and m[2] == torus: return (t, r2, m[1])
            raise RuntimeError
        t2, r2, i2 = mark[2]; return (t2, r2, i2)
    segs = []
    for k, ms in order.items():
        for q in range(len(ms)): segs.append((k[0], k[1], ms[q][1], ms[(q + 1) % len(ms)]))
    start = {(s[0], s[1], s[2]): s for s in segs}
    seen = set(); out = []
    for s in segs:
        if (s[0], s[1], s[2]) in seen: continue
        cur = s; L = 0.0; tools = []; crossings = 0
        while (cur[0], cur[1], cur[2]) not in seen:
            seen.add((cur[0], cur[1], cur[2])); tools.append(cur[0])
            e = cur[3][1]; P = rings_by_tool[cur[0]][cur[1]]; sl = ARC[id(P)] if id(P) in ARC else ARC.setdefault(id(P), np.r_[0, np.cumsum(np.linalg.norm(np.roll(P, -1, 0) - P, axis=1))])
            L += ((sl[e] - sl[cur[2]]) % sl[-1]) / sl[-1]
            nt, nr, ni = next_seg(cur[0], cur[1], cur[3])
            if nt != cur[0]: crossings += 1
            cur = start[(nt, nr, ni)]
        out.append((L, sorted(set(tools)), crossings))
    return out
def contact_list_for(R1, R2, t1, t2, tol=1e-3):
    cl = []
    for i, P in enumerate(R1):
        for j, Q in enumerate(R2):
            d, k = pairdist(P, Q)
            if d < 2 * a + tol: cl.append((t1, i, int(k[0]), t2, j, int(k[1])))
    return cl
Dc45 = first_contact(RA, lambda D: place(RA, AA, M45, D * y))
RB, AB = place(RA, AA, M45, Dc45 * y)
print(f"   (проверка: без касаний — маршрутов на сборку) A: {routes([RA], [AA], [])}")
cl = contact_list_for(RA, RB, 0, 1)
print(f"   пара, φ = 45°, касаний {len(cl)}: маршруты (длина в кольцах, сборки, переходов) = {routes([RA, RB], [AA, AB], cl)}")
M0 = np.eye(3); Dc0 = first_contact(RA, lambda D: place(RA, AA, M0, D * y)); RB0, AB0 = place(RA, AA, M0, Dc0 * y)
cl0 = contact_list_for(RA, RB0, 0, 1)
try: print(f"   пара, φ = 0°, касаний {len(cl0)}: маршруты = {routes([RA, RB0], [AA, AB0], cl0)}")
except Exception as e: print("   φ = 0°: на одном кольце два касания — маршрут неоднозначен:", e)
RC, AC = place(RA, AA, Rot(y, np.pi / 2), 2 * Dc45 * y)
clBC = contact_list_for(RB, RC, 1, 2); clAC = contact_list_for(RA, RC, 0, 2)
print(f"   цепочка A–B–C (B: 45°, C: 90° и 2·D_c): касаний A–B {len(cl)}, B–C {len(clBC)}, A–C {len(clAC)}")
print(f"   маршруты цепочки = {routes([RA, RB, RC], [AA, AB, AC], cl + clBC + clAC)}")
