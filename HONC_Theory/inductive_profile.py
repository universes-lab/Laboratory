"""Профиль замыкания из индуктивного затягивания [мост; свод п. 4.6]: форма β(t) без абсолютного масштаба.
I_β·β'' = ½·I²·dL/dβ, без затухания. Время — в единицах τ_L = √(I_β / (½ I²)) (на радиан²).
Квантрон в центре не даёт затянуться дальше 66,54° (упор). Толщина колец a = 0,015.
Запуск: python3 inductive_profile.py"""
import numpy as np, sys, os, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('ri', os.path.join(here, 'ring_inductance.py'))
src = open(os.path.join(here, 'ring_inductance.py')).read().split("a = float(sys.argv[1])")[0]
ns = {'__file__': os.path.join(here, 'ring_inductance.py'), '__name__': 'ri'}; exec(src, ns)
bs = np.arange(0.0, 66.6, 1.5); bs = np.append(bs, 66.54)
L = np.array([sum(ns['L_parts'](b, 0.015, 1000)) for b in bs])
i0 = np.argmin(L[1:-1]) + 1
print("L(β), a = 0,015:", ", ".join(f"{b:.1f}:{v:.1f}" for b, v in zip(bs[::4], L[::4])))
print(f"минимум L при β ≈ {bs[i0]:.1f}°: L = {L[i0]:.1f}; максимум на наклонной ветви при β ≈ {bs[i0:][np.argmax(L[i0:])]:.1f}°; L(66,54) = {L[-1]:.1f}; L(0) = {L[0]:.1f}")
from scipy.interpolate import CubicSpline
cs = CubicSpline(np.radians(bs), L)
def run(b_start, v_start=0.0, tmax=200.0, dt=1e-3):
    b = np.radians(b_start); v = v_start; t = 0.0; marks = {}
    for thr in (35.0, 63.5, 66.54): marks[thr] = None
    while t < tmax:
        a = cs(b, 1)                 # ½I²·dL/dβ / I_β в единицах τ_L
        v += a * dt; b += v * dt; t += dt
        for thr in marks:
            if marks[thr] is None and np.degrees(b) >= thr: marks[thr] = t
        if np.degrees(b) >= 66.54: break
        if b < 0: return marks, 'раскрылось'
    return marks, 'упор' if np.degrees(b) >= 66.54 else 'не дошло'
for bst in (bs[i0] + 0.5, 35.0, 45.0):
    m, res = run(bst)
    t35, t63, t66 = m[35.0], m[63.5], m[66.54]
    tt = (t63 - (t35 if t35 is not None else 0.0)) if t63 else None
    print(f"старт в покое с β = {bst:.1f}°: {res}; t(35°) = {t35 if t35 is None else round(t35, 2)}, t(63,5°) = {t63 if t63 is None else round(t63, 2)}, "
          f"t(66,54°) = {t66 if t66 is None else round(t66, 2)}; доля пути 35°→63,5° по времени: {tt if tt is None else round(tt, 2)} τ_L")
