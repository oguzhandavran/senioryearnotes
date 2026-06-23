---
tags: [ssi, dsp, örnekleme, nyquist, aliasing, örnek-sorular]
---

# 01 — Ayrık Zaman Sinyalleri ve Örnekleme (Örnekler)

← [[SSI Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Ayrık Zaman Sinyalleri ve Örnekleme]]

---

## Örnek 1 — Enerji Hesabı

**Verilen:** $x[n] = (1/2)^n u[n]$

**İste:** Toplam enerjiyi hesapla.

**Çözüm:**

$$E_\infty = \sum_{n=0}^{\infty}\left(\frac{1}{2}\right)^{2n} = \sum_{n=0}^{\infty}\left(\frac{1}{4}\right)^n = \frac{1}{1-\frac{1}{4}} = \frac{4}{3}$$

---

## Örnek 2 — Z-Dönüşümü ile Üstel Sinyal

**Verilen:** $x[n] = a^n u[n]$

**İste:** Z-dönüşümünü geometrik seri ile bul.

**Çözüm:**

$$X(z) = \sum_{n=0}^{\infty}(az^{-1})^n = \frac{1}{1-az^{-1}} = \frac{z}{z-a}, \quad |z| > |a|$$

- $|a| < 1$ → ROC birim çemberi içerir → DTFT mevcut
- $|a| \geq 1$ → Fourier dönüşümü mevcut değil

---

## Örnek 3 — Sistem Özellikleri Analizi: $y[n] = nx[n]$

**İste:** Doğrusal mı? Zamanla değişmez mi?

**Çözüm:**

**Doğrusallik testi:**
$$T\{ax_1[n] + bx_2[n]\} = n(ax_1[n]+bx_2[n]) = anx_1[n] + bnx_2[n] = aT\{x_1\} + bT\{x_2\}$$ ✅ Doğrusal

**Zamanla değişmezlik testi:**
$$T\{x[n-n_0]\} = nx[n-n_0]$$
$$T\{x[n]\}\big|_{n \to n-n_0} = (n-n_0)x[n-n_0]$$
$$nx[n-n_0] \neq (n-n_0)x[n-n_0]$$ ❌ Zamanla Değişir

---

## Bağlantılı Notlar

- [[../Konu Anlatımları/01 Ayrık Zaman Sinyalleri ve Örnekleme]]
- [[02 Z-Dönüşümü Örnekleri]]
