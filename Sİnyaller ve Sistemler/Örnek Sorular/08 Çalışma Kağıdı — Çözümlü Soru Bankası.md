---
tags: [ss, çalışma-kağıdı, çözümlü, sıfırdan, konvolüsyon, fourier-serisi, fourier-dönüşümü, frekans-yanıtı]
---

# 08 — Çalışma Kağıdı · Çözümlü Soru Bankası (Sıfırdan Öğretici)

← [[SS Ana Sayfa]]

> [!info] Bu sayfa nedir?
> Elimizdeki **8 çalışma kağıdının** (resmi/el yazısı çözümler) tamamı tek sayfada birleştirildi. Her soru, konuyu **hiç bilmeyen birine** anlatır gibi yazıldı: önce kavram → sonra sembollerin anlamı → sonra denklemin nereden geldiği → sonra adım adım çözüm.
>
> Kapsanan 9 örnek:
> 1. Ayrık-zaman LTI sistem (dürtü yanıtı + konvolüsyon)
> 2. Sürekli-zaman konvolüsyon (parçalı sinyal)
> 3. Üçgen × dikdörtgen konvolüsyon
> 4. Sürekli-zaman konvolüsyon (±1 darbe çifti)
> 5. Fourier serisi (sin + cos toplamı)
> 6. **Anti-nedensel** konvolüsyon ($h(t)=u(-t)$)
> 7. Fourier dönüşümü — kaydırılmış sönen üstel
> 8. Fourier dönüşümü — çift taraflı üstel $e^{-2|t-1|}$
> 9. Sistemin dürtü yanıtını bulma ($H=Y/X$ + ters dönüşüm)
>
> Kaynak görseller: `_dataset/Sinyaller Ve Sistemler/SS Çalışma Kağıdı 1–8.jpeg`

---

## 🔑 Önce Ortak Sözlük (tüm sorularda geçer)

| Kısaltma / Sembol | İngilizce | Türkçe / Anlamı |
|---|---|---|
| **CT** | Continuous-Time | **Sürekli-zaman** — sinyal her $t$ anında tanımlı: $x(t)$, $t\in\mathbb{R}$ |
| **DT** | Discrete-Time | **Ayrık-zaman** — sinyal yalnızca tam sayılarda: $x[n]$, $n\in\mathbb{Z}$ |
| **LTI** | Linear Time-Invariant | **Doğrusal & Zamanla-Değişmez** sistem |
| **BIBO** | Bounded-Input Bounded-Output | **Sınırlı giriş → sınırlı çıkış** (kararlılık ölçütü) |
| $\delta(t),\ \delta[n]$ | impulse / unit sample | **Birim dürtü** — tek noktada "iğne" |
| $u(t),\ u[n]$ | unit step | **Birim basamak** — $t<0$'da 0, $t>0$'da 1 |
| $h(t),\ h[n]$ | impulse response | **Dürtü yanıtı** — girişe $\delta$ verince çıkış; sistemin "parmak izi" |
| $*$ | convolution | **Konvolüsyon (evrişim)** — LTI sistemin çıkışını veren işlem |
| $\tau$ | dummy variable | **Yardımcı (kukla) değişken** — integral içinde kayan eksen |
| $X(j\omega)$ | Fourier Transform | $x(t)$'nin **frekans içeriği** (CTFT) |
| $\omega$ (= $w$) | angular frequency | **Açısal frekans** (rad/s); $\omega = 2\pi f$ |

> [!tip] Konvolüsyonun mantığı (her problemde lazım)
> $$y(t)=x(t)*h(t)=\int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$$
> Adımlar: **(1)** $h$'yi aynaya tut ($h(\tau)\to h(-\tau)$), **(2)** $t$ kadar kaydır ($h(t-\tau)$), **(3)** $x$ ile çarpıp **(4)** ortak alan üzerinden topla (integral al), **(5)** her $t$ aralığı için tekrarla.
> Sezgi: "$h$ penceresini $x$'in üzerinde soldan sağa kaydırıyoruz, anlık örtüşen alanı topluyoruz."

**Görsel olarak konvolüsyonun 5 adımı** (örnek: Soru 4'ün $x$ ve $h$'si):

![[ss-konv-kayan-pencere.png]]

> [!note]- 🐍 Python kaynağı (numpy) — `_assets/scripts/ss-konv-kayan-pencere.py`
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
>
> def x(t):
>     return np.where((t > 0) & (t < 1), 1.0,
>            np.where((t > 1) & (t < 2), -1.0, 0.0))
> def h(t):
>     return np.where((t >= 0) & (t <= 2), 1.0, 0.0)
>
> t = np.linspace(-2, 5, 2000); t0 = 1.5; tau = t
> fig, ax = plt.subplots(2, 2, figsize=(9, 5.5))
> ax[0,0].plot(tau, x(tau), "#c0392b", lw=2, label=r"$x(\tau)$")
> ax[0,0].plot(tau, h(tau), "#2980b9", lw=2, ls="--", label=r"$h(\tau)$")
> ax[0,1].plot(tau, x(tau), "#c0392b", lw=2)
> ax[0,1].plot(tau, h(t0 - tau), "#27ae60", lw=2, label=r"$h(t_0-\tau)$")
> prod = x(tau) * h(t0 - tau)
> ax[1,0].plot(tau, prod, "#8e44ad", lw=2)
> ax[1,0].fill_between(tau, 0, prod, color="#8e44ad", alpha=0.3)
> def y(t):
>     return np.where(t<=0,0.0, np.where(t<=1,t, np.where(t<=3,2-t,
>            np.where(t<=4,t-4,0.0))))
> ax[1,1].plot(t, y(t), "#1a1a2e", lw=2.2)
> # eksenler + kaydet: tam script dosyada
> ```

---

# Soru 1 — Ayrık-Zaman LTI Sistem (Dürtü Yanıtı + Konvolüsyon)

> [!example] Verilen
> $$x[n] = \delta[n] - \delta[n+1] + 2\delta[n-1]$$
> $$y[n] = x[n-1] + x[n] + x[n+1]$$
> **a)** Sistemin dürtü yanıtı (transfer fonksiyonu) $h[n]$'i bulun, grafiğini çizin, sistem özelliklerini (nedensellik, hafıza, kararlılık, zamanla değişmezlik, doğrusallık) gerekçeleriyle yazın.
> **b)** Çıkışı $y[n]=x[n]*h[n]$ konvolüsyonu ile bulun.

### 📘 Önce kavram
- $\delta[n-k]$, **yalnızca $n=k$ noktasında 1**, diğer her yerde 0 olan dizidir. Dikkat: $\delta[n+1]$, $n=-1$'de 1'dir (içerideki ifade sıfır olduğunda tetiklenir).
- **Dürtü yanıtı $h[n]$:** sisteme giriş olarak $x[n]=\delta[n]$ verirsek çıkan diziye denir. Bir LTI sistemi tek başına tanımlar.

### 🔤 Bu sorunun sembolleri
$x[n]$: giriş dizisi · $y[n]$: çıkış · $h[n]$: dürtü yanıtı · $x[n+1]$: **gelecek** değer · $x[n-1]$: **geçmiş** değer.

### ✏️ a) Dürtü yanıtı $h[n]$
Tanım gereği $x[n]=\delta[n]$ koyarsak ($\delta$ kaydırma kurallarını uygula): $x[n-1]\to\delta[n-1]$, $x[n]\to\delta[n]$, $x[n+1]\to\delta[n+1]$:

$$\boxed{h[n] = \delta[n+1] + \delta[n] + \delta[n-1]}$$

| $n$ | $-1$ | $0$ | $1$ | diğer |
|---|---|---|---|---|
| $h[n]$ | 1 | 1 | 1 | 0 |

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

**Sistem özellikleri (gerekçeli):**

| Özellik | Karar | Neden |
|---|---|---|
| **Nedensellik** (causality) | ❌ Nedensel **değil** | $h[-1]\neq0$, yani $n<0$'da yanıt var; sistem $x[n+1]$ (geleceği) kullanıyor |
| **Hafıza** (memory) | Hafızalı | Çıkış $x[n-1]$ (geçmiş) ve $x[n+1]$ (gelecek) değerlere bağlı |
| **Kararlılık** (BIBO) | ✅ Kararlı | $\sum_n\lvert h[n]\rvert = 1+1+1 = 3 < \infty$ |
| **Zamanla değişmezlik** | ✅ ZD | Katsayılar sabit, $n$ ile çarpım yok → giriş gecikince çıkış aynı kadar gecikir |
| **Doğrusallık** | ✅ Doğrusal | Toplama + ölçekleme (süperpozisyon) korunur; kare/mutlak değer yok |

### ✏️ b) Konvolüsyon ile çıkış
$h[n]=\delta[n+1]+\delta[n]+\delta[n-1]$ olduğundan ($\delta$ ile konvolüsyon = kaydırma):
$$y[n]=x[n+1]+x[n]+x[n-1]$$

Önce $x[n]$ değerlerini oku (yine $\delta[n+1]\Rightarrow n=-1$):
$$x[-1]=-1,\quad x[0]=1,\quad x[1]=2,\quad \text{(diğer } 0)$$

| $n$ | $x[n-1]$ | $x[n]$ | $x[n+1]$ | $y[n]$ |
|---|---|---|---|---|
| $-2$ | 0 | 0 | $-1$ | **$-1$** |
| $-1$ | 0 | $-1$ | 1 | **0** |
| $0$ | $-1$ | 1 | 2 | **2** |
| $1$ | 1 | 2 | 0 | **3** |
| $2$ | 2 | 0 | 0 | **2** |

$$\boxed{y[n] = -\delta[n+2] + 2\delta[n] + 3\delta[n-1] + 2\delta[n-2]}$$

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
  width=8.5cm, height=5cm, ymin=-1.6, ymax=3.4, xmin=-3.2, xmax=3.2,
  axis lines=middle, xlabel={$n$}, ylabel={$y[n]$},
  xtick={-2,-1,0,1,2}, ytick={-1,1,2,3}, ymajorgrids, grid style={dashed,gray!30},
  every axis plot/.append style={ycomb, thick, mark=*, mark options={fill=blue!70}}]
\addplot coordinates {(-2,-1) (-1,0) (0,2) (1,3) (2,2)};
\end{axis}
\end{tikzpicture}
\end{document}
```

> [!success] 🎯 Çıkarım
> $\delta$'larla konvolüsyon = sadece **kaydır-topla**. İntegral/karmaşık işlem gerekmez. Nedensellik için tek bakılacak şey: $h[n]$ negatif $n$'de sıfırdan farklı mı?

---

# Soru 2 — Sürekli-Zaman Konvolüsyon (Parçalı Sinyal)

> [!example] Verilen
> $$x(t)=\begin{cases}-1,&-1<t<0\\ 2,&0<t<1\\ 1,&1<t<2\\ 0,&\text{diğer}\end{cases}\qquad h(t)=u(t)-u(t-1)$$
> **a)** $x(t)$'yi çiz; zamanda/değerde süreklilik, sınırlılık, periyodiklik, enerji/güç açısından özelliklerini yaz.
> **b)** $y(t)=x(t)*h(t)$ konvolüsyonunu bul.  **c)** $x(2-t)$'yi çiz.

### 📘 Önce kavram
- $h(t)=u(t)-u(t-1)$ ifadesi bir **kapı (gate) / dikdörtgen darbe**dir: $0\le t\le1$ aralığında 1, dışında 0. Genişliği 1.
- $h(t)$ bir kapı olunca konvolüsyon **kayan ortalama**ya dönüşür: $y(t)=\int_{t-1}^{t}x(\tau)d\tau$ → "son 1 birimlik pencerede $x$'in altındaki alan".
- **Enerji sinyali:** $0<E<\infty$ (sönen/sonlu sinyaller). **Güç sinyali:** $E=\infty$ ama $0<P<\infty$ (periyodik sinyaller). İkisi aynı anda olmaz.

### ✏️ a) Grafik ve özellikler

![[ss-q2-konv.png]]

> [!note]- 🐍 Python kaynağı — `_assets/scripts/ss-q2-konv.py`
> Parçalı `np.where` ile $x(t)$, kapı $h(t)$ ve sonuç $y(t)$ çizdirilir; tam kaynak `_assets/scripts/` altında.

*(Soldaki panel $x(t)$; ortadaki kapı $h(t)$; sağdaki konvolüsyon sonucu $y(t)$ — b şıkkında türetilecek.)*

| Özellik | Karar | Neden |
|---|---|---|
| Zamanda | **Sürekli** | $t\in\mathbb{R}$ üzerinde tanımlı |
| Değerde | **Süreksiz** | $t=0$ ve $t=1$'de sıçrama (atlama) var |
| Sınırlılık | **Sınırlı** | $\lvert x(t)\rvert\le 2<\infty$ |
| Periyodiklik | **Periyodik değil** | Sonlu destekli (yalnız $[-1,2]$'de sıfırdan farklı) |
| Enerji | $E=\int_{-1}^{0}1\,dt+\int_0^1 4\,dt+\int_1^2 1\,dt=1+4+1=6$ J |
| Tür | **Enerji sinyali** | $0<E<\infty$, dolayısıyla $P=0$ |

### ✏️ b) Konvolüsyon
$$y(t)=\int_{t-1}^{t}x(\tau)\,d\tau \quad(\text{1 birimlik kayan pencere})$$
Pencereyi $x$ üzerinde kaydırıp her aralıkta örtüşen alanı yazıyoruz:

- **$t\le-1$:** pencere $x$'in solunda → $y=0$
- **$-1<t\le0$:** $\displaystyle y=\int_{-1}^{t}(-1)d\tau=-(t+1)$
- **$0<t\le1$:** $\displaystyle y=\int_{t-1}^{0}(-1)d\tau+\int_{0}^{t}2\,d\tau=-(1-t)+2t=3t-1$
- **$1<t\le2$:** $\displaystyle y=\int_{t-1}^{1}2\,d\tau+\int_{1}^{t}1\,d\tau=2(2-t)+(t-1)=3-t$
- **$2<t\le3$:** $\displaystyle y=\int_{t-1}^{2}1\,d\tau=3-t$
- **$t>3$:** $y=0$

$$\boxed{y(t)=\begin{cases}0,&t\le-1\\ -(t+1),&-1<t\le0\\ 3t-1,&0<t\le1\\ 3-t,&1<t\le3\\ 0,&t>3\end{cases}}$$

**Süreklilik kontrolü** (bitiş = başlangıç olmalı): $t=-1\!:0$ ✓ · $t=0\!:-1$ ✓ · $t=1\!:2$ ✓ · $t=3\!:0$ ✓

### ✏️ c) $x(2-t)$
$x(2-t)$ = önce **yansıt** ($x(-t)$) sonra **+2 kaydır**. Eşitlik $\tau=2-t$ ile her parçayı çevir:
- $x=-1$ ($\tau\in(-1,0)$) → $t\in(2,3)$
- $x=2$ ($\tau\in(0,1)$) → $t\in(1,2)$
- $x=1$ ($\tau\in(1,2)$) → $t\in(0,1)$
![[ss-q2c-yansima.png]]

> [!success] 🎯 Çıkarım
> Kapı ($u(t)-u(t-T)$) ile konvolüsyon = $T$ genişlikli **kayan integral**. Sınır kontrolü olarak komşu parçaların uç değerleri uyuşmalı.

---

# Soru 3 — Üçgen × Dikdörtgen Konvolüsyon

> [!example] Verilen
> $$x(t)=\begin{cases}1-\lvert t\rvert,&-1\le t\le1\\0,&\text{diğer}\end{cases}\quad(\text{birim üçgen})\qquad h(t)=u(t+0.5)-u(t-0.5)$$
> **a)** $x(t)$ ve $h(t)$ grafikleri.  **b)** $y(t)=x(t)*h(t)$.

### 📘 Önce kavram
- $x(t)=1-\lvert t\rvert$: tepe noktası $(0,1)$ olan, $[-1,1]$ tabanlı **birim üçgen**. Parçalı yazılır: $\tau<0$'da $1+\tau$, $\tau>0$'da $1-\tau$.
- $h(t)$: merkezi sıfırda, $[-0.5,0.5]$ aralığında 1 olan **simetrik kapı** (genişlik 1).
- İki **çift (simetrik)** fonksiyonun konvolüsyonu yine **çifttir** → $y(t)=y(-t)$. Bu, işin yarısını bedavaya getirir.

### ✏️ a) Grafikler

![[ss-q3-ucgen.png]]

> [!note]- 🐍 Python kaynağı — `_assets/scripts/ss-q3-ucgen.py`
> Üçgen $1-|t|$ (np.abs), genişlik-1 kapı ve parçalı parabol sonuç $y(t)$ çizdirilir.

### ✏️ b) Konvolüsyon
$$y(t)=\int_{t-0.5}^{t+0.5}x(\tau)\,d\tau \quad(\text{0.5 yarı-genişlikli kayan pencere})$$

- **$t\le-1.5$:** $y=0$
- **$-1.5<t\le-0.5$:** kesişim $[-1,\,t+0.5]$, $x=1+\tau$: $\displaystyle y=\int_{-1}^{t+0.5}(1+\tau)d\tau=\tfrac12\big(t+\tfrac32\big)^2$
- **$-0.5<t\le0.5$:** pencere sıfırı geçer:
$$y=\int_{t-0.5}^{0}(1+\tau)d\tau+\int_{0}^{t+0.5}(1-\tau)d\tau=1-\frac{(t-0.5)^2+(t+0.5)^2}{2}=\boxed{0.75-t^2}$$
- **$0.5<t\le1.5$:** (simetriden) $\displaystyle y=\tfrac12\big(t-\tfrac32\big)^2$
- **$t>1.5$:** $y=0$

**Değer kontrolü:** $y(0)=0.75$ (tepe) · $y(\pm0.5)=0.5$ ✓ · $y(\pm1.5)=0$ ✓

$$\boxed{y(t)=\begin{cases}0,&t<-1.5\\[2pt]\tfrac12\left(t+\tfrac32\right)^2,&-1.5\le t<-0.5\\[2pt]\tfrac34-t^2,&-0.5\le t\le0.5\\[2pt]\tfrac12\left(t-\tfrac32\right)^2,&0.5<t\le1.5\\[2pt]0,&t>1.5\end{cases}}$$

> [!success] 🎯 Çıkarım
> Simetrik girdilerde **çift sonuç** beklenir; bir yarıyı hesaplayıp aynala. Konvolüsyon "köşeleri yumuşatır": keskin üçgen → parabolik eğri.

---

# Soru 4 — Sürekli-Zaman Konvolüsyon (±1 Darbe Çifti, [0,2] Kapı)

> [!example] Verilen
> $$x(t)=\begin{cases}1,&0<t<1\\-1,&1<t<2\\0,&\text{diğer}\end{cases}\qquad h(t)=u(t)-u(t-2)$$
> **a)** Sistem özellikleri (nedensellik, hafıza, kararlılık).  **b)** $y(t)=x(t)*h(t)$.

### 📘 Önce kavram
$h(t)=u(t)-u(t-2)$: $[0,2]$ aralığında 1 olan, genişliği **2** olan nedensel kapı. Nedensel çünkü $t<0$'da $h=0$ (geleceğe bakmıyor).

### ✏️ a) Sistem özellikleri

| Özellik | Karar | Neden |
|---|---|---|
| Nedensellik | ✅ Nedensel | $h(t)=0,\ t<0$ |
| Hafıza | Hafızalı | $h(t)\neq\delta(t)$; çıkış geçmiş girişlere bağlı |
| Kararlılık | ✅ BIBO | $\int_{-\infty}^{\infty}\lvert h(t)\rvert dt=\int_0^2 1\,dt=2<\infty$ |

### ✏️ b) Konvolüsyon
$$y(t)=\int_{t-2}^{t}x(\tau)\,d\tau\quad(\text{2 birimlik kayan pencere})$$

- **$t\le0$:** $y=0$
- **$0<t\le1$:** $\displaystyle y=\int_0^t 1\,d\tau=t$
- **$1<t\le2$:** $\displaystyle y=\int_0^1 1\,d\tau+\int_1^t(-1)d\tau=1-(t-1)=2-t$
- **$2<t\le3$:** $\displaystyle y=\int_{t-2}^{1}1\,d\tau+\int_1^2(-1)d\tau=(1-(t-2))-1=2-t$
- **$3<t\le4$:** $\displaystyle y=\int_{t-2}^{2}(-1)d\tau=-(2-(t-2))=t-4$
- **$t>4$:** $y=0$

$$\boxed{y(t)=\begin{cases}0,&t\le0\\ t,&0<t\le1\\ 2-t,&1<t\le3\\ t-4,&3<t\le4\\ 0,&t>4\end{cases}}$$

**Süreklilik:** $t=1\!:1$ ✓ · $t=3\!:-1$ ✓ · $t=4\!:0$ ✓

> Bu sorunun $x$, $h$ ve $y(t)$ grafikleri ile "yansıt-kaydır-çarp-topla" adımları sayfanın başındaki [[#🔑 Önce Ortak Sözlük (tüm sorularda geçer)|konvolüsyon görselinde]] (5 panelli figür) gösterilmiştir — o figür birebir bu sorunun $x$ ve $h$'sini kullanır.

> [!success] 🎯 Çıkarım
> Giriş içinde +1 ve −1 olunca çıkış önce yükselir, sonra eksiye geçer. Toplam alan $\int x=0$ olduğu için çıkış $t\to\infty$'da sıfıra döner.

---

# Soru 5 — Fourier Serisi (sin + cos Toplamı)

> [!example] Verilen
> $$x(t)=2\sin\!\Big(\tfrac{\pi}{4}t+\tfrac{\pi}{8}\Big)+\cos\!\Big(\tfrac{\pi}{2}t+\tfrac{\pi}{4}\Big)-1$$
> **a)** Fourier seri katsayılarını bul.  **b)** Genlik ve faz spektrumunu çiz.

### 📘 Önce kavram
- **Fourier serisi:** periyodik bir sinyali $x(t)=\sum_n c_n e^{jn\omega_0 t}$ şeklinde **harmonik üstellerin toplamı** olarak yazmak. $c_n$ = $n$. harmoniğin karmaşık ağırlığı.
- $\omega_0$ = **temel açısal frekans**; tüm bileşenlerin ortak periyodundan gelir: $\omega_0=2\pi/T_0$.
- **Euler köprüsü** (sin/cos'u üstele çevirir):
$$\cos\theta=\tfrac12(e^{j\theta}+e^{-j\theta}),\qquad \sin\theta=\tfrac1{2j}(e^{j\theta}-e^{-j\theta})$$
- Burada integral almaya gerek yok: sinyal zaten sinüzoidlerin toplamı, sadece Euler ile üstellere açıp $c_n$'leri **okuyoruz**.

### ✏️ a) Temel frekans
- $\omega_1=\pi/4\Rightarrow T_1=2\pi/\omega_1=8$
- $\omega_2=\pi/2\Rightarrow T_2=4$
- Ortak periyot $T_0=\operatorname{OKEK}(8,4)=8\Rightarrow\boxed{\omega_0=2\pi/8=\pi/4}$

Yani $\omega_1=\omega_0$ ($n=1$), $\omega_2=2\omega_0$ ($n=2$). Sabit $-1$ ise $n=0$.

**Euler ile aç:**
$$2\sin(\omega_0 t+\tfrac{\pi}{8})=\underbrace{-je^{j\pi/8}}_{c_1}e^{j\omega_0 t}+\underbrace{je^{-j\pi/8}}_{c_{-1}}e^{-j\omega_0 t}$$
$$\cos(2\omega_0 t+\tfrac{\pi}{4})=\underbrace{\tfrac12 e^{j\pi/4}}_{c_2}e^{j2\omega_0 t}+\underbrace{\tfrac12 e^{-j\pi/4}}_{c_{-2}}e^{-j2\omega_0 t}$$
($-j=e^{-j\pi/2}$ özdeşliğiyle $-je^{j\pi/8}=e^{-j3\pi/8}$, yani $\lvert c_1\rvert=1$, $\angle c_1=-3\pi/8$.)

| $n$ | $c_n$ | $\lvert c_n\rvert$ | $\angle c_n$ |
|---|---|---|---|
| 0 | $-1$ | 1 | $\pi$ |
| $+1$ | $e^{-j3\pi/8}$ | 1 | $-3\pi/8$ |
| $-1$ | $e^{+j3\pi/8}$ | 1 | $+3\pi/8$ |
| $+2$ | $\tfrac12 e^{j\pi/4}$ | $1/2$ | $+\pi/4$ |
| $-2$ | $\tfrac12 e^{-j\pi/4}$ | $1/2$ | $-\pi/4$ |
| diğer | 0 | — | — |

### ✏️ b) Spektrumlar

![[ss-q5-spektrum.png]]

> [!note]- 🐍 Python kaynağı — `_assets/scripts/ss-q5-spektrum.py`
> `plt.stem` ile $|c_n|$ (genlik) ve $\angle c_n$ (faz) çubuk spektrumları; harmonik indeksi $n=-2\ldots2$.

> [!warning] Gerçek sinyal simetrisi
> $x(t)$ gerçek olduğu için $c_{-n}=c_n^{*}$: **genlik çift** ($\lvert c_n\rvert=\lvert c_{-n}\rvert$), **faz tek** ($\angle c_{-n}=-\angle c_n$). Bunu doğrulama olarak kullan.

> [!success] 🎯 Çıkarım
> Sinyal sinüzoid toplamıysa Fourier "hesabı" = Euler açılımı + katsayı okuma. İntegrale ancak parçalı/genel periyodik sinyallerde gerek var.

---

# Soru 6 — Anti-Nedensel Konvolüsyon ($h(t)=u(-t)$)

> [!example] Verilen
> $$x(t)=u(t)-u(t-2)\quad(\text{[0,2] kapısı}),\qquad h(t)=u(-t)$$
> $y(t)=x(t)*h(t)=?$ ve sistem özellikleri.

### 📘 Önce kavram
- $u(-t)$: **zamanda aynalanmış basamak** → $t<0$'da 1, $t>0$'da 0. Yani sistem **geleceğe bakıyor** (anti-nedensel).
- $h(t-\tau)=u(-(t-\tau))=u(\tau-t)$ → bu **$\tau>t$ için 1**'dir. Demek ki integralin alt sınırı $t$, üst sınırı $\infty$:
$$y(t)=\int_{t}^{\infty}x(\tau)\,d\tau \quad(\text{"}t\text{'nin sağındaki alan"})$$

### ✏️ Çözüm
$x(\tau)=1$ yalnız $0<\tau<2$ olduğundan, $t$'nin sağında kalan kapı alanını sayıyoruz:
- **$t<0$:** tüm kapı sağda → $\displaystyle y=\int_0^2 1\,d\tau=2$
- **$0\le t<2$:** $\displaystyle y=\int_t^2 1\,d\tau=2-t$
- **$t\ge2$:** sağda alan yok → $y=0$

$$\boxed{y(t)=\begin{cases}2,&t<0\\ 2-t,&0\le t<2\\ 0,&t\ge2\end{cases}}$$

![[ss-q6-antinedensel.png]]

> [!note]- 🐍 Python kaynağı — `_assets/scripts/ss-q6-antinedensel.py`
> Kapı $x$, aynalanmış basamak $h(t)=u(-t)$ ve azalan rampa sonuç $y(t)$ çizdirilir.

**Sistem özellikleri:**

| Özellik | Karar | Neden |
|---|---|---|
| Nedensellik | ❌ **Değil** | $h(t)\neq0$ for $t<0$; çıkış **gelecekteki** girişe bağlı |
| Hafıza | Hafızalı | Geniş aralıkta integral |
| Kararlılık | ❌ **Değil** | $\int_{-\infty}^{\infty}\lvert u(-t)\rvert dt=\int_{-\infty}^{0}1\,dt=\infty$ → BIBO bozulur |

> [!success] 🎯 Çıkarım
> $u(-t)$ gördüğünde refleks: **anti-nedensel + kararsız**, ve konvolüsyon integralinin sınırı $[t,\infty)$ olur (normaldeki $(-\infty,t]$ değil). Aynalanmış basamak = "sağdaki alanı topla".

---

# Soru 7 — Fourier Dönüşümü: Kaydırılmış Sönen Üstel

> [!example] Verilen
> $$x(t)=e^{-2(t-1)}\,u(t-1)$$
> $X(j\omega)=?$

### 📘 Önce kavram
- **Fourier dönüşümü (CTFT):** $X(j\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt$ → sinyalin **frekans içeriği**.
- Bilinen çift: $e^{-at}u(t)\ \longleftrightarrow\ \dfrac{1}{a+j\omega}$ (sönen nedensel üstel), koşul $a>0$.
- **Zaman kaydırma teoremi:** $f(t-t_0)\ \longleftrightarrow\ e^{-j\omega t_0}F(j\omega)$. (Kaydırma sadece **faz** ekler, genliği değiştirmez.)

### ✏️ Çözüm
$f(t)=e^{-2t}u(t)$ alalım: $F(j\omega)=\dfrac{1}{2+j\omega}$.
Sinyalimiz $x(t)=f(t-1)$ (1 birim sağa kaydırılmış), $t_0=1$:
$$\boxed{X(j\omega)=e^{-j\omega}\cdot\frac{1}{2+j\omega}=\frac{e^{-j\omega}}{2+j\omega}}$$

Genlik: $\lvert X\rvert=\dfrac{1}{\sqrt{4+\omega^2}}$ · Faz: $\angle X=-\omega-\arctan(\omega/2)$.

> [!success] 🎯 Çıkarım
> "Kaydırılmış sönen üstel" gördüğünde: **tablo çiftini al → kaydırma için $e^{-j\omega t_0}$ çarp**. İntegral almana gerek yok.

---

# Soru 8 — Fourier Dönüşümü: Çift Taraflı Üstel $e^{-2|t-1|}$

> [!example] Verilen
> $$x(t)=e^{-2\lvert t-1\rvert}$$
> $X(j\omega)=?$

### 📘 Önce kavram
- $\lvert t\rvert$ içeren **çift taraflı** üstel her iki yöne de söner. Bilinen çift:
$$e^{-a\lvert t\rvert}\ \longleftrightarrow\ \frac{2a}{a^2+\omega^2}\qquad(\text{gerçek ve çift} \Rightarrow X \text{ gerçek})$$
- Türetim (neden böyle): integrali ikiye böl, çünkü $\lvert t\rvert$ işaret değiştirir:
$$\int_{-\infty}^{0}e^{at}e^{-j\omega t}dt+\int_{0}^{\infty}e^{-at}e^{-j\omega t}dt=\frac{1}{a-j\omega}+\frac{1}{a+j\omega}=\frac{2a}{a^2+\omega^2}$$

### ✏️ Çözüm
Önce merkezdeki $g(t)=e^{-2\lvert t\rvert}$: $a=2\Rightarrow G(j\omega)=\dfrac{4}{4+\omega^2}$.
Sinyalimiz $x(t)=g(t-1)$ (1 birim kaydırılmış), zaman kaydırmadan $e^{-j\omega}$ çarp:
$$\boxed{X(j\omega)=e^{-j\omega}\cdot\frac{4}{4+\omega^2}}$$

> [!success] 🎯 Çıkarım
> $\lvert\cdot\rvert$ üsteli → integrali **iki parçaya** böl (negatif/pozitif eksen). Sonuç paydası $a^2+\omega^2$ (gerçek, çift). Kayma yine yalnızca faz $e^{-j\omega t_0}$ ekler.

---

# Soru 9 — Sistemin Dürtü Yanıtını Bulma ($H=Y/X$ + Ters Dönüşüm)

> [!example] Verilen
> $$x(t)=\big[e^{-t}+e^{-3t}\big]u(t)\ \xrightarrow{\ \text{sistem}\ }\ y(t)=\big[2e^{-t}-2e^{-4t}\big]u(t)$$
> Sistemin frekans yanıtı $H(j\omega)$ ve dürtü yanıtı $h(t)$?

### 📘 Önce kavram
- LTI sistemde frekans domeninde **çarpım** geçerli: $Y(j\omega)=X(j\omega)\,H(j\omega)$ → buradan $H=Y/X$.
- Strateji: $x,y$'yi dönüştür → böl → **kısmi kesirlere** ayır → her terimi ters dönüştür.
- Ters çift: $\dfrac{1}{a+j\omega}\ \longleftrightarrow\ e^{-at}u(t)$.

### ✏️ Adım 1 — $X$ ve $Y$
$$X(j\omega)=\frac{1}{1+j\omega}+\frac{1}{3+j\omega}=\frac{4+2j\omega}{(1+j\omega)(3+j\omega)}$$
$$Y(j\omega)=\frac{2}{1+j\omega}-\frac{2}{4+j\omega}=\frac{6}{(1+j\omega)(4+j\omega)}$$

### ✏️ Adım 2 — $H=Y/X$
$$H(j\omega)=\frac{Y}{X}=\frac{6}{(1+j\omega)(4+j\omega)}\cdot\frac{(1+j\omega)(3+j\omega)}{4+2j\omega}=\frac{6(3+j\omega)}{(4+j\omega)\cdot 2(2+j\omega)}=\frac{3(3+j\omega)}{(4+j\omega)(2+j\omega)}$$

### ✏️ Adım 3 — Kısmi kesirler
$$\frac{3(3+j\omega)}{(4+j\omega)(2+j\omega)}=\frac{A}{4+j\omega}+\frac{B}{2+j\omega}$$
$$A=\left.\frac{3(3+j\omega)}{2+j\omega}\right|_{j\omega=-4}=\frac{3(-1)}{-2}=\frac32,\qquad B=\left.\frac{3(3+j\omega)}{4+j\omega}\right|_{j\omega=-2}=\frac{3(1)}{2}=\frac32$$

### ✏️ Adım 4 — Ters dönüşüm
$$H(j\omega)=\frac{3/2}{4+j\omega}+\frac{3/2}{2+j\omega}\ \xrightarrow{\ \mathcal{F}^{-1}\ }\ \boxed{h(t)=\frac32\big[e^{-4t}+e^{-2t}\big]u(t)}$$

**Kontrol:** kutuplar $j\omega=-2,-4$ → ikisi de sol yarı düzlemde ($\mathrm{Re}<0$) → sistem **kararlı**. $t<0$'da $h=0$ → **nedensel**. ✓

> [!success] 🎯 Çıkarım
> "Giriş ve çıkış verilmiş, sistemi bul" → **$H=Y/X$**. Sönen üsteller toplamı → her zaman $\frac{1}{a+j\omega}$ çiftlerine ve kısmi kesirlere indirgenir. Kutupların işareti kararlılığı söyler.

---

## 🧭 Soru Tipini Tanıma Rehberi (sınavda hangi alet?)

| Soruda görürsen… | Yöntem |
|---|---|
| $\delta[n]$, fark denklemi | $x=\delta$ koy → $h[n]$; sonra kaydır-topla |
| Parçalı $x(t)$ + kapı $h(t)$ | Kayan integral $\int_{t-T}^{t}x\,d\tau$, bölge bölge |
| $u(-t)$, $h(-\ldots)$ | Anti-nedensel: integral $[t,\infty)$; kararsız |
| $\sin/\cos$ toplamı, "katsayı" | Euler aç, $c_n$ oku (Fourier serisi) |
| Tek sönen üstel $e^{-at}u(t)$ | Tablo: $\frac{1}{a+j\omega}$ (+ kayma için $e^{-j\omega t_0}$) |
| $e^{-a\lvert t\rvert}$ | İntegrali ikiye böl → $\frac{2a}{a^2+\omega^2}$ |
| $x$ ve $y$ verilmiş, sistem isteniyor | $H=Y/X$ → kısmi kesir → ters dönüşüm |
| $H(j\omega)$ paydası $-\omega^2+\ldots$ | $s=j\omega$ koy, $s^2+\ldots$ çarpanlara ayır |

---

## Bağlantılı Notlar
- [[05 Vize Sınav Soruları (Çözümlü)|Vize sınavı (1–3. sorular burada da var)]]
- [[06 Final Sınav Soruları (Çözümlü)|Final sınavı (Fourier ağırlıklı)]]
- [[../Konu Anlatımları/02 LTI Sistemler ve Konvolüsyon]] · [[../Konu Anlatımları/03 Fourier Serisi]] · [[../Konu Anlatımları/04 Fourier Dönüşümü]]
- [[../SS Formül Sayfası]]
