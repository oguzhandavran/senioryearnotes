---
tags: [mst, formül, özet, kopya-kağıdı]
aliases: [MST Formüller]
---

# MST — Formül Sayfası (Kopya Kağıdı)

← [[MST Ana Sayfa]]

---

## Mekanik Sistemler

$$\boxed{G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}}$$

| Eleman | Kuvvet | Laplace Empedans |
|--------|--------|------------------|
| Kütle $m$ | $F = m\ddot{x}$ | $ms^2$ |
| Yay $k$ | $F = kx$ | $k$ |
| Sönümleyici $b$ | $F = b\dot{x}$ | $bs$ |

**Lagrange:** $\dfrac{d}{dt}\!\left(\dfrac{\partial T}{\partial \dot{q}_i}\right) - \dfrac{\partial T}{\partial q_i} + \dfrac{\partial V}{\partial q_i} + \dfrac{\partial D}{\partial \dot{q}_i} = Q_i$

<span style="color:rgb(255, 255, 0)">> [!tip] T — Kinetik Enerji<br>> $$T = \frac{1}{2}m\dot{q}^2 \quad \text{veya} \quad T = \frac{1}{2}I\dot{\theta}^2$$</span>

<span style="color:rgb(255, 255, 0)">> [!example] V — Potansiyel Enerji<br>> $$V = \frac{1}{2}kq^2$$</span>

<span style="color:rgb(255, 255, 0)">> [!warning] D — Rayleigh Dissipation (Sönüm)<br>> $$D = \frac{1}{2}b\dot{q}^2$$</span>

<span style="color:rgb(255, 255, 0)"><span style="color:rgb(255, 255, 0)"><span style="color:rgb(255, 255, 0)">> [!info] Koordinatlar ve Kuvvetler<br>> - <b>q<i>i</b>: Genelleştirilmiş koordinat (konum)<br>> - <b>Q</i>i</b>: Genelleştirilmiş dış kuvvet (uygulanmış)</span></span></span>

---

## Elektrik Sistemleri

| Eleman | $v$-$i$ | Empedans |
|--------|---------|----------|
| $R$ | $v=Ri$ | $R$ |
| $L$ | $v=L\dot{i}$ | $Ls$ |
| $C$ | $i=C\dot{v}$ | $1/(Cs)$ |

**RLC Seri:** $G(s) = \dfrac{V_C}{V_{in}} = \dfrac{1/LC}{s^2 + (R/L)s + 1/(LC)}$

**Gerilim bölücü:** $V_2 = V_{in} \cdot \dfrac{Z_2}{Z_1+Z_2}$

---

## Durum Uzayı

$$\dot{x} = Ax + Bu, \qquad y = Cx + Du$$

$$\boxed{G(s) = C(sI - A)^{-1}B + D}$$

**Kontrolör canonical form** (TF → SS):

$$A = \begin{bmatrix} 0 & 1 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ -a_0 & -a_1 & \cdots & -a_{n-1} \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ \vdots \\ 1 \end{bmatrix}$$

**Özdeğerler** (kararlılık): $\det(\lambda I - A) = 0$

Tüm $\text{Re}(\lambda_i) < 0 \implies$ **kararlı**

**Kontrol edilebilirlik:** $\text{rank}\begin{bmatrix}B & AB & \cdots & A^{n-1}B\end{bmatrix} = n$

---

## Doğrusallaştırma

**Denge noktası:** $f(x_e, u_e) = 0$

**Lineer model:**
$$\delta\dot{x} = A\,\delta x + B\,\delta u$$

$$A = \left.\frac{\partial f}{\partial x}\right|_{x_e, u_e}, \qquad B = \left.\frac{\partial f}{\partial u}\right|_{x_e, u_e}$$

**Küçük açı:** $\sin\theta \approx \theta$, $\cos\theta \approx 1$ (radyan)

---

## Kompansatörler

| Tür | Transfer Fonksiyonu | Etki |
|-----|--------------------|----- |
| PD | $K_c(s+z_c)$ | Sıfır ekler, hızlandırır |
| PI | $K_c\dfrac{s+z_c}{s}$ | Kutup orijinde, hata sıfırlar |
| PID | $K_c\dfrac{(s+z_1)(s+z_2)}{s}$ | İkisi birden |
| Lead | $K_c\dfrac{s+z_c}{s+p_c}$, $z_c < p_c$ | PM artırır |
| Lag | $K_c\dfrac{s+z_c}{s+p_c}$, $z_c > p_c$ | Düşük f kazancı artırır |

**Açı şartı:** $\angle G_c(s_d)G_p(s_d) = \pm 180°$

**Genlik şartı:** $|K_c G_p(s_d)| = 1$

---

## KYE Hızlı Referans

$$\theta_q = \frac{(2q+1)\cdot 180°}{n-m}, \qquad \sigma_a = \frac{\sum p_i - \sum z_j}{n-m}$$

**Breakaway:** $\displaystyle\sum_{\text{kutup}} \frac{1}{s-p_i} = \sum_{\text{sıfır}} \frac{1}{s-z_j}$

---

## 2. Derece Sistem

$$G(s) = \frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$$

| | Formül |
|-|--------|
| $T_s$ (%2) | $4/(\zeta\omega_n)$ |
| $T_p$ | $\pi/\omega_d$ |
| $\%OS$ | $100 e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| $\omega_d$ | $\omega_n\sqrt{1-\zeta^2}$ |

$\zeta \leftarrow \%OS$: $\zeta = \dfrac{-\ln(\%OS/100)}{\sqrt{\pi^2+\ln^2(\%OS/100)}}$

---

## Matris Tersi (2×2)

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies A^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

**$(sI-A)^{-1}$ için:** adj$(sI-A)$ / $\det(sI-A)$

---

## Hızlı Laplace

| $f(t)$ | $F(s)$ |
|--------|--------|
| $\delta(t)$ | $1$ |
| $u(t)$ | $1/s$ |
| $e^{-at}$ | $1/(s+a)$ |
| $\sin\omega t$ | $\omega/(s^2+\omega^2)$ |
| $\cos\omega t$ | $s/(s^2+\omega^2)$ |
| $te^{-at}$ | $1/(s+a)^2$ |
| $f'(t)$ | $sF(s)-f(0)$ |

**Son değer:** $\lim_{t\to\infty} f(t) = \lim_{s\to 0} sF(s)$
