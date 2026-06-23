---
tags: [otomatik-kontrol, kararlılık, routh-hurwitz, bibo]
---

# 02 — Kararlılık ve Routh-Hurwitz Kriteri

← [[OK Ana Sayfa]]

## Kararlılık Tanımı

> [!tanim] BIBO Kararlılık
> Sınırlı her girişe karşı çıkış da sınırlı kalıyorsa sistem BIBO (Bounded-Input Bounded-Output) kararlıdır.

**Transfer fonksiyonu ile kararlılık:** Tüm kutuplar sol yarı düzlemde ($\text{Re}(s) < 0$) olmalı.

| Kutup Konumu | Sistem | Yanıt |
|-------------|--------|-------|
| Sol yarım düzlem ($\text{Re}(s) < 0$) | KARARLI | Azalan |
| Sağ yarım düzlem ($\text{Re}(s) > 0$) | KARARSIZ | Büyüyen |
| Sanal eksen (basit, $\text{Re}(s) = 0$) | MARJİNAL KARARLI | Sabit genlikli titreşim |
| Sanal eksen (katlı) | KARARSIZ | Büyüyen titreşim |

---

## Routh-Hurwitz Kriteri

### Routh Tablosu Oluşturma

Karakteristik denklem: $a_n s^n + a_{n-1}s^{n-1} + \cdots + a_1 s + a_0 = 0$

$$\begin{array}{c|cccc}
s^n & a_n & a_{n-2} & a_{n-4} & \cdots \\
s^{n-1} & a_{n-1} & a_{n-3} & a_{n-5} & \cdots \\
s^{n-2} & b_1 & b_2 & b_3 & \cdots \\
s^{n-3} & c_1 & c_2 & c_3 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \\
s^0 & \cdots & & &
\end{array}$$

**Formüller:**
$$b_1 = \frac{a_{n-1}\cdot a_{n-2} - a_n \cdot a_{n-3}}{a_{n-1}}, \quad b_2 = \frac{a_{n-1}\cdot a_{n-4} - a_n \cdot a_{n-5}}{a_{n-1}}$$

$$c_1 = \frac{b_1 \cdot a_{n-3} - a_{n-1} \cdot b_2}{b_1}, \quad \ldots$$

> [!sinav] Kararlılık Koşulu
> **Birinci sütundaki tüm elemanlar aynı işarette** olmalı (tercihen pozitif).
> - İşaret değişimi sayısı = Sağ yarım düzlemdeki kök sayısı

### 3. Derece için Hızlı Kural

$$s^3 + as^2 + bs + c = 0$$

Kararlılık için: $a > 0$, $c > 0$, **$ab > c$**

### 4. Derece için Routh Tablosu

$$s^4 + as^3 + bs^2 + cs + d = 0$$

$$\begin{array}{c|ccc}
s^4 & 1 & b & d \\
s^3 & a & c & 0 \\
s^2 & \dfrac{ab-c}{a} & d & 0 \\
s^1 & \dfrac{(ab-c)c - a^2 d}{ab-c} & 0 & \\
s^0 & d & &
\end{array}$$

---

## Özel Durumlar

### Durum 1: İlk Sütunda Sıfır (Satırın Geri Kalanı Sıfır Değil)

Sıfırı küçük bir $\varepsilon > 0$ ile değiştir, tabloyu hesapla, $\varepsilon \to 0$ limitini al.

### Durum 2: Tüm Satır Sıfır (Yardımcı Polinom)

1. Sıfır olan satırın **üstündeki** satırdan yardımcı polinom $P(s)$ oluştur
2. $P(s)$'i $s$'e göre türev al: $P'(s)$
3. $P'(s)$'in katsayılarını sıfır satıra yaz, tabloya devam et

**Yardımcı polinom:** Her zaman çift dereceli, kökleri sanal eksende → **marjinal kararlılık**

---

## Çözümlü Örnekler

### Örnek 1 — Kararlılık Aralığı

$$G(s) = \frac{K}{s^3 + 10s^2 + 25s + 10}$$

Unity feedback kapalı çevrim karakteristik denklem:
$$s^3 + 10s^2 + 25s + (10 + K) = 0$$

Routh tablosu (3. derece: $ab > c$ kuralı):

$$a = 10,\quad b = 25,\quad c = 10 + K$$

$$\frac{ab - c}{a} = \frac{10 \cdot 25 - (10+K)}{10} = \frac{240 - K}{10} > 0 \implies K < 240$$

Ayrıca $c > 0 \implies K > -10$

$$\boxed{-10 < K < 240}$$

**Sınırda kararlı ($K = 240$):** Yardımcı polinom $s^2$ satırından:
$$10s^2 + (10 + 240) = 10s^2 + 250 = 0 \implies s = \pm j5$$

$$\boxed{\omega_\text{salınım} = 5 \text{ rad/s}}$$

---

### Örnek 2 — 4. Derece Sistem

$$G(s) = \frac{K}{s^4 + 7s^3 + 11s^2 + 7s}$$

Karakteristik denklem: $s^4 + 7s^3 + 11s^2 + 7s + K = 0$

Routh tablosu:

$$\begin{array}{c|cc}
s^4 & 1 & 11 & K \\
s^3 & 7 & 7 & 0 \\
s^2 & 10 & K & \\
s^1 & \dfrac{70-7K}{10} & 0 & \\
s^0 & K & &
\end{array}$$

Kararlılık: $\dfrac{70-7K}{10} > 0 \implies K < 10$ ve $K > 0$

$$\boxed{0 < K < 10}$$

**Sınırda ($K = 10$):** $10s^2 + 10 = 0 \implies s = \pm j1$

$$\omega_\text{salınım} = 1 \text{ rad/s}$$

---

### Örnek 3 — %5 Aşım ile K Tasarımı

$$G(s) = \frac{K}{(s+2)(s+4)}$$

Kapalı çevrim: $T(s) = \dfrac{K}{s^2 + 6s + (8+K)}$

Standart 2. derece: $\omega_n^2 = 8+K$, $2\zeta\omega_n = 6 \implies \zeta\omega_n = 3$

%5 aşım: $\%OS = 5 \implies \zeta \approx 0.690$

$$\omega_n = \frac{3}{\zeta} = \frac{3}{0.690} \approx 4.347 \implies K = \omega_n^2 - 8 \approx 10.90$$

$$T_s = \frac{4}{\zeta\omega_n} = \frac{4}{3} \approx 1.33 \text{ s}$$

---

## Geçici Yanıt — Transfer Fonksiyonlarından

### Verilen TF → $T_r, T_p, T_s$, aşım, $e_{ss}$

$$G(s) = \frac{9}{s^2 + 4.2s + 9}: \quad \omega_n = 3,\ \zeta = 0.7$$

$$T_r \approx 0.709\text{ s},\quad T_p \approx 1.467\text{ s},\quad T_s \approx 1.993\text{ s},\quad \%OS \approx 4.6\%,\quad e_{ss} = 0$$

$$G(s) = \frac{3}{s^2 + 0.6s + 1}: \quad \omega_n = 1,\ \zeta = 0.3$$

$$T_r \approx 1.320\text{ s},\quad T_p \approx 3.293\text{ s},\quad T_s \approx 11.228\text{ s},\quad \%OS \approx 37.23\%$$

> [!sinav] Sınav İpucu
> - Routh'ta ilk sütunda işaret değişimini say → sağ yarıdaki kök sayısı = kararsızlık derecesi
> - "Sınırda kararlı" sorusu = j-ekseninde hangi $K$ değeri?
> - Yardımcı polinom katsayıları her zaman çift dereceliden gelir
> - 3. derece için: sadece $ab > c$ şartını kontrol et (hızlı!)

---

← [[01 Giriş Kapalı Çevrim ve Blok Diyagramları]] | [[OK Ana Sayfa]] | → [[03 Kararlı Hal Hataları]]

**İlgili:** [[05 Kök Yer Eğrisi ve Kompansasyon|MST&B - KYE]]
