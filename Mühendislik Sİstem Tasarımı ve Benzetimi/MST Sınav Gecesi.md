---
tags: [mst, sinav-gecesi, ozet]
---

# MST — Sınav Gecesi Özeti

> Tek sayfa. Transfer fonksiyonu ve durum uzayı.

---

## 1 — Transfer Fonksiyonu Çıkarma Prosedürü

1. **FBD çiz** → Newton ya da Lagrange ile hareket denklemleri yaz
2. **Laplace** (sıfır başlangıç): $s^2 \leftrightarrow \ddot{x}$, $s \leftrightarrow \dot{x}$
3. Denklem sistemini **Cramer** ile çöz
4. $G(s) = \text{Çıkış}(s)/\text{Giriş}(s)$

---

## 2 — Mekanik Sistem Referansı

**Tek kütle:** $m\ddot{x}+b\dot{x}+kx=F \implies G=\dfrac{1}{ms^2+bs+k}$

**İki kütle + bağlayan yay $k_2$ + sönümleyici $b$:**

$\Delta_1 = m_1s^2+bs+(k_1+k_2)$, $\Delta_2 = m_2s^2+bs+(k_2+k_3)$, $Z=bs+k_2$

$$\frac{X_2}{F} = \frac{Z}{\Delta_1\Delta_2 - Z^2}$$

**Dönel:** $J\ddot{\theta}+b\dot{\theta}+k\theta=T \implies G=\dfrac{1}{Js^2+bs+k}$

**Dişli:** $\dfrac{\Theta_1}{T_1}=\dfrac{(N_2/N_1)^2}{J_{ref}s^2+b_{ref}s+k_{ref}}$; ref. atalet: $J_{ref}=J_2(N_1/N_2)^2$

**Sarkaç:** $\omega_n=\sqrt{g/l}$ (küçük açı)

---

## 3 — Elektrik Sistem Referansı

**Empedanslar:** $Z_R=R$, $Z_L=Ls$, $Z_C=1/(Cs)$

**Mesh KVL (Laplace):** $Z_{toplam}\cdot I - Z_{ortak}\cdot I_{diğer} = V$

**Op-amp (sanal toprak):** $V^+=V^-=0$ (inverting için)
- İnverting: $G = -Z_f/Z_{in}$
- Non-inverting: $G = 1 + Z_f/Z_1$

**Elektromekanik:** $G = K_m/[(R+Ls)(ms^2+bs+k)]$

---

## 4 — Durum Uzayı

$$\dot{x} = Ax+Bu, \quad y = Cx+Du$$

**TF'den:**  $G(s) = C(sI-A)^{-1}B + D$

**Eşlik kanonik form** (TF: $\frac{b_0}{s^n+a_{n-1}s^{n-1}+\cdots+a_0}$):

$$A = \begin{bmatrix}0&1&0&\cdots\\0&0&1&\cdots\\\vdots&&\ddots&\vdots\\-a_0&-a_1&\cdots&-a_{n-1}\end{bmatrix}, \quad B = \begin{bmatrix}0\\\vdots\\0\\1\end{bmatrix}, \quad C = \begin{bmatrix}b_0&0&\cdots&0\end{bmatrix}$$

**$(sI-A)^{-1}$ hesabı (2×2):** $\det(sI-A)=$ karakter. polinom

$$(sI-A)^{-1} = \frac{\text{adj}(sI-A)}{\det(sI-A)}$$

---

## 5 — 2. Derece Parametreler

$$G(s) = \frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$$

$\omega_n=\sqrt{k/m}$, $\zeta=b/(2\sqrt{mk})$

| $\zeta$ | Yanıt |
|---------|-------|
| $\zeta>1$ | Aşırı sönümlü (reel kutuplar) |
| $\zeta=1$ | Kritik |
| $\zeta<1$ | Az sönümlü (kompleks) |

---

## 6 — Birim Dönüşümleri (Hata Kaynağı!)

- N/mm → N/m: ×1000
- rpm → rad/s: ×$2\pi/60$
- mH → H: ×0.001
- μF → F: ×$10^{-6}$

---

## Tuzaklar

> [!warning] MST Tuzakları
> - Lagrange: $D$ (Rayleigh sönüm) terimi unutulursa sönüm kaybolur
> - Dişli: çıkışı hangi tarafta soruyor? $\Theta_1/T_1$ mi, $\Theta_2/T_2$ mi?
> - Durum uzayı: $D=0$ çoğunlukla fiziksel sistem için
> - Cramer: $2\times2$ sistemde det hesabını tekrar kontrol et
> - $(sI-A)^{-1}$: adj matrisin köşegen elemanları yer değiştirir!

---

← [[MST Ana Sayfa]]
