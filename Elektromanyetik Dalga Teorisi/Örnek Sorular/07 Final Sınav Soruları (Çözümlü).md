---
tags: [emd, final, sınav-soruları, çözümlü, devamlılık-denklemi, düzlem-dalga, kutuplanma, kayıplı-ortam, yansıma, mükemmel-iletken]
---

# 07 — Final Sınav Soruları (Çözümlü · Sıfırdan Öğretici)

← [[EMD Ana Sayfa]]

> Kaynak: `Masaüstü/EMD Final.jpeg`

> [!abstract] Bu sınav neyi ölçüyor? (önce büyük resim)
> Final **dalga yayılması ve malzeme etkileşimi** ağırlıklı: devamlılık denklemi (S1) + düzlem dalga anlık ifadesi (S2) + kutuplanma analizi (S3) + kayıplı ortam parametreleri (S4) + mükemmel iletken sınırında yansıma (S5). Ortak fikir: **E ve H birbirinden ayrılamaz; dalga yayılır, ortam onu absorbe eder, sınır onu yansıtır**.
>
> | Sembol | Açılım |
> |---|---|
> | **α** | Zayıflama sabiti (Np/m); dalganın genliği $e^{-\alpha z}$ ile azalır |
> | **β** | Faz sabiti (rad/m); $v_p = \omega/\beta$ |
> | **γ** | Yayılma sabiti $= \alpha + j\beta = \sqrt{j\omega\mu(\sigma+j\omega\varepsilon)}$ |
> | **η_c** | Karmaşık öz empedans (Ω): $\|\eta\|\angle\theta_\eta$ |
> | **δ** | Deri kalınlığı $= 1/\alpha$ (m); genliğin $1/e$'ye düştüğü derinlik |
> | **Γ** | Yansıma katsayısı; mükemmel iletken için $\Gamma = -1$ (E için) |
> | **S_avg** | Ortalama Poynting vektörü — birim alandan geçen ortalama güç (W/m²) |

---

## Soru 1 — Yük Yoğunluğu Hesabı (14p)

**Verilen:**
$$\mathbf{J}(x,y,z,t) = \left(\hat{a}_x\,2y - \hat{a}_y\,2z + \hat{a}_z\,z^3\right)\sin(10^4 t)\,\text{A/m}^2$$

- Sınır koşulu: $z = 0$'da $\rho_v(x,y,0,t) = 0$

> [!question] 📝 Soru metni (sınavda sorulan)
> Belirli bir iletken ortamda akım yoğunluğu $\vec{J}(x,y,z,t) = (\hat{a}_x 2y - \hat{a}_y 2z + \hat{a}_z z^3)\sin 10^4 t$ A/m² olarak verilmektedir. Eğer $z = 0$'da $\rho_v(x,y,0,t) = 0$ oluyorsa ortamdaki ilgili yük dağılımı $\rho_v(x,y,z,t)$'yi hesaplayınız. **(14p)**

> [!note]- Semboller
> - Devamlılık denklemi: $\nabla\cdot\mathbf{J} = -\partial\rho_v/\partial t$ (yük korunumu)
> - $\nabla\cdot\mathbf{J} = \partial J_x/\partial x + \partial J_y/\partial y + \partial J_z/\partial z$
> - $\rho_v$: hacimsel serbest yük yoğunluğu (C/m³)

---

### Çözüm

**Adım 1 — Diverjans hesabı:**

$$\nabla\cdot\mathbf{J} = \frac{\partial(2y\sin10^4t)}{\partial x} + \frac{\partial(-2z\sin10^4t)}{\partial y} + \frac{\partial(z^3\sin10^4t)}{\partial z}$$

$$= 0 + 0 + 3z^2\sin(10^4t)$$

**Adım 2 — Devamlılık denklemi:**

$$-\frac{\partial\rho_v}{\partial t} = 3z^2\sin(10^4t)$$

$$\frac{\partial\rho_v}{\partial t} = -3z^2\sin(10^4t)$$

**Adım 3 — Zamana göre integral:**

$$\rho_v = \int -3z^2\sin(10^4t)\,dt = -3z^2 \cdot \frac{-\cos(10^4t)}{10^4} + C(x,y,z)$$

$$\rho_v = \frac{3z^2}{10^4}\cos(10^4t) + C(x,y,z)$$

**Adım 4 — Sınır koşulunu uygula** ($z = 0$'da $\rho_v = 0$):

$$0 = \frac{3\cdot0}{10^4}\cos(10^4t) + C = 0 + C \implies C = 0$$

$$\boxed{\rho_v(x,y,z,t) = \frac{3z^2}{10^4}\cos(10^4t) = 0.3z^2\cos(10^4t)\,\text{mC/m}^3}$$

> [!tip] Kontrol
> $z = 0$: $\rho_v = 0$ ✓ — sınır koşulu sağlandı.
> $\nabla\cdot\mathbf{J} + \partial\rho_v/\partial t = 3z^2\sin(10^4t) + (-3z^2\sin10^4t) = 0$ ✓

---

## Soru 2 — Düzlem Dalga Anlık İfadesi (18p)

**Verilen:**
- $\varepsilon_r = 4$, $\mu_r = 1$, $\sigma = 0$ (kayıpsız dielektrik)
- $+y$ yönünde yayılma, **x yönünde kutuplanmış**
- Frekans: $f = 30\,\text{MHz}$
- Tepe değer: $E_0 = 10\,\text{V/m}$
- $t = 0$, $y = 1\,\text{m}$'de: $E = 5\,\text{V/m}$

> [!question] 📝 Soru metni (sınavda sorulan)
> Bağıl elektrik geçirgenliği $\varepsilon_r = 4$ ve bağıl manyetik geçirgenliği $\mu_r = 1$ olan kayıpsız bir ortamda $+y$ yönünde ilerleyen 30 MHz sinüs biçimli bir düzlem dalganın x yönünde kutuplanmış bir elektrik alanı bulunmaktadır. Elektrik alan şiddetinin 10 V/m tepe değerine sahip olduğu ve $t = 0$ ve $y = 1$ m'de değerinin 5 V/m olduğu biliniyorsa, dalganın elektrik alanının anlık ifadesini elde ediniz. **(18p)**

> [!note]- Semboller
> - $\omega = 2\pi f$; $v_p = c/\sqrt{\mu_r\varepsilon_r}$; $\beta = \omega/v_p$
> - Genel form ($+y$ yönü): $\mathbf{E}(y,t) = E_0\cos(\omega t - \beta y + \varphi_0)\,\hat{a}_x$
> - $\varphi_0$: başlangıç faz açısı (rad) — $t=0, y=1$ koşulundan bulunur

---

### Çözüm

**Adım 1 — Açısal frekans ve β:**

$$\omega = 2\pi\times30\times10^6 = 6\pi\times10^7\,\text{rad/s}$$

$$v_p = \frac{c}{\sqrt{\varepsilon_r}} = \frac{3\times10^8}{2} = 1.5\times10^8\,\text{m/s}$$

$$\beta = \frac{\omega}{v_p} = \frac{6\pi\times10^7}{1.5\times10^8} = \frac{6\pi}{15} = \frac{2\pi}{5} = 0.4\pi\,\text{rad/m}$$

**Adım 2 — Genel form:**

$$\mathbf{E}(y,t) = E_0\cos(\omega t - \beta y + \varphi_0)\,\hat{a}_x$$

Sayıları yerine koy ($E_0=10$, $\omega=6\pi\times10^7$, $\beta=0.4\pi$; $\varphi_0$ henüz bilinmiyor):

$$\mathbf{E}(y,t) = 10\cos(6\pi\times10^7 t - 0.4\pi\,y + \varphi_0)\,\hat{a}_x\,\text{V/m}$$

**Adım 3 — Başlangıç fazını bul** ($t = 0,\;y = 1$ m'de $E = 5$ V/m):

$$10\cos(-0.4\pi\times1 + \varphi_0) = 5$$

$$\cos(\varphi_0 - 0.4\pi) = \frac{1}{2}$$

$$\varphi_0 - 0.4\pi = \pm\frac{\pi}{3}$$

**Çözüm 1:** $\varphi_0 = 0.4\pi + \pi/3 = 2\pi/5 + \pi/3 = 11\pi/15\,\text{rad}$

**Çözüm 2:** $\varphi_0 = 0.4\pi - \pi/3 = 2\pi/5 - \pi/3 = \pi/15\,\text{rad}$ ← daha sade

Kontrol ($\varphi_0 = \pi/15$): $10\cos(-\pi/3) = 10\times\frac{1}{2} = 5$ ✓

$$\boxed{\mathbf{E}(y,t) = 10\cos\!\left(6\pi\times10^7 t - 0.4\pi\,y + \frac{\pi}{15}\right)\hat{a}_x\,\text{V/m}}$$

| Büyüklük | Değer |
|---|---|
| $\omega$ | $6\pi\times10^7$ rad/s |
| $\beta$ | $0.4\pi \approx 1.257$ rad/m |
| $\lambda = 2\pi/\beta$ | $5$ m |
| $v_p$ | $1.5\times10^8$ m/s |
| $\varphi_0$ | $\pi/15 \approx 12°$ rad |

---

## Soru 3 — Kutuplanma Analizi (4p + 10p)

**Verilen:**
$$\mathbf{E}(z,t) = \hat{a}_x\,3\cos(2\pi\times10^8 t - 4\pi z) + \hat{a}_y\,4\cos(2\pi\times10^8 t - 4\pi z)\,\text{V/m}$$

> [!question] 📝 Soru metni (sınavda sorulan)
> Bir manyetik olmayan ($\mu = \mu_0$), kayıpsız, dielektrik ortamda yayılan düzgün düzlem dalganın elektrik alanı $\overline{E}(z,t) = \hat{a}_x3\cos(2\pi10^8t-4\pi z)+\hat{a}_y4\cos(2\pi10^8t-4\pi z)$ V/m olarak verilmektedir.
> **a)** Dalganın hangi yönde yayıldığını yazınız. **(4p)**
> **b)** Dalganın kutuplanma durumunu belirleyiniz ve sebebini açıklayınız. **(10p)**

> [!note]- Semboller
> - Yayılma yönü: faz terimindeki uzay değişkenine bakılır (burada $-4\pi z \to +z$)
> - **Doğrusal (lineer) kutuplanma:** $E_x$ ve $E_y$ arasında faz farkı $\Delta\varphi = 0$ veya $\pi$
> - **Dairesel kutuplanma:** $|E_x| = |E_y|$, $\Delta\varphi = \pm\pi/2$
> - **Eliptik kutuplanma:** genel durum

---

### 3a — Yayılma Yönü (4p)

Faz terimi: $(2\pi\times10^8\,t - 4\pi z)$ → uzay değişkeni $-4\pi z$

$$\boxed{\text{Dalga }+z\text{ yönünde yayılmaktadır.}}$$

### 3b — Kutuplanma Durumu (10p)

**E bileşenlerini yaz:**

$$E_x = 3\cos(2\pi\times10^8 t - 4\pi z)$$
$$E_y = 4\cos(2\pi\times10^8 t - 4\pi z)$$

**Faz farkı:**

İki bileşen de **tam olarak aynı faz argümanına** sahiptir → $\Delta\varphi = 0$

**Genlik oranı:**

$$\frac{E_y}{E_x} = \frac{4}{3} = \text{sabit (zamandan bağımsız)}$$

E vektörü daima $\hat{a}_x$ ile $\hat{a}_y$ arasında sabit bir doğrultuda salınır:

- Sabit açı: $\theta = \arctan(4/3) \approx 53.1°$ (x ekseninden)
- Toplam genlik: $E_0 = \sqrt{3^2 + 4^2} = \sqrt{25} = 5\,\text{V/m}$

$$\boxed{\text{Dalga \textbf{doğrusal (lineer) kutuplandırılmıştır}.}}$$

**Neden?** $E_x$ ve $E_y$ faz farkı $\Delta\varphi = 0$ olduğundan E vektörünün ucu yayılma yönüne dik düzlemde sabit bir doğru üzerinde ileri-geri salınır; elips veya daire çizmez.

---

## Soru 4 — Kayıplı Ortam: Okyanus (16p + 10p + 8p)

**Verilen:**
- Okyanus parametreleri: $\varepsilon_r = 72$, $\mu_r = 1$, $\sigma = 4\,\text{S/m}$
- $+z$ yönünde yayılma
- $\omega = 10^7\,\text{rad/s}$ ($f \approx 1.59\,\text{MHz}$)
- $\mathbf{E}(0,t) = \hat{a}_y\cdot3\cos(10^7 t)\,\text{V/m}$

> [!question] 📝 Soru metni (sınavda sorulan)
> Lineer kutuplanmış bir düzgün düzlem dalga, yapısal parametreleri $\varepsilon_r = 72$, $\mu_r = 1$, $\sigma = 4$ S/m olarak verilen okyanusun içine $+z$ yönünde (aşağıya doğru) yayılmaktadır. Okyanus yüzeyinde ($z = 0$'da) elektrik alan $\overline{E}(0,t) = \hat{a}_y3\cos(10^7t)$ V/m olarak verildiğine göre;
> **a)** Zayıflama sabiti, faz sabiti, faz hızı, ortamın öz empedansı ve deri kalınlığını hesaplayınız. **(16p)**
> **b)** Manyetik alanı hesaplayınız. **(10p)**
> **c)** Okyanusta birim alan başına güç kaybını $z$'nin bir fonksiyonu olarak bulunuz. **(8p)**

> [!note]- Semboller
> - $\sigma/(\omega\varepsilon) \gg 1$: **iyi iletken** koşulu → basitleştirilmiş formüller geçerli
> - $\alpha \approx \beta \approx \sqrt{\omega\mu\sigma/2}$ (iyi iletken)
> - $\|\eta\| = \sqrt{\omega\mu/\sigma}$, $\angle\eta = 45°$ (iyi iletken)
> - $\delta = 1/\alpha$ (deri kalınlığı); $S_{avg} = \frac{1}{2}(E_0^2/\|\eta\|)\cos(\angle\eta)\,e^{-2\alpha z}$

---

### 4a — Parametreler (16p)

**İyi iletken kontrolü:**

$$\varepsilon = \varepsilon_r\varepsilon_0 = 72\times\frac{10^{-9}}{36\pi} = \frac{2}{\pi}\times10^{-9}\,\text{F/m}$$

$$\frac{\sigma}{\omega\varepsilon} = \frac{4}{10^7 \times \frac{2}{\pi}\times10^{-9}} = \frac{4}{\frac{2}{\pi}\times10^{-2}} = \frac{4\pi}{0.02} = 200\pi \approx 628 \gg 1$$

→ **İyi iletken bölgesi** — basitleştirilmiş formüller kullanılır.

---

**Zayıflama ve Faz Sabiti:**

$$\alpha = \beta = \sqrt{\frac{\omega\mu\sigma}{2}} = \sqrt{\frac{10^7\times4\pi\times10^{-7}\times4}{2}} = \sqrt{\frac{4\pi\times4}{2}} = \sqrt{8\pi}$$

$$\boxed{\alpha = \beta = \sqrt{8\pi} \approx 5.013\,\text{Np/m (veya rad/m)}}$$

---

**Faz Hızı:**

$$v_p = \frac{\omega}{\beta} = \frac{10^7}{\sqrt{8\pi}} \approx \frac{10^7}{5.013} \approx 1.995\times10^6\,\text{m/s}$$

$$\boxed{v_p \approx 2\times10^6\,\text{m/s} \approx c/150}$$

---

**Öz Empedans:**

$$\eta_c = \sqrt{\frac{j\omega\mu}{\sigma+j\omega\varepsilon}} \approx \sqrt{\frac{j\omega\mu}{\sigma}} = \sqrt{\frac{j\times4\pi}{4}} = \sqrt{j\pi}$$

$$|\eta| = \sqrt{\frac{\omega\mu}{\sigma}} = \sqrt{\frac{4\pi}{4}} = \sqrt{\pi} \approx 1.772\,\Omega, \qquad \angle\eta = 45°$$

$$\boxed{\eta_c \approx \sqrt{\pi}\angle45° \approx 1.772\angle45°\,\Omega}$$

---

**Deri Kalınlığı:**

$$\delta = \frac{1}{\alpha} = \frac{1}{\sqrt{8\pi}} \approx \frac{1}{5.013} \approx 0.20\,\text{m} = 20\,\text{cm}$$

$$\boxed{\delta \approx 0.20\,\text{m}}$$

### Özet Tablosu

| Büyüklük | Değer |
|---|---|
| $\sigma/(\omega\varepsilon)$ | $200\pi \approx 628$ — **iyi iletken** ✓ |
| $\alpha$ | $\sqrt{8\pi} \approx 5.013$ Np/m |
| $\beta$ | $\sqrt{8\pi} \approx 5.013$ rad/m |
| $v_p$ | $\approx 2\times10^6$ m/s |
| $\|\eta\|$ | $\sqrt{\pi} \approx 1.772$ Ω |
| $\angle\eta$ | $45°$ |
| $\delta$ | $\approx 0.20$ m |

---

### 4b — Manyetik Alan H(z,t) (10p)

E alanının genel formu ($z = 0$'da genlik $E_0 = 3$ V/m):

$$\mathbf{E}(z,t) = \hat{a}_y\cdot3\,e^{-\alpha z}\cos(\omega t - \beta z)\,\text{V/m}$$

$\mathbf{H} = \frac{1}{\eta_c}(\hat{a}_k\times\mathbf{E})$ kullanarak:

$$\hat{a}_z \times \hat{a}_y = -\hat{a}_x$$

Faz ilişkisi: $\eta_c = |\eta|\angle45°$ → H, E'den $45°$ geri kalır:

$$\mathbf{H}(z,t) = \frac{3}{|\eta|}\,(-\hat{a}_x)\,e^{-\alpha z}\cos(\omega t - \beta z - 45°)$$

$$\boxed{\mathbf{H}(z,t) = -\hat{a}_x\cdot\frac{3}{\sqrt{\pi}}\,e^{-\sqrt{8\pi}\,z}\cos\!\left(10^7 t - \sqrt{8\pi}\,z - 45°\right)\,\text{A/m}}$$

Sayısal: $3/\sqrt{\pi} \approx 1.693$ A/m, $\sqrt{8\pi} \approx 5.013$ m⁻¹

---

### 4c — Birim Alan Başına Güç Kaybı (8p)

Ortalama Poynting vektörü:

$$S_{avg}(z) = \frac{1}{2}\frac{E_0^2}{|\eta|}\cos(\angle\eta)\,e^{-2\alpha z}$$

$$= \frac{1}{2}\cdot\frac{9}{\sqrt{\pi}}\cdot\cos45°\cdot e^{-2\sqrt{8\pi}\,z}$$

$$= \frac{1}{2}\cdot\frac{9}{\sqrt{\pi}}\cdot\frac{1}{\sqrt{2}}\cdot e^{-2\sqrt{8\pi}\,z} = \frac{9}{2\sqrt{2\pi}}\,e^{-2\sqrt{8\pi}\,z}$$

$$\boxed{S_{avg}(z) = \frac{9}{2\sqrt{2\pi}}\,e^{-2\sqrt{8\pi}\,z} \approx 1.795\,e^{-10.03\,z}\,\text{W/m}^2}$$

> [!info] Yorum
> $z = \delta = 0.20$ m'de güç, yüzeydeki değerin $e^{-2} \approx 13.5\%$'ine düşer. Okyanus yüksek frekanslı dalgaları (VHF, UHF) son derece hızlı söndürür; denizaltı haberleşmesi bu yüzden çok düşük frekanslarda (ELF: 3–30 Hz) yapılır.

---

## Soru 5 — Mükemmel İletken Sınırında Yansıma (20p)

**Verilen:**
- Kutuplanma: **y yönünde** (TE)
- Frekans: $f = 1\,\text{GHz}$
- Ortam: hava (serbest uzay), $\eta_0 = 120\pi\,\Omega$
- Yayılma: $+x$ yönünde, $x = 0$'da **mükemmel iletken** sınır
- Gelen dalga genliği: $E_0 = 12\,\text{mV/m}$

> [!question] 📝 Soru metni (sınavda sorulan)
> y yönünde kutuplanmış, 1 GHz'lik düzgün düzlem dalga $(\overline{E}_i, \overline{H}_i)$ havada $+x$ yönünde yayılmakta ve $x = 0$'daki mükemmel iletken sınıra dik olarak çarpmaktadır. Gelen dalganın elektrik alanının genliği 12 mV/m ise
> **a)** gelen dalga için $\overline{E}_i(x,t)$ ve $\overline{H}_i(x,t)$ anlık ifadelerini bulunuz. **(10p)**
> **b)** yansıyan dalga için $\overline{E}_r(x,t)$ ve $\overline{H}_r(x,t)$ anlık ifadelerini bulunuz. **(10p)**

> [!note]- Semboller
> - Mükemmel iletken: yüzeyde $E_t = 0$ → Yansıma katsayısı $\Gamma_E = -1$
> - $\Gamma_H = +1$: H yansıma katsayısı (E'nin tersi)
> - $\beta = \omega/c = 2\pi f/c$
> - Düzlem dalga: $\mathbf{H} = \frac{1}{\eta_0}(\hat{a}_k\times\mathbf{E})$

---

### 5a — Gelen Dalga (10p)

**Faz sabiti:**

$$\omega = 2\pi\times10^9\,\text{rad/s}$$

$$\beta = \frac{\omega}{c} = \frac{2\pi\times10^9}{3\times10^8} = \frac{20\pi}{3}\,\text{rad/m}$$

**E_i:** y-kutuplanmış, +x yönünde yayılıyor:

$$\boxed{\mathbf{E}_i(x,t) = \hat{a}_y\cdot12\cos\!\left(2\pi\times10^9 t - \frac{20\pi}{3}x\right)\,\text{mV/m}}$$

**H_i:** $\hat{a}_k = \hat{a}_x$, $\hat{a}_x\times\hat{a}_y = \hat{a}_z$:

$$|H_0| = \frac{E_0}{\eta_0} = \frac{12\times10^{-3}}{120\pi} = \frac{1}{10\pi}\times10^{-3}\,\text{A/m} = \frac{0.1}{\pi}\,\text{mA/m} \approx 31.83\,\mu\text{A/m}$$

$$\boxed{\mathbf{H}_i(x,t) = \hat{a}_z\cdot\frac{1}{10\pi}\cos\!\left(2\pi\times10^9 t - \frac{20\pi}{3}x\right)\,\text{mA/m}}$$

---

### 5b — Yansıyan Dalga (10p)

Mükemmel iletken yüzeyde ($x = 0$): $\mathbf{E}_{toplam}^{tan} = 0$

$$\Gamma_E = -1 \implies E_{r0} = -E_{i0} = -12\,\text{mV/m}$$

Yansıyan dalga $-x$ yönünde gider → $\hat{a}_{kr} = -\hat{a}_x$:

$$\boxed{\mathbf{E}_r(x,t) = -\hat{a}_y\cdot12\cos\!\left(2\pi\times10^9 t + \frac{20\pi}{3}x\right)\,\text{mV/m}}$$

H_r: $(-\hat{a}_x)\times(-\hat{a}_y) = \hat{a}_x\times\hat{a}_y = \hat{a}_z$

$$\Gamma_H = +1 \implies H_{r0} = +\frac{12\,\text{mV/m}}{\eta_0}$$

$$\boxed{\mathbf{H}_r(x,t) = +\hat{a}_z\cdot\frac{1}{10\pi}\cos\!\left(2\pi\times10^9 t + \frac{20\pi}{3}x\right)\,\text{mA/m}}$$

---

### Sınır Koşulu Kontrolü

**x = 0'da E tanjansiyeli = 0 olmalı:**

$$\mathbf{E}_i(0,t) + \mathbf{E}_r(0,t) = \hat{a}_y\cdot12\cos(\omega t) + (-\hat{a}_y\cdot12\cos(\omega t)) = 0\,\checkmark$$

**x = 0'da yüzey akımı:**

$$\mathbf{H}_{toplam}(0,t) = \hat{a}_z\cdot\frac{2}{10\pi}\cos(\omega t) = \hat{a}_z\cdot\frac{1}{5\pi}\cos(\omega t)\,\text{mA/m}$$

Bu, iletken yüzeyde oluşan yüzey akımı $\mathbf{K} = \hat{n}\times\mathbf{H}$ ile tutarlıdır. ✓

> [!success] Özet — Mükemmel İletken Kuralları
> | Büyüklük | Gelen | Yansıyan | Neden |
> |---|---|---|---|
> | E genliği | $E_0$ | $-E_0$ | $\Gamma_E = -1$ |
> | H genliği | $H_0$ | $+H_0$ | $\Gamma_H = +1$ |
> | Yayılma | $+x$ | $-x$ | Geri yansır |
> | Yüzey E | \| | $E_t(0) = 0$ | Mükemmel iletken koşulu |
