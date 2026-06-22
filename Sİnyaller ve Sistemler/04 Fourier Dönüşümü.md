---
tags: [ss, fourier-dönüşümü, ctft, dtft]
---

# 04 — Fourier Dönüşümü

← [[SS Ana Sayfa]]

## Özet

> Periyodik olmayan sinyalleri de frekans domenine taşı. CTFT: $x(t) \leftrightarrow X(j\omega)$. DTFT: $x[n] \leftrightarrow X(e^{j\omega})$ — $2\pi$ periyodik.

---

## 1. Sürekli Zaman Fourier Dönüşümü (CTFT)

### Analiz ve Sentez

$$\boxed{X(j\omega) = \int_{-\infty}^{\infty} x(t)\, e^{-j\omega t}\, dt}$$

$$\boxed{x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega)\, e^{j\omega t}\, d\omega}$$

### Temel CTFT Çiftleri

| $x(t)$ | $X(j\omega)$ | Koşul |
|--------|-------------|-------|
| $\delta(t)$ | $1$ | |
| $1$ | $2\pi\delta(\omega)$ | |
| $e^{-at}u(t)$ | $\dfrac{1}{a+j\omega}$ | $a > 0$ |
| $e^{-a|t|}$ | $\dfrac{2a}{a^2+\omega^2}$ | $a > 0$ |
| $u(t)$ | $\pi\delta(\omega) + \dfrac{1}{j\omega}$ | |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ | |
| $\sin(\omega_0 t)$ | $\dfrac{\pi}{j}[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ | |
| $\text{rect}(t/\tau)$ | $\tau \operatorname{sinc}(\omega\tau/2)$ | |
| $t^n e^{-at}u(t)$ | $\dfrac{n!}{(a+j\omega)^{n+1}}$ | $a > 0$ |

---

## 2. Ayrık Zaman Fourier Dönüşümü (DTFT)

### Analiz ve Sentez

$$\boxed{X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]\, e^{-j\omega n}}$$

$$\boxed{x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega})\, e^{j\omega n}\, d\omega}$$

> [!tanim] $2\pi$ Periyodiklik
> $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$ — DTFT her zaman $2\pi$ periyodiktir. Yeterli analiz bölgesi: $[-\pi, \pi]$.

### Temel DTFT Çiftleri

| $x[n]$ | $X(e^{j\omega})$ | Koşul |
|--------|-----------------|-------|
| $\delta[n]$ | $1$ | |
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ | |
| $1$ | $2\pi\sum_k \delta(\omega - 2\pi k)$ | |
| $a^n u[n]$ | $\dfrac{1}{1-ae^{-j\omega}}$ | $|a|<1$ |
| $na^n u[n]$ | $\dfrac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ | $|a|<1$ |
| $\cos(\omega_0 n)$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ (periyodik) | |
| Dikdörtgen pencere $w[n]$ | $e^{-j\omega\frac{N-1}{2}}\dfrac{\sin(N\omega/2)}{\sin(\omega/2)}$ | $0\le n\le N-1$ |

---

## 3. Fourier Dönüşümü Özellikleri

| Özellik | CT: $x(t) \leftrightarrow X(j\omega)$ | DT: $x[n] \leftrightarrow X(e^{j\omega})$ |
|---------|--------------------------------------|------------------------------------------|
| Doğrusallik | $ax+by \leftrightarrow aX+bY$ | aynı |
| Zaman kayması | $x(t-t_0) \leftrightarrow e^{-j\omega t_0}X(j\omega)$ | $x[n-n_0] \leftrightarrow e^{-j\omega n_0}X(e^{j\omega})$ |
| Frekans kayması | $e^{j\omega_0 t}x(t) \leftrightarrow X(j(\omega-\omega_0))$ | $e^{j\omega_0 n}x[n] \leftrightarrow X(e^{j(\omega-\omega_0)})$ |
| Zaman ölçekleme | $x(at) \leftrightarrow \frac{1}{|a|}X(j\omega/a)$ | — (DT'de yok) |
| Zaman ters çevirme | $x(-t) \leftrightarrow X(-j\omega)$ | $x[-n] \leftrightarrow X(e^{-j\omega})$ |
| Konvolüsyon | $x*h \leftrightarrow X \cdot H$ | aynı |
| Çarpma | $x \cdot h \leftrightarrow \frac{1}{2\pi}X * H$ | $x[n]h[n] \leftrightarrow \frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\theta})H(e^{j(\omega-\theta)})d\theta$ |
| CT Türev | $\frac{dx}{dt} \leftrightarrow j\omega X(j\omega)$ | — |
| DT Fark | $x[n]-x[n-1] \leftrightarrow (1-e^{-j\omega})X(e^{j\omega})$ | |
| **Parseval** | $\int|x|^2 dt = \frac{1}{2\pi}\int|X|^2 d\omega$ | $\sum|x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}|X(e^{j\omega})|^2 d\omega$ |

> [!sinav] Konvolüsyon-Çarpma Dualitesi
> Zaman domeninde konvolüsyon → frekans domeninde çarpım (ve tersi).
> Bu, filtre tasarımının temelini oluşturur: $H(e^{j\omega}) = Y(e^{j\omega}) / X(e^{j\omega})$

---

## 4. Transfer Fonksiyonu ve DTFT

Fark denklemi verildiğinde:
$$y[n] - \frac{1}{4}y[n-1] = 2x[n] + x[n-2]$$

DTFT al:
$$Y(e^{j\omega})(1 - \frac{1}{4}e^{-j\omega}) = X(e^{j\omega})(2 + e^{-2j\omega})$$

$$H(e^{j\omega}) = \frac{Y(e^{j\omega})}{X(e^{j\omega})} = \frac{2 + e^{-2j\omega}}{1 - \frac{1}{4}e^{-j\omega}}$$

---

## 5. Ters DTFT Örneği

$X(e^{j\omega}) = \dfrac{1}{1-\frac{1}{3}e^{-j\omega}}$ için $x[n]$ bul:

DTFT çiftinden doğrudan: $x[n] = \left(\frac{1}{3}\right)^n u[n]$

---

## 6. Ders Tahtası — CT Konvolüsyon (Ödev 3)

*Bağlam: Konvolüsyon teoremi, $\mathcal{F}\{x*h\} = X(j\omega)\cdot H(j\omega)$, Fourier dönüşümünün en kritik özelliğidir.*

### CT Konvolüsyon — Üstel × Basamak

$$x(t) = e^{2t}u(t), \qquad h(t) = u(t-3)$$

**Konvolüsyon integrali:**
$$y(t) = \int_{-\infty}^{\infty} e^{2\tau}u(\tau)\cdot u(t-\tau-3)\,d\tau$$

**Sınır analizi:**
- $u(\tau)=1$: $\tau \geq 0$ gerektirir
- $u(t-\tau-3)=1$: $\tau \leq t-3$ gerektirir
- İkisi birlikte aktif: $0 \leq \tau \leq t-3$, yani $t > 3$ gerekir

**$t > 3$ için:**
$$y(t) = \int_0^{t-3} e^{2\tau}\,d\tau = \left[\frac{e^{2\tau}}{2}\right]_0^{t-3} = \frac{e^{2(t-3)}-1}{2}$$

$$\boxed{y(t) = \frac{1}{2}\!\left(e^{2(t-3)}-1\right)u(t-3)}$$

**Yorumlama:**
- $t \leq 3$: $x(t)$ ve $h(t-3)$'ün etki bölgeleri örtüşmez → $y(t)=0$
- $t > 3$: üstel büyüme başlar, $t=3$'te sıfırdan kalkar
- $h(t)=u(t-3)$: Fourier domeninde $H(j\omega) = e^{-3j\omega}\!\left[\pi\delta(\omega)+\tfrac{1}{j\omega}\right]$

> [!sinav] Konvolüsyon Teoremi Uygulaması
> Zaman domeninde konvolüsyon $\leftrightarrow$ frekans domeninde nokta-nokta çarpım.
> Bu örnek için $Y(j\omega) = X(j\omega)\cdot H(j\omega)$ uygulanabilir ama $u(t)$ dönüşümü
> $\delta(\omega)$ içerdiğinden doğrudan hesap daha pratiktir.

*Konvolüsyon tekniği detayları: [[02 LTI Sistemler ve Konvolüsyon]]*

---

## Bağlantılı Notlar

- [[03 Fourier Serisi]]
- [[05 Laplace Dönüşümü]]
- [[../Sayısal Sinyal İşleme/02 Z-Dönüşümü|SSİ: Z-Dönüşümü (DT analog)]]
- [[../Sayısal Sinyal İşleme/03 DFT ve FFT|SSİ: DFT ve FFT]]
