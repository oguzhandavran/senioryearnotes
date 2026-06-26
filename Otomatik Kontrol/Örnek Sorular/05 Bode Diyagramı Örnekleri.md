---
tags: [otomatik-kontrol, bode, frekans-analizi, faz-payı, kazanç-payı, örnek-sorular]
---

# 05 — Bode Diyagramı Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Frekans Analizi ve Bode Diyagramı]]

---

## Örnek 1 — Adım Adım Bode Çizimi

> [!note]- Semboller
> - **Bode**: $|G(j\omega)|$ (dB, $20\log|G|$) ve $\angle G(j\omega)$ (derece) — log frekans ekseninde
> - **Köşe (köşeli) frekans**: her $(1+s/\omega_c)$ teriminin $\omega_c$'si; orada eğim $-20$ dB/dek değişir
> - $1/s$ (integratör): sabit $-20$ dB/dek eğim ve sabit $-90°$ faz
> - Standart biçim: paydaki sabitleri ayıkla → DC kazanç $\times$ $\dfrac{1}{(1+s/\omega_c)}$ çarpanları; düşük frekans seviyesi $20\log(\text{kazanç})$
> - Faz: her birinci derece kutup köşe frekansının $0.1\times$'inden $10\times$'ine kadar $0°\to-90°$ döner

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

> [!note]- Semboller
> - $\omega_{gc}$ (kazanç kesişimi): $|G(j\omega)|=1$ (0 dB) olduğu frekans → **faz payı** burada okunur
> - $\omega_{pc}$ (faz kesişimi): $\angle G(j\omega)=-180°$ olduğu frekans → **kazanç payı** burada okunur
> - $PM=180°+\angle G(j\omega_{gc})$: faz payı; $GM=-20\log|G(j\omega_{pc})|$: kazanç payı (dB)
> - Tasarım hedefi tipik: $PM\gtrsim45°$, $GM\gtrsim6$ dB; küçükse sistem yetersiz sönümlü
> - $\arctan a+\arctan b=90° \Leftrightarrow ab=1$ (faz kesişimi çözümünde kullanılır)

$$G(s) = \frac{10}{s(s+1)(s+5)}, \quad G(j\omega) = \frac{10}{j\omega(j\omega+1)(j\omega+5)}$$

**Kazanç kesişim frekansı** ($|G(j\omega_{gc})| = 1$):

$|G(j\omega)| = \dfrac{10}{\omega\sqrt{\omega^2+1}\sqrt{\omega^2+25}}$

$|G|=1 \Rightarrow \omega\sqrt{\omega^2+1}\sqrt{\omega^2+25}=10$. Deneme: $\omega=1.23$ → $1.23\cdot\sqrt{2.51}\cdot\sqrt{26.5}=1.23\cdot1.585\cdot5.15\approx10.0$ ✓

$$\omega_{gc} \approx 1.23 \text{ rad/s}$$

**Faz kesişim frekansı** ($\angle G = -180°$):

$$\angle G(j\omega) = -90° - \arctan(\omega) - \arctan(\omega/5)$$

$-90° - \arctan(\omega_{pc}) - \arctan(\omega_{pc}/5) = -180°$

$\arctan(\omega) + \arctan(\omega/5) = 90°$ → $\omega_{pc} = \sqrt{5} \approx 2.236$ rad/s

*(Kontrol: $\arctan(\sqrt{5}) + \arctan(\sqrt{5}/5) = 65.9° + 24.1° = 90°$ ✓)*

**Kazanç payı** ($\omega_{pc}=\sqrt5$, $\sqrt{\omega^2+1}=\sqrt6$, $\sqrt{\omega^2+25}=\sqrt{30}$):
$$|G(j\omega_{pc})| = \frac{10}{\sqrt{5}\,\sqrt{6}\,\sqrt{30}} = \frac{10}{\sqrt{900}} = \frac{10}{30} = \frac13$$
$$GM = -20\log|G(j\omega_{pc})| = -20\log\tfrac13 = +20\log 3 \approx +9.5 \text{ dB}$$

**Faz payı ($\omega = \omega_{gc} \approx 1.23$):**
$$\angle G(j1.23) = -90° - \arctan(1.23) - \arctan(0.246) \approx -90° - 50.9° - 13.8° = -154.7°$$
$$\boxed{PM = 180° - 154.7° \approx 25.3°} \quad (<45° \to \text{tasarım revizyonu gerekir})$$

---

## Örnek 3 — $G(s) = K/(s+1)^3$ için Kararlılık Sınırı

> [!note]- Semboller
> - Üç özdeş kutup → faz $=-3\arctan\omega$; $-180°$ olması için her biri $-60°$ → $\omega_{pc}=\tan60°=\sqrt3$
> - $K_\text{maks}$: faz kesişiminde $|G|=1$ yapan kazanç → kararlılık sınırı (üstünde kararsız)
> - $GM=20\log(K_\text{maks}/K)$: mevcut $K$ için kazanç payı; $K=K_\text{maks}$'ta GM $=0$ dB (sınırda)

$$|G(j\omega)|_{\omega_{pc}} = 1 \implies \frac{K}{(\sqrt{\omega^2+1})^3} = 1$$

Faz $= -180°$: $-3\arctan(\omega) = -180° \implies \omega_{pc} = \sqrt{3}$ rad/s

$$K_\text{maks} = (\sqrt{3+1})^3 = 8 \implies GM = 20\log(8/K) \text{ dB}$$

$K=1$: $GM = 18$ dB ✓; $K=8$: $GM = 0$ dB (sınırda kararlı)

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Frekans Analizi ve Bode Diyagramı]]
