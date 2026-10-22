"""Узел защёлки: входящее кольцо, общий тор, исходящее кольцо — знаки по F2–F3 на замкнутых λ-циклах.

Ничего не назначается заранее, кроме принятого:
  - геометрия ЛМ1 (honc_ring_field.build);
  - спины торов по J5: сосед — зеркальный образ в биссекторной плоскости, S_{i+1} = -M_i S_i (псевдовектор);
  - L (F2) — число зацепления Гаусса кольца со средней окружностью тора, ориентированной по спину; F3 — сумма.
Проверяется:
  1. замыкаются ли спины по циклу (J4/G3);
  2. одинаков ли знак кольца у двух его отверстий (тождество (-Mt)·(-MS) = t·S) — тогда s_i определён;
  3. eta_i = s_i·s_{i-1} равен ли относительному направлению прохождения двух колец в отверстии i
     (знак (t_in·T_i)(t_out·T_i)) — то есть не зависит от спина;
  4. L цикла при каждом наборе знаков s и что требует F4 [Г] (Z нейтрален, W заряжен);
  5. какой набор знаков соответствует правилу «вместе» из honc_ring_field (непрерывность на контакте колец).
Запуск: python3 latch_node.py
"""
import importlib.util, itertools, numpy as np, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
a = h.A0


def core(A, T, s, n=500):
    T = T / np.linalg.norm(T)
    e1 = np.cross(T, [1.0, 0, 0]) if abs(T[0]) < 0.9 else np.cross(T, [0, 1.0, 0])
    e1 /= np.linalg.norm(e1); e2 = np.cross(T, e1)
    t = np.linspace(0, 2 * np.pi, n, endpoint=False) * s
    return A + a * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))


def gauss(P, Q):
    dP = np.roll(P, -1, 0) - P; dQ = np.roll(Q, -1, 0) - Q
    R = (P + dP / 2)[:, None, :] - (Q + dQ / 2)[None, :, :]
    num = np.einsum('ijk,ijk->ij', R, np.cross(dP[:, None, :], dQ[None, :, :]))
    return (num / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)


def ring_pts(r, n=1500):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])


def tangent(r, X):
    t = np.linspace(0, 2 * np.pi, 20000, endpoint=False)
    P = r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W'])
    k = np.argmin(np.linalg.norm(P - X, axis=1))
    v = -r['p'] * np.sin(t[k]) * r['u'] + r['q'] * np.cos(t[k]) * r['W']
    return v / np.linalg.norm(v)


def analyse(N, beta):
    g = h.build(N, beta)
    A = [np.array(x) for x in g['A']]; T = [np.array(x) / np.linalg.norm(x) for x in g['T']]
    S = [T[0]]
    for i in range(N):
        d = A[(i + 1) % N] - A[i]; u = d / np.linalg.norm(d)
        S.append(-(np.eye(3) - 2 * np.outer(u, u)) @ S[-1])
    closes = np.allclose(S[N], S[0], atol=1e-9)
    S = S[:N]
    cores = [core(A[j], T[j], 1 if S[j] @ T[j] > 0 else -1) for j in range(N)]
    R = [ring_pts(r) for r in g['rings']]
    Lk = np.array([[int(round(gauss(R[i], cores[j]))) for j in range(N)] for i in range(N)])
    # знак кольца у двух его отверстий (кольцо i проходит торы i и i+1)
    ends = [(Lk[i, i], Lk[i, (i + 1) % N]) for i in range(N)]
    ident = all(x == y and x != 0 for x, y in ends)
    base = np.array([x for x, y in ends])            # знак кольца i при обходе по возрастанию параметра
    # eta через направление прохождения в отверстии i: кольцо i-1 (входящее) и i (исходящее)
    eta_dir = []
    for i in range(N):
        t_in = tangent(g['rings'][(i - 1) % N], A[i]); t_out = tangent(g['rings'][i], A[i])
        eta_dir.append(int(np.sign((t_in @ T[i]) * (t_out @ T[i]))))
    eta_sign = [int(base[i] * base[(i - 1) % N]) for i in range(N)]
    om = np.array([r['Om'] for r in g['rings']])
    s_together = base * om                              # знаки колец при обходе «вместе» (honc_ring_field)
    return dict(closes=closes, ident=ident, Lk=Lk, base=base, eta_dir=eta_dir, eta_sign=eta_sign,
                s_together=s_together, rows_ok=all(np.abs(Lk[i]).sum() == 2 for i in range(N)))


if __name__ == '__main__':
    for name, N, beta in (("Z", 2, 0.0), ("W", 4, 0.0), ("W", 4, 25.0), ("глюон", 8, 0.0), ("глюон", 8, 65.0)):
        r = analyse(N, beta)
        print(f"{name} (N = {N}, beta = {beta}): спины по J5 замыкаются: {r['closes']}; каждое кольцо проходит ровно два тора: {r['rows_ok']}; "
              f"знак кольца одинаков у двух отверстий: {r['ident']}")
        print(f"   eta по знакам Lk = {r['eta_sign']}; eta по направлению прохождения в отверстии = {r['eta_dir']}; совпадают: {r['eta_sign'] == r['eta_dir']}")
        st = r['s_together']
        print(f"   правило «вместе» (непрерывность колец на контакте): знаки колец {list(st)}, L = {2 * int(st.sum()):+d}")
        alt = np.array([(-1) ** i for i in range(N)])
        print(f"   один знак: L = {2 * N:+d};  чередование: L = {2 * int(alt.sum()):+d};  всего наборов с L = 0: "
              f"{sum(1 for s in itertools.product((1, -1), repeat=N) if sum(s) == 0)} из {2 ** N}")
