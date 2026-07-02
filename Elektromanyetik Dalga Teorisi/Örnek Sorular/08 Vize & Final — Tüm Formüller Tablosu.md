---
tags: [emd, formül, vize, final, özet, hızlı-bakış]
---

# 08 — Vize & Final · Tüm Formüller Tablosu

← [[EMD Ana Sayfa]]  ·  Vize çözümleri: [[06 Vize Sınav Soruları (Çözümlü)]]  ·  Final çözümleri: [[07 Final Sınav Soruları (Çözümlü)]]

> [!abstract] Nasıl kullanılır?
> Her bölüm hangi soru(lar)da geçtiğini köşeli parantez içinde gösteriyor: **[V1]** = Vize Soru 1, **[F4]** = Final Soru 4 vb. Sınavdan önce hızlıca taramak için tasarlandı.

---

## 1 · Maxwell Denklemleri \[V2]

### İntegral Form

| # | Denklem | İsim |
|---|---|---|
| M1 | $\displaystyle\oint_S \mathbf{D}\cdot d\mathbf{S} = Q_{enc} = \int_V \rho_v\,dV$ | Gauss — Elektrik |
| M2 | $\displaystyle\oint_S \mathbf{B}\cdot d\mathbf{S} = 0$ | Gauss — Manyetik |
| M3 | $\displaystyle\oint_C \mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{S}$ | Faraday |
| M4 | $\displaystyle\oint_C \mathbf{H}\cdot d\mathbf{l} = \int_S \mathbf{J}\cdot d\mathbf{S} + \frac{d}{dt}\int_S \mathbf{D}\cdot d\mathbf{S}$ | Ampere-Maxwell |

### Diferansiyel Form

| # | Denklem |
|---|---|
| M1 | $\nabla\cdot\mathbf{D} = \rho_v$ |
| M2 | $\nabla\cdot\mathbf{B} = 0$ |
| M3 | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ |
| M4 | $\nabla\times\mathbf{H} = \mathbf{J} + \dfrac{\partial\mathbf{D}}{\partial t}$ |

### Malzeme İlişkileri

$$\mathbf{D} = \varepsilon\mathbf{E} \qquad \mathbf{B} = \mu\mathbf{H} \qquad \mathbf{J} = \sigma\mathbf{E}$$

---

## 2 · Faraday İndüksiyon \[V1]

| Denklem | Açıklama |
|---|---|
| $\Phi = \displaystyle\iint_S \mathbf{B}\cdot d\mathbf{S}$ | Manyetik akı tanımı (her zaman integralle başla) |
| $\Phi = B \cdot A$ | Yalnızca **B homojen** ve **B ∥ yüzey normali** ise |
| $\text{EMF} = -\dfrac{d\Phi}{dt}$ | Faraday kanunu — Lenz işareti |
| $\text{EMF}_{hareket} = \displaystyle\oint (\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ | Hareketli çubuk için motörsel EMF (v≠0) |
| Toplam: $\text{EMF} = -\dfrac{d\Phi}{dt} + \displaystyle\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ | Genel durum (V1'de çubuk sabit → ikinci terim = 0) |

---

## 3 · Sınır Koşulları \[V5]

> **Genel** ($J_s$ ve $\rho_s$ sıfır olmayabilir):

| Koşul | Genel | $J_s = 0$, $\rho_s = 0$ |
|---|---|---|
| Tanjansiyel **E** | $\hat{n}_{12}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$ | $E_{1t} = E_{2t}$ |
| Tanjansiyel **H** | $\hat{n}_{12}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ | $H_{1t} = H_{2t}$ |
| Normal **B** | $\hat{n}_{12}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$ | $B_{1n} = B_{2n}$ |
| Normal **D** | $\hat{n}_{12}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$ | $D_{1n} = D_{2n}$ |

*Türetim şekli: M3 → tanjansiyel E, M4 → tanjansiyel H, M2 → normal B, M1 → normal D.*

---

## 4 · Devamlılık Denklemi \[F1]

$$\nabla\cdot\mathbf{J} = -\frac{\partial\rho_v}{\partial t}$$

$$\nabla\cdot\mathbf{J} = \frac{\partial J_x}{\partial x} + \frac{\partial J_y}{\partial y} + \frac{\partial J_z}{\partial z}$$

**Kullanımı:** $\nabla\cdot\mathbf{J}$ bul → $\partial\rho_v/\partial t$ eşitle → zamana göre integral al → sınır koşuluyla sabit belirle.

---

## 5 · Dalga Denklemi ve Potansiyeller \[V4]

| Denklem | Ad |
|---|---|
| $\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}$ | Potansiyel → E ilişkisi |
| $\mathbf{B} = \nabla\times\mathbf{A}$ | Potansiyel → B ilişkisi |
| $\nabla\cdot\mathbf{A} = -\mu\varepsilon\dfrac{\partial V}{\partial t}$ | **Lorenz ölçümü** |
| $\boxed{\nabla^2 V - \mu\varepsilon\dfrac{\partial^2 V}{\partial t^2} = -\dfrac{\rho_v}{\varepsilon}}$ | **V için dalga denklemi** (kaynaklı) |
| $\nabla^2 V = \mu\varepsilon\dfrac{\partial^2 V}{\partial t^2}$ | Kaynak yok ($\rho_v = 0$), homojen |
| $\nabla^2 V = -\dfrac{\rho_v}{\varepsilon}$ | Statik ($\partial/\partial t = 0$) → **Poisson** |
| $v = \dfrac{1}{\sqrt{\mu\varepsilon}}$ | Dalga hızı |

---

## 6 · Kayıpsız Ortam (σ = 0) \[V3, F2]

| Büyüklük | Formül | Not |
|---|---|---|
| Faz hızı | $v_p = \dfrac{c}{\sqrt{\mu_r\varepsilon_r}}$ | $c = 3\times10^8$ m/s |
| Faz sabiti | $\beta = \dfrac{\omega}{v_p} = \omega\sqrt{\mu\varepsilon}$ | rad/m |
| Dalga boyu | $\lambda = \dfrac{2\pi}{\beta}$ | m |
| Öz empedans | $\eta = \sqrt{\dfrac{\mu}{\varepsilon}} = \dfrac{\eta_0}{\sqrt{\varepsilon_r}}$ ($\mu_r=1$) | Ω |
| Serbest uzay | $\eta_0 = 120\pi \approx 377\,\Omega$ | |
| Düzlem dalga E | $\mathbf{E}(\mathbf{r},t) = E_0\cos(\omega t - \beta\,\hat{a}_k\cdot\mathbf{r} + \varphi_0)\,\hat{a}_E$ | |
| Düzlem dalga H | $\mathbf{H} = \dfrac{1}{\eta}(\hat{a}_k\times\mathbf{E})$ | $\hat{a}_k\times\hat{a}_E = \hat{a}_H$ |
| H genliği | $H_0 = \dfrac{E_0}{\eta}$ | |
| Başlangıç faz | $E_0\cos(\varphi_0 - \beta\,y_0) = E(y_0,0)$ | Koşuldan bul |

**Yön vektörü çapraz çarpımları (sağ el):**

$$\hat{a}_z\times\hat{a}_x = \hat{a}_y \qquad \hat{a}_x\times\hat{a}_y = \hat{a}_z \qquad \hat{a}_y\times\hat{a}_z = \hat{a}_x$$

---

## 7 · Kutuplanma Analizi \[F3]

$$\mathbf{E}(z,t) = \hat{a}_x\,E_x\cos(\omega t-\beta z) + \hat{a}_y\,E_y\cos(\omega t-\beta z+\delta)$$

| Tür | Koşul | Sonuç |
|---|---|---|
| **Doğrusal** | $\delta = 0$ veya $\pi$ | E sabit doğrultu, açı $\theta=\arctan(E_y/E_x)$ |
| **Dairesel** | $E_x = E_y$ **ve** $\delta = \pm\pi/2$ | E ucu daire çizer |
| **Eliptik** | Genel durum | E ucu elips çizer |

Toplam genlik (doğrusal): $E_0 = \sqrt{E_x^2 + E_y^2}$

---

## 8 · Kayıplı Ortam — Genel \[F4]

$$\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma+j\omega\varepsilon)}$$

| Büyüklük | Genel Formül |
|---|---|
| $\alpha$ (Np/m) | $\omega\sqrt{\dfrac{\mu\varepsilon}{2}\left(\sqrt{1+\left(\dfrac{\sigma}{\omega\varepsilon}\right)^2}-1\right)}$ |
| $\beta$ (rad/m) | $\omega\sqrt{\dfrac{\mu\varepsilon}{2}\left(\sqrt{1+\left(\dfrac{\sigma}{\omega\varepsilon}\right)^2}+1\right)}$ |
| $\eta_c$ (Ω) | $\sqrt{\dfrac{j\omega\mu}{\sigma+j\omega\varepsilon}}$ |
| $v_p$ (m/s) | $\dfrac{\omega}{\beta}$ |
| $\delta$ (m) | $\dfrac{1}{\alpha}$ |

### İyi İletken Yaklaşımı ($\sigma/\omega\varepsilon \gg 1$)

$$\alpha \approx \beta \approx \sqrt{\frac{\omega\mu\sigma}{2}} \qquad \delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega\mu\sigma}}$$

$$|\eta| \approx \sqrt{\frac{\omega\mu}{\sigma}}, \quad \angle\eta = 45° \qquad \eta_c = |\eta|\angle45°$$

### Kayıplı Ortamda E ve H

$$\mathbf{E}(z,t) = E_0\,e^{-\alpha z}\cos(\omega t - \beta z)\,\hat{a}_E$$

$$\mathbf{H}(z,t) = \frac{E_0}{|\eta|}\,e^{-\alpha z}\cos(\omega t - \beta z - \angle\eta)\,(\hat{a}_k\times\hat{a}_E)$$

> H, E'den $\angle\eta$ kadar **geri kalır** (kayıplı ortamda $\angle\eta > 0$).

---

## 9 · Poynting Vektörü / Güç \[F4c]

| Büyüklük | Formül |
|---|---|
| Anlık Poynting | $\mathbf{S}(t) = \mathbf{E}(t)\times\mathbf{H}(t)$ |
| Ortalama Poynting | $\mathbf{S}_{avg} = \dfrac{1}{2}\text{Re}(\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*)$ |
| Kayıplı ortamda $S_{avg}$ | $\dfrac{1}{2}\dfrac{E_0^2}{|\eta|}\cos(\angle\eta)\,e^{-2\alpha z}$ (W/m²) |
| Kayıpsız ortamda $S_{avg}$ | $\dfrac{E_0^2}{2\eta} = \dfrac{1}{2}\eta H_0^2$ (W/m²) |

---

## 10 · Mükemmel İletken Yansıma \[F5]

> Hava–mükemmel iletken sınırı: sınırda $\mathbf{E}_{tan} = 0$ zorunlu.

| Büyüklük | Değer | Sebep |
|---|---|---|
| $\Gamma_E$ (E yansıma katsayısı) | $-1$ | $E_{1t}=0$ sınır koşulu |
| $\Gamma_H$ (H yansıma katsayısı) | $+1$ | $H_r = \Gamma_H H_i$ |
| $E_{r0}$ | $-E_{i0}$ | |
| $H_{r0}$ | $+H_{i0}$ | |
| Yansıyan yayılma yönü | $-\hat{a}_{ki}$ | Ters yön |

**Gelen dalga (+x yönü, y-kutuplanmış):**

$$\mathbf{E}_i = \hat{a}_y\,E_0\cos(\omega t - \beta x) \qquad \mathbf{H}_i = \hat{a}_z\,\frac{E_0}{\eta_0}\cos(\omega t - \beta x)$$

**Yansıyan dalga (−x yönü):**

$$\mathbf{E}_r = -\hat{a}_y\,E_0\cos(\omega t + \beta x) \qquad \mathbf{H}_r = +\hat{a}_z\,\frac{E_0}{\eta_0}\cos(\omega t + \beta x)$$

**Kontrol:** $\mathbf{E}_i(0,t) + \mathbf{E}_r(0,t) = 0$ ✓

**Serbest uzayda:**

$$\beta = \frac{\omega}{c} = \frac{2\pi f}{c} \qquad \eta_0 = 120\pi \approx 377\,\Omega \qquad H_0 = \frac{E_0}{\eta_0}$$

---

## 11 · Sabitler ve Dönüşümler

| Sabit | Değer |
|---|---|
| $c$ | $3\times10^8$ m/s |
| $\mu_0$ | $4\pi\times10^{-7}$ H/m |
| $\varepsilon_0$ | $\approx 8.854\times10^{-12} \approx \dfrac{10^{-9}}{36\pi}$ F/m |
| $\eta_0 = \sqrt{\mu_0/\varepsilon_0}$ | $120\pi \approx 377\,\Omega$ |
| $c = 1/\sqrt{\mu_0\varepsilon_0}$ | $3\times10^8$ m/s |
| $\omega = 2\pi f$ | rad/s |
| $1\,\text{Np/m}$ | $\approx 8.686\,\text{dB/m}$ |

---

## 12 · Hangi Formülü Ne Zaman? — Hızlı Karar

```
Verilen: akım yoğunluğu J, ρv bulunacak
  → Devamlılık: ∇·J = -∂ρv/∂t  [F1]

Verilen: E(z,t) = ... cos(...t - βz), H = ?
  → β = ω/vp,  H = (1/η)(â_k × E)  [V3, F2]

Verilen: dalganın kutuplanması?
  → Ex, Ey faz farkına bak  [F3]

Verilen: kayıplı ortam (σ≠0), α, β, δ, η = ?
  → σ/(ωε) >> 1 ise iyi iletken formülleri  [F4]

Verilen: mükemmel iletken sınır, yansıyan dalga?
  → ΓE = -1, ΓH = +1  [F5]

Verilen: dalga denklemi türet
  → E = -∇V - ∂A/∂t → Gauss → Lorenz ölçümü  [V4]

Verilen: sınır koşulları
  → 4 Maxwell → h→0 limit  [V5]
```
