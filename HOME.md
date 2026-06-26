---
tags: [home, index, bütünleme]
cssclass: home
---

# Bütünleme Dönemi — Second Brain

> **Sınav haftası:** Haziran 2026 · **Hedef:** 6 dersten geçmek 💪

---

## Dersler

| Ders                                                                             | Hub                                             | Formül Sayfası                                       | Durum |
| -------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------- | ----- |
| [[Elektromanyetik Dalga Teorisi/EMD Ana Sayfa\|⚡ Elektromanyetik Dalga Teorisi]] | [[Elektromanyetik Dalga Teorisi/EMD Ana Sayfa]] | [[Elektromanyetik Dalga Teorisi/EMD Formül Sayfası]] | 🔴    |
| [[MST Ana Sayfa\|⚙️ MST & Benzetim]]                                             | [[MST Ana Sayfa]]                               | [[MST Formül Sayfası]]                               | 🔴    |
| [[Otomatik Kontrol/OK Ana Sayfa\|🎛️ Otomatik Kontrol]]                          | [[Otomatik Kontrol/OK Ana Sayfa]]               | [[Otomatik Kontrol/OK Formül Sayfası]]               | 🔴    |
| [[Sayısal Sinyal İşleme/SSI Ana Sayfa\|📡 Sayısal Sinyal İşleme]]                | [[Sayısal Sinyal İşleme/SSI Ana Sayfa]]         | [[Sayısal Sinyal İşleme/SSI Formül Sayfası]]         | 🔴    |
| [[Sİnyaller ve Sistemler/SS Ana Sayfa\|〰️ Sinyaller ve Sistemler]]               | [[Sİnyaller ve Sistemler/SS Ana Sayfa]]         | [[Sİnyaller ve Sistemler/SS Formül Sayfası]]         | 🔴    |
| [[Analog Haberleşme/AH Ana Sayfa\|📻 Analog Haberleşme]]                         | [[Analog Haberleşme/AH Ana Sayfa]]              | [[Analog Haberleşme/AH Formül Sayfası]]              | 🔴    |

---

## Konular Arası Bağlantılar

```mermaid
flowchart LR
    SS["Sinyaller & Sistemler (Temel)"]
    SSI["Sayısal Sinyal İşleme"]
    OK["Otomatik Kontrol"]
    MST["MST & Benzetim"]
    AH["Analog Haberleşme"]
    EMD["EM Dalga Teorisi<br/><i>(bağımsız ders)</i>"]
    SS --> SSI
    SS --> OK
    SS --> MST
    SS --> AH
    OK <--> MST
    style SS fill:#5B9BD5,color:#ffffff,stroke:#1a1a2e
    style SSI fill:#9467BD,color:#ffffff,stroke:#1a1a2e
    style OK fill:#FFA500,color:#1a1a2e,stroke:#1a1a2e
    style MST fill:#18B464,color:#ffffff,stroke:#1a1a2e
    style AH fill:#E05C2A,color:#ffffff,stroke:#1a1a2e
    style EMD fill:#DC503C,color:#ffffff,stroke:#1a1a2e
```

---

## Ortak Matematik Araçları

```mermaid
flowchart LR
    M(["Matematik"])
    M --> A["<b>Laplace Dönüşümü</b><br/>• Transfer Fonksiyonu H(s) = Y(s)/X(s)<br/>• Kutup-Sıfır analizi<br/>• Kısmi Kesir Açılımı (PFD)"]
    M --> B["<b>Fourier Analizi</b><br/>• Frekans analizi, spektrum<br/>• DFT / FFT (ayrık)<br/>• Filtre tasarımı (frekans domeni)"]
    M --> C["<b>Diferansiyel Denklemler</b><br/>• ODE (yüksek dereceli)<br/>• Durum Uzayı: ẋ = Ax + Bu<br/>• Maxwell denklemleri (PDE)"]
    M --> D["<b>Z-Dönüşümü</b><br/>• Ayrık sistemler (dijital filtreler)<br/>• IIR / FIR filtre yapıları"]
    style M fill:#1a1a2e,color:#ffffff,stroke:#1a1a2e
    style A fill:#eef2f7,stroke:#1a1a2e
    style B fill:#d6e0f0,stroke:#1a1a2e
    style C fill:#eef2f7,stroke:#1a1a2e
    style D fill:#d6e0f0,stroke:#1a1a2e
```

---

## Hızlı Bağlantılar

- [[00 Sınav Takvimi ve Strateji]] — Sınav planı ve strateji
- [[00 Dış Kaynaklar ve MSÜ Rehberi]] — MSÜ UZEM, JAST dergi, açık erişim PDF'ler
- [[_templates/Ders Notu Template]] — Yeni not şablonu

---

> **Grafik Görünümü:** `Ctrl+G` ile açıp her dersin renk grubunu görebilirsin.
> **Arama:** `Ctrl+Shift+F` ile tüm vault'ta arama yapabilirsin.
