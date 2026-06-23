---
tags: [emd, bütünleme, maxwell, örnek-sorular]
---

# 02 — Maxwell Örnekleri

← [[EMD Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Maxwell Denklemleri]]

---

## Maxwell Denklemleri — Hızlı Özet (16 Kas ders notu)

**Diferansiyel form (4 denklem):**

| | Elektrostatik | Dinamik (zamanla değişen) |
|-|---------------|--------------------------|
| Faraday | $\nabla\times\bar{E}=0$ | $\nabla\times\bar{E}=-\dfrac{\partial\bar{B}}{\partial t}$ |
| Ampere | $\nabla\times\bar{H}=\bar{J}$ | $\nabla\times\bar{H}=\bar{J}+\dfrac{\partial\bar{D}}{\partial t}$ |
| Gauss (E) | $\nabla\cdot\bar{D}=\rho_v$ | aynı |
| Gauss (B) | $\nabla\cdot\bar{B}=0$ | aynı |

**Ortam denklemleri:** $\bar{D}=\varepsilon\bar{E}$, $\bar{H}=\bar{B}/\mu$

**Akım türleri:** $\bar{J}_{iletim}=\sigma\bar{E}$, $\bar{J}_{konv}=\rho_v\bar{v}$

**Lorentz kuvvet:** $\bar{F}=q(\bar{E}+\bar{v}\times\bar{B})$

**İntegral form** (Stokes+Gauss teoremi ile türetilir):
$$\oint_C\bar{E}\cdot d\bar{l} = -\frac{d}{dt}\iint_S\bar{B}\cdot d\bar{S} \quad\text{(Faraday)}$$
$$\oint_C\bar{H}\cdot d\bar{l} = \iint_S\!\!\left(\bar{J}+\frac{\partial\bar{D}}{\partial t}\right)\!\cdot d\bar{S} \quad\text{(Ampere)}$$
$$\unicode{x222F}_S\bar{D}\cdot d\bar{S} = \iiint_V\rho_v\,dV \quad\text{(Gauss)}$$
$$\unicode{x222F}_S\bar{B}\cdot d\bar{S} = 0$$

---

## Deplasman Akımı — Kapasitör Örneği

**Problem:** $V_0$ genlikli ve $\omega$ açısal frekanslı $V_c(t)=V_0\sin(\omega t)$ AC kaynağa bağlı $C_1$ paralel plakalı kapasitörde:

a) Kapasitördeki deplasman akımının teldeki iletim akımına eşit olduğunu göster  
b) İletken telden $r$ uzaklıktaki $H$ alanını bul

**Çözüm a):**

① Kapasitör voltajı: $V_c = V_0\sin(\omega t)$

② Plakalardaki yük: $q(t) = C_1 V_c = C_1 V_0\sin(\omega t)$

③ İletim akımı:
$$i(t) = \frac{dq}{dt} = C_1 V_0\omega\cos(\omega t) \quad\text{[A]}$$

④ Kapasitör içi elektrik alanı: $E = V_c/d = (V_0/d)\sin(\omega t)$

$$J_D = \varepsilon\frac{\partial E}{\partial t} = \varepsilon\frac{V_0\omega}{d}\cos(\omega t)$$

Toplam deplasman akımı:
$$i_D = J_D\cdot A = \varepsilon\frac{A}{d}V_0\omega\cos(\omega t) = C_1 V_0\omega\cos(\omega t) \quad\because C_1=\varepsilon A/d$$

$$\boxed{i_D(t) = i(t)} \quad\checkmark$$

**Çözüm b):** Telden $r$ uzaklıktaki $H$ alanı (Ampere devre yasası):

$$\oint_C \bar{H}\cdot d\bar{l} = I_{toplam}(t) = i(t) = C_1 V_0\omega\cos(\omega t)$$
$$H\cdot(2\pi r) = i(t) \implies \boxed{H(r,t) = \frac{C_1 V_0\omega\cos(\omega t)}{2\pi r} \;\text{A/m}}$$

Manyetik akı yoğunluğu: $\bar{B} = \mu_0\bar{H}$ — sağ el kuralı ile çepeçevre.

---

## Karşılıklı İndüktans ve Faraday — Örnek (Soru 3)

**Problem:** Halka şeklinde iletken tel (a=0.1 m, b=0.2 m), $I(t)=10\cos(2\pi\times10^2 t)$ A taşıyan düz telle aynı düzlemde. Sonsuz düz telden kaynaklanan manyetik akıyı ve indüklenen EMF'yi bul.

**Çözüm:**

Düz telden $y$ uzaklıkta: $\bar{B} = \dfrac{\mu_0 I(t)}{2\pi y}\hat{a}_x$

Akı: $\Phi_m = \int_a^{a+b}\int_0^b \dfrac{\mu_0 I(t)}{2\pi y}dz\,dy = \dfrac{\mu_0 I(t)\cdot b}{2\pi}\ln\!\left(\dfrac{a+b}{a}\right)$

$$\mathcal{E} = -\frac{d\Phi_m}{dt} = -\frac{\mu_0 b}{2\pi}\ln\!\left(\frac{a+b}{a}\right)\frac{dI}{dt}$$

$\mu_0=4\pi\times10^{-7}$, $a=0.1$, $b=0.2$, $\ln(3)\approx1.0986$:

$$\frac{dI}{dt} = -10\cdot2\pi\times10^2\sin(2\pi\times10^2 t)$$

$$\mathcal{E}(t) \approx 2.76\sin(2\pi\times10^2 t) \;\text{mV}$$

$$\boxed{i(t) = \frac{\mathcal{E}}{R_{toplam}} = \frac{2.76\sin(2\pi\times10^2 t)\text{ mV}}{5\;\Omega} \approx 0.552\sin(2\pi\times10^2 t) \;\text{mA}}$$

---

## Süreklilik Denkleminin Türetimi (Soru 4)

Doğrusal, homojen, izotropik ortamda yük yoğunluğunun zamanla yok olduğu gösterilir:

$$\nabla\cdot\bar{J} = -\frac{\partial\rho_v}{\partial t} \quad\text{(Süreklilik)}$$
$$\text{Ohm: } \bar{J}=\sigma\bar{E}, \quad \text{Gauss: } \nabla\cdot\bar{E}=\rho_v/\varepsilon$$
$$\nabla\cdot(\sigma\bar{E}) = \sigma\nabla\cdot\bar{E} = \frac{\sigma}{\varepsilon}\rho_v = -\frac{\partial\rho_v}{\partial t}$$

$$\boxed{\frac{\partial\rho_v}{\partial t} + \frac{\sigma}{\varepsilon}\rho_v = 0}$$

Çözüm: $\rho_v(t) = \rho_{v0}\,e^{-(\sigma/\varepsilon)t}$ — iletkenliği olan ortamda serbest yükler $\tau=\varepsilon/\sigma$ relaksasyon süresiyle azalır.

---

## Elektromanyetik Sınır Koşulları — Dielektrik Örnekleri

> [!formul] 4 Temel Sınır Koşulu
> İki ortam sınırında ($\hat{n}$: 2. ortamdan 1. ortama doğru):
>
> | Bileşen | Koşul | Yüzey Terimi |
> |---------|-------|-------------|
> | $\bar{E}$ teğetsel | $(\bar{E}_1-\bar{E}_2)\times\hat{n}=0$ → $E_{1t}=E_{2t}$ | Sürekli |
> | $\bar{D}$ normal | $(\bar{D}_1-\bar{D}_2)\cdot\hat{n}=\rho_s$ | $\rho_s=0$ ise $\varepsilon_1 E_{1n}=\varepsilon_2 E_{2n}$ |
> | $\bar{H}$ teğetsel | $(\bar{H}_1-\bar{H}_2)\times\hat{n}=\bar{J}_s$ | $J_s=0$ ise $H_{1t}=H_{2t}$ |
> | $\bar{B}$ normal | $(\bar{B}_1-\bar{B}_2)\cdot\hat{n}=0$ → $B_{1n}=B_{2n}$ | Sürekli |

**Örnek:** $\varepsilon_{r1}=2.5$, $\varepsilon_{r2}=4$, sınır $y=0$, $\bar{E}_1=-30\hat{a}_x+50\hat{a}_y+70\hat{a}_z$ V/m. $\bar{D}_2$, $\bar{P}_2$, $\theta_1$ bul.

- Teğetsel korunur: $E_{1t}=E_{2t}$ → $E_{2x}=-30$, $E_{2z}=70$
- Normal: $\varepsilon_1 E_{1n}=\varepsilon_2 E_{2n}$ → $2.5\times50=4\times E_{2n}$ → $E_{2n}=31.25$ V/m
- $\bar{E}_2=-30\hat{a}_x+31.25\hat{a}_y+70\hat{a}_z$ V/m

Polarizasyon: $\bar{P}=\varepsilon_0(\varepsilon_r-1)\bar{E}$

**Örnek 2:** $\varepsilon_{r1}=3$, $\varepsilon_{r2}=2$, sınır $y=0$. $\bar{E}_1$ verilince $\bar{E}_2$ bul.

- Normal bileşen: $\varepsilon_1 E_{1n}=\varepsilon_2 E_{2n}$ → $E_{2n}=(\varepsilon_{r1}/\varepsilon_{r2})\cdot E_{1n}$
- Teğetsel: $E_{1t}=E_{2t}$

**Yüzey Yükü Varken:**
$$D_{2n}-D_{1n}=\rho_s \implies \varepsilon_2 E_{2n}-\varepsilon_1 E_{1n}=\rho_s$$

**Özel durumlar:**

| Sınır | $E_t$ | $E_n$ | $D_n$ |
|-------|-------|-------|-------|
| Dielektrik–Dielektrik | Sürekli | $\varepsilon_1 E_{1n}=\varepsilon_2 E_{2n}$ | Süreksiz ($\rho_s$ varsa) |
| Dielektrik–İletken | $E_{2t}=0$ → $E_{1t}=0$ | $E_{2n}=0$, $D_{1n}=\rho_s/\varepsilon_1$ | Süreksiz |
| İletken–İletken | $E_{1t}=E_{2t}$ | $\varepsilon_1 E_{1n}-\varepsilon_2 E_{2n}=\rho_s$ | — |
