---
tags: [mst, mekanik, newton, lagrange, transfer-fonksiyonu, dc-motor, disli, örnek-sorular]
---

# 01 — Mekanik Sistemler Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Mekanik Sistemler|01 Mekanik Sistemler]]

---

## DC Motor + Dişli Sistemi Tam Örneği

> [!example] Tam Çözümlü Örnek (Arş. Gör. Asım UCAR)
> **Veri:**
> - 12 V DC motor; $T_{stall}=100$ Nm, $\omega_{no-load}=1333.3$ rad/s
> - $J_a=7$ kg·m², $D_a=3$ Nm·s/rad, Load: $J_L=105$ kg·m²
> - Dişli: $N_1=12,\ N_2=25$ (1. kademe), $N_3=25,\ N_4=92$ (2. kademe)
>
> **Adım 1 — Dişli Oranı:**
> $$n = \frac{N_1 N_3}{N_2 N_4} = \frac{12 \times 25}{25 \times 92} = \frac{1}{36}$$
>
> **Adım 2 — Yansıtılmış atalet:**
> $$J_m = J_a + J_L\!\left(\frac{1}{36}\right)^{\!2} = 7 + 105 \cdot \frac{1}{1296} \approx 9.917\ \text{kg·m}^2$$
>
> **Adım 3 — Motor parametreleri:**
> $$\frac{K_t}{R_a} = \frac{T_{stall}}{E_a} = \frac{100}{12} = 8.33, \qquad K_b = \frac{E_a}{\omega_{no-load}} = \frac{12}{1333.3} \approx 0.009$$
>
> **Adım 4 — Transfer fonksiyonu:**
> $$\frac{\Theta_m(s)}{E_a(s)} = \frac{0.839}{s\bigl(s + 0.309\bigr)}$$

---

## Mekanik Örnek 1 — Newton ve Lagrange Karşılaştırması

*Sistem: Kütle $m$, yay $k$ (sol), sönümleyici $b$ (sağ) paralel, $F$ aşağı uygulanıyor.*

<svg width="220" height="290" viewBox="0 0 220 290" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mk1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
    <marker id="arrf-mk1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#c0392b"/>
    </marker>
  </defs>
  <line x1="45" y1="225" x2="175" y2="225" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="55" y1="225" x2="43" y2="238" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="75" y1="225" x2="63" y2="238" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="95" y1="225" x2="83" y2="238" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="115" y1="225" x2="103" y2="238" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="135" y1="225" x2="123" y2="238" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="155" y1="225" x2="143" y2="238" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="175" y1="225" x2="163" y2="238" stroke="#1a1a2e" stroke-width="1.3"/>
  <rect x="80" y="80" width="60" height="50" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="110" y="111" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="20" font-style="italic" fill="#1a1a2e">m</text>
  <line x1="110" y1="18" x2="110" y2="74" stroke="#c0392b" stroke-width="2.2" marker-end="url(#arrf-mk1)"/>
  <text x="122" y="48" font-family="'STIX Two Math','Times New Roman',serif" font-size="18" font-style="italic" fill="#c0392b">F</text>
  <line x1="52" y1="80" x2="52" y2="118" stroke="#1a1a2e" stroke-width="1.6" marker-end="url(#arr-mk1)"/>
  <text x="36" y="104" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">x</text>
  <line x1="93" y1="130" x2="93" y2="144" stroke="#1a1a2e" stroke-width="1.8"/>
  <polyline points="93,144 80,150 106,158 80,166 106,174 80,182 93,188" fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <line x1="93" y1="188" x2="93" y2="225" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="60" y="172" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">k</text>
  <line x1="127" y1="130" x2="127" y2="165" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="113" y1="165" x2="141" y2="165" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="113" y="165" width="28" height="22" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="127" y1="187" x2="127" y2="225" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="148" y="182" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">b</text>
</svg>

**a) Newton:** $m\ddot{x} + b\dot{x} + kx = F(t)$ → $\boxed{G(s) = \dfrac{X(s)}{F(s)} = \dfrac{1}{ms^2+bs+k}}$

**b) Lagrange:** $T=\frac{1}{2}m\dot{x}^2$, $V=\frac{1}{2}kx^2$, $D=\frac{1}{2}b\dot{x}^2$

$$\frac{d}{dt}\!\left(\frac{\partial L}{\partial\dot{x}}\right)-\frac{\partial L}{\partial x}+\frac{\partial D}{\partial\dot{x}}=F \implies m\ddot{x}+b\dot{x}+kx=F \quad\checkmark$$

---

## Mekanik Örnek 2 — İki Kütleli Sistem (Lagrange)

*İki kütle ($m_1$, $m_2$), iki yay ($k_1$, $k_2$), iki sönümleyici ($b_1$, $b_2$) yatay, dış kuvvet yok.*

<svg width="490" height="165" viewBox="0 0 490 165" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mk2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <line x1="30" y1="32" x2="30" y2="135" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="30" y1="44"  x2="16" y2="58"  stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="30" y1="62"  x2="16" y2="76"  stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="30" y1="80"  x2="16" y2="94"  stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="30" y1="98"  x2="16" y2="112" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="30" y1="116" x2="16" y2="130" stroke="#1a1a2e" stroke-width="1.3"/>
  <rect x="135" y="60" width="52" height="44" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="161" y="87" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">m₁</text>
  <rect x="303" y="60" width="52" height="44" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="329" y="87" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">m₂</text>
  <polyline points="30,72 52,72 60,62 76,82 92,62 108,82 120,72 135,72" fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="78" y="50" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">k₁</text>
  <line x1="30"  y1="104" x2="72"  y2="104" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="72"  y1="96"  x2="72"  y2="112" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="72"   y="96"   width="28" height="16" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="100" y1="104" x2="135" y2="104" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="82" y="130" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">b₁</text>
  <polyline points="187,72 205,72 213,62 229,82 245,62 261,82 273,72 303,72" fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="245" y="50" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">k₂</text>
  <line x1="187" y1="104" x2="222" y2="104" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="222" y1="96"  x2="222" y2="112" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="222"  y="96"   width="28" height="16" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="250" y1="104" x2="303" y2="104" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="245" y="130" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">b₂</text>
  <line x1="135" y1="38" x2="178" y2="38" stroke="#1a1a2e" stroke-width="1.6" marker-end="url(#arr-mk2)"/>
  <text x="157" y="26" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">x₁</text>
  <line x1="303" y1="38" x2="346" y2="38" stroke="#1a1a2e" stroke-width="1.6" marker-end="url(#arr-mk2)"/>
  <text x="325" y="26" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">x₂</text>
</svg>

**Lagrange:** $T=\frac{1}{2}m_1\dot{x}_1^2+\frac{1}{2}m_2\dot{x}_2^2$, $V=\frac{1}{2}k_1x_1^2+\frac{1}{2}k_2(x_2-x_1)^2$, $D=\frac{1}{2}b_1\dot{x}_1^2+\frac{1}{2}b_2(\dot{x}_2-\dot{x}_1)^2$

$$\boxed{m_1\ddot{x}_1 + (b_1+b_2)\dot{x}_1 - b_2\dot{x}_2 + (k_1+k_2)x_1 - k_2x_2 = 0}$$

$$\boxed{m_2\ddot{x}_2 + b_2\dot{x}_2 - b_2\dot{x}_1 + k_2x_2 - k_2x_1 = 0}$$

**Matris formu:** $M\ddot{x} + C\dot{x} + Kx = 0$ (serbest titreşim)

$$M = \begin{bmatrix}m_1&0\\0&m_2\end{bmatrix},\quad C = \begin{bmatrix}b_1+b_2&-b_2\\-b_2&b_2\end{bmatrix},\quad K = \begin{bmatrix}k_1+k_2&-k_2\\-k_2&k_2\end{bmatrix}$$

---

## Mekanik Örnek 3 — Sayısal: $k=6$, $m=1$, $b=5$

*Dikey sistem (yay üstten tavana, sönümleyici alttan zemine). $y$ kadar sıkıştırılıp serbest bırakılıyor.*

<svg width="200" height="270" viewBox="0 0 200 270" xmlns="http://www.w3.org/2000/svg">
  <line x1="50" y1="25" x2="150" y2="25" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="60" y1="25" x2="48" y2="13" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="78" y1="25" x2="66" y2="13" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="96" y1="25" x2="84" y2="13" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="114" y1="25" x2="102" y2="13" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="132" y1="25" x2="120" y2="13" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="50" y1="245" x2="150" y2="245" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="60" y1="245" x2="48" y2="257" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="78" y1="245" x2="66" y2="257" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="96" y1="245" x2="84" y2="257" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="114" y1="245" x2="102" y2="257" stroke="#1a1a2e" stroke-width="1.3"/>
  <rect x="75" y="110" width="50" height="44" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="100" y="137" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="20" font-style="italic" fill="#1a1a2e">m</text>
  <line x1="100" y1="25" x2="100" y2="38" stroke="#1a1a2e" stroke-width="1.8"/>
  <polyline points="100,38 88,46 112,56 88,66 112,76 88,86 100,94 100,110" fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="118" y="72" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">k</text>
  <line x1="100" y1="154" x2="100" y2="172" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="84" y1="172" x2="116" y2="172" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="84" y="172" width="32" height="24" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="100" y1="196" x2="100" y2="245" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="122" y="192" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">b</text>
</svg>

**TF:** $\dfrac{X(s)}{Y(s)} = \dfrac{1}{s^2+5s+6}$

**a) Doğal frekans:** $\omega_n = \sqrt{k/m} = \sqrt{6} \approx 2{,}449$ rad/s

**b) Sönüm oranı:** $\zeta = \dfrac{b}{2\sqrt{mk}} = \dfrac{5}{2\sqrt{6}} \approx 1{,}021 > 1$ → **Aşırı sönümlü**

**c) Kutuplar:** $s^2+5s+6=(s+2)(s+3)=0$ → $s_1=-2$, $s_2=-3$ (reel, negatif ✓)

**d) Birim basamak yanıtı** ($Y(s)=1/s$):

$$X(s) = \frac{1}{s(s+2)(s+3)} = \frac{1/6}{s} - \frac{1/2}{s+2} + \frac{1/3}{s+3}$$

$$\boxed{x(t) = \frac{1}{6} - \frac{1}{2}e^{-2t} + \frac{1}{3}e^{-3t}, \quad t\geq0 \qquad x(\infty) = \frac{1}{6} = \frac{1}{k}}$$

---

## Mekanik Örnek 4 — İki Kütle, Üç Yay, Newton + Cramer

*$F$ kuvveti $m_1$'e uygulanıyor. Çıkış $X_2(s)/F(s)$.*

<svg width="530" height="165" viewBox="0 0 530 165" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mk4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
    <marker id="arrf-mk4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#c0392b"/>
    </marker>
  </defs>
  <line x1="30" y1="32" x2="30" y2="135" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="30" y1="44" x2="16" y2="58" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="30" y1="64" x2="16" y2="78" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="30" y1="84" x2="16" y2="98" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="30" y1="104" x2="16" y2="118" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="500" y1="32" x2="500" y2="135" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="500" y1="44" x2="514" y2="58" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="500" y1="64" x2="514" y2="78" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="500" y1="84" x2="514" y2="98" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="500" y1="104" x2="514" y2="118" stroke="#1a1a2e" stroke-width="1.3"/>
  <rect x="135" y="60" width="52" height="44" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="161" y="87" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">m₁</text>
  <rect x="308" y="60" width="52" height="44" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="334" y="87" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">m₂</text>
  <line x1="38" y1="100" x2="130" y2="100" stroke="#c0392b" stroke-width="2.2" marker-end="url(#arrf-mk4)"/>
  <text x="72" y="92" font-family="'STIX Two Math','Times New Roman',serif" font-size="17" font-style="italic" fill="#c0392b">F</text>
  <polyline points="30,72 50,72 58,62 74,82 90,62 106,82 118,72 135,72" fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="82" y="50" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">k₁</text>
  <polyline points="187,72 205,72 213,62 229,82 245,62 261,82 273,72 308,72" fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="247" y="50" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">k₂</text>
  <line x1="187" y1="104" x2="222" y2="104" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="222" y1="96" x2="222" y2="112" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="222" y="96" width="28" height="16" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="250" y1="104" x2="308" y2="104" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="247" y="130" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">b</text>
  <polyline points="360,82 378,82 386,72 402,92 418,72 434,92 446,82 500,82" fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="430" y="60" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">k₃</text>
  <line x1="135" y1="38" x2="178" y2="38" stroke="#1a1a2e" stroke-width="1.6" marker-end="url(#arr-mk4)"/>
  <text x="157" y="26" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">x₁</text>
  <line x1="308" y1="38" x2="351" y2="38" stroke="#1a1a2e" stroke-width="1.6" marker-end="url(#arr-mk4)"/>
  <text x="330" y="26" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">x₂</text>
</svg>

**FBD + Laplace (sıfır başlangıç):**

$$\Delta_1 = m_1s^2+bs+(k_1+k_2), \quad \Delta_2 = m_2s^2+bs+(k_2+k_3), \quad Z = bs+k_2$$

$$\begin{bmatrix}\Delta_1 & -Z \\ -Z & \Delta_2\end{bmatrix}\begin{bmatrix}X_1 \\ X_2\end{bmatrix} = \begin{bmatrix}F \\ 0\end{bmatrix}$$

**Cramer Kuralı:**

$$\boxed{\frac{X_2(s)}{F(s)} = \frac{bs+k_2}{m_1m_2s^4+(m_1+m_2)bs^3+[m_1(k_2+k_3)+m_2(k_1+k_2)]s^2+b(k_1+k_3)s+(k_1k_2+k_1k_3+k_2k_3)}}$$

*4. dereceden sistem; $(bs+k_2)$ pay → sadece $k_2$ ve $b$ üzerinden $m_1$'den $m_2$'ye enerji aktarımı.*

---

## Mekanik Örnek 5 — Birim Dönüşümü ($m=2000$ kg, $k=16{,}5$ N/mm)

**SI'ya çevir:**

$$k = 16{,}5 \;\frac{\text{N}}{\text{mm}} = 16500 \;\frac{\text{N}}{\text{m}}, \quad b = 5000 \;\frac{\text{N·s}}{\text{m}}, \quad m = 2000 \;\text{kg}$$

**Hareket denklemi:** $2000\ddot{x}+5000\dot{x}+16500x = f(t)$

$$G(s) = \frac{X(s)}{F(s)} = \frac{1/2000}{s^2+2{,}5s+8{,}25}$$

**a) Doğal frekans:**

$$\omega_n = \sqrt{\frac{k}{m}} = \sqrt{\frac{16500}{2000}} = \sqrt{8{,}25} \approx 2{,}872 \;\text{rad/s}$$

**b) Sönüm oranı:**

$$\zeta = \frac{b}{2\sqrt{mk}} = \frac{5000}{2\sqrt{2000\times16500}} \approx 0{,}435 \quad (<1 \to \textbf{az sönümlü})$$

**c) Sistem tipi:** Az sönümlü → basamak girişine **salınımlı** yanıt, aşım var

**d) Sistem kazancı:**

$$\zeta = \frac{2{,}5}{2\omega_n} \implies 2\zeta\omega_n = 2{,}5 \checkmark, \quad \boxed{K = \frac{1}{k} = \frac{1}{16500} \approx 6{,}06\times10^{-5} \;\text{m/N}}$$

Kutuplar: $s_{1,2} = -1{,}25 \pm j\,2{,}587$

---

## Mekanik Örnek 6 — İki Dönel Kütle (Türetilmiş)

*$J_1$, $J_2$: atalet momentleri; $b_1$: sol duvar sönümü; $b_2$: sağ duvar sönümü; $k$: bağlayan yay. $T$ → $J_1$, çıkış $\Theta_2$.*

<svg width="100%" height="auto" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-red-mk6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#a93226"/>
    </marker>
    <marker id="arr-blue-mk6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1a5a9a"/>
    </marker>
    <marker id="arr-green-mk6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1e7a4a"/>
    </marker>
  </defs>
  <line x1="50" y1="50" x2="50" y2="150" stroke="#1a1a2e" stroke-width="3"/>
  <line x1="50" y1="100" x2="90" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="90" y1="85" x2="90" y2="115" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="90" y1="85" x2="110" y2="85" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="90" y1="115" x2="110" y2="115" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="105" y1="90" x2="105" y2="110" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="105" y1="100" x2="150" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <text x="80" y="75" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">b₁</text>
  <rect x="150" y="70" width="60" height="60" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="180" y="105" text-anchor="middle" font-family="'STIX Two Math',serif" font-size="18" font-style="italic">J₁</text>
  <path d="M 130 60 Q 150 40 170 60" fill="none" stroke="#a93226" stroke-width="2" marker-end="url(#arr-red-mk6)"/>
  <text x="150" y="35" font-family="'STIX Two Math',serif" font-size="16" fill="#a93226" font-style="italic">T</text>
  <path d="M 180 60 Q 200 40 220 60" fill="none" stroke="#1a5a9a" stroke-width="2" marker-end="url(#arr-blue-mk6)"/>
  <text x="200" y="35" font-family="'STIX Two Math',serif" font-size="16" fill="#1a5a9a" font-style="italic">θ₁</text>
  <line x1="210" y1="100" x2="240" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="240,100 245,85 255,115 265,85 275,115 285,85 295,115 300,100" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="300" y1="100" x2="330" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <text x="270" y="75" text-anchor="middle" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">k</text>
  <rect x="330" y="70" width="60" height="60" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="360" y="105" text-anchor="middle" font-family="'STIX Two Math',serif" font-size="18" font-style="italic">J₂</text>
  <path d="M 310 60 Q 330 40 350 60" fill="none" stroke="#1e7a4a" stroke-width="2" marker-end="url(#arr-green-mk6)"/>
  <text x="330" y="35" font-family="'STIX Two Math',serif" font-size="16" fill="#1e7a4a" font-style="italic">θ₂</text>
  <line x1="390" y1="100" x2="430" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="430" y1="85" x2="430" y2="115" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="430" y1="85" x2="450" y2="85" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="430" y1="115" x2="450" y2="115" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="445" y1="90" x2="445" y2="110" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="445" y1="100" x2="490" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <text x="460" y="75" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">b₂</text>
  <line x1="490" y1="50" x2="490" y2="150" stroke="#1a1a2e" stroke-width="3"/>
</svg>

**Hareket denklemleri (tork toplamı):**

$J_1$ için: $T - b_1\dot{\theta}_1 - k(\theta_1-\theta_2) = J_1\ddot{\theta}_1$

$J_2$ için: $k(\theta_1-\theta_2) - b_2\dot{\theta}_2 = J_2\ddot{\theta}_2$

**Laplace'ta:**

$(J_1s^2+b_1s+k)\Theta_1 - k\Theta_2 = T(s)$

$-k\Theta_1 + (J_2s^2+b_2s+k)\Theta_2 = 0$

**Cramer:** $\Theta_1 = \dfrac{(J_2s^2+b_2s+k)}{k}\Theta_2$, yerine koy:

$$\boxed{\frac{\Theta_2(s)}{T(s)} = \frac{k}{(J_1s^2+b_1s+k)(J_2s^2+b_2s+k) - k^2}}$$

---

## Mekanik Örnek 7 — Sarkaç Sistemi ($m=2$ kg, $g=9{,}81$ m/s²)

*Uzunluk $l$, horizontal kuvvet $F$, açı $\theta$.*

<svg width="100%" height="auto" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-red-mk7" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#a93226"/>
    </marker>
    <marker id="arr-blue-mk7" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1a5a9a"/>
    </marker>
  </defs>
  <line x1="100" y1="50" x2="300" y2="50" stroke="#1a1a2e" stroke-width="3"/>
  <line x1="200" y1="50" x2="200" y2="250" stroke="#1a1a2e" stroke-width="1" stroke-dasharray="5,5"/>
  <line x1="200" y1="50" x2="260" y2="200" stroke="#1a1a2e" stroke-width="2"/>
  <text x="220" y="130" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">l</text>
  <circle cx="260" cy="200" r="20" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="260" y="205" text-anchor="middle" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">m</text>
  <path d="M 200 100 A 50 50 0 0 1 220 96" fill="none" stroke="#1a5a9a" stroke-width="2" marker-end="url(#arr-blue-mk7)"/>
  <text x="210" y="85" font-family="'STIX Two Math',serif" font-size="16" fill="#1a5a9a" font-style="italic">θ</text>
  <line x1="180" y1="200" x2="230" y2="200" stroke="#a93226" stroke-width="2" marker-end="url(#arr-red-mk7)"/>
  <text x="160" y="205" font-family="'STIX Two Math',serif" font-size="16" fill="#a93226" font-style="italic">F</text>
</svg>

**Küçük açı yaklaşımı** ($\sin\theta\approx\theta$, $\cos\theta\approx1$):

**a) Newton (teğetsel yön):** Teğetsel kuvvet = $-mg\sin\theta + F\cos\theta$

$$ml^2\ddot{\theta} + mgl\theta = Fl \implies \boxed{\frac{\Theta(s)}{F(s)} = \frac{l}{ml^2s^2+mgl} = \frac{1}{mls^2+mg}}$$

**Serbest titreşim ($F=0$):**

$$\ddot{\theta} + \frac{g}{l}\theta = 0 \implies \boxed{\omega_n = \sqrt{\frac{g}{l}} = \sqrt{\frac{9{,}81}{l}} \;\text{rad/s}}$$

**b) Enerji metodu:** $T=\frac{1}{2}ml^2\dot{\theta}^2$, $V\approx\frac{1}{2}mgl\theta^2$

$$\frac{d}{dt}(T+V)=0 \implies ml^2\ddot{\theta}+mgl\theta=0 \implies \omega_n=\sqrt{g/l} \checkmark$$

**c) Lagrange:** $L=\frac{1}{2}ml^2\dot{\theta}^2-mgl(1-\cos\theta)$

$$\frac{d}{dt}(ml^2\dot{\theta})-(-mgl\sin\theta)=0 \implies ml^2\ddot{\theta}+mgl\theta=0 \checkmark$$

*$m=2$ kg, $l=1$ m için: $\omega_n\approx3{,}13$ rad/s*

---

## Mekanik Örnek 8 — Dişli Sistemi TF ($\Theta_1/T_1$, türetilmiş)

*Motor: $N_1$, $T_1$, $\theta_1$. Büyük dişli: $N_2$, $T_2$, $\theta_2$ (yük tarafı; $J_1$, yay $k$, sönümleyici $b$ duvara bağlı)*

<svg width="100%" height="auto" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-blue-mk8" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1a5a9a"/>
    </marker>
    <marker id="arr-green-mk8" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1e7a4a"/>
    </marker>
  </defs>
  <line x1="100" y1="180" x2="200" y2="180" stroke="#1a1a2e" stroke-width="3"/>
  <text x="120" y="210" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">motor</text>
  <rect x="200" y="150" width="20" height="60" fill="#ddd" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="230" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">N₁, T₁</text>
  <path d="M 130 160 A 20 20 0 0 1 150 140" fill="none" stroke="#1a5a9a" stroke-width="2" marker-end="url(#arr-blue-mk8)"/>
  <text x="155" y="145" font-family="'STIX Two Math',serif" font-size="16" fill="#1a5a9a" font-style="italic">θ₁</text>
  <rect x="200" y="50" width="20" height="100" fill="#ccc" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="40" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">N₂, T₂</text>
  <path d="M 130 80 A 20 20 0 0 1 150 60" fill="none" stroke="#1e7a4a" stroke-width="2" marker-end="url(#arr-green-mk8)"/>
  <text x="155" y="65" font-family="'STIX Two Math',serif" font-size="16" fill="#1e7a4a" font-style="italic">θ₂</text>
  <line x1="220" y1="100" x2="300" y2="100" stroke="#1a1a2e" stroke-width="3"/>
  <rect x="300" y="70" width="80" height="60" rx="30" ry="30" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="340" y="105" text-anchor="middle" font-family="'STIX Two Math',serif" font-size="18" font-style="italic">J₁</text>
  <line x1="380" y1="100" x2="420" y2="100" stroke="#1a1a2e" stroke-width="3"/>
  <line x1="420" y1="70" x2="420" y2="130" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="420" y1="80" x2="450" y2="80" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="450" y1="70" x2="450" y2="90" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="450" y1="70" x2="470" y2="70" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="450" y1="90" x2="470" y2="90" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="465" y1="75" x2="465" y2="85" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="465" y1="80" x2="520" y2="80" stroke="#1a1a2e" stroke-width="2"/>
  <text x="455" y="60" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">b</text>
  <line x1="420" y1="120" x2="440" y2="120" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="440,120 445,110 455,130 465,110 475,130 485,110 495,130 500,120" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="500" y1="120" x2="520" y2="120" stroke="#1a1a2e" stroke-width="2"/>
  <text x="465" y="145" font-family="'STIX Two Math',serif" font-size="16" font-style="italic">k</text>
  <line x1="520" y1="50" x2="520" y2="150" stroke="#1a1a2e" stroke-width="3"/>
</svg>

**Dişli ilişkileri:**

$$\theta_2 = \frac{N_1}{N_2}\theta_1, \qquad T_2 = \frac{N_2}{N_1}T_1$$

**$J_1$ üzerinde hareket denklemi** (şaft 2):

$$T_2 - b\dot{\theta}_2 - k\theta_2 = J_1\ddot{\theta}_2$$

$$\frac{N_2}{N_1}T_1 = \left(J_1s^2+bs+k\right)\cdot\frac{N_1}{N_2}\Theta_1$$

$$\boxed{\frac{\Theta_1(s)}{T_1(s)} = \frac{(N_2/N_1)^2}{J_1s^2+bs+k}}$$

*Motor miline yansıtılmış: $J_{ref}=J_1(N_1/N_2)^2$, $b_{ref}=b(N_1/N_2)^2$, $k_{ref}=k(N_1/N_2)^2$*
