"""Может ли квантрон радиуса 1 уйти из центра глюона не по оси, а вбок (до и после замыкания камеры)?
Для лучей из центра — «узкое место»: наименьший свободный радиус вдоль луча до выхода из сборки (ρ > 3 или |y| > 1,6).
Если наибольшее узкое место по всем лучам < 1, боковой уход для квантрона радиуса 1 закрыт. Запуск: python3 escape_geom.py"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
import docking as D
rng = np.random.default_rng(1)
dirs = rng.normal(size=(160, 3)); dirs[:, 1] = np.abs(dirs[:, 1]) * 0.6; dirs /= np.linalg.norm(dirs, axis=1)[:, None]
dirs = np.vstack([dirs, [[1, 0, 0], [np.cos(np.pi / 8), 0, np.sin(np.pi / 8)], [0, 1, 0]]])
s = np.linspace(0, 3.2, 65)
for beta in (20, 40, 55, 60, 61.56, 65):
    g = h.build(8, beta)
    obst = np.vstack([D.ring_points(r['C'], r['u'], r['W'], r['p'], r['q'], 1500) for r in g['rings']] +
                     [D.torus_surface(np.array(A), np.array(T) / np.linalg.norm(T), 90) for A, T in zip(g['A'], g['T'])])
    best = (0, None)
    for d in dirs:
        P = s[:, None] * d[None, :]
        P = P[(np.hypot(P[:, 0], P[:, 2]) <= 3.0) & (np.abs(P[:, 1]) <= 1.6)]
        fr = np.array([np.linalg.norm(obst - p, axis=1).min() for p in P])
        if fr.min() > best[0]:
            best = (fr.min(), d)
    d = best[1]
    print(f"beta={beta}: наибольшее узкое место по лучам = {best[0]:.3f} (направление: подъём {np.degrees(np.arcsin(abs(d[1]))):.0f}° над плоскостью кольца)"
          f" — {'боковой уход ОТКРЫТ' if best[0] >= 1 else 'боковой уход закрыт'} для радиуса 1")
