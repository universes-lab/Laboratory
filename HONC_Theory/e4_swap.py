"""Правило 1, вторая сторона пары. E4 буквально: «кольцо и тор меняются сторонами». Для пары (Q1, латчер L0) отношение F1 может
сохраниться с обратным продеванием: после E4 латчера уже не кольцо L0 продето через тор Q1, а кольцо Q1 — через тор L0.
Модель причала (mooring_step.py): тор Q1 рогатый, касп 0, ось z; L0: кольцо — окружность радиуса 1 в плоскости yz с центром (0, 1, 0),
тор — касп (0, 2, 0), ось z. E4 латчера: поворот на 180° вокруг u(φ) ⟂ y через (0, 1,5, 0); новый тор L0: касп (0, 1, 0), ось a(φ).
Кольцо Q1: Qs — экватор (радиус 1, плоскость xy); меридиональное — плоскость (cos α·y + sin α·x, z), α — угол к плоскости причала.
Считаем Lk(кольцо Q1, новая средняя окружность L0), расстояние кольца Q1 до нового каспа и угол между кольцом и новой осью в ближайшей точке.
Справочно — сближение тел: расстояние центров торов до и после (контакт ЛМ1 — 2) и то же для совместного E4 в замкнутой build(8, β).
Запуск: python3 e4_swap.py"""
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
def perp(v):
    v = v / np.linalg.norm(v); a = np.array([1.0, 0, 0]) if abs(v[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(v, a); e1 /= np.linalg.norm(e1); return e1, np.cross(v, e1)
X, Y, Z = np.eye(3); Mid = np.array([0, 1.5, 0]); Tn = np.array([0, 1.0, 0])
rings = {"Qs (экватор)": circle(np.zeros(3), X, Y, 1.0)}
for al in (30, 60, 90, 120, 150):
    e1 = np.cos(np.radians(al)) * Y + np.sin(np.radians(al)) * X; rings[f"меридиональное α = {al}°"] = circle(np.zeros(3), e1, Z, 1.0)
PH = np.arange(0, 180, 5.0)
old_core = circle(np.array([0, 2.0, 0]), X, Y, 0.5)
for nm, R in rings.items():
    rows = []
    for ph in PH:
        u = np.cos(np.radians(ph)) * X + np.sin(np.radians(ph)) * Z; a = Rot(u) @ Z; c = circle(Tn, *perp(a), 0.5)
        dist = np.linalg.norm(R - Tn, axis=1); k = int(np.argmin(dist)); tv = np.roll(R, -1, 0)[k] - R[k]; tv /= np.linalg.norm(tv)
        rows.append((ph, Lk(R, c), dist[k], np.degrees(np.arccos(min(1, abs(tv @ a))))))
    rows = np.array(rows); lk = np.round(rows[:, 1]).astype(int)
    keep = PH[lk != 0]
    print(f"{nm}: до E4 Lk(кольцо Q1, тор L0) = {Lk(R, old_core):+.3f}; после E4 |Lk| = 1 при φ ∈ "
          f"{'∅' if len(keep) == 0 else f'[{keep.min():.0f}°…{keep.max():.0f}°] ({len(keep)} из {len(PH)})'}; "
          f"расстояние до нового каспа {rows[0,2]:.3f}; угол кольцо/ось в каспе: мин {rows[:,3].min():.1f}° при φ = {PH[np.argmin(rows[:,3])]:.0f}°")
print("\nСближение тел (расстояние центров торов; контакт ЛМ1 при параллельных осях — 2):")
print(f"  причал: до E4 |C(Q1) − C(L0)| = 2,000; после E4 — 1,000 при любом φ (новый центр тора L0 = прежний центр кольца)")
for b in (0.0, 71.30):
    g = h.build(8, b); A = [np.array(x) for x in g['A']]; C = [r['C'] for r in g['rings']]
    print(f"  замкнутое build(8, {b:.2f}°): до |A_i − A_i+1| = {np.linalg.norm(A[0] - A[1]):.3f}; после совместного E4 |C_i − C_i+1| = {np.linalg.norm(C[0] - C[1]):.3f}")
