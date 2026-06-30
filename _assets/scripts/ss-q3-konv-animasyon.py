import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation, PillowWriter

# ── Soru 3b: Üçgen × Dikdörtgen Konvolüsyon — Kayan Pencere Animasyonu ────────
# x(τ) = 1-|τ|  (-1≤τ≤1, üçgen)
# h(t) = u(t+0.5)-u(t-0.5)  →  pencere [t-0.5, t+0.5], genişlik=1, ortalı
# y(t) = ∫[t-0.5, t+0.5] x(τ) dτ

def x(tau):
    return np.where(np.abs(tau) <= 1, 1 - np.abs(tau), 0.0)

def y(t):
    return np.where(t < -1.5, 0.0,
           np.where(t < -0.5, 0.5*(t + 1.5)**2,
           np.where(t <=  0.5, 0.75 - t**2,
           np.where(t <=  1.5, 0.5*(t - 1.5)**2, 0.0))))

def bolge_label(t):
    if   t <= -1.5: return "Bölge 1: y = 0"
    elif t <= -0.5: return "Bölge 2: y = ½(t+1.5)²"
    elif t <=  0.5: return "Bölge 3: y = 0.75 − t²"
    elif t <=  1.5: return "Bölge 4: y = ½(t−1.5)²"
    else:           return "Bölge 5: y = 0"

TAU      = np.linspace(-2.2, 2.2, 4000)
t_frames = np.linspace(-1.8, 1.8, 200)   # 200 kare, 25fps → ~8 sn

# ── Figure ─────────────────────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7),
                                gridspec_kw={'height_ratios': [1.5, 1]})
fig.patch.set_facecolor('#f8f9fa')
fig.subplots_adjust(hspace=0.45, left=0.09, right=0.97, top=0.88, bottom=0.08)

# ── Üst panel: x(τ) + kayan pencere ──────────────────────────────────────────
ax1.set_xlim(-2.2, 2.2)
ax1.set_ylim(-0.12, 1.35)
ax1.axhline(0, color='0.5', lw=0.9)
ax1.axvline(0, color='0.5', lw=0.5, ls='--', alpha=0.4)
ax1.grid(True, ls='--', alpha=0.25, lw=0.7)
ax1.set_xlabel(r'$\tau$', fontsize=10)
ax1.set_title(
    r'$x(\tau)=1-|\tau|$ sabit durur — pencere $[t{-}0.5,\; t{+}0.5]$ sağa kayar',
    fontsize=10.5, pad=6
)

# Statik x(τ) — üçgen
ax1.fill_between(TAU, 0, x(TAU), color='#c0392b', alpha=0.18)
ax1.plot(TAU, x(TAU), color='#c0392b', lw=2.2, label=r'$x(\tau)=1-|\tau|$', zorder=3)
ax1.text( 0.0, 1.06, '1',  ha='center', fontsize=9, color='#c0392b', fontweight='bold')
ax1.text(-1.0, 0.06, '−1', ha='center', fontsize=8, color='#c0392b', alpha=0.65)
ax1.text( 1.0, 0.06, '+1', ha='center', fontsize=8, color='#c0392b', alpha=0.65)
# Sınır çizgileri
for xc in [-1, 0, 1]:
    ax1.axvline(xc, color='#c0392b', lw=0.7, ls=':', alpha=0.35)

# Legend
dum_win = mpatches.Patch(color='#2980b9', alpha=0.18,
                          label=r'pencere $h(t{-}\tau)$ (genişlik=1, ortalı)')
dum_pos = mpatches.Patch(color='#27ae60', alpha=0.65,
                          label=r'+ katkı = $\int_{t-0.5}^{t+0.5}x(\tau)\,d\tau$')
ax1.legend(handles=[ax1.get_lines()[0], dum_win, dum_pos],
           fontsize=8.5, loc='upper right', framealpha=0.92)

# Animasyonlu nesneler — üst panel
win_bg = mpatches.Rectangle((-99, -0.15), 1, 1.55,
                              color='#2980b9', alpha=0.10, zorder=1)
ax1.add_patch(win_bg)
vline_l, = ax1.plot([], [], '--', color='#2980b9', lw=1.8, zorder=5)
vline_r, = ax1.plot([], [], '-',  color='#2980b9', lw=2.5, zorder=5)

info_box = ax1.text(
    0.015, 0.97, '', transform=ax1.transAxes,
    fontsize=9.5, va='top', fontweight='bold', color='#1a1a2e',
    bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#aaa', lw=1)
)
bolge_box = ax1.text(
    0.015, 0.76, '', transform=ax1.transAxes,
    fontsize=8.5, va='top', color='#e67e22',
    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#e67e22', lw=1)
)

dyn_fills = []

# ── Alt panel: y(t) izi ───────────────────────────────────────────────────────
ax2.set_xlim(-2.2, 2.2)
ax2.set_ylim(-0.05, 0.95)
ax2.axhline(0, color='0.5', lw=0.9)
ax2.axvline(0, color='0.5', lw=0.5, ls='--', alpha=0.4)
ax2.grid(True, ls='--', alpha=0.25, lw=0.7)
ax2.set_xlabel(r'$t$', fontsize=10)
ax2.set_title(
    r'$y(t) = \int_{t-0.5}^{t+0.5} x(\tau)\,d\tau$ — parabolik sonuç',
    fontsize=10.5, pad=6
)

# Referans y(t) soluk
t_ref = np.linspace(-2, 2, 2000)
ax2.plot(t_ref, y(t_ref), color='0.78', lw=1.4, ls='--', zorder=1)

# Köşe / özel noktalar
for tp, yp, lbl in [(-1.5, 0, '(−1.5, 0)'), (0, 0.75, '(0, 0.75)'), (1.5, 0, '(1.5, 0)')]:
    ax2.plot(tp, yp, 'o', color='#333', ms=6, zorder=7)
    va = 'bottom' if yp > 0.1 else 'top'
    off = 0.04 if yp > 0.1 else -0.04
    ax2.text(tp, yp + off, lbl, ha='center', fontsize=7.5, color='#333')
# Yarı-tepe noktaları
for tp in [-0.5, 0.5]:
    ax2.plot(tp, 0.5, 'o', color='#555', ms=5, zorder=7)

y_fill_area = [None]
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
    'Soru 3b — Konvolüsyon: Kayan Pencere Animasyonu\n'
    r'$y(t)=x(t)*h(t)$ ,  $h(t)=u(t+0.5)-u(t-0.5)$ (genişlik=1, simetrik kapı)',
    fontsize=11, y=0.97
)

# ── Animasyon fonksiyonu ──────────────────────────────────────────────────────
def animate(i):
    t  = t_frames[i]
    wl = t - 0.5
    wr = t + 0.5
    yn = float(y(t))

    # Pencere
    win_bg.set_x(wl)
    vline_l.set_data([wl, wl], [-0.15, 1.4])
    vline_r.set_data([wr, wr], [-0.15, 1.4])

    # Önceki fill'leri temizle
    while dyn_fills:
        dyn_fills.pop().remove()

    # Overlap fill (x her zaman ≥ 0 → sadece yeşil)
    tau_win = np.linspace(wl, wr, 600)
    xw = x(tau_win)
    c1 = ax1.fill_between(tau_win, 0, xw, where=(xw > 1e-9),
                           color='#27ae60', alpha=0.65, zorder=4)
    dyn_fills.append(c1)

    # Metin kutuları
    info_box.set_text(f't = {t:+.2f}    pencere: [{wl:.2f}, {wr:.2f}]')
    bolge_box.set_text(bolge_label(t))

    # y(t) izi
    t_past = t_frames[:i+1]
    y_past = y(t_past)
    y_trace.set_data(t_past, y_past)

    if y_fill_area[0] is not None:
        y_fill_area[0].remove()
    if i > 0:
        y_fill_area[0] = ax2.fill_between(
            t_past, 0, y_past,
            color='#1a1a2e', alpha=0.10, zorder=2
        )

    y_dot.set_data([t], [yn])
    y_vline.set_xdata([t, t])
    y_val_text.set_text(f'y({t:+.2f}) = {yn:+.4f}')


anim = FuncAnimation(fig, animate, frames=len(t_frames),
                     interval=50, blit=False, repeat=True)

writer = PillowWriter(fps=25)
anim.save("../ss-q3-konv-animasyon.gif", writer=writer, dpi=110)
print("Kaydedildi: ss-q3-konv-animasyon.gif")
plt.close()
