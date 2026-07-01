import numpy as np
import matplotlib.pyplot as plt

# Vize S2: x[n]=5cos(2pi/6 n)=5cos(pi n/3), y[n]=x[4n]=5cos(4pi n/3)=5cos(2pi n/3)
n = np.arange(-10, 10)
x = 5 * np.cos(np.pi * n / 3)            # periyot 6
y = 5 * np.cos(4 * np.pi * n / 3)        # = 5cos(2pi n/3), periyot 3 (4 kat seyreltme)

fig, ax = plt.subplots(2, 1, figsize=(8.4, 5.2), sharex=True)
ax[0].stem(n, x, basefmt=" ", linefmt="#2980b9", markerfmt="o")
ax[0].set_title(r"$x[n]=5\cos(\frac{2\pi}{6}n)$  (temel periyot $N=6$)")
ax[1].stem(n, y, basefmt=" ", linefmt="#c0392b", markerfmt="s")
ax[1].set_title(r"$y[n]=x[4n]=5\cos(\frac{4\pi}{3}n)=5\cos(\frac{2\pi}{3}n)$  (4 kat seyreltme $\Rightarrow$ periyot $N=3$)")
for a in ax:
    a.axhline(0, color="0.6", lw=0.8); a.grid(True, ls="--", alpha=0.35)
    a.set_xticks(n); a.set_ylim(-6, 6); a.set_ylabel("genlik")
ax[1].set_xlabel(r"$n$")
fig.tight_layout()
fig.savefig("../ssi-v-s2-decimation.png", dpi=130, bbox_inches="tight")
