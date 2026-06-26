---
tags: [otomatik-kontrol, hub, index]
aliases: [OK, Otomatik Kontrol]
---

# Otomatik Kontrol — Ana Sayfa

← [[HOME]]

## Konu Haritası

```mermaid
flowchart LR
    OK(["Otomatik Kontrol"])
    OK --> A["<b>Temel Kavramlar</b><br/>• Açık/Kapalı Çevrim<br/>• Blok Diyagramlar & Mason Formülü<br/>• Transfer Fonksiyonu G(s)<br/>• Kapalı Çevrim TF: G/(1+GH)"]
    OK --> B["<b>Kararlılık</b><br/>• BIBO (tüm kutuplar sol yarı düzlem)<br/>• Routh-Hurwitz Kriteri<br/>• Kutup Analizi"]
    OK --> C["<b>Kararlı Hal Hataları</b><br/>• Tip 0/1/2 sınıflandırması<br/>• Hata sabitleri: Kp, Kv, Ka<br/>• Bozucu etki hatası"]
    OK --> D["<b>Kök Yer Eğrisi (KYE)</b><br/>• Asimptotlar: açı ve merkez (σa)<br/>• Breakaway noktası<br/>• jω-ekseni kesişimi (Routh)"]
    OK --> E["<b>Geçici Yanıt</b><br/>• 2. derece sistem analizi<br/>• ζ (sönüm oranı) ve ωn<br/>• %OS, Tr, Tp, Ts"]
    OK --> F["<b>Frekans Analizi</b><br/>• Bode diyagramı (dB ve derece)<br/>• Faz payı (PM) ve kazanç payı (GM)"]
    style OK fill:#1a1a2e,color:#ffffff,stroke:#1a1a2e
    style A fill:#eef2f7,stroke:#1a1a2e
    style B fill:#d6e0f0,stroke:#1a1a2e
    style C fill:#eef2f7,stroke:#1a1a2e
    style D fill:#d6e0f0,stroke:#1a1a2e
    style E fill:#eef2f7,stroke:#1a1a2e
    style F fill:#d6e0f0,stroke:#1a1a2e
```

## Konu Anlatımları

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Giriş, Kapalı Çevrim, Blok Diyagramlar, Mason | [[Konu Anlatımları/01 Giriş Kapalı Çevrim ve Blok Diyagramları]] |
| 2 | Kararlılık ve Routh-Hurwitz | [[Konu Anlatımları/02 Kararlılık ve Routh-Hurwitz]] |
| 3 | Kararlı Hal Hataları | [[Konu Anlatımları/03 Kararlı Hal Hataları]] |
| 4 | Kök Yer Eğrisi | [[Konu Anlatımları/04 Kök Yer Eğrisi]] |
| 5 | Frekans Analizi ve Bode | [[Konu Anlatımları/05 Frekans Analizi ve Bode Diyagramı]] |
| 📄 | Formül Özeti | [[OK Formül Sayfası]] |

## Örnek Sorular

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Blok Diyagram Örnekleri | [[Örnek Sorular/01 Blok Diyagram Örnekleri]] |
| 2 | Routh-Hurwitz Örnekleri | [[Örnek Sorular/02 Routh-Hurwitz Örnekleri]] |
| 3 | Kararlı Hal Hata Örnekleri | [[Örnek Sorular/03 Kararlı Hal Hata Örnekleri]] |
| 4 | Kök Yer Eğrisi Örnekleri | [[Örnek Sorular/04 Kök Yer Eğrisi Örnekleri]] |
| 5 | Bode Diyagramı Örnekleri | [[Örnek Sorular/05 Bode Diyagramı Örnekleri]] |

## İlgili Derslerle Bağlantı

```mermaid
flowchart LR
    OK["Otomatik Kontrol"]
    MST["MST & Benzetim"]
    SS["Sinyaller & Sistemler"]
    OK <--> MST
    OK --> SS
    style OK fill:#FFA500,stroke:#1a1a2e,color:#1a1a2e
    style MST fill:#18B464,stroke:#1a1a2e,color:#ffffff
    style SS fill:#5B9BD5,stroke:#1a1a2e,color:#ffffff
```

- **[[MST Ana Sayfa|MST&B]]** — Transfer fonksiyonu, Laplace, KYE ortak
- **[[../Sİnyaller ve Sistemler/SS Ana Sayfa|SS]]** — Laplace dönüşümü temeli

## Temel Formüller (Hızlı Erişim)

**Kapalı Çevrim TF:** $T(s) = \dfrac{G(s)}{1 + G(s)H(s)}$

**Routh 3. Derece:** $s^3 + as^2 + bs + c = 0$ → Şart: $ab > c$

**Hata Sabitleri:** $K_p = \lim_{s\to 0}G(s)$, $K_v = \lim_{s\to 0}sG(s)$, $K_a = \lim_{s\to 0}s^2G(s)$

**KYE Asimptot Açısı:** $\theta_q = \dfrac{\pm 180°(2q+1)}{n-m}$

**2. Derece:** $s^2 + 2\zeta\omega_n s + \omega_n^2 = 0$ → $T_s \approx \dfrac{4}{\zeta\omega_n}$, $\%OS = 100e^{-\pi\zeta/\sqrt{1-\zeta^2}}$
