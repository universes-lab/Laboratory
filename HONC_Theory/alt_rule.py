"""Правило «встречно в отверстии» (чередование обходов): что обнуляется точно, а что нет. Глюон, 65°."""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
import spinup_torus as st
bf = float(sys.argv[1]) if len(sys.argv) > 1 else 65.0
def segs(beta, flip, n):
    g = h.build(8, beta)
    if flip:
        for i, r in enumerate(g['rings']): r['Om'] *= (-1 if i % 2 else 1)
    return h.segments(g, n)
for flip in (False, True):
    S1 = segs(bf, flip, 1000); S0 = segs(0, flip, 1000)
    dS = (np.concatenate([S1[0], S0[0]]), np.concatenate([S1[1], -S0[1]]))
    pts = np.array([[0, 0, 0], [0, 0.3, 0], [0.3, 0, 0], [0.5, 0.5, 0], [0, 0, 0.7], [0.7, 0, 0.7]])
    B = h.field(S1, pts)
    name = 'встречно' if flip else 'вместе'
    print(f"{name}: |B| в точках (0,0,0) (0,.3,0) (.3,0,0) (.5,.5,0) (0,0,.7) (.7,0,.7):", np.round(np.linalg.norm(B, axis=1), 3), flush=True)
    P0, w = st.torus_local(40)
    for th, ph in ((0, 0), (90, 0), (90, 22.5), (45, 0)):
        oy, om, dp = st.response(st.orient(P0, th, ph), w, dS)
        print(f"   тор th={th} ph={ph}: omega_y={oy:+.4f} |omega|={np.linalg.norm(om):.4f} |dp|={np.linalg.norm(dp):.4f}", flush=True)
    F = st.orient(P0, 0, 0)  # placeholder to keep API
    # шар: среднее по объёму
    i = np.arange(800) + 0.5; phi = np.arccos(1 - 2*i/800); thh = np.pi*(1 + 5**0.5)*i
    Fb = np.stack([np.sin(phi)*np.cos(thh), np.cos(phi), np.sin(phi)*np.sin(thh)], 1)
    rr = np.linspace(0.05, 0.98, 12); Pb = np.concatenate([r*Fb for r in rr]); wb = np.concatenate([np.full(800, r**2) for r in rr]); wb /= wb.sum()
    oy, om, dp = st.response(Pb, wb, dS)
    print(f"   шар: |omega|={np.linalg.norm(om):.5f}", flush=True)
