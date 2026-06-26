---
tags: [ssi, dsp, sayısal-sinyal-işleme, hub]
aliases: [SSI, SSİ, DSP, Sayısal Sinyal İşleme]
---

# 📡 Sayısal Sinyal İşleme — Ana Sayfa

← [[HOME]]

## Hızlı Özet

> DSP: ayrık zamanlı sinyallerin sayısal işlenmesi. Temel araç: **Z-dönüşümü** (Laplace'ın ayrık versiyonu) ve **DFT/FFT**.

---

## Konu Haritası

```mermaid
flowchart LR
    SSI(["Sayısal Sinyal İşleme"])
    SSI --> A["<b>Ayrık Zaman Sinyalleri</b><br/>• x[n] gösterimi, temel diziler<br/>• Örnekleme teoremi: fs &gt; 2fmax<br/>• Nyquist frekansı, Aliasing (takma ad)"]
    SSI --> B["<b>Z-Dönüşümü</b><br/>• X(z) = Σ x[n] z^{−n}<br/>• ROC, ters Z (PFD)<br/>• Kutup-Sıfır, H(z) = Y(z)/X(z)"]
    SSI --> C["<b>DFT ve FFT</b><br/>• N-noktalı DFT: X[k] = Σx[n]W_N^{nk}<br/>• Döngüsel konvolüsyon ↔ DFT çarpımı<br/>• FFT butterfly: N/2 alt-DFT'ler"]
    SSI --> D["<b>Sayısal Filtre Tasarımı</b><br/>• FIR (sonlu) vs IIR (sonsuz dürtü yanıtı)<br/>• FIR: pencere metodu (Hamming, Blackman)<br/>• IIR: Bilineer dönüşüm (s → z prewarping)"]
    style SSI fill:#1a1a2e,color:#ffffff,stroke:#1a1a2e
    style A fill:#eef2f7,stroke:#1a1a2e
    style B fill:#d6e0f0,stroke:#1a1a2e
    style C fill:#eef2f7,stroke:#1a1a2e
    style D fill:#d6e0f0,stroke:#1a1a2e
```

---

## Konu Anlatımları

| # | Konu | Bağlantı | Öncelik |
|---|------|----------|---------|
| 1 | Ayrık Zaman Sinyalleri & Örnekleme | [[Konu Anlatımları/01 Ayrık Zaman Sinyalleri ve Örnekleme]] | 🔴 |
| 2 | Z-Dönüşümü | [[Konu Anlatımları/02 Z-Dönüşümü]] | 🔴 |
| 3 | DFT ve FFT | [[Konu Anlatımları/03 DFT ve FFT]] | 🔴 |
| 4 | Sayısal Filtre Tasarımı | [[Konu Anlatımları/04 Sayısal Filtre Tasarımı]] | 🟡 |
| — | Formül Sayfası | [[SSI Formül Sayfası]] | ⭐ |

## Örnek Sorular

| # | Konu | Bağlantı | Öncelik |
|---|------|----------|---------|
| 1 | Örnekleme Örnekleri | [[Örnek Sorular/01 Örnekleme Örnekleri]] | 🔴 |
| 2 | Z-Dönüşümü Örnekleri | [[Örnek Sorular/02 Z-Dönüşümü Örnekleri]] | 🔴 |
| 3 | DFT-FFT Örnekleri | [[Örnek Sorular/03 DFT-FFT Örnekleri]] | 🔴 |
| 4 | Filtre Tasarımı Örnekleri | [[Örnek Sorular/04 Filtre Tasarımı Örnekleri]] | 🟡 |

---

## SS ile Bağlantı

```mermaid
flowchart LR
    F["SS: Fourier Dönüşümü"] -->|"Örnekleme → DTFT"| DTFT["DSP: DTFT / DFT"]
    L["SS: Laplace"] -->|"z = e^{sT}"| Z["Z-Dönüşümü"]
    K["SS: Konvolüsyon"] -->|"Döngüsel → DFT"| DK["DFT Konvolüsyon"]
    style F fill:#5B9BD5,color:#ffffff,stroke:#1a1a2e
    style L fill:#5B9BD5,color:#ffffff,stroke:#1a1a2e
    style K fill:#5B9BD5,color:#ffffff,stroke:#1a1a2e
    style DTFT fill:#9467BD,color:#ffffff,stroke:#1a1a2e
    style Z fill:#9467BD,color:#ffffff,stroke:#1a1a2e
    style DK fill:#9467BD,color:#ffffff,stroke:#1a1a2e
```

---

## Kaynaklar

- `DATASET/Sayısal Sinyal İşleme/Ecmel_notlar.pdf` — Temel sistem özellikleri + konvolüsyon + DTFT + Fourier Serisi
- `DATASET/Sayısal Sinyal İşleme/Sayısal Sinyal İşleme (DSP) Sınavı - Yazdırılabilir Sıkışık Formül Kartı.pdf`
- `DATASET/Sayısal Sinyal İşleme/sayisal_sinyal_isleme_ara_sinav.pdf` — Ara sınav soruları
- `DATASET/Sayısal Sinyal İşleme/Sinyal_Isleme_Bolum1_Matematiksel_Rapor.pdf`

## Sınav Kontrol Listesi

- [ ] Sistem özelliklerini (hafıza, nedensellik, doğrusal, ZD, kararlı) test edebiliyorum
- [ ] DT konvolüsyonu hesaplayabiliyorum
- [ ] DTFT çiftlerini ve ters DTFT'yi (PFD ile) yapabiliyorum
- [ ] Z-dönüşümü ve ters Z (PFD) yapabiliyorum
- [ ] DFT formülünü ve döngüsel konvolüsyonu yapabiliyorum
- [ ] Dikdörtgen pencere frekans yanıtını biliyorum
