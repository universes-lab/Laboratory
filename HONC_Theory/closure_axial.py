"""Этап А, режим «замыкание» (переходное сопряжение [Г], мост при О-к+): движение квантрона вдоль оси глюона,
пока кольцо затягивается (β: 5° → 65°).

Точные опоры:
  - на оси поле чисто осевое при любом β (поворот на два звена) [Д, свод п. 4.5] —
    поэтому момент на оси прецессирует вокруг y и его осевая составляющая s_y сохраняется;
  - сфера — точный диполь в центре: сила вдоль оси F_y = m s_y db/dy, b(y, β) — осевой профиль B_y.
Канал: квантрон радиуса 1 помещается, пока свободный радиус на оси ≥ 1 (геометрия ЛМ1, free_radius.py).
Пока канал открыт до |y| = 1,4, уход по оси возможен. Радиальный уход до замыкания камеры (61,56°) не учтён.
Безразмерно: y'' = s_y · db/dy(y, β(τ)), время в единицах осевого движения; длительность замыкания Θ.
Запуск: python3 closure_axial.py
"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
import docking as D
from scipy.interpolate import RectBivariateSpline

betas = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 58, 60, 61.56, 62.5, 63.49, 64.25, 65.0]); ys = np.linspace(-1.4, 1.4, 141)
def segs(beta, rule):
    g = h.build(8, beta)
    if rule == 'встречно':
        for i, r in enumerate(g['rings']): r['Om'] = r['Om'] * (-1) ** i
    return h.segments(g, 1200), g
prof, walls = {}, []
for rule in ('вместе', 'встречно'):
    Bgrid = np.array([h.field(segs(b, rule)[0], np.stack([0 * ys, ys, 0 * ys], 1))[:, 1] for b in betas])
    prof[rule] = RectBivariateSpline(betas, ys, Bgrid)
for b in betas:                                      # граница канала: первая точка |y|, где свободный радиус < 1
    g = h.build(8, b); rings = [D.ring_points(r['C'], r['u'], r['W'], r['p'], r['q'], 2000) for r in g['rings']]
    tori = [D.torus_surface(np.array(A), np.array(T) / np.linalg.norm(T), 120) for A, T in zip(g['A'], g['T'])]
    yw = 1.4
    for yv in np.arange(0, 1.41, 0.02):
        X = np.array([0, yv, 0.0])
        f = min(min(np.linalg.norm(R - X, axis=1).min() for R in rings), min(np.linalg.norm(S - X, axis=1).min() for S in tori))
        if f < 1.0:
            yw = yv; break
    walls.append(yw)
walls = np.array(walls)
print("граница канала |y| для квантрона радиуса 1:", dict(zip(betas.astype(int).tolist(), np.round(walls, 2).tolist())), "(1,4 — открыт)")

rng = np.random.default_rng(5); N = 400; sy = rng.uniform(-1, 1, N); y0 = rng.normal(0, 0.02, N)   # квантрон не точно в центре
for rule in ('вместе', 'встречно'):
    print(f"\n«{rule}»: b(0) при 65° = {prof[rule](65, 0)[0,0]:+.3f}")
    for Theta in (1.0, 3.0, 10.0, 30.0, 100.0):
        dt = min(0.01, Theta / 400); nst = int(Theta / dt)
        y = y0.copy(); v = np.zeros(N); gone = np.zeros(N, bool)
        for k in range(nst):
            bt = 5 + 60 * k / nst
            yw = np.interp(bt, betas, walls)
            a = sy * prof[rule](bt, y, dy=1, grid=False)
            v += a * dt; y += v * dt
            out = np.abs(y) >= 1.39
            if yw >= 1.39:
                gone |= out
            hit = (np.abs(y) > yw) & ~gone
            y[hit] = np.sign(y[hit]) * yw; v[hit] = 0.0     # неупругий упор в горловину
            y[gone] = np.sign(y[gone]) * 1.4; v[gone] = 0
        keep = ~gone
        b0 = prof[rule](65, 0)[0, 0]
        at_c = keep & (np.abs(y) < 0.3); at_w = keep & (np.abs(y) >= 0.3)
        sgn = np.sign(b0) if abs(b0) > 1e-6 else 1.0
        print(f"   Θ={Theta:5.0f}: ушли {gone.mean():.2f}; остались у центра {at_c.mean():.2f} (средний s_y·sign b(0) = "
              f"{(sy[at_c] * sgn).mean() if at_c.any() else float('nan'):+.2f}); у горловин {at_w.mean():.2f} "
              f"(у y>0: средний s_y {sy[at_w & (y > 0)].mean() if (at_w & (y > 0)).any() else float('nan'):+.2f}; "
              f"у y<0: {sy[at_w & (y < 0)].mean() if (at_w & (y < 0)).any() else float('nan'):+.2f})")
