"""Проверка δ(β) к замечанию Грока (25.10): сходимость по сетке, все кольца, монотонность по β, расстояние кольца до центров торов.
Запуск: python3 delta_check.py"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
def delta(beta, ring=1, n=40000):
    g = h.build(8, beta); r = g['rings'][ring]; t = np.linspace(0, 2*np.pi, n, endpoint=False)
    P = r['C'] + np.outer(r['p']*np.cos(t), r['u']) + np.outer(r['q']*np.sin(t), r['W'])
    sl = np.r_[0, np.cumsum(np.linalg.norm(np.roll(P, -1, 0) - P, axis=1))]
    A = [np.array(x) for x in g['A']]
    ia, ib = ring % 8, (ring + 1) % 8
    da, db = np.linalg.norm(P - A[ia], axis=1), np.linalg.norm(P - A[ib], axis=1)
    i0, i1 = int(np.argmin(da)), int(np.argmin(db))
    f = ((sl[i1] - sl[i0]) % sl[-1]) / sl[-1]
    return max(f, 1 - f), da.min(), db.min(), sl[-1]
for b in (66.54, 71.30):
    for n in (4000, 40000, 400000):
        d, ea, eb, L = delta(b, 1, n); print(f"β = {b:5.2f}°, n = {n:6d}: δ = {d:.5f}; до центров торов {ea:.1e}, {eb:.1e}; длина {L:.5f}")
    print("   по всем кольцам:", " ".join(f"{delta(b, k)[0]:.4f}" for k in range(8)))
print("δ(β), n = 40000:")
for b in (55, 60, 63.49, 65, 66.54, 68, 70, 71.30, 73, 75, 80):
    print(f"  {b:6.2f}° → {delta(b)[0]:.4f}")
