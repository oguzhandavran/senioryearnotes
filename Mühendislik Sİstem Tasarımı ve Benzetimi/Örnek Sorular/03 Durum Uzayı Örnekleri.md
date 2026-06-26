---
tags: [mst, durum-uzayı, state-space, matris, özdeğer, kontrol, örnek-sorular]
---

# 03 — Durum Uzayı Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/03 Durum Uzayı|03 Durum Uzayı]]

---

## Çözümlü Örnek 1: Mekanik Sistem (Ders Notları)

> [!example] Problem
> **Sistem:** $m\ddot{x} + b\dot{x} + kx = f(t)$ kütle–yay–sönümleyici, $m=1$, $b=3$, $k=2$. Giriş $f$, çıkış konum $x$.
>
> **İstenen:** Durum uzayı ($A,B,C,D$) modelini yaz ve transfer fonksiyonuyla doğrula.

> [!note]- Semboller
> - $x_1=x$: konum durumu (m); $x_2=\dot x$: hız durumu (m/s)
> - $\dot x=Ax+Bf$: durum denklemi; $y=Cx$: çıkış denklemi
> - $A$: sistem (durum) matrisi; $B$: giriş matrisi; $C$: çıkış matrisi; $D$: ileri besleme (burada 0)
> - $G(s)=C(sI-A)^{-1}B$: durum uzayından elde edilen transfer fonksiyonu
> - $I$: birim matris; $s$: Laplace değişkeni (1/s)

**Adım 1 — Durum değişkenleri seç:** $x_1 = x$ (konum), $x_2 = \dot{x}$ (hız).

**Adım 2 — Türevlerini yaz.** $\dot x_1=x_2$ tanımdan; $\dot x_2=\ddot x$ için hareket denklemini $\ddot x$ için çöz ($\ddot x=(f-b\dot x-kx)/m$, $m=1$):

$$\dot{x}_1 = x_2, \qquad \dot{x}_2 = \ddot{x} = -kx_1 - bx_2 + f = -2x_1 - 3x_2 + f$$

**Adım 3 — Matris formu:**

$$\dot{x} = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} x + \begin{bmatrix} 0 \\ 1 \end{bmatrix} f, \qquad y = \begin{bmatrix} 1 & 0 \end{bmatrix} x$$

**Adım 4 — Doğrulama.** $sI-A=\begin{bmatrix}s&-1\\2&s+3\end{bmatrix}$, $\det=s^2+3s+2$; $C(sI-A)^{-1}B$ payı 1:

$$G(s) = C(sI-A)^{-1}B = \frac{1}{s^2+3s+2} \quad \checkmark$$

---

## Çözümlü Örnek 2: RLC Devre (Ders Notları)

> [!example] Problem
> **Devre:** Seri RLC, $L = 1$ H, $R = 3$ Ω, $C = 0.5$ F; çıkış kondansatör gerilimi $v_C$.
>
> **İstenen:** Yük ve akımı durum değişkeni alarak $A,B,C$ matrislerini bul.

> [!note]- Semboller
> - $x_1=q$: kondansatör yükü durumu (C); $x_2=i$: bobin akımı durumu (A)
> - $v_{in}$: kaynak gerilimi — giriş (V); $v_C=q/C$: çıkış (V)
> - $L,R,C$: indüktans (H), direnç (Ω), kapasitans (F)
> - KVL: $L\,di/dt=-Ri-q/C+v_{in}$ (ilmek gerilim dengesi)
> - $A,B,C_{mat}$: durum, giriş, çıkış matrisleri

KVL ile (Laplace yerine doğrudan türev): bobin gerilimi = kaynak − direnç − kondansatör gerilimleri:
$$L\frac{di}{dt} = -Ri - \frac{q}{C} + v_{in}, \qquad \frac{dq}{dt} = i$$

**Durum değişkenleri:** $x_1 = q$ (yük), $x_2 = i$ (akım)

$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -1/(LC) & -R/L \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 1/L \end{bmatrix} v_{in}$$

Değerleri yerleştir:
$$A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

Çıkış $v_C = q/C = x_1/0.5$: $C_{mat} = \begin{bmatrix} 2 & 0 \end{bmatrix}$

---

## Çözümlü Örnek 3: İki Kütleli Sistem (Ders Notları)

> [!example] Problem
> **Sistem:** Duvar → $k_1$ → $m_1$ (zemine $b_1$ sönümleyici) → $k_2$ → $m_2$. Kuvvet $f(t)$ → $m_2$'ye. Konumlar $x_1,x_2$.
>
> **İstenen:** 4. dereceden durum uzayı $A,B$ matrisleri ($[x_1,\dot x_1,x_2,\dot x_2]^T$ durumlarıyla).

> [!note]- Semboller
> - $m_1,m_2$: kütleler (kg); $k_1,k_2$: yay sabitleri (N/m); $b_1$: $m_1$'in zemin sönümü (N·s/m)
> - $x_1,x_2$: konumlar (m); $\dot x_1,\dot x_2$: hızlar (m/s)
> - Durum vektörü: $[x_1,\dot x_1,x_2,\dot x_2]^T$ (4 durum = 2 kütle × 2)
> - $f(t)$: dış kuvvet — giriş (N); $A,B$: durum ve giriş matrisleri

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=1.5mm, post length=1.5mm, segment length=2.2mm, amplitude=2mm}}]
% Duvar
\draw[very thick] (0,0)--(0,1.7);
\foreach \y in {0.2,0.6,...,1.6}{ \draw (0,\y)--(-0.25,\y+0.18); }
% Zemin
\draw[very thick] (0,0) -- (6.4,0);
% k1: duvar -> m1
\draw[spring] (0,1.2)--(1.6,1.2); \node at (0.8,1.6){$k_1$};
% m1
\draw[very thick, fill=blue!5] (1.6,0.8) rectangle (2.6,1.6); \node at (2.1,1.2){$m_1$};
% k2: m1 -> m2
\draw[spring] (2.6,1.2)--(4.1,1.2); \node at (3.35,1.6){$k_2$};
% m2
\draw[very thick, fill=blue!5] (4.1,0.8) rectangle (5.1,1.6); \node at (4.6,1.2){$m_2$};
% f
\draw[->, red!70!black, very thick] (5.1,1.2)--(6.0,1.2) node[right]{$f(t)$};
% b1: m1 -> zemin
\draw[thick] (2.1,0.8)--(2.1,0.62);
\draw[thick] (1.85,0.28) rectangle (2.35,0.62);
\draw[thick] (1.9,0.5)--(2.3,0.5);
\draw[thick] (2.1,0.28)--(2.1,0);
\node at (2.65,0.4){$b_1$};
% x1, x2
\node at (2.1,-0.3){$x_1$}; \node at (4.6,-0.3){$x_2$};
\end{tikzpicture}
\end{document}
```

**Denklemler:**
$$m_1\ddot{x}_1 = -k_1 x_1 - k_2(x_1-x_2) - b_1\dot{x}_1$$
$$m_2\ddot{x}_2 = -k_2(x_2-x_1) + f$$

**4. dereceden durum uzayı:** $[x_1, \dot{x}_1, x_2, \dot{x}_2]^T$

$$A = \begin{bmatrix} 0 & 1 & 0 & 0 \\ -(k_1+k_2)/m_1 & -b_1/m_1 & k_2/m_1 & 0 \\ 0 & 0 & 0 & 1 \\ k_2/m_2 & 0 & -k_2/m_2 & 0 \end{bmatrix}$$

$$B = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1/m_2 \end{bmatrix}$$

---

## SS Örnek 1 — Mekanik Sistem State-Space

> [!example] Problem
> **Sistem:** Duvara $k$ yayı ∥ $b$ sönümleyicisiyle bağlı kütle $m$; giriş kuvveti $f(t)$, çıkış konum $x(t)$.
>
> **İstenen:** Genel $A,B,C,D$ matrisleri; ardından $m=1,k=9,b=3$ için sayısal hâli ve TF doğrulaması.

> [!note]- Semboller
> - $m,k,b$: kütle (kg), yay sabiti (N/m), sönüm (N·s/m)
> - $x_1=x$: konum durumu, $x_2=\dot x$: hız durumu
> - $u=f(t)$: giriş kuvveti (N)
> - $A,B,C,D$: durum, giriş, çıkış, ileri-besleme matrisleri
> - $G(s)=C(sI-A)^{-1}B$: transfer fonksiyonu

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2.2mm}}]
% Duvar
\draw[very thick] (0,-0.9) -- (0,0.9);
\foreach \y in {-0.7,-0.3,...,0.9}{ \draw (0,\y) -- (-0.28,\y-0.22); }
% k (üst)
\draw[spring] (0,0.45) -- (3,0.45); \node at (1.5,0.95){$k$};
% b (alt): silindir + piston
\draw[thick] (0,-0.45) -- (0.9,-0.45);
\draw[thick] (0.9,-0.72) rectangle (1.5,-0.18);
\draw[thick] (1.35,-0.65) -- (1.35,-0.25);
\draw[thick] (1.2,-0.45) -- (3,-0.45);
\node at (1.1,-1.0){$b$};
% Kütle
\draw[very thick, fill=blue!5] (3,-0.85) rectangle (4.4,0.85); \node at (3.7,0){\large $m$};
% f
\draw[->, red!70!black, very thick] (4.4,0) -- (5.7,0) node[right]{$f(t)$};
% x
\draw[->, green!50!black, thick] (3.4,1.15) -- (4.4,1.15) node[right]{$x(t)$};
\end{tikzpicture}
\end{document}
```

**Adım 1 — Hareket denklemi:** $m\ddot{x} + b\dot{x} + kx = f(t)$ → 2. dereceli → 2 durum değişkeni

**Adım 2 — Durum değişkenleri:** $x_1 = x(t)$, $x_2 = \dot{x}(t)$

$$\dot{x}_1 = x_2, \qquad \dot{x}_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2 + \frac{1}{m}u$$

**Adım 3 — Matris formu ($\dot{x} = Ax + Bu$, $y = Cx + Du$):**

$$\boxed{A = \begin{bmatrix} 0 & 1 \\ -\dfrac{k}{m} & -\dfrac{b}{m} \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ \dfrac{1}{m} \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}, \quad D = \begin{bmatrix} 0 \end{bmatrix}}$$

**Sayısal örnek** ($m=1$, $k=9$, $b=3$):

$$A = \begin{bmatrix} 0 & 1 \\ -9 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

```matlab
A = [0 1; -9 -3]; B = [0; 1]; C = [1 0]; D = 0;
G = ss(A,B,C,D);
[num,den] = ss2tf(A,B,C,D)
```

**TF doğrulaması:** $G(s) = C(sI-A)^{-1}B = \dfrac{1/m}{s^2+(b/m)s+(k/m)}$

---

## SS Örnek 2 — Verilen Matrislerden TF Hesabı

> [!example] Problem
> **Verilen:** Faz-değişken (controllable canonical) formda $A_{3\times3}$, $B$, $C$ aşağıdaki gibi.
>
> **İstenen:** $G(s)=C(sI-A)^{-1}B$ transfer fonksiyonu ve kararlılık yorumu.

> [!note]- Semboller
> - $A,B,C$: durum uzayı matrisleri; $D=0$
> - $sI-A$: karakteristik matris; $\Delta=\det(sI-A)$: karakteristik polinom (payda)
> - $\text{adj}(\cdot)$: ek (adjugate) matris; $C\,\text{adj}(sI-A)\,B$: pay
> - Faz-değişken formda payda katsayıları doğrudan $A$'nın son satırından okunur
> - Kutuplar: $\Delta=0$ kökleri; hepsi Re$<0$ → kararlı

$$A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -24 & -26 & -9 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ 24 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix}, \quad D = 0$$

**$G(s) = C(sI-A)^{-1}B$:**

$sI-A = \begin{bmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 24 & 26 & s+9 \end{bmatrix}$

**Determinant** (1. satıra göre açılım):
$$\Delta = s\bigl[s(s+9)+26\bigr] -(-1)\bigl[0\cdot(s+9)-(-1)\cdot24\bigr]= s^3+9s^2+26s+24$$

**Adjugate × B:** Pay $C\,\text{adj}(sI-A)\,B = 24$ (ayrıntılı kofaktör hesabı **SS Örnek 5**'te adım adım).

$$\boxed{G(s) = \frac{24}{s^3+9s^2+26s+24} = \frac{24}{(s+2)(s+3)(s+4)}}$$

Tüm kutuplar sol yarı düzlemde → **asimptotik kararlı** ✓

---

## SS Örnek 3 — İki Kütleli Sistem State-Space

> [!example] Problem
> **Sistem:** Duvar → $b$ sönümleyici → $m_1$ → $k$ yay → $m_2$; giriş $u$ → $m_2$'ye. Çıkışlar $y_1=$ $m_1$ konumu, $y_2=$ $m_2$ konumu.
>
> **İstenen:** $[y_1,y_2,\dot y_1,\dot y_2]^T$ durumlarıyla $A,B,C,D$ ($y=y_2$ çıkışı için).

> [!note]- Semboller
> - $m_1,m_2$: kütleler (kg); $b$: $m_1$–duvar sönümü (N·s/m); $k$: $m_1$–$m_2$ yayı (N/m)
> - $y_1,y_2$: kütle konumları (m); $\dot y_1,\dot y_2$: hızlar
> - Durum sırası: $[y_1,y_2,\dot y_1,\dot y_2]^T$
> - $u$: giriş kuvveti (N); $A,B,C,D$: durum uzayı matrisleri

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.5mm, amplitude=2mm}}]
% Duvar
\draw[very thick] (0,-0.8) -- (0,0.8);
\foreach \y in {-0.6,-0.2,...,0.8}{ \draw (0,\y) -- (-0.26,\y-0.2); }
% b: duvar -> m1
\draw[thick] (0,0) -- (0.7,0);
\draw[thick] (0.7,-0.27) rectangle (1.25,0.27);
\draw[thick] (1.12,-0.2) -- (1.12,0.2);
\draw[thick] (1.0,0) -- (1.7,0);
\node at (0.85,0.55){$b$};
% m1
\draw[very thick, fill=blue!5] (1.7,-0.7) rectangle (2.8,0.7); \node at (2.25,0){$m_1$};
% k: m1 -> m2
\draw[spring] (2.8,0) -- (4.6,0); \node at (3.7,0.5){$k$};
% m2
\draw[very thick, fill=blue!5] (4.6,-0.7) rectangle (5.7,0.7); \node at (5.15,0){$m_2$};
% u
\draw[->, red!70!black, very thick] (5.7,0) -- (6.6,0) node[right]{$u$};
% y1, y2
\draw[->, thick] (1.9,1.05) -- (2.7,1.05) node[right]{$y_1$};
\draw[->, thick] (4.8,1.05) -- (5.6,1.05) node[right]{$y_2$};
\end{tikzpicture}
\end{document}
```

**Hareket denklemleri:**

$$m_1\ddot{y}_1 + b\dot{y}_1 + ky_1 = ky_2 \implies \ddot{y}_1 = -\frac{k}{m_1}y_1 - \frac{b}{m_1}\dot{y}_1 + \frac{k}{m_1}y_2$$

$$m_2\ddot{y}_2 + ky_2 = ky_1 + u \implies \ddot{y}_2 = \frac{k}{m_2}y_1 - \frac{k}{m_2}y_2 + \frac{1}{m_2}u$$

**Durum değişkenleri:** $x = [y_1,\ y_2,\ \dot{y}_1,\ \dot{y}_2]^T$

$$\boxed{A = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -\frac{k}{m_1} & \frac{k}{m_1} & -\frac{b}{m_1} & 0 \\ \frac{k}{m_2} & -\frac{k}{m_2} & 0 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ 0 \\ \frac{1}{m_2} \end{bmatrix}}$$

$y = y_2$ için $C = \begin{bmatrix} 0 & 1 & 0 & 0 \end{bmatrix}$, $D = 0$

---

## SS Örnek 4 — RLC Devre State-Space

> [!example] Problem
> **Devre:** Kaynak $u(t)$; $C$ paralel kola, ardından $L$ seri, çıkışta $R$. Çıkış $V_o=$ direnç gerilimi.
>
> **İstenen:** $x_1=V_C$, $x_2=i_L$ durumlarıyla $A,B,C,D$.

> [!note]- Semboller
> - $u(t)$: kaynak gerilimi — giriş (V); $V_o$: direnç gerilimi — çıkış (V)
> - $x_1=V_C$: kondansatör gerilimi durumu (V); $x_2=i_L$: bobin akımı durumu (A)
> - $C,L,R$: kapasitans (F), indüktans (H), direnç (Ω)
> - Kondansatör: $i_C=C\,\dot V_C$; bobin: $v_L=L\,\dot i_L$ (durum türevleri buradan)
> - $A,B,C_{mat},D$: durum uzayı matrisleri

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$u(t)$, invert] (0,2.6);
\draw (0,2.6) -- (1.5,2.6) coordinate(a);
\draw (a) to[C=$C$, v_<=$V_C$] (1.5,0);
\draw (a) to[L=$L$, i>^=$i_L$] (4,2.6) coordinate(b);
\draw (b) to[R=$R$, v=$V_o$] (4,0);
\draw (0,0) -- (4,0);
\end{circuitikz}
\end{document}
```

**Durum değişkenleri:** $x_1 = V_C$ (kondansatör gerilimi), $x_2 = i_L$ (bobin akımı)

Çıkış: $V_o = i_L \cdot R = Rx_2$

**Devre denklemleri (KCL):**

$$\dot{x}_1 = \frac{u(t)}{C} - \frac{x_2}{C}, \qquad \dot{x}_2 = \frac{x_1}{L} - \frac{R}{L}x_2$$

$$\boxed{\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} 0 & -\dfrac{1}{C} \\ \dfrac{1}{L} & -\dfrac{R}{L} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} \dfrac{1}{C} \\ 0 \end{bmatrix} u, \quad y = \begin{bmatrix} 0 & R \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}}$$

---

## SS Örnek 5 — $C(sI-A)^{-1}B$ Adım Adım

> [!example] Problem
> **Verilen:** SS Örnek 2'deki aynı matrisler. $(sI-A)^{-1}$ tersini kofaktör/adjugate yöntemiyle açıkça hesaplayıp $G(s)$'i türet.

> [!note]- Semboller
> - $sI-A$: karakteristik matris; $\Delta=\det(sI-A)$: payda polinomu
> - $M_{ij}$: $(i,j)$ kofaktörü $=(-1)^{i+j}\times$ ilgili minör determinantı
> - $\text{adj}(sI-A)=[M_{ij}]^T$: ek matris; $(sI-A)^{-1}=\text{adj}/\Delta$
> - $C\,(sI-A)^{-1}B$: $C$ ve $B$ yalnız belirli kofaktörleri seçer (burada $M_{13}$)
> - $B_1,B_2,B_3$: $B$ vektörünün bileşenleri ($0,0,24$)

Örnek 2 ile aynı matrisler: $A_{3\times3}$, $B=[0\ 0\ 24]^T$, $C=[1\ 0\ 0]$

**Adım 1:** $sI-A = \begin{bmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 24 & 26 & s+9 \end{bmatrix}$

**Adım 2 — Det (1. sıraya göre açılım):**

$$\Delta = s\bigl[s(s+9)+26\bigr] + 1\cdot[0\cdot(s+9)+24] = s^3+9s^2+26s+24$$

**Adım 3 — Cofactor $(1,3)$ pozisyonu:**

$M_{13} = (-1)^{1+3}\begin{vmatrix} 0 & s \\ 24 & 26 \end{vmatrix} = (+1)(0\cdot26 - s\cdot24) = -24s$

**Adım 4:**

$$C\,[sI-A]^{-1}B = \frac{1}{\Delta}\bigl[M_{13}\cdot B_3 + M_{11}\cdot B_1 + M_{12}\cdot B_2\bigr] = \frac{24}{\Delta}$$

$$\boxed{G(s) = \frac{24}{s^3+9s^2+26s+24} = \frac{24}{(s+2)(s+3)(s+4)}}$$

---

## SS Örnek 6 — C₁-R-L-C₂ Üçüncü Dereceden State-Space

> [!example] Problem
> **Devre:** Kaynak $V_i$; $C_1$ paralel kola; ardından $R$ ve $L$ seri; çıkışta $C_2$. Çıkış $V_o=V_{C_2}$.
>
> **İstenen:** Üç enerji depolayan eleman → 3 durum ($V_{C_1},i_L,V_{C_2}$) ile $A,B,C,D$.

> [!note]- Semboller
> - $V_i$: kaynak gerilimi — giriş (V); $V_o=V_{C_2}$: çıkış (V)
> - $x_1=V_{C_1}$, $x_2=i_L$, $x_3=V_{C_2}$: durum değişkenleri (V, A, V)
> - $C_1,C_2$: kapasitanslar (F); $R$: direnç (Ω); $L$: indüktans (H)
> - $n=3$: durum sayısı = bağımsız enerji depolayan eleman sayısı
> - $A,B,C_{mat},D$: durum uzayı matrisleri

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$V_i$, invert] (0,2.6);
\draw (0,2.6) -- (1.3,2.6) coordinate(a);
\draw (a) to[C=$C_1$] (1.3,0);
\draw (a) to[R=$R$, i>^=$i_L$] (3.3,2.6) to[L=$L$] (5.3,2.6) coordinate(b);
\draw (b) to[C=$C_2$, v=$V_o$] (5.3,0);
\draw (0,0) -- (5.3,0);
\end{circuitikz}
\end{document}
```

**Durum değişkenleri** (3 depolama elemanı → $n=3$):

$$x_1 = V_{C_1}, \quad x_2 = i_L, \quad x_3 = V_{C_2}$$

**KCL ve KVL'den türetilen durum denklemleri:**

$$\dot{x}_1 = -\frac{1}{RC_1}x_1 + \frac{1}{C_1}x_2 - \frac{1}{RC_1}x_3 + \frac{1}{RC_1}V_i$$

$$\dot{x}_2 = -\frac{1}{L}x_1 + \frac{1}{L}V_i$$

$$\dot{x}_3 = -\frac{1}{RC_2}x_1 - \frac{1}{RC_2}x_3 + \frac{1}{RC_2}V_i$$

$$\boxed{A = \begin{bmatrix} -\frac{1}{RC_1} & \frac{1}{C_1} & -\frac{1}{RC_1} \\ -\frac{1}{L} & 0 & 0 \\ -\frac{1}{RC_2} & 0 & -\frac{1}{RC_2} \end{bmatrix}, \quad B = \begin{bmatrix} \frac{1}{RC_1} \\ \frac{1}{L} \\ \frac{1}{RC_2} \end{bmatrix}}$$

$y = V_o = V_{C_2} = x_3$ için $C_{mat} = [0\ 0\ 1]$, $D=0$
