---
tags: [ss, final, sınav-soruları, çözümlü, fourier-serisi, fourier-dönüşümü, frekans-yanıtı, konvolüsyon]
---

# 06 — Final Sınav Soruları (Çözümlü)

← [[SS Ana Sayfa]]

> Kaynak görsel: `DATASET/Sinyaller Ve Sistemler/SS_Final_Sorular.jpg`

---

## Soru 1 — Sistem Özellikleri ve Konvolüsyon (25p)

**Verilen:**
$$x(t) = \begin{cases} 1, & 0 < t < 1 \\ -1, & 1 < t < 2 \\ 0, & \text{diğer} \end{cases}$$
$$h(t) = u(t) - u(t-2) = \begin{cases} 1, & 0 \leq t \leq 2 \\ 0, & \text{diğer} \end{cases}$$

> [!note]- Semboller
> - $x(t)$: giriş (±1 darbe çifti); $h(t)$: $[0,2]$ kapısı (dürtü yanıtı, genişlik 2)
> - $u(t)$: birim basamak; nedensellik: $h(t)=0,\ t<0$
> - BIBO: $\int|h|dt<\infty$; $\tau$: konvolüsyon değişkeni
> - $y(t)=\int_{t-2}^{t}x(\tau)d\tau$: genişliği 2 olan kayan pencere

---

### 1a — Sistem Özellikleri (9p)

| Özellik | Karar | Gerekçe |
|---------|-------|---------|
| **Nedensellik** | ✅ Nedensel | $h(t) = 0$ için $t < 0$ — sistem geleceği kullanmıyor |
| **Hafıza** | Hafızalı | $h(t) \neq \delta(t)$ — çıkış geçmiş girişlere bağımlı |
| **Kararlılık** | ✅ BIBO Kararlı | $\int_{-\infty}^{\infty}\|h(t)\|dt = \int_{0}^{2}1\,dt = 2 < \infty$ |

---

### 1b — Konvolüsyon y(t) (16p)

$$y(t) = \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$$

$h(t-\tau)=1$ için $0 \leq t-\tau \leq 2$, yani $t-2 \leq \tau \leq t$:

$$y(t) = \int_{t-2}^{t} x(\tau)\,d\tau$$

**Bölge analizi:**

**Bölge 1:** $t \leq 0$ → pencere tamamen sola → $y(t) = 0$

**Bölge 2:** $0 < t \leq 1$
Pencere $[t-2, t]$, $t-2 < 0$, kesişim $[0, t]$ ile $x=1$:
$$y(t) = \int_{0}^{t}1\,d\tau = t$$

**Bölge 3:** $1 < t \leq 2$
Pencere $[t-2, t]$, $t-2 \in (-1,0)$, kesişim $[0,1]$ ve $[1,t]$:
$$y(t) = \int_{0}^{1}1\,d\tau + \int_{1}^{t}(-1)\,d\tau = 1-(t-1) = 2-t$$

**Bölge 4:** $2 < t \leq 3$
Pencere $[t-2, t]$, $t-2 \in (0,1)$, $t > 2$ (x=0 için $\tau>2$):
$$y(t) = \int_{t-2}^{1}1\,d\tau + \int_{1}^{2}(-1)\,d\tau = (1-(t-2)) + (-1) = 2-t$$

**Bölge 5:** $3 < t \leq 4$
Pencere $[t-2, t]$, $t-2 \in (1,2)$, sadece $x=-1$ bölgesi:
$$y(t) = \int_{t-2}^{2}(-1)\,d\tau = -(2-(t-2)) = t-4$$

**Bölge 6:** $t > 4$ → $y(t) = 0$

$$\boxed{y(t) = \begin{cases} 0, & t \leq 0 \\ t, & 0 < t \leq 1 \\ 2-t, & 1 < t \leq 3 \\ t-4, & 3 < t \leq 4 \\ 0, & t > 4 \end{cases}}$$

**Grafik:**
```
y(t)
 1 |    /\
   |   /  \
   |  /    \
   | /      \        /
───┼──────────────/─────── t
   0  1  2  3  \/  4
              -1
```

**Süreklilik kontrolü:** $t=1$: $1=1$ ✓ | $t=3$: $2-3=-1=3-4$ ✓ | $t=4$: $0$ ✓

---

## Soru 2 — Fourier Serisi (25p)

**Verilen:**
$$x(t) = 2\sin\!\left(\frac{\pi}{4}t + \frac{\pi}{8}\right) + \cos\!\left(\frac{\pi}{2}t + \frac{\pi}{4}\right) - 1$$

> [!note]- Semboller
> - $\omega_1,\omega_2$: bileşen frekansları; $T_0=\text{OKK}(T_1,T_2)$: ortak periyot; $\omega_0=2\pi/T_0$: temel frekans
> - $c_n$: karmaşık Fourier katsayısı ($x=\sum_n c_n e^{jn\omega_0 t}$); $n$: harmonik indeksi
> - Euler: $\sin\theta=\frac{1}{2j}(e^{j\theta}-e^{-j\theta})$, $\cos\theta=\frac12(e^{j\theta}+e^{-j\theta})$
> - $-j=e^{-j\pi/2}$ → faz kaydırır; gerçel sinyalde $c_{-n}=c_n^*$ (|·| çift, ∠ tek)

---

### 2a — Fourier Seri Katsayıları (15p)

**Temel periyot:**
- $\omega_1 = \pi/4 \Rightarrow T_1 = 2\pi/(\pi/4) = 8$
- $\omega_2 = \pi/2 \Rightarrow T_2 = 2\pi/(\pi/2) = 4$
- $T_0 = \text{OKK}(8,4) = 8$ → **Temel frekans:** $\omega_0 = 2\pi/8 = \pi/4$

**Euler formuna dönüşüm:**

$$2\sin\!\left(\omega_0 t + \frac{\pi}{8}\right) = \frac{2}{2j}\left[e^{j(\omega_0 t+\pi/8)} - e^{-j(\omega_0 t+\pi/8)}\right] = -je^{j\pi/8}e^{j\omega_0 t} + je^{-j\pi/8}e^{-j\omega_0 t}$$

$$\cos\!\left(2\omega_0 t + \frac{\pi}{4}\right) = \frac{1}{2}e^{j\pi/4}e^{j2\omega_0 t} + \frac{1}{2}e^{-j\pi/4}e^{-j2\omega_0 t}$$

**Fourier katsayıları** $x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}$:

| n | $c_n$ | $\|c_n\|$ | $\angle c_n$ |
|---|-------|-----------|-------------|
| 0 | $-1$ | $1$ | $\pi$ rad |
| $+1$ | $-je^{j\pi/8} = e^{-j3\pi/8}$ | $1$ | $-3\pi/8$ rad |
| $-1$ | $je^{-j\pi/8} = e^{j3\pi/8}$ | $1$ | $+3\pi/8$ rad |
| $+2$ | $\frac{1}{2}e^{j\pi/4}$ | $1/2$ | $+\pi/4$ rad |
| $-2$ | $\frac{1}{2}e^{-j\pi/4}$ | $1/2$ | $-\pi/4$ rad |
| diğer | $0$ | — | — |

---

### 2b — Genlik ve Faz Spektrumları (10p)

**Genlik Spektrumu $|c_n|$:**
```
|cn|
 1 |  ×    ×    ×
   |
0.5|       ×         ×
   |
───┼──────────────────── n
  -2   -1   0   +1  +2
```

**Faz Spektrumu $\angle c_n$:**
```
∠cn (rad)
3π/8|       ×
    |
π/4 |                  ×
    |
  π |            ×
────┼──────────────────── n
   -2   -1   0   +1  +2
-π/4|   ×
    |
-3π/8|                ×
```

*(Çift simetri: $|c_n| = |c_{-n}|$ ve $\angle c_{-n} = -\angle c_n$ — karmaşık konjugat özelliği)*

---

## Soru 3 — Fourier Dönüşümü (25p)

**Verilen:**
$$x(t) = e^{1+t}u(1-t)$$

> [!note]- Semboller
> - $u(1-t)$: $t\le1$'de 1 olan **yansımış** basamak (sağ tarafı keser)
> - $x(t)=e^{1+t}$ ($t\le1$): sola doğru sönen üstel; destek $(-\infty,1]$
> - $X(j\omega)=\int x(t)e^{-j\omega t}dt$: CTFT
> - Yakınsama: $\mathrm{Re}(1-j\omega)=1>0$ → integral $-\infty$'da sıfıra gider
> - $|X|$: genlik, $\angle X$: faz spektrumu

$u(1-t) = 1$ için $t \leq 1$, yani $x(t) = e^{1+t}$ ($t \leq 1$), $0$ ($t > 1$).

**Fourier Dönüşümü:**
$$X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}\,dt = \int_{-\infty}^{1} e^{1+t}e^{-j\omega t}\,dt$$

$$= e\int_{-\infty}^{1} e^{(1-j\omega)t}\,dt$$

**Yakınsama:** $t\to-\infty$ için $e^{(1-j\omega)t} \to 0$ çünkü $\text{Re}(1-j\omega) = 1 > 0$ ✓

$$= e\left[\frac{e^{(1-j\omega)t}}{1-j\omega}\right]_{-\infty}^{1} = e \cdot \frac{e^{1-j\omega}}{1-j\omega}$$

$$\boxed{X(j\omega) = \frac{e^2 \cdot e^{-j\omega}}{1-j\omega}}$$

**Not:** $|X(j\omega)| = \dfrac{e^2}{\sqrt{1+\omega^2}}$. Faz: $\angle X = \underbrace{-\omega}_{\angle e^{-j\omega}} - \underbrace{\angle(1-j\omega)}_{-\arctan\omega} = -\omega + \arctan(\omega)$ ($e^2$ pozitif gerçel, faza katkısı 0).

---

## Soru 4 — Frekans Yanıtı ile Sistem Çıkışı (25p)

**Verilen:**
$$H(j\omega) = \frac{j\omega+4}{2-\omega^2+3j\omega}$$
$$x(t) = e^{-4(t-2)}u(t-2)$$

> [!note]- Semboller
> - $H(j\omega)$: frekans yanıtı; $s=j\omega$ ile $-\omega^2+3j\omega+2 = s^2+3s+2$
> - $x(t)$: 2 birim gecikmeli üstel; zaman kaydırma $f(t-2)\leftrightarrow e^{-2j\omega}F(j\omega)$
> - $Y=H\cdot X$: çıkış spektrumu; $A,B$: kısmi kesir katsayıları
> - Ters çift: $\frac{1}{j\omega+a}\leftrightarrow e^{-at}u(t)$; kutuplar $-1,-2$ → kararlı

---

### Adım 1 — Paydayı Çarpanlara Ayır

$s = j\omega$ yerine koyunca:
$$2 - \omega^2 + 3j\omega = s^2 + 3s + 2 = (s+1)(s+2) = (j\omega+1)(j\omega+2)$$

$$\boxed{H(j\omega) = \frac{j\omega+4}{(j\omega+1)(j\omega+2)}}$$

---

### Adım 2 — X(jω) Bul

$x(t) = e^{-4(t-2)}u(t-2)$: $f(t) = e^{-4t}u(t)$'nin 2 birim gecikmesi.

$$\mathcal{F}\{e^{-4t}u(t)\} = \frac{1}{j\omega+4}$$

**Zaman kaydırma teoremi:** $x(t) = f(t-2) \Rightarrow X(j\omega) = F(j\omega)\,e^{-2j\omega}$

$$X(j\omega) = \frac{e^{-2j\omega}}{j\omega+4}$$

---

### Adım 3 — Y(jω) Hesapla

$$Y(j\omega) = H(j\omega)\,X(j\omega) = \frac{j\omega+4}{(j\omega+1)(j\omega+2)} \cdot \frac{e^{-2j\omega}}{j\omega+4}$$

$$Y(j\omega) = \frac{e^{-2j\omega}}{(j\omega+1)(j\omega+2)}$$

---

### Adım 4 — Kısmi Kesirler

$$\frac{1}{(j\omega+1)(j\omega+2)} = \frac{A}{j\omega+1} + \frac{B}{j\omega+2}$$

$$A = \lim_{j\omega \to -1}\frac{1}{j\omega+2} = \frac{1}{1} = 1$$

$$B = \lim_{j\omega \to -2}\frac{1}{j\omega+1} = \frac{1}{-1} = -1$$

$$Y(j\omega) = e^{-2j\omega}\left[\frac{1}{j\omega+1} - \frac{1}{j\omega+2}\right]$$

---

### Adım 5 — Ters Fourier

$\dfrac{1}{j\omega+a} \xleftrightarrow{\mathcal{F}^{-1}} e^{-at}u(t)$

$e^{-2j\omega}F(j\omega) \xleftrightarrow{\mathcal{F}^{-1}} f(t-2)$

$$\boxed{y(t) = \left[e^{-(t-2)} - e^{-2(t-2)}\right]u(t-2)}$$

**Yorum:**
- $t < 2$: $y(t) = 0$ (sistem nedensel, giriş $t=2$'de başlıyor)
- $t \geq 2$: çıkış iki üstel bileşenin farkı; $e^{-(t-2)}$ daha yavaş söner
- Uzun vadede: $y(t) \to 0$ (kararlı sistem, $\text{Re}(p_{1,2}) < 0$)
