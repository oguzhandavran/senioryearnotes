---
tags: [mst, elektrik, rlc, kvl, kcl, transfer-fonksiyonu, op-amp, örnek-sorular]
---

# 02 — Elektrik Sistemleri Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/02 Elektrik Sistemleri|02 Elektrik Sistemleri]]

---

## Çözümlü Örnek 1: R₁-L-R₂-C Mesh Devresi (Ders Notları)

> [!example] Problem
> **Devre:** İki ilmekli (mesh) devre. Sol ilmekte $R_1$ ve $L$, sağ ilmekte $R_2$ ve $C$; $L$ iki ilmeğin **ortak** elemanı. Giriş $V_{in}$, çıkış $V_C$ (kondansatör gerilimi).
>
> **İstenen:** (a) Sembolik $\dfrac{V_C(s)}{V_{in}(s)}$; (b) $R_1=L=R_2=C=1$ için sayısal sonuç.

> [!note]- Semboller
> - $V_{in}$: kaynak gerilimi — giriş (V); $V_C$: kondansatör gerilimi — çıkış (V)
> - $R_1,R_2$: dirençler (Ω); $L$: indüktans (H); $C$: kapasitans (F)
> - $i_1,i_2$ (büyük harf $I_1,I_2$): ilmek akımları, zaman/Laplace (A)
> - $Ls$: indüktör empedansı; $\dfrac{1}{Cs}$: kondansatör empedansı (Ω)
> - $\Delta$: katsayı matrisinin determinantı; $\Delta_2$: Cramer'da $I_2$ için pay determinantı
> - $s$: Laplace değişkeni (1/s)

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$V_{in}$, invert] (0,3);
\draw (0,3) to[R=$R_1$, i>^=$i_1$] (3,3) coordinate(a)
            to[R=$R_2$, i>^=$i_2$] (6,3) coordinate(b);
\draw (a) to[L=$L$] (3,0);
\draw (b) to[C=$C$, v=$V_C$] (6,0);
\draw (0,0) -- (6,0);
\draw (3,0) node[ground]{};
\node at (1.5,1.5) {\footnotesize Mesh 1};
\node at (4.5,1.5) {\footnotesize Mesh 2};
\end{circuitikz}
\end{document}
```

**Adım 1 — KVL ile ilmek denklemleri** (empedans formunda, $L\to Ls$, $C\to 1/Cs$):

**Mesh 1** ($i_1$): $R_1 I_1 + L s (I_1 - I_2) = V_{in} \Rightarrow (R_1+Ls)I_1 - Ls\,I_2 = V_{in}$

**Mesh 2** ($i_2$): $Ls(I_2 - I_1) + R_2 I_2 + \dfrac{1}{Cs}I_2 = 0 \Rightarrow -Ls\,I_1 + \left(Ls+R_2+\dfrac{1}{Cs}\right)I_2 = 0$

**Adım 2 — Matris biçimi:**

$$\begin{bmatrix} R_1 + Ls & -Ls \\ -Ls & Ls + R_2 + 1/(Cs) \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} V_{in} \\ 0 \end{bmatrix}$$

**Adım 3 — Cramer ile $I_2$.** $\Delta_2$ = 2. sütunu $\begin{bmatrix}V_{in}\\0\end{bmatrix}$ ile değiştir:

$$\Delta_2 = \begin{vmatrix} R_1+Ls & V_{in} \\ -Ls & 0 \end{vmatrix} = Ls\,V_{in}, \qquad I_2 = \frac{\Delta_2}{\Delta} = \frac{Ls\,V_{in}}{\Delta}$$

**Adım 4 — Determinant.** $\Delta=(R_1+Ls)\!\left(Ls+R_2+\tfrac{1}{Cs}\right)-(Ls)^2$; $\;L^2s^2$ terimleri sadeleşir:

$$\Delta = L(R_1+R_2)s + \left(R_1R_2+\tfrac{L}{C}\right) + \frac{R_1}{Cs}$$

**Adım 5 — Çıkış gerilimi.** $V_C=\dfrac{I_2}{Cs}=\dfrac{Ls\,V_{in}}{Cs\,\Delta}=\dfrac{L\,V_{in}}{C\,\Delta}$. Pay-paydayı $Cs$ ile çarpıp düzenle:

$$\boxed{\frac{V_C(s)}{V_{in}(s)} = \frac{Ls}{(R_1+R_2)LC\,s^2 + (R_1R_2C+L)\,s + R_1}}$$

**Adım 6 — Sayısal ($R_1=L=R_2=C=1$):** $(R_1+R_2)LC=2$, $R_1R_2C+L=2$, $R_1=1$, pay $Ls=s$:

$$\boxed{\frac{V_C(s)}{V_{in}(s)} = \frac{s}{2s^2 + 2s + 1}}$$

> **Bant geçiren:** $s\to0$'da $V_C\to0$ (C açık devre), $s\to\infty$'da $V_C\to0$ (L açık devre); arada tepe verir.

---

## Elektrik Örnek 2 — Ters Çevirici Op-Amp (R₁,C₁ giriş; R₂,C₂ geri besleme)

> [!example] Problem
> **Devre:** Ters çevirici (inverting) op-amp. Giriş kolunda $R_1$ ile $C_1$ **seri** ($Z_1$); geri beslemede $R_2$ ile $C_2$ **paralel** ($Z_2$). Giriş $V_i$, çıkış $V_o$.
>
> **İstenen:** (a) $\dfrac{V_o(s)}{V_i(s)}$; (b) $C_1=C_2=1$ F, $R_1=2\,\Omega$, $R_2=3\,\Omega$ ve $V_i=1$ V DC basamak için $V_o(t)$.

> [!note]- Semboller
> - $V_i,V_o$: giriş ve çıkış gerilimleri (V)
> - $R_1,R_2$: dirençler (Ω); $C_1,C_2$: kondansatörler (F)
> - $Z_1$: giriş empedansı ($R_1+1/C_1s$, seri); $Z_2$: geri besleme empedansı ($R_2\parallel C_2$)
> - Sanal toprak: ideal op-amp'ta $V_-=V_+=0$, bu yüzden giriş ve geri besleme akımları eşit
> - İnverting kazanç: $V_o/V_i=-Z_2/Z_1$ (eksi = faz çevirme)
> - $A,B$: kısmi kesir katsayıları; $s$: Laplace değişkeni (1/s)

**Adım 1 — Sanal toprak.** İdeal op-amp → $V_-=0$ ve $(-)$ girişe akım girmez, dolayısıyla giriş akımı = geri besleme akımı ($i_1=i_2$).

Giriş empedansı (seri $R_1+C_1$): $Z_1 = R_1 + \dfrac{1}{C_1s} = \dfrac{R_1C_1s+1}{C_1s}$

Geri besleme empedansı ($R_2 \parallel C_2$): $Z_2 = \dfrac{R_2\cdot\frac{1}{C_2s}}{R_2+\frac{1}{C_2s}} = \dfrac{R_2}{R_2C_2s+1}$

**Adım 2 — İnverting TF:** $\dfrac{V_o}{V_i} = -\dfrac{Z_2}{Z_1} = -\dfrac{R_2/(R_2C_2s+1)}{(R_1C_1s+1)/(C_1s)}$. Pay/payda sadeleşir:

$$\boxed{\frac{V_o(s)}{V_i(s)} = -\frac{R_2 C_1 s}{(R_1C_1s+1)(R_2C_2s+1)}}$$

**Adım 3 — Sayısal ($C_1=C_2=1$, $R_1=2$, $R_2=3$):**

$$\frac{V_o(s)}{V_i(s)} = -\frac{3s}{(2s+1)(3s+1)} = -\frac{3s}{6s^2+5s+1}$$

**Adım 4 — Basamak yanıtı.** $V_i(s)=1/s$ → $V_o(s)=-\dfrac{3s}{6s^2+5s+1}\cdot\dfrac1s=-\dfrac{3}{6s^2+5s+1}$. Paydayı çarpanlara ayır ($6s^2+5s+1=6(s+\tfrac12)(s+\tfrac13)$):

$$V_o(s) = -\frac{3}{6(s+\frac12)(s+\frac13)} = -\frac{1}{2(s+\frac12)(s+\frac13)} = \frac{A}{s+\frac12}+\frac{B}{s+\frac13}$$

Kısmi kesir: $A=\left.-\tfrac{1}{2(s+1/3)}\right|_{s=-1/2}=-\tfrac{1}{2(-1/6)}=3$, $\;B=\left.-\tfrac{1}{2(s+1/2)}\right|_{s=-1/3}=-\tfrac{1}{2(1/6)}=-3$.

$$\boxed{V_o(t) = 3e^{-t/2} - 3e^{-t/3}, \quad t\geq0}$$

*Kontrol: $V_o(0^+)=3-3=0$ ✓, $V_o(\infty)=0$ ✓ ($C_1$ DC'yi bloke eder, kalıcı çıkış sıfır).*

---

## Elektrik Örnek 3 — Ters Çevirmeyen Op-Amp (Non-Inverting)

> [!example] Problem
> **Devre:** Ters çevirmeyen (non-inverting) op-amp. Giriş $V_i$, $R_1$–$R_2$ gerilim bölücüsüyle $(+)$ girişe gelir. Geri beslemede $R_f$ (çıkıştan $(-)$'ye) ve $C_1$ ($(-)$'den toprağa). Çıkış $V_o$.
>
> **İstenen:** $\dfrac{V_o(s)}{V_i(s)}$ transfer fonksiyonu ve frekans davranışı.

> [!note]- Semboller
> - $V_i,V_o$: giriş/çıkış gerilimleri (V); $V_+,V_-$: op-amp girişleri (V)
> - $R_1,R_2$: $(+)$ girişteki bölücü dirençleri (Ω)
> - $R_f$: geri besleme direnci (Ω); $C_1$: geri besleme kondansatörü (F)
> - Non-inverting kazanç: $V_o=V_-\,(1+Z_f/Z_g)$ biçiminde, burada $(-)$ kolunda $R_f\parallel$... 
> - Sıfır: TF payını sıfırlayan $s$ değeri; bu devrede $s=-1/(R_fC_1)$
> - $s$: Laplace değişkeni (1/s)

**Adım 1 — $(+)$ giriş (gerilim bölücü):** $V_+ = V_i \cdot \dfrac{R_2}{R_1+R_2}$

**Adım 2 — $(−)$ düğümünde KCL** ($V_- = V_+$, $R_f$ ve $C_1$ bağlı):

$$\frac{V_- - V_o}{R_f} + V_- C_1 s = 0 \implies V_o = V_-(1+R_fC_1s)$$

**Adım 3 — Birleştir:**

$$\boxed{\frac{V_o(s)}{V_i(s)} = \frac{R_2}{R_1+R_2}\bigl(1+R_fC_1s\bigr)}$$

| Frekans | Davranış |
|---------|----------|
| DC ($s=0$) | $R_2/(R_1+R_2)$ — gerilim bölücü |
| Yüksek $f$ | Kazanç artar — PD etkisi |
| Sıfır | $s = -1/(R_fC_1)$ |
| Kutup | Yok — 1. dereceden |

---

## Elektrik Örnek 4 — Elektromekanik Sistem (RL + Kütle-Yay-Sönümleyici)

> [!example] Problem
> **Sistem:** Bir $RL$ bobininden geçen akım $i$, $F_m=K_m i$ manyetik kuvveti üretir. Bu kuvvet bir kütle–yay–sönümleyici sistemini ($m,k,b$) sürer. Giriş gerilimi $u(t)$, çıkış konum $x$.
>
> **İstenen:** $\dfrac{X(s)}{U(s)}$ transfer fonksiyonu ve kutup yapısı.

> [!note]- Semboller
> - $u(t)$: kaynak gerilimi — giriş (V); $U(s)$: Laplace dönüşümü
> - $R$: bobin direnci (Ω); $L$: indüktans (H); $i$: akım (A)
> - $K_m$: kuvvet sabiti — akımı kuvvete çevirir (N/A)
> - $F_m=K_m i$: manyetik kuvvet (N)
> - $m,k,b$: kütle (kg), yay sabiti (N/m), sönüm (N·s/m)
> - $x,\dot x,\ddot x$: konum, hız, ivme; $X(s)$: Laplace dönüşümü
> - $s_1=-R/L$: elektriksel kutup; $\zeta,\omega_n,\omega_d$: mekanik kutupların sönüm oranı, doğal ve sönümlü frekansı

**Adım 1 — Elektrik devresi (KVL):** Bobin için gerilim dengesi:
$$u(t) = Ri + L\frac{di}{dt} \implies U(s) = (R+Ls)I(s)$$

**Mekanik denklem:**
$$m\ddot{x} + b\dot{x} + kx = F_m = K_m i \implies (ms^2+bs+k)X(s) = K_m I(s)$$

**Birleştir:** $I(s) = \dfrac{U(s)}{R+Ls}$

$$\boxed{\frac{X(s)}{U(s)} = \frac{K_m}{(R+Ls)(ms^2+bs+k)}}$$

Bu **3. dereceden** bir sistemdir (indüktör + 2. dereceli mekanik). Kutuplar:
- $s_1 = -R/L$ (elektriksel mod)
- $s_{2,3} = -\zeta\omega_n \pm j\omega_d$ (mekanik modlar)

> [!sinav] Elektromekanik Sistemler
> DC motorda geri-EMF ($K_b\dot{\theta}$) olmadan model bu formdu. Geri-EMF eklenince $K_bK_t/(R_a J_m)$ terimi payda'ya eklenir.
