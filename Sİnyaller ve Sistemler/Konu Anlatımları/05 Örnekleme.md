---
tags: [ss, ornekleme, sampling, konu-anlatimi, bolum7]
---

# 05 Örnekleme (Bölüm 7)

← [[SS Ana Sayfa]] | Örnekler: [[../Örnek Sorular/07 Örnekleme Örnekleri|07 Örnekleme Örnekleri]]

> [!warning] Kapsam notu
> Örnekleme (Bölüm 7), **bütünleme kapsamının dışında** görünüyor (sınav: Bölüm 1–4.5; vize/final soruları konvolüsyon + Fourier). Genel kültür/SSİ dersi için tutuldu, yarınki sınava öncelik verme.

> [!abstract] 🔰 Sıfırdan: Kısaltmalar, Semboller, Sezgi
> **Ana fikir:** Sürekli sinyali bilgisayara almak için belirli aralıklarla "örnek" alırız. Eğer yeterince sık örneklersek sinyali **tam** geri kurabiliriz; seyrek örneklersek bilgi karışır (aliasing).
>
> | Kısaltma / sembol | Açılım (İng.) | Türkçe / anlamı |
> |---|---|---|
> | **ZOH** | Zero-Order Hold | **Sıfırcı-dereceden tutma** (örneği bir periyot sabit tut) |
> | **LPF** | Low-Pass Filter | **Alçak geçiren süzgeç** (yeniden kurmada kullanılır) |
> | **C/D, D/C** | Continuous↔Discrete | sürekli↔ayrık dönüştürücü |
> | $T$ | sampling period | **örnekleme periyodu** (örnekler arası süre) |
> | $\omega_s$ | sampling frequency | **örnekleme frekansı** $=2\pi/T$ |
> | $\omega_M$ | max frequency | sinyaldeki **en yüksek frekans** (bant sınırı) |
> | aliasing | — | **örtüşme**: spektrum kopyaları üst üste biner |
>
> **Nyquist neden $\omega_s>2\omega_M$?** Örnekleme, spektrumun $\omega_s$ aralıklarla kopyalarını üretir. Kopyalar üst üste binmesin diye iki komşu kopya arasındaki boşluk ($\omega_s$) sinyalin toplam genişliğinden ($2\omega_M$) büyük olmalı.

---

## 7.1 — İdeal Dürtü-Katar Örneklemesi

Örnekleme sinyali:
$$p(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT)$$

Örneklenmiş sinyal:
$$x_p(t) = x(t)\cdot p(t) = \sum_{n=-\infty}^{\infty} x(nT)\,\delta(t-nT)$$

Fourier dönüşümü:
$$\boxed{X_p(j\omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty} X\!\left(j(\omega - k\omega_s)\right)}, \quad \omega_s = \frac{2\pi}{T}$$

> Örnekleme, orijinal spektrumun $k\omega_s$ aralıklarla **periyodik kopyalarını** oluşturur.

---

## 7.2 — Nyquist-Shannon Örnekleme Teoremi

> [!sinav] Teorem (Ezber!)
> $x(t)$ bant sınırlı: $X(j\omega)=0$ için $|\omega|>\omega_M$.
> **Nyquist koşulu:** $\omega_s > 2\omega_M$ ise $x(t)$ örneklerden tam yeniden oluşturulabilir.

$$\omega_s > 2\omega_M \quad\Leftrightarrow\quad T < \frac{\pi}{\omega_M}$$

**Nyquist hızı:** $\omega_s = 2\omega_M$ (teorik minimum — pratikte biraz fazla alınır)

**Örtüşme (aliasing):** $\omega_s < 2\omega_M$ → kopyalar üst üste → bilgi kaybı, kurtarılamaz!

---

## 7.3 — Yeniden Oluşturma

Nyquist sağlanıyorsa: $x_p(t)$'yi kesim frekansı $\omega_c$ olan ideal alçak geçiş filtresinden geç.

$$H_{LPF}(j\omega) = \begin{cases} T, & |\omega|<\omega_c \\ 0, & |\omega|>\omega_c \end{cases}$$

$\omega_c = \pi/T$ seçilince:

$$\boxed{x_r(t) = \sum_{n=-\infty}^{\infty} x[nT]\,\frac{\sin\!\left[\frac{\pi}{T}(t-nT)\right]}{\frac{\pi}{T}(t-nT)}}$$

---

## 7.4 — Sıfırcı-Dereceden Tutma (ZOH)

Her örnekten sonra değeri bir $T$ süresi sabit tut:

$$H_{ZOH}(j\omega) = \frac{1 - e^{-j\omega T}}{j\omega} = T\,e^{-j\omega T/2}\,\text{sinc}\!\left(\frac{\omega T}{2\pi}\right)$$

ZOH ideal değil — kompansasyon filtresi $1/H_{ZOH}$ gerekir.

---

## 7.5 — Ayrık Zamanlı İşleme (C/D → DT-LTI → D/C)

```
x(t) → [C/D] → x[n] → [DT-LTI H(e^jω)] → y[n] → [D/C] → y(t)
```

Eşdeğer sürekli sistem fonksiyonu:

$$H_{eq}(j\omega) = H\!\left(e^{j\omega T}\right), \quad |\omega| < \frac{\pi}{T}$$

---

## 7.6 — Formüller Özeti

| Büyüklük | Formül |
|----------|--------|
| Örnekleme frekansı | $\omega_s = 2\pi/T$ |
| Nyquist koşulu | $\omega_s > 2\omega_M$ |
| Spektrum kopyaları | $k\omega_s$ aralıkta, $k\in\mathbb{Z}$ |
| İdeal yeniden oluşturma | $H_{LPF}$: kesim $\omega_s/2$, kazanç $T$ |
| ZOH | $H_0 = (1-e^{-j\omega T})/(j\omega)$ |
| İlk değer teoremi | $x(0^+) = \lim_{s\to\infty}sX(s)$ |
| Son değer teoremi | $\lim_{t\to\infty}x(t) = \lim_{s\to 0}sX(s)$ |

---

> [!warning] Sınav Tuzakları
> - Nyquist hızı $2\omega_M$, **koşul** $\omega_s > 2\omega_M$ (eşit olmaz, kesin büyük olmalı)
> - Aliasing = geri dönülmez; sadece $\omega_s$ artırarak önlenir
> - Alçak geçiş filtresi kazancı $T$ olmalı — yoksa ölçekleme hatası
> - ZOH ideal değil: yüksek frekans bozulması yapar
> - Örnekleme periyodu küçüldükçe ($T\downarrow$) kopyalar uzaklaşır → örtüşme azalır

← [[SS Ana Sayfa]] | [[SS Sınav Gecesi]]
