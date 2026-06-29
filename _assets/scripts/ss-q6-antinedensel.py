import numpy as np
import matplotlib.pyplot as plt

# Soru 6: anti-nedensel konvolüsyon  x=u(t)-u(t-2),  h=u(-t)
t = np.linspace(-3, 4, 2000)
x = np.where((t >= 0) & (t <= 2), 1.0, 0.0)
h = np.where(t <= 0, 1.0, 0.0)
y = np.where(t < 0, 2.0, np.where(t < 2, 2 - t, 0.0))

fig, ax = plt.subplots(1, 3, figsize=(11, 3.2))
ax[0].plot(t, x, color="#c0392b", lw=2); ax[0].set_title(r"$x(t)=u(t)-u(t-2)$")
ax[1].plot(t, h, color="#2980b9", lw=2); ax[1].set_title(r"$h(t)=u(-t)$ (anti-nedensel)")
ax[2].plot(t, y, color="#1a1a2e", lw=2.2)
ax[2].fill_between(t, 0, y, color="#8e44ad", alpha=0.15)
ax[2].set_title(r"$y(t)$: $t$'nin sağındaki alan")
for a in ax:
    a.axhline(0, color="0.6", lw=0.8); a.axvline(0, color="0.6", lw=0.8)
    a.grid(True, ls="--", alpha=0.35); a.set_xlabel(r"$t$"); a.set_ylim(-0.3, 2.4)
fig.tight_layout()
fig.savefig("../ss-q6-antinedensel.png", dpi=130, bbox_inches="tight")
