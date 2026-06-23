---
tags: [ss, sinyal, örnek-sorular]
---

# 01 — Sinyal Örnekleri

← [[SS Ana Sayfa]]  |  Teori: [[../Konu Anlatımları/01 Sinyal Sınıflandırması]]

---

## Örnek 1 — DT Sinyal Tam Özellik Analizi
*(Arş. Gör. Ecmel TERZİ)*

**Verilen:** $x[n]$ yalnızca $n \in \{-2, -1, 0, 1, 2, 5\}$ noktalarında sıfırdan farklı, değer kümesi $x[n] \in \{1, 2, 3\}$

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

**Verilen:** $x(t)$ sinüzoidal benzeri, $t \in (-2,\, 6)$, $x(t) \in (-2,\, 5)$

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

Herhangi bir ayrık sinyal delta dizisi cinsinden:
$$z[n] = \sum_{k=-\infty}^{\infty} z[k]\,\delta[n-k]$$

**Sızdırma (sifting) özelliği:** $z[n] \cdot \delta[n-k_0] = z[k_0]\cdot\delta[n-k_0]$

**Soru:** $z[n] = 2\delta[n] + \delta[n-2] + 2\delta[n-3]$ için $w[n] = z[n]\cdot\delta[n-2]$ bul.

**Çözüm:**
$$w[n] = z[2]\cdot\delta[n-2] = 1\cdot\delta[n-2] = \delta[n-2]$$

---

## Örnek 4 — DT Konvolüsyon (Problem 5)
*(Arş. Gör. Ecmel TERZİ)*

$$x[n] = \delta[n] + 2\delta[n-1] - \delta[n-3], \qquad h[n] = 2\delta[n+1] + 2\delta[n-1]$$

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

$$x(t) = \begin{cases}t+1, & 0 \leq t \leq 1 \\ 2-t, & 1 < t \leq 2 \\ 0, & \text{diğer}\end{cases}, \qquad h(t) = u(t+2) - u(t-5)$$

$h(t)$: genişliği 7 olan dikdörtgen pencere $[-2,\,5]$.

$h(t-\tau) = 1$ koşulu: $t-5 \leq \tau \leq t+2$ ve $x(\tau) \neq 0$: $0 \leq \tau \leq 2$

| Bölge | $y(t)$ |
|-------|--------|
| $t < -2$ | $0$ |
| $-2 \leq t < 0$ | $\int_0^{t+2}(\tau+1)\,d\tau$ |
| $0 \leq t < 1$ | Yükselen bölge parçalı integral |
| $2 \leq t < 5$ | $\int_0^2 x(\tau)\,d\tau = \frac{3}{2}$ (sabit) |
| $5 \leq t < 7$ | Alçalan integral |
| $t \geq 7$ | $0$ |
