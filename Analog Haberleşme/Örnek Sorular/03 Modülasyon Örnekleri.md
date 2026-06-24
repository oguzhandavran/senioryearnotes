---
tags: [analog-haberleşme, am, dsb-sc, ssb, vsb, modülasyon, güç-analizi, örnek-sorular]
---

# 03 — Modülasyon Örnekleri

← [[../AH Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Genlik Modülasyonu|05 Genlik Modülasyonu]]

---

## Modülasyon Türleri Karşılaştırma Tablosu

$$x_c(t) = \bigl[C_1 + C_2\,x(t)\bigr]\cos(2\pi f_c t) + C_2\,g(t)\sin(2\pi f_c t)$$

| Tür | $C_1$ | $C_2$ | $g(t)$ | Özellik |
|-----|-------|-------|--------|---------|
| **Standart AM** | $A_c$ | $mA_c$ | $0$ | Taşıyıcı var |
| **DSB-SC (ÇYB)** | $0$ | $A_c$ | $0$ | Taşıyıcı yok |
| **SSB-USB (TYB-Üst)** | $0$ | $A_c/2$ | $+\hat{x}(t)$ | Sadece üst yan bant |
| **SSB-LSB (TYB-Alt)** | $0$ | $A_c/2$ | $-\hat{x}(t)$ | Sadece alt yan bant |

$\hat{x}(t)$: $x(t)$'nin **Hilbert dönüşümü** (90° faz kaydırma)

**Örnek:** $x(t) = \sin(2\pi f_m t) \implies \hat{x}(t) = -\cos(2\pi f_m t)$

---

## Örnek 1 — Genelleştirilmiş Modülasyon İndeksi (Karmaşık Mesaj)

**Soru:** Modüle edilmiş dalga $x_c(t) = 2\!\left[1+\dfrac{3}{2}x_1(t)\right]\cos(2\pi f_c t)$ ile veriliyor. $x_1(t)$ kare dalga: max $= 3.5$, min $= 0.5$ ($k=3/2$). Standart AM formuna dönüştürün.

**Çözüm:**

**Adım 1:** $a$ ve $b$ hesapla:

$$a = \frac{\max + \min}{2} = \frac{3.5+0.5}{2} = 2, \qquad b = \frac{\max - \min}{2} = \frac{3.5-0.5}{2} = \frac{3}{2}$$

Yani $x_1(t) = a + b\,x(t) = 2 + \dfrac{3}{2}x(t)$ (burada $x(t)$ normalize edilmiş $[-1,1]$ mesaj)

**Adım 2:** Formüle yerleştir:

$$x_c(t) = 2\!\left[1+\frac{3}{2}\!\left(2+\frac{3}{2}x(t)\right)\right]\cos(2\pi f_c t)$$

$$= 2\!\left[1+3+\frac{9}{4}x(t)\right]\cos(2\pi f_c t) = 2\!\left[4+\frac{9}{4}x(t)\right]\cos(2\pi f_c t)$$

$$= \boxed{8\!\left[1+\frac{9}{16}x(t)\right]\cos(2\pi f_c t)}$$

**Sonuç:** $A_c = 8$, $m = \dfrac{9}{16}$

**Alternatif formül:**

$$m = \frac{kb}{1+ka} = \frac{\frac{3}{2}\cdot\frac{3}{2}}{1+\frac{3}{2}\cdot 2} = \frac{9/4}{4} = \frac{9}{16} \checkmark$$

---

## Örnek 2 — Tek Tonlu AM: Spektrum ve Güç

**Soru:** $x(t) = A_m\cos(2\pi f_m t)$, $A_m \leq 1$ birimiyle tek tonlu mesaj. AM işaretini açın, spektrumu yazın ve gücü hesaplayın.

**Çözüm:**

**AM işareti:**

$$x_c(t) = A_c[1+m\,x(t)]\cos(2\pi f_c t) = A_c\cos(2\pi f_c t) + mA_c\cos(2\pi f_c t)\cos(2\pi f_m t)$$

$\cos A\cos B = \frac{1}{2}[\cos(A-B)+\cos(A+B)]$ kullan:

$$= A_c\cos(2\pi f_c t) + \frac{mA_c}{2}\cos(2\pi(f_c-f_m)t) + \frac{mA_c}{2}\cos(2\pi(f_c+f_m)t)$$

**Spektrum bileşenleri:**

| Bileşen | Frekans | Genlik (tek taraflı) | Güç |
|---------|---------|---------------------|-----|
| Taşıyıcı | $\pm f_c$ | $A_c/2$ | $P_c = A_c^2/2$ |
| Alt yan bant | $\pm(f_c-f_m)$ | $mA_c/4$ | $P_{AYB} = (mA_c)^2/8$ |
| Üst yan bant | $\pm(f_c+f_m)$ | $mA_c/4$ | $P_{ÜYB} = (mA_c)^2/8$ |

**Toplam güç:**

$$P_c = \left(\frac{A_c}{2}\right)^2 \cdot 2 = \frac{A_c^2}{2}$$

$$2P_y = 2\cdot\left(\frac{mA_c}{4}\right)^2 \cdot 2 \cdot 2 = \frac{A_c^2 m^2 A_m^2}{4}$$

$$\boxed{P_T = \frac{A_c^2}{2} + \frac{A_c^2 m^2 A_m^2}{4}}$$

Eğer $A_m = 1$: $P_T = \dfrac{A_c^2}{2}\!\left(1+\dfrac{m^2}{2}\right)$

> [!sinav] Güç Formülü Hafızası
> Her kosinüs teriminin gücü = (genlik)²/2
> $P_c = (A_c)^2/2$, $P_{yan} = (mA_c/2)^2/2$ → her yan bant için ayrı hesapla

---

## Örnek 3 — ÇYB ve TYB (SSB) Karşılaştırmalı

**Soru:** $x(t) = 2\cos(2\pi f_m t)$ mesajı, $f_c$ frekanslı $A_c$ genlikli taşıyıcı ile modüle ediliyor.

**(a)** ÇYB (DSB-SC) işaretini bulun.

**(b)** $a = 0$ için ÇYB, $a = 0.5$ için USB (üst yan bant), $a = -0.5$ için LSB (alt yan bant) olduğunu gösterin.

**Filtre:** $H(f_c+f_m) = 0.5+a$, $H(f_c-f_m) = 0.5-a$

**Çözüm:**

**(a) ÇYB:**

$$x_{DSB}(t) = A_c \cdot x(t)\cos(2\pi f_c t) = 2A_c\cos(2\pi f_m t)\cos(2\pi f_c t)$$

$$= A_c\bigl[\cos(2\pi(f_c+f_m)t) + \cos(2\pi(f_c-f_m)t)\bigr]$$

**Filtre çıkışı:**

$$x_c(t) = A_c(0.5+a)\cos(2\pi(f_c+f_m)t) + A_c(0.5-a)\cos(2\pi(f_c-f_m)t)$$

**(b) Özel durumlar:**

| $a$ | Üst yan bant katsayısı | Alt yan bant katsayısı | Sonuç |
|-----|----------------------|----------------------|-------|
| $0$ | $0.5$ | $0.5$ | ÇYB (her iki ban eşit) |
| $+0.5$ | $1$ | $0$ | **USB — sadece üst** |
| $-0.5$ | $0$ | $1$ | **LSB — sadece alt** |

$a = 0.5$: $x_c(t) = A_c\cos(2\pi(f_c+f_m)t)$ → USB

$a = -0.5$: $x_c(t) = A_c\cos(2\pi(f_c-f_m)t)$ → LSB

**Bant genişliği:** ÇYB → $2f_m$; SSB → $f_m$ (yarısı kadar!)

---

## Örnek 4 — Çarpımsal Modülatör: ÇYB ve TYB

**Soru (Tahta Örneği):** $x(t) = \frac{1}{2}\cos(2\pi \cdot 10^2 t)\cos(4\pi \cdot 10^2 t)$ ve $c(t) = \cos(2\pi f_c t)$ ile:

**(a)** Zaman domenindeki ÇYB ifadesini bulun ($m=1$).

**(b)** Frekans spektrumunu çizin.

**Çözüm:**

**Adım 1:** Mesajı açalım:

$$x(t) = \frac{1}{2}\cos(200\pi t)\cos(400\pi t) = \frac{1}{4}\bigl[\cos(200\pi t) + \cos(600\pi t)\bigr]$$

*(200π-400π = -200π → 200π; 200π+400π = 600π)*

**Adım 2:** ÇYB modülasyon:

$$x_c(t) = A_c\,x(t)\cos(2\pi f_c t) = A_c\cdot\frac{1}{4}\bigl[\cos(200\pi t)+\cos(600\pi t)\bigr]\cos(2\pi f_c t)$$

$\cos A\cos B$ açılımı ile her terim için:

$$= \frac{A_c}{8}\bigl[\cos(2\pi(f_c-100)t)+\cos(2\pi(f_c+100)t)\bigr]$$
$$+\frac{A_c}{8}\bigl[\cos(2\pi(f_c-300)t)+\cos(2\pi(f_c+300)t)\bigr]$$

**Spektrum:** $f_c \pm 100$ Hz ve $f_c \pm 300$ Hz'de genliği $A_c/8$ olan 4 çizgi.

---

## Örnek 5 — Güç Analizi: AM vs DSB-SC Sayısal

**Verilen:** $m(t) = \cos(2\pi \cdot 10^3 t)$, $c(t) = 10\cos(2\pi \cdot 10^6 t)$, $m=1$

| Büyüklük | Standart AM | DSB-SC |
|----------|-------------|--------|
| $x_c(t)$ | $10[1+m(t)]\cos(2\pi\cdot10^6t)$ | $m(t)\cdot10\cos(2\pi\cdot10^6t)$ |
| Açılmış | $10\cos+5\cos(f_c+f_m)+5\cos(f_c-f_m)$ | $5\cos(f_c+f_m)+5\cos(f_c-f_m)$ |
| $P_c$ | $10^2/2 = 50$ W | $0$ W |
| $2P_y$ | $2\times5^2/2 = 25$ W | $2\times5^2/2 = 25$ W |
| $P_T$ | **75 W** | **25 W** |
| $\eta$ | $1/3$ | $1$ |

**Sonuç:** DSB-SC 3 kat daha verimli — taşıyıcı gücü bilgi taşımaz!

---

## Örnek 6 — Modülasyon İndeksi Zarftan

**Soru:** Aşağıdaki AM zarfından modülasyon indeksini bulun:

$$C_{\max} = 10 \text{ V}, \quad C_{\min} = 2 \text{ V}$$

**Çözüm:**

$$m = \frac{C_{\max}-C_{\min}}{C_{\max}+C_{\min}} = \frac{10-2}{10+2} = \frac{8}{12} = \boxed{\frac{2}{3} \approx 0.667}$$

$$A_c = \frac{C_{\max}+C_{\min}}{2} = \frac{10+2}{2} = 6 \text{ V}$$

**Kontrol:** $C_{\max} = A_c(1+m) = 6(1+2/3) = 10$ ✓, $C_{\min} = A_c(1-m) = 6(1/3) = 2$ ✓

---

> [!sinav] Modülasyon Sınavı Özeti
> **AM:** $x_c = A_c[1+mx]\cos(2\pi f_ct)$ → $m=(C_{\max}-C_{\min})/(C_{\max}+C_{\min})$
> **DSB-SC:** $x_c = A_c\,x\cos(2\pi f_ct)$ → taşıyıcı yok, $\eta=1$
> **SSB-USB:** $a=+0.5$ filtresiyle sadece üst yan bant kalır, $BW=W$
> **SSB-LSB:** $a=-0.5$ filtresiyle sadece alt yan bant kalır, $BW=W$
> **Güç:** $P_c=A_c^2/2$, her kosinüs terimi için $(A/2)^2/2 = A^2/8$
