import numpy as np
import matplotlib.pyplot as plt

# Soru 2: parçalı x(t) * kapı h(t)=u(t)-u(t-1)
def x(t):
    return np.where((t > -1) & (t < 0), -1.0,
           np.where((t > 0) & (t < 1), 2.0,
           np.where((t > 1) & (t < 2), 1.0, 0.0)))

def y(t):
    return np.where(t <= -1, 0.0,
           np.where(t <= 0, -(t + 1),
           np.where(t <= 1, 3 * t - 1,
           np.where(t <= 3, 3 - t, 0.0))))

t = np.linspace(-2, 4, 2000)
fig, ax = plt.subplots(1, 3, figsize=(11, 3.2))
ax[0].plot(t, x(t), color="#c0392b", lw=2); ax[0].set_title(r"$x(t)$")
ax[1].plot(t, np.where((t >= 0) & (t <= 1), 1.0, 0.0), color="#2980b9", lw=2)
ax[1].set_title(r"$h(t)=u(t)-u(t-1)$")
ax[2].plot(t, y(t), color="#1a1a2e", lw=2.2)
ax[2].fill_between(t, 0, y(t), color="#1a1a2e", alpha=0.12)
ax[2].set_title(r"$y(t)=x*h$")
for a in ax:
    a.axhline(0, color="0.6", lw=0.8); a.axvline(0, color="0.6", lw=0.8)
    a.grid(True, ls="--", alpha=0.35); a.set_xlabel(r"$t$"); a.set_ylim(-1.6, 2.4)
fig.tight_layout()
fig.savefig("../ss-q2-konv.png", dpi=130, bbox_inches="tight")
