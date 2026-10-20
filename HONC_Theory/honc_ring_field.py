"""
HONC, задача Б: поле колец λ-молекулы в геометрии варианта (а).

Классический аналог [мост]: кольца — витки с равным током, закон Био — Савара,
нормировка mu0*I/(4*pi) = 1, единица длины R = 1 (внешний радиус тора).
Тороидальное вращение торов как источник поля не учитывается.

Геометрия (вариант (а)): рогатые торы a = b = 1/2, кольцо — плоский эллипс
длины 2*pi через центры двух соседних торов, касательный к их осям.
Направление обхода колец задаётся условием непрерывности на контакте: соседние
кольца в общем торе идут вместе. При beta > 0 это обход по возрастанию t у всех
колец; при beta = 0 и у Z знаки чередуются (считается в build()).

Запуск: python3 honc_ring_field.py
"""
import numpy as np

A0 = B0 = 0.5  # рогатый тор, круглая трубка


def perimeter(p, q):
    a, b = max(p, q), min(p, q)
    h = ((a - b) / (a + b)) ** 2
    return np.pi * (a + b) * (1 + 3 * h / (10 + np.sqrt(4 - 3 * h)))


def ring_ellipse(c, cosg):
    """Полуоси p (вдоль хорды), q и сдвиг центра y0 для эллипса длины 2*pi."""
    if cosg < 1e-9:                      # плоская сборка: окружность-эллипс через две точки
        lo, hi = 1e-9, 10.0
        for _ in range(200):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if perimeter(c, m) < 2 * np.pi else (lo, m)
        return c, (lo + hi) / 2, 0.0
    tg = np.sqrt(1 - cosg ** 2) / cosg
    qof = lambda pp: tg * pp * np.sqrt(max(pp * pp / (c * c) - 1, 0.0))
    lo, hi = c * (1 + 1e-12), c * 60
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if perimeter(m, qof(m)) < 2 * np.pi else (lo, m)
    p = (lo + hi) / 2
    q = qof(p)
    return p, q, c * q * q / (tg * p * p)


def build(N, beta_deg):
    """Торы (центры A, оси T) и кольца (C, u, W, p, q) для N звеньев и наклона beta."""
    dl = np.pi / N
    beta = 0.0 if N == 2 else np.radians(beta_deg)
    cosg = np.sin(beta) * np.cos(dl)
    d = 2 * (A0 * np.sqrt(1 - cosg ** 2) + B0)
    c = d / 2
    Rc = c / np.sin(dl)
    p, q, y0 = ring_ellipse(c, cosg)
    yhat = np.array([0.0, 1.0, 0.0])
    A, T = [], []
    for i in range(N):
        ph = 2 * dl * i
        s = 1 if i % 2 == 0 else -1
        A.append(Rc * np.array([np.cos(ph), 0, np.sin(ph)]))
        T.append(np.cos(beta) * yhat + s * np.sin(beta) * np.array([-np.sin(ph), 0, np.cos(ph)]))
    rings = []
    for i in range(N):
        ps = 2 * dl * i + dl
        M = Rc * np.cos(dl) * np.array([np.cos(ps), 0, np.sin(ps)])
        u = np.array([-np.sin(ps), 0, np.cos(ps)])
        w = T[i] + T[(i + 1) % N]
        w /= np.linalg.norm(w)
        W = w if (np.sign(T[i] @ u) == np.sign(cosg) or cosg < 1e-12) else -w
        rings.append(dict(C=M - y0 * W, u=u, W=W, p=p, q=q))
    # Направление обхода (Om = ±1 к возрастанию t): соседние кольца в общем торе идут вместе.
    # При beta > 0 выходит Om = +1 у всех; при beta = 0 (и у Z) знаки чередуются.
    def tangent_at(r, X):
        t = np.linspace(0, 2 * np.pi, 20000, endpoint=False)
        P = r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])
        k = np.argmin(np.linalg.norm(P - X, axis=1))
        tv = -r['p'] * np.sin(t[k]) * r['u'] + r['q'] * np.cos(t[k]) * r['W']
        return tv / np.linalg.norm(tv)
    rings[0]['Om'] = 1
    for i in range(1, N):
        X = A[i]
        s = np.sign(rings[i - 1]['Om'] * tangent_at(rings[i - 1], X) @ tangent_at(rings[i], X))
        rings[i]['Om'] = int(s) if s != 0 else 1
    return dict(N=N, beta=beta_deg, d=d, Rc=Rc, p=p, q=q, y0=y0, A=A, T=T, rings=rings)


def segments(g, n=3000):
    mids, dls = [], []
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    for r in g['rings']:
        P = r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])
        if r['Om'] < 0:
            P = P[::-1]
        dl = np.roll(P, -1, 0) - P
        mids.append(P + dl / 2)
        dls.append(dl)
    return np.concatenate(mids), np.concatenate(dls)


def field(S, X, chunk=500):
    mid, dl = S
    X = np.atleast_2d(np.asarray(X, float))
    out = np.zeros_like(X)
    for s in range(0, len(X), chunk):
        R = X[s:s + chunk, None, :] - mid[None]
        out[s:s + chunk] = (np.cross(dl[None], R) / np.linalg.norm(R, axis=2)[..., None] ** 3).sum(1)
    return out


def axial_nulls(S, ymax=3.0, n=301):
    ys = np.linspace(0, ymax, n)
    by = field(S, np.stack([0 * ys, ys, 0 * ys], 1))[:, 1]
    zs = []
    for k in range(n - 1):
        if by[k] * by[k + 1] < 0:
            a, b = ys[k], ys[k + 1]
            for _ in range(50):
                m = (a + b) / 2
                fm = field(S, [[0, m, 0]])[0, 1]
                fa = field(S, [[0, a, 0]])[0, 1]
                a, b = (a, m) if fa * fm <= 0 else (m, b)
            zs.append((a + b) / 2)
    return zs


def chamber_nulls(S, ymax=1.2, rmax=1.0, starts=400, seed=1):
    """Поиск всех нулей |B| в камере |y| <= ymax, rho <= rmax: минимизация |B|^2 из случайных стартов."""
    from scipy.optimize import minimize
    rng = np.random.default_rng(seed)
    found = []
    for _ in range(starts):
        r = rmax * np.sqrt(rng.random())
        ph = 2 * np.pi * rng.random()
        x0 = np.array([r * np.cos(ph), ymax * (2 * rng.random() - 1), r * np.sin(ph)])
        res = minimize(lambda x: float((field(S, [x])[0] ** 2).sum()), x0, method='Nelder-Mead',
                       options=dict(xatol=1e-7, fatol=1e-14, maxiter=4000))
        x = res.x
        if np.sqrt(res.fun) < 1e-4 and abs(x[1]) <= ymax and np.hypot(x[0], x[2]) <= rmax:
            if not any(np.linalg.norm(x - f) < 1e-3 for f in found):
                found.append(x)
    return found


def moment(S):
    """Полный магнитный момент колец m = 1/2 * sum r x dl (I = 1), единицы I*R^2."""
    mid, dl = S
    return 0.5 * np.cross(mid, dl).sum(0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'moment':
        for N, beta in [(8, 0), (8, 30), (8, 61.56), (8, 63.49), (8, 65), (8, 66.54), (4, 0), (4, 25), (4, 50), (2, 0)]:
            m = moment(segments(build(N, beta)))
            print(f"N={N} beta={beta}: m = ({m[0]:+.4f}, {m[1]:+.4f}, {m[2]:+.4f}), |m| = {np.linalg.norm(m):.4f}")
        sys.exit(0)
    if len(sys.argv) > 1 and sys.argv[1] == 'chamber':
        beta = float(sys.argv[2]) if len(sys.argv) > 2 else 65.0
        S = segments(build(8, beta), n=1500)
        nulls = chamber_nulls(S)
        print(f"N=8 beta={beta}: nulls in chamber |y|<=1.2, rho<=1:")
        for x in nulls:
            print(f"   y={x[1]:+.4f}  rho={np.hypot(x[0], x[2]):.2e}")
        sys.exit(0)
    for N, beta in [(8, 0), (8, 30), (8, 61.56), (8, 63.49), (8, 65), (8, 66.54), (4, 0), (4, 25), (2, 0)]:
        g = build(N, beta)
        S = segments(g)
        ys = np.linspace(-3, 3, 61)
        Bax = field(S, np.stack([0 * ys, ys, 0 * ys], 1))
        B0v = field(S, [[0, 0, 0]])[0]
        print(f"N={N} beta={beta}: d={g['d']:.4f} Rc={g['Rc']:.4f} p={g['p']:.4f} q={g['q']:.4f}")
        print(f"   B(0) = ({B0v[0]:+.4f}, {B0v[1]:+.4f}, {B0v[2]:+.4f}); "
              f"max |B_perp| on y-axis = {np.hypot(Bax[:, 0], Bax[:, 2]).max():.2e}")
        if N > 2 and abs(B0v[1]) > 1e-9:
            print(f"   axial nulls (y > 0): {[round(z, 3) for z in axial_nulls(S)]}")
