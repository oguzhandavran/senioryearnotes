---
tags: [analog-haberleşme, hub, index, modülasyon, fourier]
aliases: [AH, Analog Haberleşme]
---

# Analog Haberleşme — Ana Sayfa

← [[HOME]]

## Konu Haritası

```mermaid
flowchart LR
    AH(["Analog Haberleşme"])
    AH --> A["<b>Spektral Analiz</b><br/>• FT: f-domain konvansiyonu, çiftler<br/>• FS: Dirichlet koşulları, cₙ katsayıları<br/>• Kare dalga → sinc spektrumu<br/>• Parseval bağıntısı<br/>• Konvolüsyon: x*h ↔ X·H"]
    AH --> B["<b>Güç ve Enerji</b><br/>• Enerji işareti: E = ∫|x|² dt &lt; ∞<br/>• Güç işareti: P = lim(1/T)∫|x|² dt<br/>• Özilişki R(τ) ve PSD ilişkisi"]
    AH --> C["<b>LTI Sistemler</b><br/>• Konvolüsyon: y(t) = x(t) * h(t)<br/>• Bozulmasız iletim: H(f) = K e^{−j2πft₀}<br/>• Süzgeçler: AGS, BGS, YGF (ideal)"]
    AH --> D["<b>Genlik Modülasyonu (AM)</b><br/>• Standart AM: [1 + m·x(t)]cos(2πfct)<br/>• DSB-SC: taşıyıcısız çift yan bant<br/>• SSB, VSB — BT = 2W (AM)"]
    style AH fill:#1a1a2e,color:#ffffff,stroke:#1a1a2e
    style A fill:#eef2f7,stroke:#1a1a2e
    style B fill:#d6e0f0,stroke:#1a1a2e
    style C fill:#eef2f7,stroke:#1a1a2e
    style D fill:#d6e0f0,stroke:#1a1a2e
```

## Konu Anlatımları

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Genel Haberleşme Sistemi | [[Konu Anlatımları/01 Genel Haberleşme Sistemi]] |
| 2 | Fourier Analizi | [[Konu Anlatımları/02 Fourier Analizi]] |
| 3 | Periyodik İşaretler ve Fourier Serisi | [[Konu Anlatımları/03 Periyodik İşaretler ve Fourier Serisi]] |
| 4 | Güç, Enerji ve LTI Sistemler | [[Konu Anlatımları/04 Güç Enerji ve LTI Sistemler]] |
| 5 | Genlik Modülasyonu | [[Konu Anlatımları/05 Genlik Modülasyonu]] |
| 📄 | Formül Özeti | [[AH Formül Sayfası]] |

## Örnek Sorular

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Fourier Analizi Örnekleri | [[Örnek Sorular/01 Fourier Analizi Örnekleri]] |
| 2 | Enerji, Güç ve LTI Örnekleri | [[Örnek Sorular/02 Enerji Güç ve LTI Örnekleri]] |
| 3 | Modülasyon Örnekleri | [[Örnek Sorular/03 Modülasyon Örnekleri]] |
| 4 | **AraSınav Soruları (Çözümlü)** | [[Örnek Sorular/04 AraSınav Soruları (Çözümlü)]] |

## Diğer Derslerle Bağlantı

```mermaid
flowchart LR
    AH["Analog Haberleşme"]
    SS["Sinyaller & Sistemler"]
    SSI["Sayısal Sinyal İşleme"]
    AH --> SS
    AH --> SSI
    style AH fill:#E05C2A,color:#ffffff,stroke:#1a1a2e
    style SS fill:#5B9BD5,color:#ffffff,stroke:#1a1a2e
    style SSI fill:#9467BD,color:#ffffff,stroke:#1a1a2e
```

- **[[../Sİnyaller ve Sistemler/SS Ana Sayfa|Sinyaller ve Sistemler]]** — Fourier, konvülüsyon, LTI temel
- **[[../Sayısal Sinyal İşleme/SSI Ana Sayfa|Sayısal Sinyal İşleme]]** — DFT, ayrık Fourier bağlantısı

## Temel Formüller (Hızlı Erişim)

**Fourier Dönüşümü (f-konvansiyonu):**
$$X(f) = \int_{-\infty}^{\infty} x(t)\,e^{-j2\pi ft}\,dt$$

**Dikdörtgen darbe:** $A\,\Pi(t/\tau) \leftrightarrow A\tau\,\text{sinc}(f\tau)$

**Standart AM:** $x_c(t) = A_c[1 + m\,x(t)]\cos(2\pi f_c t)$

**DSB-SC:** $x_{DSB}(t) = A_c\,x(t)\cos(2\pi f_c t)$

**Bant genişliği:** $B_T = 2W$
