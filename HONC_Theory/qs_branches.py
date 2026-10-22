"""Ветви на Qs (H-Qs): геометрическая соединимость двух и трёх прямых цепочек и знаки прохождения.

Qs: рогатый тор a = b = 0,5 в начале координат, ось T = z; собственное кольцо — внешний экватор (окружность
радиуса 1 в плоскости xy). Его отверстие свободно: своё кольцо через него не проходит (L = 0 у Q1).
Ветвь — прямая цепочка по правилу ЛМ1 (как в dock_chains.py): звено k — тор, зеркальный предыдущему в
биссекторной плоскости, и кольцо через отверстия двух соседних торов; направление хорды u одно для всех звеньев.
Qs осесимметричен, поэтому ветвь задаётся углом alpha хорды к оси T, а азимут psi — поворотом вокруг T.

Проверки для набора ветвей:
  - торы ветвей не пересекают тор Qs (кроме касания первого звена) и друг друга;
  - кольца ветвей проходят вне всех торов, кроме двух своих отверстий;
  - собственное кольцо Qs проходит вне торов ветвей;
  - минимальные расстояния: кольца ветвей до кольца Qs и друг до друга (вне окрестности общего отверстия).
Знаки: при зеркальном продолжении спина по цепочке (J5: S_k = -M S_{k-1}, M — отражение в биссекторной
плоскости) проверяется согласованность П1: sign(t . S) одинаков у обоих отверстий каждого кольца; L ветви —
сумма знаков всех прохождений (F3), включая прохождение через Qs.

ОГРАНИЧЕНИЕ (замечание Интегратора 22.10): знак прохождения первого кольца каждой ветви здесь навязан (+1),
а placed() знаков не переносит — для пар и троек проверена только геометрия. Ориентированные конструкции,
классы и L — в qs_oriented.py.

Запуск: python3 qs_branches.py
"""
import numpy as np, sys, os, itertools
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import docking as D

TOL = D.TOL
A0 = np.zeros(3); T0 = np.array([0, 0, 1.0])
t_ = np.linspace(0, 2 * np.pi, 1200, endpoint=False)
OWN = np.stack([np.cos(t_), np.sin(t_), 0 * t_], 1)          # собственное кольцо Qs, ориентировано по спину +z
QS_SURF = D.torus_surface(A0, T0, 40)
LCH = 3                                                       # звеньев в ветви


def Rz(ph):
    c, s = np.cos(ph), np.sin(ph)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])


def tangent(lk, X):
    C, u, W, p, q = lk['C'], lk['u'], lk['W'], lk['p'], lk['q']
    tt = np.arctan2(((X - C) @ W) / q, ((X - C) @ u) / p)
    v = -p * np.sin(tt) * u + q * np.cos(tt) * W
    return v / np.linalg.norm(v)


_cache = {}
def branch(al):
    """Ветвь при psi = 0: список звеньев (тор, кольцо, знаки)."""
    if al in _cache:
        return _cache[al]
    ar = np.radians(al)
    uh = np.cos(ar) * T0 + np.sin(ar) * np.array([1.0, 0, 0])
    A, T, S = A0, T0, T0.copy()                               # спин Qs вдоль +z
    links = []
    for k in range(LCH):
        lk = D.dock_link(A, T, uh)
        if lk is None or lk['Rcurv'] < D.a - 1e-6:
            _cache[al] = None; return None
        Mref = np.eye(3) - 2 * np.outer(uh, uh)
        S2 = -Mref @ S                                       # псевдовектор при отражении
        # обход кольца выбран так, что в отверстии предыдущего тора t . T > 0 у первого звена; дальше — по кольцу
        tA, tB = tangent(lk, A), tangent(lk, lk['A2'])
        sgn = 1.0
        if k == 0 and tA @ T0 < 0:
            sgn = -1.0
        links.append(dict(A=lk['A2'], T=lk['T2'], S=S2, R=D.ring_points(lk['C'], lk['u'], lk['W'], lk['p'], lk['q'], 600),
                          surf=D.torus_surface(lk['A2'], lk['T2'], 30),
                          sA=np.sign(sgn * tA @ S), sB=np.sign(sgn * tB @ S2), Afrom=A, sgn=sgn))
        A, T, S = lk['A2'], lk['T2'], S2
    _cache[al] = links
    return links


def placed(al, ps):
    br = branch(al)
    if br is None:
        return None
    Rm = Rz(np.radians(ps))
    return [dict(A=Rm @ l['A'], T=Rm @ l['T'], R=l['R'] @ Rm.T, surf=l['surf'] @ Rm.T, Afrom=Rm @ l['Afrom']) for l in br]


def single_ok(br):
    for k, l in enumerate(br):
        if k > 0 and (D.memb(l['surf'], A0, T0).min() < 1 - TOL or D.memb(QS_SURF, l['A'], l['T']).min() < 1 - TOL):
            return 'тор ветви в Qs'
        if D.memb(l['R'], A0, T0).min() < 1 - TOL:
            return 'кольцо ветви в торе Qs'
        if D.memb(OWN, l['A'], l['T']).min() < 1 - TOL:
            return 'кольцо Qs в торе ветви'
        for j, m in enumerate(br):
            if j not in (k, k - 1) and D.memb(l['R'], m['A'], m['T']).min() < 1 - TOL:
                return 'самопересечение ветви'
    return 'ok'


def pair_ok(b1, b2):
    for l in b1:
        for m in b2:
            if np.linalg.norm(l['A'] - m['A']) < 0.05:
                return 'торы совпали'
            if D.memb(l['surf'], m['A'], m['T']).min() < 1 - TOL or D.memb(m['surf'], l['A'], l['T']).min() < 1 - TOL:
                return 'торы ветвей'
            if D.memb(l['R'], m['A'], m['T']).min() < 1 - TOL or D.memb(m['R'], l['A'], l['T']).min() < 1 - TOL:
                return 'кольцо в торе другой ветви'
    return 'ok'


def dmin_rings(b1, b2):
    far = lambda R: R[np.linalg.norm(R, axis=1) > 0.6]
    return min(np.linalg.norm(far(l['R'])[:, None] - far(m['R'])[None], axis=2).min() for l in b1 for m in b2)


def d_own(b):
    return min(np.linalg.norm(l['R'][:, None] - OWN[None, ::4], axis=2).min() for l in b)


def gauss_link(P, Q):
    dP = np.roll(P, -1, 0) - P; dQ = np.roll(Q, -1, 0) - Q
    R = (P + dP / 2)[:, None, :] - (Q + dQ / 2)[None, :, :]
    num = np.einsum('ijk,ijk->ij', R, np.cross(dP[:, None, :], dQ[None, :, :]))
    return (num / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)


if __name__ == '__main__':
    ALS = list(range(10, 175, 5))
    print("1. Одна ветвь (длина", LCH, "звена): угол хорды к оси Qs, проверка, мин. расстояние до кольца Qs, знаки П1")
    good = []
    for al in ALS:
        br = placed(al, 0)
        if br is None:
            print(f"   alpha={al:3d}: ЛМ1 не выполняется"); continue
        why = single_ok(br)
        b0 = branch(al)
        p1 = all(l['sA'] == l['sB'] for l in b0)
        lk = gauss_link(br[0]['R'][::-1] if b0[0]['sgn'] < 0 else br[0]['R'], OWN)
        if why == 'ok':
            good.append(al)
        print(f"   alpha={al:3d}: {why:24s} до кольца Qs {d_own(br):.2f}; П1 по всем звеньям: {p1}; "
              f"знак у своего тора {b0[0]['sB']:+.0f}; зацепление с кольцом Qs {lk:+.2f}")
    print("   допустимые alpha:", good)

    print("\n2. Две ветви: прямая (u2 = -u1) и V-пара с тем же alpha (psi + 180), мин. расстояние между кольцами")
    for al in good:
        if 180 - al not in good:
            continue
        b1 = placed(al, 0); b2 = placed(180 - al, 180)          # u2 = -u1
        w = pair_ok(b1, b2)
        print(f"   прямая  alpha={al:3d}/{180-al:3d}: {w:28s} кольца ветвей {dmin_rings(b1, b2) if w == 'ok' else float('nan'):.2f}")
    for al in good:
        b1 = placed(al, 0); b2 = placed(al, 180)
        w = pair_ok(b1, b2)
        print(f"   V-пара  alpha={al:3d}:     {w:28s} кольца ветвей {dmin_rings(b1, b2) if w == 'ok' else float('nan'):.2f}")

    print("\n3. Две ветви, общий перебор: alpha1, alpha2 из допустимых, разнос азимутов 30..180")
    cnt = tot = 0
    for a1, a2 in itertools.combinations_with_replacement(good, 2):
        for dps in range(30, 181, 30):
            tot += 1
            if pair_ok(placed(a1, 0), placed(a2, dps)) == 'ok':
                cnt += 1
    print(f"   допустимо {cnt} из {tot}")

    print("\n4. Три ветви: alpha из допустимых (шаг 15), азимуты 0 / psi2 / psi3 (шаг 30)")
    g15 = [x for x in good if x % 15 == 0]
    ex, cnt, tot = [], 0, 0
    for a1, a2, a3 in itertools.combinations_with_replacement(g15, 3):
        for p2 in range(30, 360, 30):
            for p3 in range(p2 + 30, 360, 30):
                tot += 1
                B = [placed(a1, 0), placed(a2, p2), placed(a3, p3)]
                if all(pair_ok(B[i], B[j]) == 'ok' for i, j in ((0, 1), (0, 2), (1, 2))):
                    cnt += 1
                    if len(ex) < 6:
                        ex.append((a1, a2, a3, p2, p3, min(dmin_rings(B[i], B[j]) for i, j in ((0, 1), (0, 2), (1, 2)))))
    print(f"   допустимо {cnt} из {tot}; примеры (alpha1, alpha2, alpha3, psi2, psi3, мин. между кольцами):")
    for e in ex:
        print("     ", e[:5], f"{e[5]:.2f}")
    B = [placed(90, 0), placed(90, 120), placed(90, 240)]
    print("   плоская трёхлучевая (alpha = 90, через 120°):",
          [pair_ok(B[i], B[j]) for i, j in ((0, 1), (0, 2), (1, 2))])
