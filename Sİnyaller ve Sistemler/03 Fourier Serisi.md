---
tags: [ss, fourier-serisi, ctfs, dtfs]
---

# 03 — Fourier Serisi

← [[SS Ana Sayfa]]

## Özet

> Periyodik sinyalleri harmonik sinüzoidlerin toplamı olarak yaz. CTFS: sürekli zaman periyodik → karmaşık üstel katsayılar. DTFS: ayrık periyodik → sonlu toplam.

---

## 1. Sürekli Zaman Fourier Serisi (CTFS)

### Sentez ve Analiz Denklemleri

$$\boxed{x(t) = \sum_{k=-\infty}^{\infty} a_k\, e^{jk\omega_0 t}, \quad \omega_0 = \frac{2\pi}{T}}$$

$$\boxed{a_k = \frac{1}{T} \int_T x(t)\, e^{-jk\omega_0 t}\, dt}$$

Burada integral herhangi bir $T$ uzunluğundaki tam periyot üzerinden alınır.

### Trigonometrik Form (Gerçek Sinyaller için)

Eğer $x(t)$ gerçek değerliyse:
$$x(t) = a_0 + 2\sum_{k=1}^{\infty}\left[A_k \cos(k\omega_0 t) - B_k\sin(k\omega_0 t)\right]$$

Burada $a_k = A_k - jB_k$.

---

## 2. Ayrık Zaman Fourier Serisi (DTFS / DFS)

### Sentez ve Analiz Denklemleri

$$\boxed{x[n] = \sum_{k=\langle N\rangle} a_k\, e^{jk\omega_0 n}, \quad \omega_0 = \frac{2\pi}{N}}$$

$$\boxed{a_k = \frac{1}{N} \sum_{n=\langle N\rangle} x[n]\, e^{-jk\omega_0 n}}$$

> [!warning] DT Farkı
> Toplam **sonlu** ($N$ terim) — sonsuz değil! Katsayılar $N$-periyodik: $a_k = a_{k+N}$.

---

## 3. Fourier Serisi Özellikleri

| Özellik | CT | DT |
|---------|----|----|
| Doğrusallik | $ax(t)+by(t) \leftrightarrow aa_k+bb_k$ | aynı |
| Zaman kayması | $x(t-t_0) \leftrightarrow a_k e^{-jk\omega_0 t_0}$ | $x[n-n_0] \leftrightarrow a_k e^{-jk\omega_0 n_0}$ |
| Frekans kayması | $e^{jM\omega_0 t}x(t) \leftrightarrow a_{k-M}$ | aynı |
| Zaman ters çevirme | $x(-t) \leftrightarrow a_{-k}$ | $x[-n] \leftrightarrow a_{-k}$ |
| Konjugat | $x^*(t) \leftrightarrow a^*_{-k}$ | aynı |
| Çarpma (modülasyon) | $x(t)y(t) \leftrightarrow \sum_l a_l b_{k-l}$ | aynı |
| **Parseval** | $\frac{1}{T}\int_T \|x(t)\|^2 dt = \sum_k \|a_k\|^2$ | $\frac{1}{N}\sum_{\langle N\rangle}\|x[n]\|^2 = \sum_{\langle N\rangle}\|a_k\|^2$ |

### Simetri Özellikleri

| Sinyal | Katsayı $a_k$ |
|--------|--------------|
| Gerçek $x(t)$ | $a_{-k} = a_k^*$ (Hermitian simetri) |
| Gerçek + çift | $a_k$ gerçek ve çift |
| Gerçek + tek | $a_k$ saf sanal ve tek |

---

## 4. Örnekler

### Örnek 1 — Kare Dalga

$T$-periyodik kare dalga: $[-T_1, T_1]$ aralığında 1, geri kalan $T$ süresinde 0.

$$a_k = \frac{2\sin(k\omega_0 T_1)}{k\omega_0 T} = \frac{2T_1}{T}\,\text{sinc}\!\left(\frac{kT_1}{T/2}\right)$$

$a_0 = 2T_1/T$ (DC bileşen = doluluk oranı)

### Örnek 2 — Sınav Sorusu (Cevap Anahtarından)

$x(t) = \cos 4t + \sin 6t$

Temel periyotlar: $T_1 = \pi/2$ (cos4t için), $T_2 = \pi/3$ (sin6t için) → $T = \pi$ (LCM)

$\omega_0 = 2\pi/T = 2$, $N = $ periyot örnekler

Euler açılımı:
$$\cos 4t = \frac{e^{j4t}+e^{-j4t}}{2}, \quad \sin 6t = \frac{e^{j6t}-e^{-j6t}}{2j}$$

Katsayılar: $a_2 = a_{-2} = 1/2$; $a_3 = 1/(2j) = -j/2$; $a_{-3} = j/2$

### Örnek 3 — DT Fourier Serisi Katsayıları

$x[n] = \sin(\frac{2\pi}{3}n)$, $N=3$, $\omega_0 = 2\pi/3$

$$x[n] = \frac{e^{j\frac{2\pi}{3}n} - e^{-j\frac{2\pi}{3}n}}{2j} = \frac{1}{2j}e^{j\omega_0 n} - \frac{1}{2j}e^{-j\omega_0 n}$$

$a_1 = \frac{1}{2j}$, $a_{-1} = a_2 = -\frac{1}{2j}$ (dikkat: $a_{-1} = a_{N-1} = a_2$ periyodiklik nedeniyle)

---

## 5. Parseval Teoremi

**Ortalama güç = katsayıların karelerinin toplamı:**

$$P = \frac{1}{T}\int_T |x(t)|^2 dt = \sum_{k=-\infty}^{\infty} |a_k|^2$$

> [!sinav] Sınav İpucu
> Fourier serisini bilmeden sadece $|a_k|^2$ toplamı ile güç hesaplanabilir!

---

## Bağlantılı Notlar

- [[02 LTI Sistemler ve Konvolüsyon]]
- [[04 Fourier Dönüşümü]]
- [[../Sayısal Sinyal İşleme/03 DFT ve FFT|SSİ: DFT ve FFT]]
