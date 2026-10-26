"""Ревизия вращений (Интегратор, 26.10, п. II): наибольшая скорость точки части при двух вращениях —
основном (вокруг оси симметрии, ω) и дополнительном (вокруг диаметра, Ω). R = 1 (внешний радиус), C = 1.
Кольцо радиуса 1; рогатый тор a = b = 1/2. Скорость v = ω·ẑ × r + Ω·x̂ × r.
Плюс восстановление 0,707 и формула равного деления при весах I1, I2.
Запуск: python3 rot_budget.py"""
import numpy as np
th, ph = np.meshgrid(np.linspace(0, 2*np.pi, 721), np.linspace(0, 2*np.pi, 721))
a = b = 0.5
rho = a + b*np.cos(th); X, Y, Zc = rho*np.cos(ph), rho*np.sin(ph), b*np.sin(th)
t = np.linspace(0, 2*np.pi, 3601); rx, ry, rz = np.cos(t), np.sin(t), 0*t
def vmax(x, y, z, w, W):
    vx, vy, vz = -w*y, w*x - W*z, W*y
    return np.sqrt(vx**2 + vy**2 + vz**2).max()
print("ω, Ω  | кольцо: max|v|, √(ω²+Ω²) | тор: max|v|")
for w, W in ((1, 0), (0, 1), (1, 1), (0.6, 0.8), (0.8, 0.6), (1/np.sqrt(2), 1/np.sqrt(2))):
    print(f"{w:.3f}, {W:.3f} | {vmax(rx, ry, rz, w, W):.4f}, {np.hypot(w, W):.4f} | {vmax(X, Y, Zc, w, W):.4f}")
v1, v2 = 1/np.sqrt(3), np.sqrt(2/3)
print(f"\n0,707: равные веса → √((v1² + v2²)/2) = {np.sqrt((v1**2 + v2**2)/2):.4f}; арифметическое среднее {((v1 + v2)/2):.4f}")
for I1, I2, nm in ((1, 1, "равные веса"), (1, 5/8, "кольцо 1, тор 5/8 (оси симметрии)"), (1/2, 7/16, "кольцо 1/2, тор 7/16 (диаметры)")):
    print(f"   {nm}: v_eq = √((I1·v1² + I2·v2²)/(I1 + I2)) = {np.sqrt((I1*v1**2 + I2*v2**2)/(I1 + I2)):.4f}")
