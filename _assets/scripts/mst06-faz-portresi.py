#!/usr/bin/env python3
# MST Final — merkez tipi faz portresi: x1²+x2²=r² (Lyapunov anlamında kararlı)
# Üretir: _assets/mst06-faz-portresi.png
# Çalıştırma (vault kökünden): python3 _assets/scripts/mst06-faz-portresi.py
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "_assets/mst06-faz-portresi.png"
th = np.linspace(0, 2*np.pi, 400)
renkler = ["#2980b9", "#27ae60", "#e67e22", "#c0392b", "#8e44ad"]

fig, ax = plt.subplots(figsize=(5, 5))
for r, c in zip([1, 2, 3, 4, 4.7], renkler):
    ax.plot(r*np.cos(th), r*np.sin(th), color=c, lw=1.8)
    ax.annotate("", xy=(0.35, r), xytext=(-0.35, r),
                arrowprops=dict(arrowstyle="->", color=c, lw=1.6))  # saat yönü
ax.plot(0, 0, "o", color="#1a1a2e", ms=5)
ax.axhline(0, color="#1a1a2e", lw=0.8)
ax.axvline(0, color="#1a1a2e", lw=0.8)
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_title(r"Faz Portresi: $x_1^2 + x_2^2 = r^2$ (Lyapunov kararlı)")
ax.set_aspect("equal")
ax.set_xlim(-5.2, 5.2)
ax.set_ylim(-5.2, 5.2)
ax.grid(True, ls="--", alpha=0.3)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("yazıldı:", OUT)
