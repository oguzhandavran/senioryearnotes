---
tags: [analog-haberleşme, haberleşme-sistemi, modülasyon, blok-diyagram, konu-anlatımı]
---

# 01 — Genel Haberleşme Sistemi

← [[../AH Ana Sayfa]] | Sonraki: [[02 Fourier Analizi]]

---

## Haberleşme Sistemi Blok Diyagramı

```mermaid
flowchart LR
    K["Kaynak<br/><i>x(t)</i>"] --> V["Verici<br/>(Modülatör)"]
    V -->|"x_c(t)"| C["Kanal<br/><i>h(t) + n(t)</i><br/>(gürültü)"]
    C -->|"r(t)"| A["Alıcı<br/>(Demodülatör)"]
    A --> H["Hedef<br/><i>x̂(t)</i>"]
    style K fill:#d6e0f0,stroke:#1a1a2e
    style H fill:#d6e0f0,stroke:#1a1a2e
    style V fill:#eef2f7,stroke:#1a1a2e
    style C fill:#eef2f7,stroke:#1a1a2e,stroke-dasharray:5 3
    style A fill:#eef2f7,stroke:#1a1a2e
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
flowchart TD
    M["Modülasyon"]
    M --> AM["Genlik Mod. (AM)"]
    M --> FM["Frekans Mod. (FM/PM)<br/><i>s_FM = A_c cos(2πf_c t + 2πk_f ∫x dτ)</i>"]
    M --> PM["Açı Mod. (PM)<br/><i>s_PM = A_c cos(2πf_c t + k_p x(t))</i>"]
    AM --> S1["Standart AM<br/><i>ÇYB + taşıyıcı</i>"]
    AM --> S2["DSB-SC<br/><i>ÇYB taşıyıcısız</i>"]
    AM --> S3["SSB<br/><i>Tek yan bant</i>"]
    AM --> S4["VSB / AYB<br/><i>artık yan bant</i>"]
    style M fill:#1a1a2e,color:#ffffff,stroke:#1a1a2e
    style S1 fill:#d6e0f0,stroke:#1a1a2e
    style S2 fill:#d6e0f0,stroke:#1a1a2e
    style S3 fill:#d6e0f0,stroke:#1a1a2e
    style S4 fill:#d6e0f0,stroke:#1a1a2e
```

> [!warning] Kapsam
> Bu derste **Standart AM** ve **DSB-SC** ağırlıklı. FM/PM kapsam dışı.

---

> [!sinav] Sınav İpucu
> - Verici çıkışı: $x_c(t)$ → modüle edilmiş işaret
> - Kanal çıkışı: $r(t) = x_c(t) * h(t) + n(t)$
> - Modülasyonun amacını 3 maddede bilmek yeterli
