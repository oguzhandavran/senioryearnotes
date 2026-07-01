import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ── Soru 3 — Üst kol konvolüsyonu: h1[n]*h3[n] ──────────────────────────────
# h1[k] = 1, k=0..4  (uzunluk 5)
# h3[m] = 1, m=0,1   (uzunluk 2)
# "Yansıt - kaydır - çarp - topla":  y[n] = sum_k h1[k] * h3[n-k]
# h3[n-k] (k'nin fonksiyonu) yalnız k=n ve k=n-1'de 1 olur (h3 zaten
# çok kısa olduğundan yansıma simetrik kalıyor: {1,1} ters çevrilince yine {1,1}).

K = np.arange(-3, 9)          # k ekseni (sabit)

def h1(k):
    return np.where((k >= 0) & (k <= 4), 1.0, 0.0)

def h3_shift(k, n):
    # h3[n-k]: k=n ve k=n-1'de 1
    return np.where((k == n) | (k == n - 1), 1.0, 0.0)

def y_of_n(n):
    return float(np.sum(h1(K) * h3_shift(K, n)))

N_FRAMES_PER_N = 20                  # her n için kare sayısı (durağan duruş)
n_values = list(range(-2, 8))        # n = -2 .. 7 (girişten çıkışa tam görünüm)
y_all = {n: y_of_n(n) for n in n_values}
n_max_seen = max(y_all, key=lambda k: k)  # sadece tip kontrolü

frame_n = []
for n in n_values:
    frame_n += [n] * N_FRAMES_PER_N

# ── Figure: 3 panel (üstte h1 & kaydırılan h3, ortada çarpım, altta y[n] izi) ──
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8.5, 9),
                                     gridspec_kw={'height_ratios': [1.1, 1.0, 1.1]})
fig.patch.set_facecolor('#f8f9fa')
fig.subplots_adjust(hspace=0.55, left=0.10, right=0.96, top=0.90, bottom=0.07)

xlim = (K.min() - 0.5, K.max() + 0.5)

# --- Panel 1: h1[k] (sabit) ve h3[n-k] (kayan) ---
ax1.set_xlim(*xlim); ax1.set_ylim(-0.3, 1.6)
ax1.axhline(0, color='0.5', lw=0.9)
ax1.set_xticks(K)
ax1.grid(True, ls='--', alpha=0.25)
ax1.set_xlabel('$k$', fontsize=10)
ax1.set_title(r'$h_1[k]$ sabit durur  —  $h_3[n-k]$ (yansıtılmış+kaydırılmış) kayar',
              fontsize=10.5, pad=6)

h1_vals = h1(K)
markerline1, stemlines1, baseline1 = ax1.stem(
    K, h1_vals, linefmt='#2980b9', markerfmt='o', basefmt=' ')
plt.setp(markerline1, color='#2980b9', markersize=7)
plt.setp(stemlines1, linewidth=2.2)
markerline1.set_label(r'$h_1[k]$')

markerline2, stemlines2, baseline2 = ax1.stem(
    K, np.zeros_like(K, dtype=float), linefmt='#c0392b', markerfmt='s', basefmt=' ')
plt.setp(markerline2, color='#c0392b', markersize=7)
plt.setp(stemlines2, linewidth=2.2, linestyle='--')
markerline2.set_label(r'$h_3[n-k]$')
ax1.legend(loc='upper right', fontsize=9)

info1 = ax1.text(0.015, 0.93, '', transform=ax1.transAxes, fontsize=10,
                  va='top', fontweight='bold', color='#1a1a2e',
                  bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#aaa', lw=1))

# --- Panel 2: çarpım h1[k]*h3[n-k] ---
ax2.set_xlim(*xlim); ax2.set_ylim(-0.3, 1.6)
ax2.axhline(0, color='0.5', lw=0.9)
ax2.set_xticks(K)
ax2.grid(True, ls='--', alpha=0.25)
ax2.set_xlabel('$k$', fontsize=10)
ax2.set_title(r'Çarpım $h_1[k]\cdot h_3[n-k]$  →  toplamı $y[n]$ verir',
              fontsize=10.5, pad=6)

markerline3, stemlines3, baseline3 = ax2.stem(
    K, np.zeros_like(K, dtype=float), linefmt='#27ae60', markerfmt='D', basefmt=' ')
plt.setp(markerline3, color='#27ae60', markersize=8)
plt.setp(stemlines3, linewidth=2.6)

info2 = ax2.text(0.015, 0.93, '', transform=ax2.transAxes, fontsize=10,
                  va='top', fontweight='bold', color='#1a1a2e',
                  bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#aaa', lw=1))

# --- Panel 3: y[n] izi (biriken) ---
N_axis = np.array(n_values)
ax3.set_xlim(n_values[0] - 0.5, n_values[-1] + 0.5)
ax3.set_ylim(-0.5, 2.6)
ax3.axhline(0, color='0.5', lw=0.9)
ax3.set_xticks(N_axis)
ax3.grid(True, ls='--', alpha=0.25)
ax3.set_xlabel('$n$', fontsize=10)
ax3.set_title(r'Sonuç: $(h_1 * h_3)[n]$', fontsize=10.5, pad=6)

# soluk referans (tüm sonuç, baştan görünür)
y_ref = np.array([y_all[n] for n in n_values])
ax3.plot(N_axis, y_ref, 'o', color='0.82', ms=8, zorder=1)

markerline4, stemlines4, baseline4 = ax3.stem(
    [n_values[0]], [0.0], linefmt='#8e44ad', markerfmt='o', basefmt=' ')
plt.setp(markerline4, color='#8e44ad', markersize=10, markeredgecolor='white', markeredgewidth=1.2)
plt.setp(stemlines4, linewidth=2.6)

info3 = ax3.text(0.015, 0.93, '', transform=ax3.transAxes, fontsize=10,
                  va='top', fontweight='bold', color='#1a1a2e',
                  bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#aaa', lw=1))

fig.suptitle(
    'Soru 3 — Üst Kol Konvolüsyonu: $(h_1 * h_3)[n]$\n'
    r'$h_1[n]=\{1,1,1,1,1\}_{n=0..4}$,  $h_3[n]=\{1,1\}_{n=0,1}$',
    fontsize=11.5, y=0.975
)


def set_stem(markerline, stemlines, x, y):
    markerline.set_data(x, y)
    segs = [np.array([[xi, 0], [xi, yi]]) for xi, yi in zip(x, y)]
    stemlines.set_segments(segs)


def animate(frame_idx):
    n = frame_n[frame_idx]

    h3_vals = h3_shift(K, n)
    set_stem(markerline2, stemlines2, K, h3_vals)

    prod = h1_vals * h3_vals
    set_stem(markerline3, stemlines3, K, prod)

    yn = y_all[n]
    n_past = [nv for nv in n_values if nv <= n]
    y_past = [y_all[nv] for nv in n_past]
    set_stem(markerline4, stemlines4, n_past, y_past)

    active_k = sorted({k for k in (n, n - 1)})
    terms = " + ".join(
        f"h1[{k}]·h3[{n-k}]" for k in active_k if 0 <= k <= 4
    ) or "(örtüşme yok)"

    info1.set_text(f'n = {n}   (h3, k={n-1} ve k={n} konumunda)')
    info2.set_text(f'{terms}')
    info3.set_text(f'y[{n}] = {yn:.0f}')

    return markerline2, stemlines2, markerline3, stemlines3, markerline4, stemlines4


anim = FuncAnimation(fig, animate, frames=len(frame_n), interval=50,
                      blit=False, repeat=True)

writer = PillowWriter(fps=20)
anim.save("../ssi-v-s3-konv-animasyon.gif", writer=writer, dpi=105)
print("Kaydedildi: ssi-v-s3-konv-animasyon.gif")
plt.close()
