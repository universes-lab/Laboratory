"""Пересчёт строки Qb в таблицах закрутки (spinup_quad.py) после поправки 22.10.

Qb: тор поперёк вертикали (ось e1); кольцо по положению перпендикулярно тору (меридиональная плоскость),
вращается вокруг диаметра, параллельного оси тора. Ось симметрии кольца n = cos(phi) v + sin(phi) e2 лежит в
плоскости, перпендикулярной e1; в замороженном пределе фаза phi — случайная. Заряд несёт тор (мост), кольцо — массу.
Прежняя строка ставила кольцо соосно тору (тело Qs) — снято.
Запуск: python3 qb_row.py
"""
import numpy as np, sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import spinup_quad as Q

TP, SP = Q.torus_local(), Q.sphere_pts()
mu, q = 16 / 65, -1 / 3


def qb(v, e1, phi, B0, c):
    e2 = np.cross(v, e1)
    n_ring = np.cos(phi) * v + np.sin(phi) * e2
    L = q * Q.dL(Q.place(TP[0], e1), TP[1], B0, c)
    I = mu * (Q.I_torus(e1) + Q.I_ring(n_ring))
    return np.linalg.solve(I, L)


for bf in (63.49, 65.0):
    B0, c = Q.field_params(bf)
    y = np.array([0, 1.0, 0]); x = np.array([1.0, 0, 0])
    om = np.array([qb(y, x, ph, B0, c)[1] for ph in np.linspace(0, np.pi, 181)])
    qt = Q.quantron(Q.TYPES[4], y, x, B0, c, TP, SP)[1][1]
    print(f"beta_f={bf}: вертикаль вдоль оси цикла: Qb omega_y от {om.min():+.3f} до {om.max():+.3f}, среднее по фазе {om.mean():+.3f}; "
          f"-1/2*Qt = {-qt/2:+.3f}")
    rng = np.random.default_rng(7)
    V = rng.normal(size=(4000, 3)); V /= np.linalg.norm(V, axis=1)[:, None]
    oy, oc = [], []
    for v in V:
        e = np.cross(v, rng.normal(size=3)); e /= np.linalg.norm(e)
        ph = rng.uniform(0, 2 * np.pi)
        oy.append(qb(v, e, ph, B0, c)[1])
        oc.append(Q.quantron(Q.TYPES[3], v, e, B0, c, TP, SP)[1][1])
    oy, oc = np.array(oy), np.array(oc)
    print(f"   изотропно: Qb среднее {oy.mean():+.3f} ± {oy.std():.3f}, от {oy.min():+.3f} до {oy.max():+.3f}; "
          f"-1/2*Qc: {-oc.mean()/2:+.3f} ± {oc.std()/2:.3f}")
