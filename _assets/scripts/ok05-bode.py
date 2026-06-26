#!/usr/bin/env python3
# Otomatik Kontrol 05 — G(s)=10/[s(s+1)(s+5)] Bode diyagramı (PM/GM işaretli)
# Üretir: _assets/ok05-bode.png
# Çalıştırma (vault kökünden): python3 _assets/scripts/ok05-bode.py
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "_assets/ok05-bode.png"
w = np.logspace(-1, 2, 3000)          # 0.1 .. 100 rad/s
s = 1j * w
G = 10 / (s * (s + 1) * (s + 5))
mag = 20 * np.log10(np.abs(G))
phase = np.unwrap(np.angle(G)) * 180 / np.pi

# Kazanç kesişimi (|G| = 0 dB) ve faz kesişimi (faz = -180°)
i_gc = np.argmin(np.abs(mag));      w_gc = w[i_gc]; pm = 180 + phase[i_gc]
i_pc = np.argmin(np.abs(phase + 180)); w_pc = w[i_pc]; gm = -mag[i_pc]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
fig.suptitle(r"$G(s)=\dfrac{10}{s(s+1)(s+5)}$ — Bode Diyagramı", y=0.98)

ax1.semilogx(w, mag, color="#1a1a2e", lw=2)
ax1.axhline(0, color="0.6", lw=0.8)
ax1.axvline(w_gc, color="#2980b9", ls="--", lw=1)
ax1.plot(w_gc, 0, "o", color="#2980b9")
ax1.annotate(rf"$\omega_{{gc}}$={w_gc:.2f}", (w_gc, 0), textcoords="offset points",
             xytext=(6, 8), color="#2980b9", fontsize=8)
ax1.set_ylabel("Kazanç (dB)")
ax1.grid(True, which="both", ls="--", alpha=0.3)

ax2.semilogx(w, phase, color="#c0392b", lw=2)
ax2.axhline(-180, color="#c0392b", ls=":", lw=1)
ax2.axvline(w_pc, color="#27ae60", ls="--", lw=1)
ax2.plot(w_pc, -180, "o", color="#27ae60")
ax2.annotate(rf"$\omega_{{pc}}$={w_pc:.2f}", (w_pc, -180), textcoords="offset points",
             xytext=(6, 8), color="#27ae60", fontsize=8)
ax2.set_ylabel("Faz (°)")
ax2.set_xlabel(r"$\omega$ (rad/s)")
ax2.grid(True, which="both", ls="--", alpha=0.3)

txt = f"PM = {pm:.0f}°   (ω_gc={w_gc:.2f})\nGM = {gm:.1f} dB   (ω_pc={w_pc:.2f})"
ax1.text(0.02, 0.04, txt, transform=ax1.transAxes, fontsize=8,
         va="bottom", ha="left", bbox=dict(boxstyle="round", fc="white", ec="0.7"))

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("yazıldı:", OUT, "| PM=%.0f° GM=%.1fdB w_gc=%.2f w_pc=%.2f" % (pm, gm, w_gc, w_pc))
