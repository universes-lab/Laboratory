"""Этап А, продолжение: движение и переориентация Q1 в неоднородном поле глюонного инструмента [мост].

Мост A-13: обход колец — ток; 2D-поверхность Q1 несёт заряд-метку и, вращаясь, магнитный момент m.
Статусы: геометрия — [Д при ЛМ1]; поле — [Д, мост] при правиле обхода [Г]; динамика — [мост] при О-к.

1. Ландшафт |B| в камере (глюон N = 8): нули, экстремумы, гессиан |B| в особых точках.
   Адиабатически прецессирующий момент чувствует U = -m_par |B|: «ищущий слабое поле» (m против B) —
   к минимумам |B|, «ищущий сильное» — к максимумам.
2. Градиент поля в нулях (g) — для оценки неадиабатичности (переворот Майораны).
3. Тор-Q1 как протяжённое тело (вращающаяся заряженная поверхность рогатого тора): сила и момент
   против точечного диполя в центре. Для сферы совпадение точное (теорема о среднем) — проверка.
Запуск: python3 stageA_dynamics.py
"""
import importlib.util, numpy as np, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)

def segs(beta, rule):
    g = h.build(8, beta)
    if rule == 'встречно':
        for i, r in enumerate(g['rings']): r['Om'] = r['Om'] * (-1) ** i
    return h.segments(g, 1500)

def B(S, X): return h.field(S, np.atleast_2d(X))

def modB(S, X): return np.linalg.norm(B(S, X), axis=1)

def hess_mod(S, x, e=1e-3):
    H = np.zeros((3, 3)); f0 = modB(S, x)[0]
    for i in range(3):
        for j in range(3):
            di = np.eye(3)[i] * e; dj = np.eye(3)[j] * e
            H[i, j] = (modB(S, x + di + dj)[0] - modB(S, x + di - dj)[0] - modB(S, x - di + dj)[0] + modB(S, x - di - dj)[0]) / (4 * e * e)
    return np.linalg.eigvalsh(H)

def grad_tensor(S, x, e=1e-4):
    G = np.zeros((3, 3))
    for j in range(3):
        d = np.eye(3)[j] * e
        G[:, j] = (B(S, x + d)[0] - B(S, x - d)[0]) / (2 * e)
    return G

print("1–2. Ландшафт |B| в камере (единицы каркаса), особые точки на оси и их тип")
for beta in (45.0, 61.56, 65.0):
    for rule in ('вместе', 'встречно'):
        S = segs(beta, rule)
        ys = np.linspace(-1.4, 1.4, 281); P = np.stack([0 * ys, ys, 0 * ys], 1)
        By = B(S, P)[:, 1]; M = np.abs(By)
        pts = sorted(set([0.0] + [round((ys[k] + ys[k + 1]) / 2, 3) for k in range(len(ys) - 1) if By[k] * By[k + 1] < 0]
                         + [round(ys[k], 2) for k in range(1, len(ys) - 1) if M[k] > M[k - 1] and M[k] >= M[k + 1]]))
        line = []
        for yv in pts:
            if yv < -1e-9: continue
            x = np.array([0, yv, 0.0])
            if modB(S, x)[0] < 1e-3:                       # нуль: уточнить и взять градиент
                lo, hi = yv - 0.01, yv + 0.01
                for _ in range(40):
                    m = (lo + hi) / 2
                    lo, hi = (lo, m) if B(S, [0, lo, 0])[0, 1] * B(S, [0, m, 0])[0, 1] <= 0 else (m, hi)
                x = np.array([0, (lo + hi) / 2, 0]); ev = np.sort(np.linalg.eigvals(grad_tensor(S, x)).real)
                line.append(f"y={x[1]:+.3f}: НУЛЬ, собств. знач. градиента {np.round(ev, 2).tolist()} — точечный минимум |B|")
            else:
                ev = hess_mod(S, x)
                kind = ("минимум |B|" if (ev > 0).all() else "максимум |B|" if (ev < 0).all() else "седло |B|")
                line.append(f"y={yv:+.2f}: |B|={modB(S, x)[0]:.3f}, гессиан |B| {np.round(ev, 2).tolist()} — {kind}")
        print(f"  beta={beta}, «{rule}»:"); print("     " + "\n     ".join(line))

print("\n3. Протяжённое тело против точечного диполя в центре (beta = 65°, «вместе»)")
S = segs(65.0, 'вместе')
def body_points(kind, n=70):
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / n, np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / n)
    u, v = u.ravel(), v.ravel()
    if kind == 'тор':                                    # рогатый тор a = b = 1/2, ось — локальная z
        r = 0.5 + 0.5 * np.cos(v)
        P = np.stack([r * np.cos(u), r * np.sin(u), 0.5 * np.sin(v)], 1); w = r * 0.25
    else:                                               # сфера радиуса 1 (равномерная по площади)
        th = np.arccos(1 - 2 * (np.arange(n * n) + 0.5) / (n * n)); ph = np.pi * (1 + 5 ** 0.5) * np.arange(n * n)
        P = np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], 1); w = np.ones(n * n)
    return P, w / w.sum()
def rot_to(ax):
    ax = ax / np.linalg.norm(ax); z = np.array([0, 0, 1.0])
    v = np.cross(z, ax); s = np.linalg.norm(v); c = z @ ax
    if s < 1e-12: return np.eye(3) if c > 0 else np.diag([1, -1, -1.0])
    K = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return np.eye(3) + K + K @ K * ((1 - c) / s ** 2)
for kind in ('сфера', 'тор'):
    P0, w = body_points(kind)
    for th in (0, 45, 90):
        for dy in (0.0, 0.01):
            ax = np.array([np.sin(np.radians(th)), np.cos(np.radians(th)), 0.0])
            R = rot_to(ax); Pl = P0 @ R.T; c0 = np.array([0, dy, 0.0]); X = Pl + c0
            om = ax                                    # вращение вокруг оси тела, заряд на поверхности (вес w)
            K = w[:, None] * np.cross(om, Pl)          # поверхностный ток (на единицу заряда и ω)
            Bx = B(S, X)
            F = np.cross(K, Bx).sum(0); tau = np.cross(Pl, np.cross(K, Bx)).sum(0)
            m = 0.5 * np.cross(Pl, K).sum(0)
            G = grad_tensor(S, c0); Fpt = G.T @ m; tpt = np.cross(m, B(S, c0)[0])
            print(f"   {kind}, ось под {th:2d}° к оси сборки, центр y={dy:+.2f}: |m|={np.linalg.norm(m):.3f}; "
                  f"F={np.round(F, 4).tolist()} против точечного {np.round(Fpt, 4).tolist()}; "
                  f"τ={np.round(tau, 4).tolist()} против {np.round(tpt, 4).tolist()}")
