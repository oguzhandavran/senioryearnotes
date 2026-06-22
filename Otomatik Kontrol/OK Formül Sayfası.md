---
tags: [otomatik-kontrol, formül, özet, kopya-kağıdı]
---

# OK — Formül Sayfası (Kopya Kağıdı)

← [[OK Ana Sayfa]]

---

## Temel Transfer Fonksiyonları

$$\boxed{T(s) = \frac{G(s)}{1 + G(s)H(s)}} \quad \text{Negatif Geri Besleme}$$

$$\boxed{T(s) = \frac{G(s)}{1 - G(s)H(s)}} \quad \text{Pozitif Geri Besleme}$$

**Karakteristik denklem:** $1 + G(s)H(s) = 0$

---

## Routh-Hurwitz

| Derece | Şart |
|--------|------|
| 2: $s^2+a_1s+a_0$ | $a_1, a_0 > 0$ |
| 3: $s^3+a_2s^2+a_1s+a_0$ | $a_2, a_1, a_0 > 0$ ve $a_2 a_1 > a_0$ |
| n | Tüm katsayılar pozitif + Routh tablosu birinci sütunu pozitif |

**Routh tablosu ($b$ satırı):**
$$b_1 = \frac{a_{n-1}a_{n-2} - a_n a_{n-3}}{a_{n-1}}$$

---

## Kararlı Hal Hataları

| Giriş | $R(s)$ | Hata Formülü |
|-------|--------|-------------|
| Basamak | $1/s$ | $e(\infty) = \dfrac{1}{1 + K_p}$ |
| Rampa | $1/s^2$ | $e(\infty) = \dfrac{1}{K_v}$ |
| Parabol | $1/s^3$ | $e(\infty) = \dfrac{1}{K_a}$ |

$$K_p = \lim_{s\to 0}G(s), \quad K_v = \lim_{s\to 0}sG(s), \quad K_a = \lim_{s\to 0}s^2G(s)$$

---

## 2. Derece Sistem Parametreleri

$$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

$$\omega_d = \omega_n\sqrt{1-\zeta^2} \quad \text{(sönümlü doğal frekans)}$$

| Parametre | Formül |
|-----------|--------|
| $T_r$ (yükselme) | $\dfrac{1.8}{\omega_n}$ veya $\dfrac{\pi - \arccos\zeta}{\omega_d}$ |
| $T_p$ (tepe) | $\dfrac{\pi}{\omega_d}$ |
| $T_s$ (%2) | $\dfrac{4}{\zeta\omega_n}$ |
| $T_s$ (%5) | $\dfrac{3}{\zeta\omega_n}$ |
| $\%OS$ | $100 e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| $\zeta$ den $\%OS$ | $\dfrac{-\ln(\%OS/100)}{\sqrt{\pi^2+\ln^2(\%OS/100)}}$ |

---

## Kök Yer Eğrisi

| Kural | Formül |
|-------|--------|
| Asimptot açısı | $\theta_q = \dfrac{\pm 180°(2q+1)}{n-m}$ |
| Asimptot merkezi | $\sigma_a = \dfrac{\sum p_i - \sum z_j}{n-m}$ |
| Breakaway | $\dfrac{d}{ds}\left[\dfrac{D(s)}{N(s)}\right] = 0$ |
| j-ekseni (Routh) | $K_\text{krit}$ ve $\omega$ |
| Dal başlangıcı | Açık çevrim kutuplar ($K=0$) |
| Dal sonu | Sıfırlar veya sonsuz ($K\to\infty$) |

---

## Bode Diyagramı Özeti

| Eleman | Kazanç Eğimi | Faz Gecikmesi |
|--------|-------------|--------------|
| Sabit $K$ | 0 dB | 0° |
| Kutup $1/(s/\omega_p+1)$ | -20 dB/dekad | -90° (geçiş) |
| Sıfır $(s/\omega_z+1)$ | +20 dB/dekad | +90° (geçiş) |
| İntegratör $1/s$ | -20 dB/dekad | -90° sabit |

$$\text{PM} = 180° + \angle G(j\omega_{gc})$$
$$\text{GM [dB]} = -20\log|G(j\omega_{pc})|$$

---

## Laplace Dönüşümü Hızlı Tablo

| $f(t)$ | $F(s)$ |
|--------|--------|
| $\delta(t)$ | $1$ |
| $u(t)$ | $1/s$ |
| $t\,u(t)$ | $1/s^2$ |
| $e^{-at}$ | $1/(s+a)$ |
| $\sin(\omega t)$ | $\omega/(s^2+\omega^2)$ |
| $\cos(\omega t)$ | $s/(s^2+\omega^2)$ |
| $e^{-at}\sin(\omega t)$ | $\omega/((s+a)^2+\omega^2)$ |
| $t e^{-at}$ | $1/(s+a)^2$ |
| $f'(t)$ | $sF(s) - f(0)$ |
| $f''(t)$ | $s^2F(s) - sf(0) - f'(0)$ |

**Son değer teoremi:** $\lim_{t\to\infty}f(t) = \lim_{s\to 0}sF(s)$
