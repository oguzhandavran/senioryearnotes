---
tags: [ss, sinyaller-sistemler, hub]
aliases: [SS, Sinyaller ve Sistemler]
---

# 〰️ Sinyaller ve Sistemler — Ana Sayfa

← [[HOME]]

## Hızlı Özet

> Sinyaller & Sistemler: zamanın fonksiyonu olan işaretlerin matematiksel analizi. Temel araç: **Fourier** ve **Laplace** dönüşümleri.

---

## Sınav Kapsamı (Bütünleme)

> [!warning] Kapsam — Oppenheim kitabı bölüm bazlı
> - **Bölüm 1** — Tamamı (Sinyaller ve Sistemler)
> - **Bölüm 2** — 2.5 (Tekillik Fonksiyonları) **hariç**
> - **Bölüm 3** — **3.6'ya kadar** dahil (3.7+ yok)
> - **Bölüm 4** — **4.5'e kadar** dahil (Çarpma Özelliği) (4.6+ yok)
> - **Laplace yok · DTFT (Bölüm 5) yok · Z-dönüşümü yok**

---

## Konu Haritası

<svg width="500" height="546" viewBox="0 0 500 546" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="100" height="526" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text transform="translate(60,273) rotate(-90)" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">Sinyaller ve Sistemler</text>
  <line x1="110" y1="61" x2="110" y2="503" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="10" width="370" height="102" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="30" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Sinyal Sınıflandırması</text>
  <text x="140" y="48" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• CT x(t) / DT x[n] (sürekli / ayrık)</text>
  <text x="140" y="66" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Enerji (E&lt;∞) / Güç (0&lt;P&lt;∞)</text>
  <text x="140" y="84" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Periyodik / Aperiodik, Çift / Tek</text>
  <text x="140" y="102" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Temel sinyaller: δ(t), u(t), r(t)</text>
  <line x1="110" y1="61" x2="120" y2="61" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="120" width="370" height="102" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="140" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">LTI Sistemler</text>
  <text x="140" y="158" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Doğrusallik (superposition)</text>
  <text x="140" y="176" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Zamanla Değişmezlik (TI)</text>
  <text x="140" y="194" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Nedensellik, Kararlılık (BIBO)</text>
  <text x="140" y="212" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Konvolüsyon: y(t) = x(t) * h(t)</text>
  <line x1="110" y1="171" x2="120" y2="171" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="230" width="370" height="84" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="250" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Fourier Serisi</text>
  <text x="140" y="268" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• CTFS: cₙ = (1/T)∫x(t)e^{−jnω₀t}dt</text>
  <text x="140" y="286" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• DTFS katsayıları, Parseval bağıntısı</text>
  <text x="140" y="304" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Periyodik → darbe serisi spektrumu</text>
  <line x1="110" y1="272" x2="120" y2="272" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="322" width="370" height="84" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="342" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Fourier Dönüşümü (CTFT)</text>
  <text x="140" y="360" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• X(f) = ∫x(t)e^{−j2πft}dt</text>
  <text x="140" y="378" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• DTFT: X(e^{jω}) = Σx[n]e^{−jωn}</text>
  <text x="140" y="396" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Özellikler: kaydırma, ölçekleme, modülasyon</text>
  <line x1="110" y1="364" x2="120" y2="364" stroke="#1a1a2e" stroke-width="1.5"/>
  <rect x="120" y="414" width="370" height="84" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="130" y="434" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Laplace Dönüşümü</text>
  <text x="140" y="452" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• ROC (yakınsama bölgesi)</text>
  <text x="140" y="470" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• PFD ile ters Laplace</text>
  <text x="140" y="488" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">• Transfer Fonksiyonu H(s) = Y(s)/X(s)</text>
  <line x1="110" y1="503" x2="120" y2="503" stroke="#1a1a2e" stroke-width="1.5"/>
</svg>

---

## Konular

### Konu Anlatımları

| # | Konu | Bağlantı | Öncelik | Kapsam |
|---|------|----------|---------|--------|
| 1 | Sinyal Sınıflandırması | [[Konu Anlatımları/01 Sinyal Sınıflandırması]] | 🔴 | Tam |
| 2 | LTI Sistemler & Konvolüsyon | [[Konu Anlatımları/02 LTI Sistemler ve Konvolüsyon]] | 🔴 | 2.5 hariç |
| 3 | Fourier Serisi | [[Konu Anlatımları/03 Fourier Serisi]] | 🔴 | 3.6'ya kadar |
| 4 | Fourier Dönüşümü (CTFT) | [[Konu Anlatımları/04 Fourier Dönüşümü]] | 🔴 | 4.5'e kadar |
| ~~5~~ | ~~Laplace Dönüşümü~~ | — | ~~—~~ | **Kapsam dışı** |

### Örnek Sorular

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Sinyal Örnekleri | [[Örnek Sorular/01 Sinyal Örnekleri]] |
| 2 | LTI & Konvolüsyon Örnekleri | [[Örnek Sorular/02 LTI Örnekleri]] |
| 3 | Fourier Serisi Örnekleri | [[Örnek Sorular/03 Fourier Serisi Örnekleri]] |
| 4 | Fourier Dönüşümü Örnekleri | [[Örnek Sorular/04 Fourier Dönüşümü Örnekleri]] |
| 5 | **Vize Sınav Soruları (Çözümlü)** | [[Örnek Sorular/05 Vize Sınav Soruları (Çözümlü)]] |
| 6 | **Final Sınav Soruları (Çözümlü)** | [[Örnek Sorular/06 Final Sınav Soruları (Çözümlü)]] |

### Diğer

| Dosya | Bağlantı |
|-------|----------|
| Formül Sayfası | [[SS Formül Sayfası]] |
| Sınav Gecesi Özeti | [[SS Sınav Gecesi]] |

---

## Diğer Derslerle Bağlantı

<svg width="460" height="170" viewBox="0 0 460 170" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ss-grl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <rect x="10" y="68" width="155" height="34" rx="2" fill="#5B9BD5" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="87" y="90" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">Sinyaller &amp; Sistemler</text>
  <rect x="295" y="10" width="155" height="34" rx="2" fill="#9467BD" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="372" y="32" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">Sayısal Sinyal İşl.</text>
  <rect x="295" y="68" width="155" height="34" rx="2" fill="#FFA500" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="372" y="90" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e">Otomatik Kontrol</text>
  <rect x="295" y="126" width="155" height="34" rx="2" fill="#18B464" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="372" y="148" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">MST &amp; Benzetim</text>
  <line x1="165" y1="78" x2="295" y2="34" stroke="#1a1a2e" stroke-width="1.4" marker-end="url(#arr-ss-grl)"/>
  <text x="228" y="50" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e" font-style="italic">Ayrıklaştırma → x[n]</text>
  <line x1="165" y1="85" x2="295" y2="85" stroke="#1a1a2e" stroke-width="1.4" marker-end="url(#arr-ss-grl)"/>
  <text x="228" y="80" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e" font-style="italic">Laplace → TF</text>
  <line x1="165" y1="95" x2="295" y2="136" stroke="#1a1a2e" stroke-width="1.4" marker-end="url(#arr-ss-grl)"/>
  <text x="228" y="128" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e" font-style="italic">Durum Uzayı → ODE</text>
</svg>

---

## Sınav Kontrol Listesi

- [ ] Sinyal enerji/güç hesabı yapabiliyorum
- [ ] CT/DT konvolüsyon hesaplayabiliyorum
- [ ] Fourier serisi katsayılarını bulabiliyorum
- [ ] CTFT/DTFT çiftlerini biliyorum
- [ ] Laplace ile transfer fonksiyonu çıkarabiliyorum
- [ ] PFD (kısmi kesirler) yapabiliyorum
- [ ] ROC belirleyebiliyorum

---

## Kaynaklar

| Kaynak | Açıklama | Erişim |
|--------|----------|--------|
| **Dr. Cahit Karakuş (2018)** | CT/DT sinyal, enerji/güç, Fourier, Laplace, Z, MATLAB örnekleri — 240 sayfa | `DATASET/Sinyaller Ve Sistemler/Dr_Cahit_Karakus_SinyallerSistemler_2018.pdf` |
| Oppenheim 2nd Ed. | Klasik İngilizce ders kitabı | `DATASET/Sinyaller Ve Sistemler/Signals_and_Systems_2nd_Edition_by_Oppen.pdf` |
| Ders Notu (taranmış) | Türkçe ders notu | `DATASET/Sinyaller Ve Sistemler/SinyallerveSistemlerDersNotu.pdf` |
| Cevap Anahtarı 2026 | Sınav soruları + çözümler | `DATASET/Sinyaller Ve Sistemler/sinyaller ve sistemler cevap anahtarı_260613_195039.pdf` |
| Ankara Üni. DSP Açık Ders | 14 haftalık Türkçe kurs | [acikders.ankara.edu.tr](https://acikders.ankara.edu.tr/course/view.php?id=837) |

> **Dr. Karakuş notundaki önemli bölümler:**
> - Bölüm 1.1: Periyodik sinyaller → `T1/T2` rasyonel sayı testi
> - Bölüm 1.2: Enerji/Güç sinyalleri → E∞ ve P∞ formülleri + 7 alıştırma
> - Bölüm 3: Fourier transform (MATLAB uygulamalı)
> - Bölüm 4: Laplace transform (özellikler + diferansiyel denklem çözümü)
> - Bölüm 5: Z-dönüşümü (ters Z-dönüşüm dahil)
> - Bölüm 7: Konvolüsyon

[[../Sayısal Sinyal İşleme/SSI Ana Sayfa|SSİ ← bağlantılı ders]] · [[../00 Dış Kaynaklar ve MSÜ Rehberi|Tüm Dış Kaynaklar]]
