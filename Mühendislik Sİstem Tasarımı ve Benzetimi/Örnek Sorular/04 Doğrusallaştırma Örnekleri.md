---
tags: [mst, doğrusallaştırma, linearization, taylor, jacobian, denge-noktası, örnek-sorular]
---

# 04 — Doğrusallaştırma Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/04 Doğrusallaştırma|04 Doğrusallaştırma]]

---

## Çözümlü Örnek 1: Basit Sarkaç

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

**Diyot denklemi:** $i = I_s(e^{v/(nV_T)} - 1) \approx I_s e^{v/(nV_T)}$

**Çalışma noktası:** $(V_Q, I_Q)$

**Küçük sinyal modeli (lineerleştirilmiş):**

$$g_m = \left.\frac{di}{dv}\right|_{V_Q} = \frac{I_Q}{nV_T}$$

$$\delta i = g_m \delta v$$

---

## Çözümlü Örnek 4 — Trigonometrik Nonlineer Sistem ($x_e = \pi/4$)

**Sistem:** $\ddot{x} + 2\dot{x} + \cos x = 0$

**Doğrusal olmayan kısım:** $\cos x$

**Denge noktası bulma** ($\ddot{x}=\dot{x}=0$): $\cos x_e = 0 \implies x_e = \pi/2$ (veya $x_e = \pi/4$'te analiz istendi)

**$x_e = \pi/4$ etrafında Taylor açılımı:**

$x = \delta x + \pi/4$ (minimal sapma) yaz:

$$\frac{d^2(\delta x)}{dt^2} + 2\frac{d(\delta x)}{dt} + \cos\!\left(\delta x + \frac{\pi}{4}\right) = 0$$

$\cos$ için Taylor:

$$\cos\!\left(\delta x + \frac{\pi}{4}\right) \approx \cos\!\left(\frac{\pi}{4}\right) - \sin\!\left(\frac{\pi}{4}\right)\cdot\delta x = \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}\,\delta x$$

Denklem:

$$\ddot{\delta x} + 2\dot{\delta x} + \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}\,\delta x = 0$$

Sabit terimi ($1/\sqrt{2}$) sağa al ve Laplace'a geç:

$$\delta X(s)\!\left(s^2 + 2s - \frac{\sqrt{2}}{2}\right) = -\frac{\sqrt{2}}{2}$$

$$\boxed{\delta X(s) = \frac{-\sqrt{2}/2}{s^2+2s-\sqrt{2}/2}}$$

Özdeğerler: $s = -1 \pm \sqrt{1+\sqrt{2}/2} \approx -1 \pm 1.30$ → $s_1 \approx 0.30 > 0$ → **kararsız denge** (saddle point bölgesi)

---

## Çözümlü Örnek 5 — Doğrusal Olmayan Direnç Devresi

**Devre:** $L=1$ H endüktör + nonlineer direnç ($i_r = 2e^{0.1V_r}$) + $V(t)$ gerilim kaynağı, $V_r$ çıkış

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
