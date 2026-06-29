import numpy as np
import matplotlib.pyplot as plt

# Soru 2c: x(2-t) -- önce yansıt sonra +2 kaydır
# x(tau): -1 (-1,0), 2 (0,1), 1 (1,2)  ->  x(2-t): -1 (2,3), 2 (1,2), 1 (0,1)
def x2mt(t):
    return np.where((t > 0) & (t < 1), 1.0,
           np.where((t > 1) & (t < 2), 2.0,
           np.where((t > 2) & (t < 3), -1.0, 0.0)))

t = np.linspace(-1, 4, 2000)
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.plot(t, x2mt(t), color="#8e44ad", lw=2.2)
ax.fill_between(t, 0, x2mt(t), color="#8e44ad", alpha=0.12)
ax.axhline(0, color="0.6", lw=0.8); ax.axvline(0, color="0.6", lw=0.8)
ax.grid(True, ls="--", alpha=0.35); ax.set_xlabel(r"$t$")
ax.set_title(r"$x(2-t)$ (yansıma + 2 birim kaydırma)")
ax.set_ylim(-1.6, 2.4); ax.set_xticks([-1, 0, 1, 2, 3, 4])
fig.tight_layout()
fig.savefig("../ss-q2c-yansima.png", dpi=130, bbox_inches="tight")
