---
tags: [otomatik-kontrol, kararlılık, routh-hurwitz, bibo, konu-anlatımı]
---

# 02 — Kararlılık ve Routh-Hurwitz Kriteri

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/02 Routh-Hurwitz Örnekleri]]

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

> [!sinav] Sınav İpucu
> - Routh'ta ilk sütunda işaret değişimini say → sağ yarıdaki kök sayısı = kararsızlık derecesi
> - "Sınırda kararlı" sorusu = j-ekseninde hangi $K$ değeri?
> - Yardımcı polinom katsayıları her zaman çift dereceliden gelir
> - 3. derece için: sadece $ab > c$ şartını kontrol et (hızlı!)

---

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/02 Routh-Hurwitz Örnekleri]]

**İlgili:** [[05 Kök Yer Eğrisi ve Kompansasyon|MST&B - KYE]]
