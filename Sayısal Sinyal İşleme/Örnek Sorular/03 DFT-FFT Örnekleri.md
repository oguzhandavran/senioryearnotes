---
tags: [ssi, dsp, dft, fft, spektral-analiz, örnek-sorular]
---

# 03 — DFT ve FFT (Örnekler)

← [[SSI Ana Sayfa]] | Teori: [[../Konu Anlatımları/03 DFT ve FFT]]

---

## Örnek 1 — 4-Noktalı DFT Hesabı

**Verilen:** $x[n] = \{1, 1, 1, 1\}$ ($N = 4$)

**Çözüm:**

$W_4 = e^{-j2\pi/4} = e^{-j\pi/2} = -j$

$$X[k] = \sum_{n=0}^{3} x[n] W_4^{kn}$$

$X[0] = 1+1+1+1 = 4$

$X[1] = 1 + W_4^1 + W_4^2 + W_4^3 = 1 + (-j) + (-1) + j = 0$

$X[2] = 1 + W_4^2 + W_4^4 + W_4^6 = 1 + (-1) + 1 + (-1) = 0$

$X[3] = 1 + W_4^3 + W_4^6 + W_4^9 = 1 + j + (-1) + (-j) = 0$

$$\boxed{X[k] = \{4, 0, 0, 0\}}$$

---

## Örnek 2 — DFT ile Lineer Konvolüsyon

**Verilen:** $x[n] = \{1, 2, 3\}$, $h[n] = \{1, 1\}$

**İste:** DFT yöntemiyle lineer konvolüsyonu hesapla.

**Çözüm:**

Uzunluklar: $L_x = 3$, $L_h = 2$ → sonuç uzunluğu = $3+2-1 = 4$

$N = 4$ noktalı DFT için sıfır doldur:
- $x[n] = \{1, 2, 3, 0\}$
- $h[n] = \{1, 1, 0, 0\}$

4-noktalı DFT'leri al ($W_4 = -j$):

$X[k]: X[0]=6,\ X[1]=1-j\cdot2-3+0=\ldots$ (sayısal hesap)

$H[k]: H[0]=2,\ H[1]=1-j,\ H[2]=0,\ H[3]=1+j$

$Y[k] = X[k] \cdot H[k]$ → ters DFT:

$$y[n] = \{1, 3, 5, 3\}$$

*Doğrulama (doğrudan konvolüsyon):* $y = x * h = \{1\cdot1, 1\cdot1+2\cdot1, 2\cdot1+3\cdot1, 3\cdot1\} = \{1, 3, 5, 3\}$ ✓

---

## Örnek 3 — FFT Butterfly (N=4, DIT)

**Verilen:** $x[n] = \{x[0], x[1], x[2], x[3]\}$

**Çözüm yapısı:**

Çift indisler: $x_e = \{x[0], x[2]\}$ → 2-noktalı FFT
Tek indisler: $x_o = \{x[1], x[3]\}$ → 2-noktalı FFT

Butterfly kombinasyonu:
$$X[k] = X_e[k] + W_4^k X_o[k], \quad k = 0, 1$$
$$X[k+2] = X_e[k] - W_4^k X_o[k], \quad k = 0, 1$$

2-noktalı FFT için: $W_2^0 = 1$

$$X_e[0] = x[0] + x[2], \quad X_e[1] = x[0] - x[2]$$
$$X_o[0] = x[1] + x[3], \quad X_o[1] = x[1] - x[3]$$

---

## Bağlantılı Notlar

- [[../Konu Anlatımları/03 DFT ve FFT]]
- [[02 Z-Dönüşümü Örnekleri]]
- [[04 Filtre Tasarımı Örnekleri]]
