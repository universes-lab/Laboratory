"""Классический каркас [мост: заряд <-> темпоральный поток поверхностной подкомпоненты].
Закрутка покоящегося заряженного тела в центре цикла при замыкании (beta: 0 -> beta_f).
Импульс заряда dp = -dq*dA; угловой импульс вокруг +y: L_y = -sum dq (r x dA)_y, где dA = A(beta_f) - A(0) (mu0/4pi = 1, I = 1, R = 1).
Для однородного поля это даёт теорему Лармора: omega = -(q/2m) dB."""
import importlib.util, numpy as np, os, sys
spec = importlib.util.spec_from_file_location('h', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)

def A(S, X, chunk=300):
    mid, dl = S; X = np.atleast_2d(X); out = np.zeros_like(X)
    for s in range(0, len(X), chunk):
        R = np.linalg.norm(X[s:s+chunk, None, :] - mid[None], axis=2)
        out[s:s+chunk] = (dl[None] / R[..., None]).sum(1)
    return out

def fib(n):
    i = np.arange(n) + 0.5; phi = np.arccos(1 - 2*i/n); th = np.pi*(1 + 5**0.5)*i
    return np.stack([np.sin(phi)*np.cos(th), np.cos(phi), np.sin(phi)*np.sin(th)], 1)

def angular_impulse(points, w, S0, S1):
    dA = A(S1, points) - A(S0, points)
    rxdA_y = points[:, 2]*dA[:, 0] - points[:, 0]*dA[:, 2]
    return -(w * rxdA_y).sum()               # L_y for total charge q = 1

S0 = h.segments(h.build(8, 0), 2000)
B0 = h.field(S0, [[0, 0, 0]])[0, 1]
# uniform ball: shells weighted by r^2
rr = np.linspace(0.04, 0.98, 24); F = fib(500)
ball_pts = np.concatenate([r*F for r in rr]); ball_w = np.concatenate([np.full(len(F), r**2) for r in rr]); ball_w /= ball_w.sum()
shell_pts = 0.99*fib(4000); shell_w = np.full(len(shell_pts), 1/len(shell_pts))
for bf in [float(x) for x in (sys.argv[1:] or ['30', '61.56', '63.49', '65', '66.54'])]:
    S1 = h.segments(h.build(8, bf), 2000)
    dB = h.field(S1, [[0, 0, 0]])[0, 1] - B0
    Lb = angular_impulse(ball_pts, ball_w, S0, S1)
    Ls = angular_impulse(shell_pts, shell_w, S0, S1)
    # omega = L / I ; ball I = 2/5 m, shell I = 2/3 m (m = 1)
    print(f"beta_f={bf}: dB_y(0)={dB:.3f} | ball: L_y={Lb:+.4f}, omega={Lb/0.4:+.4f}, Larmor -dB/2={-dB/2:+.4f} "
          f"| shell r=0.99: L_y={Ls:+.4f}, omega={Ls/(2/3):+.4f}", flush=True)
