"""Проверка на «доказывает слишком много»: если одиночный E4 рвёт любую связь «кольцо через тор», то в замкнутых Z/W/глюоне
чередование (E3 [Д]: P = 2) возможно лишь при совместном E4 всех звеньев. Сохраняет ли совместный жёсткий E4 связи в замкнутом кольце?
Геометрия ЛМ1 build(8, β). Латчер i = тор i + кольцо i (кольцо i продето через торы i и i+1).
Все латчеры одновременно поворачиваются на 180° вокруг своих осей u_i(φ) ⟂ d_i через середину d_i; φ — у чётных φe, у нечётных φo
(локальный базис: e1 = проекция оси y на плоскость ⟂ d_i, e2 = d_i × e1). Считаем Lk нового кольца с новыми средними окружностями
соседей и наименьшее расстояние до их каспов.
Запуск: python3 e4_collective.py"""
import numpy as np, importlib.util, itertools
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
def Lk(P, Q):
    dP = np.roll(P, -1, 0) - P; dQ = np.roll(Q, -1, 0) - Q; mP = P + dP / 2; mQ = Q + dQ / 2
    R = mP[:, None] - mQ[None]; num = np.einsum('ijk,ijk->ij', R, np.cross(dP[:, None], dQ[None]))
    return (num / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)
def Rot(a, ang=np.pi):
    a = np.asarray(a, float) / np.linalg.norm(a); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
def circle(c, e1, e2, r, n):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False); return c + r * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))
def perp(v):
    v = v / np.linalg.norm(v); a = np.array([1.0, 0, 0]) if abs(v[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(v, a); e1 /= np.linalg.norm(e1); return e1, np.cross(v, e1)
N, n = 8, 500; Yh = np.array([0, 1.0, 0])
for b in (0.0, 71.30):
    g = h.build(N, b); A = [np.array(x) for x in g['A']]; T = [np.array(x) / np.linalg.norm(x) for x in g['T']]
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    rings = [r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W']) for r in g['rings']]
    cores = [circle(A[i], *perp(T[i]), 0.5, n) for i in range(N)]
    L0 = [[Lk(rings[i], cores[j]) for j in ((i - 1) % N, i, (i + 1) % N)] for i in (0, 1)]
    print(f"β = {b:5.2f}°: до доворота Lk(кольцо i; торы i−1, i, i+1): чётное {np.round(L0[0], 3)}, нечётное {np.round(L0[1], 3)}")
    frames = []
    for i in range(N):
        d = g['rings'][i]['C'] - A[i]; dh = d / np.linalg.norm(d); e1 = Yh - (Yh @ dh) * dh
        e1 = e1 / np.linalg.norm(e1) if np.linalg.norm(e1) > 1e-9 else perp(dh)[0]; frames.append(((g['rings'][i]['C'] + A[i]) / 2, e1, np.cross(dh, e1)))
    best = []
    PH = np.arange(0, 180, 15)
    for pe, po in itertools.product(PH, PH):
        R2, C2, A2 = [], [], []
        for i in range(N):
            M, e1, e2 = frames[i]; ph = np.radians(pe if i % 2 == 0 else po); Rm = Rot(np.cos(ph) * e1 + np.sin(ph) * e2)
            R2.append((rings[i] - M) @ Rm.T + M); C2.append((cores[i] - M) @ Rm.T + M); A2.append((A[i] - M) @ Rm.T + M)
        rec = []
        for i in (0, 1):
            for j in ((i - 1) % N, i, (i + 1) % N):
                rec.append((round(Lk(R2[i], C2[j])), np.min(np.linalg.norm(R2[i] - A2[j], axis=1))))
        links = [abs(x[0]) for x in rec]
        best.append((sum(links), pe, po, links, [round(float(x[1]), 3) for x in rec]))
    best.sort(key=lambda x: -x[0])
    print(f"  совместный E4, {len(PH)}×{len(PH)} пар (φe, φo): наибольшее число сохранённых зацеплений из 6 (кольца 0 и 1 с торами i−1, i, i+1): {best[0][0]}")
    for s, pe, po, links, dist in best[:3]:
        print(f"    φe = {pe:3.0f}°, φo = {po:3.0f}°: |Lk| = {links}; расстояние до каспов {dist}")
    cnt = {}
    for x in best: cnt[x[0]] = cnt.get(x[0], 0) + 1
    print(f"  распределение числа сохранённых зацеплений: {dict(sorted(cnt.items()))}")
    nxt = sum(1 for x in best if x[3][2] or x[3][5]); own = sum(1 for x in best if x[3][1] and x[3][4])
    print(f"  прямое продевание через тот же соседний тор (i+1) сохранилось хотя бы у одного кольца: {nxt} из {len(best)}; свой тор у обоих колец: {own} из {len(best)}")
