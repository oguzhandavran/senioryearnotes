import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

# ── Soru 2b: Sürekli Zamanlı Konvolüsyon — Kayan Pencere Adım Adım ────────────
# x(t) = -1 (-1<t<0) | 2 (0<t<1) | 1 (1<t<2) | 0 (diğer)
# h(t) = u(t)-u(t-1) = 1 (0≤t≤1) | 0 (diğer)
# y(t) = ∫[t-1, t] x(τ) dτ  — 1 birimlik kayan pencere

def x(tau):
    return np.where((tau > -1) & (tau < 0), -1.0,
           np.where((tau > 0) & (tau < 1),   2.0,
           np.where((tau > 1) & (tau < 2),   1.0, 0.0)))

def y(t):
    return np.where(t <= -1, 0.0,
           np.where(t <= 0,  -(t + 1),
           np.where(t <= 1,  3*t - 1,
           np.where(t <= 3,  3 - t, 0.0))))

# Her bölgeden bir temsil noktası
t_steps     = [-0.5,        0.5,        1.0,            1.5,        2.5       ]
bolge_labels = ['Bölge 2',  'Bölge 3',  'Sınır B3/B4',  'Bölge 4',  'Bölge 5' ]
step_colors  = ['#8e44ad',  '#16a085',  '#e67e22',       '#2980b9',  '#c0392b' ]

TAU   = np.linspace(-2.2, 3.8, 4000)
XLIM  = (-2.2, 3.8)
YLIM  = (-1.8, 2.8)

def style_ax(ax, title='', xlim=XLIM, ylim=YLIM):
    ax.axhline(0, color='0.5', lw=0.9)
    ax.axvline(0, color='0.5', lw=0.5, ls='--', alpha=0.45)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.grid(True, ls='--', alpha=0.28, lw=0.7)
    ax.tick_params(labelsize=7)
    ax.set_xlabel(r'$\tau$', fontsize=7, labelpad=1)
    if title:
        ax.set_title(title, fontsize=9, pad=4)

# ── Figure ─────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 9))
gs = GridSpec(3, 5, figure=fig,
              height_ratios=[1, 1.35, 0.85],
              hspace=0.72, wspace=0.38)

# ── Satır 0: x(τ), h(τ), açıklama ────────────────────────────────────────────
ax_x = fig.add_subplot(gs[0, :2])
ax_x.plot(TAU, x(TAU), color='#c0392b', lw=2.2)
ax_x.fill_between(TAU, 0, x(TAU), color='#c0392b', alpha=0.14)
for xc, yc, txt in [(-0.5, -0.65, '−1'), (0.5, 2.15, '2'), (1.5, 1.15, '1')]:
    ax_x.text(xc, yc, txt, ha='center', fontsize=9, color='#c0392b', fontweight='bold')
style_ax(ax_x, title=r'$x(\tau)$ — giriş sinyali')

ax_h = fig.add_subplot(gs[0, 2:4])
h_vals = np.where((TAU >= 0) & (TAU <= 1), 1.0, 0.0)
ax_h.plot(TAU, h_vals, color='#2980b9', lw=2.2)
ax_h.fill_between(TAU, 0, h_vals, color='#2980b9', alpha=0.18)
ax_h.text(0.5, 1.12, '1', ha='center', fontsize=9, color='#2980b9', fontweight='bold')
style_ax(ax_h, title=r'$h(\tau) = u(\tau)-u(\tau-1)$ — 1 birimlik kapı (genişlik=1)')

ax_info = fig.add_subplot(gs[0, 4])
ax_info.axis('off')
info = (
    r"$y(t)=\int_{-\infty}^{\infty}x(\tau)\,h(t{-}\tau)\,d\tau$" + "\n\n"
    r"$h(t{-}\tau)=1$ için $t{-}1\leq\tau\leq t$" + "\n\n"
    "→ Kayan pencere:\n"
    r"$y(t)=\int_{t-1}^{t}x(\tau)\,d\tau$" + "\n\n"
    "Her $t$ için:\n"
    "① Pencereyi $t$'ye kaydır\n"
    "② Pencere altındaki\n"
    "   $x(\tau)$ alanını al\n\n"
    "▓ sarı = + alan\n"
    "▓ mor  = − alan"
)
ax_info.text(0.05, 0.5, info, ha='left', va='center',
             transform=ax_info.transAxes, fontsize=8.2,
             bbox=dict(boxstyle='round,pad=0.55', fc='#fffde7', ec='#e0a800', lw=1.3))

# ── Satır 1: Her t için kayan pencere snapshot ────────────────────────────────
for col, (t_val, color, blabel) in enumerate(zip(t_steps, step_colors, bolge_labels)):
    ax = fig.add_subplot(gs[1, col])

    # x(τ) gri arka plan
    ax.plot(TAU, x(TAU), color='#aab0b8', lw=1.8, zorder=2)
    ax.fill_between(TAU, 0, x(TAU), color='#aab0b8', alpha=0.15, zorder=1)

    # Pencere sınırları
    wl = t_val - 1  # sol kenar
    wr = t_val      # sağ kenar (= t)

    # Pencere kutusu (h'nin geçerli olduğu bölge)
    ax.fill_between([wl, wr], YLIM[0], YLIM[1],
                    color=color, alpha=0.07, zorder=2)
    ax.axvline(wl, color=color, lw=1.6, ls='--', zorder=5)
    ax.axvline(wr, color=color, lw=2.0, zorder=5, label=f'$t={t_val}$')

    # Kesişim: pencere ile x'in sıfırdan farklı olduğu parçalar
    # Pozitif katkı (x > 0) → sarı-yeşil
    # Negatif katkı (x < 0) → mor
    tau_win = np.linspace(wl, wr, 600)
    x_win   = x(tau_win)

    pos_mask = x_win > 0
    neg_mask = x_win < 0

    ax.fill_between(tau_win, 0, x_win, where=pos_mask,
                    color='#27ae60', alpha=0.55, zorder=4, label='+alan')
    ax.fill_between(tau_win, 0, x_win, where=neg_mask,
                    color='#8e44ad', alpha=0.55, zorder=4, label='−alan')

    # Integral değeri
    yn = y(t_val)

    # t noktasını göster
    ax.plot(t_val, 0, '^', color=color, ms=8, zorder=7)
    ax.text(t_val, -1.55,
            f'$t$', ha='center', fontsize=7, color=color, fontweight='bold')

    ax.set_title(
        f"{blabel}\n$t={t_val}$   $\\rightarrow$   $y({t_val})={yn:.1f}$",
        fontsize=8, pad=3
    )
    style_ax(ax, xlim=XLIM, ylim=YLIM)

    # Pencere genişliğini yay oku ile göster
    arrow_y = 2.4
    ax.annotate('', xy=(wr, arrow_y), xytext=(wl, arrow_y),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))
    ax.text((wl + wr) / 2, arrow_y + 0.18, '1', ha='center', fontsize=7, color=color)

    # İlk panel: legend
    if col == 0:
        handles = [
            mpatches.Patch(color='#aab0b8', alpha=0.5, label=r'$x(\tau)$'),
            mpatches.Patch(color=color,    alpha=0.2, label=r'pencere $[t{-}1,\,t]$'),
            mpatches.Patch(color='#27ae60', alpha=0.6, label='+ katkı'),
            mpatches.Patch(color='#8e44ad', alpha=0.6, label='− katkı'),
        ]
        ax.legend(handles=handles, fontsize=5.8, loc='upper right', framealpha=0.9)

# ── Satır 2: Sonuç y(t) ───────────────────────────────────────────────────────
ax_y = fig.add_subplot(gs[2, :])
t_fine  = np.linspace(-2.2, 3.8, 4000)
y_fine  = y(t_fine)
ax_y.plot(t_fine, y_fine, color='#1a1a2e', lw=2.4)
ax_y.fill_between(t_fine, 0, y_fine, color='#1a1a2e', alpha=0.1)

# Köşe noktaları
for tp, yp in [(-1, 0), (0, -1), (1, 2), (3, 0)]:
    ax_y.plot(tp, yp, 'o', color='#1a1a2e', ms=7, zorder=6)
    va = 'bottom' if yp >= 0 else 'top'
    off = 0.12 if yp >= 0 else -0.12
    ax_y.text(tp, yp + off, f'$({tp},{yp})$', ha='center', fontsize=8, fontweight='bold')

# Adım noktalarını işaretle
for t_val, color in zip(t_steps, step_colors):
    ax_y.plot(t_val, y(t_val), 's', color=color, ms=8, zorder=7)
    ax_y.axvline(t_val, color=color, lw=0.7, ls=':', alpha=0.55)

style_ax(ax_y,
         title=r'Sonuç:  $y(t) = x(t)*h(t)$',
         xlim=(-2.2, 3.8), ylim=(-1.5, 2.8))
ax_y.set_xlabel('$t$', fontsize=8)

fig.suptitle(
    "Soru 2b — Sürekli Zamanlı Konvolüsyon Adım Adım (Kayan Pencere)\n"
    r"$x(t)$ parçalı sabit  $*$  $h(t)=u(t)-u(t-1)$  →  "
    r"$y(t)=\int_{t-1}^{t}x(\tau)\,d\tau$",
    fontsize=11, y=1.01
)

fig.savefig("../ss-q2-konv-adimlar.png", dpi=130, bbox_inches="tight")
print("Kaydedildi: ss-q2-konv-adimlar.png")
