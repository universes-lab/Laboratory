"""Маршруты в длинах дуг (а не по параметру эллипса): доля дуги между каспами по ходу обхода δ, на какой дуге касание,
куда по индексу торов идёт длинный маршрут; цепочки n = 1…6 с поворотом 45° на звено. Запуск: python3 contact_arcs.py"""
import numpy as np, io, contextlib, sys
with contextlib.redirect_stdout(io.StringIO()):
    src = open('contact_pair.py').read().split('print("1. Устойчивость касаний")')[0]; exec(src)
    src2 = open('contact_pair.py').read(); i0 = src2.index('ARC = {}'); i1 = src2.index('Dc45 = first_contact'); exec(src2[i0:i1])
P = RA[1]; sl = np.r_[0, np.cumsum(np.linalg.norm(np.roll(P, -1, 0) - P, axis=1))]
d = [np.linalg.norm(P - T, axis=1) for T in AA]; tw = np.argsort([x.min() for x in d])[:2]; ii = [int(np.argmin(d[k])) for k in tw]
M45 = Rot(y, np.pi / 4); Dc45 = first_contact(RA, lambda D: place(RA, AA, M45, D * y)); RB, AB = place(RA, AA, M45, Dc45 * y)
dc, k = pairdist(RA[1], RB[2]); ic = k[0]
for a_, b_ in ((0, 1), (1, 0)):
    i_from, i_to = ii[a_], ii[b_]; frac = ((sl[i_to] - sl[i_from]) % sl[-1]) / sl[-1]
    inside = ((sl[ic] - sl[i_from]) % sl[-1]) < ((sl[i_to] - sl[i_from]) % sl[-1])
    print(f"кольцо A1: дуга по ходу обхода от тора {tw[a_]} к тору {tw[b_]} — доля {frac:.4f}; касание с B2 {'на ней' if inside else 'не на ней'}")
for n in range(1, 7):
    R, T = [], []
    for kk in range(n):
        Rk, Tk = place(RA, AA, Rot(y, kk * np.pi / 4), kk * Dc45 * y); R.append(Rk); T.append(Tk)
    cl = []
    for kk in range(n - 1): cl += contact_list_for(R[kk], R[kk + 1], kk, kk + 1)
    rt = routes(R, T, cl)
    print(f"n={n}: маршруты (длина в длинах кольца / сборок / переходов): " + "; ".join(f"{L:.3f} / {len(t)} / {c}" for L, t, c in sorted(rt, key=lambda r: -r[0])), flush=True)
