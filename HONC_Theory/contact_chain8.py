"""Проверка формулы gcd(n, 4) для числа длинных маршрутов (CONTACT-R1) при n = 7, 8, 9, 12 (против gcd(n, 8) у Дипсика)."""
import numpy as np, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    src = open('contact_pair.py').read().split('print("1. Устойчивость касаний")')[0]; exec(src)
    src2 = open('contact_pair.py').read(); i0 = src2.index('ARC = {}'); i1 = src2.index('Dc45 = first_contact'); exec(src2[i0:i1])
M45 = Rot(y, np.pi / 4); Dc45 = first_contact(RA, lambda D: place(RA, AA, M45, D * y))
for n in (7, 8, 9, 12):
    R, T = [], []
    for k in range(n):
        Rk, Tk = place(RA, AA, Rot(y, k * np.pi / 4), k * Dc45 * y); R.append(Rk); T.append(Tk)
    cl = []
    for k in range(n - 1): cl += contact_list_for(R[k], R[k + 1], k, k + 1)
    rt = routes(R, T, cl); lg = [r for r in rt if r[0] > 2.5]
    print(f"n={n}: длинных маршрутов {len(lg)} (gcd(n,4) = {np.gcd(n, 4)}, gcd(n,8) = {np.gcd(n, 8)}); длины " + ", ".join(f"{r[0]:.2f}" for r in lg) +
          f"; каждый через {sorted(set(len(r[1]) for r in lg))} сборок", flush=True)
