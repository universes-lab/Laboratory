"""Закрутка шести квантронов при замыкании цикла глюона — быстрая квадратичная модель поля.

Классический каркас [мост: заряд <-> темпоральный поток поверхностной подкомпоненты].
Вблизи центра цикла приращение поля при замыкании (beta: 0 -> beta_f) берётся в виде вакуумного осесимметричного
поля второго порядка: B_y = B0 + c (y^2 - rho^2/2). Его векторный потенциал: dA = f (z, 0, -x),
f = B0/2 + c (y^2/2 - rho^2/8). B0 и c считаются по полю колец на оси (honc_ring_field.py).
Член четвёртого порядка (симметрия C4) отброшен; против полного расчёта spinup_torus.py точность ~1%.

Квантрон: 2D-тело (сфера или рогатый тор a = b = 1/2, тонкие оболочки) несёт весь заряд q и массу mu;
кольцо радиуса 1 несёт массу mu и не несёт заряда. dL = -q <r x dA>, omega = I^-1 dL (замороженный предел:
собственное вращение за время замыкания не учитывается).

Запуск: python3 spinup_quad.py [beta_f]        (по умолчанию 65)
"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
F = __import__('fractions').Fraction


def field_params(bf, n=3000, eps=0.02):
    """B0 и c для приращения поля dB = B(beta_f) - B(0) на оси цикла."""
    m1, d1 = h.segments(h.build(8, bf), n); m0, d0 = h.segments(h.build(8, 0), n)
    S = (np.concatenate([m1, m0]), np.concatenate([d1, -d0]))
    ys = np.array([-eps, 0.0, eps])
    By = h.field(S, np.stack([0 * ys, ys, 0 * ys], 1))[:, 1]
    return By[1], (By[0] - 2 * By[1] + By[2]) / eps ** 2 / 2


def dL(P, w, B0, c):
    rho2 = P[:, 0] ** 2 + P[:, 2] ** 2
    f = B0 / 2 + c * (P[:, 1] ** 2 / 2 - rho2 / 8)
    dA = f[:, None] * np.stack([P[:, 2], 0 * P[:, 0], -P[:, 0]], 1)
    return -(w[:, None] * np.cross(P, dA)).sum(0)


def torus_local(n=60):
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / n,
                       np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / n)
    P = np.stack([(0.5 + 0.5 * np.cos(v)) * np.cos(u), (0.5 + 0.5 * np.cos(v)) * np.sin(u), 0.5 * np.sin(v)], -1).reshape(-1, 3)
    w = (0.5 + 0.5 * np.cos(v)).reshape(-1)
    return P, w / w.sum()                       # ось тора — локальная z


def sphere_pts(n=3000):
    i = np.arange(n) + 0.5; phi = np.arccos(1 - 2 * i / n); th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.sin(phi) * np.cos(th), np.cos(phi), np.sin(phi) * np.sin(th)], 1), np.full(n, 1 / n)


def place(P, ax):
    """Повернуть точки так, чтобы локальная z стала осью ax."""
    ax = ax / np.linalg.norm(ax)
    e1 = np.cross(ax, [1.0, 0, 0]) if abs(ax[0]) < 0.9 else np.cross(ax, [0, 1.0, 0])
    e1 /= np.linalg.norm(e1); e2 = np.cross(ax, e1)
    return P[:, :1] * e1 + P[:, 1:2] * e2 + P[:, 2:] * ax


def I_torus(n):   return 5 / 8 * np.outer(n, n) + 7 / 16 * (np.eye(3) - np.outer(n, n))
def I_ring(n):    return np.outer(n, n) + 0.5 * (np.eye(3) - np.outer(n, n))
I_SPHERE = 2 / 3 * np.eye(3)

# тип: 2D-тело ('S' сфера, 'T' тор), ось тела ('v' вдоль вертикали, 'p' поперёк), ось кольца, заряд, mu
TYPES = [('Qd', 'S', None, 'v', F(-1, 3), F(6, 25)), ('Qu', 'S', None, 'p', F(2, 3), F(6, 25)),
         ('Qs', 'T', 'v', 'v', F(-1, 3), F(16, 65)), ('Qc', 'T', 'v', 'p', F(2, 3), F(16, 65)),
         ('Qt', 'T', 'p', 'v', F(2, 3), F(16, 65)), ('Qb', 'T', 'p', 'p', F(-1, 3), F(16, 65))]


def quantron(t, vert, e1, B0, c, TP, SP):
    name, body, bax, rax, q, mu = t
    ax_of = {'v': vert, 'p': e1}
    if body == 'S':
        l = dL(SP[0], SP[1], B0, c); I2 = I_SPHERE
    else:
        n = ax_of[bax]; l = dL(place(TP[0], n), TP[1], B0, c); I2 = I_torus(n)
    L = float(q) * l
    I = float(mu) * (I2 + I_ring(ax_of[rax]))
    return L, np.linalg.solve(I, L)


if __name__ == '__main__':
    bf = float(sys.argv[1]) if len(sys.argv) > 1 else 65.0
    B0, c = field_params(bf)
    TP, SP = torus_local(), sphere_pts()
    print(f"beta_f = {bf}: B0 = {B0:.4f}, c = {c:.3f}; Лармор -B0/2 = {-B0 / 2:+.4f}")
    print("Сверка с полным расчётом (тор, q/m = 1, omega_y = L_y / I_y):")
    for th in (0, 30, 45, 60, 90):
        n = np.array([np.sin(np.radians(th)), np.cos(np.radians(th)), 0.0])
        l = dL(place(TP[0], n), TP[1], B0, c)
        print(f"   th = {th:2d}: omega_y = {l[1] / I_torus(n)[1, 1]:+.4f}")
    print("Шесть типов, вертикаль вдоль оси цикла (omega_y):")
    y = np.array([0, 1.0, 0]); x = np.array([1.0, 0, 0])
    for t in TYPES:
        print(f"   {t[0]}: {quantron(t, y, x, B0, c, TP, SP)[1][1]:+.3f}")
    print("Шесть типов, изотропно случайная вертикаль и фаза (замороженный предел), 4000 ориентаций:")
    rng = np.random.default_rng(7)
    V = rng.normal(size=(4000, 3)); V /= np.linalg.norm(V, axis=1)[:, None]
    for t in TYPES:
        oy, tilt = [], []
        for v in V:
            e = np.cross(v, rng.normal(size=3)); e /= np.linalg.norm(e)
            L, om = quantron(t, v, e, B0, c, TP, SP)
            oy.append(om[1]); tilt.append(np.degrees(np.arccos(abs(om[1]) / np.linalg.norm(om))))
        oy = np.array(oy)
        print(f"   {t[0]}: среднее omega_y = {oy.mean():+.3f}, разброс (ст. откл.) {oy.std():.3f}, "
              f"от {oy.min():+.3f} до {oy.max():+.3f}; отход omega от оси цикла: средний {np.mean(tilt):.0f}°, макс. {np.max(tilt):.0f}°",
              flush=True)
