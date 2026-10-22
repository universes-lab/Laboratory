"""Ориентированные H2 и H3 на Qs: знаки прохождения и L по F2–F3, посчитанные на построенной конструкции.

Ответ на замечание Интегратора 22.10: в qs_branches.py знак прохождения первого кольца каждой ветви был
навязан (+1), а placed() знаков не переносил. Здесь знаки задаются независимо и L считается числом зацепления
Гаусса на реальных ориентированных контурах, без вывода из симметрии.

Ориентация:
  - кольцо ветви — обход tau = ±1 (относительно порядка параметра);
  - тор — спин sigma = ±1 вдоль своей оси; «образующая окружность» F2 — средняя окружность тора (радиус a),
    ориентированная по спину (против часовой стрелки, если смотреть с конца спина);
  - Qs: спин +z; собственное кольцо — внешний экватор, ориентированный по +z.
L (F3) = сумма по всем кольцам и всем торам Lk(кольцо, средняя окружность тора). Отдельно — Lk с кольцом Qs.
П1 для кольца: знаки Lk у двух его отверстий равны.

Части:
  1. Полный перебор знаков для прямой пары (геометрия ветви B — инверсия ветви A), 2 звена в ветви.
  2. Явные образы ветви A с её знаками: инверсия (противоположный класс) и поворот на 180° вокруг оси Qs.
  3. H3: три ветви поворотами на 120° и смешанные наборы; L при одинаковом знаке вдоль ветви.
Запуск: python3 qs_oriented.py
"""
import numpy as np, sys, os, itertools
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import docking as D
import qs_branches as QB

a = D.a
QB.LCH = 2
NC = 400
Z = np.array([0, 0, 1.0])


def core(A, T, s, n=NC):
    T = T / np.linalg.norm(T)
    e1 = np.cross(T, [1.0, 0, 0]) if abs(T[0]) < 0.9 else np.cross(T, [0, 1.0, 0])
    e1 /= np.linalg.norm(e1); e2 = np.cross(T, e1)
    t = np.linspace(0, 2 * np.pi, n, endpoint=False) * s
    return A + a * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))


def lk(P, Q):
    return int(round(QB.gauss_link(P, Q)))


def raw_branch(al):
    """Геометрия ветви A при psi = 0 без знаков: кольца (в порядке параметра) и торы (центр, ось)."""
    QB._cache.pop(al, None)
    br = QB.branch(al)
    return [l['R'] for l in br], [(l['A'], l['T']) for l in br]


def transform(rings, tori, Mx):
    """Образ ветви при ортогональном преобразовании Mx; спин — псевдовектор (det·Mx)."""
    return [R @ Mx.T for R in rings], [(Mx @ A, Mx @ T) for A, T in tori]


def evaluate(branches, own=True):
    """branches: список (rings, tori, tau, spinvec), spinvec — вектор спина каждого тора.
    Возвращает L_F3, знаки прохождения Qs, классы (знак у своего тора), П1, Lk с кольцом Qs."""
    t_ = np.linspace(0, 2 * np.pi, 1200, endpoint=False)
    OWN = np.stack([np.cos(t_), np.sin(t_), 0 * t_], 1)
    cores = [core(np.zeros(3), Z, 1)]
    for rings, tori, tau, spins in branches:
        for (A, T), S in zip(tori, spins):
            cores.append(core(A, T, 1 if S @ T > 0 else -1))
    L = 0; qs_pass, cls, p1, lk_own = [], [], True, []
    evaluate.extra = False
    idx = 1
    for rings, tori, tau, spins in branches:
        prev = 0
        for k, (R, t) in enumerate(zip(rings, tau)):
            Ro = R if t > 0 else R[::-1]
            row = [lk(Ro, c) for c in cores]
            L += sum(row)
            here_, there = row[prev], row[idx + k]
            p1 &= (here_ == there)
            evaluate.extra |= sum(abs(x) for x in row) != 2
            if k == 0:
                qs_pass.append(here_); cls.append(there); lk_own.append(lk(Ro, OWN))
            prev = idx + k
        idx += len(rings)
    return L, qs_pass, cls, p1, lk_own


def spins_P1(tori, S_start, A_start):
    """Спины торов ветви по зеркальному продолжению (J5): S_k = -M_k S_{k-1}."""
    out, S, Aprev = [], S_start, A_start
    for A, T in tori:
        u = (A - Aprev) / np.linalg.norm(A - Aprev)
        S = -(np.eye(3) - 2 * np.outer(u, u)) @ S
        out.append(S); Aprev = A
    return out


if __name__ == '__main__':
    al = 60
    RA, TA = raw_branch(al)
    INV = -np.eye(3)
    RB, TB = transform(RA, TA, INV)
    # сверка: геометрия образа совпадает с прямой парой из qs_branches (placed(180-al, 180))
    pb = QB.placed(180 - al, 180)
    dev = max(np.abs(np.sort(np.linalg.norm(R1, axis=1)) - np.sort(np.linalg.norm(l['R'], axis=1))).max() for R1, l in zip(RB, pb))
    print(f"alpha = {al}°, по 2 звена в ветви; инверсия ветви A против прямой пары qs_branches: расхождение радиусов {dev:.1e}")

    print("\n1. Полный перебор знаков для прямой пары: обходы 4 колец и спины 4 торов независимо (256 наборов)")
    stats = {}
    for labels in itertools.product((1, -1), repeat=8):
        tA, tB, sA, sB = labels[0:2], labels[2:4], labels[4:6], labels[6:8]
        spA = [s * T / np.linalg.norm(T) for s, (A, T) in zip(sA, TA)]
        spB = [s * T / np.linalg.norm(T) for s, (A, T) in zip(sB, TB)]
        L, qp, cl, p1, lo = evaluate([(RA, TA, tA, spA), (RB, TB, tB, spB)])
        key = (p1, 'встречно' if qp[0] != qp[1] else 'в одну сторону', 'классы разные' if cl[0] != cl[1] else 'классы одинаковые')
        stats.setdefault(key, []).append(L)
    for key in sorted(stats):
        Ls = stats[key]
        print(f"   П1={key[0]!s:5s} | прохождение Qs {key[1]:15s} | {key[2]:17s} | наборов {len(Ls):3d} | L: "
              + ', '.join(f"{v:+d}×{Ls.count(v)}" for v in sorted(set(Ls))))

    print("\n2. Явные образы ветви A (её знаки: обход tau = +1, спины по П1 от спина Qs +z)")
    spA = spins_P1(TA, Z, np.zeros(3))
    base = (RA, TA, (1, 1), spA)
    for name, Mx in (("инверсия в центре Qs (несобственная)", INV),
                     ("отражение в экваторе Qs (несобственная)", np.diag([1.0, 1, -1])),
                     ("поворот на 180° вокруг оси Qs (собственная)", np.diag([-1.0, -1, 1])),
                     ("отражение в плоскости, содержащей ось (меняет спин Qs)", np.diag([-1.0, 1, 1]))):
        Rb, Tb = transform(RA, TA, Mx)
        det = np.linalg.det(Mx)
        spB = [det * (Mx @ S) for S in spA]
        L, qp, cl, p1, lo = evaluate([base, (Rb, Tb, (1, 1), spB)])
        sQs = det * (Mx @ Z)
        print(f"   {name}: спин Qs у образа {'тот же' if sQs @ Z > 0 else 'обращён'}; прохождение Qs {qp}; классы {cl}; "
              f"П1 {p1}; Lk с кольцом Qs {lo}; L = {L:+d}" + ("; кольцо проходит чужой тор (столкновение)" if evaluate.extra else ""))

    print("\n3. Правило знака вдоль ветви: «одинаковый» (s_k = s_1) и «чередование» (s_k = (-1)^k s_1); знаки проверены по Lk")
    R9, T9 = raw_branch(90)

    def oriented(Mx, s1, rule):
        Rb, Tb = transform(R9, T9, Mx)
        sp = spins_P1(Tb, Z, np.zeros(3))
        prevA, prevT, prevS = np.zeros(3), Z, Z
        taus = []
        for k, (R, (A, T), S) in enumerate(zip(Rb, Tb, sp)):
            want = s1 if rule == 'один' else s1 * (-1) ** k
            c = core(prevA, prevT, 1 if prevS @ prevT > 0 else -1)
            taus.append(want * lk(R, c))
            prevA, prevT, prevS = A, T, S
        return (Rb, Tb, tuple(taus), sp)

    Rz_ = lambda th: np.array([[np.cos(th), -np.sin(th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1.0]])
    for rule in ('один', 'чередование'):
        for name, Ms, sg in (("H2 прямая, встречно", [np.eye(3), Rz_(np.pi)], (1, -1)),
                             ("H2 прямая, в одну сторону", [np.eye(3), Rz_(np.pi)], (1, 1)),
                             ("H3 через 120°, все в одну сторону", [Rz_(0), Rz_(2 * np.pi / 3), Rz_(4 * np.pi / 3)], (1, 1, 1)),
                             ("H3 через 120°, одна встречно", [Rz_(0), Rz_(2 * np.pi / 3), Rz_(4 * np.pi / 3)], (1, 1, -1))):
            L, qp, cl, p1, lo = evaluate([oriented(M, s1, rule) for M, s1 in zip(Ms, sg)])
            print(f"   [{rule:11s}] {name:34s}: прохождение Qs {qp}; классы {cl}; П1 {p1}; L = {L:+d}")
