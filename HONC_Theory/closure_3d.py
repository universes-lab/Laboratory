"""Этап А, режим «замыкание», вне оси: включается ли адиабатический режим у нулей [мост при О-к+ на время замыкания].

Поле около оси — разложение осесимметричного поля по профилю b(y, β) (вторая степень по ρ):
  B_y = b - ρ² b''/4,  B_x = -x b'/2,  B_z = -z b'/2.
Сфера — точный диполь в центре: сила ∇(s·B) (масштаб 1, время — в единицах осевого движения, как в closure_axial.py);
момент: прецессия s вокруг B с частотой P·|B| (P — отношение частоты прецессии к частоте осевого движения).
Стенки — канал радиуса (свободный радиус − 1) по геометрии ЛМ1; упор неупругий. Уход по оси — пока выход открыт.
Обход «вместе», β: 5° → 65° за Θ = 30 (медленное замыкание, в котором на оси работает отбор).
Запуск: python3 closure_3d.py
"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
import docking as D
from scipy.interpolate import RectBivariateSpline

betas = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 58, 60, 61.56, 62.5, 63.49, 64.25, 65.0])
ys = np.linspace(-1.5, 1.5, 151)
Bg = np.array([h.field(h.segments(h.build(8, b), 1200), np.stack([0 * ys, ys, 0 * ys], 1))[:, 1] for b in betas])
bsp = RectBivariateSpline(betas, ys, Bg)
yy = np.linspace(0, 1.45, 30); FR = np.zeros((len(betas), len(yy)))
for i, b in enumerate(betas):
    g = h.build(8, b)
    obst = np.vstack([D.ring_points(r['C'], r['u'], r['W'], r['p'], r['q'], 1500) for r in g['rings']] +
                     [D.torus_surface(np.array(A), np.array(T) / np.linalg.norm(T), 90) for A, T in zip(g['A'], g['T'])])
    for j, yv in enumerate(yy):
        FR[i, j] = np.linalg.norm(obst - np.array([0, yv, 0.0]), axis=1).min()
frsp = RectBivariateSpline(betas, yy, FR, kx=1, ky=1)

def field(bt, P3):
    x, y, z = P3[:, 0], P3[:, 1], P3[:, 2]
    b = bsp(bt, y, grid=False); b1 = bsp(bt, y, dy=1, grid=False); b2 = bsp(bt, y, dy=2, grid=False)
    rho2 = x * x + z * z
    return np.stack([-x * b1 / 2, b - rho2 * b2 / 4, -z * b1 / 2], 1), (b, b1, b2)

def force(s, P3, bb):
    b, b1, b2 = bb; x, z = P3[:, 0], P3[:, 2]
    Fx = -s[:, 1] * x * b2 / 2 - s[:, 0] * b1 / 2
    Fz = -s[:, 1] * z * b2 / 2 - s[:, 2] * b1 / 2
    Fy = s[:, 1] * b1 - (s[:, 0] * x + s[:, 2] * z) * b2 / 2
    return np.stack([Fx, Fy, Fz], 1)

def rotate(s, B, ang):
    n = np.linalg.norm(B, axis=1); k = B / np.maximum(n, 1e-12)[:, None]; a = (ang * n)[:, None]
    return s * np.cos(a) + np.cross(k, s) * np.sin(a) + k * (k * s).sum(1)[:, None] * (1 - np.cos(a))

rng = np.random.default_rng(11); N = 300
s0 = rng.normal(size=(N, 3)); s0 /= np.linalg.norm(s0, axis=1)[:, None]
P0 = np.stack([rng.normal(0, 0.005, N), rng.normal(0, 0.02, N), rng.normal(0, 0.005, N)], 1)
Theta = 30.0; dt = 0.002; nst = int(Theta / dt)
for Pp in (0.0, 10.0, 100.0, 1000.0, 10000.0):
    s = s0.copy(); P3 = P0.copy(); V = np.zeros((N, 3)); gone = np.zeros(N, bool); side = np.zeros(N, bool)
    for k in range(nst):
        bt = 5 + 60 * k / nst
        B, bb = field(bt, P3)
        if Pp > 0:
            s = rotate(s, B, Pp * dt)
        V += force(s, P3, bb) * dt; P3 += V * dt
        fr = frsp(bt, np.minimum(np.abs(P3[:, 1]), 1.45), grid=False)
        open_ax = frsp(bt, 1.45, grid=False)[()] >= 1.0 and frsp(bt, 1.12, grid=False)[()] >= 1.0
        rw = np.clip(fr - 1.0, 0.0, 0.3)
        rho = np.hypot(P3[:, 0], P3[:, 2])
        lat = (rho > 0.29) & (bt < 40) & ~gone
        side |= lat; gone |= lat
        hitr = (rho > rw) & ~gone
        if hitr.any():
            f = (rw[hitr] / np.maximum(rho[hitr], 1e-12))
            P3[hitr, 0] *= f; P3[hitr, 2] *= f; V[hitr, 0] = 0; V[hitr, 2] = 0
        ax_out = (np.abs(P3[:, 1]) > 1.4) & ~gone
        if open_ax:
            gone |= ax_out
        blocked = (fr < 1.0) & ~gone
        if blocked.any():
            P3[blocked, 1] -= V[blocked, 1] * dt; V[blocked, 1] = 0
        P3[gone] = 0; V[gone] = 0
    keep = ~gone
    B, _ = field(65.0, P3); bh = B / np.maximum(np.linalg.norm(B, axis=1), 1e-12)[:, None]
    cen = keep & (np.abs(P3[:, 1]) < 0.3); nul = keep & (np.abs(np.abs(P3[:, 1]) - 0.623) < 0.15); oth = keep & ~cen & ~nul
    f = lambda m, a: f"{a[m].mean():+.2f}" if m.any() else "  — "
    print(f"P={Pp:7.0f}: ушли по оси {(gone & ~side).mean():.2f}, вбок {side.mean():.2f}; у центра {cen.mean():.2f} (s·B̂ {f(cen, (s * bh).sum(1))}, s_y {f(cen, s[:, 1])}); "
          f"у нулей {nul.mean():.2f} (s·B̂ {f(nul, (s * bh).sum(1))}); прочие {oth.mean():.2f}", flush=True)
