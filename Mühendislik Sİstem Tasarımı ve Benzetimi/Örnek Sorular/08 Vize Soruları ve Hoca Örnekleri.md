---
tags: [mst, vize, sınav-soruları, çözümlü, durum-uzayı, lagrange, dişli, dc-motor, opamp, devre]
---

# 08 — MST&B Vize Soruları ve Hoca Örnekleri (Çözümlü)

← [[MST Ana Sayfa]] | İlgili: [[01 Mekanik Sistemler Örnekleri]] · [[02 Elektrik Sistemleri Örnekleri]] · [[03 Durum Uzayı Örnekleri]]

> Kaynak: Hoca (Asım) vize hazırlık çözümlü örnekleri (`Asım vize 1.pdf`, 24 sf.) + quiz soruları (`Asım vize 2.pdf`, 4 sf.). Tüm sorular soru metni + adım adım çözüm + sembol hatırlatıcısı ile yeniden yazıldı; el yazısı taramalardaki birkaç özensiz ara satır temiz biçimde yeniden türetildi.

> [!sinav] Vize Kapsamı — Tek Bakışta
> Bu dersin vizesi **sistem modelleme** üzerinedir: bir fiziksel sistemi (mekanik, elektrik, elektromekanik) denklemlerine dök → Laplace'a geçir → **transfer fonksiyonu** veya **durum-uzayı** modeli çıkar. Yinelenen iskelet:
> 1. Her kütle/düğüm/göz için denge denklemi (Newton, KVL/KCL, Lagrange)
> 2. Laplace dönüşümü (başlangıç koşulları sıfır)
> 3. Matris formu + **Cramer** ile istenen değişkeni çek
> 4. Gerekiyorsa ters Laplace ile zaman yanıtı

---

# A. Quizler (Gerçek Vize Quiz Soruları)

## Quiz 1 — Dönel Mekanik Sistem: $\theta_2(s)/T(s)$

**Soru:** Şekildeki dönel sistemde sol eylemsizliğe ($J=1$) $T(t)$ torku uygulanıyor. $\theta_1$ ile $\theta_2$ arasında paralel yay $k_1=1$ ve sönüm $b_1=1$ var. $\theta_2$ düğümünde toprağa sönüm $b_2=1$ ve duvara yay $k_2=1$ bağlı. Transfer fonksiyonu $\dfrac{\theta_2(s)}{T(s)}$'yi bulun.

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={coil, aspect=0.5, segment length=2.6mm, amplitude=1.8mm}}]
% J diski (theta1)
\draw[thick] (0,0) circle (0.7); \node at (0,0) {$J$}; \node at (0,1.0){$\theta_1$};
\draw[->, thick] (-1.4,0.8) arc (150:30:0.45); \node at (-1.0,1.15) {$T$};
% k1 ve b1 (theta1 -> theta2), paralel
\draw[spring] (0.7,0.25) -- (3.0,0.25); \node at (1.85,0.6){$k_1$};
\draw[thick] (0.7,-0.25)--(1.6,-0.25); \draw[thick](1.6,-0.45)--(1.6,-0.05);
\draw[thick](1.45,-0.45)rectangle(2.0,-0.05); \draw[thick](2.0,-0.25)--(3.0,-0.25);
\node at (1.85,-0.7){$b_1$};
% theta2 düğümü
\draw[thick,fill=black] (3.0,0) circle (0.06); \node at (3.0,0.55){$\theta_2$};
% k2 duvara (sağ)
\draw[spring] (3.0,0.25) -- (5.0,0.25); \node at (4.0,0.6){$k_2$};
\draw[very thick] (5.0,-0.4)--(5.0,0.7);
% b2 toprağa (aşağı)
\draw[thick](3.0,-0.1)--(3.0,-0.9); \draw[thick](2.75,-0.9)rectangle(3.25,-1.3);
\node at (3.6,-1.1){$b_2$}; \draw[thick](2.6,-1.45)--(3.4,-1.45);
\foreach \x in {2.65,2.85,...,3.25}{\draw(\x,-1.45)--(\x-0.12,-1.6);}
\end{tikzpicture}
\end{document}
```

> [!note]- Semboller
> - $\theta_1,\theta_2$: 1. ve 2. düğümün açısal konumları (rad)
> - $J$: eylemsizlik momenti (yalnızca 1. düğümde, $\text{kg·m}^2$); $T$: uygulanan tork (N·m)
> - $k_1,k_2$: burulma yayı katsayıları (N·m/rad); $b_1,b_2$: dönel sönüm katsayıları (N·m·s/rad)
> - Dönel benzeşim: $T=J\ddot\theta$ (eylemsizlik), $T=b\dot\theta$ (sönüm), $T=k\theta$ (yay)
> - İki düğüm **arasındaki** eleman, her iki denklemde **fark** ($\theta_1-\theta_2$) olarak görünür → çapraz (kuplaj) terimleri verir

**Çözüm:**

**1. düğüm ($\theta_1$) tork dengesi** — düğüme etkiyen tüm torklar:
$$T = \underbrace{J\ddot\theta_1}_{\text{eylemsizlik}} + \underbrace{b_1(\dot\theta_1-\dot\theta_2)}_{\text{sönüm }b_1} + \underbrace{k_1(\theta_1-\theta_2)}_{\text{yay }k_1}$$

Laplace ($J=b_1=k_1=1$):
$$T(s) = \theta_1(Js^2+b_1s+k_1) - \theta_2(b_1s+k_1) = \theta_1(s^2+s+1) - \theta_2(s+1)$$

**2. düğüm ($\theta_2$) tork dengesi** — bu düğümde eylemsizlik yok; gelen kuplaj + kendi yay/sönümü:
$$0 = b_1(\dot\theta_2-\dot\theta_1) + k_1(\theta_2-\theta_1) + b_2\dot\theta_2 + k_2\theta_2$$

Laplace ($b_2=k_2=1$):
$$0 = \theta_2(b_1s+k_1+b_2s+k_2) - \theta_1(b_1s+k_1) = \theta_2(2s+2) - \theta_1(s+1)$$

**Matris formu:**
$$\begin{bmatrix} s^2+s+1 & -(s+1) \\ -(s+1) & 2s+2 \end{bmatrix}\begin{bmatrix}\theta_1\\\theta_2\end{bmatrix} = \begin{bmatrix}T(s)\\0\end{bmatrix}$$

**Determinant** (ortak çarpan $s+1$'i dışarı al):
$$\Delta = (s^2+s+1)(2s+2) - (s+1)^2 = (s+1)\big[2(s^2+s+1)-(s+1)\big] = (s+1)(2s^2+s+1)$$
$$\Delta = 2s^3+3s^2+2s+1$$

**Cramer ile $\theta_2$** (2. sütuna sağ tarafı koy):
$$\theta_2 = \frac{1}{\Delta}\det\begin{bmatrix} s^2+s+1 & T(s) \\ -(s+1) & 0 \end{bmatrix} = \frac{T(s)\,(s+1)}{\Delta}$$

$$\boxed{\dfrac{\theta_2(s)}{T(s)} = \dfrac{s+1}{2s^3+3s^2+2s+1}}$$

---

## Quiz 2 — İki Gözlü RL Devre: $V_L/V_S$ ve Dürtü Yanıtı

**Soru:** İki gözlü devrede sol gözde $2\,\text{H}$ bobin, gözler arası ortak $2\,\Omega$ direnç, sağ gözde $2\,\Omega$ direnç ve çıkış bobini $2\,\text{H}$ ($V_L$ üzerinde). Kaynak $V_i(t)$. (a) $V_L/V_i$ transfer fonksiyonunu, (b) $V_i(t)=\delta(t)$ için $V_L(t)$'yi bulun.

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$v_i$] (0,2.5);
\draw (0,2.5) to[L=$2\,\mathrm{H}$] (3,2.5) -- (3,2.5);
\draw (3,2.5) to[R=$2\,\Omega$] (3,0); % ortak direnç
\draw (3,2.5) to[R=$2\,\Omega$] (6,2.5);
\draw (6,2.5) to[L=$2\,\mathrm{H}$, v=$v_L$] (6,0);
\draw (0,0) -- (6,0);
\node at (1.5,1.0) {$i_1$};
\node at (4.5,1.0) {$i_2$};
\end{circuitikz}
\end{document}
```

> [!note]- Semboller
> - $i_1,i_2$: 1. ve 2. göz çevre akımları (A); $V_i$: kaynak gerilimi (V); $V_L$: sağ bobin gerilimi (V)
> - Bobin empedansı: $Z_L=Ls$ → $2\,\text{H}\Rightarrow 2s$; direnç $Z_R=R$
> - Ortak (gözler arası) eleman, her iki çevre denkleminde akım farkıyla ($i_1-i_2$) görünür
> - $\delta(t)$: birim dürtü → $V_i(s)=1$, yani $V_L(s)=$ transfer fonksiyonunun kendisi
> - $\cosh,\sinh$: payda kökleri **reel ve ayrık** olduğunda ortaya çıkar (aşırı sönümlü)

**Çözüm:**

**Çevre denklemleri (KVL, $Z_L=2s$, $R=2$):**
$$V_i = 2s\,i_1 + 2(i_1-i_2) \;\Rightarrow\; I_1(2s+2) - 2I_2 = V_i(s)$$
$$0 = 2(i_2-i_1) + 2i_2 + 2s\,i_2 \;\Rightarrow\; -2I_1 + I_2(2s+4) = 0$$

**Matris + Cramer ile $I_2$:**
$$\begin{bmatrix}2s+2 & -2\\ -2 & 2s+4\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}=\begin{bmatrix}V_i\\0\end{bmatrix}, \quad \Delta=(2s+2)(2s+4)-4 = 4s^2+12s+4$$
$$I_2 = \frac{\det\begin{bmatrix}2s+2 & V_i\\ -2 & 0\end{bmatrix}}{\Delta} = \frac{2V_i}{4s^2+12s+4}$$

**Çıkış bobini gerilimi** ($i_2$ üzerinden, $V_L=2s\,I_2$):
$$V_L = 2s\cdot\frac{2V_i}{4s^2+12s+4} = \frac{4s\,V_i}{4s^2+12s+4}$$

$$\boxed{\dfrac{V_L(s)}{V_i(s)} = \dfrac{s}{s^2+3s+1}}$$

**(b) Dürtü yanıtı** ($V_i(s)=1$):
$$V_L(s)=\frac{s}{s^2+3s+1}$$
Payda kökleri: $s=\dfrac{-3\pm\sqrt{9-4}}{2}=-1{,}5\pm\underbrace{1{,}118}_{a=\sqrt{1{,}25}}$ → tamkareye tamamla:
$$s^2+3s+1=(s+1{,}5)^2-1{,}25$$
Payı $(s+1{,}5)$ etrafında yaz: $s=(s+1{,}5)-1{,}5$:
$$V_L(s)=\frac{(s+1{,}5)}{(s+1{,}5)^2-1{,}25} - \frac{1{,}5}{(s+1{,}5)^2-1{,}25}$$

Ters Laplace ($\mathcal{L}^{-1}\{\frac{s+a}{(s+a)^2-b^2}\}=e^{-at}\cosh bt$, $\mathcal{L}^{-1}\{\frac{1}{(s+a)^2-b^2}\}=\frac{1}{b}e^{-at}\sinh bt$):
$$\boxed{v_L(t) = e^{-1{,}5t}\cosh(1{,}12t) - 1{,}34\,e^{-1{,}5t}\sinh(1{,}12t)}$$
(burada $\dfrac{1{,}5}{1{,}118}\approx1{,}34$)

---

## Quiz 3 — İki Gözlü RLC Devre: $V_L/V_i$ ve Basamak Yanıtı

**Soru:** Devrede üst kolda $2\,\Omega + 1\,\text{F}$, gözler arası ortak kolda $2\,\Omega + 1\,\text{F}$, sağ kolda $2\,\Omega + 2\,\text{H}$ ($V_L$ çıkışı). Kaynak $V_i(t)$. (a) $G(s)=V_L/V_i$, (b) $V_i(t)=u(t)$ (birim basamak) için $V_L(t)$'yi bulun.

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$v_i$] (0,2.5);
\draw (0,2.5) to[R=$2\,\Omega$] (2,2.5) to[C=$1\,\mathrm{F}$] (4,2.5);
\draw (4,2.5) to[R=$2\,\Omega$] (4,1.4) to[C=$1\,\mathrm{F}$] (4,0); % ortak kol
\draw (4,2.5) to[R=$2\,\Omega$] (6,2.5);
\draw (6,2.5) to[L=$2\,\mathrm{H}$, v=$v_L$] (6,0);
\draw (0,0) -- (6,0);
\node at (2,1.0) {$i_1$};
\node at (5,1.0) {$i_2$};
\end{circuitikz}
\end{document}
```

> [!note]- Semboller
> - $i_1,i_2$: çevre akımları (A); kapasitör empedansı $Z_C=\dfrac{1}{Cs}$ → $1\,\text{F}\Rightarrow \dfrac{1}{s}$
> - $u(t)$: birim basamak → $V_i(s)=\dfrac{1}{s}$
> - Çevre öz-empedansı = o gözdeki tüm elemanların toplamı; ortak kol iki denklemde de görünür
> - $\det$'i $s$ paydalarından kurtarmak için tüm satırı $s^2$ ile çarp → polinom payda

**Çözüm:**

**Çevre denklemleri (empedans yöntemi):**
$$V_i = I_1\underbrace{\Big(2+\tfrac1s+2+\tfrac1s\Big)}_{\text{öz}} - I_2\underbrace{\Big(2+\tfrac1s\Big)}_{\text{ortak}} = I_1\Big(4+\tfrac2s\Big) - I_2\Big(2+\tfrac1s\Big)$$
$$0 = -I_1\Big(2+\tfrac1s\Big) + I_2\underbrace{\Big(2+\tfrac1s+2+2s\Big)}_{\text{öz: ortak kol + sağ kol}} = -I_1\Big(2+\tfrac1s\Big)+I_2\Big(2s+4+\tfrac1s\Big)$$

**Determinant:**
$$\Delta=\Big(4+\tfrac2s\Big)\Big(2s+4+\tfrac1s\Big)-\Big(2+\tfrac1s\Big)^2 = 8s+16+\tfrac8s+\tfrac1{s^2}$$
$s^2$ ile düzenle → ortak payda $s^2$: $\;\Delta=\dfrac{8s^3+16s^2+8s+1}{s^2}$

**Cramer ile $I_2$:**
$$I_2=\frac{\det\begin{bmatrix}4+\frac2s & V_i\\ -(2+\frac1s) & 0\end{bmatrix}}{\Delta} = \frac{V_i\big(2+\frac1s\big)}{\Delta} = \frac{V_i\,(2s+1)\,s}{8s^3+16s^2+8s+1}$$

**Çıkış** ($V_L=2s\,I_2$):
$$V_L = 2s\cdot\frac{V_i(2s+1)s}{8s^3+16s^2+8s+1} = \frac{2s^2(2s+1)\,V_i}{8s^3+16s^2+8s+1}$$

Payda çarpanlara ayrılır: $8s^3+16s^2+8s+1=(2s+1)(4s^2+6s+1)$, pay $2s^2(2s+1)$ → $(2s+1)$ sadeleşir:
$$G(s)=\frac{2s^2}{4s^2+6s+1} \;\xrightarrow{\div 4}\; \boxed{G(s)=\dfrac{V_L}{V_i}=\dfrac{\tfrac12 s^2}{s^2+1{,}5s+0{,}25}}$$

**(b) Basamak yanıtı** ($V_i(s)=\tfrac1s$):
$$V_L(s)=G(s)\cdot\frac1s = \frac{\tfrac12 s^2}{s(s^2+1{,}5s+0{,}25)} = \frac{\tfrac12 s}{s^2+1{,}5s+0{,}25}$$
Payda: $(s+0{,}75)^2-0{,}3125$, $\;b=\sqrt{0{,}3125}=0{,}559\approx0{,}55$. Payı $(s+0{,}75)$ etrafında yaz:
$$V_L(s)=\tfrac12\frac{(s+0{,}75)}{(s+0{,}75)^2-0{,}3125} - \frac{0{,}375}{(s+0{,}75)^2-0{,}3125}$$
$$\boxed{v_L(t)=\tfrac12 e^{-0{,}75t}\cosh(0{,}55t) - 0{,}67\,e^{-0{,}75t}\sinh(0{,}55t)}$$
(burada $\dfrac{0{,}375}{0{,}559}\approx0{,}67$)

> [!warning] Tarama notu
> El yazısı çözümde ara satırda $\frac12 s^2$ payı $\frac12 s$ yerine sehven $s^2$ olarak kalmıştı; basamak girişi $\frac1s$ ile çarpınca doğru pay $\frac12 s$ olur ve yukarıdaki sonuç çıkar (öğrencinin nihai sayısal cevabıyla uyumlu).

---

# B. Durum-Uzayı (State-Space) Modelleme

> [!formul] Genel İskelet
> $$\dot{\mathbf x}=A\mathbf x+B u,\qquad y=C\mathbf x+Du$$
> - **Durum seçimi:** her enerji depolayan eleman bir durum verir → mekanikte konum & hız ($x,\dot x$), elektrikte **kapasitör gerilimi** $v_C$ & **bobin akımı** $i_L$.
> - Durum-uzayı → transfer fonksiyonu: $\;G(s)=C(sI-A)^{-1}B+D$.

## Örnek B1 — Kütle-Yay-Sönüm → Durum Uzayı

**Soru:** $m\ddot x+b\dot x+kx=f(t)$ kütle-yay-sönüm sistemini durum-uzayı formunda yazın ve $X(s)/F(s)$ transfer fonksiyonunu bulun.

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=2mm, post length=2mm, segment length=2.6mm, amplitude=2mm}}]
% Duvar
\draw[very thick] (0,-1.3) -- (0,1.3);
\foreach \y in {-1.1,-0.7,...,1.1}{ \draw (0,\y) -- (-0.24,\y+0.2); }
% Yay (üst) ve sönüm (alt)
\draw[spring] (0,0.6) -- (2.6,0.6); \node at (1.3,1.05) {$k$};
\draw[thick] (0,-0.6)--(1.2,-0.6); \draw[thick](1.2,-0.85)--(1.2,-0.35);
\draw[thick](1.05,-0.85)rectangle(1.7,-0.35); \draw[thick](1.7,-0.6)--(2.6,-0.6);
\node at (1.3,-1.05) {$b$};
% Kütle
\draw[thick] (2.6,-0.95) rectangle (4.0,0.95); \node at (3.3,0) {$m$};
% Kuvvet
\draw[->,thick] (4.0,0) -- (5.2,0) node[right]{$f(t)$};
\draw[->] (3.3,1.25) -- (4.1,1.25) node[right]{$x$};
\end{tikzpicture}
\end{document}
```

> [!note]- Semboller
> - $x$: kütlenin konumu (m); $\dot x$: hız (m/s); $f(t)$: uygulanan kuvvet (N)
> - $m$: kütle (kg); $b$: viskoz sönüm (N·s/m); $k$: yay sabiti (N/m)
> - Durumlar: $x_1=x$ (konum), $x_2=\dot x$ (hız) — biri konum biri hız (2. derece sistem → 2 durum)

**Çözüm:** Durumları $x_1=x,\;x_2=\dot x$ seç. O hâlde $\dot x_1=x_2$. İkinci denklemi $\ddot x$ için çöz:
$$\ddot x = \frac{f}{m}-\frac{b}{m}\dot x-\frac{k}{m}x \;\Rightarrow\; \dot x_2 = -\frac{k}{m}x_1-\frac{b}{m}x_2+\frac1m f$$
$$\begin{bmatrix}\dot x_1\\\dot x_2\end{bmatrix}=\begin{bmatrix}0&1\\-\frac{k}{m}&-\frac{b}{m}\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}+\begin{bmatrix}0\\\frac1m\end{bmatrix}f,\qquad y=\begin{bmatrix}1&0\end{bmatrix}\mathbf x$$
Transfer fonksiyonu ($G=C(sI-A)^{-1}B$):
$$\boxed{\dfrac{X(s)}{F(s)}=\dfrac{1}{ms^2+bs+k}}$$

## Örnek B2 — 3. Derece DD → Durum Uzayı

**Soru:** $\dddot x+\ddot x+\dot x+x=5$ diferansiyel denklemini durum-uzayı formunda yazın.

> [!note]- Semboller
> - $n$. derece DD → $n$ durum. Burada $n=3$: $x_1=x,\;x_2=\dot x,\;x_3=\ddot x$
> - En yüksek türevi yalnız bırak: $\dddot x = 5-x-\dot x-\ddot x$
> - Sağdaki sabit $5$ → giriş (basamak); $B$ vektörüne yerleşir

**Çözüm:** $\dot x_1=x_2,\;\dot x_2=x_3$ ve
$$\dot x_3=\dddot x = 5 - x_1 - x_2 - x_3$$
$$\begin{bmatrix}\dot x_1\\\dot x_2\\\dot x_3\end{bmatrix}=\begin{bmatrix}0&1&0\\0&0&1\\-1&-1&-1\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}+\begin{bmatrix}0\\0\\5\end{bmatrix}u,\quad u=1$$
(Bu **eşlik/companion** kanonik formdur: son satır karakteristik polinomun katsayılarının negatifidir.)

## Örnek B3 — Durum Uzayı → Transfer Fonksiyonu

**Soru:** $\dot{\mathbf x}=\begin{bmatrix}0&1&0\\0&0&1\\-24&-26&-9\end{bmatrix}\mathbf x+\begin{bmatrix}0\\0\\24\end{bmatrix}u,\;\; y=\begin{bmatrix}1&0&0\end{bmatrix}\mathbf x$ için $G(s)=Y(s)/U(s)$'yi bulun.

> [!note]- Semboller
> - $G(s)=C(sI-A)^{-1}B+D$; $\;D=0$
> - $\det(sI-A)$ → karakteristik polinom (paydadaki ifade)
> - Eşlik formunda $C=[1\;0\;0]$, $B=[0\;0\;b]^T$ ise $G(s)=\dfrac{b}{\det(sI-A)}$ (kısayol)

**Çözüm:**
$$sI-A=\begin{bmatrix}s&-1&0\\0&s&-1\\24&26&s+9\end{bmatrix}$$
$$\det(sI-A)=s\big[s(s+9)+26\big]+1\big[0+24\big]=s^3+9s^2+26s+24$$
Eşlik formu kısayoluyla ($b=24$, $C=[1\,0\,0]$):
$$\boxed{G(s)=\dfrac{24}{s^3+9s^2+26s+24}}$$

## Örnek B4 — İki Kütleli Sistem → Durum Uzayı

**Soru:** $m_1$ ve $m_2$ kütleleri arası yay $k$, $m_1$'de sönüm $b$, kuvvet $u$ $m_2$'ye uygulanıyor. Denklemler: $m_1\ddot y_1+b\dot y_1+k(y_1-y_2)=0$ ve $m_2\ddot y_2+k(y_2-y_1)=u$. Durum-uzayı modelini ($y_1,y_2$ çıkışları) yazın.

> [!note]- Semboller
> - $y_1,y_2$: kütlelerin konumları (m); iki kütle → $2\times2=4$ durum
> - Durumlar: $x_1=y_1,\;x_2=\dot y_1,\;x_3=y_2,\;x_4=\dot y_2$
> - Yay her iki denklemde **fark** $(y_1-y_2)$ olarak → çapraz kuplaj

**Çözüm:** Türevleri yalnız bırak:
$$\ddot y_1=-\frac{k}{m_1}y_1-\frac{b}{m_1}\dot y_1+\frac{k}{m_1}y_2,\qquad \ddot y_2=\frac{k}{m_2}y_1-\frac{k}{m_2}y_2+\frac{1}{m_2}u$$
$$\dot{\mathbf x}=\begin{bmatrix}0&1&0&0\\-\frac{k}{m_1}&-\frac{b}{m_1}&\frac{k}{m_1}&0\\0&0&0&1\\\frac{k}{m_2}&0&-\frac{k}{m_2}&0\end{bmatrix}\mathbf x+\begin{bmatrix}0\\0\\0\\\frac{1}{m_2}\end{bmatrix}u,\qquad y=\begin{bmatrix}1&0&0&0\\0&0&1&0\end{bmatrix}\mathbf x$$

## Örnek B5 — Seri RLC Devre → Durum Uzayı + Transfer Fonksiyonu

**Soru:** Gerilim kaynağı $u(t)$ ile sürülen seri RLC devrede ($R,L,C$) durumları $v_C$ ve $i_L$ alarak durum-uzayı modelini çıkarın; $L=1,\,C=1,\,R=2$ için $V_C(s)/U(s)$'yi bulun.

> [!note]- Semboller
> - $v_C$: kapasitör gerilimi (V, durum 1); $i_L$: bobin akımı (A, durum 2)
> - Yapı denklemleri: $i_L=C\dfrac{dv_C}{dt}$ (kapasitör), $v_L=L\dfrac{di_L}{dt}$ (bobin)
> - Seri kolda kapasitör akımı = bobin akımı = göz akımı

**Çözüm:** Kapasitörden $\dot v_C=\dfrac{i_L}{C}$. KVL ($u=L\dot i_L+Ri_L+v_C$) → $\dot i_L=\dfrac{u-Ri_L-v_C}{L}$:
$$\begin{bmatrix}\dot v_C\\\dot i_L\end{bmatrix}=\begin{bmatrix}0&\frac1C\\-\frac1L&-\frac{R}{L}\end{bmatrix}\begin{bmatrix}v_C\\i_L\end{bmatrix}+\begin{bmatrix}0\\\frac1L\end{bmatrix}u,\qquad y=v_C=\begin{bmatrix}1&0\end{bmatrix}\mathbf x$$
$$\frac{V_C(s)}{U(s)}=\frac{1/LC}{s^2+\frac{R}{L}s+\frac1{LC}}\;\xrightarrow{L=C=1,\,R=2}\;\boxed{\dfrac{1}{s^2+2s+1}}$$

## Örnek B6 — Üç Enerji Elemanlı Devre → 3 Durumlu Model

**Soru:** İki kapasitör ($C_1,C_2$) ve bir bobin ($L$, seri $R$) içeren devrede durum-uzayı modelini kurun.

> [!note]- Semboller
> - Durumlar: $v_{C_1},\,i_L,\,v_{C_2}$ → 3 enerji elemanı = 3 durum
> - Her durum için tek bir türev denklemi: kapasitörde $\dot v_C=\dfrac{i_C}{C}$, bobinde $\dot i_L=\dfrac{v_L}{L}$
> - $i_C$ ve $v_L$'yi KCL/KVL ile **yalnızca durumlar ve giriş** cinsinden yaz

**Çözüm (yöntem):** Durum vektörü $\mathbf x=[v_{C_1},\,i_L,\,v_{C_2}]^T$. Her elemanın yapı denkleminden başla, sağ tarafı düğüm/çevre denklemleriyle durumlara indirge:
$$\dot v_{C_1}=\frac{i_{C_1}}{C_1},\qquad \dot i_L=\frac{v_L}{L}=\frac{v_{C_1}-v_{C_2}-Ri_L}{L},\qquad \dot v_{C_2}=\frac{i_{C_2}}{C_2}=\frac{i_L-i_{R_{çıkış}}}{C_2}$$
Sonuç, $3\times3$ bir $A$ matrisi verir; çıkış $y=v_{C_2}=[0\;0\;1]\mathbf x$. **Ders notu:** durum sayısı = bağımsız enerji elemanı sayısı; her birine bir yapı denklemi yazıp sağ tarafı düğüm denklemleriyle temizlemek tüm modellerin ortak reçetesidir.

---

# C. Lagrange ve Dönel Mekanik

## Örnek C1 — Lagrange Yöntemi (Öteleme + Dönme Bağlaşımı)

**Soru:** $m_1$ ötelenen kütle (konum $x$), $m_2$ ise $2a$ kolla $\theta$ açısına bağlı kütle; yaylar $k_1$ ($x$'e) ve $k_2$ ($x+2a\theta$'ya). Lagrange yöntemiyle hareket denklemlerini çıkarın.

> [!note]- Semboller
> - $x$: öteleme konumu (m); $\theta$: dönme açısı (rad); $a$: kol uzunluğu (m)
> - $KE$: kinetik enerji, $PE$: potansiyel (yay) enerjisi
> - **Lagrange denklemi:** $\dfrac{d}{dt}\!\left(\dfrac{\partial KE}{\partial \dot q}\right)-\dfrac{\partial KE}{\partial q}+\dfrac{\partial PE}{\partial q}=F_q$, her genelleştirilmiş koordinat $q\in\{x,\theta\}$ için
> - $m_2$'nin hızı $\dot x+2a\dot\theta$ (öteleme + dönme katkısı)

**Çözüm:** Enerjileri yaz:
$$KE=\tfrac12 m_1\dot x^2+\tfrac12 m_2(\dot x+2a\dot\theta)^2,\qquad PE=\tfrac12 k_1 x^2+\tfrac12 k_2(x+2a\theta)^2$$

**$x$ için** Lagrange:
$$\frac{d}{dt}\frac{\partial KE}{\partial\dot x}=m_1\ddot x+m_2(\ddot x+2a\ddot\theta),\qquad \frac{\partial PE}{\partial x}=k_1 x+k_2(x+2a\theta)$$
$$\boxed{F(t)=(m_1+m_2)\ddot x+2am_2\ddot\theta+(k_1+k_2)x+2ak_2\theta}$$

**$\theta$ için** Lagrange:
$$\frac{d}{dt}\frac{\partial KE}{\partial\dot\theta}=2am_2(\ddot x+2a\ddot\theta),\qquad \frac{\partial PE}{\partial\theta}=2ak_2(x+2a\theta)$$
$$\boxed{F_\theta=2am_2\ddot x+4a^2m_2\ddot\theta+2ak_2 x+4a^2k_2\theta}$$

## Örnek C2 — İki Eylemsizlikli Dönel Sistem: $\theta_2/T$

**Soru:** $J_1$'e tork $T$ uygulanıyor; $J_1$–$J_2$ arasında yay $k$, her eylemsizlikte toprağa sönüm $b_1,b_2$. $\dfrac{\theta_2(s)}{T(s)}$'yi bulun.

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={coil, aspect=0.5, segment length=3mm, amplitude=2mm}}]
% J1 diski
\draw[thick] (0,0) circle (0.8); \node at (0,0) {$J_1$};
\node at (0,1.1) {$\theta_1$};
% Tork oku
\draw[->, thick] (-1.6,0.9) arc (150:30:0.5); \node at (-1.1,1.3) {$T$};
% Yay J1->J2
\draw[spring] (0.8,0) -- (3.2,0); \node at (2,0.4) {$k$};
% J2 diski
\draw[thick] (4,0) circle (0.8); \node at (4,0) {$J_2$};
\node at (4,1.1) {$\theta_2$};
% Sönümler (toprağa)
\draw[->] (0,-0.8) -- (0,-1.6) node[below]{$b_1$};
\draw[->] (4,-0.8) -- (4,-1.6) node[below]{$b_2$};
\end{tikzpicture}
\end{document}
```

> [!note]- Semboller
> - $J_1,J_2$: eylemsizlik momentleri ($\text{kg·m}^2$); $k$: burulma yayı (N·m/rad); $b_1,b_2$: dönel sönüm (N·m·s/rad)
> - Aralarındaki yay $k$, her iki denklemde $(\theta_1-\theta_2)$ farkı olarak görünür → çapraz $-k$ terimleri

**Çözüm:** Düğüm denklemleri (Laplace):
$$T = \theta_1(J_1s^2+b_1s+k) - \theta_2 k$$
$$0 = \theta_2(J_2s^2+b_2s+k) - \theta_1 k$$
$$\Delta=(J_1s^2+b_1s+k)(J_2s^2+b_2s+k)-k^2$$
Cramer ile $\theta_2 = \dfrac{Tk}{\Delta}$:
$$\boxed{\dfrac{\theta_2(s)}{T(s)}=\dfrac{k}{(J_1s^2+b_1s+k)(J_2s^2+b_2s+k)-k^2}}$$

## Örnek C3 — Basit Sarkaç: 4 Farklı Yöntem ($\omega_n$)

**Soru:** Uzunluğu $L=1\,\text{m}$, kütlesi $m=2\,\text{kg}$ olan basit sarkacın hareket denklemini **(a) Newton, (b) enerji, (c) Lagrange, (d) açısal momentum** yöntemleriyle çıkarın; küçük açı için doğal frekansı bulun ($g=9{,}81$).

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small]
% Tavan
\draw[very thick] (-1.2,0) -- (1.2,0);
\foreach \x in {-1.0,-0.6,...,1.0}{ \draw (\x,0) -- (\x-0.25,0.22); }
% İp
\draw[dashed] (0,0) -- (0,-3); % düşey referans
\draw[thick] (0,0) -- (1.6,-2.55); % ip
% Açı
\draw (0,-0.9) arc (-90:-58:0.9); \node at (0.45,-1.25) {$\theta$};
% Kütle
\fill (1.6,-2.55) circle (0.18); \node at (2.0,-2.55) {$m$};
% Uzunluk
\node at (1.0,-1.2) {$L$};
% Ağırlık
\draw[->] (1.6,-2.55) -- (1.6,-3.5) node[right]{$mg$};
\end{tikzpicture}
\end{document}
```

> [!note]- Semboller
> - $\theta$: düşeyle yapılan açı (rad); $L$: ip uzunluğu (m); $m$: kütle (kg); $g$: yerçekimi ivmesi ($\text{m/s}^2$)
> - Yay konumu $s=L\theta$, hız $v=L\dot\theta$; küçük açı yaklaşımı: $\sin\theta\approx\theta$
> - $\omega_n$: doğal açısal frekans (rad/s); kütleden **bağımsız**

**Çözüm:**

**(a) Newton (teğet yön):** Geri çağırıcı kuvvet $-mg\sin\theta$, ivme $L\ddot\theta$:
$$m(L\ddot\theta)=-mg\sin\theta \;\Rightarrow\; \ddot\theta+\frac{g}{L}\sin\theta=0$$

**(b) Enerji:** $E=KE+PE=\tfrac12 m(L\dot\theta)^2+mgL(1-\cos\theta)$. $\dfrac{dE}{dt}=0$:
$$mL^2\dot\theta\ddot\theta+mgL\sin\theta\,\dot\theta=0 \;\Rightarrow\; \ddot\theta+\frac{g}{L}\sin\theta=0$$

**(c) Lagrange:** $\mathcal L=KE-PE$; $\dfrac{d}{dt}\dfrac{\partial\mathcal L}{\partial\dot\theta}-\dfrac{\partial\mathcal L}{\partial\theta}=0$:
$$mL^2\ddot\theta+mgL\sin\theta=0 \;\Rightarrow\; \ddot\theta+\frac{g}{L}\sin\theta=0$$

**(d) Açısal momentum:** $I_o\ddot\theta=-mgL\sin\theta$, $\;I_o=mL^2$ → aynı sonuç.

**Küçük açı** ($\sin\theta\approx\theta$): $\;\ddot\theta+\dfrac{g}{L}\theta=0$
$$\boxed{\omega_n=\sqrt{\frac{g}{L}}=\sqrt{\frac{9{,}81}{1}}\approx 3{,}13\ \text{rad/s}}$$
(Dört yöntem de aynı denkleme çıkar; $\omega_n$ kütleden bağımsızdır.)

---

# D. Dişli Sistemler

## Örnek D1 — Dişli Kutusu ile Transfer Fonksiyonu

**Soru:** Motor tarafına $T(t)$ uygulanıyor; $N_1$ dişlisi yükteki $N_2$ dişlisini sürüyor. Yük tarafında eylemsizlik $J_L$ ve sönüm $b_L$ var. Motor tarafına indirgenmiş modeli ve $\dfrac{\theta_1(s)}{T(s)}$'yi yazın.

> [!note]- Semboller
> - $N_1,N_2$: diş sayıları; $\theta_1,\theta_2$: motor/yük açıları
> - **İdeal dişli bağıntıları:** $\dfrac{\theta_2}{\theta_1}=\dfrac{N_1}{N_2}$ ve $\dfrac{T_2}{T_1}=\dfrac{N_2}{N_1}$ (güç korunur, $T_1\theta_1=T_2\theta_2$)
> - İndirgeme: bir elemanı diğer mile taşırken $(N/N)^2$ ile çarpılır

**Çözüm:** Yük tarafındaki eylemsizlik ve sönümü **motor miline indir** (her biri $(N_1/N_2)^2$ ile ölçeklenir):
$$J_{eq}=J_1+J_L\!\left(\frac{N_1}{N_2}\right)^2,\qquad b_{eq}=b_1+b_L\!\left(\frac{N_1}{N_2}\right)^2$$
İndirgenmiş tek-mil denklemi:
$$T(t)=J_{eq}\ddot\theta_1+b_{eq}\dot\theta_1 \;\Rightarrow\; T(s)=\theta_1(J_{eq}s^2+b_{eq}s)$$
$$\boxed{\dfrac{\theta_1(s)}{T(s)}=\dfrac{1}{J_{eq}s^2+b_{eq}s}=\dfrac{1}{s\big(J_{eq}s+b_{eq}\big)}}$$
Yük açısı istenirse: $\theta_2=\dfrac{N_1}{N_2}\theta_1$ ile ölçekle. **Püf:** indirgemeyi yaptıktan sonra problem tek eylemsizlik–sönüm sistemine iner.

---

# E. DC Motor (Elektromekanik Sistemler)

## Örnek E1 — Armatür Kontrollü DC Motor: $\theta_m/E_a$ Türetimi

**Soru:** Armatür kontrollü DC motorun $\dfrac{\theta_m(s)}{E_a(s)}$ transfer fonksiyonunu adım adım türetin.

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
% Armatür devresi
\draw (0,0) to[V=$e_a$] (0,2.5);
\draw (0,2.5) to[R=$R_a$] (2,2.5) to[L=$L_a$] (4,2.5);
\draw (4,2.5) to[V<=$v_b$] (4,0); % back-emf
\draw (0,0) -- (4,0);
% Motor + yük
\draw (4,1.25) -- (5,1.25);
\node[draw, circle, minimum size=1cm] (M) at (5.7,1.25) {$M$};
\draw (M.east) -- (7,1.25);
\node[right] at (7,1.25) {$J_m,\,D_m,\,\theta_m$};
\node at (2,1.5) {$i_a \rightarrow$};
\end{circuitikz}
\end{document}
```

> [!note]- Semboller
> - $e_a$: armatür gerilimi (V, giriş); $i_a$: armatür akımı (A); $R_a,L_a$: armatür direnci/endüktansı
> - $v_b$: zıt emk (V); $\theta_m$: motor mil açısı (rad); $T_m$: motor torku (N·m)
> - $K_b$: zıt emk sabiti (V·s/rad); $K_t$: tork sabiti (N·m/A); $J_m,D_m$: motor eylemsizliği/sönümü

**Çözüm (6 adım):**

1. **Zıt emk:** $v_b=K_b\dfrac{d\theta_m}{dt}\Rightarrow V_b(s)=K_b s\,\theta_m(s)$
2. **Armatür KVL:** $e_a=R_a i_a+L_a\dfrac{di_a}{dt}+v_b\Rightarrow E_a(s)=(R_a+L_a s)I_a(s)+V_b(s)$
3. **Tork:** $T_m=K_t i_a\Rightarrow I_a(s)=\dfrac{T_m(s)}{K_t}$
4. **Mekanik:** $T_m=J_m\ddot\theta_m+D_m\dot\theta_m\Rightarrow T_m(s)=\theta_m(s)(J_m s^2+D_m s)$
5. **Yerine koy** (3→2, sonra 4):
$$E_a=(R_a+L_a s)\frac{\theta_m(J_m s^2+D_m s)}{K_t}+K_b s\,\theta_m$$
6. **Düzenle:**
$$\boxed{\dfrac{\theta_m(s)}{E_a(s)}=\dfrac{K_t}{(R_a+L_a s)(J_m s^2+D_m s)+K_t K_b s}}$$
$L_a\approx0$ (yaygın kabul) ile sadeleşir:
$$\dfrac{\theta_m(s)}{E_a(s)}=\dfrac{K_t/R_a}{s\Big(J_m s+D_m+\dfrac{K_t K_b}{R_a}\Big)}$$

## Örnek E2 — DC Motor Sayısal + Dişli İndirgeme

**Soru:** Bir DC motora $e_a=12\,\text{V}$ uygulanınca: $\omega=600\,\text{rad/s}$'de $T=55\,\text{N·m}$, durma anında ($\omega=0$) $T_{durma}=100\,\text{N·m}$ üretiyor. Motor eylemsizliği $J_m$, yük eylemsizliği $J_L$, dişli oranı $N_1/N_2=1/6$. Motor sabitlerini bulup $\theta_m/E_a$'yı yazın.

> [!note]- Semboller
> - Tork–hız doğrusu: $T_m=T_{durma}-\dfrac{T_{durma}}{\omega_{boş}}\omega$ (lineer)
> - $T_{durma}$: durma (stall) torku ($\omega=0$); $\omega_{boş}$: boştaki hız ($T=0$)
> - Durmada: $T_{durma}=\dfrac{K_t}{R_a}e_a$; boşta: $e_a=K_b\,\omega_{boş}$

**Çözüm:**

**Boştaki hızı bul** — iki nokta $(600,\,55)$ ve $(0,\,100)$ doğrusal:
$$\text{eğim}=\frac{55-100}{600-0}=-0{,}075,\quad T=0\Rightarrow \omega_{boş}=\frac{100}{0{,}075}\approx1333\,\text{rad/s}$$

**Motor sabitleri:**
$$\frac{K_t}{R_a}=\frac{T_{durma}}{e_a}=\frac{100}{12}\approx8{,}33,\qquad K_b=\frac{e_a}{\omega_{boş}}=\frac{12}{1333}\approx0{,}009$$

**Dişli indirgeme** (yük → motor mili, $(N_1/N_2)^2=1/36$):
$$J_{eq}=J_m+J_L\!\left(\frac{N_1}{N_2}\right)^2=J_m+\frac{J_L}{36}$$

**Transfer fonksiyonu** (E1'deki formda, $D_m\to D_{eq}$):
$$\dfrac{\theta_m(s)}{E_a(s)}=\dfrac{K_t/R_a}{s\Big(J_{eq}s+D_{eq}+\dfrac{K_tK_b}{R_a}\Big)}=\dfrac{8{,}33}{s\big(J_{eq}s+D_{eq}+0{,}075\big)}$$
Yük açısı: $\theta_L=\dfrac{N_1}{N_2}\theta_m=\dfrac16\theta_m$. **Püf:** durma torku ve boş hız → iki denklemle $K_t/R_a$ ve $K_b$ doğrudan çıkar.

---

# F. OPAMP Devreleri

> [!formul] İdeal OPAMP Kuralları
> 1. Giriş uçlarına akım girmez: $i_+ = i_- = 0$
> 2. **Sanal kısa devre:** $v_+ = v_-$ (geri besleme varken)

## Örnek F1 — Eviren ve Evirmeyen Yükselteç

**Soru:** Eviren ve evirmeyen yükselteç konfigürasyonları için $E_o/E_i$ kazançlarını çıkarın.

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\node[op amp] (OA) at (0,0) {};
\draw (OA.-) -- ++(-0.7,0) coordinate(n);
\draw (n) to[R=$Z_1$] ++(-2,0) node[left]{$e_i$};
\draw (n) -- ++(0,1.3) coordinate(a) to[R=$Z_2$] (a-|OA.out) -- (OA.out);
\draw (OA.+) -- ++(-0.7,0) node[ground]{};
\draw (OA.out) -- ++(0.6,0) node[right]{$e_o$};
\end{circuitikz}
\end{document}
```
*(Eviren yükselteç: giriş $Z_1$ üzerinden eviren uca, geri besleme $Z_2$.)*

> [!note]- Semboller
> - $Z_1$: giriş empedansı; $Z_2$: geri besleme empedansı; $e_i,e_o$: giriş/çıkış gerilimleri
> - Eviren uçta **sanal toprak** ($v_-=v_+=0$) → düğüm denklemi tek satırda çıkar

**Çözüm:**

**Eviren yükselteç** — sanal toprak ($v_-=0$), giriş akımı = geri besleme akımı:
$$\frac{e_i-0}{Z_1}=\frac{0-e_o}{Z_2}\;\Rightarrow\;\boxed{\frac{E_o}{E_i}=-\frac{Z_2}{Z_1}}$$

**Evirmeyen yükselteç** — $v_-=v_+=e_i$, gerilim bölücü:
$$e_i=e_o\frac{Z_1}{Z_1+Z_2}\;\Rightarrow\;\boxed{\frac{E_o}{E_i}=\frac{Z_1+Z_2}{Z_1}=1+\frac{Z_2}{Z_1}}$$

## Örnek F2 — RC Geri Beslemeli Eviren OPAMP (Transfer Fonksiyonu)

**Soru:** Eviren yükselteçte giriş $Z_1=R_1$, geri besleme $Z_2=R_2\,\Vert\,\dfrac{1}{C s}$ (paralel direnç+kapasitör). $\dfrac{E_o(s)}{E_i(s)}$'yi bulun.

> [!note]- Semboller
> - $R_2\,\Vert\,\dfrac{1}{Cs}=\dfrac{R_2\cdot\frac{1}{Cs}}{R_2+\frac{1}{Cs}}=\dfrac{R_2}{R_2 C s+1}$ (paralel empedans)
> - Bu devre **birinci derece alçak geçiren** yükselteçtir (kesim $\omega=1/R_2C$)

**Çözüm:** Eviren kazanç $-Z_2/Z_1$:
$$\frac{E_o}{E_i}=-\frac{Z_2}{Z_1}=-\frac{1}{R_1}\cdot\frac{R_2}{R_2 C s+1}$$
$$\boxed{\frac{E_o(s)}{E_i(s)}=-\frac{R_2}{R_1(R_2 C s+1)}}$$
DC kazancı $-R_2/R_1$, yüksek frekansta kapasitör kısa devre olur → kazanç düşer.

---

# G. Elektriksel Sistemler (Devre Modelleme)

## Örnek G1 — Seri RLC: $V_C/V_i$

**Soru:** Seri $R$–$L$–$C$ devresinde çıkış kapasitör gerilimi $v_C$ ise $\dfrac{V_C(s)}{V_i(s)}$ transfer fonksiyonunu bulun.

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$v_i$] (0,2.5);
\draw (0,2.5) to[L=$L$] (2,2.5) to[R=$R$] (4,2.5) -- (5,2.5);
\draw (5,2.5) to[C=$C$, v=$v_C$] (5,0);
\draw (0,0) -- (5,0);
\end{circuitikz}
\end{document}
```

> [!note]- Semboller
> - $i$: göz akımı (A); $v_C$: kapasitör gerilimi (çıkış, V)
> - Empedanslar: $Z_L=Ls$, $Z_R=R$, $Z_C=\dfrac{1}{Cs}$; seri → gerilim bölücü

**Çözüm:** Gerilim bölücü ($v_C$, toplam empedansa oranla):
$$\frac{V_C}{V_i}=\frac{\frac{1}{Cs}}{Ls+R+\frac{1}{Cs}}=\frac{1}{LCs^2+RCs+1}$$
$$\boxed{\frac{V_C(s)}{V_i(s)}=\frac{1/LC}{s^2+\frac{R}{L}s+\frac{1}{LC}}}$$

## Örnek G2 — Üç Gözlü Devre (Cramer)

**Soru:** Üç bağımsız gözlü ($i_1,i_2,i_3$) bir devrede $R,L,C$ elemanlarıyla, istenen akım/gerilimi **Cramer** ile çekmek için kurulumu yazın.

> [!note]- Semboller
> - Her göz için bir KVL → $3\times3$ empedans matrisi $\mathbf{Z}\,\mathbf{I}=\mathbf{V}$
> - Köşegen: gözün **öz-empedansı** (tüm elemanların toplamı); köşegen dışı: **ortak** eleman (işaret $-$)
> - $I_k=\dfrac{\det(\mathbf Z_k)}{\det(\mathbf Z)}$, $\mathbf Z_k$ = $k$. sütunu $\mathbf V$ ile değiştirilmiş matris

**Çözüm (yöntem):** Genel form:
$$\begin{bmatrix}Z_{11}&-Z_{12}&-Z_{13}\\-Z_{21}&Z_{22}&-Z_{23}\\-Z_{31}&-Z_{32}&Z_{33}\end{bmatrix}\begin{bmatrix}I_1\\I_2\\I_3\end{bmatrix}=\begin{bmatrix}V_1\\0\\0\end{bmatrix}$$
- $Z_{kk}$ = $k$. gözdeki tüm empedansların toplamı
- $Z_{jk}$ = $j$ ve $k$ gözlerinin **ortak** kolundaki empedans
- Aranan akım: $I_k=\dfrac{\Delta_k}{\Delta}$; gerilim gerekiyorsa eleman empedansıyla çarp (örn. $V_L=Ls\cdot I_k$)

**Püf:** Tüm $\frac{1}{s}$ paydalarını ortadan kaldırmak için satırları uygun $s$ kuvvetiyle çarp; böylece $\Delta$ temiz bir polinom olur (bkz. Quiz 3).

---

> [!sinav] Vize Gecesi — Hızlı Kontrol Listesi
> - **Mekanik/dönel:** her kütle/düğüm için denge denklemi → arada eleman = fark terimi → Cramer
> - **Elektrik:** durumlar $v_C,\,i_L$; çevre yöntemi için empedans $Ls,\,R,\,\frac1{Cs}$
> - **Durum-uzayı:** enerji elemanı sayısı = durum sayısı; $G(s)=C(sI-A)^{-1}B+D$
> - **DC motor:** durma torku → $K_t/R_a$; boş hız → $K_b$; dişli → $(N_1/N_2)^2$ indirgeme
> - **OPAMP:** eviren $-Z_2/Z_1$, evirmeyen $1+Z_2/Z_1$, sanal kısa devre
> - **Ters Laplace:** kökler reel-ayrık → $\cosh/\sinh$; karmaşık → $\cos/\sin$; tamkareye tamamla
