"""Этап А: глубина ловушек для момента «против поля» [мост при О-к+].

Ловушка — точечный минимум |B| (нуль). Барьер ухода — наименьший по направлениям максимум |B| на луче
из нуля до выхода из сборки (rho > 2,6 или |y| > 2,5). Это оценка перевала сверху: луч, а не оптимальный путь.
Лучи, задевающие кольца (|B| > 50), считаются закрытыми.
Запуск: python3 trap_depth.py
"""
import importlib.util, numpy as np, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)

def segs(beta, rule):
    g = h.build(8, beta)
    if rule == 'встречно':
        for i, r in enumerate(g['rings']): r['Om'] = r['Om'] * (-1) ** i
    return h.segments(g, 1500), g

def null_on_axis(S, y0):
    lo, hi = y0 - 0.05, y0 + 0.05
    f = lambda y: h.field(S, [[0, y, 0]])[0, 1]
    for _ in range(50):
        m = (lo + hi) / 2
        lo, hi = (lo, m) if f(lo) * f(m) <= 0 else (m, hi)
    return (lo + hi) / 2

rng = np.random.default_rng(3)
D = rng.normal(size=(1200, 3)); D /= np.linalg.norm(D, axis=1)[:, None]
s = np.linspace(0.02, 3.0, 150)
for beta, rule, y0 in ((65.0, 'вместе', 0.62), (65.0, 'встречно', 0.0), (61.56, 'вместе', 0.69), (63.49, 'встречно', 0.0)):
    S, g = segs(beta, rule)
    yn = null_on_axis(S, y0) if y0 else 0.0
    X0 = np.array([0, yn, 0.0])
    P = X0[None, None, :] + s[None, :, None] * D[:, None, :]
    rho = np.hypot(P[..., 0], P[..., 2]); out = (rho > 2.6) | (np.abs(P[..., 1]) > 2.5)
    M = np.linalg.norm(h.field(S, P.reshape(-1, 3)), axis=1).reshape(len(D), len(s))
    bar = []
    for k in range(len(D)):
        idx = np.argmax(out[k]) if out[k].any() else len(s)
        prof = M[k, :idx]
        if prof.size == 0 or prof.max() > 50: continue
        bar.append((prof.max(), D[k], s[np.argmax(prof)]))
    bar.sort(key=lambda t: t[0])
    b, d, sm = bar[0]
    Xp = X0 + sm * d
    print(f"beta={beta} «{rule}»: нуль на y={yn:+.3f}; открытых лучей {len(bar)} из {len(D)}; наименьший барьер |B| = {b:.3f} "
          f"в точке (rho={np.hypot(Xp[0], Xp[2]):.2f}, y={Xp[1]:+.2f}); направление: {'вдоль оси' if abs(d[1]) > 0.9 else 'поперёк/наклонно'} (d_y={d[1]:+.2f})")
    for q in (0.1, 0.5):
        print(f"      квантиль {q}: барьер {np.quantile([t[0] for t in bar], q):.3f}")
