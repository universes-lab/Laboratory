"""Контрольные числа к заданию об изотропии: A_l = sqrt(<P_l(n_i·n_j)>_{ij}), нормировка 1 при полном выстраивании."""
import sys, numpy as np
from numpy.polynomial import legendre as L
sys.path.insert(0, '/home/claude/universes-lab/laboratory/HONC_Theory')
def A(ns, l, w=None):
    ns = np.asarray(ns, float); ns /= np.linalg.norm(ns, axis=1)[:, None]
    w = np.ones(len(ns)) / len(ns) if w is None else np.asarray(w) / np.sum(w)
    c = np.clip(ns @ ns.T, -1, 1); P = L.legval(c, [0]*l + [1])
    return np.sqrt(max(w @ P @ w, 0))
ax3 = np.eye(3)
diag4 = np.array([[1,1,1],[1,1,-1],[1,-1,1],[-1,1,1]])
g = (1 + 5**0.5) / 2
ico6 = np.array([[0,1,g],[0,1,-g],[1,g,0],[1,-g,0],[g,0,1],[-g,0,1]])
for name, s in [('3 оси куба', ax3), ('4 диагонали куба', diag4), ('6 осей икосаэдра', ico6)]:
    print(name, ' '.join(f'A{l}={A(s,l):.4f}' for l in (2,4,6,8)))
rng = np.random.default_rng(1)
for N in (10, 100, 1000):
    a2 = [A(rng.normal(size=(N,3)), 2)**2 for _ in range(400)]
    print('случайные N=%d: sqrt<A2^2>=%.4f  1/sqrt(N)=%.4f' % (N, np.sqrt(np.mean(a2)), N**-0.5))
# полусфера: знак и плоскость
h = rng.normal(size=(200000,3)); h[h[:,1] < 0] *= -1
print('полусфера: <n_y>=%.4f  <P2(n_y)>=%.4f' % (h[:,1].mean()/np.linalg.norm(h,axis=1).mean(), np.mean(L.legval(h[:,1]/np.linalg.norm(h,axis=1), [0,0,1]))))
from honc_ring_field import build
for N, betas in [(8, (0, 30, 54.7356, 61.56, 65, 66.54, 71.30)), (4, (0, 25, 50.67)), (2, (0,))]:
    for b in betas:
        gg = build(N, b); T = np.array(gg['T']); R = np.array([np.cross(r['u'], r['W']) for r in gg['rings']])
        print(f'N={N} β={b}: торы A2={A(T,2):.4f} A4={A(T,4):.4f} | кольца A2={A(R,2):.4f} A4={A(R,4):.4f} | вместе A2={A(np.vstack([T,R]),2):.4f}')
# КТ-Г (28.10): совместная компенсация торов и колец глюона; тождество при β⊥
s2 = np.sin(np.pi / 8) ** 2
Tyy = lambda b: np.cos(np.radians(b)) ** 2
def Ryy(b, N=8):
    t = np.tan(np.radians(b)) ** 2 * np.sin(np.pi / N) ** 2; return t / (1 + t)
for b in (63.49, 65, 66.54):
    print(f'β={b}: (M_T)yy={Tyy(b):.4f} (M_R)yy={Ryy(b):.4f} кольца:торы={(1/3 - Tyy(b)) / (Ryy(b) - 1/3):.3f}')
def roots(f, a, b, n=4000):
    x = np.linspace(a, b, n); v = f(x); out = []
    for i in np.nonzero(v[:-1] * v[1:] < 0)[0]:
        lo, hi = x[i], x[i + 1]
        for _ in range(60):
            m = (lo + hi) / 2; lo, hi = (m, hi) if f(lo) * f(m) > 0 else (lo, m)
        out.append(round(float((lo + hi) / 2), 2))
    return out
for r in (0.5, 1, 2):
    print(f'кольца:торы={r}: компенсация при β =', roots(lambda b: (Tyy(b) + r * Ryy(b)) / (1 + r) - 1 / 3, 0.1, 71.30))
bp = np.degrees(np.arccos(np.tan(np.pi / 8))); gg = build(8, bp)
T = np.array(gg['T']); R = np.array([np.cross(r['u'], r['W']) for r in gg['rings']]); R /= np.linalg.norm(R, axis=1)[:, None]
tri = np.array([T[3], R[2], R[3]])
print(f'β⊥={bp:.2f}: тройка у тора 3 ортонормирована до {np.abs(tri @ tri.T - np.eye(3)).max():.1e};',
      ' '.join(f'A{l}={A(np.vstack([T, R]), l, [1]*8 + [2]*8):.4f}' for l in (2, 4, 6)), '(вес колец 2)')
