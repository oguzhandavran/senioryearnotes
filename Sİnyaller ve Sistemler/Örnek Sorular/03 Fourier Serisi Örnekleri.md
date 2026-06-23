---
tags: [ss, fourier-serisi, örnek-sorular]
---

# 03 — Fourier Serisi Örnekleri

← [[SS Ana Sayfa]]  |  Teori: [[../Konu Anlatımları/03 Fourier Serisi]]

---

## Örnek 1 — Kare Dalga CTFS Katsayıları

**Verilen:** $T$-periyodik kare dalga: $[-T_1, T_1]$ aralığında 1, geri kalan sürede 0.

**Çözüm:**
$$a_k = \frac{1}{T}\int_{-T_1}^{T_1} e^{-jk\omega_0 t}\,dt = \frac{2\sin(k\omega_0 T_1)}{k\omega_0 T} = \frac{2T_1}{T}\,\operatorname{sinc}\!\left(\frac{kT_1}{T/2}\right)$$

$$a_0 = \frac{2T_1}{T} \quad \text{(DC bileşen = doluluk oranı)}$$

---

## Örnek 2 — Bileşik Sinüzoidalin Fourier Serisi
*(Cevap Anahtarından)*

**Soru:** $x(t) = \cos 4t + \sin 6t$ için temel periyot ve $a_k$ katsayılarını bul.

**Çözüm:**
- $\cos 4t$: $T_1 = \pi/2$  
- $\sin 6t$: $T_2 = \pi/3$  
- Temel periyot: $T = \text{LCM}(\pi/2,\, \pi/3) = \pi$  
- $\omega_0 = 2\pi/T = 2$

Euler açılımı:
$$\cos 4t = \frac{e^{j4t}+e^{-j4t}}{2} = \frac{e^{j2\cdot 2t}+e^{-j2\cdot 2t}}{2}$$
$$\sin 6t = \frac{e^{j6t}-e^{-j6t}}{2j} = \frac{e^{j3\cdot 2t}-e^{-j3\cdot 2t}}{2j}$$

| $k$ | $a_k$ |
|-----|-------|
| $\pm 2$ | $1/2$ |
| $+3$ | $1/(2j) = -j/2$ |
| $-3$ | $j/2$ |
| diğer | $0$ |

---

## Örnek 3 — DTFS Katsayıları

**Soru:** $x[n] = \sin\!\left(\dfrac{2\pi}{3}n\right)$, $N = 3$, $\omega_0 = 2\pi/3$ için $a_k$ bul.

**Çözüm:**
$$x[n] = \frac{e^{j\frac{2\pi}{3}n} - e^{-j\frac{2\pi}{3}n}}{2j} = \frac{1}{2j}e^{j\omega_0 n} - \frac{1}{2j}e^{-j\omega_0 n}$$

$$a_1 = \frac{1}{2j} = -\frac{j}{2}, \qquad a_{-1} = a_2 = \frac{j}{2}$$

> Dikkat: $a_{-1} = a_{N-1} = a_2$ — DTFS katsayıları $N$-periyodik.

---

## Örnek 4 — Parseval ile Güç Hesabı

**Soru:** $x(t) = \cos(2t) + 2\sin(3t)$ sinyalinin ortalama gücünü bul.

**Çözüm:** $a_k$ katsayılarını bul:

| $k$ | $a_k$ | $|a_k|^2$ |
|-----|-------|-----------|
| $\pm 1$ | $1/2$ | $1/4$ |
| $\pm \frac{3}{2}$ | $\mp j$ | $1$ |

$$P = \sum_k |a_k|^2 = \frac{1}{4} + \frac{1}{4} + 1 + 1 = \frac{5}{2}$$

*Ya da doğrudan:* $P_{\cos} = A^2/2 = 1/2$, $P_{\sin} = (2)^2/2 = 2$, toplam $= 5/2$.
