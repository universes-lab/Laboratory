"""Проверка В (пространство): навесы на прямой цепи — «гребёнка» (одна сторона) против чередования сторон (1)(−1).

Цепь: прямая по ЛМ1 вдоль x (оси торов вдоль z), 6 торов. Навес — звено по ЛМ1, причаленное к тору k хордой
m = cos(alpha) z + sin(alpha) (cos(psi) x + sin(psi) y); сторона (1) — psi в (0, 180), (−1) — psi в (180, 360).
Навесы на торах 1–4. Гребёнка: у всех (alpha, psi); чередование: (alpha, psi), (alpha, −psi), ...
Проверка: торы и кольца навесов против торов и колец цепи и друг друга (функция принадлежности, как в docking.py).
Только пространство: знаки и фазы не участвуют.
Запуск: python3 moorings.py
"""
import numpy as np, sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import docking as D
TOL = D.TOL
X = np.array([1.0, 0, 0]); Y = np.array([0, 1.0, 0]); Zv = np.array([0, 0, 1.0])

chain = []; A, T = np.zeros(3), Zv
chain.append(dict(A=A, T=T, S=D.torus_surface(A, T, 30), R=None))
for k in range(5):
    lk = D.dock_link(A, T, X)
    R = D.ring_points(lk['C'], lk['u'], lk['W'], lk['p'], lk['q'], 400)
    chain[-1]['R'] = R
    A, T = lk['A2'], lk['T2']
    chain.append(dict(A=A, T=T, S=D.torus_surface(A, T, 30), R=None))
rings = [c['R'] for c in chain if c['R'] is not None]


def mooring(k, al, ps):
    A, T = chain[k]['A'], chain[k]['T']
    ar, pr = np.radians(al), np.radians(ps)
    m = np.cos(ar) * T + np.sin(ar) * (np.cos(pr) * X + np.sin(pr) * Y)
    lk = D.dock_link(A, T, m)
    if lk is None or lk['Rcurv'] < D.a - 1e-6:
        return None
    return dict(k=k, A=lk['A2'], T=lk['T2'], S=D.torus_surface(lk['A2'], lk['T2'], 30),
                R=D.ring_points(lk['C'], lk['u'], lk['W'], lk['p'], lk['q'], 400))


def ok_vs_chain(mo):
    for j, c in enumerate(chain):
        if np.linalg.norm(mo['A'] - c['A']) < 0.05:
            return False
        if j != mo['k'] and (D.memb(mo['S'], c['A'], c['T']).min() < 1 - TOL or D.memb(c['S'], mo['A'], mo['T']).min() < 1 - TOL):
            return False
        if D.memb(mo['R'], c['A'], c['T']).min() < 1 - TOL:
            return False
    return all(D.memb(r, mo['A'], mo['T']).min() >= 1 - TOL for r in rings)


def ok_pair(m1, m2):
    if np.linalg.norm(m1['A'] - m2['A']) < 0.05:
        return False
    if D.memb(m1['S'], m2['A'], m2['T']).min() < 1 - TOL or D.memb(m2['S'], m1['A'], m1['T']).min() < 1 - TOL:
        return False
    return D.memb(m1['R'], m2['A'], m2['T']).min() >= 1 - TOL and D.memb(m2['R'], m1['A'], m1['T']).min() >= 1 - TOL


res = {'гребёнка': [], 'чередование': []}
single = 0
for al in range(15, 170, 15):
    for ps in range(15, 180, 15):
        ms = {k: mooring(k, al, ps) for k in range(1, 5)}
        mm = {k: mooring(k, al, -ps) for k in range(1, 5)}
        if any(v is None for v in list(ms.values()) + list(mm.values())):
            continue
        if not (ok_vs_chain(ms[2]) and ok_vs_chain(mm[3])):
            continue
        single += 1
        comb = [ms[k] for k in range(1, 5)]
        alt = [ms[k] if k % 2 else mm[k] for k in range(1, 5)]
        for name, L in (('гребёнка', comb), ('чередование', alt)):
            if all(ok_vs_chain(m) for m in L) and all(ok_pair(L[i], L[i + 1]) for i in range(3)) and all(ok_pair(L[i], L[i + 2]) for i in range(2)):
                res[name].append((al, ps))
print(f"направлений, допустимых для одиночного навеса: {single}")
for name, v in res.items():
    print(f"{name}: допустимо {len(v)}; примеры: {v[:8]}")
