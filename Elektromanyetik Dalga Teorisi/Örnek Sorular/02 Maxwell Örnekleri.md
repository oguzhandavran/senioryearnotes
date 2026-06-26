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

> [!example] Problem
> $V_c(t)=V_0\sin(\omega t)$ AC kaynağa bağlı $C_1$ paralel plakalı kapasitör için: **(a)** deplasman akımının teldeki iletim akımına eşit olduğunu göster; **(b)** telden $r$ uzaklıktaki $H$ alanını bul.

> [!note]- Semboller
> - $V_c$: kapasitör gerilimi (V); $V_0,\omega$: genlik ve açısal frekans
> - $q=C_1V_c$: plaka yükü; $i=dq/dt$: iletim akımı (A)
> - $E=V_c/d$: plakalar arası alan ($d$: plaka aralığı); $A$: plaka alanı; $C_1=\varepsilon A/d$
> - $J_D=\varepsilon\,\partial E/\partial t$: deplasman akım yoğunluğu; $i_D=J_D A$: deplasman akımı
> - Ampere: $\oint\bar H\cdot d\bar l=I_{toplam}$ → $H\cdot2\pi r=i$

**Çözüm a):**

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

> [!example] Problem
> Dikdörtgen iletken çerçeve ($a=0.1$ m, $b=0.2$ m), $I(t)=10\cos(2\pi\times10^2 t)$ A taşıyan sonsuz düz telle aynı düzlemde. Telden kaynaklanan manyetik akıyı ve çerçevede indüklenen EMF'yi bul.

> [!note]- Semboller
> - $I(t)$: düz telin akımı; $\bar B=\frac{\mu_0 I}{2\pi y}$: telden $y$ uzaklıkta manyetik alan
> - $a$: telin çerçeveye en yakın kenarına uzaklık; $b$: çerçeve boyutu; sınırlar $y\in[a,a+b]$, $z\in[0,b]$
> - $\Phi_m=\iint\bar B\cdot d\bar S$: çerçeveden geçen akı (Wb)
> - $\mathcal{E}=-d\Phi_m/dt$: Faraday indüksiyon EMF'si (V)
> - $\mu_0=4\pi\times10^{-7}$ H/m; $\ln\frac{a+b}{a}=\ln3$

**Çözüm.** Düz telden $y$ uzaklıkta: $\bar{B} = \dfrac{\mu_0 I(t)}{2\pi y}\hat{a}_x$.

Akı (genişlik $z\in[0,b]$, uzaklık $y\in[a,a+b]$):
$$\Phi_m = \int_a^{a+b}\!\!\int_0^b \frac{\mu_0 I(t)}{2\pi y}\,dz\,dy = \frac{\mu_0 I(t)\,b}{2\pi}\ln\!\left(\frac{a+b}{a}\right)$$

$$\mathcal{E} = -\frac{d\Phi_m}{dt} = -\frac{\mu_0 b}{2\pi}\ln\!\left(\frac{a+b}{a}\right)\frac{dI}{dt}$$

Katsayıyı hesapla: $\dfrac{\mu_0 b}{2\pi}\ln3 = \dfrac{4\pi\times10^{-7}\cdot0.2}{2\pi}\cdot1.0986 = 0.4\times10^{-7}\cdot1.0986 \approx 4.39\times10^{-8}$.

$\dfrac{dI}{dt} = -10\cdot(2\pi\times10^2)\sin(2\pi\times10^2 t) \approx -6283\sin(2\pi\times10^2 t)$. Çarp:

$$\boxed{\mathcal{E}(t) \approx 4.39\times10^{-8}\cdot6283\,\sin(\cdots) \approx 2.76\times10^{-4}\,\sin(2\pi\times10^2 t)\ \text{V} = 0.276\sin(2\pi\times10^2 t)\ \text{mV}}$$

> Devre direnci $R$ verilirse indüklenen akım $i=\mathcal{E}/R$ olur (örn. $R=5\,\Omega$ için $i\approx0.0552\sin(\cdots)$ mA). *(Not: önceki sürümdeki $2.76$ mV değeri 10× yanlıştı; doğru genlik $0.276$ mV.)*

---

## Süreklilik Denkleminin Türetimi (Soru 4)

> [!note]- Semboller
> - $\bar J$: akım yoğunluğu; $\rho_v$: hacim yük yoğunluğu; süreklilik: $\nabla\cdot\bar J=-\partial\rho_v/\partial t$ (yük korunumu)
> - Ohm: $\bar J=\sigma\bar E$ ($\sigma$: iletkenlik); Gauss: $\nabla\cdot\bar E=\rho_v/\varepsilon$
> - $\tau=\varepsilon/\sigma$: relaksasyon (gevşeme) süresi — serbest yükün sönme zaman sabiti
> - Çözüm: $\rho_v(t)=\rho_{v0}e^{-t/\tau}$ (üstel sönüm)

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

> [!note]- Semboller (sınır koşulları örnekleri)
> - $\varepsilon_{r1},\varepsilon_{r2}$: bağıl dielektrik sabitleri; $\hat n$: yüzey normali (burada $\hat a_y$, çünkü sınır $y=0$)
> - Teğetsel ($E_t$): yüzeye paralel bileşenler ($E_x,E_z$) — sürekli
> - Normal ($E_n$): yüzeye dik bileşen ($E_y$) — $\varepsilon_1 E_{1n}=\varepsilon_2 E_{2n}$ ($\rho_s=0$)
> - $\bar D=\varepsilon_0\varepsilon_r\bar E$: deplasman; $\bar P=\varepsilon_0(\varepsilon_r-1)\bar E$: polarizasyon
> - $\theta_1$: $\bar E_1$'in normalle açısı; $\rho_s$: yüzey yük yoğunluğu

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
