import numpy as np
import matplotlib.pyplot as plt

# Soru 3: üçgen x(t) * dikdörtgen h(t) -> parçalı parabol y(t)
def x(t):
    return np.where(np.abs(t) <= 1, 1 - np.abs(t), 0.0)

def y(t):
    return np.where(t < -1.5, 0.0,
           np.where(t < -0.5, 0.5 * (t + 1.5) ** 2,
           np.where(t <= 0.5, 0.75 - t ** 2,
           np.where(t <= 1.5, 0.5 * (t - 1.5) ** 2, 0.0))))

t = np.linspace(-2.5, 2.5, 2000)
fig, ax = plt.subplots(1, 3, figsize=(11, 3.2))
ax[0].plot(t, x(t), color="#c0392b", lw=2); ax[0].set_title(r"$x(t)=1-|t|$ (üçgen)")
ax[1].plot(t, np.where(np.abs(t) <= 0.5, 1.0, 0.0), color="#2980b9", lw=2)
ax[1].set_title(r"$h(t)$ (dikdörtgen, genişlik 1)")
ax[2].plot(t, y(t), color="#1a1a2e", lw=2.2)
ax[2].fill_between(t, 0, y(t), color="#27ae60", alpha=0.2)
ax[2].set_title(r"$y(t)$: köşeler yumuşadı (parabol)")
for a in ax:
    a.axhline(0, color="0.6", lw=0.8); a.axvline(0, color="0.6", lw=0.8)
    a.grid(True, ls="--", alpha=0.35); a.set_xlabel(r"$t$"); a.set_ylim(-0.1, 1.1)
fig.tight_layout()
fig.savefig("../ss-q3-ucgen.png", dpi=130, bbox_inches="tight")
