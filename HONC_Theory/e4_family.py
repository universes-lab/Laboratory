"""Правило 1, условие Хранителя (25.10): «заморозка ⇔ разрыв при всех допустимых осях E4».
E4: поворот Qf на 180° вокруг оси, перпендикулярной смещению d = C_кольца − C_тора, через середину d (кольцо и тор меняются сторонами).
Семейство осей: u(φ) ⟂ d, φ ∈ [0°, 180°).
Часть А — модель причала (mooring_step.py): тор Q1 рогатый, касп в 0, ось z, средняя окружность r = 1/2 в плоскости xy;
  кольцо латчера — окружность радиуса 1 в плоскости yz с центром (0, 1, 0) через касп Q1 и через касп своего тора (0, 2, 0), ось z (ЛМ1).
  Контраст: повороты вокруг осей через центр самого кольца (прежняя модель Дипсика) — не E4.
Часть Б — устойчивость к наклону: геометрия ЛМ1 build(8, β): латчер = тор 0 + кольцо 0, хозяин = тор 1 (касп A1, ось T1).
Часть В — пункт 3 (передача по ветви): латчер 0 заморожен, латчер 1 (тор 1 + кольцо 1) делает E4 один;
  считаем Lk(кольцо 0, средняя окружность повёрнутого тора 1).
Запуск: python3 e4_family.py"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
def Lk(P, Q):
    dP = np.roll(P, -1, 0) - P; dQ = np.roll(Q, -1, 0) - Q; mP = P + dP / 2; mQ = Q + dQ / 2
    R = mP[:, None] - mQ[None]; num = np.einsum('ijk,ijk->ij', R, np.cross(dP[:, None], dQ[None]))
    return (num / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)
def Rot(a, ang=np.pi):
    a = np.asarray(a, float) / np.linalg.norm(a); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
def circle(c, e1, e2, r, n=1500):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False); return c + r * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))
def perp_basis(d):
    d = d / np.linalg.norm(d); a = np.array([1.0, 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(d, a); e1 /= np.linalg.norm(e1); return e1, np.cross(d, e1)
def turn(P, Mid, u): return (P - Mid) @ Rot(u).T + Mid
mind = lambda P, Q: np.min(np.linalg.norm(P[::3, None] - Q[None, ::3], axis=2))
X, Y, Z = np.eye(3); PH = np.arange(0, 180, 7.5)

print("А. Модель причала (окружность радиуса 1, оси параллельны)")
core = circle(np.zeros(3), X, Y, 0.5); ring = circle(np.array([0, 1.0, 0]), -Y, Z, 1.0)
Cr, Ct = np.array([0, 1.0, 0]), np.array([0, 2.0, 0]); d = Cr - Ct; Mid = (Cr + Ct) / 2; e1, e2 = perp_basis(d)
L0 = Lk(ring, core); out = []
for ph in PH:
    u = np.cos(np.radians(ph)) * e1 + np.sin(np.radians(ph)) * e2; R2 = turn(ring, Mid, u)
    out.append((Lk(R2, core), np.min(np.linalg.norm(R2, axis=1)), mind(R2, core)))
out = np.array(out)
print(f"  до поворота Lk = {L0:+.3f}")
print(f"  E4, {len(PH)} осей φ = 0…172,5°: Lk ∈ [{out[:,0].min():+.4f}, {out[:,0].max():+.4f}]; "
      f"мин. расстояние нового кольца до каспа Q1 {out[:,1].min():.3f}; до средней окружности {out[:,2].min():.3f}")
print("  контраст — ось через центр самого кольца (не E4):")
for nm, u in (("ось y (диаметр через оба каспа)", Y), ("ось z", Z)):
    R2 = turn(ring, Cr, u); T2 = (Ct - Cr) @ Rot(u).T + Cr
    print(f"    {nm}: Lk {L0:+.3f} → {Lk(R2, core):+.3f}; центр тора латчера уходит в {np.round(T2, 3)}")

print("\nБ. Наклон: ЛМ1 build(8, β), латчер = тор 0 + кольцо 0, хозяин — тор 1")
for b in (0.0, 30.0, 50.0, 63.49, 71.30, 85.0):
    g = h.build(8, b); r = g['rings'][0]; A = [np.array(x) for x in g['A']]; T = [np.array(x) / np.linalg.norm(x) for x in g['T']]
    t = np.linspace(0, 2 * np.pi, 1500, endpoint=False); P = r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])
    f1, f2 = perp_basis(T[1]); core1 = circle(A[1], f1, f2, 0.5)
    d = r['C'] - A[0]; Mid = (r['C'] + A[0]) / 2; e1, e2 = perp_basis(d); res = []
    for ph in PH:
        u = np.cos(np.radians(ph)) * e1 + np.sin(np.radians(ph)) * e2; P2 = turn(P, Mid, u)
        res.append((Lk(P2, core1), np.min(np.linalg.norm(P2 - A[1], axis=1))))
    res = np.array(res)
    print(f"  β = {b:5.2f}°: до Lk = {Lk(P, core1):+.3f}; после E4 Lk ∈ [{res[:,0].min():+.4f}, {res[:,0].max():+.4f}]; "
          f"мин. расстояние до каспа хозяина {res[:,1].min():.3f} (средняя окружность хозяина — 0,5 от каспа)")

print("\nВ. Пункт 3: латчер 0 заморожен, латчер 1 делает E4 один (связь: кольцо 0 продето через тор 1)")
for b in (0.0, 63.49, 71.30):
    g = h.build(8, b); r0, r1 = g['rings'][0], g['rings'][1]; A = [np.array(x) for x in g['A']]; T = [np.array(x) / np.linalg.norm(x) for x in g['T']]
    t = np.linspace(0, 2 * np.pi, 1500, endpoint=False); P0 = r0['C'] + np.outer(r0['p'] * np.cos(t), r0['u']) + np.outer(r0['q'] * np.sin(t), r0['W'])
    f1, f2 = perp_basis(T[1]); core1 = circle(A[1], f1, f2, 0.5)
    d = r1['C'] - A[1]; Mid = (r1['C'] + A[1]) / 2; e1, e2 = perp_basis(d); res = []
    for ph in PH:
        u = np.cos(np.radians(ph)) * e1 + np.sin(np.radians(ph)) * e2; c2 = turn(core1, Mid, u); A2 = (A[1] - Mid) @ Rot(u).T + Mid
        res.append((Lk(P0, c2), np.min(np.linalg.norm(P0 - A2, axis=1))))
    res = np.array(res)
    print(f"  β = {b:5.2f}°: до Lk(кольцо 0, тор 1) = {Lk(P0, core1):+.3f}; после E4 латчера 1 Lk ∈ [{res[:,0].min():+.4f}, {res[:,0].max():+.4f}]; "
          f"мин. расстояние кольца 0 до нового каспа тора 1 {res[:,1].min():.3f}")
