---
tags: [emd, bütünleme, maxwell, konu-anlatımı]
---

# 02 — Maxwell Denklemleri

← [[EMD Ana Sayfa]] | Örnekler: [[../Örnek Sorular/02 Maxwell Örnekleri]]

> **Özet:** 4 denklem → elektrik ve manyetik alanların her koşuldaki davranışını belirler. Sınır koşulları → iki ortam arasındaki geçiş.

---

## Maxwell Denklemleri — Ana Tablo

> [!formul] 4 Maxwell Denklemi (Diferansiyel Form)

| # | Yasa | Diferansiyel | Fiziksel Anlam |
|---|------|--------------|----------------|
| 1 | **Faraday** | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ | Değişen B → rotasyonel E üretir |
| 2 | **Ampere-Maxwell** | $\nabla\times\mathbf{H} = \mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}$ | Akım + değişen D → H üretir |
| 3 | **Gauss (E)** | $\nabla\cdot\mathbf{D} = \rho$ | E'nin kaynağı serbest yük |
| 4 | **Gauss (B)** | $\nabla\cdot\mathbf{B} = 0$ | Manyetik monopol yok |

---

## İntegral Formlar (Stokes + Gauss Teoremleri ile)

| Yasa           | İntegral Form                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------------- |
| Faraday        | $\oint_C \mathbf{E}\cdot d\mathbf{l} = -\dfrac{d}{dt}\iint_S \mathbf{B}\cdot d\mathbf{S}$          |
| Ampere-Maxwell | $\oint_C \mathbf{H}\cdot d\mathbf{l} = I_{enc} + \dfrac{d}{dt}\iint_S \mathbf{D}\cdot d\mathbf{S}$ |
| Gauss (E)      | $\unicode{x222F}_S \mathbf{D}\cdot d\mathbf{S} = Q_{enc}$                                                   |
| Gauss (B)      | $\unicode{x222F}_S \mathbf{B}\cdot d\mathbf{S} = 0$                                                         |

---

## Ortam / Kurucu Denklemler (Constitutive Relations)

> [!tanim] Lineer, İzotropik, Homojen (LHI) Ortam
> $$\mathbf{D} = \epsilon\mathbf{E} = \epsilon_r\epsilon_0\mathbf{E}$$
> $$\mathbf{B} = \mu\mathbf{H} = \mu_r\mu_0\mathbf{H}$$
> $$\mathbf{J} = \sigma\mathbf{E} \quad\text{(Ohm Yasası)}$$

| Sembol | Ad | SI Birimi |
|--------|-----|-----------|
| $\epsilon_0 = 8.854\times10^{-12}$ | Boşluk permitivitesi | F/m |
| $\mu_0 = 4\pi\times10^{-7}$ | Boşluk permeabilitesi | H/m |
| $c = 1/\sqrt{\mu_0\epsilon_0} \approx 3\times10^8$ | Işık hızı | m/s |

---

## Deplasman Akımı — Maxwell'in Katkısı

> [!tanim] Neden Ampere yasasına $\partial\mathbf{D}/\partial t$ eklendi?

Statik Ampere: $\nabla\times\mathbf{H}=\mathbf{J}$  
→ Her iki tarafın diverjansı: $\nabla\cdot(\nabla\times\mathbf{H})=0=\nabla\cdot\mathbf{J}$  
Ama süreklilik denklemi: $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t \neq 0$ (dinamik durumda!)

**Çözüm:** $\mathbf{J}_d = \partial\mathbf{D}/\partial t$ (deplasman akımı) ekle:
$$\nabla\times\mathbf{H} = \mathbf{J} + \frac{\partial\mathbf{D}}{\partial t}$$

→ Artık diverjans tutarlı: $\nabla\cdot(\mathbf{J}+\partial\mathbf{D}/\partial t) = \nabla\cdot\mathbf{J}+\partial\rho/\partial t = 0$ ✓

---

## Süreklilik Denklemi

$$\nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t} = 0 \quad\text{(Yük korunumu)}$$

---

## Sınır Koşulları

### Genel (İki Ortam Arası)

Birim normal $\hat{n}_{12}$: ortam 1'den 2'ye doğru.

| Bileşen | Koşul | Açıklama |
|---------|-------|----------|
| $E_t$ (teğet) | $\hat{n}_{12}\times(\mathbf{E}_1-\mathbf{E}_2)=0$ | $E_{1t}=E_{2t}$ — sürekli |
| $H_t$ (teğet) | $\hat{n}_{12}\times(\mathbf{H}_1-\mathbf{H}_2)=\mathbf{J}_s$ | Yüzey akımı varsa atlıyor |
| $D_n$ (normal) | $\hat{n}_{12}\cdot(\mathbf{D}_1-\mathbf{D}_2)=\rho_s$ | Yüzey yükü varsa atlıyor |
| $B_n$ (normal) | $\hat{n}_{12}\cdot(\mathbf{B}_1-\mathbf{B}_2)=0$ | $B_{1n}=B_{2n}$ — sürekli |

### İdeal İletken Arayüzeyi ($\sigma_2=\infty$, iç alanlar=0)

| Koşul | Fiziksel Anlam |
|-------|----------------|
| $E_{1t}=0$ | Teğet E yok |
| $\hat{n}\times\mathbf{H}_1=\mathbf{J}_s$ | Yüzey akımı mevcut |
| $\hat{n}\cdot\mathbf{D}_1=\rho_s$ | Yüzey yük yoğunluğu |
| $B_{1n}=0$ | Normal B yok |

---

## Formül Sayfası — Temel Sabitler

| Büyüklük | Değer |
|----------|-------|
| Boş uzay manyetik geçirgenliği | $\mu_0 = 4\pi\times10^{-7}$ H/m |
| Boş uzay elektrik geçirgenliği | $\varepsilon_0 = \dfrac{10^{-9}}{36\pi} \approx 8.854\times10^{-12}$ F/m |
| EM dalga hızı (boş uzay) | $c = 3\times10^8$ m/s |
| Serbest uzay empedansı | $\eta_0 = \sqrt{\mu_0/\varepsilon_0} = 120\pi \approx 377\;\Omega$ |

**Vektör Özdeşlikleri:**
$$\nabla\times\nabla\times\bar{A} = \nabla(\nabla\cdot\bar{A}) - \nabla^2\bar{A}$$
$$\nabla\cdot(\nabla\times\bar{A}) = 0, \qquad \nabla\times(\nabla V) = 0, \qquad \nabla\cdot(\nabla V) = \nabla^2 V$$

**Koordinat Sistemleri:**

| | Kartezyen $(x,y,z)$ | Silindirik $(r,\phi,z)$ | Küresel $(R,\theta,\phi)$ |
|--|---------------------|------------------------|--------------------------|
| Baz vektörler | $\hat{a}_x,\hat{a}_y,\hat{a}_z$ | $\hat{a}_r,\hat{a}_\phi,\hat{a}_z$ | $\hat{a}_R,\hat{a}_\theta,\hat{a}_\phi$ |
| Metrik $h_1,h_2,h_3$ | $1,1,1$ | $1,\,r,\,1$ | $1,\,R,\,R\sin\theta$ |

Genel koordinatlarda gradyan, diverjans, rotasyonel:
$$\nabla V = \hat{a}_{u_1}\frac{1}{h_1}\frac{\partial V}{\partial u_1} + \hat{a}_{u_2}\frac{1}{h_2}\frac{\partial V}{\partial u_2} + \hat{a}_{u_3}\frac{1}{h_3}\frac{\partial V}{\partial u_3}$$
$$\nabla\cdot\bar{A} = \frac{1}{h_1 h_2 h_3}\left[\frac{\partial}{\partial u_1}(h_2 h_3 A_1)+\frac{\partial}{\partial u_2}(h_1 h_3 A_2)+\frac{\partial}{\partial u_3}(h_1 h_2 A_3)\right]$$

---

## Statik vs Dinamik Karşılaştırma

| Özellik | Statik ($\partial/\partial t=0$) | Dinamik |
|---------|----------------------------------|---------|
| Faraday | $\nabla\times\mathbf{E}=0$ | $\nabla\times\mathbf{E}=-\partial_t\mathbf{B}$ |
| Ampere | $\nabla\times\mathbf{H}=\mathbf{J}$ | $+\partial_t\mathbf{D}$ eklendi |
| E ve H | Tamamen bağımsız | Birbirini doğurur (kuple) |
| Dalga | Yok | EM dalgalar yayılır |

---

> [!sinav] Sınav İpuçları
> - **4 denklemi hem diferansiyel hem integral formda yaz** — sınavda ikisi de sorulur
> - **Deplasman akımı neden eklendi?** → tutarlılık argümanı (diverjans sıfır olmalı)
> - **Sınır koşulları türetimi:** Stokes teor. çok ince döngüye + Gauss teor. çok ince hacme uygula
> - **İdeal iletken:** iç alan sıfır → $E_t=0$, $B_n=0$
> - **Birimler:** $D$: C/m², $E$: V/m, $B$: Wb/m²=T, $H$: A/m

---

**Bağlantılar:** [[01 Vektör Analizi ve del Operatörü]] | [[03 Dalga Yayılması ve Düzlemsel Dalgalar]] | [[04 Yansıma Kırılma ve Sınır Koşulları]] | [[EMD Formül Sayfası]]
