import numpy as np, sys
sys.argv = ['x']
exec(open('stageA_dynamics.py').read().split('print("1–2.')[0])
exec('def body_points' + open('stageA_dynamics.py').read().split('def body_points')[1].split('for kind in')[0])
for rule in ('вместе', 'встречно'):
    S = segs(65.0, rule)
    for n in (70, 120):
        P0, w = body_points('тор', n)
        for th in (45, 90):
            ax = np.array([np.sin(np.radians(th)), np.cos(np.radians(th)), 0.0]); R = rot_to(ax); Pl = P0 @ R.T
            K = w[:, None] * np.cross(ax, Pl); Bx = B(S, Pl)
            F = np.cross(K, Bx).sum(0); tau = np.cross(Pl, np.cross(K, Bx)).sum(0)
            m = 0.5 * np.cross(Pl, K).sum(0); tpt = np.cross(m, B(S, np.zeros(3))[0])
            print(f"«{rule}» сетка {n}: тор под {th}° в центре: F={np.round(F,4).tolist()}, τ={np.round(tau,4).tolist()}, точечный τ={np.round(tpt,4).tolist()}")
