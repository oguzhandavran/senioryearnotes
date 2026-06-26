---
tags: [mst, kök-yer-eğrisi, kompansatör, pd, pi, lead-lag, kontrol-tasarımı, örnek-sorular]
---

# 05 — Kök Yer Eğrisi Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Kök Yer Eğrisi ve Kompansasyon|05 Kök Yer Eğrisi ve Kompansasyon]]

---

## Çözümlü Örnek 1: PD Tasarımı

> [!example] Problem
> **Bitki:** $G_p(s) = \dfrac{1}{s(s+4)(s+6)}$.
>
> **İstenen:** $\%OS = 16\%$ ve $T_s \leq 2$ s sağlayan PD kompansatörü $G_c(s)=K_c(s+z_c)$ tasarla (açı kriteriyle $z_c$, genlik kriteriyle $K_c$).

> [!note]- Semboller
> - $G_p$: bitki (plant) transfer fonksiyonu; $G_c=K_c(s+z_c)$: PD kompansatör
> - $\%OS$: yüzde aşım; $\zeta$: sönüm oranı (≈0.5 ↔ %16 OS); $\omega_n$: doğal frekans
> - $T_s=4/(\zeta\omega_n)$: %2 yerleşme süresi; $\sigma=\zeta\omega_n$: kutbun reel kısmı; $\omega_d=\omega_n\sqrt{1-\zeta^2}$: sönümlü frekans
> - $s_d$: hedeflenen baskın (dominant) kapalı çevrim kutbu
> - Açı kriteri: $\angle G(s_d)=-180°$; $\theta_c$: kompansatör sıfırının eklemesi gereken açı
> - $z_c$: kompansatör sıfırı; $K_c$: kompansatör kazancı (genlik kriterinden $|K_cG(s_d)|=1$)

**Bitki:** $G_p(s) = \dfrac{1}{s(s+4)(s+6)}$, **Hedef:** $\%OS = 16\%$, $T_s \leq 2$ s

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

**Adım 5:** Genlik şartından $K_c$. Sıfır $(s+6)$, bitki kutbu $(s+6)$'yı iptal ettiğinden o terimler sadeleşir:

$$|K_c G_c G_p(s_d)| = 1 \implies K_c = \frac{|s_d|\,|s_d+4|\,|s_d+6|}{|s_d+z_c|} = \frac{|s_d|\,|s_d+4|\,|s_d+6|}{|s_d+6|} = |s_d|\,|s_d+4|$$

Uzunlukları koy: $|s_d|=|-2+j3{,}46|=\sqrt{4+12}=4$, $\;|s_d+4|=|2+j3{,}46|=\sqrt{4+12}=4$:

$$\boxed{K_c = 4\times4 = 16,\qquad G_c(s)=16(s+6)}$$

---

## Çözümlü Örnek 2: PD Tasarımı — 3× Yerleşme Süresi İyileştirme (Hocanın Notu)

> [!example] Problem
> **Bitki:** $G(s) = \dfrac{K}{s(s+4)(s+6)}$.
>
> **İstenen:** $\%OS = 16\%$ korunurken yerleşme süresini **3 kat** düşüren PD kompansatörü, kazancı $K$ ve kalıcı hal hatası.

> [!note]- Semboller
> - $\%OS$: yüzde aşım; $\zeta$: sönüm oranı; $\beta=\cos^{-1}\zeta$: kutbun açısı (gerçel eksenden)
> - $\sigma=\zeta\omega_n$: kutbun reel kısmı; $\omega_d$: sönümlü (sanal) kısım; $s_d$: baskın kutup
> - $\sigma_a$: asimptot kesişimi; ayrılma (breakaway): $dK/ds=0$ noktası
> - $t_s=4/\sigma$: yerleşme süresi; alt-indis $y$ = "yeni" (tasarım hedefi)
> - $\theta_1,\theta_2,\theta_3$: bitki kutuplarının $s_d$'ye açıları; $\theta_{z_c}$: PD sıfırının açısı (açı kriteri)
> - $z_c$: PD sıfırı; $\ell_i$: $s_d$'den kutup/sıfırlara vektör uzunlukları; $K$: kök yer eğrisi kazancı
> - $K_v=\lim_{s\to0}sG(s)$: hız hata sabiti (Tip 1); $e_{ss}=1/K_v$: ramp kalıcı hal hatası
> - $R_1,R_2,C$: op-amp gerçeklemesi eleman değerleri

---

### Adım 1-2 — KYE Mevcut Sistem

Sıfır yok ($n=0$), kutuplar $0, -4, -6$ ($m=3$).

- Asimptot sayısı: $3$, açıları: $60°, 180°, 300°$
- Asimptot kesişimi: $\sigma_a = (0-4-6)/3 = -3{,}33$
- Ayrılma noktası: $(s^3+10s^2+24s)' = 0$ → $3s^2+20s+24=0$ → $s_1=-1{,}57$

### Adım 7-8 — Sönüm Oranı ve Açısı

$$\zeta = \frac{-\ln(16/100)}{\sqrt{\pi^2+\ln^2(16/100)}} = \frac{1{,}83}{3{,}65} = \boxed{0{,}504}$$

$$\beta = \cos^{-1}(0{,}504) = \boxed{59{,}74°}$$

### Mevcut Sistemin İstenen Kutbu

$$\sigma = -1{,}2, \quad \omega_d = 2{,}064 \quad \Rightarrow \quad s_d = -1{,}2 + j2{,}064$$

Yerleşme süresi: $t_s = 4/\sigma = 4/1{,}2 = 3{,}32$ s

### PD Tasarım — İstenen Kutup

3 kat azaltma: $t_{s,\text{yeni}} = 3{,}32/3 = 1{,}107$ s

$$\zeta\omega_{ny} = 4/t_{s,\text{yeni}} = 4/1{,}107 \Rightarrow \omega_{ny} = \frac{4}{0{,}504 \times 1{,}107} = 7{,}17 \approx 7{,}18$$

$$\sigma_y = \zeta\omega_{ny} = 0{,}504 \times 7{,}18 = \boxed{3{,}613}$$

$$\omega_y = \tan(59{,}74°) \times 3{,}613 = \boxed{6{,}193}$$

İstenen kutup: $s_{d,\text{yeni}} = -3{,}613 + j6{,}193$

### PD Sıfırı Bulma (Açı Kriteri)

$G_{PD}(s) = s + z_c$ (sıfır ekler). Açı kriteri:

$$\theta_{z_c} - (\theta_1 + \theta_2 + \theta_3) = -180°$$

$$\theta_{z_c} - (120{,}29° + 86{,}42° + 68{,}82°) = -180°$$

$$\theta_{z_c} = -180° + 275{,}63° = 95{,}63° \Rightarrow \theta_{z_c}' = 180° - 95{,}63° = 84{,}37°$$

$$\tan(84{,}37°) = \frac{6{,}193}{3{,}613 - z_c} \Rightarrow z_c = 3{,}613 - \frac{6{,}193}{10{,}14} = \boxed{z_c = 3{,}002}$$

### K Kazancı

$$\ell_1 = \sqrt{(6-3{,}613)^2+6{,}193^2} = 6{,}64$$
$$\ell_2 = \sqrt{(4-3{,}613)^2+6{,}193^2} = 6{,}20$$
$$\ell_3 = \sqrt{(3{,}002-3{,}613)^2+6{,}193^2} = 6{,}22$$
$$\ell_4 = \sqrt{(0-3{,}613)^2+6{,}193^2} = 7{,}17$$

$$K = \frac{\ell_1\cdot\ell_2\cdot\ell_4}{\ell_3} = \frac{6{,}64 \times 6{,}20 \times 7{,}17}{6{,}22} = \boxed{47{,}46}$$

### Yeni Sistem ve Hata

$$\boxed{G(s) = \frac{47{,}46(s+3{,}002)}{s(s+4)(s+6)}}$$

Tip 1 sistem → hız hatası:
$$K_v = \lim_{s\to 0} s\,G(s) = \frac{47{,}46 \times 3{,}002}{4 \times 6} = 5{,}93$$

$$e_{ss} = \frac{1}{K_v} = \frac{1}{5{,}93} = \boxed{0{,}168}$$

### Op-Amp Gerçeklemesi

$$G_{PD}(s) = -R_2C\!\left(s + \frac{1}{R_1C}\right)$$

Seçimler: $\frac{1}{R_1C} = 3{,}002$ ve $R_2C = 1$
