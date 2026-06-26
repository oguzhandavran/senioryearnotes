---
tags: [ssi, dsp, örnekleme, nyquist, aliasing, örnek-sorular]
---

# 01 — Ayrık Zaman Sinyalleri ve Örnekleme (Örnekler)

← [[SSI Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Ayrık Zaman Sinyalleri ve Örnekleme]]

---

## Örnek 1 — Enerji Hesabı

> [!note]- Semboller
> - $x[n]=(1/2)^nu[n]$: nedensel sönen üstel dizi; $u[n]$: birim basamak
> - $E_\infty=\sum_n|x[n]|^2$: toplam enerji
> - Geometrik seri: $\sum_{n=0}^\infty r^n=\frac{1}{1-r}$ (yakınsama için $|r|<1$; burada $r=1/4$)

**Verilen:** $x[n] = (1/2)^n u[n]$

**İste:** Toplam enerjiyi hesapla.

**Çözüm:**

$$E_\infty = \sum_{n=0}^{\infty}\left(\frac{1}{2}\right)^{2n} = \sum_{n=0}^{\infty}\left(\frac{1}{4}\right)^n = \frac{1}{1-\frac{1}{4}} = \frac{4}{3}$$

---

## Örnek 2 — Z-Dönüşümü ile Üstel Sinyal

> [!note]- Semboller
> - $x[n]=a^nu[n]$: nedensel üstel; $a$: taban
> - $X(z)=\sum_n x[n]z^{-n}$: Z-dönüşümü; $z$: karmaşık değişken
> - ROC (yakınsama bölgesi): $|z|>|a|$; birim çemberi ($|z|=1$) içeriyorsa DTFT vardır
> - $|a|<1$ → DTFT mevcut; $|a|\ge1$ → mevcut değil

**Verilen:** $x[n] = a^n u[n]$

**İste:** Z-dönüşümünü geometrik seri ile bul.

**Çözüm:**

$$X(z) = \sum_{n=0}^{\infty}(az^{-1})^n = \frac{1}{1-az^{-1}} = \frac{z}{z-a}, \quad |z| > |a|$$

- $|a| < 1$ → ROC birim çemberi içerir → DTFT mevcut
- $|a| \geq 1$ → Fourier dönüşümü mevcut değil

---

## Örnek 3 — Sistem Özellikleri Analizi: $y[n] = nx[n]$

> [!note]- Semboller
> - $T\{\cdot\}$: sistem operatörü; $y[n]=nx[n]$ (zamanla değişen kazanç $n$)
> - Doğrusallık: $T\{ax_1+bx_2\}=aT\{x_1\}+bT\{x_2\}$ (süperpozisyon)
> - Zamanla değişmezlik (ZD): girişi $n_0$ geciktir → çıkış da aynı $n_0$ gecikmeli olmalı
> - $n$ çarpanı konuma bağlı olduğundan kayma simetrisi bozulur → ZD değil

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
