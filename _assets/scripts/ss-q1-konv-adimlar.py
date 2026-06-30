import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D

# ── Soru 1b: Ayrık Zamanlı Konvolüsyon — Adım Adım (çevir + kaydır) ──────────
# x[n] = δ[n] - δ[n+1] + 2δ[n-1]
# h[n] = δ[n+1] + δ[n] + δ[n-1]
# y[n] = x[n]*h[n]

x_dict = {-1: -1, 0: 1, 1: 2}
h_dict = {-1: 1,  0: 1, 1: 1}
y_dict = {-2: -1, -1: 0, 0: 2, 1: 3, 2: 2}
n_steps    = [-2, -1, 0, 1, 2]
step_colors = ['#8e44ad', '#16a085', '#e67e22', '#2980b9', '#c0392b']

XLIM = (-3.7, 3.7)
YLIM = (-2.6, 3.9)

def draw_stems(ax, d, color, lw=2, ms=7, marker='o', alpha=1.0):
    for n, v in sorted(d.items()):
        ax.plot([n, n], [0, v], color=color, lw=lw, alpha=alpha, solid_capstyle='round')
        ax.plot(n, v, marker, color=color, ms=ms, zorder=5, alpha=alpha)

def style_ax(ax, title='', xlim=XLIM, ylim=YLIM):
    ax.axhline(0, color='0.55', lw=0.9)
    ax.axvline(0, color='0.55', lw=0.5, ls='--', alpha=0.5)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.grid(True, ls='--', alpha=0.3, lw=0.7)
    ax.tick_params(labelsize=7)
    ax.set_xlabel('$k$', fontsize=7, labelpad=1)
    ax.set_xticks([i for i in range(int(xlim[0]), int(xlim[1])+1) if i % 1 == 0])
    if title:
        ax.set_title(title, fontsize=9, pad=4)

# ── Figure ─────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 9))
gs = GridSpec(3, 5, figure=fig,
              height_ratios=[1, 1.3, 0.85],
              hspace=0.72, wspace=0.38)

# ── Satır 0: x[k]  |  h[k]  |  açıklama ──────────────────────────────────────
ax_x = fig.add_subplot(gs[0, :2])
draw_stems(ax_x, x_dict, '#c0392b')
for n, v in x_dict.items():
    offset = 0.2 if v >= 0 else -0.35
    ax_x.text(n, v + offset, str(v), ha='center', fontsize=9,
              color='#c0392b', fontweight='bold')
style_ax(ax_x, title=r'$x[k]$ — giriş sinyali')

ax_h = fig.add_subplot(gs[0, 2:4])
draw_stems(ax_h, h_dict, '#2980b9')
for n, v in h_dict.items():
    ax_h.text(n, v + 0.2, str(v), ha='center', fontsize=9, color='#2980b9', fontweight='bold')
style_ax(ax_h, title=r'$h[k]$ — dürtü yanıtı  (simetrik: $h[-k]=h[k]$)')

ax_info = fig.add_subplot(gs[0, 4])
ax_info.axis('off')
info = (
    r"$y[n]=\sum_{k} x[k]\,h[n{-}k]$" + "\n\n"
    "Adım adım:\n"
    "① $h[k]$'yı çevir: $h[-k]$\n"
    "② $n$ kadar kaydır: $h[n{-}k]$\n"
    "③ $x[k]$ ile çarp\n"
    "④ Topla → $y[n]$\n\n"
    "▓ sarı = çakışan bölge\n"
    "□ = $h[n{-}k]$ konumu"
)
ax_info.text(0.05, 0.5, info, ha='left', va='center',
             transform=ax_info.transAxes, fontsize=8.2,
             bbox=dict(boxstyle='round,pad=0.55', fc='#fffde7', ec='#e0a800', lw=1.3))

# ── Satır 1: Her n için h[n-k] kaydırma adımı ─────────────────────────────────
for col, (n, color) in enumerate(zip(n_steps, step_colors)):
    ax = fig.add_subplot(gs[1, col])

    # x[k] — gri arka plan
    draw_stems(ax, x_dict, '#bdc3c7', lw=1.5, ms=5, alpha=0.85)

    # h[n-k]: k pozisyonunda h[n-k] değerini koy
    h_shifted = {}
    for k in range(int(XLIM[0]) - 1, int(XLIM[1]) + 2):
        hval = h_dict.get(n - k, 0)
        if hval != 0:
            h_shifted[k] = hval
    draw_stems(ax, h_shifted, color, lw=2, ms=7, marker='s')

    # Çakışma: x[k]≠0 ve h[n-k]≠0 olan k'lar
    products = {}
    for k, xv in x_dict.items():
        hv = h_dict.get(n - k, 0)
        if hv != 0:
            products[k] = xv * hv
            ax.axvspan(k - 0.35, k + 0.35, alpha=0.22, color='#f39c12', zorder=1)

    yn = y_dict.get(n, 0)
    if products:
        parts = []
        for v in products.values():
            parts.append(f"({v})" if v < 0 else str(v))
        prod_str = "+".join(parts)
        line2 = f"{prod_str}={yn}"
    else:
        line2 = "0 (çakışma yok)"

    ax.set_title(f"$n={n:+d}$\n$y[{n}]={line2}$", fontsize=8, pad=3)
    style_ax(ax)

    # İlk panel için legend
    if col == 0:
        handles = [
            Line2D([0], [0], color='#bdc3c7', marker='o', lw=1.5, ms=5, label=r'$x[k]$'),
            Line2D([0], [0], color=color,     marker='s', lw=2,   ms=7, label=r'$h[n{-}k]$'),
        ]
        ax.legend(handles=handles, fontsize=6.5, loc='upper right', framealpha=0.9)

# ── Satır 2: Sonuç y[n] (tam genişlik) ────────────────────────────────────────
ax_y = fig.add_subplot(gs[2, :])
draw_stems(ax_y, y_dict, '#1a1a2e', lw=2.4, ms=9)
for n, v in y_dict.items():
    offset = 0.2 if v >= 0 else -0.35
    ax_y.text(n, v + offset, str(v), ha='center', fontsize=10,
              color='#1a1a2e', fontweight='bold')
style_ax(ax_y,
         title=r'Sonuç:  $y[n] = x[n]*h[n] = -\delta[n+2]+2\delta[n]+3\delta[n-1]+2\delta[n-2]$',
         xlim=(-4.5, 4.5), ylim=(-2.5, 4.5))
ax_y.set_xlabel('$n$', fontsize=8)
# Sonuç noktalarının altına hafif gölge
for n, v in y_dict.items():
    ax_y.fill_between([n - 0.35, n + 0.35], 0, v,
                       color='#1a1a2e', alpha=0.08)

fig.suptitle(
    "Soru 1b — Ayrık Zamanlı Konvolüsyon Adım Adım\n"
    r"$x[n]=\delta[n]-\delta[n+1]+2\delta[n-1]$  $*$  "
    r"$h[n]=\delta[n+1]+\delta[n]+\delta[n-1]$",
    fontsize=11, y=1.01
)

fig.savefig("../ss-q1-konv-adimlar.png", dpi=130, bbox_inches="tight")
print("Kaydedildi: ss-q1-konv-adimlar.png")
