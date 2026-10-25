"""И-2 (Интегратор, 25.10): совместное состояние «Q1 + причаленное кольцо Qf» за один шаг (доворот E0/В3 на 180°).
Геометрия ЛМ1: тор Q1 — рогатый (a = b = 1/2, R = 1), ось z, касп в начале координат.
Кольцо Q1: Qs — на экваторе (плоскость xy, радиус 1); Qc, Qt, Qb — в меридиональной плоскости под углом α к плоскости причала.
Причальное кольцо: окружность радиуса 1 в плоскости yz с центром (0, 1, 0) — проходит касп по оси z (длина 2π, вне тела тора).
Считаем гауссовы числа зацепления причала: с кольцом Q1 и со средней окружностью тора (радиус 1/2, ориентирована по спину тора),
и знак η — направление прохода причала через касп относительно оси тора.
Доворот (чтение R-or: ориентация переносится жёстким поворотом): Qt — тор на 180° вокруг диаметра (оси x); Qb — тор так же и кольцо
на 180° вокруг диаметра, параллельного оси тора (ось z); Qc — только кольцо, вокруг оси z. При чтении R-pos (только положения) ничего не меняется.
Запуск: python3 mooring_step.py"""
import numpy as np
def circle(c, e1, e2, r, n=4000):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False); return c + r * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))
def Lk(P, Q):
    dP = np.roll(P, -1, 0) - P; dQ = np.roll(Q, -1, 0) - Q; mP = P + dP / 2; mQ = Q + dQ / 2
    R = mP[:, None] - mQ[None]; num = np.einsum('ijk,ijk->ij', R, np.cross(dP[:, None], dQ[None]))
    return (num / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)
def Rot(axis, ang):
    a = np.asarray(axis, float) / np.linalg.norm(axis); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
X, Y, Z = np.eye(3)
moor = circle(np.array([0, 1.0, 0]), -Y, Z, 1.0)            # (0, 1 - cos t, sin t): проходит касп, касательная вдоль +z при t = 0
def memb(P, axis=Z):   # рогатый тор: < 1 внутри тела
    z = P @ axis; rho = np.linalg.norm(P - np.outer(z, axis), axis=1); return ((rho - 0.5) ** 2 + z ** 2) / 0.25
m = memb(moor); print(f"причал вне тела тора: min функции принадлежности {np.sort(m)[1]:.4f} (касп — единственная точка ≈ 1)")
tmid = 0; v = moor[1] - moor[-1]; eta0 = np.sign(v @ Z); print(f"направление прохода причала через касп вдоль оси тора: η = {eta0:+.0f}")
core = circle(np.zeros(3), X, Y, 0.5)                        # средняя окружность тора, ориентирована по спину +z
print(f"Lk(причал, средняя окружность тора) = {Lk(moor[::2], core[::2]):+.3f}")
print("\nКольцо Q1:")
qs_ring = circle(np.zeros(3), X, Y, 1.0)
print(f"  Qs (экватор): Lk(причал, кольцо) = {Lk(moor[::2], qs_ring[::2]):+.3f}; наименьшее расстояние {np.min(np.linalg.norm(moor[::8, None] - qs_ring[None, ::8], axis=2)):.3f}")
for al in (30, 60, 90, 120, 150):
    e1 = np.cos(np.radians(al)) * Y + np.sin(np.radians(al)) * X   # горизонтальное направление в меридиональной плоскости кольца
    ring = circle(np.zeros(3), e1, Z, 1.0)
    d = np.min(np.linalg.norm(moor[::8, None] - ring[None, ::8], axis=2))
    print(f"  меридиональное кольцо, угол к плоскости причала α = {al}°: Lk(причал, кольцо) = {Lk(moor[::2], ring[::2]):+.3f}; наименьшее расстояние {d:.3f}")
print("\nДоворот на 180° при чтении R-or (ориентация переносится):")
Mx = Rot(X, np.pi); Mz = Rot(Z, np.pi)
core_t = core @ Mx.T; axis_t = Mx @ Z
print(f"  тор (Qt, Qb): ось тора → {np.round(axis_t, 3)}; Lk(причал, средняя окружность) {Lk(moor[::2], core[::2]):+.3f} → {Lk(moor[::2], core_t[::2]):+.3f}; η {eta0:+.0f} → {np.sign(v @ axis_t):+.0f}")
ring90 = circle(np.zeros(3), X, Z, 1.0); ring90_t = ring90 @ Mz.T
print(f"  кольцо в меридиональной плоскости (Qc, Qb), вокруг оси z: Lk {Lk(moor[::2], ring90[::2]):+.3f} → {Lk(moor[::2], ring90_t[::2]):+.3f}; "
      f"как множество совпадает: {np.allclose(np.sort(np.round(ring90_t, 6), axis=0), np.sort(np.round(ring90, 6), axis=0))}")
qs_t = qs_ring @ Mx.T
print(f"  (справочно) экваториальное кольцо, если бы его повернули вокруг диаметра: Lk {Lk(moor[::2], qs_ring[::2]):+.3f} → {Lk(moor[::2], qs_t[::2]):+.3f}")
