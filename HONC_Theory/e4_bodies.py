"""Тела при обращённом продевании (Qs): если кольцо Q1 продето через рогатый тор L0, касп L0 лежит на кольце Q1 (расстояние 1 от центра Q1).
Рогатые торы a = b = 1/2: тела (трубки радиуса 1/2 вокруг средних окружностей) не пересекаются ⇔ расстояние между средними окружностями ≥ 1.
(а) Причал до E4: контакт? (б) Касп L0 в (0, 1, 0), ось L0 — любая (сетка по сфере): наибольшее достижимое расстояние между средними окружностями.
(в) Справочно: совместный жёсткий E4 в замкнутой build(8, β) — расстояние между средними окружностями соседей после поворота.
Запуск: python3 e4_bodies.py"""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('h', 'honc_ring_field.py'); h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
def circle(c, e1, e2, r, n=720):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False); return c + r * (np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2))
def perp(v):
    v = v / np.linalg.norm(v); a = np.array([1.0, 0, 0]) if abs(v[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(v, a); e1 /= np.linalg.norm(e1); return e1, np.cross(v, e1)
def Rot(a, ang=np.pi):
    a = np.asarray(a, float) / np.linalg.norm(a); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
dmin = lambda P, Q: np.min(np.linalg.norm(P[:, None] - Q[None], axis=2))
X, Y, Z = np.eye(3); core_Q1 = circle(np.zeros(3), X, Y, 0.5)
print(f"(а) причал до E4: расстояние средних окружностей Q1 и L0 = {dmin(core_Q1, circle(np.array([0, 2.0, 0]), X, Y, 0.5)):.4f} (контакт — 1)")
best = (0, None)
for th in np.linspace(0, np.pi, 61):
    for ph in np.linspace(0, np.pi, 61):
        a = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
        v = dmin(core_Q1, circle(np.array([0, 1.0, 0]), *perp(a), 0.5, 360))
        if v > best[0]: best = (v, a)
print(f"(б) касп L0 на кольце Qs, ось L0 любая: наибольшее расстояние средних окружностей {best[0]:.4f} при оси {np.round(best[1], 3)} — "
      f"{'тела пересекаются при любой оси' if best[0] < 1 else 'есть ось без пересечения'}")
a45 = Rot(np.cos(np.pi / 4) * X + np.sin(np.pi / 4) * Z) @ Z
print(f"    при E4 с φ = 45° (ось L0 → {np.round(a45, 3)}): {dmin(core_Q1, circle(np.array([0, 1.0, 0]), *perp(a45), 0.5)):.4f}")
for b, phs in ((0.0, 30), (71.30, 0)):
    g = h.build(8, b); A = [np.array(x) for x in g['A']]; T = [np.array(x) / np.linalg.norm(x) for x in g['T']]
    cores = [circle(A[i], *perp(T[i]), 0.5) for i in range(8)]; Yh = np.array([0, 1.0, 0]); new = []
    for i in range(8):
        C = g['rings'][i]['C']; d = C - A[i]; dh = d / np.linalg.norm(d); e1 = Yh - (Yh @ dh) * dh; e1 /= np.linalg.norm(e1)
        M = (C + A[i]) / 2; u = np.cos(np.radians(phs)) * e1 + np.sin(np.radians(phs)) * np.cross(dh, e1); new.append((cores[i] - M) @ Rot(u).T + M)
    print(f"(в) build(8, {b:.2f}°): соседи до доворота {dmin(cores[0], cores[1]):.4f}; после совместного E4 (φ = {phs}°) {dmin(new[0], new[1]):.4f}")
