"""Закрутка и толчок торовых квантронов при замыкании цикла глюона (N = 8).

Классический каркас [мост: заряд <-> темпоральный поток поверхностной подкомпоненты].
Тонкостенный рогатый тор a = b = 1/2 (внешний радиус 1), однородный q/m по поверхности (вес — площадь),
полный заряд q = 1, масса m = 1. Квантрон покоится в центре цикла; цикл замыкается, beta: 0 -> beta_f.
Индукция за время замыкания: dp = -dq * dA, где dA = A(beta_f) - A(0) (mu0 I / 4 pi = 1, R = 1).

Печатает для ориентации оси тора n = (sin th cos ph, cos th, sin th sin ph), ось цикла — y:
  omega_y = L_y / I_y                       — закрутка вокруг оси цикла (для шара это точный Лармор -dB_y(0)/2);
  omega   = I^-1 L                           — полный вектор угловой скорости, его угол к оси цикла;
  dp      = -<dA>                            — линейный толчок (на единицу q/m; для шара равен 0 точно).
ph = 0 — ось наклонена к тору цикла, ph = 22,5 — к кольцу.

Запуск: python3 spinup_torus.py [beta_f ...]      (по умолчанию 63.49 65 66.54)
        python3 spinup_torus.py conv              (проверка сходимости по сетке)
Нужны honc_ring_field.py и spinup.py в той же папке.
"""
import importlib.util, numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)


def A(S, X, chunk=300):
    """Векторный потенциал сегментов S в точках X (кулоновская калибровка)."""
    mid, dl = S; X = np.atleast_2d(X); out = np.zeros_like(X)
    for s in range(0, len(X), chunk):
        R = np.linalg.norm(X[s:s + chunk, None, :] - mid[None], axis=2)
        out[s:s + chunk] = (dl[None] / R[..., None]).sum(1)
    return out


def torus_local(n=90):
    a = b = 0.5
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / n,
                       np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / n)
    # ось тора — локальная z
    P = np.stack([(a + b * np.cos(v)) * np.cos(u), (a + b * np.cos(v)) * np.sin(u), b * np.sin(v)], -1).reshape(-1, 3)
    w = (a + b * np.cos(v)).reshape(-1)
    return P, w / w.sum()


def orient(P, th_deg, ph_deg):
    th, ph = np.radians(th_deg), np.radians(ph_deg)
    nax = np.array([np.sin(th) * np.cos(ph), np.cos(th), np.sin(th) * np.sin(ph)])
    e1 = np.cross(nax, [0.0, 0.0, 1.0]) if abs(nax[2]) < 0.9 else np.cross(nax, [1.0, 0.0, 0.0])
    e1 /= np.linalg.norm(e1); e2 = np.cross(nax, e1)
    return P[:, :1] * e1 + P[:, 1:2] * e2 + P[:, 2:] * nax


def response(P, w, dS):
    dA = A(dS, P)
    L = -(w[:, None] * np.cross(P, dA)).sum(0)
    r2 = (P ** 2).sum(1)
    I = (w[:, None, None] * (r2[:, None, None] * np.eye(3) - P[:, :, None] * P[:, None, :])).sum(0)
    om = np.linalg.solve(I, L)
    dp = -(w[:, None] * dA).sum(0)
    return L[1] / I[1, 1], om, dp


def delta_segments(bf, n=2000):
    """dA = A(beta_f) - A(0) одним вызовом: сегменты конечной сборки плюс начальные с обратным знаком."""
    m1, d1 = h.segments(h.build(8, bf), n)
    m0, d0 = h.segments(h.build(8, 0), n)
    return np.concatenate([m1, m0]), np.concatenate([d1, -d0])


if __name__ == '__main__':
    if sys.argv[1:2] == ['conv']:
        dS = delta_segments(65, 2000)
        for n in (60, 90, 140):
            P0, w = torus_local(n)
            print(f"grid {n}: ", ' | '.join(f"th={th}: omega_y={response(orient(P0, th, 0), w, dS)[0]:+.4f}"
                                            for th in (0, 90)), flush=True)
        sys.exit(0)
    P0, w = torus_local(90)
    for bf in [float(x) for x in (sys.argv[1:] or ['63.49', '65', '66.54'])]:
        dS = delta_segments(bf)
        dB = h.field(dS, [[0, 0, 0]])[0, 1]
        print(f"beta_f = {bf}: Larmor (шар) omega_y = -dB_y(0)/2 = {-dB / 2:+.4f}", flush=True)
        for ph in (0.0, 22.5):
            for th in (0, 30, 45, 60, 90):
                if th == 0 and ph > 0:
                    continue
                oy, om, dp = response(orient(P0, th, ph), w, dS)
                tilt = np.degrees(np.arccos(abs(om[1]) / np.linalg.norm(om)))
                print(f"   th={th:2d} ph={ph:4.1f}: omega_y={oy:+.4f}  |omega|={np.linalg.norm(om):.4f} "
                      f"(угол к оси цикла {tilt:4.1f})  dp=({dp[0]:+.4f}, {dp[1]:+.4f}, {dp[2]:+.4f})", flush=True)
