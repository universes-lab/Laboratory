"""Причал короткой латчерной цепочки к тору λ-молекулы — геометрическая вместимость (вариант (а)).

Модель причала [Д при ЛМ1]: звено цепочки — тор, зеркальный тору-хозяину в биссекторной плоскости, и кольцо
по правилу ЛМ1: плоский эллипс длины 2*pi через центры обоих торов, касательный к их осям. Направление хорды
u (от центра хозяина к центру причального тора) — свободный параметр; d = 2*h(|T.u|).

Для каждого u проверяется:
  - причальный тор не пересекает торы сборки (кроме хозяина, которого касается по построению);
  - причальное кольцо проходит вне всех торов, кроме двух своих отверстий (функция принадлежности >= 1 - tol);
  - кольца сборки проходят вне причального тора;
  - радиус кривизны причального кольца в отверстии >= a (условие ЛМ1);
  - (глюон в окне) причальный тор и кольцо не заходят в шар квантрона радиуса 1 в центре.
Минимальное расстояние причального кольца до колец сборки (вне отверстия хозяина) печатается отдельно:
кольца одномерны, их сближение — вопрос О-о, а не геометрии торов.

Направления: alpha — угол хорды к оси тора-хозяина, psi — азимут вокруг оси, отсчёт от направления «наружу»
(радиус сборки, спроектированный на плоскость, перпендикулярную оси).

Запуск: python3 docking.py N beta [quantron]     например: python3 docking.py 8 65 quantron;  python3 docking.py 2 0
"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
a = b = 0.5
TOL = 2e-3


def memb(X, A, T):
    v = X - A; z = v @ T
    rho = np.linalg.norm(v - np.outer(z, T), axis=1)
    return ((rho - a) ** 2 + z ** 2) / b ** 2


def torus_surface(A, T, n=36):
    e1 = np.cross(T, [1.0, 0, 0]) if abs(T[0]) < 0.9 else np.cross(T, [0, 1.0, 0])
    e1 /= np.linalg.norm(e1); e2 = np.cross(T, e1)
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, n, endpoint=False), np.linspace(0, 2 * np.pi, n, endpoint=False))
    u, v = u.ravel(), v.ravel()
    r = a + b * np.cos(v)
    return A + np.outer(r * np.cos(u), e1) + np.outer(r * np.sin(u), e2) + np.outer(b * np.sin(v), T)


def ring_points(C, u, W, p, q, n=500):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return C + np.outer(p * np.cos(t), u) + np.outer(q * np.sin(t), W)


def dock_link(A, T, uhat):
    """Причальный тор (A2, T2) и кольцо (C, u, W, p, q) для хорды uhat; None, если ЛМ1 не выполняется."""
    cg = float(T @ uhat)
    s = np.sign(cg) if abs(cg) > 1e-12 else 1.0
    cg = abs(cg)
    if cg > 0.985:
        return None
    hgt = a * np.sqrt(1 - cg ** 2) + b
    d = 2 * hgt; c = d / 2
    A2 = A + d * uhat
    T2 = T - 2 * (T @ uhat) * uhat
    p, q, y0 = h.ring_ellipse(c, cg)
    M = (A + A2) / 2
    Tp = T - (T @ uhat) * uhat
    W = Tp / np.linalg.norm(Tp) if np.linalg.norm(Tp) > 1e-9 else np.cross(uhat, [0, 0, 1.0])
    # выбрать знак W так, чтобы касательная в A была параллельна T
    for Ws in (W, -W):
        C = M - y0 * Ws
        tA = np.arctan2(((A - C) @ Ws) / q, ((A - C) @ uhat) / p)
        tang = -p * np.sin(tA) * uhat + q * np.cos(tA) * Ws
        tang /= np.linalg.norm(tang)
        if abs(abs(tang @ T) - 1) < 1e-6 and np.linalg.norm(C + p * np.cos(tA) * uhat + q * np.sin(tA) * Ws - A) < 1e-6:
            kap = p * q / (p ** 2 * np.sin(tA) ** 2 + q ** 2 * np.cos(tA) ** 2) ** 1.5
            return dict(A2=A2, T2=T2, C=C, u=uhat, W=Ws, p=p, q=q, Rcurv=1 / kap)
    return None


def assembly(N, beta):
    g = h.build(N, beta)
    tori = [(np.array(A), np.array(T) / np.linalg.norm(T)) for A, T in zip(g['A'], g['T'])]
    rings = [ring_points(r['C'], r['u'], r['W'], r['p'], r['q']) for r in g['rings']]
    return g, tori, rings


def check(link, k, tori, rings, quantron):
    A2, T2 = link['A2'], link['T2']
    if min(np.linalg.norm(A2 - A) for A, T in tori) < 0.05:
        return False, 'занято циклом', None
    S2 = torus_surface(A2, T2)
    for j, (A, T) in enumerate(tori):
        if j == k:
            continue
        if memb(S2, A, T).min() < 1 - TOL or memb(torus_surface(A, T), A2, T2).min() < 1 - TOL:
            return False, 'тор', None
    R = ring_points(link['C'], link['u'], link['W'], link['p'], link['q'])
    for j, (A, T) in enumerate(tori):
        if memb(R, A, T).min() < 1 - TOL:
            return False, 'кольцо в торе', None
    for rp in rings:
        if memb(rp, A2, T2).min() < 1 - TOL:
            return False, 'кольцо сборки в причальном торе', None
    if link['Rcurv'] < a - 1e-6:
        return False, 'кривизна', None
    if quantron and (np.linalg.norm(S2, axis=1).min() < 1 - TOL or np.linalg.norm(R, axis=1).min() < 1 - TOL):
        return False, 'квантрон', None
    Ak = tori[k][0]
    far = np.linalg.norm(R - Ak, axis=1) > 0.6
    dmin = min(np.linalg.norm(R[far][:, None] - rp[None], axis=2).min() for rp in rings)
    return True, 'ok', dmin


def frame(k, tori):
    A, T = tori[k]
    rad = A - (A @ T) * T if np.linalg.norm(A) > 1e-9 else np.array([1.0, 0, 0])
    eo = A / np.linalg.norm(A) if np.linalg.norm(A) > 1e-9 else np.array([1.0, 0, 0])
    eo = eo - (eo @ T) * T; eo /= np.linalg.norm(eo)
    return T, eo, np.cross(T, eo)


def angles(uhat, T, eo, et):
    al = np.degrees(np.arccos(np.clip(uhat @ T, -1, 1)))
    ps = np.degrees(np.arctan2(uhat @ et, uhat @ eo)) % 360
    return al, ps


if __name__ == '__main__':
    N = int(sys.argv[1]); beta = float(sys.argv[2]); quantron = 'quantron' in sys.argv
    g, tori, rings = assembly(N, beta)
    k = 0
    T, eo, et = frame(k, tori)
    print(f"N={N} beta={beta} quantron={quantron}; хозяин — тор 0")
    for j in ((k - 1) % N, (k + 1) % N) if N > 2 else (1,):
        uh = tori[j][0] - tori[k][0]; uh /= np.linalg.norm(uh)
        print(f"   кольцо цикла к тору {j}: alpha={angles(uh, T, eo, et)[0]:.1f}, psi={angles(uh, T, eo, et)[1]:.1f}")
    free, reasons = [], {}
    for al in np.arange(5, 180, 5.0):
        for ps in np.arange(0, 360, 5.0):
            ar, pr = np.radians(al), np.radians(ps)
            uh = np.cos(ar) * T + np.sin(ar) * (np.cos(pr) * eo + np.sin(pr) * et)
            link = dock_link(tori[k][0], T, uh)
            if link is None:
                reasons['ЛМ1'] = reasons.get('ЛМ1', 0) + 1; continue
            ok, why, dmin = check(link, k, tori, rings, quantron)
            reasons[why] = reasons.get(why, 0) + 1
            if ok:
                free.append((al, ps, dmin))
    print("   причины:", reasons)
    print(f"   свободных направлений: {len(free)} из {len(np.arange(5,180,5.0))*72}")
    # сводка по азимуту: диапазон alpha
    import collections
    byps = collections.defaultdict(list)
    for al, ps, dm in free:
        byps[ps].append((al, dm))
    line = []
    for ps in sorted(byps):
        als = [x[0] for x in byps[ps]]; dm = min(x[1] for x in byps[ps])
        line.append(f"psi={ps:5.1f}: alpha {min(als):.0f}-{max(als):.0f} (n={len(als)}, мин. до колец {dm:.2f})")
    print('\n'.join('   ' + l for l in line))
    np.save(os.path.join(here, f'dock_free_{N}_{beta}{"_q" if quantron else ""}.npy'), np.array(free))
