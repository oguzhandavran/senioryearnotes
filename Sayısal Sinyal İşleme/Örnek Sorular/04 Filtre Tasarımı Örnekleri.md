---
tags: [ssi, dsp, filtre, fir, iir, butterworth, örnek-sorular]
---

# 04 — Sayısal Filtre Tasarımı (Örnekler)

← [[SSI Ana Sayfa]] | Teori: [[../Konu Anlatımları/04 Sayısal Filtre Tasarımı]]

---

## Örnek 1 — 2. Derece Butterworth Sayısal LP Filtre (Tam Çözüm)

> [!note]- Semboller
> - $\omega_p,\omega_s$: sayısal geçiş/durdurma (band kenarı) frekansları (rad); $A_p,A_s$: izin verilen zayıflama (dB)
> - $T$: örnekleme periyodu; $\Omega$ (büyük omega): **analog** frekans
> - Prewarping: $\Omega=\frac{2}{T}\tan(\omega/2)$ — bilineer dönüşümün frekans bükmesini telafi eder
> - $N$: filtre derecesi; $\Omega_c$: analog kesim frekansı; $s_k$: analog kutuplar (birim çemberde eşit aralıklı)
> - $H_a(s)$: analog prototip; bilineer $s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}$ ile $H(z)$ sayısal filtreye geçilir
> - $b_i,a_i$: sayısal filtre pay/payda katsayıları

**Şartlar:** $\omega_p = 0.2\pi$ (geçiş), $A_p = 3$ dB; $\omega_s = 0.4\pi$ (durdurma), $A_s = 20$ dB; $T = 1$ s

### Adım 1: Önceden Düzeltme (Prewarping)

$$\Omega_p = \frac{2}{T}\tan\!\left(\frac{\omega_p}{2}\right) = 2\tan(0.1\pi) = 2\tan(18°) \approx 0.6498 \text{ rad/s}$$

$$\Omega_s = 2\tan(0.2\pi) = 2\tan(36°) \approx 1.4531 \text{ rad/s}$$

### Adım 2: Butterworth Derecesi

$$N \geq \frac{\log\!\left(\sqrt{10^{0.1\times20}-1}/\sqrt{10^{0.1\times3}-1}\right)}{\log(\Omega_s/\Omega_p)} = \frac{\log(9.95/1.0)}{\log(1.4531/0.6498)} \approx \frac{0.998}{0.349} \approx 2.86 \implies N=3$$

*Ancak genellikle sınavda $N=2$ verilerek kutup hesabı yapılır:*

### Adım 3: N=2 Analog Prototip ($\Omega_c = \Omega_p = 0.6498$)

Kutuplar: $s_k = \Omega_c e^{j(2k+1)\pi/4}$, $k=0,1$

$$s_1 = 0.6498 e^{j135°} = 0.6498(-\tfrac{\sqrt2}{2}+j\tfrac{\sqrt2}{2}) \approx -0.4596 + j0.4596$$

$$s_2 = 0.6498 e^{j225°} \approx -0.4596 - j0.4596$$

Analog LP:
$$H_a(s) = \dfrac{\Omega_c^2}{(s-s_1)(s-s_2)} = \dfrac{0.4225}{s^2 + 0.9192s + 0.4225}$$

### Adım 4: Bilineer Dönüşüm ($s = 2(1-z^{-1})/(1+z^{-1})$)

$$\boxed{H(z) = \frac{0.4225(1+z^{-1})^2}{4(1-z^{-1})^2 + 0.9192\cdot2(1-z^{-1})(1+z^{-1}) + 0.4225(1+z^{-1})^2}}$$

Standart biçim:
$$H(z) = \frac{b_0 + b_1 z^{-1} + b_2 z^{-2}}{1 + a_1 z^{-1} + a_2 z^{-2}}, \quad b_0=b_2, \; b_1 = 2b_0 \text{ (LP için)}$$

> [!sinav] Butterworth Sınav Tüyosu
> - Kutuplar birim çemberde eşit aralıklı (asimptotik formül)
> - $N=2$: kutuplar $\pm 135°$ → $s^2 + \sqrt{2}\,\Omega_c s + \Omega_c^2 = 0$
> - Prewarping'i atlama! $\Omega_c \neq \omega_c/T$ — her zaman $2\tan(\omega/2)$ kullan
> - Bilinear dönüşüm tüm frekansları $[-\pi,\pi]$'ye eşler → aliasing yok

---

## Örnek 2 — Fark Denklemi → Z-TF → FIR/IIR Tayini

> [!note]- Semboller
> - $x[n],y[n]$: giriş/çıkış; $y[n-1]$: geri besleme terimi (geçmiş çıkış)
> - $H(z)=Y(z)/X(z)$: transfer fonksiyonu; kutup $z=0.5$, $|z|<1$ → kararlı
> - **IIR**: paydada geri besleme → sonsuz dürtü yanıtı; **FIR**: yalnız $x$ terimleri → sonlu, daima kararlı
> - $h[n]$: dürtü yanıtı ($x=\delta$ girişine çıkış)

**Verilen:** $y[n] = x[n] + 0.5y[n-1]$

**Çözüm:**

Z-dönüşümü:
$$Y(z) = X(z) + 0.5z^{-1}Y(z) \implies H(z) = \frac{1}{1-0.5z^{-1}} = \frac{z}{z-0.5}$$

- **Kutup:** $z = 0.5$ → $|0.5| < 1$ → **kararlı** ✓
- **IIR:** geri besleme ($y[n-1]$ terimi) var → sonsuz impuls yanıtı
- İmpuls yanıtı: $h[n] = (0.5)^n u[n]$ → üstel azalma

**FIR karşılaştırması:**

$y[n] = x[n] + 0.3x[n-1]$ → $H(z) = 1 + 0.3z^{-1}$ → sadece sıfır; kutup yok → **FIR**

---

## Bağlantılı Notlar

- [[../Konu Anlatımları/04 Sayısal Filtre Tasarımı]]
- [[03 DFT-FFT Örnekleri]]
- [[02 Z-Dönüşümü Örnekleri]]
