---
tags: [emd, bütünleme, formül-sayfası]
cssclass: formul-sheet
---

# EMD — Formül Sayfası (Sınav İçin)

← [[EMD Ana Sayfa]]

> Baskı için kompakt özet. Her formül sınav için kritik.

---

## 1. Vektör Özdeşlikleri

| Özdeşlik | İfade |
|----------|-------|
| $\nabla\cdot(\nabla\times\mathbf{A})$ | $\equiv 0$ |
| $\nabla\times(\nabla\phi)$ | $\equiv 0$ |
| $\nabla\times(\nabla\times\mathbf{A})$ | $\nabla(\nabla\cdot\mathbf{A})-\nabla^2\mathbf{A}$ |
| Stokes | $\oint_C\mathbf{A}\cdot d\mathbf{l}=\iint_S(\nabla\times\mathbf{A})\cdot d\mathbf{S}$ |
| Gauss | $\unicode{x222F}_S\mathbf{A}\cdot d\mathbf{S}=\iiint_V(\nabla\cdot\mathbf{A})\,dv$ |

---

## 2. Maxwell Denklemleri

| Yasa | Diferansiyel | İntegral |
|------|-------------|----------|
| Faraday | $\nabla\times\mathbf{E}=-\partial_t\mathbf{B}$ | $\oint\mathbf{E}\cdot d\mathbf{l}=-d\Phi_B/dt$ |
| Ampere-Maxwell | $\nabla\times\mathbf{H}=\mathbf{J}+\partial_t\mathbf{D}$ | $\oint\mathbf{H}\cdot d\mathbf{l}=I+d\Phi_D/dt$ |
| Gauss E | $\nabla\cdot\mathbf{D}=\rho$ | $\unicode{x222F}\mathbf{D}\cdot d\mathbf{S}=Q_{enc}$ |
| Gauss B | $\nabla\cdot\mathbf{B}=0$ | $\unicode{x222F}\mathbf{B}\cdot d\mathbf{S}=0$ |

Ortam: $\mathbf{D}=\epsilon\mathbf{E}$, $\mathbf{B}=\mu\mathbf{H}$, $\mathbf{J}=\sigma\mathbf{E}$

---

## 3. Sınır Koşulları

| Bileşen | Genel | İdeal İletken ($\sigma_2=\infty$) |
|---------|-------|-----------------------------------|
| $E_t$ | $E_{1t}=E_{2t}$ | $E_{1t}=0$ |
| $H_t$ | $H_{1t}-H_{2t}=J_s$ | $\hat{n}\times\mathbf{H}_1=\mathbf{J}_s$ |
| $D_n$ | $D_{1n}-D_{2n}=\rho_s$ | $\hat{n}\cdot\mathbf{D}_1=\rho_s$ |
| $B_n$ | $B_{1n}=B_{2n}$ | $B_{1n}=0$ |

---

## 4. Dalga ve Ortam Parametreleri

| Büyüklük | Formül |
|----------|--------|
| Yayılma hızı | $u_p=1/\sqrt{\mu\epsilon}$, serbest uzay $c=3\times10^8$ m/s |
| Dalga sayısı | $k=\omega/u_p=\omega\sqrt{\mu\epsilon}$ |
| Öz empedans | $\eta=\sqrt{\mu/\epsilon}$, serbest uzay $\eta_0\approx377\ \Omega$ |
| Dalga boyu | $\lambda=2\pi/k=u_p/f$ |
| Kompleks $\gamma$ | $\gamma=\alpha+j\beta=j\omega\sqrt{\mu\epsilon_c}$ |
| Deri kalınlığı | $\delta=1/\alpha=\sqrt{2/\omega\mu\sigma}$ (iletken) |
| Grup hızı | $u_g=1/(d\beta/d\omega)$ |

---

## 5. Düzlemsel Dalga

$$\mathbf{E}=\hat{x}E_0e^{-\alpha z}\cos(\omega t-\beta z)$$
$$\mathbf{H}=\frac{\hat{y}E_0}{|\eta|}e^{-\alpha z}\cos(\omega t-\beta z-\theta_\eta)$$
$$\mathbf{E}\perp\mathbf{H}\perp\hat{k}$$

---

## 6. Poynting Vektörü

$$\mathbf{S}_{av}=\frac{1}{2}\text{Re}[\mathbf{E}_s\times\mathbf{H}_s^*]=\frac{|E_0|^2}{2\eta}\hat{k}$$

---

## 7. Yansıma ve Kırılma

**Dik Gelme:**
$$\Gamma=\frac{\eta_2-\eta_1}{\eta_2+\eta_1}, \quad \tau=\frac{2\eta_2}{\eta_2+\eta_1}=1+\Gamma$$
$$R=|\Gamma|^2, \quad T=1-|\Gamma|^2$$

**Snell:** $n_1\sin\theta_i=n_2\sin\theta_t$

**TE Fresnel:** $\Gamma_{TE}=\dfrac{\eta_2\cos\theta_i-\eta_1\cos\theta_t}{\eta_2\cos\theta_i+\eta_1\cos\theta_t}$

**TM Fresnel:** $\Gamma_{TM}=\dfrac{\eta_2\cos\theta_t-\eta_1\cos\theta_i}{\eta_2\cos\theta_t+\eta_1\cos\theta_i}$

**Kritik açı:** $\theta_c=\arcsin(n_2/n_1)$ (sadece $n_1>n_2$)

**Brewster:** $\tan\theta_B=n_2/n_1$ (TM pol.)

---

## 8. İletim Hatları

| Büyüklük | Formül |
|----------|--------|
| $\gamma$ | $\sqrt{(R'+j\omega L')(G'+j\omega C')}$ |
| $Z_0$ (kayıpsız) | $\sqrt{L'/C'}$ |
| $\Gamma_L$ | $(Z_L-Z_0)/(Z_L+Z_0)$ |
| $Z_{in}$ (kayıpsız) | $Z_0\dfrac{Z_L+jZ_0\tan\beta\ell}{Z_0+jZ_L\tan\beta\ell}$ |
| SWR | $(1+|\Gamma_L|)/(1-|\Gamma_L|)$ |
| $\lambda/4$ dönüştürücü | $Z_{in}=Z_0^2/Z_L$ |

---

## 9. Sabitler

$$\mu_0=4\pi\times10^{-7}\ \text{H/m}, \quad \epsilon_0=8.854\times10^{-12}\ \text{F/m}$$
$$c=2.998\times10^8\ \text{m/s}\approx3\times10^8, \quad \eta_0=120\pi\approx377\ \Omega$$
$$k_0=\omega/c, \quad \lambda_0=c/f$$

---

**Bağlantılar:** [[01 Vektör Analizi ve del Operatörü]] | [[02 Maxwell Denklemleri]] | [[03 Dalga Yayılması ve Düzlemsel Dalgalar]] | [[04 Yansıma Kırılma ve Sınır Koşulları]] | [[05 İletim Hatları]]
