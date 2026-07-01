import numpy as np
import matplotlib.pyplot as plt

# Vize S5: N=3 hareketli ortalama, x[n]=(1/3)^n u[n]
N = 3
n = np.arange(0, 10)
x = (1/3.0) ** n
# y[n] = (1/3)(x[n]+x[n-1]+x[n-2])
xpad = np.concatenate([np.zeros(2), x])
y = (xpad[2:] + xpad[1:-1] + xpad[:-2]) / 3.0

fig, ax = plt.subplots(figsize=(8.0, 3.6))
ax.stem(n, x, basefmt=" ", linefmt="0.7", markerfmt="x", label=r"giriş $x[n]=(1/3)^n u[n]$")
ax.stem(n, y, basefmt=" ", linefmt="#8e44ad", markerfmt="o", label=r"çıkış $y[n]$ (3'lü ortalama)")
ax.set_title(r"Hareketli ortalama (alçak geçiren): $y[n]=\frac{1}{3}\sum_{k=0}^{2}x[n-k]$")
ax.set_xlabel(r"$n$"); ax.set_ylabel("genlik")
ax.set_xticks(n)
ax.axhline(0, color="0.6", lw=0.8); ax.grid(True, ls="--", alpha=0.35)
ax.legend(loc="upper right")
fig.tight_layout()
fig.savefig("../ssi-v-s5-ma.png", dpi=130, bbox_inches="tight")
