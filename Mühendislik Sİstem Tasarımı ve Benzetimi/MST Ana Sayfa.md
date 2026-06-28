---
tags: [mst, hub, index, sistem-tasarımı, benzetim]
aliases: [MST, MST&B, Mühendislik Sistem Tasarımı]
---
****
# Mühendislik Sistem Tasarımı ve Benzetimi — Ana Sayfa

← [[HOME]]

## Konu Haritası

```mermaid
flowchart LR
    MST(["MST & Benzetim"])
    MST --> A["<b>Fiziksel Sistemler</b><br/>• Newton 2. Yasa, Lagrange (mekanik)<br/>• Yay-Kütle-Sönümleyici modeli<br/>• KVL / KCL (elektrik)<br/>• RLC devreleri, Op-Amp<br/>• Transfer Fonksiyonu türetimi"]
    MST --> B["<b>Durum Uzayı (State-Space)</b><br/>• ẋ = Ax + Bu, y = Cx + Du<br/>• A, B, C, D matrisleri<br/>• TF ↔ SS: G(s) = C(sI−A)⁻¹B + D"]
    MST --> C["<b>Doğrusallaştırma</b><br/>• Denge noktası (ẋ = 0) bulma<br/>• Taylor serisi (1. derece)<br/>• Jacobian matrisleri A, B"]
    MST --> D["<b>Kök Yer Eğrisi ve Kompansasyon</b><br/>• Asimptotlar: açı (180°/q), merkez σa<br/>• Breakaway noktası<br/>• PD/PI/PID, Lead/Lag kompansatörler"]
    MST --> E["<b>Faz Düzlemi Analizi</b><br/>• Faz portresi (x1−x2 düzlemi)<br/>• Özdeğer: Re(λ) &lt; 0 → kararlı"]
    style MST fill:#1a1a2e,color:#ffffff,stroke:#1a1a2e
    style A fill:#eef2f7,stroke:#1a1a2e
    style B fill:#d6e0f0,stroke:#1a1a2e
    style C fill:#eef2f7,stroke:#1a1a2e
    style D fill:#d6e0f0,stroke:#1a1a2e
    style E fill:#eef2f7,stroke:#1a1a2e
```

## Konu Anlatımları

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Mekanik Sistemler | [[Konu Anlatımları/01 Mekanik Sistemler]] |
| 2 | Elektrik Sistemleri | [[Konu Anlatımları/02 Elektrik Sistemleri]] |
| 3 | Durum Uzayı | [[Konu Anlatımları/03 Durum Uzayı]] |
| 4 | Doğrusallaştırma | [[Konu Anlatımları/04 Doğrusallaştırma]] |
| 5 | KYE ve Kompansasyon | [[Konu Anlatımları/05 Kök Yer Eğrisi ve Kompansasyon]] |
| 📄 | Formül Özeti | [[MST Formül Sayfası]] |

## Örnek Sorular

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Mekanik Sistemler Örnekleri | [[Örnek Sorular/01 Mekanik Sistemler Örnekleri]] |
| 2 | Elektrik Sistemleri Örnekleri | [[Örnek Sorular/02 Elektrik Sistemleri Örnekleri]] |
| 3 | Durum Uzayı Örnekleri | [[Örnek Sorular/03 Durum Uzayı Örnekleri]] |
| 4 | Doğrusallaştırma Örnekleri | [[Örnek Sorular/04 Doğrusallaştırma Örnekleri]] |
| 5 | Kök Yer Eğrisi Örnekleri | [[Örnek Sorular/05 Kök Yer Eğrisi Örnekleri]] |
| 6 | **Final Sınav Soruları (Çözümlü)** | [[Örnek Sorular/06 Final Sınav Soruları (Çözümlü)]] |
| 7 | Nise Ch9 Kompansatör Tasarımı | [[Örnek Sorular/07 Nise Ch9 Kompansatör Tasarımı]] |
| 8 | Vize Quizleri ve Hoca Örnekleri (Çözümlü) | [[Örnek Sorular/08 Vize Soruları ve Hoca Örnekleri]] |
| 9 | **★ Resmi Vize Sınavı (Cevap Anahtarlı)** | [[Örnek Sorular/09 Resmi Vize Sınavı (Cevap Anahtarlı)]] |

## Diğer Derslerle Bağlantı

```mermaid
flowchart LR
    MST["MST & Benzetim"]
    OK["Otomatik Kontrol"]
    SS["Sinyaller & Sistemler"]
    MST <--> OK
    MST --> SS
    style MST fill:#18B464,stroke:#1a1a2e,color:#ffffff
    style OK fill:#FFA500,stroke:#1a1a2e,color:#1a1a2e
    style SS fill:#5B9BD5,stroke:#1a1a2e,color:#ffffff
```

- **[[../Otomatik Kontrol/OK Ana Sayfa|Otomatik Kontrol]]** — KYE, kararlılık, kompansasyon ortak
- **[[../Sİnyaller ve Sistemler/SS Ana Sayfa|SS]]** — Laplace, transfer fonksiyonu temeli

## Temel Formüller (Hızlı Erişim)

**Mekanik:** $m\ddot{x} + b\dot{x} + kx = f(t) \implies G(s) = \dfrac{1}{ms^2+bs+k}$

**Elektrik (RLC seri):** $L\ddot{q} + R\dot{q} + \dfrac{q}{C} = v(t)$

**State-Space:** $\dot{x} = Ax + Bu$, $y = Cx + Du$

**SS → TF:** $G(s) = C[sI-A]^{-1}B + D$

**Doğrusallaştırma:** $\delta\dot{x} = \left.\dfrac{\partial f}{\partial x}\right|_{x_e} \delta x$
