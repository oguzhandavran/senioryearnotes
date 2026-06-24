---
tags: [analog-haberleşme, fourier, spektrum, ft-özellikleri, konu-anlatımı]
---

# 02 — Fourier Analizi

← [[../AH Ana Sayfa]] | Önceki: [[01 Genel Haberleşme Sistemi]] | Sonraki: [[03 Periyodik İşaretler ve Fourier Serisi]]

---

## Fourier Dönüşümü Tanımı

> [!tanim] Fourier Dönüşümü (f-konvansiyonu)
> $$\boxed{X(f) = \int_{-\infty}^{\infty} x(t)\,e^{-j2\pi ft}\,dt}$$
> $$\boxed{x(t) = \int_{-\infty}^{\infty} X(f)\,e^{j2\pi ft}\,df}$$

> [!warning] Konvansiyon Uyarısı
> Bu derste **f (Hz) konvansiyonu** kullanılır, $\omega$ (rad/s) değil!
> - SS dersindeki $X(j\omega)$ yerine burada $X(f)$
> - $e^{-j\omega t}$ yerine $e^{-j2\pi ft}$
> - Türev özelliği: $(j2\pi f)^n$ (SS'deki $(j\omega)^n$ değil!)

---

## Genlik ve Faz Spektrumu

$X(f)$ genellikle karmaşık sayıdır. Bunu iki gerçel fonksiyona ayırırız:

$$X(f) = |X(f)|\,e^{j\angle X(f)}$$

| Spektrum | Tanım | Özellik |
|---------|-------|---------|
| **Genlik spektrumu** | $\|X(f)\|$ | $x(t)$ gerçekse: $\|X(f)\| = \|X(-f)\|$ (çift) |
| **Faz spektrumu** | $\angle X(f)$ | $x(t)$ gerçekse: $\angle X(f) = -\angle X(-f)$ (tek) |

---

## Örnek — 4 Bileşenli Sinyal

$$x(t) = 1 + 3\cos(2\pi \cdot 16t - \pi/6) + \sin(60\pi t) + 5\cos(70\pi t)$$

**Not:** $\sin(\omega t) = \cos(\omega t - \pi/2)$ dönüşümünü kullan.

| Terim | $f$ (Hz) | Genlik | Faz |
|-------|----------|--------|-----|
| $1$ | $0$ | $1$ | $0$ |
| $3\cos(2\pi\cdot16t - \pi/6)$ | $16$ | $3$ | $-\pi/6$ |
| $\sin(60\pi t) = \cos(60\pi t - \pi/2)$ | $30$ | $1$ | $-\pi/2$ |
| $5\cos(70\pi t)$ | $35$ | $5$ | $0$ |

Tek taraflı gösterim → çift taraflı spektrumda genlikler **ikiye bölünür** ($\pm f$ konumlarına).

---

## Fourier Dönüşümü Özellikleri

| Özellik | Zaman $x(t)$ | Frekans $X(f)$ |
|---------|-------------|----------------|
| **Doğrusallık** | $ax(t) + by(t)$ | $aX(f) + bY(f)$ |
| **Zaman kaydırma** | $x(t - t_0)$ | $e^{-j2\pi ft_0}X(f)$ |
| **Frekans kaydırma** | $x(t)e^{j2\pi f_0 t}$ | $X(f - f_0)$ |
| **Ölçekleme** | $x(at)$ | $\dfrac{1}{|a|}X\!\left(\dfrac{f}{a}\right)$ |
| **Konvülüsyon** | $x(t) * h(t)$ | $X(f) \cdot H(f)$ |
| **Çarpma** | $x(t) \cdot y(t)$ | $X(f) * Y(f)$ |
| **Türev** | $x^{(n)}(t)$ | $(j2\pi f)^n X(f)$ |
| **Parseval** | $\int\|x\|^2\,dt$ | $\int\|X\|^2\,df$ |
| **Dualite** | $X(t)$ | $x(-f)$ |

> [!sinav] Zaman Kaydırma
> $x(t-t_0) \leftrightarrow e^{-j2\pi ft_0}X(f)$
> - Genlik değişmez: $|e^{-j2\pi ft_0}X(f)| = |X(f)|$
> - Faza doğrusal ek gelir: $-2\pi ft_0$

---

## Önemli FD Çiftleri

| $x(t)$ | $X(f)$ | Not |
|--------|--------|-----|
| $\delta(t)$ | $1$ | Birim darbe |
| $\delta(t - t_0)$ | $e^{-j2\pi ft_0}$ | Gecikmeli darbe |
| $1$ | $\delta(f)$ | Sabit işaret |
| $e^{j2\pi f_0 t}$ | $\delta(f - f_0)$ | Kompleks üstel |
| $\cos(2\pi f_0 t)$ | $\tfrac{1}{2}[\delta(f-f_0)+\delta(f+f_0)]$ | |
| $\sin(2\pi f_0 t)$ | $\tfrac{1}{2j}[\delta(f-f_0)-\delta(f+f_0)]$ | |
| $A\,\Pi(t/\tau)$ | $A\tau\,\text{sinc}(f\tau)$ | Dikdörtgen darbe |
| $A\tau\,\text{sinc}(\tau t)$ | $A\,\Pi(f/\tau)$ | Dualite ile |
| $e^{-at}u(t)$, $a>0$ | $\dfrac{1}{a + j2\pi f}$ | Tek taraflı üstel |
| $e^{-a\|t\|}$, $a>0$ | $\dfrac{2a}{a^2 + (2\pi f)^2}$ | Çift taraflı üstel |
| $u(t)$ | $\tfrac{1}{2}\delta(f) + \dfrac{1}{j2\pi f}$ | Basamak |

---

## Dikdörtgen Darbe — FD Türetmesi

$$x(t) = A\,\Pi\!\left(\frac{t}{\tau}\right) = \begin{cases} A & |t| \leq \tau/2 \\ 0 & |t| > \tau/2 \end{cases}$$

$$X(f) = \int_{-\tau/2}^{\tau/2} A\,e^{-j2\pi ft}\,dt = \frac{A}{-j2\pi f}\Big[e^{-j2\pi ft}\Big]_{-\tau/2}^{\tau/2}$$

$$= \frac{A}{\pi f}\sin(\pi f\tau) = A\tau\,\text{sinc}(f\tau)$$

$$\boxed{A\,\Pi\!\left(\frac{t}{\tau}\right) \leftrightarrow A\tau\,\text{sinc}(f\tau)}$$

---

## Frekans Kaydırma — Modülasyonun Temeli

$$\boxed{x(t)\cos(2\pi f_0 t) \leftrightarrow \frac{1}{2}\bigl[X(f-f_0) + X(f+f_0)\bigr]}$$

Bu özellik modülasyonun frekans alanındaki temel açıklamasıdır:
- Mesaj spektrumu $X(f)$ taşıyıcı frekansı $f_0$ etrafına **kopyalanır**
- Sol kopy: $X(f+f_0)$, sağ kopya: $X(f-f_0)$
- Her kopyanın genliği **yarıya düşer** ($1/2$ çarpanı)

---

## Güç İşaretleri için Özel FD Çiftleri

Güç işaretleri $(E = \infty)$ için standart FD integral yakınsamaz; impuls kullanılır:

| İşaret | $X(f)$ |
|--------|--------|
| $e^{j2\pi f_0 t}$ | $\delta(f - f_0)$ |
| $\cos(2\pi f_0 t)$ | $\tfrac{1}{2}[\delta(f-f_0)+\delta(f+f_0)]$ |
| $u(t)$ | $\tfrac{1}{2}\delta(f) + \tfrac{1}{j2\pi f}$ |

---

> [!sinav] Sınav İpucu
> - Kare → f alanında sinc; sinc → f alanında kare (dualite)
> - Zaman kaydırma: sadece faza etki, genlik sabit kalır
> - $\cos$ çarparak modüle etmek = spektrumu $\pm f_c$'ye taşımak + $1/2$ katsayısı
> - $\sin(\omega t) = \cos(\omega t - \pi/2)$ → faz $-\pi/2$ ekler
