import numpy as np
import matplotlib.pyplot as plt

# Konvolüsyonun "yansıt-kaydır-çarp-topla" mantığı (Soru 4 üzerinden)
# x(t): 0<t<1 -> +1, 1<t<2 -> -1 ;  h(t): 0<=t<=2 -> 1 (kapı)
def x(t):
    return np.where((t > 0) & (t < 1), 1.0,
           np.where((t > 1) & (t < 2), -1.0, 0.0))

def h(t):
    return np.where((t >= 0) & (t <= 2), 1.0, 0.0)

t = np.linspace(-2, 5, 2000)
t0 = 1.5                                   # seçilen anlık kaydırma değeri
tau = t

fig, ax = plt.subplots(2, 2, figsize=(9, 5.5))

# (a) x(tau) ve h(tau)
ax[0, 0].plot(tau, x(tau), color="#c0392b", lw=2, label=r"$x(\tau)$")
ax[0, 0].plot(tau, h(tau), color="#2980b9", lw=2, ls="--", label=r"$h(\tau)$")
ax[0, 0].set_title(r"1) $x(\tau)$ ve $h(\tau)$")

# (b) h(t0 - tau): yansıt + t0 kadar kaydır
ax[0, 1].plot(tau, x(tau), color="#c0392b", lw=2, label=r"$x(\tau)$")
ax[0, 1].plot(tau, h(t0 - tau), color="#27ae60", lw=2, label=r"$h(t_0-\tau),\ t_0=1.5$")
ax[0, 1].set_title(r"2-3) $h$ yansıt + kaydır")

# (c) çarpım x(tau)*h(t0-tau) -> taranan alan = y(t0)
prod = x(tau) * h(t0 - tau)
ax[1, 0].plot(tau, prod, color="#8e44ad", lw=2)
ax[1, 0].fill_between(tau, 0, prod, color="#8e44ad", alpha=0.3)
ax[1, 0].set_title(r"4) çarpım $\rightarrow$ alan $= y(1.5)$")

# (d) tum y(t)
def y(t):
    return np.where(t <= 0, 0.0,
           np.where(t <= 1, t,
           np.where(t <= 3, 2 - t,
           np.where(t <= 4, t - 4, 0.0))))
ax[1, 1].plot(t, y(t), color="#1a1a2e", lw=2.2)
ax[1, 1].axvline(t0, color="#8e44ad", ls=":", lw=1.2)
ax[1, 1].set_title(r"5) sonuç $y(t)=x*h$")

for a in ax.ravel():
    a.axhline(0, color="0.6", lw=0.8)
    a.axvline(0, color="0.6", lw=0.8)
    a.grid(True, ls="--", alpha=0.35)
    a.set_xlabel(r"$t$ / $\tau$")
    a.set_xlim(-2, 5); a.set_ylim(-1.4, 1.4)
ax[0, 0].legend(fontsize=8); ax[0, 1].legend(fontsize=8)
fig.suptitle("Konvolüsyon: yansıt → kaydır → çarp → topla", fontweight="bold")
fig.tight_layout()
fig.savefig("../ss-konv-kayan-pencere.png", dpi=130, bbox_inches="tight")
