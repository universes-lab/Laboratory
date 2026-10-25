"""Пункт 3 (передача заморозки по ветви) с обращённым продеванием. Пара соседей ЛМ1 build(8, β): латчер i = (тор i, кольцо i),
кольцо i продето через тор i+1. Один из пары заморожен, другой делает E4 один (180° вокруг u(φ) ⟂ d через середину d).
Случай 1: доворачивается владелец кольца (i), заморожен тор-хозяин (i+1). Случай 2: доворачивается хозяин (i+1), заморожен i.
Для каждого: прямое продевание после E4 (то же кольцо через тот же тор), обращённое (кольцо другого через тор доворачивающегося или
новое кольцо доворачивающегося через тор замороженного) и расстояние средних окружностей торов пары (тела не пересекаются ⇔ ≥ 1).
Плюс справочно — параметры кольца для сверки δ с Гроком.
Запуск: python3 e4_branch.py"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
def Lk(P, Q):
    dP = np.roll(P, -1, 0) - P; dQ = np.roll(Q, -1, 0) - Q; mP = P + dP / 2; mQ = Q + dQ / 2
    R = mP[:, None] - mQ[None]; num = np.einsum('ijk,ijk->ij', R, np.cross(dP[:, None], dQ[None]))
    return (num / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)
def Rot(a, ang=np.pi):
    a = np.asarray(a, float) / np.linalg.norm(a); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
def circle(c, e1, e2, r, n=900):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False); return c + r * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))
def perp(v):
    v = v / np.linalg.norm(v); a = np.array([1.0, 0, 0]) if abs(v[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(v, a); e1 /= np.linalg.norm(e1); return e1, np.cross(v, e1)
dmin = lambda P, Q: np.min(np.linalg.norm(P[::2, None] - Q[None, ::2], axis=2))
PH = np.arange(0, 180, 10.0)
for b in (0.0, 63.49, 71.30):
    g = h.build(8, b); A = [np.array(x) for x in g['A']]; T = [np.array(x) / np.linalg.norm(x) for x in g['T']]; t = np.linspace(0, 2 * np.pi, 900, endpoint=False)
    R = [r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W']) for r in g['rings']]
    Cc = [circle(A[k], *perp(T[k]), 0.5) for k in range(8)]
    def flip(k, ph):
        d = g['rings'][k]['C'] - A[k]; M = (g['rings'][k]['C'] + A[k]) / 2; e1, e2 = perp(d)
        Rm = Rot(np.cos(np.radians(ph)) * e1 + np.sin(np.radians(ph)) * e2); f = lambda P: (P - M) @ Rm.T + M
        return f(R[k]), f(Cc[k])
    i, j = 0, 1
    s1 = np.array([(Lk(flip(i, ph)[0], Cc[j]), Lk(R[j], flip(i, ph)[1]), dmin(flip(i, ph)[1], Cc[j])) for ph in PH])
    s2 = np.array([(Lk(R[i], flip(j, ph)[1]), Lk(flip(j, ph)[0], Cc[i]), dmin(flip(j, ph)[1], Cc[i])) for ph in PH])
    rng = lambda v: f"[{v.min():+.3f}, {v.max():+.3f}]"
    print(f"β = {b:5.2f}°: до доворота Lk(кольцо i, тор i+1) = {Lk(R[i], Cc[j]):+.3f}; Lk(кольцо i+1, тор i) = {Lk(R[j], Cc[i]):+.3f}; средние окружности {dmin(Cc[i], Cc[j]):.3f}")
    print(f"   случай 1 (доворачивается владелец кольца): прямое Lk {rng(s1[:,0])}; обращённое {rng(s1[:,1])}; средние окружности {s1[:,2].min():.3f}…{s1[:,2].max():.3f}")
    print(f"   случай 2 (доворачивается хозяин-тор):       прямое Lk {rng(s2[:,0])}; обращённое {rng(s2[:,1])}; средние окружности {s2[:,2].min():.3f}…{s2[:,2].max():.3f}")
print("\nСверка δ с Гроком — параметры build(8, β), кольцо 1:")
for b in (66.54, 71.30):
    g = h.build(8, b); r = g['rings'][1]; dl = np.pi / 8; cosg = np.sin(np.radians(b)) * np.cos(dl); d = 2 * (0.5 * np.sqrt(1 - cosg ** 2) + 0.5)
    print(f"  β = {b:5.2f}°: cos γ = {cosg:.5f}; d (шаг торов) = {d:.5f}; c = {d/2:.5f}; p = {r['p']:.5f}; q = {r['q']:.5f}; "
          f"сдвиг центра y0 = {np.linalg.norm(r['C'] - (g['A'][1] + g['A'][2]) / 2 * 0) :.5f}")
