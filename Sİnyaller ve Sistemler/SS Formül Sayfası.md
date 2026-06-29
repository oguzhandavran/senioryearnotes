---
tags: [ss, formül, cheatsheet]
---

# SS — Formül Sayfası

← [[SS Ana Sayfa]]

> Sınavda yanında tut. Tüm kritik formüller tek sayfada.

> [!key] 🔑 Kısaltma & Sembol Anahtarı (önce bunu oku)
> | Sembol | Okunuş / anlamı | Sembol | Okunuş / anlamı |
> |---|---|---|---|
> | $x(t)$ / $x[n]$ | CT / DT sinyal | $h$ | dürtü yanıtı |
> | $\delta$ | birim dürtü | $u$ | birim basamak |
> | $*$ | konvolüsyon | $\omega_0$ | temel açısal frekans $2\pi/T$ |
> | $a_k,c_n$ | Fourier serisi katsayısı | $\omega$ | açısal frekans (rad/s) |
> | $X(j\omega)$ | Fourier dönüşümü (spektrum) | $H(j\omega)$ | frekans yanıtı |
> | $E_\infty,P_\infty$ | enerji / güç | $\tau$ | konvolüsyon kukla değişkeni |
> | $\lvert\cdot\rvert$ | genlik/modül | $\angle$ | faz (açı) |
>
> **CT** = sürekli-zaman · **DT** = ayrık-zaman · **LTI** = doğrusal & zamanla-değişmez · **BIBO** = sınırlı giriş–sınırlı çıkış · **CTFS/CTFT** = sürekli-zaman Fourier serisi/dönüşümü · **PFD** = kısmi kesir ayrışımı.

---

## Sinyal Özellikleri

| İşlem | Formül |
|-------|--------|
| CT Enerji | $E_\infty = \int_{-\infty}^{\infty}\|x(t)\|^2 dt$ |
| DT Enerji | $E_\infty = \sum_{n=-\infty}^{\infty}\|x[n]\|^2$ |
| CT Güç | $P_\infty = \lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}\|x(t)\|^2 dt$ |
| DT Güç | $P_\infty = \lim_{N\to\infty}\frac{1}{2N+1}\sum_{n=-N}^{N}\|x[n]\|^2$ |
| Çift bileşen | $x_e(t) = \frac{x(t)+x(-t)}{2}$ |
| Tek bileşen | $x_o(t) = \frac{x(t)-x(-t)}{2}$ |

---

## LTI Sistem Özellikleri

| Özellik | Koşul |
|---------|-------|
| Hafızasız | Çıkış sadece $x[n]$'e bağlı |
| Nedensel | $x[n+k]$ ($k>0$) yok |
| Doğrusal | Süperpozisyon; $x=0 \Rightarrow y=0$ |
| ZD | Katsayıda bağımsız $n$ yok |
| Kararlı | $\sum\|h[n]\|<\infty$ veya $\int\|h(t)\|dt<\infty$ |

---

## Konvolüsyon

$$y(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau)d\tau$$

$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$

**Boyut:** $L_y = L_x + L_h - 1$; $n \in [N_1+M_1, N_2+M_2]$

---

## Fourier Serisi

| | CT | DT |
|-|----|----|
| Sentez | $x(t)=\sum_k a_k e^{jk\omega_0 t}$ | $x[n]=\sum_{k=\langle N\rangle} a_k e^{jk\omega_0 n}$ |
| Analiz | $a_k=\frac{1}{T}\int_T x(t)e^{-jk\omega_0 t}dt$ | $a_k=\frac{1}{N}\sum_{\langle N\rangle}x[n]e^{-jk\omega_0 n}$ |
| $\omega_0$ | $2\pi/T$ | $2\pi/N$ |
| Parseval | $\frac{1}{T}\int\|x\|^2=\sum\|a_k\|^2$ | $\frac{1}{N}\sum\|x[n]\|^2=\sum\|a_k\|^2$ |

---

## CTFT Çiftleri

| $x(t)$ | $X(j\omega)$ |
|--------|-------------|
| $\delta(t)$ | $1$ |
| $e^{-at}u(t)$ | $\frac{1}{a+j\omega}$ |
| $u(t)$ | $\pi\delta(\omega)+\frac{1}{j\omega}$ |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ |
| $\sin(\omega_0 t)$ | $\frac{\pi}{j}[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |

---

## DTFT Çiftleri

| $x[n]$ | $X(e^{j\omega})$ |
|--------|-----------------|
| $\delta[n]$ | $1$ |
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ |
| $a^n u[n]$, $\|a\|<1$ | $\frac{1}{1-ae^{-j\omega}}$ |
| $na^n u[n]$, $\|a\|<1$ | $\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ |
| Dikdörtgen pencere $[0,N-1]$ | $e^{-j\omega\frac{N-1}{2}}\frac{\sin(N\omega/2)}{\sin(\omega/2)}$ |

---

## Laplace Çiftleri

| $x(t)$ | $X(s)$ | ROC |
|--------|--------|-----|
| $\delta(t)$ | $1$ | Tümü |
| $u(t)$ | $\frac{1}{s}$ | $\text{Re}(s)>0$ |
| $e^{-at}u(t)$ | $\frac{1}{s+a}$ | $\text{Re}(s)>-a$ |
| $te^{-at}u(t)$ | $\frac{1}{(s+a)^2}$ | $\text{Re}(s)>-a$ |
| $\sin(\omega_0 t)u(t)$ | $\frac{\omega_0}{s^2+\omega_0^2}$ | $\text{Re}(s)>0$ |
| $\cos(\omega_0 t)u(t)$ | $\frac{s}{s^2+\omega_0^2}$ | $\text{Re}(s)>0$ |
| $e^{-at}\sin(\omega_0 t)u(t)$ | $\frac{\omega_0}{(s+a)^2+\omega_0^2}$ | $\text{Re}(s)>-a$ |
| $e^{-at}\cos(\omega_0 t)u(t)$ | $\frac{s+a}{(s+a)^2+\omega_0^2}$ | $\text{Re}(s)>-a$ |

---

## PFD (Kısmi Kesirler)

$$X(s) = \frac{N(s)}{D(s)}, \quad A_i = \lim_{s\to p_i}(s-p_i)X(s)$$

**Başlangıç değer:** $x(0^+) = \lim_{s\to\infty}sX(s)$

**Son değer:** $x(\infty) = \lim_{s\to 0}sX(s)$

---

## Euler Açılımları

$$e^{j\theta} = \cos\theta + j\sin\theta$$

$$\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}, \qquad \sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$$
