---
tags: [emd, bütünleme, vektör-analizi, konu-anlatımı]
---

# 01 — Vektör Analizi ve ∇ Operatörü

← [[EMD Ana Sayfa]] | Örnekler: [[../Örnek Sorular/01 Vektör Analizi Örnekleri]]

> **Özet:** Elektromanyetik denklemlerin dili. ∇ operatörünün üç kullanımı ve iki integral teoremi → Maxwell denklemlerinin temeli.

---

## Koordinat Sistemleri

<svg width="380" height="130" viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-emd01a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Kartezyen (center-left) -->
  <rect x="10" y="40" width="130" height="50" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="75" y="60" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">Kartezyen</text>
  <text x="75" y="78" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#aac4e8">(x, y, z)</text>
  <!-- Arrow to Silindirik (upper right) -->
  <line x1="140" y1="55" x2="222" y2="28" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-emd01a)"/>
  <!-- Silindirik box -->
  <rect x="224" y="10" width="146" height="44" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="297" y="28" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">Silindirik</text>
  <text x="297" y="46" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">(r, φ, z)</text>
  <!-- Arrow to Küresel (lower right) -->
  <line x1="140" y1="75" x2="222" y2="95" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-emd01a)"/>
  <!-- Küresel box -->
  <rect x="224" y="76" width="146" height="44" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="297" y="95" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">Küresel</text>
  <text x="297" y="112" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">(R, θ, φ)</text>
</svg>

| Sistem | Hacim Elemanı $dv$ | Alan Elemanı |
|--------|-------------------|--------------|
| Kartezyen | $dx\,dy\,dz$ | $dy\,dz,\;dx\,dz,\;dx\,dy$ |
| Silindirik | $r\,dr\,d\phi\,dz$ | $r\,d\phi\,dz,\;dr\,dz,\;r\,dr\,d\phi$ |
| Küresel | $R^2\sin\theta\,dR\,d\theta\,d\phi$ | $R^2\sin\theta\,d\theta\,d\phi$ |

---

## ∇ Operatörünün Üç Kullanımı

> [!tanim] del (nabla) Operatörü — Kartezyen
> $$\nabla = \hat{x}\frac{\partial}{\partial x} + \hat{y}\frac{\partial}{\partial y} + \hat{z}\frac{\partial}{\partial z}$$

### 1. Gradient (Skaler → Vektör)

$$\nabla\phi = \hat{x}\frac{\partial\phi}{\partial x} + \hat{y}\frac{\partial\phi}{\partial y} + \hat{z}\frac{\partial\phi}{\partial z}$$

**Fiziksel anlam:** $\phi$'nin en hızlı arttığı yönü ve hızını verir.  
**Elektrik alan:** $\mathbf{E} = -\nabla V$

### 2. Divergence / Diverjans (Vektör → Skaler)

$$\nabla\cdot\mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$

**Fiziksel anlam:** Bir noktadan dışarıya "akan" net akı. Kaynak varsa $\neq 0$.  
**Gauss:** $\nabla\cdot\mathbf{D} = \rho$

### 3. Curl / Rotasyonel (Vektör → Vektör)

$$\nabla\times\mathbf{A} = \begin{vmatrix}\hat{x}&\hat{y}&\hat{z}\\\partial_x&\partial_y&\partial_z\\A_x&A_y&A_z\end{vmatrix}$$

**Fiziksel anlam:** Döngüsel/rotasyonel karakteri ölçer.  
**Faraday:** $\nabla\times\mathbf{E} = -\partial_t\mathbf{B}$

### 4. Laplacian (Skaler → Skaler)

$$\nabla^2\phi = \nabla\cdot(\nabla\phi) = \frac{\partial^2\phi}{\partial x^2}+\frac{\partial^2\phi}{\partial y^2}+\frac{\partial^2\phi}{\partial z^2}$$

Vektörel Laplacian: $\nabla^2\mathbf{A} = \nabla(\nabla\cdot\mathbf{A}) - \nabla\times(\nabla\times\mathbf{A})$

---

## İki Temel İntegral Teoremi

> [!formul] Stokes Teoremi
> $$\oint_C \mathbf{A}\cdot d\mathbf{l} = \iint_S (\nabla\times\mathbf{A})\cdot d\mathbf{S}$$
> Rotasyonel (curl) denklemlerini → integral forma dönüştürür (Faraday, Ampere).

> [!formul] Diverjans (Gauss) Teoremi
> $$\unicode{x222F}_S \mathbf{A}\cdot d\mathbf{S} = \iiint_V (\nabla\cdot\mathbf{A})\,dv$$
> Diverjans denklemlerini → integral forma dönüştürür (Gauss yasaları).

---

## Vektörel Özdeşlikler (Ezberle!)

> [!formul] Kritik Özdeşlikler
> 1. $\nabla\cdot(\nabla\times\mathbf{A}) \equiv 0$ — Rotasyonelin diverjansı her zaman sıfır
> 2. $\nabla\times(\nabla\phi) \equiv 0$ — Skalerin gradyentinin rotasyoneli sıfır
> 3. $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$
> 4. $\nabla\cdot(\nabla\phi) = \nabla^2\phi$

| Özdeşlik | İfade |
|---------|-------|
| $\nabla\cdot(\mathbf{A}\times\mathbf{B})$ | $\mathbf{B}\cdot(\nabla\times\mathbf{A}) - \mathbf{A}\cdot(\nabla\times\mathbf{B})$ |
| $\nabla(\psi\phi)$ | $\psi\nabla\phi + \phi\nabla\psi$ |
| $\nabla\cdot(\psi\mathbf{A})$ | $\psi\nabla\cdot\mathbf{A} + \mathbf{A}\cdot\nabla\psi$ |
| $\nabla\times(\psi\mathbf{A})$ | $\psi\nabla\times\mathbf{A} + (\nabla\psi)\times\mathbf{A}$ |

---

## Silindirik ve Küresel Koordinatlarda ∇

**Silindirik $(r, \phi, z)$:**
$$\nabla\cdot\mathbf{A} = \frac{1}{r}\frac{\partial(rA_r)}{\partial r} + \frac{1}{r}\frac{\partial A_\phi}{\partial\phi} + \frac{\partial A_z}{\partial z}$$

$$\nabla^2\phi = \frac{1}{r}\frac{\partial}{\partial r}\!\left(r\frac{\partial\phi}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2\phi}{\partial\phi^2} + \frac{\partial^2\phi}{\partial z^2}$$

**Küresel $(R, \theta, \phi)$:**
$$\nabla\cdot\mathbf{A} = \frac{1}{R^2}\frac{\partial(R^2 A_R)}{\partial R} + \frac{1}{R\sin\theta}\frac{\partial(\sin\theta\, A_\theta)}{\partial\theta} + \frac{1}{R\sin\theta}\frac{\partial A_\phi}{\partial\phi}$$

---

## Özdeşliğin Kullanımı: Dalga Denklemi Türetimi

<svg width="340" height="298" viewBox="0 0 340 298" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-emd01b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <rect x="20" y="10" width="300" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="28" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">1. Maxwell curl denklemleri</text>
  <text x="170" y="44" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">∇×E = −∂B/∂t</text>
  <line x1="170" y1="52" x2="170" y2="68" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-emd01b)"/>
  <rect x="20" y="70" width="300" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="92" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">2. ∇×(∇×E) = −∂(∇×B)/∂t</text>
  <line x1="170" y1="104" x2="170" y2="120" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-emd01b)"/>
  <rect x="20" y="122" width="300" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="140" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">3. Vektör özdeşliği uygula</text>
  <text x="170" y="156" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">∇(∇·E) − ∇²E</text>
  <line x1="170" y1="164" x2="170" y2="180" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-emd01b)"/>
  <rect x="20" y="182" width="300" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="200" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">4. Kaynaksız: ∇·E = 0</text>
  <text x="170" y="216" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">→  −∇²E = −με·∂²E/∂t²</text>
  <line x1="170" y1="224" x2="170" y2="240" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-emd01b)"/>
  <rect x="20" y="242" width="300" height="44" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="260" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">5. Dalga Denklemi ✓</text>
  <text x="170" y="278" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#aac4e8">∇²E = με · ∂²E/∂t²</text>
</svg>

---

> [!sinav] Sınav İpuçları
> - Sınır koşullarını türetmek için Stokes ve Gauss teoremlerini çok ince ($\Delta h \to 0$) yüzeylere/hacme uygula
> - $\nabla\times(\nabla\times\mathbf{A})$ özdeşliği dalga denklemi türetiminin kalbidir — ezberle
> - Koordinat sistemi seçimi simetriyi kullan: küresel → nokta yük, silindirik → tel

---

**Bağlantılar:** [[02 Maxwell Denklemleri]] | [[03 Dalga Yayılması ve Düzlemsel Dalgalar]] | [[EMD Formül Sayfası]]
