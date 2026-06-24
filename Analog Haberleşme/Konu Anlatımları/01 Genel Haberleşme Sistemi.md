---
tags: [analog-haberleşme, haberleşme-sistemi, modülasyon, blok-diyagram, konu-anlatımı]
---

# 01 — Genel Haberleşme Sistemi

← [[../AH Ana Sayfa]] | Sonraki: [[02 Fourier Analizi]]

---

## Haberleşme Sistemi Blok Diyagramı

```mermaid
flowchart LR
    K["Kaynak\nx(t)"] --> V["Verici\nModülatör"]
    V -->|"x_c(t)"| KN["Kanal\nh(t) + n(t)"]
    KN -->|"r(t)"| A["Alıcı\nDemodülatör"]
    A --> H["Hedef\nx̂(t)"]

    style K fill:#4A90D9,color:#fff
    style V fill:#E05C2A,color:#fff
    style KN fill:#888,color:#fff
    style A fill:#E05C2A,color:#fff
    style H fill:#4A90D9,color:#fff
```

| Blok | Görev |
|------|-------|
| **Kaynak** | İletilecek bilgi — ses, görüntü, veri |
| **Verici (Modülatör)** | Mesajı taşıyıcıya bindirip iletim kanalına uygun hale getirir |
| **Kanal** | Fiziksel ortam — kablo, hava, fiber; gürültü ve parazit ekler |
| **Alıcı (Demodülatör)** | Kanaldan gelen sinyali işleyip mesajı geri çıkarır |
| **Hedef** | Alınan mesajın tüketicisi |

---

## Modülasyon Nedir?

> [!tanim] Modülasyon
> Mesaj sinyalinin $x(t)$ bilgisini yüksek frekanslı bir **taşıyıcı sinyal** üzerine bindirme işlemidir.
> $$x_c(t) = f\bigl(x(t),\; A_c\cos(2\pi f_c t)\bigr)$$

---

## Modülasyon Neden Gerekli?

> [!sinav] 3 Temel Neden — Sınavda sorulur!

**1. Uzak mesafe iletimi:**
- Düşük frekanslı ses sinyalleri (~300 Hz – 3 kHz) havada hızla söner
- Yüksek frekanslı elektromanyetik dalgalar ($f_c$ MHz – GHz) çok daha uzağa gider
- $\lambda = c/f$: frekans arttıkça dalga boyu kısalır → anten boyutu küçülür

**2. Kanal paylaşımı (Frekans Çoklama / FDM):**
- Farklı yayıncılar farklı taşıyıcı frekanslarına ($f_{c1}, f_{c2}, \ldots$) yerleşir
- Her biri $B_T$ bant genişliği kaplar → kanallar çakışmaz
- Radyo, TV, cep telefonu hepsi aynı havayı paylaşır

**3. Gürültüye karşı direnç:**
- Uygun modülasyon türü seçilerek gürültü etkisi azaltılır
- FM ve PM, AM'e göre gürültüde daha başarılıdır

---

## Temel Büyüklükler

| Sembol | İsim | Tipik değer |
|--------|------|-------------|
| $x(t)$ | Mesaj (modüle edici) işaret | Bant sınırlı: $\|f\| \leq W$ |
| $A_c$ | Taşıyıcı genliği | Sabit |
| $f_c$ | Taşıyıcı frekansı | $f_c \gg W$ |
| $W$ | Mesaj bant genişliği | Hz cinsinden |
| $B_T$ | İletim bant genişliği | $B_T = 2W$ (AM için) |

---

## Modülasyon Türleri

```mermaid
graph TD
    M["Modülasyon"] --> AM["Genlik Mod.\n(AM)"]
    M --> FM["Frekans Mod.\n(FM)"]
    M --> PM["Faz Mod.\n(PM)"]

    AM --> SAM["Standart AM\nA_c[1+mx(t)]cos(2πfct)"]
    AM --> DSB["DSB-SC\nA_c·x(t)cos(2πfct)"]
    AM --> SSB["SSB\n(Tek Yan Bant)"]
    AM --> VSB["VSB/AYB\n(Artık Yan Bant)"]
```

> [!warning] Kapsam
> Bu derste **Standart AM** ve **DSB-SC** ağırlıklı. FM/PM kapsam dışı.

---

> [!sinav] Sınav İpucu
> - Verici çıkışı: $x_c(t)$ → modüle edilmiş işaret
> - Kanal çıkışı: $r(t) = x_c(t) * h(t) + n(t)$
> - Modülasyonun amacını 3 maddede bilmek yeterli
