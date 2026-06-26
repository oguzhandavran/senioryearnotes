---
tags: [otomatik-kontrol, kararlı-hal-hatası, hata-sabitleri, tip-sistemi, örnek-sorular]
---

# 03 — Kararlı Hal Hata Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/03 Kararlı Hal Hataları]]

---

## Örnek 1 — Tip 1 Sistem (Görünüşte Tip 0)

> [!note]- Semboller
> - **Sistem tipi**: paydadaki orijin kutbu sayısı ($s^N$ → Tip $N$)
> - $K_p=\lim_{s\to0}G(s)$: konum hata sabiti (basamak); $K_v=\lim_{s\to0}sG(s)$: hız hata sabiti (rampa); $K_a=\lim_{s\to0}s^2G(s)$: ivme hata sabiti (parabol)
> - Basamak hatası $=\dfrac{A}{1+K_p}$; rampa hatası $=\dfrac{A}{K_v}$; parabol hatası $=\dfrac{A}{K_a}$ ($A$: giriş genliği)

$$G(s) = \frac{120 \cdot 2}{(s)(s+3)(s+4)} \quad \text{[Tip 1!]}$$

**Not:** Paydada $s$ var → Tip 1

$K_p = \lim_{s\to 0} G(s) = \infty$ → Basamak hatası = 0

$K_v = \lim_{s\to 0} s\cdot G(s) = \frac{120\cdot 2}{3\cdot 4} = 20$

- Basamak $5u(t)$: $e(\infty) = 0$
- Rampa $5tu(t)$: $e(\infty) = 5/K_v = 5/20 = \mathbf{0.25}$
- Parabol $5t^2 u(t)$: $e(\infty) = \infty$

---

## Örnek 2 — Hata Şartı ile K Tasarımı

> [!note]- Semboller
> - $K$: tasarlanacak kazanç; $K_v$: hız hata sabiti
> - Rampa girişine kalıcı hata $e(\infty)=\dfrac{1}{K_v}$; verilen üst sınırı sağlamak için $K$ alt sınırı bulunur
> - $\lim_{s\to0}sG(s)$: $s$ ile çarpınca orijindeki bir kutup sadeleşir, kalan paydanın sabit terimleri çarpılır

$$G(s) = \frac{K(5)}{s(s+6)(s+7)(s+8)} \quad \text{[Tip 1]}$$

$K_v = \lim_{s\to 0}s\cdot G(s) = \frac{5K}{6\cdot 7\cdot 8} = \frac{5K}{336}$

Şart: $e(\infty) = \dfrac{1}{K_v} = \dfrac{336}{5K} \leq 0.1$

$$K \geq \frac{336}{5 \cdot 0.1} = \frac{336}{0.5} = 672$$

$$\boxed{K = 672}$$

---

## Örnek 3 — Kararlılık ile Hata Şartı Çelişkisi

> [!note]- Semboller
> - İki kısıt aynı anda: **hata** (küçük $e_{ss}$ → büyük $K$) ve **kararlılık** (Routh → küçük $K$)
> - $e_{ss,\text{step}}=\dfrac{1}{1+K_p}$ (Tip 0); $e_{ss,\text{ramp}}=\dfrac{1}{K_v}$ (Tip 1)
> - İki aralık kesişmiyorsa tek bir $K$ ile her iki şart sağlanamaz → tasarım imkânsız (kompansatör gerekir)

**Soru 1:** $G(s) = \dfrac{K}{s^3+10s^2+25s+10}$ (Tip 0)

$K_p = \lim_{s\to 0}G(s) = \dfrac{K}{10}$

$e_{ss,\text{step}} = \dfrac{1}{1+K_p} = \dfrac{10}{10+K}$

Hata < 0.01 için: $K > 990$, ama kararlılık için $K < 240$. **Çelişki — mümkün değil!**

---

**Soru 2:** $G(s) = \dfrac{K}{s^4+7s^3+11s^2+7s}$ (Tip 1, paydada $s$ var)

$K_p = \infty \implies e_{ss,\text{step}} = 0$

$K_v = \lim_{s\to 0}s\cdot G(s) = \dfrac{K}{7}$

$e_{ss,\text{ramp}} = \dfrac{7}{K}$

Hata < 0.1 için: $K > 70$, ama kararlılık için $K < 10$. **Çelişki — mümkün değil!**

---

## Örnek 4 — Tip 0 Sistem, Üç Giriş Tipi (Doç.Dr. Haluk Görgün Slayt 25)

> [!note]- Semboller
> - Tip 0 → $K_p$ sonlu, $K_v=K_a=0$
> - $u(t)$: basamak; $t\,u(t)$: rampa; $t^2u(t)$: parabol giriş (parabol için $\dfrac{2}{K_a}$, $5t^2$ için $\dfrac{10}{K_a}$)
> - $K_v=0$ veya $K_a=0$ → ilgili hata $\infty$ (sistem o girişi takip edemez)

$$G(s) = \frac{120(s+2)}{(s+3)(s+4)} \quad \text{[Tip 0]}$$

**Tip 0** — paydada $s$ yok. $K_p = \lim_{s\to 0}G(s) = \frac{120\cdot 2}{3\cdot 4} = 20$

| Giriş | $e(\infty)$ formülü | Sonuç |
|-------|---------------------|-------|
| $5u(t)$ | $\dfrac{5}{1+K_p} = \dfrac{5}{21}$ | $\mathbf{5/21}$ |
| $5t\,u(t)$ | $\dfrac{5}{K_v},\; K_v = \lim sG = 0$ | $\mathbf{\infty}$ |
| $5t^2u(t)$ | $\dfrac{10}{K_a},\; K_a = \lim s^2G = 0$ | $\mathbf{\infty}$ |

> Tip 0 sistemi rampa ve parabol girdilerini takip edemez.

---

## Örnek 5 — Bozucu Etki Sürekli Hal Hatası (Doç.Dr. Haluk Görgün Slayt 37–40)

> [!note]- Semboller
> - $G_1$: kontrolör; $G_2$: sistem (plant); $D(s)$: bozucu (disturbance) giriş; $R(s)$: referans
> - $E(s)$: hata; süperpozisyonla iki bileşen: referanstan $e_R$ ve bozucudan $e_D$
> - Bozucu hatasını küçültmek için: $G_1$ DC kazancını **artır** (büyük döngü kazancı) veya $G_2$ DC kazancını **azalt**
> - $G_2$ orijinde kutuplu ($1/s$ terimi) → $\lim_{s\to0}1/G_2=0$, bozucu reddi iyileşir

**Yapı:** Controller $G_1(s)$, bozucu $D(s)$, Plant $G_2(s)$ — standart geri besleme

$$E(s) = \underbrace{\frac{1}{1+G_1G_2}R(s)}_{e_R} \;-\; \underbrace{\frac{G_2}{1+G_1G_2}D(s)}_{e_D}$$

**Birim basamak bozucu** $D(s) = 1/s$:

$$\boxed{e_D(\infty) = -\frac{1}{\displaystyle\lim_{s\to 0}\frac{1}{G_2(s)} + \lim_{s\to 0}G_1(s)}}$$

$G_1$ DC kazancını **artır** veya $G_2$ DC kazancını **azalt** → $|e_D|$ küçülür.

**Sayısal Örnek:** $G_1(s) = 1000$, $G_2(s) = \dfrac{1}{s(s+25)}$

$$e_D(\infty) = -\frac{1}{0 + 1000} = -\frac{1}{1000}$$

> $G_2$ orijinde kutuplu → $\lim 1/G_2 = 0$.

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/03 Kararlı Hal Hataları]]
