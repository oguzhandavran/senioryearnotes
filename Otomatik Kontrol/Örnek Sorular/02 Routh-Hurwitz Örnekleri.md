---
tags: [otomatik-kontrol, kararlılık, routh-hurwitz, bibo, örnek-sorular]
---

# 02 — Routh-Hurwitz Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Kararlılık ve Routh-Hurwitz]]

---

## Örnek 1 — Kararlılık Aralığı

> [!note]- Semboller
> - $G(s)$: açık çevrim TF; $K$: kazanç; birim geri besleme → karakteristik denklem payda$+K\cdot$pay
> - Routh tablosu: 1. sütundaki işaret değişimi sayısı = sağ yarı düzlem kök sayısı
> - 3. derece kararlılık kuralı: tüm katsayılar $>0$ **ve** $a_2a_1>a_0$
> - Sınırda kararlı: $K$ kritikte $s^2$ satırından **yardımcı polinom** → sanal eksen kökleri ($\pm j\omega$)

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

> [!note]- Semboller
> - $G(s)$: açık çevrim TF; $K$: kazanç; karakteristik denklem $=$ payda $+K\cdot$pay
> - Routh tablosu satırları $s^4\dots s^0$: her satır bir önceki iki satırdan determinant kuralıyla üretilir
> - $\dfrac{70-7K}{10}$: $s^1$ satırının ilk elemanı ($s^2$ ve $s^3$ satırlarından)
> - Sınırda kararlı: $s^2$ satırından **yardımcı polinom** $\to$ sanal eksen kökleri $\pm j\omega$

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

> [!note]- Semboller
> - $\zeta$: sönüm oranı (boyutsuz); $\omega_n$: doğal frekans (rad/s)
> - $\%OS$: yüzde maksimum aşım; $\zeta=\dfrac{-\ln(\%OS/100)}{\sqrt{\pi^2+\ln^2(\%OS/100)}}$
> - Standart 2. derece payda: $s^2+2\zeta\omega_n s+\omega_n^2$
> - $T_s\approx\dfrac{4}{\zeta\omega_n}$: %2 yerleşme süresi (s)

$$G(s) = \frac{K}{(s+2)(s+4)}$$

Kapalı çevrim: $T(s) = \dfrac{K}{s^2 + 6s + (8+K)}$

Standart 2. derece: $\omega_n^2 = 8+K$, $2\zeta\omega_n = 6 \implies \zeta\omega_n = 3$

%5 aşım: $\%OS = 5 \implies \zeta \approx 0.690$

$$\omega_n = \frac{3}{\zeta} = \frac{3}{0.690} \approx 4.347 \implies K = \omega_n^2 - 8 \approx 10.90$$

$$T_s = \frac{4}{\zeta\omega_n} = \frac{4}{3} \approx 1.33 \text{ s}$$

---

## Geçici Yanıt — Transfer Fonksiyonlarından

> [!note]- Semboller
> - $\omega_n=\sqrt{a_0}$: doğal frekans (paydanın sabit teriminin karekökü); $\zeta=\dfrac{a_1}{2\omega_n}$ ($a_1$: $s$ katsayısı)
> - $T_r$: yükselme süresi (%10→%90); $T_p=\dfrac{\pi}{\omega_n\sqrt{1-\zeta^2}}$: tepe süresi (s)
> - $T_s\approx\dfrac{4}{\zeta\omega_n}$: yerleşme süresi (s); $\%OS=100\,e^{-\zeta\pi/\sqrt{1-\zeta^2}}$
> - $e_{ss}$: birim basamağa karşı kalıcı durum hatası; DC kazanç $=1$ ise $e_{ss}=0$

### Verilen TF → $T_r, T_p, T_s$, aşım, $e_{ss}$

$$G(s) = \frac{9}{s^2 + 4.2s + 9}: \quad \omega_n = 3,\ \zeta = 0.7$$

$$T_r \approx 0.709\text{ s},\quad T_p \approx 1.467\text{ s},\quad T_s \approx 1.993\text{ s},\quad \%OS \approx 4.6\%,\quad e_{ss} = 0$$

$$G(s) = \frac{3}{s^2 + 0.6s + 1}: \quad \omega_n = 1,\ \zeta = 0.3$$

$$T_r \approx 1.320\text{ s},\quad T_p \approx 3.293\text{ s},\quad T_s \approx 11.228\text{ s},\quad \%OS \approx 37.23\%$$

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Kararlılık ve Routh-Hurwitz]]

**İlgili:** [[05 Kök Yer Eğrisi ve Kompansasyon|MST&B - KYE]]
