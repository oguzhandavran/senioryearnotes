---
tags: [ss, fourier-dönüşümü, ctft, örnek-sorular]
---

# 04 — Fourier Dönüşümü Örnekleri

← [[SS Ana Sayfa]]  |  Teori: [[../Konu Anlatımları/04 Fourier Dönüşümü]]

---

## Örnek 1 — Transfer Fonksiyonu (Fark Denkleminden)

> [!note]- Semboller
> - $x[n],y[n]$: giriş/çıkış dizileri; $x[n-k]$: $k$ gecikmiş giriş
> - $H(e^{j\omega})=Y/X$: frekans yanıtı (DTFT)
> - DTFT kaydırma: $x[n-k]\leftrightarrow e^{-j\omega k}X(e^{j\omega})$
> - Pay = girişin katsayıları, payda = çıkışın katsayıları

**Soru:** Aşağıdaki fark denkleminden $H(e^{j\omega})$ bul.

$$y[n] - \frac{1}{4}y[n-1] = 2x[n] + x[n-2]$$

**Çözüm:** Her terimin DTFT'sini al ($x[n-k] \leftrightarrow e^{-j\omega k}X$):

$$Y(e^{j\omega})\!\left(1 - \frac{1}{4}e^{-j\omega}\right) = X(e^{j\omega})\!\left(2 + e^{-2j\omega}\right)$$

$$\boxed{H(e^{j\omega}) = \frac{Y(e^{j\omega})}{X(e^{j\omega})} = \frac{2 + e^{-2j\omega}}{1 - \frac{1}{4}e^{-j\omega}}}$$

---

## Örnek 2 — CTFT Özelliği: Zaman Kayması

> [!note]- Semboller
> - $x(t)=e^{-2t}u(t)$: nedensel üstel; çift $e^{-at}u(t)\leftrightarrow\frac{1}{a+j\omega}$
> - Zaman kayması: $x(t-t_0)\leftrightarrow e^{-j\omega t_0}X(j\omega)$ (sadece faz değişir, genlik aynı)
> - $X,Y$: giriş/çıkış CTFT'leri; $t_0=3$: gecikme

**Soru:** $x(t) = e^{-2t}u(t)$ için $X(j\omega)$ bul. Sonra $y(t) = x(t-3)$ için $Y(j\omega)$ nedir?

**Çözüm:**
$$X(j\omega) = \frac{1}{2+j\omega}$$

Zaman kayması özelliği: $y(t) = x(t-3)$
$$Y(j\omega) = e^{-3j\omega}\cdot X(j\omega) = \frac{e^{-3j\omega}}{2+j\omega}$$

---

## Örnek 3 — CT Konvolüsyon: Üstel × Basamak
*(Arş. Gör. Ecmel TERZİ)*

> [!note]- Semboller
> - $x(t)=e^{2t}u(t)$: nedensel **büyüyen** üstel; $h(t)=u(t-3)$: 3'te başlayan basamak
> - $\tau$: konvolüsyon değişkeni; $u(\tau)$ ve $u(t-\tau-3)$ örtüşme sınırlarını verir
> - Örtüşme: $0\le\tau\le t-3$ (yalnız $t>3$); $y(t)$ bu yüzden $u(t-3)$ ile çarpılır

**Soru:** $x(t) = e^{2t}u(t)$, $h(t) = u(t-3)$ için $y(t) = x(t)*h(t)$ bul.

**Çözüm:**
$$y(t) = \int_{-\infty}^{\infty} e^{2\tau}u(\tau)\cdot u(t-\tau-3)\,d\tau$$

Sınır analizi:
- $u(\tau)=1$: $\tau \geq 0$
- $u(t-\tau-3)=1$: $\tau \leq t-3$
- Her ikisi aktif: $0 \leq \tau \leq t-3$, yani $t > 3$ gerekir

**$t > 3$ için:**
$$y(t) = \int_0^{t-3} e^{2\tau}\,d\tau = \left[\frac{e^{2\tau}}{2}\right]_0^{t-3} = \frac{e^{2(t-3)}-1}{2}$$

$$\boxed{y(t) = \frac{1}{2}\!\left(e^{2(t-3)}-1\right)u(t-3)}$$

**Yorum:**
- $t \leq 3$: Etki bölgeleri örtüşmez → $y(t) = 0$
- $t > 3$: Üstel büyüme başlar

---

## Örnek 4 — Çarpma Özelliği Uygulaması (4.5)

> [!note]- Semboller
> - $\operatorname{rect}(t)$: birim genişlikli kapı (0/1 değerli); $\operatorname{rect}^2=\operatorname{rect}$ (çünkü değerler 0/1)
> - Çarpma özelliği: zamanda çarpım ↔ frekansta $\frac{1}{2\pi}$ ölçekli **evrişim**
> - $\operatorname{sinc}$: dikdörtgenin Fourier dönüşümü; $Y(j\omega)$: çıkışın CTFT'si

**Soru:** $x(t) = \operatorname{rect}(t)$ ve $h(t) = \operatorname{rect}(t)$ için $y(t) = x(t)\cdot h(t)$ nedir ve $Y(j\omega) = ?$

**Çözüm:**

Zaman domeninde: $y(t) = x(t)\cdot h(t) = \operatorname{rect}^2(t) = \operatorname{rect}(t)$

Frekans domeninde çarpma özelliği:
$$Y(j\omega) = \frac{1}{2\pi} X(j\omega) * H(j\omega) = \frac{1}{2\pi} \operatorname{sinc}^2\!\left(\frac{\omega}{2\pi}\right) \text{ (evrişim)}$$

*Not: Zaman domeninde çarpım basit olduğundan doğrudan sonuç:*
$$Y(j\omega) = \mathcal{F}\{\operatorname{rect}(t)\} = \operatorname{sinc}\!\left(\frac{\omega}{2\pi}\right)$$

---

## Örnek 5 — Parseval ile Enerji Hesabı

> [!note]- Semboller
> - $x(t)=e^{-at}u(t)$: nedensel sönen üstel, $a>0$
> - $E=\int|x(t)|^2dt$: zaman domeni enerjisi
> - Parseval (CTFT): $E=\frac{1}{2\pi}\int|X(j\omega)|^2d\omega$
> - $|X(j\omega)|^2=\frac{1}{a^2+\omega^2}$; $\int\frac{d\omega}{a^2+\omega^2}=\frac{\pi}{a}$ (arctan integrali)

**Soru:** $x(t) = e^{-at}u(t)$ ($a>0$) için toplam enerjiyi hem zaman hem frekans domeninde bul.

**Zaman domeninde:**
$$E = \int_0^\infty e^{-2at}\,dt = \frac{1}{2a}$$

**Frekans domeninde** (Parseval):
$$E = \frac{1}{2\pi}\int_{-\infty}^{\infty} |X(j\omega)|^2\,d\omega = \frac{1}{2\pi}\int_{-\infty}^{\infty} \frac{1}{a^2+\omega^2}\,d\omega = \frac{1}{2\pi}\cdot\frac{\pi}{a} = \frac{1}{2a} \checkmark$$
