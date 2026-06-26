---
tags: [mst, kompansator, pid, lead, lag, kye, nise-ch9, ornek-sorular]
---

# 07 — Nise Bölüm 9: Kompansatör Tasarımı Soruları

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Kök Yer Eğrisi ve Kompansasyon]]

> Tüm sorularda aksi belirtilmedikçe **şekil P9.1** = birim geri besleme sistemi: $R(s) \to G_c(s)G(s) \to C(s)$.

> [!note]- Ortak Semboller (tüm P9.x soruları için)
> - $G(s)$: bitki (plant); $G_c(s)$: kompansatör; $R(s),C(s)$: referans giriş ve çıkış
> - $K$: değişken kazanç; $z_c,p_c$: kompansatör sıfırı ve kutbu
> - $\%OS$: yüzde aşım; $\zeta$: sönüm oranı ($\%OS\to\zeta$); $\beta=\cos^{-1}\zeta$: kutup açısı
> - $\sigma=\zeta\omega_n=4/T_s$: kutbun reel kısmı; $\omega_d=\sigma\tan\beta$: sönümlü frekans; $s_d=-\sigma\pm j\omega_d$: baskın kutup
> - $T_s$: yerleşme süresi; $T_p$: doruk (peak) zamanı; $\omega_n$: doğal frekans
> - $K_p=\lim_{s\to0}G$ (Tip 0, basamak), $K_v=\lim_{s\to0}sG$ (Tip 1, rampa): statik hata sabitleri; $e_{ss}$: kalıcı hal hatası
> - **PI** $\frac{s+z_c}{s}$: hatayı sıfırlar · **PD** $s+z_c$: $T_s$ azaltır · **Lag**/**Lead**/**Lag-Lead**: aşağıdaki özet tabloya bak

> [!tip] Bu dosya bir **alıştırma bankası**
> Aşağıdaki P9.x soruları Nise Bölüm 9'dan; şu an yalnızca **soru metinleri** var. Adım adım çözümler için dosya sonundaki **"Tasarım Adımları (Ezber)"** reçetesini ve çözümlü örnekler için [[05 Kök Yer Eğrisi Örnekleri]] ile [[06 Final Sınav Soruları (Çözümlü)]] dosyalarını kullan.

---

## 9.2 — PI ve Lag Kompansatörü

### P9.1 — PI Kontrolör (Basamak Hatası Sıfırlama)

$$G(s) = \frac{K}{(s+1)(s+3)(s+10)}, \quad \zeta = 0.5$$

PI kontrolör tasarla: basamak yanıt hatasını sıfırla. Kompansasyonsuz ve kompansasyonlu sistem özelliklerini karşılaştır.

---

### P9.2 — PI Kontrolör (Rampa Hatası Sıfırlama)

$$G(s) = \frac{K}{s(s+3)(s+6)}$$

Kararlılık sağlayan her $K$ için rampa yanıt hatasını sıfırlayan PI kontrolörü tasarla.

---

### P9.3 — Lag Ağı

$$G(s) = \frac{K}{(s+2)(s+3)(s+7)}, \quad \%OS = 10\%$$

**(a)** Uygun statik hata sabiti nedir?

**(b)** Baskın kutupları önemli ölçüde değiştirmeden statik hata sabitini 4'e yükseltecek lag ağının transfer fonksiyonunu bulun.

---

### P9.4 — Lag Ağı (Tekrar)

$$G(s) = \frac{K}{s(s+3)(s+7)}$$

Problem 9.3'ü bu sistem için tekrarla.

---

### P9.5 — Lag: $K_p = 20$ Hedefi

$$G(s) = \frac{K}{(s+3)(s+5)(s+7)}, \quad \%OS = 10\%$$

Baskın kutup konumunu önemli ölçüde değiştirmeden $K_p = 20$ sağlayacak kompansatör tasarla.

---

## 9.3 — PD ve Lead Kompansatörü

### P9.6 — PD Kontrolör ($T_s$ Yarıya İndir)

$$G(s) = \frac{K}{(s+2)(s+3)(s+5)}, \quad \zeta = 0.707$$

PD kontrolör tasarla: yerleşme süresini **2 kat** azalt. Kompansasyonsuz ve kompansasyonlu sistem performansını karşılaştır.

---

### P9.8 — PD Kontrolör ($T_s$ Dörtte Bire İndir)

$$G(s) = \frac{K}{s(s+10)(s+20)}, \quad \%OS = 20\%$$

PD kontrolör tasarla: yerleşme süresini **4 kat** azalt, aşım sabit kalacak.

---

### P9.9 — Lead Kompansatörü

$$G(s) = \frac{K}{(s+4)^3}$$

**(a)** $T_s = 1.6$ s, $\%OS = 25\%$ için baskın kutup konumunu bul.

**(b)** Sıfır $-1$'de olan lead kompansatörünün kutup açısal katkısı nedir?

**(c)** Kompansatör kutbunu bul.

**(d)** Gereken kazancı bul.

**(e)** Diğer kapalı çevrim kutupları nerede?

**(f)** 2. derece yaklaşımının geçerliliğini tartış.

---

### P9.10 — Lead ($z_c = -1$, $T_s$ ve $\%OS$ Hedefi)

$$G(s) = \frac{K}{s(s+20)(s+40)}, \quad T_s = 1.667\text{ s},\; \%OS = 16.3\%$$

Kompansatör sıfırı $-1$'de.

**(a)** Baskın kutup koordinatları.
**(b)** Kompansatör kutbu.
**(c)** Sistem kazancı $K$.
**(d)** Tüm baskın olmayan kutuplar.
**(e)** 2. derece yaklaşımı doğruluğu.
**(f)** Kararlı hal hata özellikleri.

---

### P9.11 — Lead Kompansatörü ($\zeta = 0.8$)

$$G(s) = \frac{K}{(s+3)(s+4)(s+7)(s+9)}$$

**(a)** Kök yer eğrisini çiz.

**(b)** $\zeta = 0.8$ için baskın kutup koordinatları.

**(c)** $\zeta = 0.8$ için kazanç $K$.

**(d)** $T_s = 1$ s, $\zeta = 0.8$: kompansatör sıfırı $-4.5$'te ise kompansatör kutbunu bul.

**(e)** 2. derece yaklaşımının geçerliliği.

---

### P9.13 — Lead ($T_s$ Yarıya, $\%OS$ Sabit)

$$G(s) = \frac{K}{s(s+20)(s+40)}, \quad \%OS = 20\%$$

Aşım değişmeden yerleşme süresini **2 kat** azaltacak lead kompansatörü tasarla.

**(a)** Kompansasyonsuz baskın kutuplar, kazanç ve $T_s$.
**(b)** Kompansasyonlu baskın kutuplar ve $T_s$.
**(c)** Kompansatör kutup ve sıfırı, gereken kazanç.

---

### P9.14 — Lead ($T_s$ Yarıya İndir)

$$G(s) = \frac{K}{(s+15)(s^2+6s+13)}, \quad \%OS = 30\%$$

Kompansatör sıfırı $-7$'de, $T_s$'i yarıya indirecek cascade kompansatör TF'sini ve baskın kutup konumunu bul.

---

### P9.16 — Lead ($\%OS = 20.5\%$, $T_s = 3$ s)

$$G(s) = \frac{K}{s^2(s+4)(s+12)}$$

Lead kompansatörü tasarla: $\%OS = 20.5\%$, $T_s = 3$ s. $K$ değerini de belirle.

---

### P9.17 — Lead ($\zeta = 0.4$, $T_s = 0.5$ s)

$$G(s) = \frac{K}{(s^2+20s+101)(s+20)}$$

**(a)** Baskın kutup koordinatları.
**(b)** Kompansatör kutbu $-15$'te ise kompansatör sıfırını bul.
**(c)** Gereken sistem kazancı.
**(d)** Kompansasyonsuz ve kompansasyonlu performans karşılaştırması.

---

### P9.18 — Lead (2/3 s $T_s$, $\%OS = 1.5\%$)

$$G(s) = \frac{K}{(s+3)(s+5)}$$

**(a)** Basit kazanç ayarıyla $T_s = 2/3$ s ve $\%OS = 1.5\%$ sağlanamayacağını göster.

**(b)** Bu hedefleri sağlayan lead kompansatörünü tasarla: kutup, sıfır ve kazancı belirle.

---

## 9.4 — PID ve Lag-Lead Kompansatörü

### P9.19 — Lag-Lead

$$G(s) = \frac{K}{(s+2)(s+4)(s+6)(s+8)}$$

Lag-lead kompansatörü tasarla: kompansasyonsuz sistemden **0.5 s daha kısa** $T_s$, $\zeta = 0.5$, kararlı hal hatasını **30 kat** iyileştir. Kompansatör sıfırı $-5$'te.

---

### P9.21 — Lag-Lead (Bütünleşik Tasarım)

$$G(s) = \frac{K}{s(s+1)(s+3)}$$

**(a)** Kompansatör tasarla: $T_s = 2.86$ s, $\%OS = 4.32\%$, kararlı hal hatası **2 kat** iyileştirilmiş.

**(b)** Kompansasyonsuz ve kompansasyonlu geçici + kararlı hal karşılaştırması.

**(c)** Kazanç karşılaştırması.

---

### P9.22 — Lag-Lead ($T_p$ Yarıya, $\%OS$ Yarıya)

$$G(s) = \frac{K}{(s+4)(s+5)(s+11)}$$

**(a)** $30\%$ aşım için kazanç $K$, doruk zamanı ve $K_v$.

**(b)** $T_p$ **2 kat** azalt, $\%OS$ **2 kat** azalt, kararlı hal hatası **30 kat** iyileştir.

---

### P9.23 — Passive Kompansatör (Bütünleşik Tasarım)

$$G(s) = \frac{K}{(s^2+4s+8)(s+10)}$$

**Hedefler:** $\%OS < 25\%$, $T_s < 1$ s, $K_p = 10$.

**(a)** $10\%$ aşımlı kompansasyonsuz sistem analizi.

**(b)** Hedefleri sağlayan passive kompansatör tasarla.

---

### P9.25 — PID ($T_p = 1.047$ s, $\zeta = 0.8$)

$$G(s) = \frac{K(s+3)}{(s+1)(s+4)}$$

PID kontrolör tasarla: $T_p = 1.047$ s, $\zeta = 0.8$, basamak için sıfır hata.

---

### P9.26 — PID ($\%OS \leq 25\%$, $T_s \leq 2$ s, sıfır hata)

$$G(s) = \frac{K}{(s+4)(s+6)(s+10)}$$

**(a)** Basamak ve rampa için sıfır kararlı hal hatası, $\%OS \leq 25\%$, $T_s \leq 2$ s sağlayacak kontrolör tasarla.

---

## 9.5 — Hız Geri Beslemesi (Rate Feedback)

### P9.29 — Rate Feedback

$$G(s) = \frac{K}{(s^2+2s+0.25)}, \quad \%OS \leq 15\%, \quad T_s \leq 3 \text{ s}$$

Hız geri beslemesi ile tasarla.

---

### P9.30 — İç Çevrim + Dış Çevrim

Şekil P9.4: İç çevrim ile $s+a$ geri beslemesi.

**(a)** $K_1$ ve $\alpha$: iç çevrim $T_s = 1$ s, $\%OS = 5\%$.

**(b)** Dış çevrim $K$: $\%OS = 10\%$ için.

---

## Özet: Hangi Kompansatör Ne Zaman?

| Kompansatör | Transfer Fonksiyonu | Etki |
|-------------|---------------------|------|
| **PI** | $\dfrac{s+z_c}{s}$ | Basamak/rampa hatası → 0 |
| **PD** | $s + z_c$ | $T_s$, $T_p$ azaltır |
| **PID** | $\dfrac{(s+z_1)(s+z_2)}{s}$ | Her ikisi |
| **Lag** | $\dfrac{s+z_c}{s+p_c}$, $z_c>p_c$, orijine yakın | $K_{\text{ss}}$ artar, geçici yanıt az değişir |
| **Lead** | $\dfrac{s+z_c}{s+p_c}$, $z_c<p_c$ | $T_s$ azaltır, faz artar |
| **Lag-Lead** | Lead × Lag | Her ikisi |

> [!sinav] Tasarım Adımları (Ezber)
> 1. $\%OS \to \zeta$, $T_s \to \sigma = 4/T_s$, $\omega_d = \sigma\tan(\arccos\zeta)$
> 2. Baskın kutup: $s_d = -\sigma \pm j\omega_d$
> 3. $G_p(s_d)$ açısını hesapla
> 4. Açı farkı → kompansatör sıfır/kutbunu yerleştir
> 5. Genlik şartı: $|G_c(s_d)G_p(s_d)| = 1 \Rightarrow K$

← [[MST Ana Sayfa]] | [[MST Sınav Gecesi]]
