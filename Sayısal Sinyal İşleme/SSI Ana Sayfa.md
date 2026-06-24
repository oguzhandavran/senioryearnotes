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

<svg width="500" height="432" viewBox="0 0 500 432" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="100" height="412" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text transform="translate(60,216) rotate(-90)" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">Sayısal Sinyal İşleme</text>
  <line x1="110" y1="57" x2="110" y2="387" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="10" width="370" height="84" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="30" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Ayrık Zaman Sinyalleri</text>
  <text x="140" y="48" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• x[n] gösterimi, temel diziler</text>
  <text x="140" y="66" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Örnekleme teoremi: fs &gt; 2fmax</text>
  <text x="140" y="84" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Nyquist frekansı, Aliasing (takma ad)</text>
  <line x1="110" y1="57" x2="120" y2="57" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="102" width="370" height="84" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="122" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Z-Dönüşümü</text>
  <text x="140" y="140" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• X(z) = Σ x[n] z^{−n}</text>
  <text x="140" y="158" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• ROC, ters Z (PFD)</text>
  <text x="140" y="176" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Kutup-Sıfır analizi, H(z) = Y(z)/X(z)</text>
  <line x1="110" y1="144" x2="120" y2="144" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="194" width="370" height="84" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="214" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">DFT ve FFT</text>
  <text x="140" y="232" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• N-noktalı DFT: X[k] = Σx[n]W_N^{nk}</text>
  <text x="140" y="250" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Döngüsel konvolüsyon ↔ DFT çarpımı</text>
  <text x="140" y="268" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• FFT butterfly: N/2 alt-DFT'ler</text>
  <line x1="110" y1="236" x2="120" y2="236" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="286" width="370" height="84" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="306" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Sayısal Filtre Tasarımı</text>
  <text x="140" y="324" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• FIR (sonlu) vs IIR (sonsuz dürtü yanıtı)</text>
  <text x="140" y="342" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• FIR: pencere metodu (Hamming, Blackman)</text>
  <text x="140" y="360" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• IIR: Bilineer dönüşüm (s → z prewarping)</text>
  <line x1="110" y1="387" x2="120" y2="387" stroke="#1a1a2e" stroke-width="1.5"/>
</svg>

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

<svg width="460" height="176" viewBox="0 0 460 176" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ssi-grl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <rect x="10" y="10" width="175" height="34" rx="2" fill="#5B9BD5" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="97" y="32" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">SS: Fourier Dönüşümü</text>
  <rect x="10" y="71" width="175" height="34" rx="2" fill="#5B9BD5" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="97" y="93" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">SS: Laplace</text>
  <rect x="10" y="132" width="175" height="34" rx="2" fill="#5B9BD5" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="97" y="154" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">SS: Konvolüsyon</text>
  <rect x="275" y="10" width="175" height="34" rx="2" fill="#9467BD" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="362" y="32" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">DSP: DTFT / DFT</text>
  <rect x="275" y="71" width="175" height="34" rx="2" fill="#9467BD" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="362" y="93" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">Z-Dönüşümü</text>
  <rect x="275" y="132" width="175" height="34" rx="2" fill="#9467BD" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="362" y="154" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">DFT Konvolüsyon</text>
  <line x1="185" y1="27" x2="275" y2="27" stroke="#1a1a2e" stroke-width="1.4" marker-end="url(#arr-ssi-grl)"/>
  <text x="230" y="22" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">Örnekleme → DTFT</text>
  <line x1="185" y1="88" x2="275" y2="88" stroke="#1a1a2e" stroke-width="1.4" marker-end="url(#arr-ssi-grl)"/>
  <text x="230" y="83" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">z = e^{sT}</text>
  <line x1="185" y1="149" x2="275" y2="149" stroke="#1a1a2e" stroke-width="1.4" marker-end="url(#arr-ssi-grl)"/>
  <text x="230" y="144" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">Döngüsel → DFT</text>
</svg>

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
