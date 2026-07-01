import numpy as np
import matplotlib.pyplot as plt

# Final S2: x[n]=3cos(pi n/4)+2sin(pi n/2)
# 3cos -> 1.5 e^{+jpi/4 n} + 1.5 e^{-jpi/4 n}   (faz 0)
# 2sin -> -j e^{+jpi/2 n} + j e^{-jpi/2 n}        (faz -pi/2 / +pi/2)
w = np.array([-np.pi/2, -np.pi/4, np.pi/4, np.pi/2])
mag = np.array([1.0, 1.5, 1.5, 1.0])
phase = np.array([np.pi/2, 0.0, 0.0, -np.pi/2])

fig, ax = plt.subplots(1, 2, figsize=(9.4, 3.6))
ax[0].stem(w, mag, basefmt=" ", linefmt="#c0392b", markerfmt="o")
ax[0].set_title(r"Genlik spektrumu $|c_k|$")
ax[0].set_ylim(0, 1.9)
ax[1].stem(w, phase, basefmt=" ", linefmt="#2980b9", markerfmt="s")
ax[1].set_title(r"Faz spektrumu $\angle c_k$ (rad)")
ax[1].set_yticks([-np.pi/2, 0, np.pi/2])
ax[1].set_yticklabels([r"$-\pi/2$", r"$0$", r"$+\pi/2$"])
for a in ax:
    a.axhline(0, color="0.6", lw=0.8); a.grid(True, ls="--", alpha=0.35)
    a.set_xlabel(r"$\omega$ (rad/örnek)")
    a.set_xticks(w)
    a.set_xticklabels([r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$"])
fig.tight_layout()
fig.savefig("../ssi-f-s2-spektrum.png", dpi=130, bbox_inches="tight")
