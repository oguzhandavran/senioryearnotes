---
tags: [otomatik-kontrol, blok-diyagram, mason, transfer-fonksiyonu, örnek-sorular]
---

# 01 — Blok Diyagram Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Giriş Kapalı Çevrim ve Blok Diyagramları]]

---

## Ödev-1 — Çok Çevrimli Blok Diyagram (Y/U = ?)

> [!note]- Semboller
> - $G_1\dots G_6$: ileri yol/blok transfer fonksiyonları; $\Sigma$: toplama düğümü
> - İç çevrim: $G_3,G_4$ ile negatif geri besleme; dış çevrim: $G_5$ ile
> - Negatif geri besleme indirgeme: $\dfrac{G}{1+GH}$ (kapalı çevrim)
> - $A(s)$: indirgenmiş iç çevrim; $Y/U$: tüm sistemin transfer fonksiyonu

**Verilen:**
$$G_1=\frac{1}{s+1},\quad G_2=\frac{s+0.2}{s},\quad G_3=\frac{5}{s+2},\quad G_4=2,\quad G_5=\frac{10}{s+10},\quad G_6=3$$

**Topoloji:** $U \to G_1 \to \Sigma_1 \to G_2 \to \Sigma_2 \to G_3 \to G_6 \to Y$
- İç geri besleme: $G_3$ çıkışı $\to G_4 \to \Sigma_2$ (negatif)
- Dış geri besleme: $Y \to G_5 \to \Sigma_1$ (negatif)

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc}
\begin{document}
\begin{tikzpicture}[
  font=\scriptsize, >={Stealth[length=1.8mm]},
  block/.style={draw, thick, fill=blue!5, minimum height=7mm, inner sep=2.5pt},
  fb/.style={draw, thick, fill=blue!12, minimum height=6mm, inner sep=2.5pt},
  sum/.style={draw, thick, circle, minimum size=5mm, inner sep=0pt},
  link/.style={->, thick}, node distance=4.5mm and 5.5mm
]
\node (u) {$U$};
\node[block, right=of u] (g1) {$G_1=1/(s{+}1)$};
\node[sum, right=of g1] (s1) {};
\node[block, right=of s1] (g2) {$G_2=(s{+}0.2)/s$};
\node[sum, right=of g2] (s2) {};
\node[block, right=of s2] (g3) {$G_3=5/(s{+}2)$};
\node[block, right=7mm of g3] (g6) {$G_6=3$};
\node[right=6mm of g6] (y) {$Y$};
\foreach \s in {s1,s2}{
  \node[font=\tiny] at ([xshift=-1mm,yshift=1.4mm]\s.center){$+$};
  \node[font=\tiny] at ([xshift=-1mm,yshift=-1.4mm]\s.center){$-$};
}
\draw[link](u)--(g1); \draw[link](g1)--(s1); \draw[link](s1)--(g2);
\draw[link](g2)--(s2); \draw[link](s2)--(g3);
\coordinate (b1) at ($(g3.east)!0.5!(g6.west)$);
\draw[link](g3)--(g6); \fill(b1)circle(1.1pt);
\coordinate (b2) at ($(g6.east)!0.5!(y)$);
\draw[link](g6)--(y); \fill(b2)circle(1.1pt);
\node[fb, below=8mm of g3] (g4) {$G_4=2$};
\draw[link](b1)|-(g4.east);
\draw[link](g4.west)-|(s2);
\node[fb, below=17mm of g2] (g5) {$G_5=10/(s{+}10)$};
\draw[link](b2)|-(g5.east);
\draw[link](g5.west)-|(s1);
\end{tikzpicture}
\end{document}
```

**Çözüm (iç çevrimden dışa):**

**Adım 1 — İç çevrim** ($\Sigma_2, G_3, G_4$):

$$A(s) = \frac{G_3}{1+G_3 G_4} = \frac{\frac{5}{s+2}}{1+\frac{10}{s+2}} = \frac{5}{s+12}$$

**Adım 2 — Dış çevrim** ($\Sigma_1, G_2, A, G_6, G_5$):

$$\frac{Y}{U} = \frac{G_1 \cdot G_2 \cdot A(s) \cdot G_6}{1 + G_2 \cdot A(s) \cdot G_6 \cdot G_5}$$

Pay: $N=G_1 G_2 A G_6 = \dfrac{1}{s+1}\cdot\dfrac{s+0.2}{s}\cdot\dfrac{5}{s+12}\cdot 3 = \dfrac{15(s+0.2)}{s(s+1)(s+12)}$

Çevrim terimi: $G_2 A G_6 G_5 = \dfrac{s+0.2}{s}\cdot\dfrac{5}{s+12}\cdot 3\cdot\dfrac{10}{s+10} = \dfrac{150(s+0.2)}{s(s+12)(s+10)}$

**Adım 3 — Birleştir.** $\dfrac{Y}{U}=\dfrac{N}{1+G_2AG_6G_5}$; pay-paydayı $s(s+1)(s+12)(s+10)$ ile çarpıp sadeleştir:

$$\frac{Y}{U}=\frac{15(s+0.2)(s+10)}{(s+1)\big[s(s+12)(s+10)+150(s+0.2)\big]}$$

Paydayı aç ($s(s+12)(s+10)=s^3+22s^2+120s$; $+150s+30$):

$$\boxed{\frac{Y}{U} = \frac{15(s+0.2)(s+10)}{(s+1)(s^3+22s^2+270s+30)} = \frac{15s^2+153s+30}{s^4+23s^3+292s^2+300s+30}}$$

> [!sinav] Hızlı Yaklaşım
> İç çevrim sadeleştir → dış çevrim uygula. Negatif geri besleme her zaman: $\frac{G}{1+GH}$

---

## Ödev-2 — İkili Negatif Geri Besleme (Y/U = ?)

> [!note]- Semboller
> - $G_1,G_2,G_4$: ileri bloklar; $G_3=1$: iç geri besleme; $G_5$: dış geri besleme
> - $B(s)$: indirgenmiş iç çevrim ($G_2$ ile $G_3$); $\Sigma$: toplama düğümü
> - Negatif geri besleme: $\dfrac{G}{1+GH}$; $Y/U$: sistemin transfer fonksiyonu

**Verilen:**
$$G_1=\frac{s+1}{s},\quad G_2=\frac{s+2}{s+1},\quad G_3=1,\quad G_4=\frac{1}{s^2+s+1},\quad G_5=\frac{10}{s+10}$$

**Topoloji:** $U \to \Sigma_1 \to G_1 \to \Sigma_2 \to G_2 \to \Sigma_3 \to G_4 \to Y$
- 1. iç geri besleme: $G_2$ çıkışı $\to G_3=1 \to \Sigma_2$ (negatif)
- Dış geri besleme: $Y \to G_5 \to \Sigma_1$ (negatif)

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc}
\begin{document}
\begin{tikzpicture}[
  font=\scriptsize, >={Stealth[length=1.8mm]},
  block/.style={draw, thick, fill=blue!5, minimum height=7mm, inner sep=2.5pt},
  fb/.style={draw, thick, fill=blue!12, minimum height=6mm, inner sep=2.5pt},
  sum/.style={draw, thick, circle, minimum size=5mm, inner sep=0pt},
  link/.style={->, thick}, node distance=4.5mm and 5.5mm
]
\node (u) {$U$};
\node[sum, right=of u] (s1) {};
\node[block, right=of s1] (g1) {$G_1=(s{+}1)/s$};
\node[sum, right=of g1] (s2) {};
\node[block, right=of s2] (g2) {$G_2=(s{+}2)/(s{+}1)$};
\node[sum, right=of g2] (s3) {};
\node[block, right=of s3] (g4) {$G_4=1/(s^2{+}s{+}1)$};
\node[right=6mm of g4] (y) {$Y$};
\foreach \s in {s1,s2,s3}{
  \node[font=\tiny] at ([xshift=-1mm,yshift=1.4mm]\s.center){$+$};
  \node[font=\tiny] at ([xshift=-1mm,yshift=-1.4mm]\s.center){$-$};
}
\draw[link](u)--(s1); \draw[link](s1)--(g1); \draw[link](g1)--(s2);
\draw[link](s2)--(g2);
\coordinate (b1) at ($(g2.east)!0.5!(s3.west)$);
\draw[link](g2)--(s3); \fill(b1)circle(1.1pt);
\draw[link](s3)--(g4);
\coordinate (b2) at ($(g4.east)!0.5!(y)$);
\draw[link](g4)--(y); \fill(b2)circle(1.1pt);
\node[fb, below=8mm of g2] (g3) {$G_3=1$};
\draw[link](b1)|-(g3.east);
\draw[link](g3.west)-|(s2);
\node[fb, below=17mm of g2] (g5) {$G_5=10/(s{+}10)$};
\draw[link](b2)|-(g5.east);
\draw[link](g5.west)-|(s1);
\end{tikzpicture}
\end{document}
```

**Adım 1 — İç çevrim** ($\Sigma_2, G_2, G_3=1$):

$$B(s) = \frac{G_2}{1+G_2 G_3} = \frac{G_2}{1+G_2} = \frac{\frac{s+2}{s+1}}{1+\frac{s+2}{s+1}} = \frac{s+2}{s+1+s+2} = \frac{s+2}{2s+3}$$

**Adım 2 — Dış çevrim:**

$$\frac{Y}{U} = \frac{G_1 \cdot B(s) \cdot G_4}{1 + G_1 \cdot B(s) \cdot G_4 \cdot G_5}$$

Pay: $N=G_1 B G_4 = \dfrac{s+1}{s}\cdot\dfrac{s+2}{2s+3}\cdot\dfrac{1}{s^2+s+1} = \dfrac{(s+1)(s+2)}{s(2s+3)(s^2+s+1)}$

**Adım 3 — Birleştir.** $\dfrac{Y}{U}=\dfrac{N}{1+N G_5}$; pay-paydayı $s(2s+3)(s^2+s+1)(s+10)$ ile çarp:

$$\boxed{\frac{Y}{U} = \frac{(s+1)(s+2)(s+10)}{s(2s+3)(s^2+s+1)(s+10) + 10(s+1)(s+2)}}$$

*(Payda 5. dereceden: $s(2s+3)(s^2+s+1)(s+10)$ açılırsa $2s^5+25s^4+\ldots$; $+10(s+1)(s+2)$ sabit/düşük dereceli terimlere eklenir.)*

---

### Mason Formülü Örneği

> [!note]- Semboller
> - $P_k$: $k$. ileri yol kazancı; $L_i$: $i$. döngü kazancı (negatif geri beslemede işaret $-$)
> - $\Delta=1-\sum L_i+\sum(\text{değmeyen ikili})-\dots$: sistem determinantı
> - $\Delta_k$: $P_k$ yolunu silince kalan determinant (yolla değmeyen döngüler)
> - Mason: $T=\dfrac{1}{\Delta}\sum_k P_k\Delta_k$

Sistem: $G_1 \to G_2 \to G_3$, geri besleme $H_1$ (iç), $H_2$ (dış)

**İleri yollar:** $P_1 = G_1 G_2 G_3$

**Döngüler:** $L_1 = -G_2 H_1$, $L_2 = -G_1 G_2 G_3 H_2$

**Determinant:** $\Delta = 1 - (L_1 + L_2) = 1 + G_2 H_1 + G_1 G_2 G_3 H_2$

**$\Delta_1$:** $P_1$ ile temas eden döngü yok → $\Delta_1 = 1$

$$\boxed{T = \frac{G_1 G_2 G_3}{1 + G_2 H_1 + G_1 G_2 G_3 H_2}}$$

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Giriş Kapalı Çevrim ve Blok Diyagramları]]
