---
tags: [otomatik-kontrol, kararlılık, routh-hurwitz, bibo, örnek-sorular]
---

# 02 — Routh-Hurwitz Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Kararlılık ve Routh-Hurwitz]]

---

## Örnek 1 — Kararlılık Aralığı

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

## Örnek 2 — 4. Derece Sistem

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

## Örnek 3 — %5 Aşım ile K Tasarımı

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

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Kararlılık ve Routh-Hurwitz]]

**İlgili:** [[05 Kök Yer Eğrisi ve Kompansasyon|MST&B - KYE]]
