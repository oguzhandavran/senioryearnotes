---
tags: [otomatik-kontrol, bode, frekans-analizi, faz-payı, kazanç-payı, örnek-sorular]
---

# 05 — Bode Diyagramı Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Frekans Analizi ve Bode Diyagramı]]

---

## Örnek 1 — Adım Adım Bode Çizimi

### $G(s) = \dfrac{10}{s(s+1)(s+5)}$

**Adım 1:** Standart biçime getir:

$$G(s) = \frac{10}{5}\cdot\frac{1}{s}\cdot\frac{1}{(1+s)}\cdot\frac{1}{(1+s/5)} = \frac{2}{s(1+s)(1+s/5)}$$

**Adım 2 — Kazanç diyagramı (kırık-çizgi yaklaşımı):**

| Frekans Aralığı | Eğim | Başlangıç |
|----------------|------|-----------|
| $\omega < 1$ | $-20$ dB/dekad | $\omega=1$'de $20\log 2 = 6$ dB |
| $1 < \omega < 5$ | $-20 + (-20) = -40$ dB/dekad | ($\omega=1$ köşe noktası) |
| $\omega > 5$ | $-40 + (-20) = -60$ dB/dekad | ($\omega=5$ köşe noktası) |

**Adım 3 — Faz diyagramı:**

| Blok | Faz Katkısı |
|------|------------|
| $1/s$ | $-90°$ (sabit) |
| $1/(1+s)$ | $0° \to -90°$ ($\omega=0.1 \to 10$) |
| $1/(1+s/5)$ | $0° \to -90°$ ($\omega=0.5 \to 50$) |
| **Toplam** | $-90° \to -270°$ |

**Faz payı hesabı:** $|G(j\omega_{gc})| = 0$ dB noktasını bul, o frekansda faz ölç:
$$PM = 180° + \angle G(j\omega_{gc})$$

---

## Örnek 2 — PM ve GM Sayısal Hesabı

$$G(s) = \frac{10}{s(s+1)(s+5)}, \quad G(j\omega) = \frac{10}{j\omega(j\omega+1)(j\omega+5)}$$

**Kazanç kesişim frekansı** ($|G(j\omega_{gc})| = 1$):

$|G(j\omega)| = \dfrac{10}{\omega\sqrt{\omega^2+1}\sqrt{\omega^2+25}}$

$\omega_{gc} \approx 1.12$ rad/s ($|G| = 1$ yaklaşık çözüm)

**Faz kesişim frekansı** ($\angle G = -180°$):

$$\angle G(j\omega) = -90° - \arctan(\omega) - \arctan(\omega/5)$$

$-90° - \arctan(\omega_{pc}) - \arctan(\omega_{pc}/5) = -180°$

$\arctan(\omega) + \arctan(\omega/5) = 90°$ → $\omega_{pc} = \sqrt{5} \approx 2.236$ rad/s

*(Kontrol: $\arctan(\sqrt{5}) + \arctan(\sqrt{5}/5) = 65.9° + 24.1° = 90°$ ✓)*

**Kazanç payı:**
$$GM = -20\log|G(j\omega_{pc})| = -20\log\frac{10}{\sqrt{5}\sqrt{6}\sqrt{30}} = -20\log\frac{10}{20} = +6 \text{ dB} ✓$$

**Faz payı ($\omega = \omega_{gc} \approx 1.12$):**
$$\angle G(j1.12) = -90° - \arctan(1.12) - \arctan(0.224) \approx -90° - 48.3° - 12.6° = -150.9°$$
$$\boxed{PM = 180° - 150.9° \approx 29.1°} \quad (<45° \to \text{tasarım revizyonu gerekir})$$

---

## Örnek 3 — $G(s) = K/(s+1)^3$ için Kararlılık Sınırı

$$|G(j\omega)|_{\omega_{pc}} = 1 \implies \frac{K}{(\sqrt{\omega^2+1})^3} = 1$$

Faz $= -180°$: $-3\arctan(\omega) = -180° \implies \omega_{pc} = \sqrt{3}$ rad/s

$$K_\text{maks} = (\sqrt{3+1})^3 = 8 \implies GM = 20\log(8/K) \text{ dB}$$

$K=1$: $GM = 18$ dB ✓; $K=8$: $GM = 0$ dB (sınırda kararlı)

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Frekans Analizi ve Bode Diyagramı]]
