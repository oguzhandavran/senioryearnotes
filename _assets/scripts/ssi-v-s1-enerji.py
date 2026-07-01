import numpy as np
import matplotlib.pyplot as plt

# Vize S1: x[n] = (1/2)^n u[n] — çizim + enerji (geometrik seri)
n = np.arange(0, 9)
x = (0.5) ** n

fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.stem(n, x, basefmt=" ", linefmt="#c0392b", markerfmt="o")
ax.set_title(r"$x[n]=\left(\frac{1}{2}\right)^n u[n]$  —  enerji $=\sum (1/4)^n = 4/3$")
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$x[n]$")
ax.set_xticks(n)
ax.axhline(0, color="0.6", lw=0.8); ax.grid(True, ls="--", alpha=0.35)
# enerji = alttaki kareler (|x[n]|^2) ipucu olarak gri
ax.stem(n, x**2, basefmt=" ", linefmt="0.7", markerfmt="x", label=r"$|x[n]|^2$")
ax.legend(loc="upper right")
fig.tight_layout()
fig.savefig("../ssi-v-s1-enerji.png", dpi=130, bbox_inches="tight")
