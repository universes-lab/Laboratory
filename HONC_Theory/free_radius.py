"""Условие размера: свободный радиус на оси глюона — расстояние от точки оси до ближайшего тора или кольца (ЛМ1).
Квантрон радиуса r с центром в этой точке помещается, если r ≤ свободного радиуса. Запуск: python3 free_radius.py"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
import docking as D
def free_r(beta, y):
    g = h.build(8, beta); X = np.array([0, y, 0.0])
    dr = min(np.linalg.norm(D.ring_points(r['C'], r['u'], r['W'], r['p'], r['q'], 4000) - X, axis=1).min() for r in g['rings'])
    dt = min(np.linalg.norm(D.torus_surface(np.array(A), np.array(T) / np.linalg.norm(T), 200) - X, axis=1).min() for A, T in zip(g['A'], g['T']))
    return min(dr, dt), dr, dt
for beta in (61.56, 63.49, 65.0, 66.54):
    row = []
    for y in (0.0, 0.3, 0.6, 0.623, 0.73, 1.0, 1.12):
        f, dr, dt = free_r(beta, y); row.append(f"y={y:.3f}: {f:.3f}")
    print(f"beta={beta}: " + "; ".join(row))
