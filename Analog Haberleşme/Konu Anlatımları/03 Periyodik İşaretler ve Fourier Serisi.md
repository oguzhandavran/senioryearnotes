---
tags: [analog-haberleşme, fourier-serisi, periyodik, kare-dalga, sinc, konu-anlatımı]
---

# 03 — Periyodik İşaretler ve Fourier Serisi

← [[../AH Ana Sayfa]] | Önceki: [[02 Fourier Analizi]] | Sonraki: [[04 Güç Enerji ve LTI Sistemler]]

---

## Periyodik İşaret Tanımı

> [!tanim] Periyodik İşaret
> $x(t) = x(t + T_0)$ koşulunu sağlayan işaret.
> - $T_0$: temel periyot (s)
> - $f_0 = 1/T_0$: temel frekans (Hz)
> - $\omega_0 = 2\pi f_0 = 2\pi/T_0$: temel açısal frekans (rad/s)

---

## Fourier Serisi

> [!tanim] Fourier Serisi (Karmaşık Üstel Form)
> Dirichlet koşullarını sağlayan periyodik işaret:
> $$x(t) = \sum_{n=-\infty}^{\infty} c_n\,e^{jn\omega_0 t}$$
> Fourier serisi katsayıları:
> $$\boxed{c_n = \frac{1}{T_0}\int_0^{T_0} x(t)\,e^{-jn\omega_0 t}\,dt}$$

### Dirichlet Koşulları

| # | Koşul |
|---|-------|
| 1 | $\int_0^{T_0}\|x(t)\|\,dt < \infty$ (mutlak integrallenebilir) |
| 2 | Bir periyotta sonlu sayıda min/maks noktası |
| 3 | Bir periyotta sonlu sayıda süreksizlik noktası |

### Katsayı Özellikleri

| Özellik | İfade |
|---------|-------|
| Karmaşık form | $c_n = a_n - jb_n$ |
| Genlik | $\|c_n\| = \sqrt{a_n^2 + b_n^2}$ |
| Faz | $\theta_n = \arctan(b_n/a_n)$ |
| Genlik simetrisi | $\|c_n\| = \|c_{-n}\|$ |
| Faz simetrisi | $\theta_n = -\theta_{-n}$ |

**Özel durumlar:**
- $c_0 = \dfrac{1}{T_0}\int_0^{T_0}x(t)\,dt$ → işaretin ortalaması (DC değer)
- $x(t)$ gerçekse: $c_{-n} = c_n^*$ (eşlenmiş karmaşık)

---

## Kare Dalganın Fourier Serisi

Genliği $A$, genişliği $\tau$, periyodu $T_0$ olan simetrik kare dalga:

$$c_n = \frac{1}{T_0}\int_{-\tau/2}^{\tau/2} A\,e^{-jn\omega_0 t}\,dt = \frac{A\tau}{T_0}\,\text{sinc}\!\left(\frac{n\tau}{T_0}\right)$$

$$\boxed{c_n = \frac{A\tau}{T_0}\,\text{sinc}\!\left(\frac{n\tau}{T_0}\right)}$$

**Yorum:**
- $n=0$: $c_0 = A\tau/T_0$ (ortalama = doluluk oranı × genlik)
- sinc sıfırları: $n\tau/T_0$ tam sayı olduğunda → harmonikler kaybolur
- Düşük harmonikler güçlü, yüksek harmonikler zayıf

---

## Sinc Fonksiyonu

$$\boxed{\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}, \qquad \text{sinc}(0) = 1}$$

**Özellikleri:**
- $x = \pm 1, \pm 2, \pm 3, \ldots$ noktalarında sıfır
- Ana lob: $-1 < x < 1$ aralığında, yüksekliği 1
- Yan loblar giderek azalır
- Zaman alanında darbe genişledikçe frekans alanında ana lob **daralır** (belirsizlik ilkesi)

---

## Gibbs Fenomeni

Kare dalganın $N$ harmonikle yaklaşımı, süreksizlik noktasında **≈ %9 aşım** yapar.

- $N$ arttıkça aşım yeri daralır ama tamamen kaybolmaz
- Fiziksel sebep: süreksiz değişim → sonsuz bant genişliği gerektirir

---

## Periyodik İşaretin Fourier Dönüşümü

Periyodik işaret için standart FD integrali yakınsamaz. Fourier serisi katsayıları üzerinden:

$$\boxed{X(f) = \sum_{n=-\infty}^{\infty} c_n\,\delta\!\left(f - \frac{n}{T_0}\right)}$$

**Yorum:**
- Spektrum **çizgisel** (ayrık): yalnızca $f = n/T_0$ frekanslarında impuls
- $c_n$ her impulssun **ağırlığı** (genlik ve faz)
- Sürekli işaretler için $|X(f)|$ sürekli bir eğridir; periyodik işaretler için impuls dizisi

---

## Örnek — 4 Bileşenli Periyodik Sinyal

$$x(t) = 1 + 3\cos(2\pi \cdot 16t - \pi/6) + \sin(60\pi t) + 5\cos(70\pi t)$$

$\sin(\omega t) = \cos(\omega t - \pi/2)$ dönüşümünü uygulayarak:

| Terim | $f$ (Hz) | $\|c_n\|$ | $\theta_n$ |
|-------|----------|-----------|------------|
| $1$ | $0$ | $1$ | $0$ |
| $3\cos(2\pi \cdot 16t - \pi/6)$ | $\pm 16$ | $3/2$ | $\mp\pi/6$ |
| $\sin(60\pi t)$ | $\pm 30$ | $1/2$ | $-\pi/2$ / $+\pi/2$ |
| $5\cos(70\pi t)$ | $\pm 35$ | $5/2$ | $0$ |

---

## Özet: Periyodik vs. Periyodik Olmayan

| Özellik | Periyodik $x(t)$ | Periyodik Olmayan $x(t)$ |
|---------|-----------------|--------------------------|
| FT | İmpuls dizisi $\sum c_n\delta(f-n/T_0)$ | Sürekli $X(f)$ |
| Araç | Fourier Serisi | Fourier Dönüşümü |
| Enerji | $E = \infty$ (güç işareti) | $E < \infty$ (enerji işareti) |
| Spektrum | Çizgisel (ayrık) | Sürekli |

---

> [!sinav] Sınav İpucu
> - Periyodik işaret → önce $c_n$ hesapla, sonra $X(f) = \sum c_n\delta(f-n/T_0)$ yaz
> - Kare dalga $c_n$: $\dfrac{A\tau}{T_0}\text{sinc}(n\tau/T_0)$ — sinc sıfırları hangi harmonikleri sıfırlar?
> - $c_0$ = DC değeri = zaman ortalaması
> - Gerçek işarette $c_{-n} = c_n^*$ → genlik çift, faz tek
