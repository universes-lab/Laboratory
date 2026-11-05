"""Оценка (класс В) величин прежнего выборочного ядра по записям нового протокола.
Не сертификат. Цель — проверить предположение [Г], что расхождения 0,0057 и 0,0325 — разница определений.
Определения прежнего ядра (qfnode/core.js, check()):
  касп:  min по точкам кольца на расстоянии >= 0,12 от центра своего тора: dist(X, средняя окружность) - 0,5
  кольцо-кольцо: min |X - Y| по точкам двух колец, кроме точек ближе 0,25 к общему центру тора
Запуск: python3 old_definitions.py protocol_K4.json [N]"""
import json, math, sys
p = json.load(open(sys.argv[1])); N = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
mid = lambda v: [(a + b) / 2 for a, b in v]
tori = {t['name']: (mid(t['A']), mid(t['T'])) for t in p['configuration']['tori']}
rings = {r['name']: r for r in p['configuration']['rings']}
def pts(r, n):
    C, E1, E2 = mid(r['C']), mid(r['E1']), mid(r['E2']); a, b = sum(r['s1']) / 2, sum(r['s2']) / 2
    return [[C[k] + a * math.cos(2 * math.pi * i / n) * E1[k] + b * math.sin(2 * math.pi * i / n) * E2[k] for k in range(3)] for i in range(n)]
def dmid(X, A, T):
    r = [X[k] - A[k] for k in range(3)]; z = sum(r[k] * T[k] for k in range(3))
    rho = math.sqrt(max(sum(r[k] ** 2 for k in range(3)) - z * z, 0)); return math.hypot(rho - 0.5, z)
P = {nm: pts(r, N) for nm, r in rings.items()}
owners = {nm: [x for x in rings[nm]['threads']] for nm in rings}
print('owners', owners)
for nm, X in P.items():
    for tn in owners[nm]:
        A, T = tori[tn]
        m = min(dmid(x, A, T) - 0.5 for x in X if math.dist(x, A) >= 0.12)
        print(f'касп (0,12): {nm}:{tn}  {m:.5f}')
names = sorted(rings)
M = max(2000, N // 10); Q = {nm: pts(rings[nm], M) for nm in names}
for i, a in enumerate(names):
    for b in names[i + 1:]:
        sh = [tori[t][0] for t in owners[a] if t in owners[b]]
        far = lambda x: all(math.dist(x, S) >= 0.25 for S in sh)
        A_ = [x for x in Q[a] if far(x)]; B_ = [y for y in Q[b] if far(y)]
        if not A_ or not B_: continue
        import numpy as np
        m = float(np.sqrt(((np.array(A_)[:, None, :] - np.array(B_)[None, :, :]) ** 2).sum(-1)).min())
        if m < 1.0: print(f'кольцо–кольцо (0,25): {a}–{b}  {m:.5f}  общие торы {[t for t in owners[a] if t in owners[b]]}')

# Выборка прежнего ядра: 240 точек на кольце (RS), сдвиг фазы выборки — диапазон значений
def phased(r, n, ph):
    C, E1, E2 = mid(r['C']), mid(r['E1']), mid(r['E2']); a, b = sum(r['s1']) / 2, sum(r['s2']) / 2
    return [[C[k] + a * math.cos(2 * math.pi * (i + ph) / n) * E1[k] + b * math.sin(2 * math.pi * (i + ph) / n) * E2[k] for k in range(3)] for i in range(n)]
import numpy as np
for nm, tn in [('RH1', 'T2'), ('RH1', 'H1'), ('R1', 'T2')]:
    A, T = tori[tn]; vals = []
    for ph in np.linspace(0, 1, 101)[:-1]:
        X = phased(rings[nm], 240, ph); vals.append(min(dmid(x, A, T) - 0.5 for x in X if math.dist(x, A) >= 0.12))
    print(f'касп, выборка 240, по фазам: {nm}:{tn}  [{min(vals):.5f}; {max(vals):.5f}]  при фазе 0: {vals[0]:.5f}')
for a, b in [('R1', 'RH1'), ('R2', 'RH1')]:
    S = tori['T2'][0]; vals = []
    for ph in np.linspace(0, 1, 41)[:-1]:
        A_ = np.array([x for x in phased(rings[a], 240, ph) if math.dist(x, S) >= 0.25])
        for ph2 in np.linspace(0, 1, 11)[:-1]:
            B_ = np.array([y for y in phased(rings[b], 240, ph2) if math.dist(y, S) >= 0.25])
            vals.append(float(np.sqrt(((A_[:, None] - B_[None]) ** 2).sum(-1)).min()))
    print(f'кольцо–кольцо, выборка 240×240, по фазам: {a}–{b}  [{min(vals):.5f}; {max(vals):.5f}]')
for nm in ['R1', 'RH1']: print(nm, 'полуоси', sum(rings[nm]['s1']) / 2, sum(rings[nm]['s2']) / 2)
