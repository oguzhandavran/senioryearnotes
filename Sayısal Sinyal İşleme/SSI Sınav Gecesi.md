---
tags: [ssi, dsp, sinav-gecesi, ozet]
---

# SSI — Sınav Gecesi Özeti

> Tek sayfa. Her şey burada.

---

## 1 — Sistem Özellikleri (Hızlı Test)

| Özellik | Test |
|---------|------|
| Hafızasız | $y[n]$ sadece $x[n]$'e bağlı mı? |
| Nedensel | $x[n+k]$, $k>0$ yok mu? |
| Doğrusal | $T\{ax_1+bx_2\}=aT\{x_1\}+bT\{x_2\}$ ve $x=0 \Rightarrow y=0$ |
| ZD | Katsayılarda $n$ yok mu? |
| BIBO Kararlı | $\sum|h[n]| < \infty$ |

**Örnek:** $y[n]=nx[n]$ → Doğrusal ✓, ZD Değil ✗

---

## 2 — Örnekleme Teoremi

$$f_s > 2f_{max} \quad \text{(Nyquist)}$$

Alias frekansı: $f_a = |f - kf_s|$ (en küçük $k$ için)

Dijital açısal frekans: $\omega = 2\pi f/f_s = \Omega T_s$

---

## 3 — Z-Dönüşümü

$$X(z) = \sum_{n=-\infty}^{\infty} x[n]z^{-n}$$

| $x[n]$ | $X(z)$ | ROC |
|--------|--------|-----|
| $\delta[n]$ | $1$ | tüm $z$ |
| $u[n]$ | $z/(z-1)$ | $\|z\|>1$ |
| $a^n u[n]$ | $z/(z-a)$ | $\|z\|>\|a\|$ |
| $-a^n u[-n-1]$ | $z/(z-a)$ | $\|z\|<\|a\|$ |
| $na^n u[n]$ | $az^{-1}/(1-az^{-1})^2$ | $\|z\|>\|a\|$ |

**Özellikler:**
- Gecikme: $x[n-k] \leftrightarrow z^{-k}X(z)$
- Son değer: $x[\infty] = \lim_{z\to1}(z-1)X(z)$ (kararlıysa)
- Konvolüsyon: $x*h \leftrightarrow X\cdot H$

**Kararlılık:** Tüm kutuplar birim çemberin **içinde** ($|p|<1$).

**Ters Z (PFD):** $X(z)/z$ kısmi kesirlere ayır → $z$ ile çarp → çiftleri kullan.

---

## 4 — DFT

$$X[k] = \sum_{n=0}^{N-1}x[n]W_N^{kn}, \quad W_N = e^{-j2\pi/N}$$

$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1}X[k]W_N^{-kn}$$

**Parseval:** $\sum|x[n]|^2 = \frac{1}{N}\sum|X[k]|^2$

**Döngüsel konvolüsyon = DFT domeninde çarpım.**

Lineer → döngüsel: her ikiyi **sıfırla doldur** ($N \geq L_x+L_h-1$), DFT al, çarp, ters DFT.

**FFT:** $O(N^2) \to O(N\log_2 N)$; $N=2^m$ olmalı.

---

## 5 — İdeal Filtreler

$$h_{LP}[n] = \frac{\sin(\omega_c n)}{\pi n} = \frac{\omega_c}{\pi}\operatorname{sinc}(\omega_c n), \quad h[0]=\frac{\omega_c}{\pi}$$

$$h_{HP}[n] = \delta[n] - h_{LP}[n]$$

$$H_{BS} = 1 - H_{BP}, \quad H_{HP} = 1 - H_{LP}$$

---

## 6 — FIR vs IIR

| | FIR | IIR |
|-|-----|-----|
| Kararlılık | Her zaman ✅ | Kutuplara bağlı |
| Faz | Doğrusal faz ✅ | Zor |
| Tasarım | Pencele $h_d[n]$ | Bilineer dönüşüm |

**FIR doğrusal faz:** $h[n] = h[N-1-n]$ (simetrik)

---

## 7 — Bilineer Dönüşüm (IIR)

$$s = \frac{2}{T}\cdot\frac{1-z^{-1}}{1+z^{-1}}$$

**Prewarping:** $\Omega_c = \frac{2}{T}\tan\!\left(\frac{\omega_c}{2}\right)$

**Butterworth derecesi:**
$$N \geq \frac{\log\!\sqrt{\frac{10^{0.1A_s}-1}{10^{0.1A_p}-1}}}{\log(\Omega_s/\Omega_p)}$$

$N=2$ kutup: $s_{1,2} = \Omega_c e^{\pm j135°}$ → $H_a = \Omega_c^2/(s^2+\sqrt{2}\Omega_c s+\Omega_c^2)$

---

## Tuzaklar

> [!warning] SSI Sınav Tuzakları
> - ROC'suz Z dönüşümü eksik — ROC'u her zaman yaz!
> - DFT'de $k=0$: DC bileşeni $= \sum x[n]$ (basit toplam)
> - Döngüsel konvolüsyon $\neq$ lineer konvolüsyon — sıfır doldur!
> - $h[0] = \omega_c/\pi$ (LP impuls yanıtı $n=0$ değeri)
> - Bilinear: prewarping atlanırsa hedef frekans kaçar
> - Kararlılık: kutup $|z|<1$ mü? Değil $|z|<\infty$

---

← [[SSI Ana Sayfa]] | [[SSI Formül Sayfası]]
