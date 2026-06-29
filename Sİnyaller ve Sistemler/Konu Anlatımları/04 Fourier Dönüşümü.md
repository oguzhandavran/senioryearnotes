---
tags: [ss, fourier-dönüşümü, ctft, konu-anlatımı]
---

# 04 — Fourier Dönüşümü (CTFT)

← [[SS Ana Sayfa]]  |  Örnekler: [[../Örnek Sorular/04 Fourier Dönüşümü Örnekleri]]

## Özet

> Periyodik olmayan sinyalleri de frekans domenine taşı. CTFT: $x(t) \leftrightarrow X(j\omega)$.
> **Kapsam: 4.1–4.5 (Çarpma Özelliğine kadar)**

> [!abstract] 🔰 Sıfırdan: Kısaltmalar, Semboller, Sezgi
> **Ana fikir:** Fourier serisi sadece **periyodik** sinyaller içindi. Periyodik olmayan bir sinyali "periyodu sonsuz" kabul edersek ($T\to\infty$), harmonikler birbirine yaklaşıp **sürekli bir frekans ekseni** olur. İşte Fourier dönüşümü budur: sinyalin hangi frekansları ne kadar içerdiğinin sürekli haritası.
>
> | Kısaltma / sembol | Açılım (İng.) | Türkçe / anlamı |
> |---|---|---|
> | **CTFT** | Continuous-Time Fourier Transform | **Sürekli-zaman Fourier dönüşümü** |
> | **FT** | Fourier Transform | Fourier dönüşümü |
> | $X(j\omega)$ | spectrum | sinyalin **frekans içeriği** (genelde karmaşık) |
> | $\lvert X(j\omega)\rvert$ | magnitude spectrum | **genlik spektrumu** |
> | $\angle X(j\omega)$ | phase spectrum | **faz spektrumu** |
> | $\omega$ | angular frequency | **açısal frekans** (rad/s), $\omega=2\pi f$ |
> | $\mathcal{F},\ \mathcal{F}^{-1}$ | (inverse) transform | (ters) dönüşüm operatörü |
>
> **Analiz denklemi nereden? ($X(j\omega)=\int x(t)e^{-j\omega t}dt$)** $e^{-j\omega t}$ çarpanı, sinyali $\omega$ frekanslı bir "prob" ile karşılaştırır; integral o frekansın sinyaldeki toplam katkısını ölçer. **Sentez** ($x=\frac1{2\pi}\int X e^{j\omega t}d\omega$) ise tüm frekansları geri toplayıp sinyali yeniden kurar.
>
> **Sınav refleksi:** İntegral almadan önce **tabloya** bak ($e^{-at}u(t)\to\frac1{a+j\omega}$ vb.) + **özellikleri** uygula (kaydırma → $e^{-j\omega t_0}$, türev → $j\omega$). İntegrali ancak tablo yetmezse al (örn. sola uzanan $u(1-t)$ sinyali).

---

## 1. CTFT — Analiz ve Sentez (4.1)

$$\boxed{X(j\omega) = \int_{-\infty}^{\infty} x(t)\, e^{-j\omega t}\, dt}$$

$$\boxed{x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega)\, e^{j\omega t}\, d\omega}$$

### Temel CTFT Çiftleri

| $x(t)$ | $X(j\omega)$ | Koşul |
|--------|-------------|-------|
| $\delta(t)$ | $1$ | |
| $1$ | $2\pi\delta(\omega)$ | |
| $e^{-at}u(t)$ | $\dfrac{1}{a+j\omega}$ | $a > 0$ |
| $e^{-a\|t\|}$ | $\dfrac{2a}{a^2+\omega^2}$ | $a > 0$ |
| $u(t)$ | $\pi\delta(\omega) + \dfrac{1}{j\omega}$ | |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ | |
| $\sin(\omega_0 t)$ | $\dfrac{\pi}{j}[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ | |
| $\text{rect}(t/\tau)$ | $\tau \operatorname{sinc}(\omega\tau/2)$ | |
| $t^n e^{-at}u(t)$ | $\dfrac{n!}{(a+j\omega)^{n+1}}$ | $a > 0$ |

---

## 2. Periyodik Sinyallerin CTFT'si (4.2)

Fourier serisi katsayıları $a_k$ olan periyodik $x(t)$ için:

$$\boxed{X(j\omega) = 2\pi \sum_{k=-\infty}^{\infty} a_k\, \delta(\omega - k\omega_0)}$$

> İmpuls dizisi — her harmonik $k\omega_0$'da ağırlıklı delta.

---

## 3. CTFT Özellikleri (4.3)

| Özellik | İşlem | CTFT |
|---------|-------|------|
| Doğrusallik | $ax+by$ | $aX+bY$ |
| Zaman kayması | $x(t-t_0)$ | $e^{-j\omega t_0}X(j\omega)$ |
| Frekans kayması | $e^{j\omega_0 t}x(t)$ | $X(j(\omega-\omega_0))$ |
| Eşlenik simetri | $x^*(t)$ | $X^*(-j\omega)$ |
| Zaman ölçekleme | $x(at)$ | $\dfrac{1}{\|a\|}X(j\omega/a)$ |
| Zaman ters çevirme | $x(-t)$ | $X(-j\omega)$ |
| Türev | $\dfrac{dx}{dt}$ | $j\omega X(j\omega)$ |
| İntegral | $\int_{-\infty}^t x\,d\tau$ | $\dfrac{X(j\omega)}{j\omega} + \pi X(0)\delta(\omega)$ |
| **Dualite** | $X(t)$ | $2\pi x(-\omega)$ |
| **Parseval** | $\int\|x\|^2 dt$ | $\dfrac{1}{2\pi}\int\|X\|^2 d\omega$ |

### Simetri (Gerçek Sinyaller)

| Sinyal | $X(j\omega)$ |
|--------|-------------|
| $x(t)$ gerçek | $X(-j\omega) = X^*(j\omega)$ |
| $x(t)$ gerçek + çift | $X(j\omega)$ gerçek ve çift |
| $x(t)$ gerçek + tek | $X(j\omega)$ saf sanal ve tek |

---

## 4. Evrişim Özelliği (4.4)

$$\boxed{x(t)*h(t) \;\longleftrightarrow\; X(j\omega)\cdot H(j\omega)}$$

Zaman domeninde evrişim → frekans domeninde **çarpım**.

Filtre tasarımı: $H(j\omega) = Y(j\omega)/X(j\omega)$

---

## 5. Çarpma Özelliği (4.5)

$$\boxed{x(t)\cdot h(t) \;\longleftrightarrow\; \frac{1}{2\pi}\,X(j\omega) * H(j\omega)}$$

Zaman domeninde çarpım → frekans domeninde **evrişim** (÷ $2\pi$).

> [!sinav] Evrişim ↔ Çarpma Dualitesi
> | Zaman | Frekans |
> |-------|---------|
> | $x * h$ (evrişim) | $X \cdot H$ (çarpım) |
> | $x \cdot h$ (çarpım) | $\frac{1}{2\pi} X * H$ (evrişim) |
> 
> Çarpma özelliği → **frekans seçici süzgeçlemenin** teorik temelidir.

---

## Bağlantılı Notlar

- [[../Örnek Sorular/04 Fourier Dönüşümü Örnekleri|Örnek Sorular — Fourier Dönüşümü]]
- [[03 Fourier Serisi]]
- [[02 LTI Sistemler ve Konvolüsyon]]
