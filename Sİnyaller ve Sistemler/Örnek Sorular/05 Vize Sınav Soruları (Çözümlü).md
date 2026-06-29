---
tags: [ss, vize, sınav-soruları, çözümlü, konvolüsyon, lti]
---

# 05 — Vize Sınav Soruları (Çözümlü · Sıfırdan Öğretici)

← [[SS Ana Sayfa]]  ·  Aynı sorular grafiklerle: [[08 Çalışma Kağıdı — Çözümlü Soru Bankası]]

> Kaynak: `_dataset/Sinyaller Ve Sistemler/SS_Vize.pdf` · resmi çözüm `SS Çalışma Kağıdı 1–2.jpeg`

> [!abstract] Bu sınav neyi ölçüyor? (önce büyük resim)
> Vize tamamen **LTI sistemler + konvolüsyon** üzerine. Üç soru da aynı iskelet: *bir sistem/sinyal ver → özelliklerini söyle → çıkışı $y=x*h$ ile bul*.
>
> | Kısaltma | Açılım (İng. → Tür.) |
> |---|---|
> | **LTI** | Linear Time-Invariant → **Doğrusal & Zamanla-Değişmez** |
> | **CT / DT** | Continuous / Discrete-Time → **Sürekli / Ayrık-zaman** |
> | **BIBO** | Bounded-Input Bounded-Output → **Sınırlı giriş–sınırlı çıkış** (kararlılık) |
> | $h$ | impulse response → **dürtü yanıtı** (girişe $\delta$ verince çıkış) |
> | $*$ | convolution → **konvolüsyon (evrişim)** |
>
> **Nereden geliyor?** Konvolüsyon $y(t)=\int x(\tau)h(t-\tau)d\tau$, "her giriş anını bir $\delta$ kabul edip sistemin $h$ yanıtını üst üste bindirme (süperpozisyon)" fikrinden doğar. Adım adım anlatımı ve tüm grafikler için → [[08 Çalışma Kağıdı — Çözümlü Soru Bankası]].

---

## Soru 1 — Ayrık Zamanlı LTI Sistemi

**Verilen:**
$$x[n] = \delta[n] - \delta[n+1] + 2\delta[n-1]$$
$$y[n] = x[n-1] + x[n] + x[n+1]$$

> [!note]- Semboller
> - $x[n]$: giriş dizisi; $\delta[n-k]$: $k$'da dürtü ($\delta[n+1]$ → $n=-1$'de)
> - $h[n]$: dürtü yanıtı ($x[n]=\delta[n]$ verince çıkış)
> - Nedensellik: $h[n]=0$, $\forall n<0$ olmalı; gelecek değer ($x[n+1]$) kullanımı nedenselliği bozar
> - BIBO kararlılık: $\sum_n|h[n]|<\infty$
> - $y[n]=x*h$: çıkış (konvolüsyon)

---

### 1a — İmpuls Yanıtı ve Sistem Özellikleri (15p)

**İmpuls yanıtı h[n]:**

$x[n] = \delta[n]$ girişi verilince çıkış doğrudan $h[n]$ olur:

$$h[n] = \delta[n-1] + \delta[n] + \delta[n+1]$$

$$\boxed{h[n] = \delta[n+1] + \delta[n] + \delta[n-1]}$$

| n  | h[n] |
|----|------|
| -1 | 1    |
| 0  | 1    |
| 1  | 1    |
| diğer | 0 |

**Grafik:**

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  width=8cm, height=4.5cm, ymin=0, ymax=1.4, xmin=-2.6, xmax=2.6,
  axis lines=middle, xlabel={$n$}, ylabel={$h[n]$},
  xtick={-2,-1,0,1,2}, ytick={1}, ymajorgrids, grid style={dashed,gray!30},
  every axis plot/.append style={ycomb, thick, mark=*, mark options={fill=red!70}}]
\addplot coordinates {(-1,1) (0,1) (1,1)};
\end{axis}
\end{tikzpicture}
\end{document}
```

**Sistem Özellikleri:**

| Özellik | Karar | Gerekçe |
|---------|-------|---------|
| **Nedensellik** | ❌ Nedensel Değil | $h[n] \neq 0$ için $n = -1 < 0$; sistem $x[n+1]$ (gelecek değeri) kullanıyor |
| **Hafıza** | Hafızalı | $h[n]$ yalnızca $n=0$'da sıfırdan farklı değil; $x[n-1]$ geçmiş, $x[n+1]$ gelecek kullanılıyor |
| **Kararlılık** | ✅ BIBO Kararlı | $\sum_{n=-\infty}^{\infty} |h[n]| = 1+1+1 = 3 < \infty$ |
| **Zamanla Değişmezlik** | ✅ ZD | Girişin gecikmesi çıkışı aynı miktarda geciktirir (koeffisyenler sabit) |
| **Doğrusallık** | ✅ Doğrusal | Süperpozisyon ilkesi sağlanıyor |

---

### 1b — Konvolüsyon ile Çıkış (15p)

$$y[n] = x[n] * h[n]$$

**Yöntem:** $h[n] = \delta[n+1] + \delta[n] + \delta[n-1]$ olduğundan:

$$y[n] = x[n] * \delta[n+1] + x[n] * \delta[n] + x[n] * \delta[n-1]$$
$$= x[n+1] + x[n] + x[n-1]$$

**Hesaplama.** Önce $x[n]$'in değerlerini her $n$ için tek tek oku ($\delta[n+1]$ → $n=-1$'de 1, dikkat):
- $n=-1$: $x[-1] = \delta[-1] - \delta[0] + 2\delta[-2] = 0 - 1 + 0 = -1$
- $n=0$: $x[0] = \delta[0] - \delta[1] + 2\delta[-1] = 1 - 0 + 0 = 1$
- $n=1$: $x[1] = \delta[1] - \delta[2] + 2\delta[0] = 0 - 0 + 2 = 2$

Yani: $x[n]$: $\{\ldots, 0, \underset{n=-1}{-1}, \underset{n=0}{1}, \underset{n=1}{2}, 0, \ldots\}$

$y[n] = x[n-1] + x[n] + x[n+1]$ ile doğrudan hesap:

| n  | $x[n-1]$ | $x[n]$ | $x[n+1]$ | $y[n]$ |
|----|----------|--------|----------|--------|
| -2 | 0        | 0      | -1       | **-1** |
| -1 | 0        | -1     | 1        | **0**  |
| 0  | -1       | 1      | 2        | **2**  |
| 1  | 1        | 2      | 0        | **3**  |
| 2  | 2        | 0      | 0        | **2**  |

$$\boxed{y[n] = -\delta[n+2] + 2\delta[n] + 3\delta[n-1] + 2\delta[n-2]}$$

---

## Soru 2 — Sürekli Zamanlı Konvolüsyon

**Verilen:**
$$x(t) = \begin{cases} -1, & -1 < t < 0 \\ 2, & 0 < t < 1 \\ 1, & 1 < t < 2 \\ 0, & \text{diğer} \end{cases}$$
$$h(t) = u(t) - u(t-1) = \begin{cases} 1, & 0 \leq t \leq 1 \\ 0, & \text{diğer} \end{cases}$$

> [!note]- Semboller
> - $x(t)$: parçalı sabit sinyal; $h(t)$: $[0,1]$ kapısı (genişlik 1 dikdörtgen)
> - $u(t)$: birim basamak; $\tau$: konvolüsyon değişkeni
> - $y(t)=\int_{t-1}^{t}x(\tau)d\tau$: 1 birimlik kayan pencere (h yansıyıp kayar)
> - $E=\int|x|^2dt$: enerji; $x(2-t)$: önce yansıma sonra kaydırma

---

### 2a — x(t) Grafiği ve Özellikleri (15p)

**Grafik (numpy ile render — $x$, $h$, $y$ birlikte):**

![[ss-q2-konv.png]]

**Özellikler:**

| Özellik | Karar | Gerekçe |
|---------|-------|---------|
| **Zamanda Süreklilik** | Sürekli zamanlı | $t \in \mathbb{R}$ üzerinde tanımlı |
| **Değerde Süreklilik** | Kesintili (süreksiz) | $t=0$ ve $t=1$'de atlama var |
| **Sınırlılık** | Sınırlı | $\|x(t)\| \leq 2 < \infty$ |
| **Periyodiklik** | Periyodik değil | Sonlu destekli (finite support) |
| **Enerji** | $E = \int_{-1}^{0}1\,dt + \int_{0}^{1}4\,dt + \int_{1}^{2}1\,dt = 1+4+1 = 6$ J |
| **Güç** | $P = 0$ (enerji sinyali) | Sonlu enerji → sıfır ortalama güç |
| **Sinyal Tipi** | **Enerji Sinyali** | $0 < E < \infty$, $P = 0$ |

---

### 2b — Konvolüsyon y(t) = x(t) * h(t) (15p)

$$y(t) = \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$$

$h(t-\tau) = 1$ için $t-1 \leq \tau \leq t$, yani:

$$y(t) = \int_{t-1}^{t} x(\tau)\,d\tau \quad \text{(1 birimlik kayan pencere)}$$

**Bölge analizi:**

**Bölge 1:** $t \leq -1$
Pencere tamamen $x$'in solunda → $y(t) = 0$

**Bölge 2:** $-1 < t \leq 0$
Pencere $[t-1, t]$, sol uç $t-1 < -1$, sağ uç $t \in (-1,0)$
$$y(t) = \int_{-1}^{t}(-1)\,d\tau = -(t+1)$$

**Bölge 3:** $0 < t \leq 1$
Pencere $[t-1, t]$, $t-1 \in (-1,0)$, $t \in (0,1)$ → sol parça $x=-1$, sağ parça $x=2$:
$$y(t) = \int_{t-1}^{0}(-1)\,d\tau + \int_{0}^{t}2\,d\tau = -\big(0-(t-1)\big) + 2t = -(1-t) + 2t = 3t - 1$$

**Bölge 4:** $1 < t \leq 2$
Pencere $[t-1, t]$, $t-1 \in (0,1)$, $t \in (1,2)$
$$y(t) = \int_{t-1}^{1}2\,d\tau + \int_{1}^{t}1\,d\tau = 2(1-(t-1)) + (t-1) = 2(2-t)+(t-1) = 3-t$$

**Bölge 5:** $2 < t \leq 3$
Pencere $[t-1, t]$, $t-1 \in (1,2)$, $t > 2$ (x sıfır)
$$y(t) = \int_{t-1}^{2}1\,d\tau = 2-(t-1) = 3-t$$

**Bölge 6:** $t > 3$ → $y(t) = 0$

$$\boxed{y(t) = \begin{cases} 0, & t \leq -1 \\ -(t+1), & -1 < t \leq 0 \\ 3t-1, & 0 < t \leq 1 \\ 3-t, & 1 < t \leq 3 \\ 0, & t > 3 \end{cases}}$$

**Süreklilik kontrolü:** $t=-1$: $0$ ✓ | $t=0$: $-1$ ✓ | $t=1$: $2$ ✓ | $t=3$: $0$ ✓

---

### 2c — x(2-t) Çizimi (10p)

**Adımlar:** $x(t) \xrightarrow{\text{yansıma}} x(-t) \xrightarrow{t\to t-2} x(-(t-2)) = x(2-t)$

$x(2-t)$: $\tau = 2-t$ dönüşümü ile:
- $x(\tau)=-1$ için $\tau\in(-1,0)$ → $2-t\in(-1,0)$ → $t\in(2,3)$: $x(2-t)=-1$
- $x(\tau)=2$ için $\tau\in(0,1)$ → $t\in(1,2)$: $x(2-t)=2$
- $x(\tau)=1$ için $\tau\in(1,2)$ → $t\in(0,1)$: $x(2-t)=1$

```
x(2-t)
 2 |    ████
 1 |         ████
   |
───┼─────────────────── t
-1 |              ████
   0    1    2    3
```

---

## Soru 3 — Üçgen × Dikdörtgen Konvolüsyon

**Verilen:**
$$x(t) = \begin{cases} 1-|t|, & -1 \leq t \leq 1 \\ 0, & \text{diğer} \end{cases} \quad \text{(üçgen/tri)}$$

$$h(t) = u(t+0.5) - u(t-0.5) = \begin{cases} 1, & -0.5 \leq t \leq 0.5 \\ 0, & \text{diğer} \end{cases} \quad \text{(rect)}$$

> [!note]- Semboller
> - $x(t)=1-|t|$: birim üçgen ($[-1,1]$, tepe 1); $h(t)$: $[-0.5,0.5]$ kapısı (genişlik 1)
> - $\tau$: konvolüsyon değişkeni; pencere her iki yana $\pm0.5$
> - $y(t)=\int_{t-0.5}^{t+0.5}x(\tau)d\tau$; sonuç **çift** fonksiyon (her ikisi de simetrik)
> - Parçalı $x$: $\tau<0$'da $1+\tau$, $\tau>0$'da $1-\tau$

---

### 3a — Grafikler (10p)

**Üçgen $x(t)$, dikdörtgen $h(t)$ ve parabolik sonuç $y(t)$ (numpy):**

![[ss-q3-ucgen.png]]

---

### 3b — Konvolüsyon y(t) = x(t) * h(t) (20p)

$$y(t) = \int_{t-0.5}^{t+0.5} x(\tau)\,d\tau \quad \text{(0.5 birimlik kayan pencere, her iki yana)}$$

x(τ) = 1+τ (τ < 0) ve 1-τ (τ > 0) diye parçalara ayrılır.

**Bölgeler (simetri: $y(t)$ çifttir):**

**Bölge 1:** $t \leq -1.5$ → $y(t) = 0$

**Bölge 2:** $-1.5 < t \leq -0.5$
Kesişim: $[-1, t+0.5]$, $x(\tau)=1+\tau$
$$y(t) = \int_{-1}^{t+0.5}(1+\tau)\,d\tau = \left[\tau+\frac{\tau^2}{2}\right]_{-1}^{t+0.5}$$
$$= (t+0.5) + \frac{(t+0.5)^2}{2} + 0.5$$

**Bölge 3:** $-0.5 < t \leq 0.5$
Pencere $[t-0.5, t+0.5]$ sıfırı geçiyor:
$$y(t) = \int_{t-0.5}^{0}(1+\tau)\,d\tau + \int_{0}^{t+0.5}(1-\tau)\,d\tau$$

$$= \left[-(t-0.5) - \frac{(t-0.5)^2}{2}\right] + \left[(t+0.5) - \frac{(t+0.5)^2}{2}\right]$$

$$= 1 - \frac{(t-0.5)^2+(t+0.5)^2}{2} = 1 - \frac{2t^2+0.5}{2}$$

$$\boxed{y(t) = 0.75 - t^2, \quad -0.5 < t \leq 0.5}$$

**Bölge 4:** $0.5 < t \leq 1.5$
Kesişim: $[t-0.5, 1]$, $x(\tau)=1-\tau$
$$y(t) = \int_{t-0.5}^{1}(1-\tau)\,d\tau = \left[\tau-\frac{\tau^2}{2}\right]_{t-0.5}^{1} = 0.5 - (t-0.5) + \frac{(t-0.5)^2}{2}$$

**Bölge 5:** $t > 1.5$ → $y(t) = 0$

**Değer kontrolü:**
- $t=0$: $y(0) = 0.75$ (tepe)
- $t=\pm 0.5$: $y(\pm 0.5) = 0.75 - 0.25 = 0.5$ ✓ (süreklilik)
- $t=\pm 1.5$: $y(\pm 1.5) = 0$ ✓
