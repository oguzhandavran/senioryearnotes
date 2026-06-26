#!/usr/bin/env python3
# Otomatik Kontrol 01 — 2. derece sistemin birim adım yanıtı (sönüm oranı karşılaştırması)
# Üretir: _assets/ok01-birim-adim-yaniti.png
# Çalıştırma (vault kökünden): python3 _assets/scripts/ok01-birim-adim-yaniti.py
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "_assets/ok01-birim-adim-yaniti.png"
wn = 5.0                       # doğal frekans [rad/s]
t = np.linspace(0, 4, 600)
egriler = [
    (0.2, "#c0392b", r"$\zeta=0.2$  (%OS$\approx$52%)"),
    (0.5, "#e67e22", r"$\zeta=0.5$  (%OS$\approx$16%)"),
    (0.7, "#2980b9", r"$\zeta=0.7$  (%OS$\approx$5%)"),
    (1.0, "#27ae60", r"$\zeta=1.0$  (kritik sönüm)"),
]

fig, ax = plt.subplots(figsize=(7, 4))
for z, renk, etiket in egriler:
    if z < 1:                  # az sönümlü
        wd = wn * np.sqrt(1 - z**2)
        phi = np.arccos(z)
        y = 1 - np.exp(-z*wn*t) / np.sqrt(1 - z**2) * np.sin(wd*t + phi)
    else:                      # kritik sönüm
        y = 1 - np.exp(-wn*t) * (1 + wn*t)
    ax.plot(t, y, color=renk, lw=2, label=etiket)

ax.axhline(1.0, color="0.5", lw=0.8)
ax.set_title(r"Birim Adım Yanıtı — $\omega_n = 5$ rad/s")
ax.set_xlabel("t (s)")
ax.set_ylabel("y(t)")
ax.set_ylim(0, 1.6)
ax.grid(True, ls="--", alpha=0.4)
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("yazıldı:", OUT)
