#!/usr/bin/env python3
# MST Final S1 — G(s)=K/[(s+1)(s+2)(s+3)] kök yer eğrisi (gerçek hesap)
# Üretir: _assets/mst06-kye.png
# Çalıştırma (vault kökünden): python3 _assets/scripts/mst06-kye.py
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "_assets/mst06-kye.png"
poles = [-1, -2, -3]
Ks = np.concatenate([np.linspace(0, 6, 800), np.linspace(6, 300, 2000)])
roots = np.array([np.roots([1, 6, 11, 6 + K]) for K in Ks])  # s^3+6s^2+11s+(6+K)

fig, ax = plt.subplots(figsize=(6, 5))
allr = roots.flatten()
ax.scatter(allr.real, allr.imag, s=2, color="#1a1a2e", label="KYE dalları")
ax.plot(poles, [0, 0, 0], "x", color="#c0392b", ms=11, mew=2, label="kutuplar")
ax.plot(-2, 0, "o", color="gray", ms=5)
ax.annotate(r"$\sigma_a=-2$", (-2, 0), xytext=(0, 9), textcoords="offset points",
            ha="center", color="gray", fontsize=8)
ax.axhline(0, color="0.6", lw=0.8)
ax.axvline(0, color="0.6", lw=0.8)
ax.set_xlabel(r"$\sigma$")
ax.set_ylabel(r"$j\omega$")
ax.set_title(r"Kök Yer Eğrisi: $G(s)=\dfrac{K}{(s+1)(s+2)(s+3)}$")
ax.grid(True, ls="--", alpha=0.3)
ax.set_xlim(-6, 2)
ax.set_ylim(-4, 4)
ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("yazıldı:", OUT)
