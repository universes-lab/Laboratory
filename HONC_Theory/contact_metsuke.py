"""Поправка Мецуке к этапу Б (Интегратор, 24.10, 13:58).
(1) Касание при d = 2a — касание условных проводов. Предел a → 0: где сходятся сами 1D-контуры колец (общая точка носителей).
    D_c(a) по сетке точек колец; D0 — расстояние, при котором контуры A1 и B2 имеют общую точку (минимизация по параметрам эллипсов).
(2) Конструктивное разъединение: путь — поступательный отвод B вдоль общей оси от касания до полного разделения плоскостью.
    На сетке шага h проверяется зазор кольцо — кольцо, кольцо — тело тора, тело тора — тело тора (обе сборки).
    Расстояние между жёсткими множествами при сдвиге меняется не быстрее сдвига, поэтому зазор > h/2 + ошибка дискретизации
    в узлах сетки означает: на всём пути пересечений нет. φ = 45°, β = 65°. Запуск: python3 contact_metsuke.py"""
import numpy as np, io, contextlib, importlib.util, os, sys
from scipy.spatial import cKDTree
from scipy.optimize import minimize
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
import docking as D
y = np.array([0, 1.0, 0])
def Rot(axis, ang):
    axis = np.asarray(axis, float); axis /= np.linalg.norm(axis)
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
g = h.build(8, 65.0); M = Rot(y, np.pi / 4)
def ring_fun(r, Mx=np.eye(3), sh=np.zeros(3)):
    return lambda t: (r['C'] + r['p'] * np.cos(t) * r['u'] + r['q'] * np.sin(t) * r['W']) @ Mx.T + sh
def ring_pts(r, n, Mx=np.eye(3), sh=np.zeros(3)):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False); return (r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])) @ Mx.T + sh
NP = 6000
RA = [ring_pts(r, NP) for r in g['rings']]; tA = cKDTree(np.vstack(RA))
def gmin(Dd): return tA.query(np.vstack([ring_pts(r, NP, M, Dd * y) for r in g['rings']]))[0].min()
print("(1) Касание проводов толщины a и предел a → 0")
for a in (0.015, 0.0075, 0.003, 0.001):
    lo, hi = 2.20, 2.30
    for _ in range(40):
        m = (lo + hi) / 2; lo, hi = (lo, m) if gmin(m) >= 2 * a else (m, hi)
    print(f"   a = {a}: D_c = {hi:.5f}", flush=True)
rA, rB = g['rings'][1], g['rings'][2]; fA = ring_fun(rA)
def dmin_cont(Dd):
    fB = ring_fun(rB, M, Dd * y)
    PA = ring_pts(rA, 4000); PB = ring_pts(rB, 4000, M, Dd * y); dd, j = cKDTree(PB).query(PA); i = int(np.argmin(dd))
    t0, s0 = 2 * np.pi * i / 4000, 2 * np.pi * j[i] / 4000
    res = minimize(lambda v: np.sum((fA(v[0]) - fB(v[1])) ** 2), [t0, s0], method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-20, maxiter=4000))
    return np.sqrt(res.fun), fA(res.x[0])
Ds = np.linspace(2.236, 2.254, 37); dd = np.array([dmin_cont(x)[0] for x in Ds]); k = int(np.argmin(dd))
lo, hi = Ds[max(k - 1, 0)], Ds[min(k + 1, len(Ds) - 1)]
for _ in range(60):
    m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
    if dmin_cont(m1)[0] < dmin_cont(m2)[0]: hi = m2
    else: lo = m1
D0 = (lo + hi) / 2; d0, X0 = dmin_cont(D0)
ymax = max(ring_pts(r, 20000)[:, 1].max() for r in g['rings'])
print(f"   контуры A1 и B2 (1D, без толщины): наименьшее расстояние {d0:.2e} при D0 = {D0:.5f}; точка ρ = {np.hypot(X0[0], X0[2]):.4f}, y = {X0[1]:.4f}; 2·y_max = {2 * ymax:.5f}")
print("   d(D) около D0: " + ", ".join(f"{x:.4f}:{dmin_cont(x)[0]:.4f}" for x in (D0 - 0.004, D0 - 0.002, D0, D0 + 0.002, D0 + 0.004)))
print("\n(2) Конструктивное разъединение: отвод B вдоль оси")
TS = [(np.array(A), np.array(T) / np.linalg.norm(T)) for A, T in zip(g['A'], g['T'])]
SA = [D.torus_surface(A, T, 120) for A, T in TS]
def tube_sd(X, A, T):   # знаковое расстояние до трубки рогатого тора (a = b = 1/2): > 0 снаружи
    v = X - A; z = v @ T; rho = np.linalg.norm(v - np.outer(z, T), axis=1); return np.sqrt((rho - 0.5) ** 2 + z ** 2) - 0.5
allA = np.vstack(RA + SA); Y = np.abs(allA[:, 1]).max()
print(f"   протяжённость сборки по оси |y| ≤ {Y:.3f}: при D > {2 * Y:.3f} сборки разделены плоскостью")
seg = 2 * np.pi * 1.2 / NP; hstep = 0.004
worst = (9, None)
for Dd in np.arange(D0 + 1e-4, 2 * Y + 0.05, hstep):
    RB = [ring_pts(r, 1500, M, Dd * y) for r in g['rings']]; SB = [S @ M.T + Dd * y for S in SA]
    TB = [(M @ A + Dd * y, M @ T) for A, T in TS]
    rr = tA.query(np.vstack(RB))[0].min()
    rt = min(min(tube_sd(np.vstack(RB), A, T).min() for A, T in TS), min(tube_sd(np.vstack(RA[::1])[::4], A, T).min() for A, T in TB))
    tt = min(tube_sd(np.vstack(SB), A, T).min() for A, T in TS)
    c = min(rr, rt, tt)
    if c < worst[0]: worst = (c, Dd, rr, rt, tt)
print(f"   шаг {hstep}; наименьший зазор на пути {worst[0]:.4f} при D = {worst[1]:.4f} (кольцо—кольцо {worst[2]:.4f}, кольцо—тор {worst[3]:.4f}, тор—тор {worst[4]:.4f})")
print(f"   условие: зазор > h/2 + ошибка дискретизации ≈ {hstep / 2 + 0.01:.4f} — " + ("выполнено" if worst[0] > hstep / 2 + 0.01 else "НЕ выполнено у самого начала пути — см. ниже"))
for Dd in (D0 + 0.001, D0 + 0.005, D0 + 0.02, 2.2749):
    RB = [ring_pts(r, 1500, M, Dd * y) for r in g['rings']]; TB = [(M @ A + Dd * y, M @ T) for A, T in TS]
    rr = tA.query(np.vstack(RB))[0].min()
    rt = min(min(tube_sd(np.vstack(RB), A, T).min() for A, T in TS), min(tube_sd(np.vstack(RA)[::4], A, T).min() for A, T in TB))
    print(f"   D = {Dd:.4f}: кольцо—кольцо {rr:.4f}, кольцо—тор {rt:.4f}")
