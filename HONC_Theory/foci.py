"""Этап А: два «фокуса» глюонной сборки — где они в геометрии колец и где в поле [мост].

1. Геометрические фокусы: точки, где оси колец (нормали, по Автору «оси зацеплённых колец») пересекают ось сборки y.
2. Поле колец (Био — Савар, мост A-13) на оси при двух правилах обхода: «вместе» (honc_ring_field) и «встречно».
   Нули и максимумы |B| на оси; сравнение с радиусом квантрона R = 1 (квантрон в центре).
Запуск: python3 foci.py
"""
import importlib.util, numpy as np, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
y = np.array([0, 1.0, 0])

def ring_normal(r):
    n = np.cross(r['u'], r['W']); return n / np.linalg.norm(n)

def geo_foci(N, beta):
    g = h.build(N, beta); out = []
    for r in g['rings']:
        C = r['C']; n = ring_normal(r)
        rad = C - (C @ y) * y; rr = np.linalg.norm(rad); er = rad / rr
        nr = n @ er
        if abs(nr) < 1e-9:
            out.append(np.inf); continue
        t = -rr / nr                                  # точка оси: радиальная координата обнуляется
        P = C + t * n
        out.append(P @ y if np.linalg.norm(P - (P @ y) * y) < 1e-6 else np.nan)
    return out

def segs(N, beta, rule):
    g = h.build(N, beta)
    if rule == 'встречно':
        for i, r in enumerate(g['rings']):
            r['Om'] = r['Om'] * (-1) ** i
    return h.segments(g, 1500)

ys = np.linspace(-3, 3, 601)
P = np.stack([0 * ys, ys, 0 * ys], 1)
print("Геометрические фокусы осей колец, глюон N = 8 (y пересечения оси кольца с осью сборки; по кольцам 0 и 1):")
for b in (5, 15, 30, 45, 61.56, 63.49, 65, 66.54, 71.3):
    f = geo_foci(8, b)
    print(f"   beta = {b:6.2f}: чётные кольца y = {f[0]:+.3f}, нечётные y = {f[1]:+.3f}; одинаковы внутри групп: "
          f"{np.allclose(f[0::2], f[0]) and np.allclose(f[1::2], f[1])}")
f = geo_foci(4, 25.0); print(f"   W (N = 4) при 25°: {f[0]:+.3f} / {f[1]:+.3f}")
print("\nПоле на оси (глюон): нули и максимумы |B|, квантрон радиуса 1 в центре")
for rule in ('вместе', 'встречно'):
    for b in (10, 30, 61.56, 65, 71.3):
        B = h.field(segs(8, b, rule), P)
        By = B[:, 1]; mod = np.linalg.norm(B, axis=1)
        zeros = [round((ys[k] + ys[k + 1]) / 2, 3) for k in range(len(ys) - 1) if By[k] * By[k + 1] < 0]
        k0 = len(ys) // 2
        mx = [round(ys[k], 2) for k in range(1, len(ys) - 1) if mod[k] > mod[k - 1] and mod[k] >= mod[k + 1]]
        print(f"   «{rule}» beta = {b:5.2f}: B_y(0) = {By[k0]:+.3f}; нули B_y на оси: {zeros}; максимумы |B|: {mx} "
              f"(|B| там {[round(float(mod[np.argmin(abs(ys - m))]), 2) for m in mx]})")
