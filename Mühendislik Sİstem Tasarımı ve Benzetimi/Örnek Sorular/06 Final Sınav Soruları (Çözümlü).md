---
tags: [mst, final, sınav-soruları, çözümlü, kök-yer-eğrisi, doğrusallaştırma, faz-portresi, denge-noktası]
---

# 06 — MST&B Final Sınav Soruları (Çözümlü)

← [[MST Ana Sayfa]]

> Kaynak PDF: `DATASET/Mühendislik Sistem Tasarımı ve Benzetimi/MST_Final_Cevap_Anahtari.pdf`

---

## Soru 1 — Kök Yer Eğrisi ve PD Denetleyici Tasarımı

**Verilen:**
$$G(s) = \frac{K}{(s+1)(s+2)(s+3)}$$

Sistemin kök yer eğrisini çizin ve tasarım adımlarını gerçekleştirin.

---

### Adım 1 — Sıfır ve Kutup Sayıları (1p)

- **Sıfırlar:** yok → $n = 0$
- **Kutuplar:** $s = -1,\,-2,\,-3$ → $m = 3$

---

### Adım 2 — Kök Yer Eğrisi Taslağı (1p)

```
jω
 ↑     +1.317j
 |    /
─X────X────X────── σ
-3   -2   -1
 |    \
 |     -1.317j
```

3 dal, 3 kutuptan çıkar, 3 asimptota gider.

---

### Adım 3 — Asimptot Sayısı (1p)

$$m - n = 3 - 0 = \boxed{3 \text{ adet}}$$

---

### Adım 4 — Asimptot Açıları (1p)

$$\beta = \frac{180°(2k+1)}{m-n} = \frac{180°(2k+1)}{3} \Rightarrow \boxed{60°,\ 180°,\ 300°}$$

---

### Adım 5 — Asimptotların Reel Ekseni Kestiği Nokta (1p)

$$\sigma_a = \frac{\sum\text{kutuplar} - \sum\text{sıfırlar}}{m-n} = \frac{(-1-2-3) - 0}{3} = \frac{-6}{3} = \boxed{-2}$$

---

### Adım 6 — Ayrılma-Birleşme Noktası (1p)

$$\left(\frac{1}{G(s)}\right)' = 0 \Rightarrow \left(\frac{(s+1)(s+2)(s+3)}{K}\right)' = 0$$

Açılırsa:
$$(s^2+3s+2)(s+3) = s^3+6s^2+11s+6$$

$$(s^3+6s^2+11s+6)' = 3s^2+12s+11 = 0$$

$$s = \frac{-12 \pm \sqrt{144-132}}{6} = \frac{-12 \pm \sqrt{12}}{6}$$

$$\boxed{s_1 = -1{,}142 \quad (\text{reel eksende, geçerli})}$$
$$s_2 = -2{,}57 \quad (\text{reel eksende, geçerli})$$

---

### Adım 7 — Sönüm Oranı (%20 aşım için) (1p)

$$\zeta = \frac{-\ln(\%OS)}{\sqrt{\pi^2 + \ln^2(\%OS)}} = \frac{-\ln(0{,}20)}{\sqrt{\pi^2 + \ln^2(0{,}20)}} = \frac{1{,}609}{\sqrt{9{,}870 + 2{,}590}} = \boxed{0{,}456}$$

---

### Adım 8 — Sönüm Açısı (1p)

$$\beta = \cos^{-1}(\zeta) = \cos^{-1}(0{,}456) = \boxed{62{,}87°}$$

---

### Adım 9 — İstenen Kutup Konumu ve K Kritik (her biri 1p)

$s_d = 1{,}8594\angle 117{,}26°$:
$$s_d = 1{,}8594(\cos 117{,}26° + j\sin 117{,}26°) = -0{,}866 + j1{,}169$$

Kutuplardan uzaklıklar:
$$\ell_1 = \sqrt{(3-0{,}866)^2 + 1{,}169^2} = 2{,}72$$
$$\ell_2 = \sqrt{(2-0{,}866)^2 + 1{,}169^2} = 2{,}035$$
$$\ell_3 = \sqrt{(1-0{,}866)^2 + 1{,}169^2} = 1{,}695$$

$$\boxed{K = \frac{\prod\text{kutup uzaklıkları}}{\prod\text{sıfır uzaklıkları}} = \ell_1 \cdot \ell_2 \cdot \ell_3 = 2{,}72 \times 2{,}035 \times 1{,}695 = 8{,}33}$$

---

### Adım 10 — Kararlı Durum Hatası (1p + 1p)

**Tip 0** sistem (açık çevrimde serbest integratör yok):

$$K_p = \lim_{s\to 0} G(s) = \frac{8{,}33}{(1)(2)(3)} = 1{,}565$$

$$\boxed{e_{ss} = \frac{1}{1+K_p} = \frac{1}{2{,}565} = 0{,}39}$$

---

### Adım 11 — İmajiner Ekseni Kesme Noktası (Routh-Hurwitz) (1p)

Kapalı çevrim karakteristik polinomu:
$$s^3 + 6s^2 + 11s + (6+K) = 0$$

| $s^3$ | 1 | 11 |
|--------|---|-----|
| $s^2$ | 6 | $6+K$ |
| $s^1$ | $\frac{66-(6+K)}{6} = \frac{60-K}{6}$ | 0 |
| $s^0$ | $6+K$ | — |

Kararlılık koşulu: $60 - K > 0$ ve $6+K > 0$ → $\boxed{-6 < K < 60}$

$K = 60$ olursa imajiner eksen kesimi: $s^3 + 6s^2 + 11s + 66 = 0$

Çözüm: $s_1 = -6$, $s_{2,3} = \pm j3{,}317$

---

### Adım 12 — Yerleşme Süresi ve PD Tasarımı (her biri 1p)

**Mevcut sistem için:**
$$t_s = \frac{4}{\zeta\omega_n} = \frac{4}{0{,}866} = 4{,}62 \text{ s}$$

**İstenen yerleşme süresi** (4 kat iyileştirme):
$$t_{s,\text{yeni}} = \frac{4{,}62}{4} = 1{,}155 \text{ s}$$

**İstenen $\omega_n$:**
$$\omega_{ny} = \frac{4}{\zeta \cdot t_{s,\text{yeni}}} = \frac{4}{0{,}456 \times 1{,}155} = 7{,}59 \text{ rad/s}$$

$$\alpha_y = \omega_{ny}\cdot\zeta = 7{,}59 \times 0{,}456 = 3{,}46$$
$$\omega_y = \tan(62{,}87°) \times 3{,}46 = 6{,}75$$

**İstenen kutup:** $s_y = -3{,}46 + j6{,}75$

**PD sıfırının bulunması** (açı koşulu):
$$\theta_1 - (\theta_2 + \theta_3 + \theta_4) = -180°$$
$$\theta_1 - (83{,}9° + 102{,}2° + 110{,}02°) = -180°$$
$$\theta_1 = 126{,}12° \Rightarrow \theta_1' = 180° - 126{,}12° = 53{,}88°$$

$$\tan(53{,}88°) = \frac{6{,}75}{3{,}46 - x} \Rightarrow 1{,}37 = \frac{6{,}75}{3{,}46-x} \Rightarrow \boxed{z_c = x = 3{,}32}$$

**PD transfer fonksiyonu:**
$$G_{PD}(s) = -R_2 C\!\left(s + \frac{1}{R_1 C}\right)$$

Tasarım kısıtları:
$$\frac{1}{R_1 C} = 3{,}32, \quad R_2 C = 1$$

---

## Soru 2 — Doğrusal Olmayan Sistem: Denge ve Kararlılık

**Verilen:**
$$\dot{x} = x^2 - y - 1 \equiv f_1(x,y)$$
$$\dot{y} = y(x-2) \equiv f_2(x,y)$$

---

### 2a — Denge Noktaları (2p + 2p + 2p)

$\dot{x} = 0$, $\dot{y} = 0$ koşulu:

$$0 = x^2 - y - 1 \quad \Rightarrow \quad x^2 = y+1$$
$$0 = y(x-2) \quad \Rightarrow \quad y = 0 \text{ veya } x = 2$$

**$y = 0$ için:** $x^2 = 1$ → $x = \pm 1$ → **(−1, 0)** ve **(1, 0)**

**$x = 2$ için:** $y = 4-1 = 3$ → **(2, 3)**

$$\boxed{\text{Denge noktaları: } (-1,0),\ (1,0),\ (2,3)}$$

---

### 2b — Jacobian Matrisi (3p)

$$J = \begin{bmatrix} \dfrac{\partial f_1}{\partial x} & \dfrac{\partial f_1}{\partial y} \\[8pt] \dfrac{\partial f_2}{\partial x} & \dfrac{\partial f_2}{\partial y} \end{bmatrix} = \begin{bmatrix} 2x & -1 \\ y & x-2 \end{bmatrix}$$

---

### 2c — Her Denge Noktasında Kararlılık (her biri 3p)

#### (−1, 0) noktası:

$$J_{(-1,0)} = \begin{bmatrix} -2 & -1 \\ 0 & -3 \end{bmatrix}$$

$$\det(\lambda I - J) = (\lambda+2)(\lambda+3) = 0 \Rightarrow \lambda_1 = -2,\ \lambda_2 = -3$$

✅ Her iki özdeğer negatif reel → **Kararlı nokta (Stable Point)**

---

#### (1, 0) noktası:

$$J_{(1,0)} = \begin{bmatrix} 2 & -1 \\ 0 & -1 \end{bmatrix}$$

$$(\lambda - 2)(\lambda + 1) = 0 \Rightarrow \lambda_1 = +2,\ \lambda_2 = -1$$

⚠️ Özdeğerler zıt işaretli → **Eyer Noktası (Saddle Point)**

---

#### (2, 3) noktası:

$$J_{(2,3)} = \begin{bmatrix} 4 & -1 \\ 3 & 0 \end{bmatrix}$$

$$\lambda(\lambda-4) + 3 = 0 \Rightarrow \lambda^2 - 4\lambda + 3 = 0 \Rightarrow (\lambda-3)(\lambda-1) = 0$$
$$\lambda_1 = 3,\ \lambda_2 = 1$$

❌ Her iki özdeğer pozitif → **Kararsız Nokta (Unstable)**

---

### Faz Portresi Yorumu (3p)

| Denge Noktası | Tür | Davranış |
|---|---|---|
| (−1, 0) | Kararlı düğüm | Yörüngeler bu noktaya yaklaşır |
| (1, 0) | Eyer noktası | Bir yönde yaklaşır, diğerinde uzaklaşır |
| (2, 3) | Kararsız düğüm | Yörüngeler bu noktadan uzaklaşır |

---

## Soru 3 — Doğrusal Olmayan Elektrik Devresi Doğrusallaştırma

**Verilen devre:** Gerilim kaynağı $u(t)$, $L=1\text{H}$ endüktör, doğrusal olmayan direnç $V_r = 2i^2(t)$, DC kaynak $5\text{V}$.

---

### 3a — Sistem Denklemi (5p)

KVL uygulayınca:
$$\boxed{u(t) = \frac{di(t)}{dt} + 2i^2(t) - 5}$$

---

### 3b — Çalışma Noktası (5p)

DC kararlı durumda $\dot{i} = 0$, $u(t) = 0$:
$$0 = 0 + 2i_0^2 - 5 \Rightarrow i_0^2 = 2{,}5 \Rightarrow \boxed{i_0 = 1{,}58\text{ A}}$$

---

### 3c — Taylor Serisi ile Doğrusallaştırma (5p)

$f(i) = 2i^2$ için:
$$f(i) \approx f(i_0) + \left.\frac{df}{di}\right|_{i_0}(i - i_0) = 5 + 4i_0\cdot\delta i(t) = 5 + 6{,}32\,\delta i(t)$$

$i(t) = i_0 + \delta i(t)$ yerine koyunca:
$$u(t) = \frac{d(\delta i)}{dt} + 5 + 6{,}32\,\delta i(t) - 5$$

$$\boxed{u(t) = \frac{d(\delta i)}{dt} + 6{,}32\,\delta i(t)}$$

---

### 3d — Laplace Dönüşümü ve Transfer Fonksiyonu (5p + 5p)

$$U(s) = s\,\Delta I(s) + 6{,}32\,\Delta I(s) = \Delta I(s)(s + 6{,}32)$$

$$\Delta I(s) = \frac{U(s)}{s + 6{,}32}$$

Direnç gerilimi için: $V_r(s) = 4i_0\,\Delta I(s) = 6{,}32\,\Delta I(s)$

$$\boxed{\frac{V_r(s)}{U(s)} = \frac{6{,}32}{s + 6{,}32}}$$

---

## Soru 4 — Yay-Kütle Sistemi: Faz Portresi

**Verilen:** $k=1$, $m=1$, sönümsüz yay-kütle sistemi.

---

### 4a — Hareket Denklemi (5p)

$$F_{net} = ma \Rightarrow -kx = m\ddot{x}$$
$$\boxed{\ddot{x} + x = 0}$$

---

### 4b — Özdeğerler (5p)

Durum değişkenleri: $x_1 = x$, $\dot{x}_1 = \lambda$, $\ddot{x}_1 = \lambda^2$:

$$\lambda^2 + 1 = 0 \Rightarrow \lambda^2 = -1 \Rightarrow \boxed{\lambda = \pm j}$$

Saf sanal özdeğerler → **Merkez noktası (Center)**

---

### 4c — Genel Çözüm (3p + 2p)

$$x_1(t) = A\sin t + B\cos t$$
$$x_2(t) = \dot{x}_1 = A\cos t - B\sin t$$

---

### 4d — Faz Portresi (5p)

$$x_1^2 + x_2^2 = (A\sin t + B\cos t)^2 + (A\cos t - B\sin t)^2$$
$$= A^2(\sin^2 t + \cos^2 t) + B^2(\cos^2 t + \sin^2 t) = A^2 + B^2 = r^2$$

$$\boxed{x_1^2 + x_2^2 = r^2 = \text{sabit}}$$

→ Faz düzleminde **iç içe daireler** — sistem ne kararlı ne kararsız, **Lyapunov anlamında kararlı**.

```
x₂
↑
│  ○○○
│ ○   ○
│○  ·  ○   (merkez)
│ ○   ○
│  ○○○
└──────────→ x₁
```

**Yorum:** Başlangıç koşulları ($A$, $B$) yarıçapı belirler. Sistem salınım yapar, enerji korunur, yörüngeler kapalı.
