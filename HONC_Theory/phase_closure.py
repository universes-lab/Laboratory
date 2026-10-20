"""ТФ-1, модель М2 (состояние бежит по кольцу равномерно): фазовое замыкание λ-цикла.

delta(beta) — доля пути по кольцу от отверстия тора i до отверстия тора i+1 (по направлению обхода).
Два условия:
  (а) у каждого тора прохождения двух колец цикла разнесены ровно на треть периода (знак s_i = ±1):
      N*delta + (1/3)*sum(s_i) ≡ 0 (mod 1)  ->  N*delta ≡ k/3 (mod 1);
  (б) общая свободная треть у всех торов (прохождения привязаны к одним и тем же двум третям):
      delta ≡ ±1/3 (mod 1), при этом N любое.
Для встречного обхода (чередование) сумма задержек по циклу целая, условие (а) выполняется при любом beta.

Запуск: python3 phase_closure.py
"""
import importlib.util, numpy as np, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'honc_ring_field.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)


def delta(N, beta, n=None):
    """Точная доля пути: углы отверстий на эллипсе и интеграл длины дуги (scipy.quad)."""
    from scipy.integrate import quad
    g = h.build(N, beta); r = g['rings'][0]
    C, u, W, p, q = r['C'], r['u'], r['W'], r['p'], r['q']
    ang = lambda X: np.arctan2(((np.array(X) - C) @ W) / q, ((np.array(X) - C) @ u) / p) % (2 * np.pi)
    speed = lambda s: np.sqrt(p * p * np.sin(s) ** 2 + q * q * np.cos(s) ** 2)
    L = quad(speed, 0, 2 * np.pi, limit=200)[0]
    t0, t1 = ang(g['A'][0]), ang(g['A'][1])
    if r['Om'] > 0:          # обход по возрастанию t: от t0 вперёд до t1
        a, b = t0, t1 if t1 > t0 else t1 + 2 * np.pi
    else:                    # обход по убыванию t: от t0 назад до t1
        a, b = t1, t0 if t0 > t1 else t0 + 2 * np.pi
    return quad(speed, a, b, limit=200)[0] / L


def roots(N, bmax, targets):
    bs = np.linspace(0, bmax, 200); ds = np.array([delta(N, b) for b in bs])
    out = []
    for tgt in targets:
        f = ds - tgt
        for k in range(len(bs) - 1):
            if f[k] == 0 or f[k] * f[k + 1] < 0:
                lo, hi = bs[k], bs[k + 1]
                for _ in range(45):
                    m = (lo + hi) / 2
                    lo, hi = (lo, m) if (delta(N, lo) - tgt) * (delta(N, m) - tgt) <= 0 else (m, hi)
                out.append((tgt, (lo + hi) / 2))
    return sorted(out, key=lambda x: x[1])


if __name__ == '__main__':
    for N, bmax in ((8, 71.30), (4, 50.67), (2, 0.0)):
        print(f"N={N}: delta(0)={delta(N, 0):.4f}" + (f", delta(bmax={bmax})={delta(N, bmax):.4f}" if bmax else " (Z жёсткий, delta = 1/2 всегда)"))
        if not bmax:
            print("   (а): 2*delta = 1 ≡ 0 — выполнено; (б): delta = 1/2 ≠ ±1/3 — общей свободной трети нет")
            continue
        ta = [k / (3 * N) for k in range(int(1.5 * N), int(2.4 * N) + 1)]   # delta = k/(3N) в диапазоне 0,5…0,8
        ra = [(t, b) for t, b in roots(N, bmax, ta)]
        print("   (а) N*delta ≡ k/3: ", ', '.join(f"delta={round(t*3*N)}/{3*N} при beta={b:.2f}" for t, b in ra))
        rb = roots(N, bmax, [2 / 3])
        print("   (б) delta ≡ ±1/3:  ", ', '.join(f"beta={b:.2f}" for t, b in rb) if rb else "нет решений в допустимом диапазоне")
        if N == 8:
            print("   окно захвата 63,49–66,54°: delta =", f"{delta(8, 63.49):.4f}–{delta(8, 66.54):.4f}")
