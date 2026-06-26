---
tags: [mst, mekanik, newton, lagrange, transfer-fonksiyonu, dc-motor, disli, konu-anlatımı]
---

# 01 — Mekanik Sistemler

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/01 Mekanik Sistemler Örnekleri|01 Mekanik Sistemler Örnekleri]]

> Newton 2. Yasası ile mekanik sistemlerin Laplace domeninde modellenmesi; DC motor ve dişli sistemleri.

---

## Temel Mekanik Elemanlar

| Eleman | Simge | Kuvvet-Hareket İlişkisi | Laplace Empedansı |
|--------|-------|------------------------|--------------------|
| Kütle $m$ | $M$ | $F = m\ddot{x}$ | $ms^2$ |
| Yay $k$ | $\wedge\wedge\wedge$ | $F = kx$ | $k$ |
| Sönümleyici $b$ | $\dashv\vdash$ | $F = b\dot{x}$ | $bs$ |

---

## Newton 2. Yasası Yöntemi

**Adım 1:** Her kütle için Serbest Cisim Diyagramı (FBD) çiz
**Adım 2:** Her kuvveti topla → $\sum F = m\ddot{x}$
**Adım 3:** Laplace dönüşümü al → transfer fonksiyonu

---

## Tek Kütleli Sistem (Yay-Kütle-Sönümleyici)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=3mm, post length=3mm, segment length=3mm, amplitude=2.4mm}}]
% Duvar (taralı)
\draw[very thick] (0,-1.5) -- (0,1.5);
\foreach \y in {-1.3,-0.9,...,1.3}{ \draw (0,\y) -- (-0.28,\y+0.22); }
% Yay (üst)
\draw[spring] (0,0.7) -- (3,0.7);
\node at (1.5,1.2) {$k$};
% Sönümleyici (alt): silindir + piston
\draw[thick] (0,-0.7) -- (1.2,-0.7);
\draw[thick] (1.2,-1.05) rectangle (1.85,-0.35);
\draw[thick] (1.55,-1.0) -- (1.55,-0.4);
\draw[thick] (1.55,-0.7) -- (3,-0.7);
\node at (0.95,-0.2) {$b$};
% Kütle
\draw[very thick, fill=blue!5] (3,-1.05) rectangle (4.5,1.05);
\node at (3.75,0) {\large $m$};
% Kuvvet
\draw[->, red!70!black, very thick] (4.5,0) -- (5.8,0) node[right]{$f(t)$};
% Yer değiştirme
\draw[->, green!50!black, thick] (3.5,1.4) -- (4.6,1.4) node[right]{$x(t)$};
\end{tikzpicture}
\end{document}
```

**Hareket denklemi:**

$$m\ddot{x}(t) + b\dot{x}(t) + kx(t) = f(t)$$

**Laplace'ta (sıfır başlangıç koşulları):**

$$\boxed{G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}}$$

> [!tanim] İkinci Dereceden Standart Form
> - **Doğal Frekans**: $\omega_n = \sqrt{\frac{k}{m}}$
> - **Sönüm Oranı**: $\zeta = \frac{b}{2\sqrt{mk}}$

---

## İki Kütleli Sistem

**$m_1$ için FBD:**
$$m_1\ddot{x}_1 + b_1\dot{x}_1 + k_1 x_1 + k_2(x_1-x_2) + b_2(\dot{x}_1-\dot{x}_2) = f(t)$$

**$m_2$ için FBD:**
$$m_2\ddot{x}_2 + k_2(x_2-x_1) + b_2(\dot{x}_2-\dot{x}_1) = 0$$

**Laplace domeninde** ($x(0)=0$, $\dot{x}(0)=0$):

$$Y_1(s)\bigl(m_1s^2 + b_1s + k_1 + b_2s + k_2\bigr) - Y_2(s)(k_2+b_2s) = F(s)$$
$$-Y_1(s)(k_2+b_2s) + Y_2(s)\bigl(m_2s^2 + b_2s + k_2\bigr) = 0$$

Transfer fonksiyonu $\dfrac{Y_2(s)}{F(s)}$, matris yöntemiyle:

$$Y_1(s)\bigl(m_1s^2+b_1s+k_1+k_2+b_2s\bigr) - X_1(s)(k_2+b_2s) = F(s)$$

$$Y_2(s)(m_2s^2+b_2s+k_2) = Y_1(s)(k_2+b_2s)$$

$$\frac{Y_1(s)}{F(s)} = \frac{m_2s^2 + b_2s + k_2}{\Delta(s)}, \qquad \frac{Y_2(s)}{F(s)} = \frac{k_2+b_2s}{\Delta(s)}$$

---

## Lagrange Yöntemi

<span style="color:rgb(255, 255, 0)">Daha karmaşık sistemlerde Newton yerine kullanılır.</span>

$$\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{q}_i}\right) - \frac{\partial \mathcal{L}}{\partial q_i} + \frac{\partial D}{\partial \dot{q}_i} = Q_i$$

Burada $\mathcal{L} = T - V$ (Lagrangian):

| Eleman | Kinetik $T$ | Potansiyel $V$ | Sönümleme $D$ |
|--------|------------|----------------|---------------|
| Kütle $m$ | $\frac{1}{2}m\dot{x}^2$ | — | — |
| Yay $k$ | — | $\frac{1}{2}kx^2$ | — |
| Sönümleyici $b$ | — | — | $\frac{1}{2}b\dot{x}^2$ |
| Dönel $J$ | $\frac{1}{2}J\dot{\theta}^2$ | — | — |

---

## Dönel Mekanik Sistemler

| Öteleme | Dönel Karşılık |
|---------|----------------|
| Kütle $m$ | Atalet momenti $J$ |
| Sönümleyici $b$ | Dönel sönüm $B$ |
| Yay $k$ | Dönel yay $K$ |
| Kuvvet $F$ | Tork $T$ |

$$J\ddot{\theta} + B\dot{\theta} + K\theta = T(t) \quad\longrightarrow\quad G(s) = \frac{\Theta(s)}{T(s)} = \frac{1}{Js^2+Bs+K}$$

---

## DC Motor Modeli (Armatür Kontrolü)

```tikz
\usepackage{circuitikz}
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{circuitikz}[american, >={Stealth[length=2mm]}]
\draw (0,0) to[V=$V_a$, invert] (0,3);
\draw (0,3) to[R=$R_a$, i>^=$i_a$] (2.5,3) to[L=$L_a$] (5,3) -- (6,3);
\draw (6,3) to[european voltage source, l_=$e_b$] (6,0);
\draw (0,0) -- (6,0);
% Mil
\draw[dashed, very thick] (6,1.5) -- (7.4,1.5);
% Rotor (mekanik)
\node[draw, very thick, circle, minimum size=14mm, fill=blue!5] (m) at (8.1,1.5) {$J_m,B_m$};
\draw[->, thick, red!70!black] (8.7,2.35) arc (55:-35:1.0);
\node[red!70!black] at (9.9,1.5) {$\Theta_m$};
\end{circuitikz}
\end{document}
```

**Üç temel denklem:**

**1) KVL (Armatür Devresi):**
$$V_a(s) = (R_a + L_a s)\,I_a(s) + K_b s\,\Theta_m(s)$$

**2) Tork:** $T_m(s) = K_t\,I_a(s)$

**3) Mekanik:** $T_m(s) = s(J_m s + B_m)\,\Theta_m(s)$

**Transfer Fonksiyonu ($L_a \approx 0$ yaklaşımı):**

$$\boxed{\frac{\Theta_m(s)}{V_a(s)} = \frac{K_t/R_a J_m}{s\!\left(s + \dfrac{R_a B_m + K_b K_t}{R_a J_m}\right)}}$$

---

## Dişli (Gear) Sistemi

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[font=\small]
% Küçük dişli
\draw[thick, fill=blue!5] (0,0) circle (1);
\node at (0,0.22) {$N_1, r_1$};
\node at (0,-0.28) {$T_1,\theta_1$};
% Büyük dişli
\draw[thick, fill=blue!5] (2.6,0) circle (1.6);
\node at (2.6,0.28) {$N_2, r_2$};
\node at (2.6,-0.32) {$T_2,\theta_2$};
% Temas noktası (dış temas: merkezler arası = r1+r2)
\fill[red] (1.0,0) circle (1.6pt);
\node[gray, font=\footnotesize] at (1.3,-2.3) {$N_2 > N_1 \;\Rightarrow\;$ Yavaş, yüksek tork};
\end{tikzpicture}
\end{document}
```

**Dişli oranı formülleri:**

$$\frac{T_1}{T_2} = \frac{r_1}{r_2} = \frac{N_1}{N_2}, \qquad \frac{\theta_2}{\theta_1} = \frac{N_1}{N_2}$$

> [!info] Dişli Formülü Terimleri
> - **T**: Tork (moment)
> - **r**: Dişli yarıçapı
> - **N**: Diş sayısı
> - **θ**: Dönme açısı

**Yük yansıtma (motor miline):**

$$J_t = J_a + J_L\!\left(\frac{N_1}{N_2}\right)^{\!2}, \qquad D_t = D_a + D_L\!\left(\frac{N_1}{N_2}\right)^{\!2}$$

> [!info] Yük Yansıtma Terimleri
> - **J_t**: Toplam eylemsizlik (motor + yük)
> - **J_a**: Motor eylemsizliği
> - **J_L**: Yük eylemsizliği
> - **D_t**: Toplam sönüm
> - **D_a**: Motor sönümü
> - **D_L**: Yük sönümü

---

## Mekanik ↔ Elektrik Analogisi

| Mekanik | Elektrik (hız-voltaj) |
|---------|----------------------|
| Kuvvet $F$ | Voltaj $v$ |
| Hız $\dot{x}$ | Akım $i$ |
| Kütle $m$ | İndüktör $L$ |
| Sönümleyici $b$ | Direnç $R$ |
| Yay $k$ | $1/C$ |

> [!sinav] Sınav İpuçları
> - FBD çiz → her kuvveti tek tek yaz → Newton 2. Yasası
> - Laplace'ta $\ddot{x} \to s^2 X(s)$, $\dot{x} \to sX(s)$ (sıfır başlangıç şartıyla)
> - İki kütle → iki denklem → matris veya yerine koyma ile çöz
> - DC motorda $L_a \approx 0$ sıkça kullanılır → sistem 2. dereceden 1. dereceye iner
> - Dişli: $J$ ve $D$ değerleri $(N_1/N_2)^2$ ile motor miline yansıtılır
