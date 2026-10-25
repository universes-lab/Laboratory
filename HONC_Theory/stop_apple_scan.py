"""Продолжение stop_apple.py: (1) упор β*(n) по сетке ориентаций оси Q1 (тело — рогатый тор, ограничения A-5 и A-14(4));
(2) влияние собственного кольца Q1 (A-14(4): 1D кольцо Q1 не входит в тела торов глюона; контакт 1D–1D не учитывается, З-7):
экваториальное (Qs) и меридиональное под углом α вокруг оси Q1.
Запуск: python3 stop_apple_scan.py"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('s', 'stop_apple.py')
src = open('stop_apple.py').read().split('betas = np.round')[0]; exec(src)
betas = np.round(np.arange(63.0, 71.31, 0.1), 2); cache = {b: geom(b, 900) for b in betas}
def ring_ok(b, ring):
    R, C = cache[b]; return min(np.min(np.linalg.norm(ring[:, None] - c[None], axis=2)) for c in C) >= 0.5
def stop(f):
    last = None
    for b in betas:
        if f(b): last = b
        elif last is not None: break
    return last
res = []
for th in np.radians(np.arange(0, 91, 15)):            # угол оси Q1 от оси сборки y
    for az in np.radians(np.arange(0, 46, 7.5)):       # азимут в плоскости xz от направления на тор 0
        n = np.array([np.sin(th) * np.cos(az), np.cos(th), np.sin(th) * np.sin(az)])
        res.append((np.degrees(th), np.degrees(az), stop(lambda b: ok(b, n, cache[b])[0])))
        if th == 0: break
v = np.array([r[2] for r in res])
print(f"(1) тело Q1 — рогатый тор, {len(res)} ориентаций оси: упор β* от {v.min():.1f}° до {v.max():.1f}°; "
      f"при 66,5° ± 0,1 — {np.sum(np.abs(v - 66.5) < 0.15)} из {len(v)}")
for th, az, s in res:
    if s > 66.6: print(f"    ось под {th:.0f}° к оси сборки, азимут {az:.1f}°: β* = {s:.1f}°")
print("(2) с собственным кольцом Q1:")
for nm, n in (("ось вдоль оси сборки", np.array([0, 1.0, 0])), ("ось ⟂, между торами", np.array([np.cos(np.pi/8), 0, np.sin(np.pi/8)]))):
    n = n / np.linalg.norm(n); e1, e2 = perp(n)
    base = stop(lambda b: ok(b, n, cache[b])[0])
    rings = {"экваториальное (Qs)": circle(np.zeros(3), e1, e2, 1.0, 600)}
    for al in (0, 45, 90):
        a = np.radians(al); w = np.cos(a) * e1 + np.sin(a) * e2; rings[f"меридиональное, α = {al}°"] = circle(np.zeros(3), w, n, 1.0, 600)
    out = ", ".join(f"{k}: {stop(lambda b: ok(b, n, cache[b])[0] and ring_ok(b, r))}°" for k, r in rings.items())
    print(f"   {nm} (тело — {base}°): {out}")
