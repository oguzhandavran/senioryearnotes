---
tags: [otomatik-kontrol, kök-yer-eğrisi, kye, root-locus, örnek-sorular]
---

# 04 — Kök Yer Eğrisi Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/04 Kök Yer Eğrisi]]

---

## Örnek 1: $G(s) = \dfrac{K}{s^3+10s^2+25s+10}$

> [!note]- Semboller
> - **KYE**: $K$ değiştikçe kapalı çevrim kutuplarının izlediği eğri ($0\le K<\infty$); dal sayısı $=$ kutup sayısı $n$
> - $n$: kutup, $m$: sıfır sayısı; asimptot sayısı $=n-m$, açılar $\dfrac{(2k+1)180°}{n-m}$
> - $\sigma_a=\dfrac{\sum\text{kutup}-\sum\text{sıfır}}{n-m}$: asimptot merkezi (gerçek eksende)
> - **Breakaway** (ayrılma): KYE'nin gerçek ekseni terk ettiği nokta; $\dfrac{dK}{ds}=0$ ya da $D'(s)=0$
> - **$j$-ekseni kesişimi**: kararlılık sınırı; Routh'tan kritik $K$ ve yardımcı polinomdan $\omega$
> - Gerçek eksen kuralı: bir noktanın sağındaki kutup+sıfır sayısı **tek** ise o nokta KYE üzerindedir

**Kutuplar:** $p_1 = -6.264$, $p_2 = -3.244$, $p_3 = -0.492$ (sıfır yok)

**Dal sayısı:** 3

**Gerçek eksen üzerindeki KYE:**
- $(-\infty, -6.264)$: sağda 3 kutup → tek → **KYE var**
- $(-6.264, -3.244)$: sağda 2 → çift → **KYE yok**
- $(-3.244, -0.492)$: sağda 1 → tek → **KYE var**

**Asimptotlar:** $n-m=3$, açılar $60°, 180°, 300°$

$$\sigma_a = \frac{-6.264 - 3.244 - 0.492}{3} = \frac{-10}{3} \approx -3.33$$

**Breakaway:** $D(s) = s^3+10s^2+25s+10$, $D'(s) = 3s^2+20s+25=0$
$$s = -5 \text{ veya } s = -1.667 \quad \to \quad \text{sadece } s = -1.667 \text{ KYE üzerinde}$$

**j-Ekseni:** Routh'tan $K=240$, yardımcı polinom $10s^2+250=0 \implies \omega=5$ rad/s

---

## Örnek 2: $G(s) = \dfrac{K}{s^4+7s^3+11s^2+7s}$

**Kutuplar:** $0, -5.118, -0.941\pm j0.694$ (sıfır yok)

**Asimptotlar:** $n-m=4$, açılar $45°, 135°, 225°, 315°$

$$\sigma_a = \frac{0 + (-5.118) + (-0.941) + (-0.941)}{4} = \frac{-7}{4} = -1.75$$

**Gerçek eksen KYE:** $(-5.118, 0)$ aralığı

**Breakaway:** $D'(s) = 4s^3+21s^2+22s+7=0 \implies s \approx -3.978$

**j-Ekseni:** $K=10$, $s = \pm j1$, $\omega = 1$ rad/s

---

## Örnek 3: %5 Aşım için $K$ Tasarımı (Tam Çözüm)

> [!note]- Semboller
> - $\zeta$: sönüm oranı; %5 aşım → $\zeta\approx0.690$; $\theta=\arccos\zeta$: $\zeta$ doğrusunun gerçek eksenle açısı
> - $s_d$: istenen baskın kutup (deneme noktası); $\zeta$ doğrusu üzerinde aranır
> - **Açı şartı**: $\angle G(s_d)=-180°$ → $s_d$'nin KYE üzerinde olması; kutuplara çizilen vektör açıları toplamı
> - **Genlik şartı**: $K=\dfrac{\prod|\text{kutup vektörleri}|}{\prod|\text{sıfır vektörleri}|}$ → o noktadaki $K$ değeri
> - $\omega_d=\omega_n\sqrt{1-\zeta^2}$: sönümlü frekans; $T_p=\pi/\omega_d$, $T_s\approx4/(\zeta\omega_n)$

$G(s) = \dfrac{K}{s(s+2)(s+5)}$, unity feedback

**Kutuplar:** $0,\,-2,\,-5$ (sıfır yok)

**Asimptotlar:** $n-m=3$, açılar $60°,\,180°,\,300°$

$$\sigma_a = \frac{0+(-2)+(-5)}{3} = -\frac{7}{3} \approx -2.33$$

**Gerçek eksen KYE:** $(-2,0)$ ve $(-\infty,-5)$ aralıkları

**Breakaway** ($d/ds[-s(s+2)(s+5)]=0$): $3s^2+14s+10=0$

$$s = \frac{-14\pm\sqrt{196-120}}{6} = \frac{-14\pm8.72}{6} \implies s_1 \approx -0.88, \quad s_2 \approx -3.78$$

*$s_1 \approx -0.88$: KYE üzerinde (breakaway) ✓; $s_2 \approx -3.78$: KYE üzerinde değil*

**%5 aşım:** $\zeta \approx 0.690$, $\theta = \arccos(0.690) \approx 46.4°$

Baskın kutup doğrusu: $s = -\zeta\omega_n + j\omega_n\sqrt{1-\zeta^2}$, eğim $\tan(180°-46.4°) = \tan(133.6°)$

**Açı şartı** ($\angle G(s_d) = -180°$):

Deneme noktası $s_d = -1.0 + j1.4$ için:

$$\angle\frac{1}{s(s+2)(s+5)}\bigg|_{s_d} = -(146°+36°+9.6°) = -191.6° \approx -180° ✓ \text{ yaklaşık}$$

**Genlik şartından K:**

$$K = |s_d|\cdot|s_d+2|\cdot|s_d+5| = 1.72\times1.47\times4.28 \approx \boxed{10.8}$$

**Doğrulama:** $T_s \approx 4/(\zeta\omega_n) = 4/1.0 = 4$ s, $T_p = \pi/\omega_d \approx \pi/1.4 \approx 2.24$ s

---

## Örnek 4 — KYE ve $j$-Ekseni Kesişimi Özet

> [!note]- Semboller
> - $j$-ekseni kesişimi: karakteristik denkleme $s=j\omega$ koyup reel ve imajiner kısımları **ayrı ayrı sıfıra** eşitle
> - İmajiner kısım $=0$ → salınım frekansı $\omega$; reel kısım $=0$ → kritik kazanç $K_\text{kritik}$
> - $K_\text{kritik}$: sistemin kararlılık sınırındaki kazanç (bu değerin üstünde sağ yarı düzleme geçer)

$G(s) = \dfrac{K}{s(s+3)(s+6)}$

$\sigma_a = (-3-6)/3 = -3$; asimptot açıları $60°, 180°, 300°$

Breakaway: $3s^2+18s+18=0 \Rightarrow s^2+6s+6=0 \Rightarrow s=-3\pm\sqrt{3}$ → KYE üzerindeki kök $s \approx -1.27$

$j$-ekseni ($s=j\omega$):

$$j\omega(j\omega+3)(j\omega+6) + K = 0 \implies (-18\omega^2 + K) + j\omega(18-\omega^2) = 0$$

İmajiner: $\omega^2 = 18 \implies \omega = 3\sqrt{2}$ rad/s; Reel: $K = 18\omega^2 = 324$

$$\boxed{K_\text{kritik} = 324, \quad \omega_\text{salınım} = 3\sqrt{2} \approx 4.24 \text{ rad/s}}$$

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/04 Kök Yer Eğrisi]]

**İlgili:** [[05 Kök Yer Eğrisi ve Kompansasyon|MST&B - KYE & Kompansasyon]]
