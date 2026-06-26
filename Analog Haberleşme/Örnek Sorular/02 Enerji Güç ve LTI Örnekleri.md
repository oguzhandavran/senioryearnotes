---
tags: [analog-haberleşme, enerji, güç, lti, konvülüsyon, fourier, örnek-sorular]
---

# 02 — Enerji, Güç ve LTI Sistem Örnekleri

← [[../AH Ana Sayfa]] | Teori: [[../Konu Anlatımları/04 Güç Enerji ve LTI Sistemler|04 Güç Enerji ve LTI Sistemler]]

---

## Örnek 1 — $x(t) = e^{-3|t|}$ Fourier Dönüşümü

**Soru:** $x(t) = e^{-3|t|}$ işaretinin Fourier dönüşümünü bulun ve enerji/güç sınıfını belirleyin.

> [!note]- Semboller
> - $|t|$: mutlak değer → sinyal çift fonksiyon; $t<0$'da $e^{3t}$, $t>0$'da $e^{-3t}$ olarak ikiye bölünür
> - $X(f)$: Fourier dönüşümü; çift gerçek sinyal → $X(f)$ gerçek ve çift
> - **Enerji işareti**: $E=\int|x(t)|^2dt<\infty$ (sönen sinyaller); **güç işareti**: $E=\infty$ ama $P<\infty$ (kalıcı sinyaller)
> - Parseval: $E=\int|x(t)|^2dt=\int|X(f)|^2df$
> - Eşlenik çarpım: $(3-j2\pi f)(3+j2\pi f)=9+4\pi^2f^2$ (paydayı gerçekleştirir)

**Çözüm:**

Mutlak değer nedeniyle iki parçaya böl:

$$X(f) = \int_{-\infty}^{0} e^{3t}\,e^{-j2\pi ft}\,dt + \int_{0}^{\infty} e^{-3t}\,e^{-j2\pi ft}\,dt$$

**Sol parça** ($t \leq 0$: $e^{3t} \cdot e^{-j2\pi ft} = e^{(3-j2\pi f)t}$):

$$\int_{-\infty}^{0} e^{(3-j2\pi f)t}\,dt = \frac{e^{(3-j2\pi f)t}}{3-j2\pi f}\Bigg|_{-\infty}^{0} = \frac{1}{3-j2\pi f}$$

**Sağ parça** ($t \geq 0$: $e^{-3t} \cdot e^{-j2\pi ft} = e^{(-3-j2\pi f)t}$):

$$\int_{0}^{\infty} e^{(-3-j2\pi f)t}\,dt = \frac{e^{(-3-j2\pi f)t}}{-3-j2\pi f}\Bigg|_{0}^{\infty} = \frac{1}{3+j2\pi f}$$

**Toplam:**

$$X(f) = \frac{1}{3-j2\pi f} + \frac{1}{3+j2\pi f} = \frac{(3+j2\pi f)+(3-j2\pi f)}{9+(2\pi f)^2}$$

$$\boxed{X(f) = \frac{6}{9+4\pi^2 f^2}}$$

**Enerji/Güç sınıfı:**

$x(t) = e^{-3|t|}$ → $t\to\pm\infty$'da sıfıra gider → **Enerji işareti**

$E = \int_{-\infty}^{\infty} |X(f)|^2\,df = \int_{-\infty}^{\infty} \frac{36}{(9+4\pi^2 f^2)^2}\,df$ *(sonlu)*

> [!sinav] Kritik adım
> $j^2\omega^2 = -\omega^2$ → $\omega = 2\pi f$ → $(j2\pi f)^2 = -4\pi^2 f^2$
> Payda: $(3-j2\pi f)(3+j2\pi f) = 9 + 4\pi^2 f^2$ ← karışık sayı çarpımı!

---

## Örnek 2 — Konvülüsyon: İki Dikdörtgen

**Soru:** $h(t)$: $[1,3]$ aralığında genlik 1; $x(t)$: $[0,2]$ aralığında genlik $\frac{1}{2}$. $y(t) = x(t)*h(t)$'yi hesaplayın.

> [!note]- Semboller
> - $*$: konvolüsyon; $y(t)=\int x(\tau)h(t-\tau)d\tau$
> - $h(t-\tau)$: $\tau$ ekseninde ters çevrilmiş, $t$ kadar kaydırılmış darbe → $[t-3,t-1]$ aralığını kaplar
> - Dikdörtgenlerde $y(t)=(\text{genlik çarpımı})\times(\text{örtüşme uzunluğu})$
> - Eşit genişlik → üçgen; başlangıç/bitiş = kenarların toplamı, tepe = merkezlerin toplamı

**Çözüm:** $h(t-\tau)$'yu kaydırarak örtüşme bölgelerini analiz et:

$h(t-\tau)$: $[t-3, t-1]$ aralığında genlik 1 — $t$ arttıkça sağa kayar.

| Bölge | Koşul | Örtüşme | İntegral | $y(t)$ |
|-------|-------|---------|---------|--------|
| 1 | $t < 1$ | Yok | — | $0$ |
| 2 | $1 \leq t < 3$ | $[0, t-1]$ | $\int_0^{t-1}\frac{1}{2}\,d\tau$ | $\dfrac{t-1}{2}$ |
| 3 | $3 \leq t < 5$ | $[t-3, 2]$ | $\int_{t-3}^{2}\frac{1}{2}\,d\tau$ | $\dfrac{5-t}{2}$ |
| 4 | $t \geq 5$ | Yok | — | $0$ |

$$\boxed{y(t) = \begin{cases} 0 & t<1 \\ \dfrac{t-1}{2} & 1 \leq t < 3 \\ \dfrac{5-t}{2} & 3 \leq t < 5 \\ 0 & t \geq 5 \end{cases}}$$

**Şekil:** Üçgen biçimli çıkış — $t=3$'te tepe $y_{\max} = 1$.

> [!sinav] Kural
> İki dikdörtgen eşit genişlikte → çıkış **üçgen**.
> Başlangıç = $1+0=1$, Bitiş = $3+2=5$, Tepe = $(1+3)/2 + 0 = 3$

---

## Örnek 3 — Dikdörtgen Darbe: İki Ayrık Bölge FT

**Soru:** Aşağıdaki sinyalin Fourier dönüşümünü bulun:

$$x(t) = \begin{cases} A & -3T \leq t \leq -T \\ A & T \leq t \leq 3T \\ 0 & \text{diğer} \end{cases}$$

> [!note]- Semboller
> - $A$: darbe genliği; $T$: zaman ölçeği; sinyal çift (simetrik) → $X(f)$ gerçek
> - İki darbe: merkezler $\pm2T$, genişlik $2T$; her biri sinc verir, kayma $\cos$ çarpanı doğurur
> - Euler: $e^{j\theta}-e^{-j\theta}=2j\sin\theta$; toplam-fark: $\sin a-\sin b=2\cos\tfrac{a+b}{2}\sin\tfrac{a-b}{2}$
> - $\text{sinc}(x)=\sin(\pi x)/(\pi x)$; $\cos(4\pi fT)$: iki darbenin $\pm2T$ konumundan gelen girişim çarpanı

**Çözüm:**

$$X(f) = \int_{-3T}^{-T} A\,e^{-j2\pi ft}\,dt + \int_{T}^{3T} A\,e^{-j2\pi ft}\,dt$$

**Sol parça:**

$$= \frac{A}{-j2\pi f}\Big[e^{-j2\pi ft}\Big]_{-3T}^{-T} = \frac{A}{-j2\pi f}\!\left(e^{j2\pi fT} - e^{j2\pi f3T}\right)$$

**Sağ parça:**

$$= \frac{A}{-j2\pi f}\Big[e^{-j2\pi ft}\Big]_{T}^{3T} = \frac{A}{-j2\pi f}\!\left(e^{-j2\pi f3T} - e^{-j2\pi fT}\right)$$

**Toplamı düzenle** — $\sin a - \sin b = 2\cos\!\frac{a+b}{2}\sin\!\frac{a-b}{2}$ kullan:

$$X(f) = \frac{-A}{\pi f}\!\left(\sin(2\pi fT) - \sin(6\pi fT)\right) = \frac{A}{\pi f}\!\left(\sin(6\pi fT) - \sin(2\pi fT)\right)$$

$\sin a - \sin b = 2\cos\!\!\left(\frac{a+b}{2}\right)\!\sin\!\!\left(\frac{a-b}{2}\right)$ ile:

$$= \frac{A}{\pi f} \cdot 2\cos(4\pi fT)\cdot\sin(2\pi fT)$$

$$\boxed{X(f) = 4AT\,\cos(4\pi fT)\,\text{sinc}(2fT)}$$

**Yorumlama:** sinc zarfının içinde $\cos(4\pi fT)$ modülasyonu → $f_0=1/(2T)$ periyotlu salınım.

---

## Örnek 4 — LTI Sistem ve Enerji Hesabı

**Soru:** Bir işaretin tüm frekanslardaki güç spektral yoğunluğu sabit $S_x(f) = 4$ J/Hz olsun. Bu işaret kesim frekansı $f_0 = 50$ Hz ve kazanç $k = 3$ olan alçak geçiren filtreden geçiriliyor. Çıkış işaretinin enerjisini hesaplayın.

> [!note]- Semboller
> - $S_x(f)$: (enerji) spektral yoğunluk (J/Hz) — birim frekans başına enerji
> - $H(f)$: filtre transfer fonksiyonu; $|H(f)|^2$: güç/enerji kazancı
> - Alçak geçiren: $|f|\le f_0$ → $k$ kazanç, $|f|>f_0$ → 0 (bant dışını bloke eder)
> - Çıkış: $S_y(f)=|H(f)|^2S_x(f)$; toplam enerji $E_y=\int S_y(f)\,df$ (yalnız geçen bantta)

**Çözüm:**

**Adım 1:** Transfer fonksiyonu $H(f) = k = 3$ ($|f| \leq f_0$ için):

$$|H(f)|^2 = k^2 = 9$$

**Adım 2:** Çıkış enerji spektral yoğunluğu:

$$S_y(f) = |H(f)|^2 \cdot S_x(f) = 9 \times 4 = 36 \text{ J/Hz}$$

**Adım 3:** Toplam enerji (filtre sadece $[-50, 50]$ Hz'i geçirir):

$$E_y = \int_{-50}^{50} S_y(f)\,df = 36 \times 100 = \boxed{3600 \text{ J}}$$

> [!sinav] Dikkat
> $S_x(f) = 4$ J/Hz → **enerji** spektral yoğunluğu (W/Hz değil)
> Toplam enerji $= S_y \times \text{bant genişliği} = 36 \times (50-(-50)) = 3600$ J

**Not:** Alçak geçiren filtrenin bant dışındaki frekansları bloke ettiğini unutma. Eğer bant geçiren filtre olsaydı $[f_1, f_2]$ aralığında integral alınırdı.

---

## Örnek 5 — $x(t) = \cos(\omega_0 t)$ Güç mü Enerji mi?

**Soru:** $x(t) = \cos(\omega_0 t)$ işaretini sınıflandırın.

> [!note]- Semboller
> - $\omega_0=2\pi f_0$: açısal frekans (rad/s); $\cos$ sonsuza dek sürer → enerjisi $\infty$
> - $E=\int|x|^2dt$: enerji; $P=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}|x|^2dt$: ortalama güç
> - Trig özdeşlik: $\cos^2x=\tfrac{1+\cos2x}{2}$ → ortalaması $\tfrac12$ (salınım terimi uzun ortalama da sıfır)
> - Genel kural: genlik $A$ sinüzoid → $P=A^2/2$ (güç işareti); sönen üstel → enerji işareti

**Çözüm:**

**Enerji kontrolü:**

$$E = \int_{-\infty}^{\infty} \cos^2(\omega_0 t)\,dt = \infty \quad \text{→ enerji işareti değil}$$

**Güç hesabı** ($\cos^2 x = \frac{1+\cos 2x}{2}$):

$$P = \lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}\cos^2(\omega_0 t)\,dt = \lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}\frac{1+\cos(2\omega_0 t)}{2}\,dt$$

$$= \frac{1}{2} + \underbrace{\lim_{T\to\infty}\frac{1}{T}\cdot\frac{\sin(\omega_0 T)}{2\omega_0}}_{0} = \boxed{P = \frac{1}{2}}$$

**Sonuç:** $P = 1/2 < \infty$ → **Güç işareti**

> [!sinav] Ezbere
> Sin ve cos → her zaman **güç** işareti. $P = A^2/2$
> Üstel bozunan ($e^{-at}u(t)$) → **enerji** işareti

---

> [!sinav] Bu Sayfadan Çıkarılacaklar
> 1. $e^{-a|t|} \leftrightarrow \dfrac{2a}{a^2+4\pi^2f^2}$ — ezbere!
> 2. Konvülüsyon bölgelerini doğru tespit et: $h(t-\tau)$ hangi $\tau$ aralığında $x(\tau)$ ile örtüşür?
> 3. Filtreden geçen enerji: $E_y = \int |H(f)|^2 S_x(f)\,df$ — sadece filtre bandında sıfır dışı
> 4. $S(f)$ özellikleri: $S(f)\geq 0$, $S(f)=S(-f)$, $E=\int S(f)\,df$
