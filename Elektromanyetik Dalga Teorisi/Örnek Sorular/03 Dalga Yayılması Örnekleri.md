---
tags: [emd, bütünleme, dalga-yayılması, örnek-sorular]
---

# 03 — Dalga Yayılması Örnekleri

← [[EMD Ana Sayfa]] | Teori: [[../Konu Anlatımları/03 Dalga Yayılması ve Düzlemsel Dalgalar]]

---

## Soru 2 — Düzlemsel Dalga Anlık Görüntü

**Problem:** Serbest uzayda $\bar{E}=\hat{a}_y 20\sin(4\pi\times10^8 t - \beta z)$ V/m. $t=0$'da $z$ boyunca $\lambda/4$ ilerlemesi için gereken $t_1$'i bul; $\beta$ ve $\lambda$ değerlerini hesapla.

**Çözüm:**

$$\omega = 4\pi\times10^8 \;\text{rad/s} \implies f = \frac{\omega}{2\pi} = 2\times10^8 \;\text{Hz} = 200 \;\text{MHz}$$

$$\lambda = \frac{c}{f} = \frac{3\times10^8}{2\times10^8} = 1.5 \;\text{m}$$

$$\beta = \frac{2\pi}{\lambda} = \frac{4\pi}{3} \approx 4.19 \;\text{rad/m}$$

$$\lambda/4 = 0.375 \;\text{m}, \quad t_1 = \frac{\lambda/4}{c} = \frac{0.375}{3\times10^8} = 1.25\times10^{-9} \;\text{s} = \boxed{1.25 \;\text{ns}}$$

---

## Soru 5 — Düzlemsel Dalga H Bileşeni (Serbest Uzay)

**Problem:** $f=50$ MHz'lik dalga: $\bar{E}(z,t)=\hat{a}_y\,12\pi\sin(\omega t-\beta z)$ V/m. H bileşenini bul ve $t=0$'daki anlık görüntüyü çiz.

**Çözüm:**

- Yayılma yönü: $+\hat{a}_z$; Elektrik alan yönü: $\hat{a}_y$
- $\hat{a}_z\times\hat{a}_y = -\hat{a}_x$ → H manyetik alan yönü: $-\hat{a}_x$

$$\omega = 2\pi\times50\times10^6 = 10^8\pi \;\text{rad/s}, \quad \beta = \frac{\omega}{c} = \frac{\pi}{3} \;\text{rad/m}$$

$$\eta_0 = 120\pi \;\Omega \implies H_0 = \frac{E_0}{\eta_0} = \frac{12\pi}{120\pi} = 0.1 \;\text{A/m}$$

$$\boxed{\bar{H}(z,t) = -\hat{a}_x\,0.1\sin\!\left(10^8\pi t - \frac{\pi}{3}z\right) \;\text{A/m}}$$

---

## Soru 6 — Kayıp Tanjantı (Bakır ve Deniz Suyu)

**Problem:** $\varepsilon_r=1$, $\sigma=5.8\times10^7$ S/m bakır ile $\varepsilon_r=81$, $\sigma=4$ S/m deniz suyu için 100 MHz ve 10 GHz'de kayıp tanjantını hesapla.

$$\tan\delta = \frac{\varepsilon''}{\varepsilon'} = \frac{\sigma}{\omega\varepsilon} = \frac{\sigma}{2\pi f\varepsilon_0\varepsilon_r}$$

**Bakır** ($\varepsilon_r=1$, $\sigma=5.8\times10^7$):
$$\tan\delta_{bakır} \approx \frac{18\times5.8\times10^7\times10^7}{f} = \frac{1.044\times10^{15}}{f}$$

| Frekans | $\tan\delta$ | Sınıf |
|---------|-------------|-------|
| 100 MHz | $1.044\times10^7 \gg 1$ | **İyi iletken** |
| 10 GHz | $1.044\times10^5 \gg 1$ | **İyi iletken** |

**Deniz suyu** ($\varepsilon_r=81$, $\sigma=4$):
$$\tan\delta_{deniz} \approx \frac{0.888\times10^8}{f}$$

| Frekans | $\tan\delta$ | Sınıf |
|---------|-------------|-------|
| 100 Hz | $\approx8.88\times10^5 \gg 1$ | **İyi iletken** |
| 1 GHz | $\approx0.888 < 1$ | **Kayıplı dielektrik** |
| 10 GHz | $\approx0.088 \ll 1$ | **Dielektrik** |

> [!sinav] Sınıflandırma Kriteri
> - $\tan\delta \gg 1$: İyi iletken ($\sigma \gg \omega\varepsilon$)
> - $\tan\delta \ll 1$: İyi dielektrik ($\sigma \ll \omega\varepsilon$)
> - $\tan\delta \approx 1$: Kayıplı dielektrik
