---
tags: [ss, fourier-serisi, örnek-sorular]
---

# 03 — Fourier Serisi Örnekleri

← [[SS Ana Sayfa]]  |  Teori: [[../Konu Anlatımları/03 Fourier Serisi]]

---

## Örnek 1 — Kare Dalga CTFS Katsayıları

> [!note]- Semboller
> - $T$: periyot; $T_1$: darbenin yarı genişliği; $2T_1/T$: doluluk oranı (duty cycle)
> - $\omega_0=2\pi/T$: temel açısal frekans; $k$: harmonik indeksi
> - $a_k$: CTFS katsayısı ($a_k=\frac1T\int_T x(t)e^{-jk\omega_0t}dt$)
> - $\text{sinc}$: dikdörtgen darbenin spektral şekli; $a_0$: DC bileşen

**Verilen:** $T$-periyodik kare dalga: $[-T_1, T_1]$ aralığında 1, geri kalan sürede 0.

**Çözüm:**
$$a_k = \frac{1}{T}\int_{-T_1}^{T_1} e^{-jk\omega_0 t}\,dt = \frac{2\sin(k\omega_0 T_1)}{k\omega_0 T} = \frac{2T_1}{T}\,\operatorname{sinc}\!\left(\frac{kT_1}{T/2}\right)$$

$$a_0 = \frac{2T_1}{T} \quad \text{(DC bileşen = doluluk oranı)}$$

---

## Örnek 2 — Bileşik Sinüzoidalin Fourier Serisi
*(Cevap Anahtarından)*

> [!note]- Semboller
> - $T_1,T_2$: bileşenlerin tek tek periyotları; $T=\text{LCM}(T_1,T_2)$: ortak temel periyot
> - $\omega_0=2\pi/T$: temel frekans; bir bileşenin frekansı $\omega_0$'ın kaç katıysa o $k$
> - $a_k$: Fourier serisi katsayısı; Euler ile $\cos,\sin$ üstellere açılır
> - $\cos 4t$ → $k=\pm2$ (çünkü $4=2\omega_0$), $\sin 6t$ → $k=\pm3$ (çünkü $6=3\omega_0$)

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

> [!note]- Semboller
> - $x[n]$: ayrık periyodik sinyal; $N$: periyot (örnek sayısı); $\omega_0=2\pi/N$: temel frekans
> - $a_k$: DTFS katsayıları — **$N$-periyodiktir** ($a_{k}=a_{k+N}$, bu yüzden $a_{-1}=a_{N-1}=a_2$)
> - Euler: $\sin\theta=\tfrac{1}{2j}(e^{j\theta}-e^{-j\theta})$

**Soru:** $x[n] = \sin\!\left(\dfrac{2\pi}{3}n\right)$, $N = 3$, $\omega_0 = 2\pi/3$ için $a_k$ bul.

**Çözüm:**
$$x[n] = \frac{e^{j\frac{2\pi}{3}n} - e^{-j\frac{2\pi}{3}n}}{2j} = \frac{1}{2j}e^{j\omega_0 n} - \frac{1}{2j}e^{-j\omega_0 n}$$

$$a_1 = \frac{1}{2j} = -\frac{j}{2}, \qquad a_{-1} = a_2 = \frac{j}{2}$$

> Dikkat: $a_{-1} = a_{N-1} = a_2$ — DTFS katsayıları $N$-periyodik.

---

## Örnek 4 — Parseval ile Güç Hesabı

> [!note]- Semboller
> - $a_k$: Fourier katsayıları; $|a_k|^2$: $k$. harmoniğin güç katkısı
> - Parseval (CTFS): ortalama güç $P=\sum_k|a_k|^2$
> - Temel frekans $\omega_0=1$ (periyot $2\pi$): $\cos2t\to k=\pm2$, $2\sin3t\to k=\pm3$
> - Doğrudan: bir sinüzoidin gücü $A^2/2$

**Soru:** $x(t) = \cos(2t) + 2\sin(3t)$ sinyalinin ortalama gücünü bul.

**Çözüm:** $\omega_0=1$ alındığında ($\cos2t$ → $k=\pm2$, $2\sin3t$ → $k=\pm3$) katsayılar:

| $k$ | $a_k$ | $|a_k|^2$ |
|-----|-------|-----------|
| $\pm 2$ | $1/2$ | $1/4$ |
| $\pm 3$ | $\mp j$ | $1$ |

$$P = \sum_k |a_k|^2 = \underbrace{\tfrac14+\tfrac14}_{k=\pm2} + \underbrace{1+1}_{k=\pm3} = \frac{5}{2}$$

*Ya da doğrudan:* $P_{\cos} = A^2/2 = 1/2$, $P_{\sin} = (2)^2/2 = 2$, toplam $= 5/2$.
