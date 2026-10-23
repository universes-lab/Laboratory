"""Ось кольца (X по КВ: «X+ — кольцо направлено вверх») против направления прохождения в отверстии.

Для каждого цикла при обходе «вместе» (одинаковое направление прохождения в отверстиях, honc_ring_field) считается
вектор оси кольца n_i = сумма (r - C) x dr (ориентирован по обходу) и его проекция на ось цикла (вертикаль y).
Затем то же при обходе «встречно» (чередование). Для прямой открытой цепи — проекция на нормаль к плоскости цепи.
Вопрос: какому правилу обхода соответствует канонический принцип стыковки «X- <-> X+» (оси колец соседей противоположны).
Запуск: python3 ring_axes.py
"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
import docking as D

def axis(r, om):
    t = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
    P = r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])
    if om < 0: P = P[::-1]
    dP = np.roll(P, -1, 0) - P
    n = np.cross(P - r['C'], dP).sum(0); return n / np.linalg.norm(n)

y = np.array([0, 1.0, 0])
for name, N, beta in (("Z", 2, 0.0), ("W", 4, 0.0), ("W", 4, 25.0), ("глюон", 8, 30.0), ("глюон", 8, 65.0)):
    g = h.build(N, beta)
    om = [r['Om'] for r in g['rings']]
    tog = [axis(r, o) for r, o in zip(g['rings'], om)]
    alt = [axis(r, o * (-1) ** i) for i, (r, o) in enumerate(zip(g['rings'], om))]
    A = [np.array(a) for a in g['A']]
    rad = [((g['rings'][i]['C']) / (np.linalg.norm(g['rings'][i]['C']) + 1e-12)) for i in range(N)]
    print(f"{name} N={N} beta={beta}:")
    print("   «вместе»:  проекция оси кольца на вертикаль", [f"{n @ y:+.2f}" for n in tog], "; на радиус", [f"{n @ e:+.2f}" for n, e in zip(tog, rad)])
    print("   «встречно»: проекция оси кольца на вертикаль", [f"{n @ y:+.2f}" for n in alt], "; соседние оси: n_i·n_(i+1) =",
          [f"{alt[i] @ alt[(i + 1) % N]:+.2f}" for i in range(N)])
    print("   «вместе»:  соседние оси n_i·n_(i+1) =", [f"{tog[i] @ tog[(i + 1) % N]:+.2f}" for i in range(N)])

# прямая открытая цепь: оси соседних колец при одинаковом («вместе») и противоположном («встречно») направлении
# прохождения в общем отверстии
X = np.array([1.0, 0, 0])
def chain_axes(rule):
    A, T = np.zeros(3), np.array([0, 0, 1.0]); out = []; t_end = np.array([0, 0, 1.0])
    for k in range(3):
        lk = D.dock_link(A, T, X)
        t = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
        P = lk['C'] + np.outer(lk['p'] * np.cos(t), lk['u']) + np.outer(lk['q'] * np.sin(t), lk['W'])
        k0 = np.argmin(np.linalg.norm(P - A, axis=1)); tang = P[(k0 + 1) % len(P)] - P[k0]
        want = t_end if (k == 0 or rule == 'вместе') else -t_end      # направление в общем отверстии
        if tang @ want < 0: P = P[::-1]
        dP = np.roll(P, -1, 0) - P; n = np.cross(P - lk['C'], dP).sum(0); out.append(n / np.linalg.norm(n))
        k1 = np.argmin(np.linalg.norm(P - lk['A2'], axis=1)); t_end = P[(k1 + 1) % len(P)] - P[k1]; t_end /= np.linalg.norm(t_end)
        A, T = lk['A2'], lk['T2']
    return out
for rule in ('вместе', 'встречно'):
    ax = chain_axes(rule)
    print(f"прямая цепь, «{rule}»: оси колец", [np.round(n, 2).tolist() for n in ax])
