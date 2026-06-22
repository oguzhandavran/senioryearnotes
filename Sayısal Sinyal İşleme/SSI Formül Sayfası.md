---
tags: [ssi, dsp, formül, cheatsheet]
---

# SSİ — Formül Sayfası

← [[SSI Ana Sayfa]]

> Sınavda yanında tut.

---

## Sistem Özellikleri

| Özellik | Test |
|---------|------|
| Hafızasız | $y[n]$ sadece $x[n]$'e bağlı |
| Nedensel | $x[n+k]$ yok ($k>0$) |
| Doğrusal | Süperpozisyon sağlansın |
| Zamanla Değişmez | Katsayıda bağımsız $n$ yok |
| Kararlı (BIBO) | $\sum_{n}|h[n]| < \infty$ |

---

## DT Konvolüsyon

$$y[n] = \sum_{k=-\infty}^{\infty}x[k]h[n-k]$$

**Boyut:** $L_y = L_x + L_h - 1$; $n \in [N_1+M_1, N_2+M_2]$

**Özel:** $x[n]*\delta[n] = x[n]$; $x[n]*\delta[n-k] = x[n-k]$

---

## Fourier Serisi (DFS)

$$x[n] = \sum_{k=0}^{N-1}a_k e^{jk\omega_0 n}, \quad a_k = \frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-jk\omega_0 n}, \quad \omega_0=\frac{2\pi}{N}$$

---

## DTFT Çiftleri

| $x[n]$ | $X(e^{j\omega})$ | ROC |
|--------|-----------------|-----|
| $\delta[n]$ | $1$ | Tümü |
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ | |
| $a^n u[n]$, $|a|<1$ | $\frac{1}{1-ae^{-j\omega}}$ | |
| $na^n u[n]$, $|a|<1$ | $\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ | |
| Dikdörtgen $[0,N-1]$ | $e^{-j\omega\frac{N-1}{2}}\frac{\sin(N\omega/2)}{\sin(\omega/2)}$ | |

**Transfer:** $H(e^{j\omega}) = Y(e^{j\omega})/X(e^{j\omega})$

---

## Z-Dönüşümü Çiftleri

| $x[n]$ | $X(z)$ | ROC |
|--------|--------|-----|
| $\delta[n]$ | $1$ | Tümü |
| $u[n]$ | $\frac{1}{1-z^{-1}}$ | $|z|>1$ |
| $a^n u[n]$ | $\frac{1}{1-az^{-1}}$ | $|z|>|a|$ |
| $na^n u[n]$ | $\frac{az^{-1}}{(1-az^{-1})^2}$ | $|z|>|a|$ |
| $-a^n u[-n-1]$ | $\frac{1}{1-az^{-1}}$ | $|z|<|a|$ |

**Gecikme:** $\mathcal{Z}\{x[n-k]\} = z^{-k}X(z)$

**Başlangıç:** $x[0] = \lim_{z\to\infty}X(z)$

**Son değer:** $x[\infty] = \lim_{z\to 1}(z-1)X(z)$

**Kararlılık:** Tüm kutuplar $|z|<1$

---

## DFT

$$X[k] = \sum_{n=0}^{N-1}x[n]W_N^{kn}, \quad x[n] = \frac{1}{N}\sum_{k=0}^{N-1}X[k]W_N^{-kn}, \quad W_N = e^{-j2\pi/N}$$

**Döngüsel konvolüsyon:** $x[n]\circledast h[n] \leftrightarrow X[k]\cdot H[k]$

**Lineer via DFT:** zero-pad her ikisini $N \geq L_x + L_h - 1$'e

---

## Dikdörtgen Pencere

$$H(e^{j\omega}) = e^{-j\omega\frac{N-1}{2}} \cdot \frac{\sin(N\omega/2)}{\sin(\omega/2)}$$

Merkez lob yüksekliği: $N$; İlk sıfır: $\omega = 2\pi/N$

---

## Bilineer Dönüşüm

$$s = \frac{2}{T}\cdot\frac{1-z^{-1}}{1+z^{-1}}, \qquad \Omega_{analog} = \frac{2}{T}\tan\!\left(\frac{\omega}{2}\right)$$

---

## Euler Açılımları

$$\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}, \qquad \sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$$

$$|e^{j\theta}| = 1, \qquad \angle e^{j\theta} = \theta$$
