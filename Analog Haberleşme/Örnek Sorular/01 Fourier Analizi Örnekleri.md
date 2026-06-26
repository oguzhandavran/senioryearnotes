---
tags: [analog-haberleşme, fourier, spektrum, örnek-sorular]
---

# 01 — Fourier Analizi Örnekleri

← [[../AH Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Fourier Analizi|02 Fourier Analizi]] | [[../Konu Anlatımları/03 Periyodik İşaretler ve Fourier Serisi|03 Fourier Serisi]]

---

## Örnek 1 — Güç Sinyali FD: $x(t) = e^{3t}u(-t)$

**Soru:** $x(t) = e^{3t}u(-t)$ işaretinin Fourier dönüşümünü bulun.

> [!note]- Semboller
> - $u(-t)$: zaman-ters basamak → $t\le0$ için 1, $t>0$ için 0 (sinyal sadece geçmişte var)
> - $X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt$: Fourier dönüşümü (frekans $f$ Hz cinsinden)
> - Yakınsama koşulu: üstelin reel kısmı $>0$ olduğu uçta integral sıfıra gider
> - $|X(f)|$: genlik spektrumu; $\angle X(f)$: faz spektrumu

**Çözüm:**

$u(-t) = 1$ için $t \leq 0$, 0 için $t > 0$:

$$X(f) = \int_{-\infty}^{0} e^{3t}\,e^{-j2\pi ft}\,dt = \int_{-\infty}^{0} e^{(3-j2\pi f)t}\,dt$$

İntegral: $\text{Re}(3 - j2\pi f) = 3 > 0$ → $t \to -\infty$'da $e^{(3-j2\pi f)t} \to 0$ → yakınsar ✓

$$X(f) = \frac{e^{(3-j2\pi f)t}}{3 - j2\pi f}\Bigg|_{-\infty}^{0} = \frac{1}{3 - j2\pi f} - 0$$

$$\boxed{X(f) = \frac{1}{3 - j2\pi f}}$$

**Genlik:** $|X(f)| = \dfrac{1}{\sqrt{9 + (2\pi f)^2}}$

---

## Örnek 2 — Kaydırılmış Dikdörtgen Darbe FD

**Soru:** $x(t) = \Pi\!\left(\dfrac{t-\tau}{2a}\right)$ işaretinin Fourier dönüşümünü bulun ($0 < a < \tau$).

> [!note]- Semboller
> - $\Pi(\cdot)$: birim dikdörtgen fonksiyon (argüman $|\cdot|<1/2$ iken 1); $\Pi\!\big(\tfrac{t-\tau}{2a}\big)$ → merkez $\tau$, genişlik $2a$
> - $\tau$: zaman kaydırması (gecikme, s); $a$: yarı-genişlik
> - $\text{sinc}(x)=\dfrac{\sin(\pi x)}{\pi x}$ (normalize sinc); Euler: $e^{j\theta}-e^{-j\theta}=2j\sin\theta$
> - Zaman kaydırma teoremi: $x(t-\tau)\leftrightarrow e^{-j2\pi f\tau}X(f)$ → sadece **doğrusal faz** ekler

**Çözüm:**

Merkezi $t = \tau$, genişliği $2a$ dikdörtgen darbe:

$$x(t) = \begin{cases} 1 & \tau - a \leq t \leq \tau + a \\ 0 & \text{diğer} \end{cases}$$

$$X(f) = \int_{\tau-a}^{\tau+a} e^{-j2\pi ft}\,dt = \frac{1}{-j2\pi f}\Big[e^{-j2\pi ft}\Big]_{\tau-a}^{\tau+a}$$

$$= \frac{e^{-j2\pi f(\tau-a)} - e^{-j2\pi f(\tau+a)}}{j2\pi f} = e^{-j2\pi f\tau} \cdot \frac{e^{j2\pi fa} - e^{-j2\pi fa}}{j2\pi f}$$

$$= e^{-j2\pi f\tau} \cdot \frac{2\sin(2\pi fa)}{2\pi f} = e^{-j2\pi f\tau} \cdot 2a\,\text{sinc}(2af)$$

$$\boxed{X(f) = 2a\,e^{-j2\pi f\tau}\,\text{sinc}(2af)}$$

**Yorumlama:**
- Genlik: $|X(f)| = 2a|\text{sinc}(2af)|$ — kaydırma genliği değiştirmez
- Faz: $e^{-j2\pi f\tau}$ → doğrusal faz kaydırma (gecikme $\tau$)

---

## Örnek 3 — Genlik ve Faz Spektrumu

**Soru:** $x(t) = 1 + \sin(2\pi f_c t) + 3\cos(2\pi ft) + 5\sin(2\pi f_m t)$, $f_m < f < f_c$

> [!note]- Semboller
> - $f_c,f,f_m$: taşıyıcı / ara / mesaj frekansları (Hz); DC terim "1" → $f=0$ bileşeni
> - Çift taraflı spektrum: her gerçek kosinüs $A\cos\to \pm f$'de $A/2$ genlikli iki çizgi
> - $\sin(\omega t)=\cos(\omega t-\pi/2)$ → genlik aynı, faz $-\pi/2$
> - Genlik spektrumu **çift** (simetrik), faz spektrumu **tek** (antisimetrik) fonksiyondur

**Çözüm:** $\sin(\omega t) = \cos(\omega t - \pi/2)$ dönüşümünü uygula:

| Terim | $f$ (Hz) | Genlik | Faz |
|-------|----------|--------|-----|
| $1$ | $0$ | $1$ | $0$ |
| $\sin(2\pi f_c t)$ | $\pm f_c$ | $1/2$ | $-\pi/2$ / $+\pi/2$ |
| $3\cos(2\pi ft)$ | $\pm f$ | $3/2$ | $0$ |
| $5\sin(2\pi f_m t)$ | $\pm f_m$ | $5/2$ | $-\pi/2$ / $+\pi/2$ |

**Genlik spektrumu** (simetrik, çift fonksiyon):

```
|X(f)|
  5/2     ←           →     5/2
  3/2      ←         →      3/2
  1/2        ←     →        1/2
   1  ←————|————————————————|→ f
     -fc  -f  -fm  0  fm  f  fc
```

**Faz spektrumu** (antisimetrik, tek fonksiyon):
- $\pm f_m$, $\pm f_c$'de: $-\pi/2$ (pozitif f) / $+\pi/2$ (negatif f)
- $\pm f$'de: faz $= 0$

---

## Örnek 4 — 4 Bileşenli Sinyal Spektrumu

**Soru:** $x(t) = 1 + 3\cos(2\pi \cdot 16t - \pi/6) + \sin(60\pi t) + 5\cos(70\pi t)$

> [!note]- Semboller
> - $\omega=2\pi f$ → frekansı bulmak için açısal terimi $2\pi$'ye böl: $60\pi t\Rightarrow f=30$ Hz, $70\pi t\Rightarrow f=35$ Hz
> - $|c_n|$: $n$. harmoniğin (çift taraflı) genliği $=$ tek-taraflı genliğin yarısı; $\theta_n$: faz açısı
> - Kosinüsün fazı $\pm f$'de işaret değiştirir: $A\cos(\omega t-\phi)\to$ pozitif $f$'de $-\phi$, negatif $f$'de $+\phi$

**Çözüm:**

| Terim | $f$ (Hz) | $|c_n|$ | $\theta_n$ |
|-------|----------|---------|------------|
| $1$ | $0$ | $1$ | $0$ |
| $3\cos(32\pi t - \pi/6)$ | $\pm 16$ | $3/2$ | $\mp\pi/6$ |
| $\sin(60\pi t)=\cos(60\pi t-\pi/2)$ | $\pm 30$ | $1/2$ | $-\pi/2$ / $+\pi/2$ |
| $5\cos(70\pi t)$ | $\pm 35$ | $5/2$ | $0$ |

**Not:** Tek taraflı genlikler çift taraflı spektrumda **ikiye bölünür**.

---

## Örnek 5 — Konvülüsyon (Kayan Pencere)

**Soru:** $h(t)$: $[1,3]$ aralığında genlik 1; $x(t)$: $[0,2]$ aralığında genlik $1/2$. $y(t) = x(t) * h(t)$'yi bulun.

> [!note]- Semboller
> - $*$: konvolüsyon; $y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau$
> - $h(t-\tau)$: $\tau$ ekseninde **ters çevrilip** $t$ kadar kaydırılan darbe
> - Örtüşme uzunluğu $L(t)$ → dikdörtgenlerde $y(t)=(\text{genlik}_x\cdot\text{genlik}_h)\cdot L(t)$
> - Eşit genişlikli iki dikdörtgen → **üçgen**; farklı genişlikte → trapez. Tepe konumu $=$ merkezlerin toplamı

**Çözüm:** $y(t)=\int x(\tau)h(t-\tau)\,d\tau$. $x(\tau)$: $[0,2]$'de $1/2$; $h(t-\tau)$: $1\le t-\tau\le3$ → $t-3\le\tau\le t-1$. Örtüşme aralığı $[\max(0,t-3),\,\min(2,t-1)]$, uzunluğu $L(t)$ → $y(t)=\tfrac12 L(t)$:

| Koşul | Örtüşme uzunluğu $L(t)$ | $y(t)$ |
|-------|---------|--------|
| $t < 1$ | $0$ | $0$ |
| $1 \leq t < 3$ | $\int_0^{t-1}d\tau=t-1$ | $(t-1)/2$ |
| $3 \leq t < 5$ | $\int_{t-3}^{2}d\tau=5-t$ | $(5-t)/2$ |
| $t \geq 5$ | $0$ | $0$ |

**Çıkış:** **Üçgen** şekli (eşit genişlikli iki dikdörtgenin konvolüsyonu). Tepe değer $y=1$, yalnızca $t=3$'te; taban $t=1\to5$.

---

## Örnek 6 — $c_n$ Hesabı ve Çizgi Spektrumu

**Soru:** $f_0 = 1$ Hz, $T_0 = 1$ s, $A = 2$, $\tau = 0.5$ s kare dalga. $c_n$'yi hesapla.

> [!note]- Semboller
> - $T_0$: periyot (s); $f_0=1/T_0$: temel frekans (Hz); $A$: darbe genliği; $\tau$: darbe genişliği
> - $\tau/T_0$: doluluk oranı (duty cycle); $c_n$: $n$. Fourier serisi katsayısı (çizgi spektrumu)
> - $c_n=\dfrac{A\tau}{T_0}\,\text{sinc}\!\big(\tfrac{n\tau}{T_0}\big)$; $c_0=A\tau/T_0$ ortalama (DC) değer
> - $\text{sinc}$ sıfırları tam sayılarda → doluluk $1/2$ iken çift harmonikler ($n=\pm2,\pm4,\dots$) sıfır

**Çözüm:**

$$c_n = \frac{A\tau}{T_0}\,\text{sinc}\!\left(\frac{n\tau}{T_0}\right) = \frac{2 \times 0.5}{1}\,\text{sinc}(0.5n) = \text{sinc}(0.5n)$$

| $n$ | $0.5n$ | $\text{sinc}(0.5n)$ | $c_n$ |
|-----|--------|---------------------|-------|
| $0$ | $0$ | $1$ | $1$ |
| $\pm 1$ | $\pm 0.5$ | $2/\pi \approx 0.637$ | $0.637$ |
| $\pm 2$ | $\pm 1$ | $0$ | $0$ |
| $\pm 3$ | $\pm 1.5$ | $-2/(3\pi) \approx -0.212$ | $-0.212$ |

**Not:** $n = \pm 2$ harmonikleri sıfır — çünkü $\tau/T_0 = 1/2$ → her çift harmonik kaybolur.

---

> [!sinav] Sınav Önce Oku
> - FT: $\int e^{(a-j2\pi f)t}dt$ → sınırlarda yakınsama kontrolü yap
> - Zaman kaydırma sadece faz ekler, genlik sabit kalır
> - Kare dalga $c_n$: doluluk oranı $\times$ sinc → doluluk 1/2 ise çift harmonikler sıfır
> - Konvülüsyon: dikdörtgen ★ dikdörtgen = trapez veya üçgen
