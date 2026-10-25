"""Доля пути δ(β) между каспами по ходу обхода (длинная дуга) у кольца глюона N = 8 — для И-5: меняет ли груз (упор квантрона
при 66,54° против касания колец пустой сборки при 71,30°) период бега состояния T ∝ N·δ·2π/v (работа о защёлке, Δt = δ·ℓ/v).
Запуск: python3 delta_beta.py"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
def delta(beta, n=40000):
    g = h.build(8, beta); r = g['rings'][1]; t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    P = r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])
    if r['Om'] < 0: P = P[::-1]
    sl = np.r_[0, np.cumsum(np.linalg.norm(np.roll(P, -1, 0) - P, axis=1))]
    A = [np.array(x) for x in g['A']]; d = [np.linalg.norm(P - a, axis=1) for a in A]
    k = np.argsort([x.min() for x in d])[:2]; i0, i1 = int(np.argmin(d[k[0]])), int(np.argmin(d[k[1]]))
    f = ((sl[i1] - sl[i0]) % sl[-1]) / sl[-1]; return max(f, 1 - f)
for b in (63.49, 65.0, 66.54, 71.30):
    print(f"β = {b:6.2f}°: δ = {delta(b):.4f}")
d1, d2 = delta(66.54), delta(71.30)
print(f"отношение периодов гружёной (упор 66,54°) и пустой (71,30°) сборки: {d1 / d2:.4f} (разница {100 * (d1 / d2 - 1):+.2f}%)")
