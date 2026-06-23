---
tags: [ss, lti, konvolüsyon, örnek-sorular]
---

# 02 — LTI ve Konvolüsyon Örnekleri

← [[SS Ana Sayfa]]  |  Teori: [[../Konu Anlatımları/02 LTI Sistemler ve Konvolüsyon]]

---

## Örnek 1 — DT Konvolüsyon (Üstel)

**Soru:** $x[n] = a^n u[n]$, $h[n] = b^n u[n]$ ($a \neq b$) için $y[n] = x[n]*h[n]$ bul.

**Çözüm:**
$$y[n] = \sum_{k=0}^{n} a^k b^{n-k} = b^n \sum_{k=0}^{n} \left(\frac{a}{b}\right)^k = b^n \cdot \frac{1-(a/b)^{n+1}}{1-a/b}$$

$$\boxed{y[n] = \frac{a^{n+1} - b^{n+1}}{a-b}\,u[n]}$$

**Özel durum** $a = b$: $y[n] = (n+1)a^n u[n]$

---

## Örnek 2 — Kayan Ortalama Filtresi

$h[n] = u[n] - u[n-5]$ (uzunluk 5 dikdörtgen pencere)

$$y[n] = x[n]*h[n] = \sum_{k=0}^{4} x[n-k]$$

Bu bir **kayan ortalama (moving average)** filtredir. Çıkış, son 5 örneğin toplamı.

---

## Örnek 3 — CT Konvolüsyon: Basamak × Üstel

**Soru:** $x(t) = u(t)$, $h(t) = e^{-at}u(t)$ ($a>0$) için $y(t)$ bul.

**Çözüm:**
$$y(t) = \int_0^t e^{-a\tau}d\tau = \frac{1-e^{-at}}{a}\,u(t)$$

$$\boxed{y(t) = \frac{1-e^{-at}}{a}\,u(t)}$$

---

## Örnek 4 — Frekans Domeninde Ters Analiz
*(Arş. Gör. Ecmel TERZİ)*

**Soru:** $H(j\omega) = \dfrac{1}{j\omega+3}$, $y(t) = e^{-t}u(t) - e^{-4t}u(t)$ verildiğinde $x(t) = ?$

**Adım 1** — $Y(j\omega)$:
$$Y(j\omega) = \frac{1}{j\omega+1} - \frac{1}{j\omega+4}$$

**Adım 2** — $X(j\omega) = Y(j\omega)/H(j\omega)$:
$$X(j\omega) = Y(j\omega)\cdot(j\omega+3) = \frac{j\omega+3}{j\omega+1} - \frac{j\omega+3}{j\omega+4}$$

**Adım 3** — Kısmi kesir:
$$\frac{j\omega+3}{j\omega+1} = 1 + \frac{2}{j\omega+1}, \qquad \frac{j\omega+3}{j\omega+4} = 1 - \frac{1}{j\omega+4}$$

$$X(j\omega) = \frac{2}{j\omega+1} + \frac{1}{j\omega+4}$$

$$\boxed{x(t) = 2e^{-t}u(t) + e^{-4t}u(t)}$$

---

## Örnek 5 — Genlik Modülasyonu / Frekans Kaydırma
*(Arş. Gör. Ecmel TERZİ)*

$$z(t) = x(t)\cdot\cos(\omega_c t) \;\longleftrightarrow\; Z(j\omega) = \frac{1}{2}\!\left[X\!\left(j(\omega-\omega_c)\right) + X\!\left(j(\omega+\omega_c)\right)\right]$$

**İspat:** $\cos(\omega_c t) = \tfrac{1}{2}(e^{j\omega_c t}+e^{-j\omega_c t})$, frekans kaydırma özelliğinden gelir.

**Yorum:** Zaman domeninde $\cos$ ile çarpım → frekans spektrumunu $\pm\omega_c$'ye kaydırır ve $\tfrac{1}{2}$ ile ölçekler.

---

## Örnek 6 — Temel CTFT Türetimleri
*(Arş. Gör. Ecmel TERZİ)*

### $\mathcal{F}\{\delta(t)\} = 1$
$$X(j\omega) = \int_{-\infty}^{\infty}\delta(t)\,e^{-j\omega t}\,dt = e^{0} = 1$$

### $\mathcal{F}\{e^{-at}u(t)\} = \dfrac{1}{a+j\omega}$ ($a > 0$)
$$X(j\omega) = \int_0^{\infty}e^{-(a+j\omega)t}\,dt = \frac{1}{a+j\omega}$$

$$|X(j\omega)| = \frac{1}{\sqrt{a^2+\omega^2}}, \qquad \angle X(j\omega) = -\arctan\!\left(\frac{\omega}{a}\right)$$

### $\mathcal{F}\{\text{rect}_{[-T,T]}\}$
$$X(j\omega) = \int_{-T}^{T}e^{-j\omega t}\,dt = \frac{2\sin(\omega T)}{\omega}$$

### İdeal LP filtre ters FT
$X(j\omega) = 1$ için $|\omega| \leq \omega_c$:
$$x(t) = \frac{\sin(\omega_c t)}{\pi t} = \frac{\omega_c}{\pi}\,\operatorname{sinc}\!\left(\frac{\omega_c t}{\pi}\right)$$

---

## Örnek 7 — Fourier Serisi Katsayıları
*(Arş. Gör. Ecmel TERZİ)*

**Soru:** $x(t) = 1 + \sin(\omega_0 t) + 2\cos(\omega_0 t) + \cos\!\left(2\omega_0 t + \tfrac{\pi}{4}\right)$ için $a_k$ bul.

**Çözüm** — Euler açılımıyla:

| $k$ | $a_k$ | $|a_k|$ | $\angle a_k$ |
|-----|-------|---------|-------------|
| $0$ | $1$ | $1$ | $0$ |
| $+1$ | $1 - j/2$ | $\sqrt{5}/2$ | $-\arctan(1/2)$ |
| $-1$ | $1 + j/2$ | $\sqrt{5}/2$ | $+\arctan(1/2)$ |
| $+2$ | $e^{j\pi/4}/2$ | $1/2$ | $+\pi/4$ |
| $-2$ | $e^{-j\pi/4}/2$ | $1/2$ | $-\pi/4$ |

Gerçek $x(t)$ için $a_{-k} = a_k^*$ — büyüklük çift, faz tek simetri.
