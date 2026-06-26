---
tags: [ssi, dsp, z-dönüşümü, roc, pfd, örnek-sorular]
---

# 02 — Z-Dönüşümü (Örnekler)

← [[SSI Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Z-Dönüşümü]]

---

## Örnek 1 — PFD ile Ters Z-Dönüşümü (Sınav Sorusundan)

> [!note]- Semboller
> - $X(z)$: Z-dönüşümü; $z^{-1}$: birim gecikme operatörü
> - PFD (kısmi kesirler): paydayı çarpanlara ayırıp basit terimlere böl
> - $A,B$: kalıntı (residue) katsayıları; her biri ilgili kutupta hesaplanır
> - Ters çift: $\dfrac{1}{1-pz^{-1}}\leftrightarrow p^n u[n]$ (nedensel, $|z|>|p|$); kutuplar burada $p=\tfrac13,\,-\tfrac12$

**Verilen:** *(payda nedensel; kutuplar $\tfrac13$ ve $-\tfrac12$)*
$$X(z) = \frac{1}{1+\frac{1}{6}z^{-1}-\frac{1}{6}z^{-2}}$$

**Çözüm:**

Paydayı çarpanlara ayır: $1+\tfrac{1}{6}z^{-1}-\tfrac{1}{6}z^{-2}=(1-\tfrac{1}{3}z^{-1})(1+\tfrac{1}{2}z^{-1})$

$$X = \frac{A}{1-\frac{1}{3}z^{-1}} + \frac{B}{1+\frac{1}{2}z^{-1}}$$

$A = \left.(1-\frac{1}{3}z^{-1})X(z)\right|_{z^{-1}=3} = \frac{1}{1+\frac{3}{2}} = \frac{2}{5}$

$B = \left.(1+\frac{1}{2}z^{-1})X(z)\right|_{z^{-1}=-2} = \frac{1}{1+\frac{2}{3}} = \frac{3}{5}$

$$\boxed{x[n] = \frac{2}{5}\left(\frac{1}{3}\right)^n u[n] + \frac{3}{5}\left(-\frac{1}{2}\right)^n u[n]}$$

---

## Örnek 2 — ROC ile Doğru Ters Z (Tam Çözüm)

> [!note]- Semboller
> - $X(z)$: Z-dönüşümü; kutuplar $z=1,2$; **ROC** $|z|>2$ → nedensel (sağ taraflı)
> - $X(z)/z$ ile böl: kalıntı yöntemi için standart hile
> - $A,B$: kalıntı katsayıları; ters çift $\dfrac{z}{z-p}\leftrightarrow p^n u[n]$
> - ROC $|z|<1$ olsaydı sol taraflı: $-p^n u[-n-1]$

**Verilen:**
$$X(z) = \frac{z^2}{(z-1)(z-2)}, \quad \text{ROC: } |z|>2 \text{ (nedensel)}$$

**Çözüm:**

$X(z)/z = z/[(z-1)(z-2)] = A/(z-1) + B/(z-2)$

$A = (z-1)\cdot X(z)/z\big|_{z=1} = 1/(1-2) = -1$

$B = (z-2)\cdot X(z)/z\big|_{z=2} = 2/(2-1) = 2$

$X(z)/z = -1/(z-1) + 2/(z-2) \implies X(z) = \frac{-z}{z-1} + \frac{2z}{z-2}$

$$\boxed{x[n] = -u[n] + 2\cdot2^n u[n] = (-1+2^{n+1})u[n]}$$

*ROC $|z|<1$ olsaydı: $x[n] = u[-n-1] - 2\cdot2^n u[-n-1]$ (sol taraflı sinyal)*

---

## Örnek 3 — Birim Gecikme İspatı (Sınav Sorusu)

> [!note]- Semboller
> - $\mathcal{Z}\{\cdot\}$: Z-dönüşümü operatörü; $X(z)=\sum_n x[n]z^{-n}$ (tanım)
> - $x[n-1]$: bir örnek gecikmiş dizi
> - $m=n-1$: indeks değişken dönüşümü (toplam sınırları değişmez, $\pm\infty$)
> - Sonuç: gecikme ↔ $z^{-1}$ çarpanı (zaman kaydırma özelliği)

**İste:** $\mathcal{Z}\{x[n-1]\} = z^{-1}X(z)$ olduğunu göster.

**Çözüm:**

$$\mathcal{Z}\{x[n-1]\} = \sum_{n=-\infty}^{\infty}x[n-1]z^{-n}$$

$m = n-1$ değişken dönüşümü:

$$= \sum_{m=-\infty}^{\infty}x[m]z^{-(m+1)} = z^{-1}\sum_m x[m]z^{-m} = z^{-1}X(z) \quad \checkmark$$

---

## Örnek 4 — Fark Denklemi → Transfer Fonksiyonu

> [!note]- Semboller
> - $x[n],y[n]$: giriş/çıkış; $y[n-1]$: geri besleme (geçmiş çıkış)
> - $H(z)=Y(z)/X(z)$: transfer fonksiyonu; kutup $z=0.5$ ($|z|<1$ → kararlı)
> - **IIR**: geri besleme var → sonsuz dürtü yanıtı; **FIR**: yalnız giriş terimleri → sonlu
> - $h[n]$: dürtü yanıtı ($x[n]=\delta[n]$ verince çıkış)

**Verilen:** $y[n] = x[n] + 0.5y[n-1]$

**Çözüm:**

Z-dönüşümü:
$$Y(z) = X(z) + 0.5z^{-1}Y(z) \implies H(z) = \frac{Y(z)}{X(z)} = \frac{1}{1-0.5z^{-1}} = \frac{z}{z-0.5}$$

- **Kutup:** $z = 0.5$ → $|0.5| < 1$ → **kararlı** ✓
- **IIR:** geri besleme ($y[n-1]$ terimi) var → sonsuz impuls yanıtı
- İmpuls yanıtı: $h[n] = (0.5)^n u[n]$

**FIR karşılaştırması:** $y[n] = x[n] + 0.3x[n-1]$ → $H(z) = 1 + 0.3z^{-1}$ → sıfır var, kutup yok → FIR

---

## Bağlantılı Notlar

- [[../Konu Anlatımları/02 Z-Dönüşümü]]
- [[01 Örnekleme Örnekleri]]
- [[03 DFT-FFT Örnekleri]]
