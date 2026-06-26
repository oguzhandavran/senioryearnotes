---
tags: [emd, bütünleme, dalga-yayılması, örnek-sorular]
---

# 03 — Dalga Yayılması Örnekleri

← [[EMD Ana Sayfa]] | Teori: [[../Konu Anlatımları/03 Dalga Yayılması ve Düzlemsel Dalgalar]]

---

## Soru 2 — Düzlemsel Dalga Anlık Görüntü

> [!note]- Semboller
> - $\omega$: açısal frekans (rad/s); $f=\omega/2\pi$: frekans (Hz)
> - $\beta=2\pi/\lambda=\omega/c$: faz sabiti (dalga sayısı, rad/m); $\lambda$: dalga boyu (m)
> - $c=3\times10^8$ m/s: ışık hızı (serbest uzay); $\hat a_y$: alan yönü
> - $t_1=\frac{\lambda/4}{c}=\frac{T}{4}$: çeyrek dalga boyu ilerleme süresi

**Problem:** Serbest uzayda $\bar{E}=\hat{a}_y 20\sin(4\pi\times10^8 t - \beta z)$ V/m. $t=0$'da $z$ boyunca $\lambda/4$ ilerlemesi için gereken $t_1$'i bul; $\beta$ ve $\lambda$ değerlerini hesapla.

**Çözüm:**

$$\omega = 4\pi\times10^8 \;\text{rad/s} \implies f = \frac{\omega}{2\pi} = 2\times10^8 \;\text{Hz} = 200 \;\text{MHz}$$

$$\lambda = \frac{c}{f} = \frac{3\times10^8}{2\times10^8} = 1.5 \;\text{m}$$

$$\beta = \frac{2\pi}{\lambda} = \frac{4\pi}{3} \approx 4.19 \;\text{rad/m}$$

$$\lambda/4 = 0.375 \;\text{m}, \quad t_1 = \frac{\lambda/4}{c} = \frac{0.375}{3\times10^8} = 1.25\times10^{-9} \;\text{s} = \boxed{1.25 \;\text{ns}}$$

---

## Soru 5 — Düzlemsel Dalga H Bileşeni (Serbest Uzay)

> [!note]- Semboller
> - $\bar E$: elektrik alan ($\hat a_y$ yönlü); $\bar H$: manyetik alan; yayılma $+\hat a_z$
> - $\eta_0=120\pi\approx377\,\Omega$: serbest uzay dalga empedansı; $H_0=E_0/\eta_0$
> - Yön kuralı: yayılma $\hat k=\hat E\times\hat H$ → $\hat a_z=\hat a_y\times\hat H$ → $\hat H=-\hat a_x$
> - $\beta=\omega/c$: faz sabiti

**Problem:** $f=50$ MHz'lik dalga: $\bar{E}(z,t)=\hat{a}_y\,12\pi\sin(\omega t-\beta z)$ V/m. H bileşenini bul ve $t=0$'daki anlık görüntüyü çiz.

**Çözüm:**

- Yayılma yönü: $+\hat{a}_z$; Elektrik alan yönü: $\hat{a}_y$
- $\hat{a}_z\times\hat{a}_y = -\hat{a}_x$ → H manyetik alan yönü: $-\hat{a}_x$

$$\omega = 2\pi\times50\times10^6 = 10^8\pi \;\text{rad/s}, \quad \beta = \frac{\omega}{c} = \frac{\pi}{3} \;\text{rad/m}$$

$$\eta_0 = 120\pi \;\Omega \implies H_0 = \frac{E_0}{\eta_0} = \frac{12\pi}{120\pi} = 0.1 \;\text{A/m}$$

$$\boxed{\bar{H}(z,t) = -\hat{a}_x\,0.1\sin\!\left(10^8\pi t - \frac{\pi}{3}z\right) \;\text{A/m}}$$

---

## Soru 6 — Kayıp Tanjantı (Bakır ve Deniz Suyu)

> [!note]- Semboller
> - $\tan\delta=\dfrac{\sigma}{\omega\varepsilon}=\dfrac{\sigma}{2\pi f\varepsilon_0\varepsilon_r}$: kayıp tanjantı (iletim/deplasman akımı oranı)
> - $\sigma$: iletkenlik (S/m); $\varepsilon_r$: bağıl geçirgenlik; $\varepsilon_0=8.854\times10^{-12}$ F/m
> - Kısayol: $\dfrac{1}{2\pi\varepsilon_0}\approx1.8\times10^{10}$ → $\tan\delta=\dfrac{1.8\times10^{10}\,\sigma}{\varepsilon_r\,f}$
> - $\tan\delta\gg1$: iyi iletken · $\tan\delta\approx1$: kayıplı dielektrik · $\tan\delta\ll1$: iyi dielektrik

**Problem:** $\varepsilon_r=1$, $\sigma=5.8\times10^7$ S/m bakır ile $\varepsilon_r=81$, $\sigma=4$ S/m deniz suyu için kayıp tanjantını hesapla.

$$\tan\delta = \frac{\sigma}{2\pi f\varepsilon_0\varepsilon_r} = \frac{1.8\times10^{10}\,\sigma}{\varepsilon_r\,f}$$

**Bakır** ($\varepsilon_r=1$, $\sigma=5.8\times10^7$): $\;\tan\delta = \dfrac{1.8\times10^{10}\times5.8\times10^7}{f} = \dfrac{1.04\times10^{18}}{f}$

| Frekans | $\tan\delta$ | Sınıf |
|---------|-------------|-------|
| 100 MHz ($10^8$) | $1.04\times10^{10} \gg 1$ | **İyi iletken** |
| 10 GHz ($10^{10}$) | $1.04\times10^{8} \gg 1$ | **İyi iletken** |

**Deniz suyu** ($\varepsilon_r=81$, $\sigma=4$): $\;\tan\delta = \dfrac{1.8\times10^{10}\times4}{81\,f} = \dfrac{8.89\times10^{8}}{f}$

| Frekans | $\tan\delta$ | Sınıf |
|---------|-------------|-------|
| 100 Hz ($10^2$) | $\approx8.89\times10^6 \gg 1$ | **İyi iletken** |
| 1 GHz ($10^9$) | $\approx0.889 \approx 1$ | **Kayıplı dielektrik** |
| 10 GHz ($10^{10}$) | $\approx0.0889 \ll 1$ | **Dielektrik** |

> *(Düzeltme: önceki sürümde $\frac{1}{2\pi\varepsilon_0}$ çarpanı eksik girilmişti; sınıflandırmalar doğruydu ama sayılar ~$10^3$ kata kadar küçüktü. Yukarıdaki değerler doğru büyüklüktedir.)*

> [!sinav] Sınıflandırma Kriteri
> - $\tan\delta \gg 1$: İyi iletken ($\sigma \gg \omega\varepsilon$)
> - $\tan\delta \ll 1$: İyi dielektrik ($\sigma \ll \omega\varepsilon$)
> - $\tan\delta \approx 1$: Kayıplı dielektrik
