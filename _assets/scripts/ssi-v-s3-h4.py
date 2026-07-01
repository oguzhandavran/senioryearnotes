import numpy as np
import matplotlib.pyplot as plt

# Vize S3: h1=u[n]-u[n-5]={1,1,1,1,1}(0..4), h3=u[n]-u[n-2]={1,1}(0,1)
# ust kol seri: hu = h1*h3 ; alt kol paralel: h2=delta[n+2]
# h4 = h1*h3 + h2
hu = np.convolve(np.ones(5), np.ones(2))   # n=0..5 -> {1,2,2,2,2,1}
# h4 indeksleri n=-2..5
n = np.arange(-2, 6)
h4 = np.zeros_like(n, dtype=float)
h4[n == -2] = 1.0                          # h2 = delta[n+2]
for k in range(6):                         # hu yerlesimi n=0..5
    h4[n == k] += hu[k]

fig, ax = plt.subplots(figsize=(7.6, 3.4))
ax.stem(n, h4, basefmt=" ", linefmt="#16a085", markerfmt="o")
ax.set_title(r"$h_4[n]=h_1*h_3+h_2$  —  $\sum|h_4|=11<\infty$ (kararlı), $h_4[-2]\neq0$ (nedensel değil)")
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$h_4[n]$")
ax.set_xticks(n)
ax.axhline(0, color="0.6", lw=0.8); ax.grid(True, ls="--", alpha=0.35)
for xi, yi in zip(n, h4):
    if yi != 0:
        ax.annotate(f"{yi:g}", (xi, yi), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=9)
fig.tight_layout()
fig.savefig("../ssi-v-s3-h4.png", dpi=130, bbox_inches="tight")
