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
