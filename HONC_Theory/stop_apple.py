"""Правило 2, кандидат «остаточный β»: зависит ли упор замыкания глюона от ориентации Q1, если Q1 — не шар (мост этапов А/Б),
а рогатый тор (A-3, A-5). Канонные ограничения: тор–тор не проникают (A-5): средние окружности Q1 и тора глюона не ближе 1;
кольцо в тело не входит (A-14(4)): точки колец глюона вне тела Q1 ((ρ − ½)² + z² ≥ ¼ относительно оси n).
Кольцо Q1 (1D) в упор не включено: контакт 1D–1D не определён (З-7). Q1 в центре камеры, ось n.
Для сравнения — шар радиуса 1 (мост): упор 66,54°.
Запуск: python3 stop_apple.py"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
def circle(c, e1, e2, r, n=400):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False); return c + r * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))
def perp(v):
    v = v / np.linalg.norm(v); a = np.array([1.0, 0, 0]) if abs(v[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(v, a); e1 /= np.linalg.norm(e1); return e1, np.cross(v, e1)
def geom(b, nr=1500):
    g = h.build(8, b); t = np.linspace(0, 2 * np.pi, nr, endpoint=False)
    R = np.vstack([r['C'] + np.outer(r['p'] * np.cos(t), r['u']) + np.outer(r['q'] * np.sin(t), r['W']) for r in g['rings']])
    C = [circle(np.array(A), *perp(np.array(T)), 0.5) for A, T in zip(g['A'], g['T'])]
    return R, C
def ok(b, n, G=None):
    R, C = G if G is not None else geom(b); n = n / np.linalg.norm(n); core = circle(np.zeros(3), *perp(n), 0.5)
    z = R @ n; rho = np.linalg.norm(R - np.outer(z, n), axis=1); ring_ok = np.min((rho - 0.5) ** 2 + z ** 2) >= 0.25
    tor = min(np.min(np.linalg.norm(core[:, None] - c[None], axis=2)) for c in C); return ring_ok and tor >= 1.0, ring_ok, tor
def ball_ok(b, G=None):
    R, C = G if G is not None else geom(b)
    return np.min(np.linalg.norm(R, axis=1)) >= 1.0 and min(np.min(np.linalg.norm(c, axis=1)) for c in C) >= 1.5
betas = np.round(np.arange(63.0, 71.31, 0.1), 2); cache = {b: geom(b) for b in betas}
def stop(f):
    last = None
    for b in betas:
        if f(b): last = b
        elif last is not None: break
    return last
print(f"шар радиуса 1 (мост этапов А/Б): упор ≈ {stop(lambda b: ball_ok(b, cache[b]))}°")
Y = np.array([0, 1.0, 0]); X = np.array([1.0, 0, 0]); Z = np.array([0, 0, 1.0])
for nm, n in (("ось Q1 вдоль оси сборки (y)", Y), ("ось Q1 ⟂ оси сборки, на центр тора (x)", X),
              ("ось Q1 ⟂ оси сборки, между торами (поворот x на 22,5° вокруг y)", np.array([np.cos(np.pi/8), 0, np.sin(np.pi/8)])),
              ("ось Q1 под 45° к оси сборки", (X + Y) / np.sqrt(2))):
    s = stop(lambda b: ok(b, n, cache[b])[0])
    _, r_ok, tor = ok(s + 0.1 if s and s < 71.3 else s, n, geom(min(s + 0.1, 71.3))) if s else (None, None, None)
    print(f"{nm}: упор ≈ {s}°; что упирается сразу после: {'кольцо глюона в тело Q1' if r_ok is False else ''}"
          f"{'' if tor is None or tor >= 1 else f' тор глюона в тор Q1 (средние окружности {tor:.3f})'}")
print("предел пустой сборки (касание колец): 71,30°")
