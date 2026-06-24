---
tags: [otomatik-kontrol, sinav-gecesi, ozet]
---

# OK — Sınav Gecesi Özeti

> Tek sayfa. Her şey burada. Başka yere bakma.

> [!danger] BÜTÜNLEME İPUCU (24.06.2026)
> **Muhammet hoca:** "Vize ve final sorularına çalışırsanız 100 alırsınız — soruları ezberlemeyin, mantığını anlayın, rakamlar değişir."
> Hoca vize + final soruları benzeri yapacakmış, farklı bir şey beklemeyin.
> **Classroom'daki çalışma sorularına da bak** — ekstra hazırlık materyali orada.

---

## 1 — Kapalı Çevrim TF

$$T(s) = \frac{G(s)}{1+G(s)H(s)} \qquad \text{unity feedback: } H=1$$

**Blok sadeleştirme:** İç çevrimden dışa doğru git. Her adımda $G/(1+GH)$.

**Mason:** $T = \sum P_k\Delta_k/\Delta$; $\Delta = 1 - \sum L_i + \sum L_iL_j - \cdots$

---

## 2 — 2. Derece Sistem Parametreleri

$$G(s) = \frac{K\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$$

| Parametre | Formül |
|-----------|--------|
| $\omega_n$ | $\sqrt{\text{sabit terim}}$ |
| $\zeta$ | $\frac{\text{s katsayısı}}{2\omega_n}$ |
| $T_p$ | $\pi/\omega_d$, $\omega_d=\omega_n\sqrt{1-\zeta^2}$ |
| $T_s$ | $4/(\zeta\omega_n)$ |
| $\%OS$ | $100e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| $\zeta$ ← %OS | $\frac{-\ln(\%OS/100)}{\sqrt{\pi^2+\ln^2(\%OS/100)}}$ |

---

## 3 — Routh-Hurwitz

$$s^n:\, a_n \quad a_{n-2} \quad \cdots$$
$$s^{n-1}:\, a_{n-1} \quad a_{n-3} \quad \cdots$$
$$s^{n-2}:\, b_1=\frac{a_{n-1}a_{n-2}-a_na_{n-3}}{a_{n-1}} \quad b_2=\cdots$$

**Kararlı ↔ 1. sütun hepsi aynı işaret.**  
**3. derece hızlı:** $ab > c$ ($s^3+as^2+bs+c$)

Sıfır satır → yardımcı pol. türev al. Sıfır eleman → $\varepsilon$.

**$K$ aralığı:** $s^1$ satırını $> 0$ yap. Sınırda ($s^1=0$) → yardımcı pol. → $\omega$.

---

## 4 — Kararlı Hal Hatası

| | Tip 0 | Tip 1 | Tip 2 |
|-|-------|-------|-------|
| Basamak | $1/(1+K_p)$ | 0 | 0 |
| Rampa | $\infty$ | $1/K_v$ | 0 |
| Parabol | $\infty$ | $\infty$ | $1/K_a$ |

$K_p=\lim_{s\to0}G$; $K_v=\lim_{s\to0}sG$; $K_a=\lim_{s\to0}s^2G$

**Tip = payda'da orijin kutup sayısı.**

---

## 5 — Kök Yer Eğrisi (Adımlar)

1. Kutuplar (✕) ve sıfırlar (○) işaretle
2. Gerçek eksende: sağdaki ✕+○ sayısı **tek** → KYE var
3. Asimptotlar: $\theta_q = (2q+1)180°/(n-m)$; $\sigma_a = (\sum p_i - \sum z_j)/(n-m)$
4. Breakaway: $dK/ds=0$ → $\sum 1/(s-p_i) = \sum 1/(s-z_j)$
5. $j$-ekseni: Routh'tan $K_c$, yardımcı pol. → $\omega$

**KYE kutuptan başlar, sıfıra/sonsuza gider.**  
Baskın kutuplar: $|\text{Re}| \leq 1/5$ diğer kutupların gerçek kısımları.

---

## 6 — Bode ve Faz/Kazanç Payı

**Standart biçim:** $G(s) = \frac{K\prod(1+s/z_i)}{s^N\prod(1+s/p_j)}$

Kazanç: başla $20\log K - 20N$ dB/dekad; köşe frekansında ±20 dB/dekad değiş.

$$PM = 180° + \angle G(j\omega_{gc}) \qquad (\omega_{gc}: |G|=0\text{ dB})$$
$$GM = -20\log|G(j\omega_{pc})| \text{ dB} \qquad (\omega_{pc}: \angle G=-180°)$$

**Kararlı: PM > 0 VE GM > 0.** Hedef: PM ≈ 45–60°.

---

## Tuzaklar

> [!warning] Sınav Tuzakları
> - Son değer teoremi: **önce kararlılık kontrol et!**
> - Routh'ta eksik katsayı → doğrudan **kararsız**
> - Tip sistemi için açık çevrim $G(s)$'e bak, kapalı değil
> - KYE: sadece **negatif** geri besleme için bu kurallar geçer
> - Bode'da $j\omega$'yı $s$'e koy ($s = j\omega$); genlik ve fazı ayrı hesapla
> - %OS'tan $\zeta$ bulmayı ezberle (tablo yok!)

---

← [[OK Ana Sayfa]] | [[OK Formül Sayfası]]
