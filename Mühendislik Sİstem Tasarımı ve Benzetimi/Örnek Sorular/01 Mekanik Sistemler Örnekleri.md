---
tags: [mst, mekanik, newton, lagrange, transfer-fonksiyonu, dc-motor, disli, örnek-sorular]
---

# 01 — Mekanik Sistemler Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Mekanik Sistemler|01 Mekanik Sistemler]]

---

## DC Motor + Dişli Sistemi Tam Örneği

> [!example] Problem
> **Veri:** 12 V DC motor; $T_{stall}=100$ Nm, $\omega_{no-load}=1333.3$ rad/s  
> $J_a=7$ kg·m², $D_a=3$ Nm·s/rad, $J_L=105$ kg·m²  
> Dişli: $N_1=12,\ N_2=25$ (1. kademe), $N_3=25,\ N_4=92$ (2. kademe)
>
> **İstenen:** $\displaystyle \frac{\Theta_m(s)}{E_a(s)}$ transfer fonksiyonu

> [!note]- Semboller — DC Motor + Dişli
> - $T_{stall}$: kilitlenme (stall) torku — mil tutuluyken motorun ürettiği maksimum tork (Nm)
> - $\omega_{no-load}$: boşta (yüksüz) dönüş hızı — yük yokken ulaşılan maksimum hız (rad/s)
> - $J_a$: armatür ataleti — motor milinin kendi dönme ataleti (kg·m²)
> - $D_a$: viskoz sönüm — hızla orantılı sürtünme (Nm·s/rad)
> - $J_L$: yük ataleti (kg·m²)
> - $N_1,\dots,N_4$: dişli çark diş sayıları (birimsiz)
> - $n=\dfrac{N_1 N_3}{N_2 N_4}$: toplam dişli oranı (birimsiz)
> - $J_m$: motora yansıtılmış toplam atalet (kg·m²)
> - $K_t$: tork sabiti — akımı torka çevirir (Nm/A)
> - $R_a$: armatür direnci (Ω)
> - $K_b$: zıt-EMK (back-EMF) sabiti — hızı gerilime çevirir (V·s/rad)
> - $E_a$: armatür gerilimi — sistemin girişi (V)
> - $\theta_m,\dot\theta_m,\ddot\theta_m$: motor açısı, açısal hızı, açısal ivmesi (rad, rad/s, rad/s²)
> - $s$: Laplace değişkeni (1/s)
> - $G(s)=\Theta_m(s)/E_a(s)$: aranan transfer fonksiyonu

---

**─── ADIM 1 — Toplam Dişli Oranı ───**

Her kademe ayrı:
$$n_1 = \frac{N_1}{N_2} = \frac{12}{25} = 0.48, \qquad n_2 = \frac{N_3}{N_4} = \frac{25}{92} \approx 0.2717$$

Toplam (ardışık çarpım):
$$n = n_1 \cdot n_2 = \frac{N_1 N_3}{N_2 N_4} = \frac{12 \times 25}{25 \times 92} = \frac{1}{36}$$

**Fizik:** Motor 36 tur → yük 1 tur. Tork 36 kat artar, hız 36'da biri.

---

**─── ADIM 2 — Yansıtılmış Atalet ───**

Yük ataleti $n^2$ faktörüyle motora yansır (kinetik enerji korunumu):
$$J_{L,\text{yansıyan}} = J_L \cdot n^2 = 105 \cdot \left(\frac{1}{36}\right)^2 = \frac{105}{1296} \approx 0.081\ \text{kg·m}^2$$

Toplam atalet (motor + yansıyan yük):
$$J_m = J_a + J_{L,\text{yansıyan}} = 7 + 0.081 = 7.081\ \text{kg·m}^2$$

---

**─── ADIM 3 — Motor Parametreleri ───**

**a) $K_t/R_a$ (kilitlenme/stall):** Motor dönmezken ($\omega=0$), $E_a = R_a i_a$, $T_{stall}=K_t i_a$
$$\frac{K_t}{R_a} = \frac{T_{stall}}{E_a} = \frac{100}{12} = 8.33\ \text{Nm/V}$$

**b) $K_b$ (boşta/no-load):** Yük yokken ($T=0 \to i_a\approx0$), $E_a \approx K_b \omega_{no-load}$
$$K_b = \frac{E_a}{\omega_{no-load}} = \frac{12}{1333.3} \approx 0.009\ \text{V·s/rad}$$

---

**─── ADIM 4 — Motor Denklemleri ───**

**[1] Elektrik (Kirchoff):** $E_a = R_a i_a + K_b \dot\theta_m \;\longrightarrow\; i_a = \dfrac{E_a - K_b \dot\theta_m}{R_a}$

**[2] Mekanik (Newton-dönel):** $K_t i_a = J_m \ddot\theta_m + D_a \dot\theta_m$

**[2]'ye [1]'i koy:** $\displaystyle K_t \cdot \frac{E_a - K_b \dot\theta_m}{R_a} = J_m \ddot\theta_m + D_a \dot\theta_m$

**Düzenle:**
$$\frac{K_t}{R_a} E_a = J_m \ddot\theta_m + \left(D_a + \frac{K_t K_b}{R_a}\right) \dot\theta_m \quad\leftarrow \text{HAREKET DENKLEMİ}$$

---

**─── ADIM 5 — Laplace Dönüşümü ───**

Sıfır başlangıç: $\ddot\theta_m \to s^2\Theta_m(s)$, $\;\dot\theta_m \to s\Theta_m(s)$, $\;E_a \to E_a(s)$

$$\frac{K_t}{R_a} E_a(s) = J_m s^2 \Theta_m(s) + \left(D_a + \frac{K_t K_b}{R_a}\right) s \Theta_m(s)$$

$s\Theta_m(s)$ parantezine al:
$$\frac{K_t}{R_a} E_a(s) = s \Theta_m(s) \left[ J_m s + \left(D_a + \frac{K_t K_b}{R_a}\right) \right]$$

Transfer fonksiyonu:
$$G(s) = \frac{\Theta_m(s)}{E_a(s)} = \frac{K_t/R_a}{s \left[ J_m s + \left(D_a + \dfrac{K_t K_b}{R_a}\right) \right]}$$

Payı ve paydayı $J_m$'e bölüp standart forma getir:
$$G(s) = \frac{\dfrac{K_t/R_a}{J_m}}{s \left( s + \dfrac{D_a + K_t K_b/R_a}{J_m} \right)}$$

---

**─── ADIM 6 — Sayısal Değerleri Koy ───**

| Büyüklük | Değer | Kaynak |
|----------|-------|--------|
| $J_m$ | $7.081$ kg·m² | Adım 2 |
| $K_t/R_a$ | $8.33$ Nm/V | Adım 3a |
| $K_b$ | $0.009$ V·s/rad | Adım 3b |
| $D_a$ | $3$ Nm·s/rad | Veri |

**①** $K_t K_b / R_a = 8.33 \times 0.009 = 0.075$ *(elektriksel sönüm)*

**②** $D_{\text{toplam}} = D_a + \dfrac{K_t K_b}{R_a} = 3 + 0.075 = 3.075$

**③** $a = \dfrac{D_{\text{toplam}}}{J_m} = \dfrac{3.075}{7.081} \approx 0.434$

**④** $K = \dfrac{K_t/R_a}{J_m} = \dfrac{8.33}{7.081} \approx 1.176$

$$\boxed{\frac{\Theta_m(s)}{E_a(s)} = \frac{1.176}{s(s + 0.434)}}$$

> Orijinal kaynak $0.839/(s(s+0.309))$ demiş — bu fark, orada $J_m$'e $D_a$'nın da eklendiği farklı bir toplam atalet kullanıldığı için oluşur. Buradaki türetim saf fiziksel modeli gösterir.

---

**─── ADIM 7 — TF'nin Yorumu ───**

$$G(s) = \frac{1.176}{s(s+0.434)}$$

| Sembol | Nedir? | Anlamı |
|--------|--------|--------|
| Paydaki $s$ | **İntegral** (Tip 1 sistem) | Gerilim verince motor sürekli döner, konum birikir |
| $(s+0.434)$ | **1. derece gecikme** | Zaman sabiti $\tau = 1/0.434 \approx 2.3$ s |
| $1.176$ | **Kazanç** | 1 V uygulanırsa motor kalıcı durumda ramp şeklinde döner |

**Karşılık gelen doğrusal sistem:** $m\ddot x + b\dot x = F$ → sadece kütle+sönüm, yay yok.

---

## Mekanik Örnek 1 — Newton ve Lagrange Karşılaştırması

> [!example] Problem
> **Sistem:** Bir kütle $m$; üstten/soldan bir yay $k$ ve buna paralel bir sönümleyici $b$ ile zemine bağlı. Kütleye dışarıdan $F(t)$ kuvveti uygulanıyor, konumu $x$.
>
> **İstenen:** Hareket denklemini hem **Newton** hem **Lagrange** yöntemiyle çıkar ve $G(s)=X(s)/F(s)$ transfer fonksiyonunu bul.

> [!note]- Semboller
> - $m$: kütle (kg)
> - $k$: yay sabiti (N/m)
> - $b$: viskoz sönüm katsayısı (N·s/m)
> - $F$: dış kuvvet — giriş (N)
> - $x,\dot x,\ddot x$: konum, hız, ivme (m, m/s, m/s²)
> - $T=\tfrac12 m\dot x^2$: kinetik enerji (J)
> - $V=\tfrac12 kx^2$: potansiyel (yay) enerjisi (J)
> - $D=\tfrac12 b\dot x^2$: Rayleigh sönüm fonksiyonu (J)
> - $L=T-V$: Lagrangian (J)
> - $s$: Laplace değişkeni (1/s); $G(s)=X(s)/F(s)$: transfer fonksiyonu

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2.2mm}}]
% Zemin
\draw[very thick] (-1,0) -- (2,0);
\foreach \x in {-0.8,-0.4,...,1.8}{ \draw (\x,0) -- (\x-0.28,-0.28); }
% Kütle
\draw[very thick, fill=blue!5] (-0.5,2.0) rectangle (1.5,3.2);
\node at (0.5,2.6) {\large $m$};
% Yay (sol, dikey)
\draw[spring] (0,0) -- (0,2.0);
\node at (-0.45,1.0) {$k$};
% Sönümleyici (sağ, dikey)
\draw[thick] (1,2.0) -- (1,1.45);
\draw[thick] (0.72,0.95) rectangle (1.28,1.45);
\draw[thick] (0.78,1.32) -- (1.22,1.32);
\draw[thick] (1,0.95) -- (1,0);
\node at (1.5,1.2) {$b$};
% Kuvvet F
\draw[->, red!70!black, very thick] (0.5,4.3) -- (0.5,3.2) node[midway, right]{$F$};
% x
\draw[->, thick] (-0.9,3.1) -- (-0.9,2.3) node[midway, left]{$x$};
\end{tikzpicture}
\end{document}
```

**a) Newton (kuvvet dengesi):** Kütleye etkiyen kuvvetler — dış kuvvet $F$ (aşağı/pozitif), yay geri çağırma $-kx$, sönüm direnci $-b\dot x$. Newton'un 2. yasası $\sum F = m\ddot x$:

$$m\ddot x = F - kx - b\dot x \;\Longrightarrow\; m\ddot{x} + b\dot{x} + kx = F(t)$$

Laplace (sıfır başlangıç, $\ddot x\to s^2X$, $\dot x\to sX$):

$$(ms^2+bs+k)X(s) = F(s) \;\Longrightarrow\; \boxed{G(s) = \dfrac{X(s)}{F(s)} = \dfrac{1}{ms^2+bs+k}}$$

**b) Lagrange (enerji yöntemi):** Üç enerji terimini yaz:

$$T=\tfrac{1}{2}m\dot{x}^2,\qquad V=\tfrac{1}{2}kx^2,\qquad D=\tfrac{1}{2}b\dot{x}^2$$

Lagrangian $L=T-V=\tfrac12 m\dot x^2-\tfrac12 kx^2$. Lagrange–Rayleigh denklemini kur:

$$\frac{d}{dt}\!\left(\frac{\partial L}{\partial\dot{x}}\right)-\frac{\partial L}{\partial x}+\frac{\partial D}{\partial\dot{x}}=F$$

Her parçayı tek tek hesapla:

$$\frac{\partial L}{\partial\dot x}=m\dot x \;\Rightarrow\; \frac{d}{dt}(m\dot x)=m\ddot x,\qquad \frac{\partial L}{\partial x}=-kx,\qquad \frac{\partial D}{\partial\dot x}=b\dot x$$

Yerine koy: $\;m\ddot x-(-kx)+b\dot x=F \implies m\ddot{x}+b\dot{x}+kx=F \quad\checkmark$ (Newton ile **birebir aynı**).

---

## Mekanik Örnek 2 — İki Kütleli Sistem (Lagrange)

> [!example] Problem
> **Sistem:** Duvara bağlı seri zincir — duvar → ($k_1$ yay ∥ $b_1$ sönümleyici) → $m_1$ → ($k_2$ yay ∥ $b_2$ sönümleyici) → $m_2$. Yatay hareket, dış kuvvet yok (serbest titreşim). Kütle konumları $x_1$ ve $x_2$.
>
> **İstenen:** Lagrange ile iki hareket denklemini çıkar ve $M\ddot x+C\dot x+Kx=0$ matris formunu yaz.

> [!note]- Semboller
> - $m_1,m_2$: kütleler (kg)
> - $k_1,k_2$: yay sabitleri (N/m)
> - $b_1,b_2$: viskoz sönüm katsayıları (N·s/m)
> - $x_1,x_2$: kütle konumları (m); $\dot x,\ddot x$: hız, ivme
> - $x_2-x_1$: $k_2/b_2$ elemanının uzaması (iki kütle **arasındaki** göreli hareket)
> - $T,V,D$: kinetik enerji, yay enerjisi, Rayleigh sönüm fonksiyonu (J)
> - $M,C,K$: kütle, sönüm, rijitlik matrisleri

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2mm}}]
% Duvar
\draw[very thick] (0,-0.9) -- (0,0.9);
\foreach \y in {-0.7,-0.3,...,0.9}{ \draw (0,\y) -- (-0.28,\y-0.22); }
% k1 (üst), b1 (alt): duvar -> m1
\draw[spring] (0,0.45) -- (2,0.45); \node at (1,0.95){$k_1$};
\draw[thick] (0,-0.45) -- (0.7,-0.45);
\draw[thick] (0.7,-0.72) rectangle (1.25,-0.18);
\draw[thick] (1.12,-0.65) -- (1.12,-0.25);
\draw[thick] (1.0,-0.45) -- (2,-0.45);
\node at (0.95,-1.0){$b_1$};
% m1
\draw[very thick, fill=blue!5] (2,-0.75) rectangle (3.1,0.75); \node at (2.55,0){$m_1$};
% k2 (üst), b2 (alt): m1 -> m2
\draw[spring] (3.1,0.45) -- (5,0.45); \node at (4.05,0.95){$k_2$};
\draw[thick] (3.1,-0.45) -- (3.8,-0.45);
\draw[thick] (3.8,-0.72) rectangle (4.35,-0.18);
\draw[thick] (4.22,-0.65) -- (4.22,-0.25);
\draw[thick] (4.1,-0.45) -- (5,-0.45);
\node at (4.05,-1.0){$b_2$};
% m2
\draw[very thick, fill=blue!5] (5,-0.75) rectangle (6.1,0.75); \node at (5.55,0){$m_2$};
% x1, x2
\draw[->, thick] (2.2,1.2) -- (3.0,1.2) node[right]{$x_1$};
\draw[->, thick] (5.2,1.2) -- (6.0,1.2) node[right]{$x_2$};
\end{tikzpicture}
\end{document}
```

**Adım 1 — Enerjileri yaz.** İkinci yay/sönümleyici iki kütle *arasında* olduğu için göreli hareket $x_2-x_1$ kullanılır:

$$T=\tfrac{1}{2}m_1\dot{x}_1^2+\tfrac{1}{2}m_2\dot{x}_2^2,\quad V=\tfrac{1}{2}k_1x_1^2+\tfrac{1}{2}k_2(x_2-x_1)^2,\quad D=\tfrac{1}{2}b_1\dot{x}_1^2+\tfrac{1}{2}b_2(\dot{x}_2-\dot{x}_1)^2$$

**Adım 2 — $x_1$ denklemi.** $\dfrac{d}{dt}\!\left(\dfrac{\partial L}{\partial\dot x_1}\right)-\dfrac{\partial L}{\partial x_1}+\dfrac{\partial D}{\partial\dot x_1}=0$ için her terim:

$$\frac{\partial L}{\partial\dot x_1}=m_1\dot x_1\Rightarrow\frac{d}{dt}=m_1\ddot x_1,\quad \frac{\partial L}{\partial x_1}=-k_1x_1+k_2(x_2-x_1),\quad \frac{\partial D}{\partial\dot x_1}=b_1\dot x_1-b_2(\dot x_2-\dot x_1)$$

Toplayıp düzenle (zincir kuralı $x_1$ türevinde $(x_2-x_1)$'i $-1$ ile çarpar):

$$\boxed{m_1\ddot{x}_1 + (b_1+b_2)\dot{x}_1 - b_2\dot{x}_2 + (k_1+k_2)x_1 - k_2x_2 = 0}$$

**Adım 3 — $x_2$ denklemi.** Aynı işlem $x_2$ için ($\partial V/\partial x_2=k_2(x_2-x_1)$, $\partial D/\partial\dot x_2=b_2(\dot x_2-\dot x_1)$):

$$\boxed{m_2\ddot{x}_2 + b_2\dot{x}_2 - b_2\dot{x}_1 + k_2x_2 - k_2x_1 = 0}$$

**Matris formu:** $M\ddot{x} + C\dot{x} + Kx = 0$ (serbest titreşim) — katsayıları matrise dizdiğimizde:

$$M = \begin{bmatrix}m_1&0\\0&m_2\end{bmatrix},\quad C = \begin{bmatrix}b_1+b_2&-b_2\\-b_2&b_2\end{bmatrix},\quad K = \begin{bmatrix}k_1+k_2&-k_2\\-k_2&k_2\end{bmatrix}$$

> Matrislerin **köşegen dışı** ($-b_2$, $-k_2$) terimleri iki kütleyi birbirine bağlayan ikinci eleman yüzünden çıkar; bunlar olmasaydı sistem iki bağımsız kütleye ayrılırdı.

---

## Mekanik Örnek 3 — Sayısal: $k=6$, $m=1$, $b=5$

> [!example] Problem
> **Veri:** $m=1$ kg, $k=6$ N/m, $b=5$ N·s/m  
> Dikey sistem: yay üstten tavana, sönümleyici alttan zemine. Kütle $y$ kadar sıkıştırılıp serbest bırakılıyor.  
> TF: $\displaystyle \frac{X(s)}{Y(s)} = \frac{1}{s^2+5s+6}$

> [!note]- Semboller
> - $m,k,b$: kütle (kg), yay sabiti (N/m), sönüm (N·s/m)
> - $y$: giriş — başlangıç sıkıştırma miktarı (m); $Y(s)$: Laplace dönüşümü
> - $x(t)$: kütlenin konumu (m); $X(s)$: Laplace dönüşümü
> - $\omega_n=\sqrt{k/m}$: doğal frekans (rad/s) — sönümsüz salınım hızı
> - $\zeta=\dfrac{b}{2\sqrt{mk}}$: sönüm oranı (birimsiz) — $\zeta>1$ aşırı sönümlü
> - $s_1,s_2$: kutuplar (karakteristik kökler, 1/s)
> - $A,B,C$: kısmi kesir (PFE) katsayıları
> - $x(\infty)$: kalıcı durum değeri (m)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2.2mm}}]
% Tavan
\draw[very thick] (-1,4) -- (1.5,4);
\foreach \x in {-0.8,-0.4,...,1.4}{ \draw (\x,4) -- (\x-0.28,4.28); }
% Zemin
\draw[very thick] (-1,0) -- (1.5,0);
\foreach \x in {-0.8,-0.4,...,1.4}{ \draw (\x,0) -- (\x-0.28,-0.28); }
% Kütle
\draw[very thick, fill=blue!5] (-0.4,1.6) rectangle (0.9,2.6);
\node at (0.25,2.1) {\large $m$};
% Yay (tavan -> kütle)
\draw[spring] (0.25,4) -- (0.25,2.6);
\node at (0.85,3.3) {$k$};
% Sönümleyici (kütle -> zemin)
\draw[thick] (0.25,1.6) -- (0.25,1.1);
\draw[thick] (-0.05,0.6) rectangle (0.55,1.1);
\draw[thick] (0.0,0.98) -- (0.5,0.98);
\draw[thick] (0.25,0.6) -- (0.25,0);
\node at (0.9,0.85) {$b$};
\end{tikzpicture}
\end{document}
```

**─── ADIM 1 — Transfer Fonksiyonunun Yazılması ───**

Sistem $m\ddot x + b\dot x + kx = y(t)$ denklemiyle modellenmiş. Sayısal değerleri koy:

$$\ddot x + 5\dot x + 6x = y(t)$$

Laplace (sıfır başlangıç): $(s^2 + 5s + 6) X(s) = Y(s)$

$$G(s) = \frac{X(s)}{Y(s)} = \frac{1}{s^2 + 5s + 6}$$

---

**─── ADIM 2 — Doğal Frekans ───**

$$\omega_n = \sqrt{\frac{k}{m}} = \sqrt{\frac{6}{1}} = \sqrt{6} \approx 2.449\ \text{rad/s}$$

---

**─── ADIM 3 — Sönüm Oranı ───**

$$\zeta = \frac{b}{2\sqrt{mk}} = \frac{5}{2\sqrt{1 \cdot 6}} = \frac{5}{2\sqrt{6}} \approx 1.021$$

$\zeta > 1$ → **Aşırı sönümlü** (sönüm kritik değerden büyük, salınım yok)

---

**─── ADIM 4 — Kutuplar ───**

Payda: $s^2 + 5s + 6 = 0$

Çarpanlara ayır: $(s + 2)(s + 3) = 0$

$$s_1 = -2,\qquad s_2 = -3$$

İkisi de **reel negatif** → sistem kararlı, aşırı sönümlü.

---

**─── ADIM 5 — Birim Basamak Yanıtı (Laplace) ───**

Giriş: birim basamak → $Y(s) = 1/s$

$$X(s) = G(s) \cdot Y(s) = \frac{1}{s^2+5s+6} \cdot \frac{1}{s} = \frac{1}{s(s+2)(s+3)}$$

Kısmi kesir (PFE):
$$\frac{1}{s(s+2)(s+3)} = \frac{A}{s} + \frac{B}{s+2} + \frac{C}{s+3}$$

Katsayıları bul:

| $s$ değeri | Denklem | Sonuç |
|------------|---------|-------|
| $s=0$ | $1 = A(0+2)(0+3) = 6A$ | $A = 1/6$ |
| $s=-2$ | $1 = B(-2)(-2+3) = -2B$ | $B = -1/2$ |
| $s=-3$ | $1 = C(-3)(-3+2) = 3C$ | $C = 1/3$ |

$$X(s) = \frac{1/6}{s} - \frac{1/2}{s+2} + \frac{1/3}{s+3}$$

---

**─── ADIM 6 — Zaman Domeni Yanıtı ───**

Ters Laplace dönüşümü: $\displaystyle \mathcal{L}^{-1}\left\{\frac{1}{s+a}\right\} = e^{-at}$

$$x(t) = \frac{1}{6} - \frac{1}{2}e^{-2t} + \frac{1}{3}e^{-3t},\qquad t \geq 0$$

**Kalıcı durum ($t\to\infty$):** $e^{-2t}, e^{-3t} \to 0$

$$x(\infty) = \frac{1}{6} = \frac{1}{k}$$

> **Anlamı:** Kütle $y=1$ m kadar sıkıştırılıp bırakıldığında, önce yukarı fırlar, sonra sönümleyici sayesinde $1/6 \approx 0.167$ m'de (yayın denge noktası) durur. Aşırı sönümlü olduğu için **salınım yapmaz**, yavaşça dengeye oturur.

---

### 📊 Hızlı Referans: Kararlılık & Sönüm Kuralları

<div style="display: flex; gap: 20px;">
<div style="flex: 1;">

| Kutupların Konumu | Kararlılık |
|---|---|
| Tümü **sol yarı düzlem** (Re $<0$) | ✅ **Kararlı** |
| Herhangi biri **sağ yarı düzlem** (Re $>0$) | ❌ **Kararsız** |
| Sanal eksende **tekrarsız** (Re $=0$) | ⚠️ Marjinal kararlı |
| Sanal eksende **tekrarlı** | ❌ Kararsız |

</div>
<div style="flex: 1;">

| Sönüm oranı $\zeta$ | Davranış |
|---|---|
| $\zeta = 0$ | Sönümsüz — sabit genlikli salınım |
| $0 < \zeta < 1$ | **Az sönümlü** — sönümlü salınım |
| $\zeta = 1$ | **Kritik sönümlü** — en hızlı denge |
| $\zeta > 1$ | **Aşırı sönümlü** — yavaş denge |
| $\zeta < 0$ | Negatif sönüm — **kararsız** |

</div>
</div>

<br>

| Kutup yapısı | $\zeta$ aralığı | Basamak yanıtı |
|---|---|---|
| İki reel negatif ($s_1,s_2<0$) | $\zeta > 1$ | Aşırı sönümlü, salınımsız |
| Reel eşit ($s_1=s_2<0$) | $\zeta = 1$ | Kritik sönümlü, salınımsız |
| Karmaşık eşlenik (Re $<0$) | $0 < \zeta < 1$ | Az sönümlü, salınımlı |
| Sanal eksen ($\pm j\omega$) | $\zeta = 0$ | Sönümsüz, sabit salınım |
| Reel pozitif veya sağ düzlem | $\zeta < 0$ veya Re $>0$ | Patlayan / kararsız |

---

## Mekanik Örnek 4 — İki Kütle, Üç Yay, Newton + Cramer

> [!example] Problem
> **Sistem:** Sol duvar → $k_1$ → $m_1$ → ($k_2$ yay ∥ $b$ sönümleyici) → $m_2$ → $k_3$ → sağ duvar. $F$ kuvveti $m_1$'e uygulanıyor; konumlar $x_1,x_2$.
>
> **İstenen:** Newton + Cramer ile $\dfrac{X_2(s)}{F(s)}$ transfer fonksiyonu.

> [!note]- Semboller
> - $F$: dış kuvvet — giriş, $m_1$'e uygulanır (N)
> - $m_1,m_2$: kütleler (kg)
> - $k_1,k_2,k_3$: yay sabitleri (N/m)
> - $b$: viskoz sönüm katsayısı (N·s/m)
> - $x_1,x_2$: kütle konumları (m); $X_1(s),X_2(s),F(s)$: Laplace dönüşümleri
> - $\Delta_1,\Delta_2$: her kütlenin köşegen empedans polinomu ($m_is^2+bs+\dots$)
> - $Z=bs+k_2$: bağlaşım (coupling) terimi — iki kütleyi bağlayan $k_2/b$ elemanı
> - $s$: Laplace değişkeni (1/s)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2mm}}]
% Sol duvar
\draw[very thick] (0,-0.9) -- (0,0.9);
\foreach \y in {-0.7,-0.3,...,0.9}{ \draw (0,\y) -- (-0.28,\y-0.22); }
% Sağ duvar
\draw[very thick] (8,-0.9) -- (8,0.9);
\foreach \y in {-0.7,-0.3,...,0.9}{ \draw (8,\y) -- (8.28,\y-0.22); }
% k1: sol duvar -> m1
\draw[spring] (0,0.3) -- (2,0.3); \node at (1,0.85){$k_1$};
% F -> m1
\draw[->, red!70!black, very thick] (0.2,-0.0) -- (1.9,-0.0); \node[red!70!black] at (1,-0.4){$F$};
% m1
\draw[very thick, fill=blue!5] (2,-0.75) rectangle (3.1,0.75); \node at (2.55,0){$m_1$};
% k2 (üst) + b (alt): m1 -> m2
\draw[spring] (3.1,0.3) -- (5,0.3); \node at (4.05,0.85){$k_2$};
\draw[thick] (3.1,-0.45) -- (3.8,-0.45);
\draw[thick] (3.8,-0.72) rectangle (4.35,-0.18);
\draw[thick] (4.22,-0.65) -- (4.22,-0.25);
\draw[thick] (4.1,-0.45) -- (5,-0.45);
\node at (4.05,-1.0){$b$};
% m2
\draw[very thick, fill=blue!5] (5,-0.75) rectangle (6.1,0.75); \node at (5.55,0){$m_2$};
% k3: m2 -> sağ duvar
\draw[spring] (6.1,0.3) -- (8,0.3); \node at (7.05,0.85){$k_3$};
% x1, x2
\draw[->, thick] (2.2,1.15) -- (3.0,1.15) node[right]{$x_1$};
\draw[->, thick] (5.2,1.15) -- (6.0,1.15) node[right]{$x_2$};
\end{tikzpicture}
\end{document}
```

**Adım 1 — Her kütle için Newton (FBD), Laplace'ta.** $m_1$'e: $k_1$ (duvar) + $k_2,b$ ($m_2$'ye) + $F$; $m_2$'ye: $k_3$ (duvar) + $k_2,b$ ($m_1$'e). Konum değişkenlerinin katsayılarını grupla:

$$\Delta_1 = m_1s^2+bs+(k_1+k_2), \quad \Delta_2 = m_2s^2+bs+(k_2+k_3), \quad Z = bs+k_2$$

burada $\Delta_1$ = $m_1$'in kendi terimleri toplamı, $Z$ = iki kütleyi bağlayan ortak ($k_2,b$) terim. Matris formu:

$$\begin{bmatrix}\Delta_1 & -Z \\ -Z & \Delta_2\end{bmatrix}\begin{bmatrix}X_1 \\ X_2\end{bmatrix} = \begin{bmatrix}F \\ 0\end{bmatrix}$$

**Adım 2 — Cramer kuralı.** $X_2$ için, katsayı matrisinin 2. sütununu sağ taraf $\begin{bmatrix}F\\0\end{bmatrix}$ ile değiştir:

$$X_2(s) = \frac{\begin{vmatrix}\Delta_1 & F \\ -Z & 0\end{vmatrix}}{\begin{vmatrix}\Delta_1 & -Z \\ -Z & \Delta_2\end{vmatrix}} = \frac{\Delta_1\cdot 0-F\cdot(-Z)}{\Delta_1\Delta_2-Z^2} = \frac{Z\,F}{\Delta_1\Delta_2-Z^2}$$

**Adım 3 — Pay ve paydayı aç.** Pay: $Z=bs+k_2$. Payda $\Delta_1\Delta_2-Z^2$:

$$\Delta_1\Delta_2=\big(m_1s^2+bs+k_1+k_2\big)\big(m_2s^2+bs+k_2+k_3\big),\qquad Z^2=(bs+k_2)^2=b^2s^2+2bk_2s+k_2^2$$

Çarpımı açıp $Z^2$'yi çıkarınca ($b^2s^2$ ve $k_2^2$ terimleri sadeleşir):

$$\boxed{\frac{X_2(s)}{F(s)} = \frac{bs+k_2}{m_1m_2s^4+(m_1+m_2)bs^3+[m_1(k_2+k_3)+m_2(k_1+k_2)]s^2+b(k_1+k_3)s+(k_1k_2+k_1k_3+k_2k_3)}}$$

*4. dereceden sistem; $(bs+k_2)$ payı → enerji $m_1$'den $m_2$'ye yalnızca ortak $k_2$ yayı ve $b$ sönümleyicisi üzerinden aktarılır.*

---

## Mekanik Örnek 5 — Birim Dönüşümü ($m=2000$ kg, $k=16{,}5$ N/mm)

> [!example] Problem
> **Veri (araç süspansiyonu):** $m=2000$ kg, $k=16{,}5$ N/mm, $b=5000$ N·s/m. Kütle–yay–sönümleyici sistemi $f(t)$ kuvvetiyle sürülüyor.
>
> **İstenen:** (a) doğal frekans $\omega_n$, (b) sönüm oranı $\zeta$, (c) sistem tipi, (d) DC kazancı $K$. **Dikkat:** $k$ farklı birimde verilmiş, önce SI'ya çevir.

> [!note]- Semboller
> - $m,k,b$: kütle (kg), yay sabiti (N/m), sönüm (N·s/m)
> - $f(t)$: dış kuvvet — giriş (N); $F(s)$: Laplace dönüşümü
> - $x,\dot x,\ddot x$: konum, hız, ivme (m, m/s, m/s²); $X(s)$: Laplace dönüşümü
> - $G(s)=X(s)/F(s)$: transfer fonksiyonu
> - $\omega_n=\sqrt{k/m}$: doğal frekans (rad/s)
> - $\zeta=\dfrac{b}{2\sqrt{mk}}$: sönüm oranı (birimsiz)
> - $K=1/k$: DC (kalıcı durum) kazancı (m/N)
> - $j=\sqrt{-1}$: sanal birim; $s$: Laplace değişkeni (1/s)

**Adım 0 — Birim dönüşümü (SI).** $1$ mm $=10^{-3}$ m olduğundan N/mm → N/m için $\times 1000$:

$$k = 16{,}5 \;\frac{\text{N}}{\text{mm}} = 16{,}5\times1000 = 16500 \;\frac{\text{N}}{\text{m}}, \quad b = 5000 \;\frac{\text{N·s}}{\text{m}}, \quad m = 2000 \;\text{kg}$$

**Hareket denklemi:** $2000\ddot{x}+5000\dot{x}+16500x = f(t)$. Tümünü $m=2000$'e böl (standart $s^2+2\zeta\omega_n s+\omega_n^2$ formu için):

$$G(s) = \frac{X(s)}{F(s)} = \frac{1/2000}{s^2+2{,}5s+8{,}25} \qquad\left(\tfrac{5000}{2000}=2{,}5,\;\tfrac{16500}{2000}=8{,}25\right)$$

**a) Doğal frekans:**

$$\omega_n = \sqrt{\frac{k}{m}} = \sqrt{\frac{16500}{2000}} = \sqrt{8{,}25} \approx 2{,}872 \;\text{rad/s}$$

**b) Sönüm oranı:**

$$\zeta = \frac{b}{2\sqrt{mk}} = \frac{5000}{2\sqrt{2000\times16500}} \approx 0{,}435 \quad (<1 \to \textbf{az sönümlü})$$

**c) Sistem tipi:** Az sönümlü → basamak girişine **salınımlı** yanıt, aşım var

**d) Sistem kazancı:**

$$\zeta = \frac{2{,}5}{2\omega_n} \implies 2\zeta\omega_n = 2{,}5 \checkmark, \quad \boxed{K = \frac{1}{k} = \frac{1}{16500} \approx 6{,}06\times10^{-5} \;\text{m/N}}$$

Kutuplar (paydanın kökleri $s=\frac{-2{,}5\pm\sqrt{2{,}5^2-4\cdot8{,}25}}{2}=\frac{-2{,}5\pm\sqrt{-26{,}75}}{2}$): $s_{1,2} = -1{,}25 \pm j\,2{,}587$ — karmaşık eşlenik, Re $<0$ → kararlı + salınımlı.

---

## Mekanik Örnek 6 — İki Dönel Kütle (Türetilmiş)

> [!example] Problem
> **Sistem:** Sol duvar → $b_1$ sönümleyici → $J_1$ → $k$ burulma yayı → $J_2$ → $b_2$ sönümleyici → sağ duvar. Giriş torku $T$ → $J_1$'e; çıkış açısı $\theta_2$.
>
> **İstenen:** $\dfrac{\Theta_2(s)}{T(s)}$ transfer fonksiyonu (Cramer ile).

> [!note]- Semboller
> - $J_1,J_2$: atalet momentleri — dönel kütleler (kg·m²)
> - $b_1$: sol duvar sönümü, $b_2$: sağ duvar sönümü (Nm·s/rad)
> - $k$: burulma (torsiyon) yayı sabiti (Nm/rad)
> - $T$: giriş torku (Nm); $T(s)$: Laplace dönüşümü
> - $\theta_1,\theta_2$: açısal konumlar (rad); $\dot\theta,\ddot\theta$: açısal hız/ivme
> - $\Theta_1(s),\Theta_2(s)$: Laplace dönüşümleri
> - $s$: Laplace değişkeni (1/s)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2.2mm}}]
% Sol duvar
\draw[very thick] (-0.3,-1) -- (-0.3,1);
\foreach \y in {-0.8,-0.4,...,1.0}{ \draw (-0.3,\y) -- (-0.6,\y-0.2); }
% Sağ duvar
\draw[very thick] (8.3,-1) -- (8.3,1);
\foreach \y in {-0.8,-0.4,...,1.0}{ \draw (8.3,\y) -- (8.6,\y-0.2); }
% b1: sol duvar -> J1
\draw[thick] (-0.3,0) -- (0.4,0);
\draw[thick] (0.4,-0.28) rectangle (0.95,0.28);
\draw[thick] (0.82,-0.2) -- (0.82,0.2);
\draw[thick] (0.7,0) -- (1.6,0);
\node at (0.65,-0.55){$b_1$};
% J1
\draw[very thick, fill=blue!5] (1.6,-0.7) rectangle (2.8,0.7); \node at (2.2,0){$J_1$};
% k (burulma yayı)
\draw[spring] (2.8,0) -- (4.6,0); \node at (3.7,0.5){$k$};
% J2
\draw[very thick, fill=blue!5] (4.6,-0.7) rectangle (5.8,0.7); \node at (5.2,0){$J_2$};
% b2: J2 -> sağ duvar
\draw[thick] (5.8,0) -- (6.7,0);
\draw[thick] (6.7,-0.28) rectangle (7.25,0.28);
\draw[thick] (7.12,-0.2) -- (7.12,0.2);
\draw[thick] (7.0,0) -- (8.3,0);
\node at (6.9,-0.55){$b_2$};
% T, theta1, theta2
\draw[->, red!70!black, thick] (1.75,1.25) arc (160:20:0.45); \node[red!70!black] at (2.2,1.65){$T$};
\draw[->, blue!60!black, thick] (4.75,1.1) arc (160:20:0.45); \node[blue!60!black] at (5.6,1.5){$\theta_2$};
\node[blue!60!black] at (2.95,1.15){$\theta_1$};
\end{tikzpicture}
\end{document}
```

**Hareket denklemleri (tork toplamı):**

$J_1$ için: $T - b_1\dot{\theta}_1 - k(\theta_1-\theta_2) = J_1\ddot{\theta}_1$

$J_2$ için: $k(\theta_1-\theta_2) - b_2\dot{\theta}_2 = J_2\ddot{\theta}_2$

**Laplace'ta:**

$(J_1s^2+b_1s+k)\Theta_1 - k\Theta_2 = T(s)$

$-k\Theta_1 + (J_2s^2+b_2s+k)\Theta_2 = 0$

**Cramer kuralı.** İkinci denklemden $\Theta_1$'i çek ($-k\Theta_1+(J_2s^2+b_2s+k)\Theta_2=0$):

$$\Theta_1 = \frac{(J_2s^2+b_2s+k)}{k}\,\Theta_2$$

Birinci denkleme yerine koy:

$$(J_1s^2+b_1s+k)\cdot\frac{(J_2s^2+b_2s+k)}{k}\Theta_2 - k\Theta_2 = T(s)$$

$\Theta_2$ parantezine al ve $k$ ile çarp:

$$\Theta_2\left[\frac{(J_1s^2+b_1s+k)(J_2s^2+b_2s+k)-k^2}{k}\right]=T(s)$$

$$\boxed{\frac{\Theta_2(s)}{T(s)} = \frac{k}{(J_1s^2+b_1s+k)(J_2s^2+b_2s+k) - k^2}}$$

> Paydadaki $-k^2$, iki diski bağlayan yayın bağlaşımından gelir; payda iki diskin tek başına dinamiğinin çarpımından bu bağlaşımın çıkarılmasıdır.

---

## Mekanik Örnek 7 — Sarkaç Sistemi ($m=2$ kg, $g=9{,}81$ m/s²)

> [!example] Problem
> **Sistem:** Tavana asılı basit sarkaç — kol uzunluğu $l$, ucunda kütle $m$. Bob'a yatay $F$ kuvveti uygulanıyor; düşeyden sapma açısı $\theta$.
>
> **İstenen:** Küçük açı yaklaşımıyla hareket denklemini **üç yöntemle** (Newton, enerji, Lagrange) çıkar ve $\dfrac{\Theta(s)}{F(s)}$ ile $\omega_n$'i bul.

> [!note]- Semboller
> - $m$: bob kütlesi (kg)
> - $g$: yerçekimi ivmesi (m/s²)
> - $l$: sarkaç kolu uzunluğu (m)
> - $F$: yatay dış kuvvet — giriş (N)
> - $\theta,\dot\theta,\ddot\theta$: açısal konum, hız, ivme (rad, rad/s, rad/s²)
> - Küçük açı: $\sin\theta\approx\theta$, $\cos\theta\approx1$ ($\theta$ küçükken geçerli)
> - $\Theta(s),F(s)$: Laplace dönüşümleri
> - $\omega_n=\sqrt{g/l}$: doğal frekans (rad/s)
> - $T,V,L$: kinetik, potansiyel enerji, Lagrangian (J)

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta, calc}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small]
% Tavan
\draw[very thick] (-1.5,0) -- (1.5,0);
\foreach \x in {-1.3,-0.9,...,1.3}{ \draw (\x,0) -- (\x-0.25,0.25); }
% Pivot
\fill (0,0) circle (1.6pt);
% Dikey referans
\draw[dashed] (0,0) -- (0,-3);
% Çubuk + bob
\coordinate (bob) at (1.5,-2.6);
\draw[very thick] (0,0) -- (bob);
\node at (0.6,-1.45) {$l$};
\draw[very thick, fill=blue!5] (bob) circle (0.3);
\node at (bob) {$m$};
% Açı
\draw[->, blue!60!black, thick] (0,-1.1) arc (-90:-60:1.1); \node[blue!60!black] at (0.5,-1.0){$\theta$};
% Kuvvet
\draw[->, red!70!black, very thick] ($(bob)+(-0.65,0)$) -- ($(bob)+(0.75,0)$);
\node[red!70!black] at ($(bob)+(-1.0,0)$){$F$};
\end{tikzpicture}
\end{document}
```

**Küçük açı yaklaşımı** ($\sin\theta\approx\theta$, $\cos\theta\approx1$):

**a) Newton (tork dengesi, pivot etrafında):** Pivota göre tork = atalet × açısal ivme, $I\ddot\theta=\sum\tau$ ile $I=ml^2$ (nokta kütle). Yerçekimi geri çağırıcı tork $-mgl\sin\theta$, kuvvet torku $+Fl\cos\theta$:

$$ml^2\ddot\theta = -mgl\sin\theta + Fl\cos\theta$$

Küçük açı ($\sin\theta\approx\theta$, $\cos\theta\approx1$) ile doğrusallaştır:

$$ml^2\ddot{\theta} + mgl\theta = Fl \implies \boxed{\frac{\Theta(s)}{F(s)} = \frac{l}{ml^2s^2+mgl} = \frac{1}{mls^2+mg}}$$

**Serbest titreşim ($F=0$):**

$$\ddot{\theta} + \frac{g}{l}\theta = 0 \implies \boxed{\omega_n = \sqrt{\frac{g}{l}} = \sqrt{\frac{9{,}81}{l}} \;\text{rad/s}}$$

**b) Enerji metodu:** $T=\frac{1}{2}ml^2\dot{\theta}^2$, $V\approx\frac{1}{2}mgl\theta^2$

$$\frac{d}{dt}(T+V)=0 \implies ml^2\ddot{\theta}+mgl\theta=0 \implies \omega_n=\sqrt{g/l} \checkmark$$

**c) Lagrange:** $L=\frac{1}{2}ml^2\dot{\theta}^2-mgl(1-\cos\theta)$

$$\frac{d}{dt}(ml^2\dot{\theta})-(-mgl\sin\theta)=0 \implies ml^2\ddot{\theta}+mgl\theta=0 \checkmark$$

*$m=2$ kg, $l=1$ m için: $\omega_n=\sqrt{9{,}81/1}\approx3{,}13$ rad/s. Not: $\omega_n$ kütleden bağımsız, yalnızca $g$ ve $l$'ye bağlı.*

---

## Mekanik Örnek 8 — Dişli Sistemi TF ($\Theta_1/T_1$, türetilmiş)

> [!example] Problem
> **Sistem:** Motor mili küçük dişli $N_1$'i döndürür ($T_1$, $\theta_1$). Bu, büyük dişli $N_2$'ye kavrar ($T_2$, $\theta_2$); yük tarafında $J_1$ ataleti, $k$ yayı ve $b$ sönümleyicisi duvara bağlı.
>
> **İstenen:** Motor tarafına göre $\dfrac{\Theta_1(s)}{T_1(s)}$ transfer fonksiyonu (yük dişli oranıyla motora yansıtılarak).

> [!note]- Semboller
> - $N_1,N_2$: küçük/büyük dişli diş sayıları (birimsiz)
> - $T_1,T_2$: motor ve yük tarafı torkları (Nm)
> - $\theta_1,\theta_2$: açısal konumlar (rad); $\dot\theta,\ddot\theta$: hız/ivme
> - $J_1$: yük ataleti (kg·m²)
> - $b$: viskoz sönüm (Nm·s/rad); $k$: yay sabiti (Nm/rad)
> - Dişli ilişkisi: $\theta_2=\dfrac{N_1}{N_2}\theta_1$ (büyük dişli yavaş döner), $T_2=\dfrac{N_2}{N_1}T_1$ (tork artar)
> - $\Theta_1(s),T_1(s)$: Laplace dönüşümleri; $s$: Laplace değişkeni (1/s)
> - $J_{ref},b_{ref},k_{ref}$: motora yansıtılmış değerler ($\times(N_1/N_2)^2$)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2mm}}]
% Motor
\draw[very thick, fill=gray!15] (-0.6,-0.5) rectangle (0.4,0.5);
\node at (-0.1,0){\footnotesize motor};
% Küçük dişli N1
\draw[very thick, fill=blue!8] (1.1,0) circle (0.5);
\node at (1.1,0){\scriptsize $N_1$};
\draw[->, blue!60!black] (1.1,0.7) arc (90:25:0.7); \node[blue!60!black] at (2.0,0.65){$\theta_1$};
% Büyük dişli N2
\draw[very thick, fill=blue!8] (1.1,1.45) circle (0.9);
\node at (1.1,1.45){\scriptsize $N_2$};
\draw[->, green!50!black] (1.1,2.55) arc (90:30:1.1); \node[green!50!black] at (2.4,2.5){$\theta_2$};
% Motor mili
\draw[thick] (0.4,0) -- (0.6,0);
% Yük şaftı: büyük dişli -> J1
\draw[thick] (2.0,1.45) -- (3,1.45);
% J1
\draw[very thick, fill=blue!5, rounded corners=10pt] (3,0.85) rectangle (4.4,2.05); \node at (3.7,1.45){$J_1$};
% Sağ duvar
\draw[very thick] (6.6,0.4) -- (6.6,2.5);
\foreach \y in {0.6,1.0,...,2.4}{ \draw (6.6,\y) -- (6.9,\y-0.2); }
% b (üst)
\draw[thick] (4.4,1.85) -- (4.95,1.85);
\draw[thick] (4.95,1.6) rectangle (5.5,2.1);
\draw[thick] (5.37,1.68) -- (5.37,2.02);
\draw[thick] (5.25,1.85) -- (6.6,1.85);
\node at (5.15,2.35){$b$};
% k (alt)
\draw[spring] (4.4,1.05) -- (6.6,1.05); \node at (5.5,0.65){$k$};
\end{tikzpicture}
\end{document}
```

**Dişli ilişkileri:**

$$\theta_2 = \frac{N_1}{N_2}\theta_1, \qquad T_2 = \frac{N_2}{N_1}T_1$$

**Adım 1 — Yük şaftı ($J_2$ tarafı) hareket denklemi.** Büyük dişliye etkiyen torklar: kaynak $T_2$, sönüm $-b\dot\theta_2$, yay $-k\theta_2$:

$$T_2 - b\dot{\theta}_2 - k\theta_2 = J_1\ddot{\theta}_2 \;\xrightarrow{\text{Laplace}}\; T_2 = (J_1s^2+bs+k)\Theta_2$$

**Adım 2 — Dişli ilişkilerini koy.** $T_2=\dfrac{N_2}{N_1}T_1$ ve $\Theta_2=\dfrac{N_1}{N_2}\Theta_1$ yerine:

$$\frac{N_2}{N_1}T_1 = \left(J_1s^2+bs+k\right)\cdot\frac{N_1}{N_2}\Theta_1$$

**Adım 3 — $\Theta_1/T_1$'i çek.** $T_1$'i yalnız bırak ($N_2/N_1$ karşıya $N_1/N_2$ olarak geçer, ikisi çarpılır):

$$\boxed{\frac{\Theta_1(s)}{T_1(s)} = \frac{(N_2/N_1)^2}{J_1s^2+bs+k}}$$

> **Yorum — empedans yansıtma:** Sonucu pay-payda $(N_1/N_2)^2$ ile bölersek payda $J_1(N_1/N_2)^2 s^2+b(N_1/N_2)^2 s+k(N_1/N_2)^2$ olur. Yani yük elemanları motora $\;J_{ref}=J_1(N_1/N_2)^2,\; b_{ref}=b(N_1/N_2)^2,\; k_{ref}=k(N_1/N_2)^2\;$ olarak yansır — **dişli oranının karesiyle**.
