---
tags: [emd, bütünleme, hub]
aliases: [EMD, Elektromanyetik]
---

# ⚡ Elektromanyetik Dalga Teorisi — Ana Sayfa

← [[HOME]]

> **Özet:** Maxwell denklemleri → dalga denklemi → düzlemsel dalgalar → yansıma/kırılma → iletim hatları

---

## Konu Haritası

<svg width="500" height="650" viewBox="0 0 500 650" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="100" height="630" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text transform="translate(60,325) rotate(-90)" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-weight="bold" fill="white">EMD</text>
  <line x1="110" y1="47" x2="110" y2="607" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="10" width="370" height="84" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="30" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Vektör Analizi</text>
  <text x="140" y="48" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Gradient ∇φ, Divergence ∇·A, Curl ∇×A</text>
  <text x="140" y="66" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Stokes teoremi: ∮E·dl = ∫(∇×E)·dS</text>
  <text x="140" y="84" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Gauss teoremi: ∮D·dS = ∫ρ dV</text>
  <line x1="110" y1="47" x2="120" y2="47" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="102" width="370" height="120" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="122" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Maxwell Denklemleri</text>
  <text x="140" y="140" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Faraday: ∇×E = −∂B/∂t</text>
  <text x="140" y="158" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Ampere-Maxwell: ∇×H = J + ∂D/∂t</text>
  <text x="140" y="176" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Gauss (E): ∇·D = ρ  |  Gauss (B): ∇·B = 0</text>
  <text x="140" y="194" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Sınır koşulları (tanjansiyel/normal süreklilik)</text>
  <text x="140" y="212" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Ortam denklemleri: D=εE, B=μH, J=σE</text>
  <line x1="110" y1="162" x2="120" y2="162" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="230" width="370" height="102" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="250" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Dalga Yayılması</text>
  <text x="140" y="268" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Dalga denklemi: ∇²E = με ∂²E/∂t²</text>
  <text x="140" y="286" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Helmholtz: ∇²Es + k²Es = 0</text>
  <text x="140" y="304" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Faz hızı up = 1/√με, grup hızı ug = 1/(dβ/dω)</text>
  <text x="140" y="322" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Poynting: Sav = ½ Re[E × H*]</text>
  <line x1="110" y1="281" x2="120" y2="281" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="340" width="370" height="84" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="360" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Düzlemsel Dalgalar</text>
  <text x="140" y="378" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Kayıpsız: E = E₀e^{−jkz}, η = √μ/ε</text>
  <text x="140" y="396" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Kayıplı: γ = α + jβ, deri kalınlığı δ = 1/α</text>
  <text x="140" y="414" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Polarizasyon (doğrusal, dairesel)</text>
  <line x1="110" y1="382" x2="120" y2="382" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="432" width="370" height="102" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="452" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Yansıma &amp; Kırılma</text>
  <text x="140" y="470" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Normal gelme: Γ = (η₂−η₁)/(η₂+η₁)</text>
  <text x="140" y="488" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Snell: n₁ sin θᵢ = n₂ sin θₜ</text>
  <text x="140" y="506" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Fresnel katsayıları (TE/TM)</text>
  <text x="140" y="524" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Brewster açısı (TM) ve kritik açı</text>
  <line x1="110" y1="483" x2="120" y2="483" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="542" width="370" height="84" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="562" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">İletim Hatları</text>
  <text x="140" y="580" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Telegraf denklemleri, Z₀ = √L'/C'</text>
  <text x="140" y="598" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• ΓL = (ZL−Z₀)/(ZL+Z₀), SWR</text>
  <text x="140" y="616" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Smith çizimi, Zin formülü</text>
  <line x1="110" y1="607" x2="120" y2="607" stroke="#1a1a2e" stroke-width="1.5"/>
</svg>

---

## Konu Anlatımları

| # | Not | İçerik |
|---|-----|--------|
| 01 | [[Konu Anlatımları/01 Vektör Analizi ve del Operatörü]] | ∇, curl, div, Stokes, koordinatlar |
| 02 | [[Konu Anlatımları/02 Maxwell Denklemleri]] | 4 denklem + sınır koşulları |
| 03 | [[Konu Anlatımları/03 Dalga Yayılması ve Düzlemsel Dalgalar]] | Dalga denklemi, Helmholtz, Poynting |
| 04 | [[Konu Anlatımları/04 Yansıma ve Sınır Koşulları]] | Fresnel, Snell, Brewster |
| 05 | [[Konu Anlatımları/05 İletim Hatları]] | Telegraf, empedans, duran dalga |
| FS | [[EMD Formül Sayfası]] | Tüm formüller özet |

## Örnek Sorular

| # | Not | İçerik |
|---|-----|--------|
| 01 | [[Örnek Sorular/01 Vektör Analizi Örnekleri]] | Hacim integrali, çizgi integrali, Stokes |
| 02 | [[Örnek Sorular/02 Maxwell Örnekleri]] | Deplasman akımı, Faraday, süreklilik |
| 03 | [[Örnek Sorular/03 Dalga Yayılması Örnekleri]] | Düzlemsel dalga, kayıp tanjantı |
| 04 | [[Örnek Sorular/04 Yansıma ve Sınır Koşulları Örnekleri]] | Dalga denklemi (silindirik), sınır koşulları |
| 05 | [[Örnek Sorular/05 İletim Hatları Örnekleri]] | Kapasitans, elektrostatik sınır örnekleri |

---

## Kritik Formüller (Özet)

### Maxwell (Diferansiyel)
$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}, \quad \nabla\times\mathbf{H} = \mathbf{J}+\frac{\partial\mathbf{D}}{\partial t}$$
$$\nabla\cdot\mathbf{D}=\rho, \quad \nabla\cdot\mathbf{B}=0$$

### Dalga Denklemi (Kaynaksız)
$$\nabla^2\mathbf{E} - \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2}=0$$

### Poynting
$$\mathbf{S}=\mathbf{E}\times\mathbf{H}, \quad P_{av}=\frac{1}{2}\text{Re}[\mathbf{E}\times\mathbf{H}^*]$$

---

> [!sinav] Sınav Stratejisi
> 1. Maxwell denklemlerini diferansiyel + integral formda yaz
> 2. Sınır koşulları tablosunu ezberle
> 3. Düzlemsel dalga çözümünü türet
> 4. Fresnel katsayılarını uygula
