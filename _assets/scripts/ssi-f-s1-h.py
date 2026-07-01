import numpy as np
import matplotlib.pyplot as plt

# Final S1: h1=delta[n]+0.5delta[n-1], h3=delta[n]-0.5delta[n-2] (seri, ust kol)
#           h2=-0.2delta[n+1] (paralel, alt kol).  h = h1*h3 + h2
h1 = np.array([1.0, 0.5])          # n=0,1
h3 = np.array([1.0, 0.0, -0.5])    # n=0,1,2
hu = np.convolve(h1, h3)           # n=0..3 -> {1,0.5,-0.5,-0.25}
n = np.arange(-1, 4)
h = np.zeros_like(n, dtype=float)
h[n == -1] = -0.2                  # h2
for k in range(len(hu)):
    h[n == k] += hu[k]

fig, ax = plt.subplots(figsize=(7.4, 3.4))
ax.stem(n, h, basefmt=" ", linefmt="#2c3e50", markerfmt="o")
ax.set_title(r"$h[n]=h_1*h_3+h_2$  —  $\sum|h|=2.45<\infty$ (kararlı), $h[-1]\neq0$ (nedensel değil)")
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$h[n]$")
ax.set_xticks(n)
ax.axhline(0, color="0.6", lw=0.8); ax.grid(True, ls="--", alpha=0.35)
for xi, yi in zip(n, h):
    if yi != 0:
        ax.annotate(f"{yi:g}", (xi, yi), textcoords="offset points",
                    xytext=(0, 7 if yi > 0 else -12), ha="center", fontsize=9)
fig.tight_layout()
fig.savefig("../ssi-f-s1-h.png", dpi=130, bbox_inches="tight")
