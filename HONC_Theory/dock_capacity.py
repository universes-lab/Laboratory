"""Вместимость причала: сколько звеньев короткой цепочки можно причалить одновременно.

Берёт свободные направления из docking.py (сетка 10°) и жадно (с многими случайными порядками) набирает
совместимые причалы:
  - к одному тору-хозяину (остальные торы без причалов);
  - ко всем торам сразу по одному узору (образы узора по симметрии сборки).
Совместимость двух причалов: причальные торы не пересекаются и не совпадают; кольцо каждого проходит вне
причального тора другого. Это нижняя оценка максимума (жадный поиск), не доказательство верхней границы.

Запуск: python3 dock_capacity.py N beta [quantron]
"""
import numpy as np, sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import docking as D

N = int(sys.argv[1]); beta = float(sys.argv[2]); quantron = 'quantron' in sys.argv
g, tori, rings = D.assembly(N, beta)
T, eo, et = D.frame(0, tori)
TOL = D.TOL


def Ry(th):
    c, s = np.cos(th), np.sin(th)
    return np.array([[c, 0, -s], [0, 1, 0], [s, 0, c]])


REF = np.diag([1.0, -1.0, 1.0])
def M(i):
    step = 2 * np.pi / N
    m = Ry(i * step)
    return m @ REF if (i % 2 and N > 2) else m


# проверка симметрии: образ тора 0 — тор i
for i in range(N):
    A0, T0 = tori[0]; Ai, Ti = tori[i]
    assert np.linalg.norm(M(i) @ A0 - Ai) < 1e-9 and abs(abs((M(i) @ T0) @ Ti) - 1) < 1e-9, i


def make(al, ps):
    ar, pr = np.radians(al), np.radians(ps)
    uh = np.cos(ar) * T + np.sin(ar) * (np.cos(pr) * eo + np.sin(pr) * et)
    L = D.dock_link(tori[0][0], T, uh)
    if L is None:
        return None
    ok, why, _ = D.check(L, 0, tori, rings, quantron)
    if not ok:
        return None
    R = D.ring_points(L['C'], L['u'], L['W'], L['p'], L['q'], 300)
    return dict(A2=L['A2'], T2=L['T2'], R=R, S=D.torus_surface(L['A2'], L['T2'], 30), al=al, ps=ps)


def image(dk, i):
    m = M(i)
    return dict(A2=m @ dk['A2'], T2=m @ dk['T2'], R=dk['R'] @ m.T, S=dk['S'] @ m.T, al=dk['al'], ps=dk['ps'], host=i)


def compatible(x, y):
    if np.linalg.norm(x['A2'] - y['A2']) < 0.05:
        return False
    if D.memb(x['S'], y['A2'], y['T2']).min() < 1 - TOL or D.memb(y['S'], x['A2'], x['T2']).min() < 1 - TOL:
        return False
    if D.memb(x['R'], y['A2'], y['T2']).min() < 1 - TOL or D.memb(y['R'], x['A2'], x['T2']).min() < 1 - TOL:
        return False
    return True


def also_free_vs_assembly(dk):
    """Образ на другом хозяине обязан проходить те же проверки против сборки (по симметрии — проходит)."""
    return True


cands = [c for c in (make(al, ps) for al in range(10, 180, 10) for ps in range(0, 360, 10)) if c]
print(f"N={N} beta={beta} quantron={quantron}: свободных направлений (сетка 10°): {len(cands)}")
rng = np.random.default_rng(1)

# 1) один хозяин
best1 = []
for trial in range(60):
    order = rng.permutation(len(cands)); chosen = []
    for k in order:
        c = cands[k]
        if all(compatible(c, x) for x in chosen):
            chosen.append(c)
    if len(chosen) > len(best1):
        best1 = chosen
print(f"   один хозяин: не меньше {len(best1)} причалов одновременно; направления (alpha, psi):",
      [(int(c['al']), int(c['ps'])) for c in best1])

# 2) все хозяева по одному узору
best = []
for trial in range(40):
    order = rng.permutation(len(cands)); chosen = []; allimgs = []
    for k in order:
        c = cands[k]
        imgs = [image(c, i) for i in range(N)]
        okself = all(compatible(imgs[i], imgs[j]) for i in range(N) for j in range(i + 1, N))
        if okself and all(compatible(u, v) for u in imgs for v in allimgs):
            chosen.append(c); allimgs += imgs
    if len(chosen) > len(best):
        best = chosen
print(f"   все {N} торов по одному узору: не меньше {len(best)} на тор (всего {len(best) * N}); направления:",
      [(int(c['al']), int(c['ps'])) for c in best])
