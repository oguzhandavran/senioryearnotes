import numpy as np
import matplotlib.pyplot as plt

# Final S5: x[n]=(0.4)^n u[n] + (-2)^n u[-n-1]
# kutup 0.4 (nedensel, ROC disi) ve -2 (anti-nedensel, ROC ici)
# ROC: 0.4 < |z| < 2 (halka). Birim cember halkanin icinde -> DTFT var.
fig, ax = plt.subplots(figsize=(5.6, 5.6))
th = np.linspace(0, 2*np.pi, 400)

# ROC halkasi (yesil dolgu)
r_in, r_out = 0.4, 2.0
ax.fill(np.cos(th)*r_out, np.sin(th)*r_out, color="#2ecc71", alpha=0.18)
ax.fill(np.cos(th)*r_in, np.sin(th)*r_in, color="white")
ax.plot(np.cos(th)*r_in, np.sin(th)*r_in, "g--", lw=1.2)
ax.plot(np.cos(th)*r_out, np.sin(th)*r_out, "g--", lw=1.2)

# birim cember
ax.plot(np.cos(th), np.sin(th), color="0.4", lw=1.4, ls=":")
ax.annotate("birim çember\n|z|=1", (np.cos(2.4), np.sin(2.4)),
            textcoords="offset points", xytext=(-6, 6), fontsize=8, color="0.3")

# kutuplar (x) ve sifir (o)
ax.plot(0.4, 0, "x", ms=12, mew=3, color="#c0392b")
ax.plot(-2.0, 0, "x", ms=12, mew=3, color="#c0392b")
ax.annotate(r"$z=0.4$", (0.4, 0), textcoords="offset points", xytext=(4, 8), fontsize=10)
ax.annotate(r"$z=-2$", (-2.0, 0), textcoords="offset points", xytext=(4, 8), fontsize=10)

ax.axhline(0, color="0.7", lw=0.8); ax.axvline(0, color="0.7", lw=0.8)
ax.set_title(r"ROC: $0.4<|z|<2$ (halka) — birim çember içeride $\Rightarrow$ DTFT var")
ax.set_xlabel("Re(z)"); ax.set_ylabel("Im(z)")
ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6)
ax.set_aspect("equal"); ax.grid(True, ls="--", alpha=0.3)
fig.tight_layout()
fig.savefig("../ssi-f-s5-roc.png", dpi=130, bbox_inches="tight")
