---
tags: [ss, sinyal, örnek-sorular]
---

# 01 — Sinyal Örnekleri

← [[SS Ana Sayfa]]  |  Teori: [[../Konu Anlatımları/01 Sinyal Sınıflandırması]]

---

## Örnek 1 — DT Sinyal Tam Özellik Analizi
*(Arş. Gör. Ecmel TERZİ)*

> [!example] Problem
> **Verilen:** $x[n]$ yalnızca $n \in \{-2,-1,0,1,2,5\}$'te sıfırdan farklı, değerleri $\{1,2,3\}$ kümesinden.
>
> **İstenen:** Sinyalin tüm temel özelliklerini (zaman/genlik türü, sınırlılık, periyodiklik, simetri, enerji/güç) sınıflandır.

> [!note]- Semboller
> - $x[n]$: ayrık zamanlı sinyal; $n$: tam sayı indeks
> - DT: ayrık zamanlı (discrete-time); CT: sürekli zamanlı
> - $E_\infty=\sum_n|x[n]|^2$: toplam enerji; $P$: ortalama güç
> - Enerji sinyali: $0<E<\infty$ (ve $P=0$); periyodik destek sonlu → aperiyodik
> - $u[n]$: birim basamak; $\delta[n]$: birim dürtü (impuls)

| Özellik | Test | Sonuç |
|---------|------|-------|
| Zaman türü | $n$ tam sayı indeks | **Ayrık zamanlı (DT)** |
| Genlik türü | Değerler tam sayılar | **Ayrık değer → Sayısal** |
| Sınırlılık | $|x[n]| \leq 3 < \infty$ | **Sınırlı** |
| Periyodiklik | Sonlu destek → $x[n] \neq x[n+N]$ | **Aperiyodik** |
| Simetri | $x[5] \neq x[-5]$ | **Çift değil** |
| Enerji | $E = \sum|x[n]|^2 = 13 < \infty$ | **Enerji sinyali**, $P = 0$ |

Enerji hesabı:
$$E_\infty = \sum_{n \in \{-2,-1,0,1,2,5\}} |x[n]|^2 = 13$$

**Dikdörtgen pencere gösterimi:**
$$y[n] = u[n-1] - u[n-4] = \begin{cases}1 & 1 \leq n \leq 3 \\ 0 & \text{diğer}\end{cases}$$

---

## Örnek 2 — CT Sinyal Tam Özellik Analizi
*(Arş. Gör. Ecmel TERZİ)*

> [!example] Problem
> **Verilen:** $x(t)$ sürekli, sonlu destekli ($t\in(-2,6)$), genlik aralığı $(-2,5)$.
>
> **İstenen:** Temel sinyal özelliklerini sınıflandır (CT/analog, sınırlılık, simetri, periyodiklik, enerji).

> [!note]- Semboller
> - $x(t)$: sürekli zamanlı sinyal; $t\in\mathbb{R}$: gerçel zaman
> - CT/Analog: sürekli zaman + sürekli genlik
> - Sınırlı: $|x(t)|\le M<\infty$; sonlu destek → aperiyodik
> - $E=\int|x(t)|^2dt$: enerji; $0<E<\infty$ → enerji sinyali

| Özellik | Test | Sonuç |
|---------|------|-------|
| Zaman türü | $t \in \mathbb{R}$ | **Sürekli zamanlı (CT)** |
| Genlik türü | Sürekli aralık | **Sürekli değer → Analog** |
| Sınırlılık | $|x(t)| \leq 5 < \infty$ | **Sınırlı** |
| Simetri | $x(t) \neq x(-t)$ | **Asimetrik** |
| Periyodiklik | Sonlu destek | **Aperiyodik** |
| Enerji | $\int_{-2}^{6} |x(t)|^2\,dt < \infty$ | **Enerji sinyali** |

---

## Örnek 3 — Delta Fonksiyonu ile Örnekleme

> [!example] Problem
> **Soru:** $z[n] = 2\delta[n] + \delta[n-2] + 2\delta[n-3]$ için $w[n]=z[n]\cdot\delta[n-2]$'yi bul (sızdırma özelliği).

> [!note]- Semboller
> - $\delta[n-k]$: $k$ konumundaki birim dürtü (sadece $n=k$'da 1)
> - Sızdırma (sifting): $z[n]\cdot\delta[n-k_0]=z[k_0]\,\delta[n-k_0]$ — sinyalin $k_0$'daki değerini "seçer"
> - $z[k_0]$: $z$ sinyalinin $n=k_0$'daki değeri

Herhangi bir ayrık sinyal delta dizisi cinsinden:
$$z[n] = \sum_{k=-\infty}^{\infty} z[k]\,\delta[n-k]$$

**Sızdırma (sifting) özelliği:** $z[n] \cdot \delta[n-k_0] = z[k_0]\cdot\delta[n-k_0]$

**Soru:** $z[n] = 2\delta[n] + \delta[n-2] + 2\delta[n-3]$ için $w[n] = z[n]\cdot\delta[n-2]$ bul.

**Çözüm:**
$$w[n] = z[2]\cdot\delta[n-2] = 1\cdot\delta[n-2] = \delta[n-2]$$

---

## Örnek 4 — DT Konvolüsyon (Problem 5)
*(Arş. Gör. Ecmel TERZİ)*

> [!example] Problem
> **Verilen:** $x[n] = \delta[n] + 2\delta[n-1] - \delta[n-3]$, $h[n] = 2\delta[n+1] + 2\delta[n-1]$.
>
> **İstenen:** $y[n]=x[n]*h[n]$ konvolüsyonunu süperpozisyon ile bul.

> [!note]- Semboller
> - $x[n]$: giriş sinyali; $h[n]$: dürtü yanıtı; $y[n]=x*h$: çıkış
> - $\delta[n-k]$: $k$'da dürtü; $\delta[n+1]$: $n=-1$'de dürtü (sola kaymış)
> - Süperpozisyon kuralı: $x[n]=\sum_k a_k\delta[n-n_k]$ ise $y[n]=\sum_k a_k\,h[n-n_k]$
> - Her $h[n-n_k]$ = $h[n]$'in $n_k$ kadar sağa kaydırılmışı

**Çözüm** (süperpozisyon ile):

$$y[n] = 1\cdot h[n] + 2\cdot h[n-1] + (-1)\cdot h[n-3]$$

Her terimi hesapla:
$$h[n] = 2\delta[n+1] + 2\delta[n-1]$$
$$2h[n-1] = 4\delta[n] + 4\delta[n-2]$$
$$-h[n-3] = -2\delta[n-2] - 2\delta[n-4]$$

Topla:
$$\boxed{y[n] = 2\delta[n+1] + 4\delta[n] + 2\delta[n-1] + 2\delta[n-2] - 2\delta[n-4]}$$

| $n$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|-----|------|-----|-----|-----|-----|-----|
| $y[n]$ | $2$ | $4$ | $2$ | $2$ | $0$ | $-2$ |

> [!sinav] Kural
> $x[n] = \sum_k a_k\,\delta[n-n_k]$ ise $y[n] = \sum_k a_k\,h[n-n_k]$

---

## Örnek 5 — CT Konvolüsyon: Üçgen × Dikdörtgen (Problem 4)
*(Arş. Gör. Ecmel TERZİ)*

> [!example] Problem
> **Verilen:** $x(t)=\begin{cases}t+1,&0\le t\le1\\ 2-t,&1<t\le2\\0,&\text{diğer}\end{cases}$, $\;h(t)=u(t+2)-u(t-5)$.
>
> **İstenen:** $y(t)=x(t)*h(t)$ konvolüsyonunu tüm bölgelerde adım adım hesapla.

> [!note]- Semboller
> - $x(t)$: parçalı sinyal (toplam alanı $A=\int x\,d\tau$); $h(t)$: $[-2,5]$ aralığında 1 olan genişliği 7 dikdörtgen pencere
> - $u(t)$: birim basamak; $u(t+2)-u(t-5)$ = $-2$'de başlayıp $5$'te biten kapı
> - $\tau$: konvolüsyon (kayan) değişkeni; $h(t-\tau)$: pencerenin yansıyıp $t$ kadar kaymış hâli
> - Örtüşme: $h(t-\tau)=1 \Leftrightarrow t-5\le\tau\le t+2$; $x(\tau)\ne0 \Leftrightarrow 0\le\tau\le2$
> - $y(t)=\displaystyle\int_{\max(0,\,t-5)}^{\min(2,\,t+2)} x(\tau)\,d\tau$

**Adım 1 — Sinyalin alanı (düz-tepe değeri).** Pencere $x$'i tamamen örttüğünde çıkış sabit kalır ve $x$'in toplam alanına eşittir:

$$A=\int_0^1(\tau+1)\,d\tau+\int_1^2(2-\tau)\,d\tau=\underbrace{1{,}5}_{[\tau^2/2+\tau]_0^1}+\underbrace{0{,}5}_{[2\tau-\tau^2/2]_1^2}=2$$

**Adım 2 — İntegral sınırları.** $y(t)=\int_{\max(0,t-5)}^{\min(2,t+2)}x(\tau)\,d\tau$; örtüşme yalnızca $-2<t<7$ için var.

**Adım 3 — Bölge bölge çözüm:**

| Bölge | Sınırlar | $y(t)$ |
|-------|----------|--------|
| $t<-2$ | örtüşme yok | $0$ |
| $-2\le t<-1$ | $0 \to t+2\ (\le1)$ | $\displaystyle\int_0^{t+2}(\tau+1)d\tau=\frac{(t+2)^2}{2}+(t+2)$ |
| $-1\le t<0$ | $0 \to t+2\ (\in[1,2])$ | $\displaystyle 2(t+2)-\frac{(t+2)^2}{2}$ |
| $0\le t<5$ | $0 \to 2$ (tam örtüşme) | $A=2$ (sabit, düz tepe) |
| $5\le t<6$ | $t-5\ (\le1) \to 2$ | $\displaystyle 2-\frac{(t-5)^2}{2}-(t-5)$ |
| $6\le t<7$ | $t-5\ (\in[1,2]) \to 2$ | $\displaystyle 2-\Big[2(t-5)-\frac{(t-5)^2}{2}\Big]$ |
| $t\ge7$ | örtüşme yok | $0$ |

**Kontrol:** Düz tepe $y=A=2$ (eski nottaki $3/2$ **hatalıydı**; $x$'in gerçek alanı 2'dir). Çıkış sürekli: $t=0$'da üst satır $2(2)-2=2$ ✓; $t=5$'te alt satır $2-0-0=2$ ✓.
