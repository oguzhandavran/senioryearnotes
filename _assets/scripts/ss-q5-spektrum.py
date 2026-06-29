import numpy as np
import matplotlib.pyplot as plt

# Soru 5: Fourier serisi genlik ve faz spektrumu
n = np.array([-2, -1, 0, 1, 2])
mag = np.array([0.5, 1.0, 1.0, 1.0, 0.5])
phase = np.array([-np.pi/4, 3*np.pi/8, np.pi, -3*np.pi/8, np.pi/4])

fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
ax[0].stem(n, mag, basefmt=" ", linefmt="#c0392b", markerfmt="o")
ax[0].set_title(r"Genlik spektrumu $|c_n|$")
ax[0].set_ylim(0, 1.2)
ax[1].stem(n, phase, basefmt=" ", linefmt="#2980b9", markerfmt="s")
ax[1].set_title(r"Faz spektrumu $\angle c_n$ (rad)")
ax[1].set_yticks([-np.pi/4, np.pi/4, 3*np.pi/8, np.pi])
ax[1].set_yticklabels([r"$-\pi/4$", r"$\pi/4$", r"$3\pi/8$", r"$\pi$"])
for a in ax:
    a.axhline(0, color="0.6", lw=0.8); a.grid(True, ls="--", alpha=0.35)
    a.set_xlabel(r"$n$ (harmonik)"); a.set_xticks(n)
fig.tight_layout()
fig.savefig("../ss-q5-spektrum.png", dpi=130, bbox_inches="tight")
