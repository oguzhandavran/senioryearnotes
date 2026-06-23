---
tags: [mst, kök-yer-eğrisi, kompansatör, pd, pi, lead-lag, kontrol-tasarımı, örnek-sorular]
---

# 05 — Kök Yer Eğrisi Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Kök Yer Eğrisi ve Kompansasyon|05 Kök Yer Eğrisi ve Kompansasyon]]

---

## Çözümlü Örnek 1: PD Tasarımı

**Bitki:** $G_p(s) = \dfrac{1}{s(s+4)(s+6)}$

**Hedef:** $\%OS = 16\%$, $T_s \leq 2$ s

**Adım 1:** $\%OS = 16\% \implies \zeta \approx 0.5$

**Adım 2:** $T_s = 4/(\zeta\omega_n) \leq 2 \implies \omega_n \geq 4$

$\sigma = \zeta\omega_n = 0.5 \times 4 = 2$, $\omega_d = \omega_n\sqrt{1-\zeta^2} = 4\cdot\sqrt{3}/2 \approx 3.46$

**Baskın kutup:** $s_d = -2 + j3.46$

**Adım 3:** Kompansatörsüz açı hesabı

$\angle G_p(s_d) = \angle\frac{1}{s_d(s_d+4)(s_d+6)}$

- $\angle s_d = \angle(-2+j3.46) = 180° - \arctan(3.46/2) = 180° - 60° = 120°$
- $\angle(s_d+4) = \angle(2+j3.46) = \arctan(3.46/2) = 60°$
- $\angle(s_d+6) = \angle(4+j3.46) = \arctan(3.46/4) = 40.9°$

$\angle G_p = -(120° + 60° + 40.9°) = -220.9°$

Gereken ek açı: $-220.9° + \theta_c = -180° \implies \theta_c = 40.9°$

**Adım 4:** $z_c$ bul

Sıfır katkısı: $\angle(s_d + z_c) = 40.9°$

$\arctan\left(\dfrac{3.46}{-2+z_c}\right) = 40.9° \implies -2+z_c = 3.46/\tan(40.9°) \approx 4 \implies z_c = 6$

$$G_c(s) = K_c(s + 6)$$

**Not:** Bu durumda $z_c = 6$ bitki kutpunu iptal eder → **kutup-sıfır iptali**

**Adım 5:** Genlik şartından $K_c$:

$$|K_c G_p(s_d)| = 1 \implies K_c = \frac{|s_d||s_d+4||s_d+6|}{|s_d+6|} \approx \frac{|s_d||s_d+4|}{1}$$
