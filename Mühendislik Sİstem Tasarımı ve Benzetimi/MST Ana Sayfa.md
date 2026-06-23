---
tags: [mst, hub, index, sistem-tasarımı, benzetim]
aliases: [MST, MST&B, Mühendislik Sistem Tasarımı]
---
****
# Mühendislik Sistem Tasarımı ve Benzetimi — Ana Sayfa

← [[HOME]]

## Konu Haritası

```mermaid
mindmap
  root((MST & Benzetim))
    Fiziksel Sistemler
      Mekanik Sistemler
        Newton 2. Yasa
        Lagrange
        Yay-Kütle-Sönümleyici
      Elektrik Sistemleri
        KVL / KCL
        RLC Devreleri
        Op-Amp
    Durum Uzayı
      State-Space Gösterimi
      A B C D Matrisleri
      TF ↔ SS Dönüşümü
    Doğrusallaştırma
      Denge Noktası
      Taylor Serisi
      Jacobian
    Kök Yer Eğrisi
      Asimptotlar
      Breakaway
      Kompansatörler
    Faz Düzlemi
      Faz Portresi
      Özdeğer Analizi
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

## Diğer Derslerle Bağlantı

```mermaid
graph LR
    MST["⚙️ MST & Benzetim"] <--> OK["🎛️ Otomatik Kontrol"]
    MST --> SS["〰️ Sinyaller & Sistemler"]
    style MST fill:#18B464,color:#fff
    style OK fill:#FFA500,color:#000
    style SS fill:#5B9BD5,color:#fff
```

- **[[../Otomatik Kontrol/OK Ana Sayfa|Otomatik Kontrol]]** — KYE, kararlılık, kompansasyon ortak
- **[[../Sİnyaller ve Sistemler/SS Ana Sayfa|SS]]** — Laplace, transfer fonksiyonu temeli

## Temel Formüller (Hızlı Erişim)

**Mekanik:** $m\ddot{x} + b\dot{x} + kx = f(t) \implies G(s) = \dfrac{1}{ms^2+bs+k}$

**Elektrik (RLC seri):** $L\ddot{q} + R\dot{q} + \dfrac{q}{C} = v(t)$

**State-Space:** $\dot{x} = Ax + Bu$, $y = Cx + Du$

**SS → TF:** $G(s) = C[sI-A]^{-1}B + D$

**Doğrusallaştırma:** $\delta\dot{x} = \left.\dfrac{\partial f}{\partial x}\right|_{x_e} \delta x$
