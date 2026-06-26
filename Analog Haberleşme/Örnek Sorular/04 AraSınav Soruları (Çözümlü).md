---
tags: [analog-haberleşme, arasınav, çözümlü, fourier, am, dsb-sc, konvülüsyon, örnek-sorular]
---

# 04 — AraSınav Soruları (Çözümlü)

← [[../AH Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Genlik Modülasyonu|05 Genlik Modülasyonu]]

*Kaynak: Analog Haberleşme Ara Sınavı 2025–2026 Bahar*

---

## Soru 1 — Kaydırılmış Kare Dalganın Fourier Dönüşümü

**Soru:** $x(t) = \Pi\!\left(\dfrac{t-\tau}{2a}\right)$ işaretinin Fourier dönüşümünü bulunuz ($0 < a < \tau$).

> [!note]- Semboller
> - $\Pi(\cdot)$: birim dikdörtgen; $\Pi\!\big(\tfrac{t-\tau}{2a}\big)$ → merkez $\tau$, genişlik $2a$
> - $\tau$: gecikme (s); $a$: yarı-genişlik; $\text{sinc}(x)=\sin(\pi x)/(\pi x)$
> - FT çifti: $\Pi(t/2a)\leftrightarrow 2a\,\text{sinc}(2af)$; zaman kaydırma $\to e^{-j2\pi f\tau}$ faz çarpanı

**Çözüm:**

Merkezi $\tau$, genişliği $2a$ dikdörtgen darbe. İntegrasyon sınırları: $[\tau-a,\; \tau+a]$.

$$X(f) = \int_{\tau-a}^{\tau+a} 1 \cdot e^{-j2\pi ft}\,dt$$

$t = \tau + u$ değişken dönüşümü ($u$: $-a$'dan $+a$'ya):

$$X(f) = e^{-j2\pi f\tau}\int_{-a}^{a} e^{-j2\pi fu}\,du = e^{-j2\pi f\tau} \cdot 2a\,\text{sinc}(2af)$$

$$\boxed{X(f) = 2a\,e^{-j2\pi f\tau}\,\text{sinc}(2af)}$$

**Alternatif yol (FT çifti + zaman kaydırma):**

$\Pi(t/2a) \leftrightarrow 2a\,\text{sinc}(2af)$ çiftini kullan, sonra $t \to t-\tau$ kaydırma özelliği:

$$\Pi\!\left(\frac{t-\tau}{2a}\right) \leftrightarrow 2a\,\text{sinc}(2af) \cdot e^{-j2\pi f\tau}$$

---

## Soru 2 — Genlik ve Faz Spektrumları

**Soru:** $x(t) = 1 + \sin(2\pi f_c t) + 3\cos(2\pi ft) + 5\sin(2\pi f_m t)$, $f_m < f < f_c$, spektrumları çiziniz.

> [!note]- Semboller
> - $f_c,f,f_m$: bileşen frekansları (Hz); "1" → DC ($f=0$)
> - $\sin(\omega t)=\cos(\omega t-\pi/2)$ → genlik aynı, faz $-\pi/2$ kazanır
> - Çift taraflı spektrum: tek-taraflı genlik $A$ → $\pm f$'de $A/2$
> - Genlik spektrumu **çift**, faz spektrumu **tek** (negatif $f$'de faz işareti ters)

**Çözüm:**

**Adım 1:** Tüm terimleri kosinüs formuna çevir:

$$\sin(\omega t) = \cos(\omega t - \pi/2)$$

| Bileşen | $f$ (Hz) | Genlik $A$ | Faz $\theta$ |
|---------|----------|-----------|--------------|
| DC: $1$ | $0$ | $1$ | $0$ |
| $\sin(2\pi f_c t)$ | $f_c$ | $1$ | $-\pi/2$ |
| $3\cos(2\pi ft)$ | $f$ | $3$ | $0$ |
| $5\sin(2\pi f_m t)$ | $f_m$ | $5$ | $-\pi/2$ |

**Adım 2:** Çift taraflı spektruma çevir (tek taraflı genlik → $A/2$ her iki tarafta):

**Genlik spektrumu** $|X(f)|$:

```
|X(f)|
 5/2 |       |           |       |
     |   |   |           |   |
 3/2 |   |   |   |   |   |   |   |
 1/2 |   |   |   |   |   |   |   |
  1  |---+---+---+---+---+---+---→ f
    -fc  -f  -fm  0   fm   f   fc
```

**Faz spektrumu** $\angle X(f)$ (antisimetrik):
- $f = f_m, f_c$: faz $= -\pi/2$ (kosinüse çevirince negatif)
- $f = -f_m, -f_c$: faz $= +\pi/2$
- $f = f$: faz $= 0$
- $f = 0$: faz $= 0$

---

## Soru 3 — Konvülüsyon ile Çıkış İşareti

**Soru:** $x(t)$: $[0,3]$'te genlik 1; $h(t)$: $[1,3]$'te genlik 1. $y(t) = x(t) * h(t)$'yi bulun.

> [!note]- Semboller
> - $*$: konvolüsyon; $y(t)=\int x(\tau)h(t-\tau)\,d\tau$
> - $h(t-\tau)$: ters çevrilip $t$ kadar kaydırılmış darbe → $[t-3,t-1]$
> - Genlik 1 dikdörtgenlerde $y(t)=$ örtüşme uzunluğu
> - Farklı genişlik ($3\ne2$) → **trapez**; başlangıç/bitiş $=$ kenar toplamları, plato genişliği $=$ genişlik farkı

**Çözüm:** $h(t-\tau)$, $\tau$-ekseninde $[t-3,\,t-1]$ aralığını kaplar; $x(\tau)$ ise $[0,3]$'te 1. Örtüşme $=[\max(0,t-3),\,\min(3,t-1)]$, uzunluğu $y(t)$:

| Bölge | Koşul | Örtüşme aralığı | $y(t)$ |
|-------|-------|---------|--------|
| 1 | $t < 1$ | yok | $0$ |
| 2 | $1 \leq t < 3$ | $[0,\,t-1]$ | $t - 1$ |
| 3 | $3 \leq t < 4$ | $[t-3,\,t-1]$ | $2$ |
| 4 | $4 \leq t < 6$ | $[t-3,\,3]$ | $6 - t$ |
| 5 | $t \geq 6$ | yok | $0$ |

**Şekil:** Trapez — $t=1$'de yükselmeye başlar, $t=2$'de $y=1$, $t=3$'te $y=2$, $t=4$'e kadar $y=2$ (plato), $t=6$'da $y=0$. Plato genişliği $=|3-2|=1$ (genişlik farkı), tepe $=\min(3,2)\times1=2$.

*Genel kural: iki dikdörtgen konvülüsyonu → çıkış trapez (veya üçgen, genişlikler eşitse).*

---

## Soru 4 — AM ve DSB-SC Güç Karşılaştırması

**Verilen:** $m(t) = \cos(2\pi \cdot 10^3 t)$, $c(t) = 10\cos(2\pi \cdot 10^6 t)$, $m = 1$

> [!note]- Semboller
> - $m(t)$: mesaj ($f_m=10^3$ Hz); $c(t)$: taşıyıcı ($A_c=10$, $f_c=10^6$ Hz); $m$: modülasyon indeksi
> - $P_c=A_c^2/2$: taşıyıcı gücü; $2P_y$: iki yan bant toplam gücü; $P_T=P_c+2P_y$
> - $\eta=2P_y/P_T$: güç verimliliği; AM'de $\eta=1/3$, DSB-SC'de $\eta=1$
> - Yan bant frekansları $f_c\pm f_m$: $0.999\cdot10^6$ ve $1.001\cdot10^6$ Hz

### a) Zaman Domeni İfadeleri

**Standart AM** ($m_n(t) = m(t)$ normalize mesaj):

$$s_{AM}(t) = A_c[1 + m \cdot m(t)]\cos(2\pi f_c t) = 10[1 + \cos(2\pi \cdot 10^3 t)]\cos(2\pi \cdot 10^6 t)$$

Açılmış hali:

$$s_{AM}(t) = 10\cos(2\pi \cdot 10^6 t) + 5\cos(2\pi \cdot 1.001 \cdot 10^6 t) + 5\cos(2\pi \cdot 0.999 \cdot 10^6 t)$$

**DSB-SC:**

$$s_{DSB}(t) = m(t) \cdot c(t) = \cos(2\pi \cdot 10^3 t) \cdot 10\cos(2\pi \cdot 10^6 t)$$

$$= 5\cos(2\pi \cdot 1.001 \cdot 10^6 t) + 5\cos(2\pi \cdot 0.999 \cdot 10^6 t)$$

### b) Toplam Güç Hesabı

| Parametre | Standart AM | DSB-SC |
|-----------|-------------|--------|
| Taşıyıcı gücü $P_c$ | $10^2/2 = 50$ W | $0$ W |
| Yan bant gücü $2P_y$ | $2 \times 5^2/2 = 25$ W | $2 \times 5^2/2 = 25$ W |
| **Toplam $P_T$** | **$75$ W** | **$25$ W** |
| Verimlilik $\eta$ | $25/75 = 1/3$ | $25/25 = 1$ |

> [!sinav] Kritik Sonuç
> AM'de taşıyıcı 50 W güç tüketir ama bilgi taşımaz!
> DSB-SC'de bu israf yoktur → 3× daha verimli.

---

## Soru 5 — Çarpımsal Modülatör ve Spektrum

**Verilen:** $x(t) = 4\cos(20\pi t)$, $c(t) = 10\cos(1000\pi t)$

> [!note]- Semboller
> - $x(t)$: mesaj; $c(t)$: taşıyıcı; çarpımsal modülatör $\to$ ÇYB (DSB-SC) çıkışı $x(t)c(t)$
> - $\omega=2\pi f$: $1000\pi t\Rightarrow f_c=500$ Hz, $20\pi t\Rightarrow f_m=10$ Hz
> - $\cos A\cos B=\tfrac12[\cos(A-B)+\cos(A+B)]$ → iki yan bant $f_c\pm f_m$
> - $BW=2f_m=2W$: ÇYB'de bant genişliği mesajın iki katı

### a) Çıkış Sinyali

$$x_c(t) = x(t) \cdot c(t) = 4\cos(20\pi t) \cdot 10\cos(1000\pi t) = 40\cos(20\pi t)\cos(1000\pi t)$$

$\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$ özdeşliğini kullan:

$$\boxed{x_c(t) = 20\cos(980\pi t) + 20\cos(1020\pi t)}$$

### b) Frekans Spektrumu (Hz Cinsinden)

- $f_c = 1000\pi/(2\pi) = 500$ Hz
- $f_m = 20\pi/(2\pi) = 10$ Hz
- Alt yan bant: $f_c - f_m = 490$ Hz
- Üst yan bant: $f_c + f_m = 510$ Hz

Spektrum: $\pm 490$ Hz ve $\pm 510$ Hz'de genliği 10 olan impulslar.

```
|X_c(f)|
  10 |   |               |   |
     |   |               |   |
  ———+———+———+———+———+———+———+———→ f (Hz)
    -510-490   0       490 510
```

### c) Minimum Bant Genişliği

$$BW = f_{\text{üst}} - f_{\text{alt}} = 510 - 490 = 20 \text{ Hz} = 2f_m$$

Genel formül: $BW = 2W$ (DSB tipi modülasyon).

---

## Ek Örnek — Genelleştirilmiş Modülasyon İndeksi

**Soru:** $x_c(t) = 2\left[1 + \frac{3}{2}x_1(t)\right]\cos(2\pi f_c t)$

$x_1(t)$ kare dalga: max değer $3.5$, min değer $0.5$ (ortalama $a = 2$, $k = 3/2$)

> [!note]- Semboller
> - $x_1(t)$: ham mesaj; $x(t)=(x_1-a)/b$: $[-1,1]$ normalize mesaj
> - $a=\dfrac{\max+\min}{2}$ (DC), $b=\dfrac{\max-\min}{2}$ (tepe sapması)
> - $m=\dfrac{kb}{1+ka}$: modülasyon indeksi; $A_c=A_1(1+ka)$: efektif taşıyıcı genliği ($A_1=2$ verilen önçarpan)

**Çözüm:**

$$a = \langle x_1(t)\rangle = \frac{3.5 + 0.5}{2} = 2, \qquad b = 3.5 - 2 = \frac{3}{2}$$

$$m = \frac{kb}{1 + ka} = \frac{\frac{3}{2} \cdot \frac{3}{2}}{1 + \frac{3}{2} \cdot 2} = \frac{9/4}{4} = \frac{9}{16}$$

$$A_c = A_1(1 + ka) = 2\!\left(1 + \frac{3}{2} \cdot 2\right) = 2 \times 4 = 8$$

$$\boxed{x_c(t) = 8\!\left(1 + \frac{9}{16}\,x(t)\right)\cos(2\pi f_c t)}$$

Burada $x(t) = [x_1(t) - a]/b$ normalize edilmiş mesaj işaretidir.

---

> [!sinav] Sınav Öncesi Hızlı Özet
> 1. **FT hesabı:** İntegrasyon sınırlarını belirle → üstel integral → sinc formuna getir → zaman kaydırma faz çarpanı ekler
> 2. **Spektrum çizimi:** sin → cos(-π/2) dönüşümü → tabloya yaz → çift taraflı çiz (genlik ikiye böl)
> 3. **Konvülüsyon:** başlangıç ve bitiş = sınırlar toplamı; dikdörtgen★dikdörtgen=trapez
> 4. **AM güç:** $P_T = P_c + 2P_y = A_c^2/2 \times (1 + m^2/2)$ tek ton için
> 5. **DSB-SC güç:** $P_T = A_c^2\langle m^2\rangle/2$ — taşıyıcı yok
> 6. **Modülasyon indeksi:** $m = (C_{\max}-C_{\min})/(C_{\max}+C_{\min})$
