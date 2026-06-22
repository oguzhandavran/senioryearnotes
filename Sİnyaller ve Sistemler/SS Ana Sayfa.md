---
tags: [ss, sinyaller-sistemler, hub]
aliases: [SS, Sinyaller ve Sistemler]
---

# 〰️ Sinyaller ve Sistemler — Ana Sayfa

← [[HOME]]

## Hızlı Özet

> Sinyaller & Sistemler: zamanın fonksiyonu olan işaretlerin matematiksel analizi. Temel araç: **Fourier** ve **Laplace** dönüşümleri.

---

## Konu Haritası

```mermaid
mindmap
  root((Sinyaller ve Sistemler))
    Sinyal Sınıflandırması
      CT x(t) / DT x[n]
      Enerji / Güç
      Periyodik / Aperiodik
      Çift / Tek
      Temel Sinyaller δ u ramp
    LTI Sistemler
      Doğrusallik
      Zamanla Değişmezlik
      Nedensellik
      Kararlılık
      Konvolüsyon
    Fourier Serisi
      CTFS katsayıları
      DTFS katsayıları
      Parseval
    Fourier Dönüşümü
      CTFT
      DTFT
      Özellikler
    Laplace Dönüşümü
      ROC
      PFD
      Transfer Fonksiyonu
```

---

## Konular

| # | Konu | Bağlantı | Öncelik |
|---|------|----------|---------|
| 1 | Sinyal Sınıflandırması | [[01 Sinyal Sınıflandırması]] | 🔴 |
| 2 | LTI Sistemler & Konvolüsyon | [[02 LTI Sistemler ve Konvolüsyon]] | 🔴 |
| 3 | Fourier Serisi | [[03 Fourier Serisi]] | 🟡 |
| 4 | Fourier Dönüşümü | [[04 Fourier Dönüşümü]] | 🔴 |
| 5 | Laplace Dönüşümü | [[05 Laplace Dönüşümü]] | 🔴 |
| — | Formül Sayfası | [[SS Formül Sayfası]] | ⭐ |

---

## Diğer Derslerle Bağlantı

```mermaid
graph LR
    SS["SS: Sinyaller & Sistemler"] -->|"Ayrıklaştırma → x[n]"| SSI["📡 Sayısal Sinyal İşleme"]
    SS -->|"Laplace → Transfer Fonksiyonu"| OK["🎛️ Otomatik Kontrol"]
    SS -->|"Durum Uzayı → ODE"| MST["⚙️ MST&B"]
    
    style SS fill:#5B9BD5,color:#fff
    style SSI fill:#9467BD,color:#fff
    style OK fill:#FFA500,color:#000
    style MST fill:#18B464,color:#fff
```

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
