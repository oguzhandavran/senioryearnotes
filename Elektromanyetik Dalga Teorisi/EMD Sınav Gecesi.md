---
tags: [emd, sinav-gecesi, ozet]
---

# EMD — Sınav Gecesi Özeti

> Tek sayfa. Maxwell'den İletim Hattına.

---

## 1 — Maxwell Denklemleri (Ezberle)

| | Diferansiyel | İntegral |
|-|-------------|---------|
| Faraday | $\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t$ | $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Phi_B/dt$ |
| Ampere-Maxwell | $\nabla\times\mathbf{H}=\mathbf{J}+\partial\mathbf{D}/\partial t$ | $\oint\mathbf{H}\cdot d\mathbf{l} = I_{enc}+dD/dt$ |
| Gauss-E | $\nabla\cdot\mathbf{D}=\rho_v$ | $\unicode{x222F}\mathbf{D}\cdot d\mathbf{S}=Q_{enc}$ |
| Gauss-B | $\nabla\cdot\mathbf{B}=0$ | $\unicode{x222F}\mathbf{B}\cdot d\mathbf{S}=0$ |

**Ortam:** $\mathbf{D}=\varepsilon\mathbf{E}$, $\mathbf{B}=\mu\mathbf{H}$, $\mathbf{J}=\sigma\mathbf{E}$

---

## 2 — Dalga Denklemleri ve Parametreler

**Serbest uzay:** $c = 1/\sqrt{\mu_0\varepsilon_0} = 3\times10^8$ m/s, $\eta_0 = 120\pi \approx 377\;\Omega$

**Genel ortam:** $v_p = 1/\sqrt{\mu\varepsilon}$, $\eta = \sqrt{\mu/\varepsilon}$

**Yayılma sabiti (kayıplı):** $\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma+j\omega\varepsilon)}$

**Düzlemsel dalga çözümü:**

$$\mathbf{E}(z,t) = E_0 e^{-\alpha z}\cos(\omega t - \beta z)\hat{a}_x$$

$$\mathbf{H} = \frac{\mathbf{E}}{\eta} \quad (\hat{a}_k \times \hat{a}_E = \hat{a}_H)$$

**Hız bul:** $\omega = 2\pi f$, $\beta = \omega/v_p$, $\lambda = 2\pi/\beta$

---

## 3 — Sınır Koşulları

| Bileşen | Koşul |
|---------|-------|
| Teğetsel E | $E_{t1} = E_{t2}$ |
| Normal D | $D_{n2}-D_{n1} = \rho_s$ (yüksüz: eşit) |
| Teğetsel H | $H_{t1}-H_{t2} = \mathbf{K}\times\hat{n}$ (yüksüz: eşit) |
| Normal B | $B_{n1} = B_{n2}$ |

**İki dielektrik sınırı:** $\varepsilon_1 E_{n1} = \varepsilon_2 E_{n2}$; $E_{t1}=E_{t2}$

---

## 4 — Yansıma ve Kırılma

**Normal gelme:**

$$\Gamma = \frac{\eta_2-\eta_1}{\eta_2+\eta_1}, \quad \tau = \frac{2\eta_2}{\eta_2+\eta_1}$$

**Eğik gelme (Snell):** $n_1\sin\theta_i = n_2\sin\theta_t$ ($n = c/v_p = \sqrt{\mu_r\varepsilon_r}$)

**Brewster (TE yok, sadece TM):** $\tan\theta_B = n_2/n_1$

**Toplam yansıma:** $\theta_c = \arcsin(n_2/n_1)$ (sadece $n_1>n_2$)

---

## 5 — İletim Hattı (Kayıpsız)

$$Z_0 = \sqrt{L'/C'}, \quad \beta = \omega\sqrt{L'C'}, \quad v_p = 1/\sqrt{L'C'}$$

$$\Gamma_L = \frac{Z_L-Z_0}{Z_L+Z_0}$$

$$Z_{in} = Z_0\frac{Z_L+jZ_0\tan(\beta\ell)}{Z_0+jZ_L\tan(\beta\ell)}$$

$$SWR = \frac{1+|\Gamma_L|}{1-|\Gamma_L|}$$

**Özel:** Kısa devre $\Gamma=-1$; Açık devre $\Gamma=+1$; Uyumlu $\Gamma=0$.

**$\lambda/4$ dönüştürücü:** $Z_{in}=Z_0^2/Z_L$

---

## 6 — Poynting ve Güç

$$\mathbf{S} = \mathbf{E}\times\mathbf{H}, \quad P_{av} = \frac{1}{2}\text{Re}[\mathbf{E}\times\mathbf{H}^*]$$

---

## Tuzaklar

> [!warning] EMD Tuzakları
> - $\hat{a}_k \times \hat{a}_E = \hat{a}_H$ — yön ilişkisini hep kontrol et!
> - $\eta$ gerçel ise lossless, karmaşık ise kayıplı ortam
> - Sınırda teğetsel $E$ sürekli, normal $D$ sürekli (yüksüz)
> - Snell: açılar **normale** göre ölçülür, yüzeye değil
> - İletim hattı empedansı: $Z_{in}$ formülünde $\tan(\beta\ell)$ — $\lambda/4$ için $\tan = \infty$
> - Deplasman akımı: $J_D = \varepsilon\partial E/\partial t$ — kapasitörde iletim akımına eşit

---

← [[EMD Ana Sayfa]] | [[EMD Formül Sayfası]]
