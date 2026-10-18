"""Classical analog [мост]: does the magnetic interaction of the ring currents tighten (beta up) or loosen the gluon ring?
Generalized force at fixed currents is +1/2 I^2 dL_total/dbeta (toward larger total inductance).
Rings: thin wires of radius a; Neumann double integral with smoothing sqrt(r^2 + a^2)."""
import importlib.util, numpy as np, sys, os
# needs honc_ring_field.py in the same folder
spec = importlib.util.spec_from_file_location('h', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)

def ring_pts(r, n):
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    P = r['C'] + np.outer(r['p']*np.cos(t), r['u']) + np.outer(r['q']*np.sin(t), r['W'])
    if r['Om'] < 0: P = P[::-1]
    dl = np.roll(P, -1, 0) - P
    return P + dl/2, dl

def L_parts(beta, a, n):
    g = h.build(8, beta)
    R = [ring_pts(r, n) for r in g['rings']]
    def pair(i, j):
        Pi, di = R[i]; Pj, dj = R[j]; s = 0.0
        for k in range(0, n, 400):
            d = np.linalg.norm(Pi[k:k+400, None, :] - Pj[None], axis=2)
            s += ((di[k:k+400] @ dj.T) / np.sqrt(d*d + a*a)).sum()
        return s
    self_ = 8*pair(0, 0)
    nb = 8*2*pair(0, 1)                       # each ring has two neighbours; symmetric pairs
    far = 8*(2*pair(0, 2) + 2*pair(0, 3) + pair(0, 4))
    return self_, nb, far

a = float(sys.argv[1]) if len(sys.argv) > 1 else 0.02
n = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
print(f"a={a} n={n}   beta   L_self   L_neigh   L_far   L_total")
prev = None
for b in [0, 30, 50, 58, 61.56, 63.49, 65, 66.54, 68, 71.3]:
    s, nb, far = L_parts(b, a, n)
    tot = s + nb + far
    print(f"   {b:6.2f} {s:9.3f} {nb:9.3f} {far:9.3f} {tot:9.3f}", flush=True)
