---
tags: [otomatik-kontrol, hub, index]
aliases: [OK, Otomatik Kontrol]
---

# Otomatik Kontrol — Ana Sayfa

← [[HOME]]

## Konu Haritası

```mermaid
mindmap
  root((Otomatik\nKontrol))
    Temel Kavramlar
      Açık/Kapalı Çevrim
      Blok Diyagramlar
      Mason Formülü
      Transfer Fonksiyonu
    Kararlılık
      BIBO Kararlılık
      Routh-Hurwitz
      Kutup Analizi
    Kararlı Hal Hataları
      Tip 0/1/2 Sistem
      Hata Sabitleri Kp Kv Ka
      Bozucu Etki Hatası
    Kök Yer Eğrisi
      Asimptotlar
      Breakaway
      j-ekseni Kesişimi
    Geçici Yanıt
      2. Derece Sistem
      ζ ωn
      %OS Tr Tp Ts
    Frekans Analizi
      Bode Diyagramı
      PM GM Faz/Kazanç Payı
```

## Notlar

| # | Konu | Bağlantı |
|---|------|----------|
| 1 | Giriş, Kapalı Çevrim, Blok Diyagramlar, Mason | [[01 Giriş Kapalı Çevrim ve Blok Diyagramları]] |
| 2 | Kararlılık ve Routh-Hurwitz | [[02 Kararlılık ve Routh-Hurwitz]] |
| 3 | Kararlı Hal Hataları | [[03 Kararlı Hal Hataları]] |
| 4 | Kök Yer Eğrisi | [[04 Kök Yer Eğrisi]] |
| 5 | Frekans Analizi ve Bode | [[05 Frekans Analizi ve Bode Diyagramı]] |
| 📄 | Formül Özeti | [[OK Formül Sayfası]] |

## İlgili Derslerle Bağlantı

```mermaid
graph LR
    OK["🎛️ Otomatik Kontrol"] <--> MST["⚙️ MST&B"]
    OK --> SS["〰️ Sinyaller & Sistemler"]
    MST --> OK
    style OK fill:#FFA500,color:#000
    style MST fill:#18B464,color:#fff
    style SS fill:#5B9BD5,color:#fff
```

- **[[../Mühendislik Sİstem Tasarımı ve Benzetimi/MST Ana Sayfa|MST&B]]** — Transfer fonksiyonu, Laplace, KYE ortak
- **[[../Sİnyaller ve Sistemler/SS Ana Sayfa|SS]]** — Laplace dönüşümü temeli

## Temel Formüller (Hızlı Erişim)

**Kapalı Çevrim TF:** $T(s) = \dfrac{G(s)}{1 + G(s)H(s)}$

**Routh 3. Derece:** $s^3 + as^2 + bs + c = 0$ → Şart: $ab > c$

**Hata Sabitleri:** $K_p = \lim_{s\to 0}G(s)$, $K_v = \lim_{s\to 0}sG(s)$, $K_a = \lim_{s\to 0}s^2G(s)$

**KYE Asimptot Açısı:** $\theta_q = \dfrac{\pm 180°(2q+1)}{n-m}$

**2. Derece:** $s^2 + 2\zeta\omega_n s + \omega_n^2 = 0$ → $T_s \approx \dfrac{4}{\zeta\omega_n}$, $\%OS = 100e^{-\pi\zeta/\sqrt{1-\zeta^2}}$
