import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation, PillowWriter

# ── Soru 2b: Kayan Pencere Konvolüsyon Animasyonu ────────────────────────────
# y(t) = ∫[t-1, t] x(τ) dτ  — pencere sağa kayarken alanı süpürür

def x(tau):
    return np.where((tau > -1) & (tau < 0), -1.0,
           np.where((tau > 0) & (tau < 1),   2.0,
           np.where((tau > 1) & (tau < 2),   1.0, 0.0)))

def y(t):
    return np.where(t <= -1, 0.0,
           np.where(t <= 0,  -(t + 1),
           np.where(t <= 1,  3*t - 1,
           np.where(t <= 3,  3 - t, 0.0))))

def bolge_label(t):
    if t <= -1:   return "Bölge 1: y = 0"
    elif t <= 0:  return f"Bölge 2: y = −(t+1)"
    elif t <= 1:  return f"Bölge 3: y = 3t−1"
    elif t <= 3:  return f"Bölge 4/5: y = 3−t"
    else:         return "Bölge 6: y = 0"

TAU      = np.linspace(-2.5, 4.5, 4000)
t_frames = np.linspace(-1.8, 3.6, 200)   # 200 kare, 25fps → ~8 sn

# ── Figure ─────────────────────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7),
                                gridspec_kw={'height_ratios': [1.5, 1]})
fig.patch.set_facecolor('#f8f9fa')
fig.subplots_adjust(hspace=0.45, left=0.09, right=0.97, top=0.88, bottom=0.08)

# ── Üst panel: x(τ) + kayan pencere ──────────────────────────────────────────
ax1.set_xlim(-2.5, 4.5)
ax1.set_ylim(-1.9, 3.1)
ax1.axhline(0, color='0.5', lw=0.9)
ax1.axvline(0, color='0.5', lw=0.5, ls='--', alpha=0.4)
ax1.grid(True, ls='--', alpha=0.25, lw=0.7)
ax1.set_xlabel(r'$\tau$', fontsize=10)
ax1.set_title(
    r'$x(\tau)$ sabit durur — pencere $[t{-}1,\; t]$ sağa kayar',
    fontsize=10.5, pad=6
)

# Statik x(τ)
ax1.fill_between(TAU, 0, x(TAU), color='#c0392b', alpha=0.18)
ax1.plot(TAU, x(TAU), color='#c0392b', lw=2.2, label=r'$x(\tau)$', zorder=3)
ax1.text(-0.5, -0.62, '−1', ha='center', fontsize=9, color='#c0392b', fontweight='bold')
ax1.text( 0.5,  2.18, '2',  ha='center', fontsize=9, color='#c0392b', fontweight='bold')
ax1.text( 1.5,  1.18, '1',  ha='center', fontsize=9, color='#c0392b', fontweight='bold')

# Süreksizlik çizgileri
for xc in [-1, 0, 1, 2]:
    ax1.axvline(xc, color='#c0392b', lw=0.7, ls=':', alpha=0.35)

# Legend için dummy patch'ler (sabit)
dum_pos = mpatches.Patch(color='#27ae60', alpha=0.65, label=r'+ katkı ($x>0$)')
dum_neg = mpatches.Patch(color='#8e44ad', alpha=0.65, label=r'− katkı ($x<0$)')
dum_win = mpatches.Patch(color='#2980b9', alpha=0.18, label=r'pencere $h(t{-}\tau)$')
ax1.legend(handles=[ax1.get_lines()[0], dum_win, dum_pos, dum_neg],
           fontsize=8.5, loc='upper right', framealpha=0.92)

# Animasyonlu nesneler — üst panel
win_bg   = mpatches.Rectangle((-99, -2), 1, 5.2,
                               color='#2980b9', alpha=0.10, zorder=1)
ax1.add_patch(win_bg)
vline_l, = ax1.plot([], [], '--', color='#2980b9', lw=1.8, zorder=5)
vline_r, = ax1.plot([], [], '-',  color='#2980b9', lw=2.5, zorder=5)

info_box = ax1.text(
    0.015, 0.95, '', transform=ax1.transAxes,
    fontsize=9.5, va='top', fontweight='bold', color='#1a1a2e',
    bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#aaa', lw=1)
)
bolge_box = ax1.text(
    0.015, 0.72, '', transform=ax1.transAxes,
    fontsize=8.5, va='top', color='#e67e22',
    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#e67e22', lw=1)
)

# Dinamik fill_between koleksiyonları
dyn_fills = []

# ── Alt panel: y(t) izi ───────────────────────────────────────────────────────
ax2.set_xlim(-2.5, 4.5)
ax2.set_ylim(-1.5, 2.9)
ax2.axhline(0, color='0.5', lw=0.9)
ax2.axvline(0, color='0.5', lw=0.5, ls='--', alpha=0.4)
ax2.grid(True, ls='--', alpha=0.25, lw=0.7)
ax2.set_xlabel(r'$t$', fontsize=10)
ax2.set_title(
    r'$y(t) = \int_{t-1}^{t} x(\tau)\,d\tau$ — pencere kayarken iz',
    fontsize=10.5, pad=6
)

# Referans y(t) soluk
t_ref = np.linspace(-2, 4, 2000)
ax2.plot(t_ref, y(t_ref), color='0.78', lw=1.4, ls='--', zorder=1)

# Köşe noktaları
for tp, yp in [(-1, 0), (0, -1), (1, 2), (3, 0)]:
    ax2.plot(tp, yp, 'o', color='#333', ms=6, zorder=7)

# Animasyonlu nesneler — alt panel
y_fill_area = [None]        # y(t) altındaki doldurulmuş alan
y_trace, = ax2.plot([], [], color='#1a1a2e', lw=2.5, zorder=4)
y_dot,   = ax2.plot([], [], 'o', color='#e67e22', ms=10, zorder=6,
                    markeredgecolor='white', markeredgewidth=1.5)
y_vline  = ax2.axvline(-99, color='#e67e22', lw=1.4, ls=':', zorder=3)
y_val_text = ax2.text(
    0.015, 0.93, '', transform=ax2.transAxes,
    fontsize=9.5, va='top', fontweight='bold', color='#1a1a2e',
    bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#aaa', lw=1)
)

fig.suptitle(
    'Soru 2b — Konvolüsyon: Kayan Pencere Animasyonu\n'
    r'$y(t) = x(t)*h(t)$ ,  $h(t)=u(t)-u(t-1)$ (genişlik=1 kapı)',
    fontsize=11, y=0.97
)

# ── Animasyon fonksiyonu ──────────────────────────────────────────────────────
def animate(i):
    t  = t_frames[i]
    wl = t - 1
    wr = t
    yn = float(y(t))

    # --- Üst panel güncelle ---
    # Pencere arka planı
    win_bg.set_x(wl)

    # Pencere kenar çizgileri
    vline_l.set_data([wl, wl], [-2, 3.2])
    vline_r.set_data([wr, wr], [-2, 3.2])

    # Önceki dinamik fill'leri temizle
    while dyn_fills:
        dyn_fills.pop().remove()

    # Yeni overlap fill'leri ekle
    tau_win = np.linspace(wl, wr, 600)
    xw      = x(tau_win)
    c1 = ax1.fill_between(tau_win, 0, xw, where=(xw >  1e-6),
                           color='#27ae60', alpha=0.65, zorder=4)
    c2 = ax1.fill_between(tau_win, 0, xw, where=(xw < -1e-6),
                           color='#8e44ad', alpha=0.65, zorder=4)
    dyn_fills.extend([c1, c2])

    # Metin kutuları
    info_box.set_text(f't = {t:+.2f}    pencere: [{wl:.2f}, {wr:.2f}]')
    bolge_box.set_text(bolge_label(t))

    # --- Alt panel güncelle ---
    # y(t) izi (t_frames[0]'dan şimdiye)
    t_past = t_frames[:i+1]
    y_past = y(t_past)
    y_trace.set_data(t_past, y_past)

    # y(t) altındaki alan
    if y_fill_area[0] is not None:
        y_fill_area[0].remove()
    if i > 0:
        y_fill_area[0] = ax2.fill_between(
            t_past, 0, y_past,
            color='#1a1a2e', alpha=0.10, zorder=2
        )

    # Hareketli nokta ve dikey çizgi
    y_dot.set_data([t], [yn])
    y_vline.set_xdata([t, t])
    y_val_text.set_text(f'y({t:+.2f}) = {yn:+.2f}')


anim = FuncAnimation(fig, animate, frames=len(t_frames),
                     interval=50, blit=False, repeat=True)

writer = PillowWriter(fps=25)
anim.save("../ss-q2-konv-animasyon.gif", writer=writer, dpi=110)
print("Kaydedildi: ss-q2-konv-animasyon.gif")
plt.close()
