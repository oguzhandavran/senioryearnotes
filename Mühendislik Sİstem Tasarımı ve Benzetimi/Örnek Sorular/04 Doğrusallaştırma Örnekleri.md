---
tags: [mst, doğrusallaştırma, linearization, taylor, jacobian, denge-noktası, örnek-sorular]
---

# 04 — Doğrusallaştırma Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/04 Doğrusallaştırma|04 Doğrusallaştırma]]

---

## Çözümlü Örnek 1: Basit Sarkaç

> [!example] Problem
> **Sistem:** Sönümsüz sarkaç $\ddot\theta+\dfrac{g}{L}\sin\theta=0$ (doğrusal değil).
>
> **İstenen:** Denge noktalarını bul ve her birinde Jacobian ile doğrusallaştırıp kararlılığı incele.

> [!note]- Semboller
> - $\theta$: sarkaç açısı (rad); $g$: yerçekimi (m/s²); $L$: kol uzunluğu (m)
> - $x_1=\theta$, $x_2=\dot\theta$: durum değişkenleri
> - $f_1,f_2$: durum türev fonksiyonları ($\dot x_1=f_1,\ \dot x_2=f_2$)
> - $x_e$: denge (equilibrium) noktası — tüm türevlerin sıfır olduğu nokta
> - $A$: Jacobian matrisi $[\partial f_i/\partial x_j]$, $x_e$'de değerlendirilir
> - $\lambda$: özdeğer (eigenvalue); Re$(\lambda)$ işareti kararlılığı belirler

**Doğrusal olmayan sistem:**
$$\ddot{\theta} + \frac{g}{L}\sin\theta = 0$$

**Durum değişkenleri:** $x_1 = \theta$, $x_2 = \dot{\theta}$

$$f_1 = x_2, \quad f_2 = -\frac{g}{L}\sin x_1$$

**Denge noktaları:** $f_1 = 0 \implies x_2 = 0$, $f_2 = 0 \implies \sin x_1 = 0$
$$x_e = (0, 0) \quad \text{veya} \quad x_e = (\pi, 0)$$

**$x_e = (0, 0)$ çevresinde Jacobian:**

$$A = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \end{bmatrix}_{(0,0)} = \begin{bmatrix} 0 & 1 \\ -\frac{g}{L}\cos(0) & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -g/L & 0 \end{bmatrix}$$

Özdeğerler: $\lambda^2 + g/L = 0 \implies \lambda = \pm j\sqrt{g/L}$ → **sınır kararlı** (salınım)

**$x_e = (\pi, 0)$ çevresinde:**

$$A = \begin{bmatrix} 0 & 1 \\ -\frac{g}{L}\cos(\pi) & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ g/L & 0 \end{bmatrix}$$

Özdeğerler: $\lambda = \pm\sqrt{g/L}$ → **kararsız** (ters sarkaç)

---

## Çözümlü Örnek 2: Doğrusal Olmayan Mekanik

> [!example] Problem
> **Sistem:** $m\ddot{x} + b\dot{x}^3 + kx^2 = f$ — sönüm $\dot x^3$ ve yay $x^2$ ile doğrusal değil.
>
> **İstenen:** $f_e=0$ girişinde denge noktası ve Jacobian ile doğrusallaştırılmış $A,B$.

> [!note]- Semboller
> - $m,b,k$: kütle, (doğrusal olmayan) sönüm ve yay katsayıları
> - $x_1=x$, $x_2=\dot x$: durum değişkenleri; $f$: giriş kuvveti
> - $x_{1e}$: denge konumu; $\delta x,\delta f$: denge etrafındaki küçük sapmalar
> - $A=[\partial f_i/\partial x_j]_{x_e}$: Jacobian; $B=[\partial f_i/\partial f]_{x_e}$: giriş Jacobian'ı
> - Türevler: $\partial(kx_1^2)/\partial x_1=2kx_1$, $\partial(bx_2^3)/\partial x_2=3bx_2^2$ → dengede ($x_e=0$) ikisi de 0

**Sistem:** $m\ddot{x} + b\dot{x}^3 + kx^2 = f$

Durum değişkenleri: $x_1 = x$, $x_2 = \dot{x}$

$$f_1 = x_2$$
$$f_2 = \frac{1}{m}(f - b x_2^3 - k x_1^2)$$

**Denge noktası ($f_e = 0$ girişi için):** $x_2 = 0$, $k x_{1e}^2 = 0 \implies x_{1e} = 0$

**Jacobian:**

$$A = \begin{bmatrix} 0 & 1 \\ -2kx_1/m & -3bx_2^2/m \end{bmatrix}_{(0,0,0)} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$$

$$B = \begin{bmatrix} 0 \\ 1/m \end{bmatrix}_{(0,0)} = \begin{bmatrix} 0 \\ 1/m \end{bmatrix}$$

**Lineerleştirilmiş sistem:**
$$\delta\dot{x} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}\delta x + \begin{bmatrix} 0 \\ 1/m \end{bmatrix}\delta f$$

---

## Çözümlü Örnek 3: Elektrik (Diyot)

> [!example] Problem
> **Eleman:** Diyot $i = I_s(e^{v/(nV_T)} - 1)$. $(V_Q,I_Q)$ çalışma noktası verilmiş.
>
> **İstenen:** Küçük sinyal iletkenliği $g_m$ ve doğrusallaştırılmış $\delta i$–$\delta v$ ilişkisi.

> [!note]- Semboller
> - $i,v$: diyot akımı (A) ve gerilimi (V)
> - $I_s$: ters doyma akımı; $n$: idealite faktörü; $V_T$: ısıl gerilim (≈26 mV)
> - $(V_Q,I_Q)$: çalışma (Q) noktası — etrafında doğrusallaştırılır
> - $g_m=di/dv|_{V_Q}$: küçük sinyal iletkenliği (eğim, S)
> - $\delta i,\delta v$: Q noktası etrafındaki küçük değişimler

**Diyot denklemi:** $i = I_s(e^{v/(nV_T)} - 1) \approx I_s e^{v/(nV_T)}$

**Çalışma noktası:** $(V_Q, I_Q)$

**Küçük sinyal modeli (lineerleştirilmiş):**

$$g_m = \left.\frac{di}{dv}\right|_{V_Q} = \frac{I_Q}{nV_T}$$

$$\delta i = g_m \delta v$$

---

## Çözümlü Örnek 4 — Trigonometrik Nonlineer Sistem ($x_0 = \pi/4$)

> [!example] Problem
> **Sistem:** $\ddot{x} + 2\dot{x} + \cos x = 0$. $x_0=\pi/4$ çalışma noktası etrafında doğrusallaştır.
>
> **İstenen:** Taylor ile doğrusallaştırılmış denklem ve $\delta X(s)$.
> *(Bu, aşağıdaki [#Örnek 5 — cos x İçeren ODE Doğrusallaştırma (Hocanın Notu)](#örnek-5--cos-x-i̇çeren-ode-doğrusallaştırma-hocanın-notu) ile aynı sorudur — orada hocanın çözümü adım adım var.)*

> [!note]- Semboller
> - $x,\dot x,\ddot x$: konum, hız, ivme
> - $x_0=\pi/4$: **çalışma noktası** (denge değil — aşağıdaki nota bak); $\delta x=x-x_0$: sapma
> - Taylor (1. derece): $\cos x\approx\cos x_0-\sin x_0\,\delta x$
> - $\delta X(s)$: $\delta x$'in Laplace dönüşümü; $s$: Laplace değişkeni

> [!warning] Denge mi, çalışma noktası mı?
> Gerçek denge $\cos x_e=0\Rightarrow x_e=\pi/2$'dir. Soru $\pi/4$'te doğrusallaştırma istediği için bu nokta **denge değildir**: bu yüzden doğrusallaştırılmış denklemde sıfırlanmayan bir **sabit terim** ($\cos\frac{\pi}{4}=\frac{\sqrt2}{2}$) kalır. Bu sabit, dış basamak gibi davranır.

**$x_0 = \pi/4$ etrafında Taylor açılımı:**

$x = \delta x + \pi/4$ (minimal sapma) yaz:

$$\frac{d^2(\delta x)}{dt^2} + 2\frac{d(\delta x)}{dt} + \cos\!\left(\delta x + \frac{\pi}{4}\right) = 0$$

$\cos$ için Taylor ($\frac{1}{\sqrt2}=\frac{\sqrt2}{2}$):

$$\cos\!\left(\delta x + \frac{\pi}{4}\right) \approx \cos\!\left(\frac{\pi}{4}\right) - \sin\!\left(\frac{\pi}{4}\right)\cdot\delta x = \frac{\sqrt2}{2} - \frac{\sqrt2}{2}\,\delta x$$

Denklem:

$$\ddot{\delta x} + 2\dot{\delta x} - \frac{\sqrt2}{2}\,\delta x = -\frac{\sqrt2}{2}$$

Sabit terim ($-\frac{\sqrt2}{2}$) sağdadır ve **basamak girişi** gibidir; Laplace'ı $-\frac{\sqrt2/2}{s}$:

$$\delta X(s)\!\left(s^2 + 2s - \frac{\sqrt{2}}{2}\right) = -\frac{\sqrt{2}/2}{s}\;\Longrightarrow\; \boxed{\delta X(s) = \frac{-\sqrt{2}/2}{s\left(s^2+2s-\sqrt{2}/2\right)}}$$

**Kararlılık (karakteristik kökler).** $s^2+2s-\frac{\sqrt2}{2}=0$: $\;s = -1 \pm \sqrt{1+\frac{\sqrt{2}}{2}} \approx -1 \pm 1{,}30$, yani $s_1\approx 0{,}30>0$ → **kararsız** çalışma noktası (eyer bölgesi).

---

## Çözümlü Örnek 5 — Doğrusal Olmayan Direnç Devresi

> [!example] Problem
> **Devre:** $L=1$ H bobin + doğrusal olmayan direnç ($i_r = 2e^{0.1V_r}$) seri, $V(t)$ kaynağı. Çıkış bobin gerilimi $V_L$.
>
> **İstenen:** Çalışma noktası etrafında doğrusallaştırarak $\dfrac{V_L(s)}{V(s)}$.

> [!note]- Semboller
> - $V(t)$: kaynak gerilimi — giriş (V); $V_L$: bobin gerilimi — çıkış (V)
> - $i,i_r$: devre/direnç akımı (A); $V_r$: direnç gerilimi (V)
> - $L$: indüktans (H); doğrusal olmayan direnç: $i_r=2e^{0.1V_r}$
> - $i_0$: denge (çalışma) akımı; $\delta i$: küçük sapma
> - Doğrusallaştırma: $\ln\frac{i}{2}$'nin türevi $\frac1i$ → dengede $\frac{1}{i_0}$ eğimi
> - $s$: Laplace değişkeni (1/s)

**Hedef:** $V_L(s)/V(s)$

**Adım 1 — Ters çöz:** $V_r = 10\ln(i_r/2)$

**Adım 2 — KVL:**

$$L\frac{di}{dt} + 10\ln\!\frac{i}{2} - 20 = V(t)$$

**Adım 3 — Denge noktası** ($V=0$, $\dot{i}=0$):

$$10\ln\!\frac{i_0}{2} = 20 \implies i_0 = 2e^2 \approx 14.78 \text{ A}$$

**Adım 4 — Lineerizasyon** ($i = i_0 + \delta i$):

$$\ln\!\frac{i_0+\delta i}{2} \approx \ln\!\frac{i_0}{2} + \frac{1}{i_0}\,\delta i$$

Denge şartını çıkar:

$$L\frac{d(\delta i)}{dt} + \frac{10}{i_0}\,\delta i = V(t)$$

$$\frac{d(\delta i)}{dt} + \underbrace{\frac{10}{14.78}}_{0.677}\,\delta i = V(t)$$

**Adım 5 — Laplace:**

$$\delta I(s)(s + 0.677) = V(s) \implies \delta I(s) = \frac{V(s)}{s+0.677}$$

**Adım 6 — Çıkış** ($V_L = L\cdot s\cdot\delta I$, $L=1$):

$$\boxed{\frac{V_L(s)}{V(s)} = \frac{s}{s+0.677}}$$

*Yüksek geçiren karakteristik — saf DC girişe sıfır yanıt (beklenen: endüktör DC'de kısa devre)*

---

## Örnek 5 — cos x İçeren ODE Doğrusallaştırma (Hocanın Notu)

> [!example] Problem
> **Soru:** $\ddot{x} + 2\dot{x} + \cos x = 0$'ı $x_0 = \pi/4$ noktasında doğrusallaştırın. *(Çözümlü Örnek 4 ile aynı; bu, hocanın adım adım çözümüdür.)*

> [!note]- Semboller
> - $x,\dot x,\ddot x$: konum, hız, ivme; $x_0=\pi/4$: doğrusallaştırma noktası
> - $\delta x=x-x_0$: sapma değişkeni; $\delta X(s)$: Laplace dönüşümü
> - Taylor: $\cos(x_0+\delta x)\approx\cos x_0-\sin x_0\,\delta x$
> - $\cos\frac{\pi}{4}=\sin\frac{\pi}{4}=\frac{\sqrt2}{2}$; sabit terim basamak girişi gibi (Laplace'ı $\frac{1}{s}$ ile)

**Soru:** $\ddot{x} + 2\dot{x} + \cos x = 0$'ı $x_0 = \pi/4$ noktasında doğrusallaştırın.

**Adım 1 — Doğrusal olmayan terim:** $\cos x$

**Adım 2 — Taylor açılımı** ($x = x_0 + \delta x$):

$$\cos(x_0 + \delta x) \approx \cos(x_0) - \sin(x_0)\,\delta x$$

$$x_0 = \pi/4: \quad \cos\!\tfrac{\pi}{4} = \frac{\sqrt{2}}{2}, \quad \sin\!\tfrac{\pi}{4} = \frac{\sqrt{2}}{2}$$

$$\cos x \approx \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}\,\delta x$$

**Adım 3 — Doğrusallaştırılmış denklem:**

$$\frac{d^2(\delta x)}{dt^2} + 2\frac{d(\delta x)}{dt} + \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}\,\delta x = 0$$

$$\boxed{\frac{d^2(\delta x)}{dt^2} + 2\frac{d(\delta x)}{dt} - \frac{\sqrt{2}}{2}\,\delta x = -\frac{\sqrt{2}}{2}}$$

**Laplace (sıfır B.K.):**

$$\delta X(s)\!\left(s^2 + 2s - \frac{\sqrt{2}}{2}\right) = -\frac{\sqrt{2}/2}{s}$$

$$\delta X(s) = \frac{-\sqrt{2}/2}{s\!\left(s^2+2s-\frac{\sqrt{2}}{2}\right)}$$

---

## Örnek 6 — Faz Düzlemi: Denge Noktası Kararlılığı (Hocanın Notu)

> [!example] Problem
> **Soru:** $\ddot{x} + 0{,}6\dot{x} + 3x + x^2 = 0$ sisteminin denge noktalarını bulun ve her birinin kararlılığını (faz düzlemi tipiyle) inceleyin.

> [!note]- Semboller
> - $x_1=x$, $x_2=\dot x$: durum değişkenleri
> - Denge: $\dot x_1=\dot x_2=0$ → $x_2=0$ ve $x_1(x_1+3)=0$
> - $J=[\partial f_i/\partial x_j]$: Jacobian; her denge noktasında ayrı değerlendirilir
> - $\lambda$: özdeğer; **Kararlı Odak**: Re$<0$, karmaşık (spiral); **Eyer**: zıt işaretli gerçel
> - $0{,}6$: sönüm katsayısı; $3,1$: doğrusal ve karesel yay katsayıları

**Soru:** $\ddot{x} + 0{,}6\dot{x} + 3x + x^2 = 0$ sisteminin denge noktalarını bulun ve kararlılıklarını inceleyin.

**Adım 1 — Durum uzayı:**

$$x_1 = x, \quad \dot{x}_1 = x_2$$
$$\dot{x}_2 = -0{,}6x_2 - 3x_1 - x_1^2$$

**Adım 2 — Denge noktaları** ($\dot{x}_1=\dot{x}_2=0$):

$x_2=0$ ve $-3x_1-x_1^2 = x_1(x_1+3)=0$

$$\boxed{(x_1, x_2) = (0,0) \quad \text{ve} \quad (-3, 0)}$$

**Adım 3 — Jacobian:**

$$J = \begin{bmatrix} 0 & 1 \\ -3-2x_1 & -0{,}6 \end{bmatrix}$$

**Adım 4a — (0,0) noktası:**

$$J_{(0,0)} = \begin{bmatrix} 0 & 1 \\ -3 & -0{,}6 \end{bmatrix}$$

$$\det(\lambda I - J) = 0 \Rightarrow \lambda^2 + 0{,}6\lambda + 3 = 0 \Rightarrow \lambda_{1,2} = -0{,}3 \pm j1{,}71$$

$\text{Re}(\lambda)<0$ → **Kararlı Odak (Stable Focus)** — iç içe sarılan spiraller

**Adım 4b — (−3, 0) noktası:**

$$J_{(-3,0)} = \begin{bmatrix} 0 & 1 \\ 3 & -0{,}6 \end{bmatrix}$$

$$\lambda^2 + 0{,}6\lambda - 3 = 0 \Rightarrow \lambda_1 = 1{,}46, \quad \lambda_2 = -2{,}06$$

Zıt işaretli gerçel → **Eyer Noktası (Saddle)** — hem yaklaşır hem uzaklaşır
