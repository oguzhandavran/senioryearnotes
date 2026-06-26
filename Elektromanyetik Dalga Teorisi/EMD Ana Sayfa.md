---
tags: [emd, bütünleme, hub]
aliases: [EMD, Elektromanyetik]
---

# ⚡ Elektromanyetik Dalga Teorisi — Ana Sayfa

← [[HOME]]

> **Özet:** Maxwell denklemleri → dalga denklemi → düzlemsel dalgalar → yansıma/kırılma → iletim hatları

---

## Konu Haritası

```mermaid
flowchart LR
    EMD(["EMD"])
    EMD --> A["<b>Vektör Analizi</b><br/>• Gradient ∇φ, Divergence ∇·A, Curl ∇×A<br/>• Stokes: ∮E·dl = ∫(∇×E)·dS<br/>• Gauss: ∮D·dS = ∫ρ dV"]
    EMD --> B["<b>Maxwell Denklemleri</b><br/>• Faraday: ∇×E = −∂B/∂t<br/>• Ampere-Maxwell: ∇×H = J + ∂D/∂t<br/>• Gauss: ∇·D = ρ, ∇·B = 0<br/>• Sınır koşulları (süreklilik)<br/>• D=εE, B=μH, J=σE"]
    EMD --> C["<b>Dalga Yayılması</b><br/>• Dalga denklemi: ∇²E = με ∂²E/∂t²<br/>• Helmholtz: ∇²Es + k²Es = 0<br/>• up = 1/√με, ug = 1/(dβ/dω)<br/>• Poynting: Sav = ½ Re[E × H*]"]
    EMD --> D["<b>Düzlemsel Dalgalar</b><br/>• Kayıpsız: E = E₀e^{−jkz}, η = √μ/ε<br/>• Kayıplı: γ = α + jβ, δ = 1/α<br/>• Polarizasyon (doğrusal, dairesel)"]
    EMD --> E["<b>Yansıma & Kırılma</b><br/>• Normal: Γ = (η₂−η₁)/(η₂+η₁)<br/>• Snell: n₁ sin θᵢ = n₂ sin θₜ<br/>• Fresnel katsayıları (TE/TM)<br/>• Brewster ve kritik açı"]
    EMD --> F["<b>İletim Hatları</b><br/>• Telegraf denk., Z₀ = √(L'/C')<br/>• ΓL = (ZL−Z₀)/(ZL+Z₀), SWR<br/>• Smith çizimi, Zin formülü"]
    style EMD fill:#1a1a2e,color:#ffffff,stroke:#1a1a2e
    style A fill:#eef2f7,stroke:#1a1a2e
    style B fill:#d6e0f0,stroke:#1a1a2e
    style C fill:#eef2f7,stroke:#1a1a2e
    style D fill:#d6e0f0,stroke:#1a1a2e
    style E fill:#eef2f7,stroke:#1a1a2e
    style F fill:#d6e0f0,stroke:#1a1a2e
```

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
