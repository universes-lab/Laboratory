"""Дополнение к contact_pair.py: (1) где кончается режим четырёх касаний по φ; (2) при нарушении симметрии —
какая пара колец касается первой (те же четыре или другие); (3) маршруты состояния (чтение R1) в цепочках из n = 2…6
сборок с поворотом 45° на звено. Запуск: python3 contact_chain.py"""
import numpy as np, io, contextlib, sys
with contextlib.redirect_stdout(io.StringIO()):
    sys.argv = ['x']; src = open('contact_pair.py').read().split('print("1. Устойчивость касаний")')[0]; exec(src)
    src2 = open('contact_pair.py').read(); i0 = src2.index('def routes('); i1 = src2.index('Dc45 = first_contact'); exec(src2[i0:i1])
print("(1) Режим касаний по φ:")
for ph in (5, 10, 15, 20, 25, 30, 35, 38):
    M = Rot(y, np.radians(ph)); f = lambda D, M=M: place(RA, AA, M, D * y)
    Dc = first_contact(RA, f); c = contacts(RA, f(Dc)[0])
    print(f"   φ={ph:4.1f}°: D_c={Dc:.4f}; касаний {len(c)}: " + ", ".join(f"A{i}–B{j}" for i, j, *_ in c), flush=True)
print("(2) Первое касание при нарушении симметрии (φ = 45°):")
for kind, v in (('ε', 0.5), ('ε', 1.0), ('ε', 2.0), ('δ', 0.02), ('δ', 0.05)):
    if kind == 'ε': M = Rot(np.array([1.0, 0, 0]), np.radians(v)) @ Rot(y, np.pi / 4); f = lambda D, M=M: place(RA, AA, M, D * y)
    else: M = Rot(y, np.pi / 4); f = lambda D, M=M, v=v: place(RA, AA, M, D * y + np.array([v, 0, 0]))
    Dc = first_contact(RA, f); c = contacts(RA, f(Dc)[0])
    print(f"   {kind} = {v}: первое касание при D = {Dc:.4f}: " + ", ".join(f"A{i}–B{j}" for i, j, *_ in c), flush=True)
print("(3) Цепочки (R1), поворот 45° на звено, шаг D_c(45°):")
M45 = Rot(y, np.pi / 4); Dc45 = first_contact(RA, lambda D: place(RA, AA, M45, D * y))
for n in range(1, 7):
    R, T = [], []
    for k in range(n):
        Rk, Tk = place(RA, AA, Rot(y, k * np.pi / 4), k * Dc45 * y); R.append(Rk); T.append(Tk)
    cl = []
    for k in range(n - 1): cl += contact_list_for(R[k], R[k + 1], k, k + 1)
    for k in range(n - 2): assert not contact_list_for(R[k], R[k + 2], k, k + 2)
    rt = routes(R, T, cl); long_ = sorted([r for r in rt if r[0] > 2], key=lambda r: -r[0])
    print(f"   n={n}: касаний {len(cl)}; длинные маршруты (длина в кольцах / сборок / переходов): " +
          "; ".join(f"{L:.2f} / {len(t)} / {c}" for L, t, c in long_) + f"; коротких {sum(1 for r in rt if r[0] <= 2)}", flush=True)
