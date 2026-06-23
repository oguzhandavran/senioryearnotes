---
tags: [mst, durum-uzayı, state-space, matris, özdeğer, kontrol, örnek-sorular]
---

# 03 — Durum Uzayı Örnekleri

← [[MST Ana Sayfa]] | Teori: [[../Konu Anlatımları/03 Durum Uzayı|03 Durum Uzayı]]

---

## Çözümlü Örnek 1: Mekanik Sistem (Ders Notları)

**Sistem:** $m\ddot{x} + b\dot{x} + kx = f(t)$, $m=1$, $b=3$, $k=2$

**Durum değişkenleri:** $x_1 = x$ (konum), $x_2 = \dot{x}$ (hız)

$$\dot{x}_1 = x_2$$
$$\dot{x}_2 = \ddot{x} = -kx_1 - bx_2 + f = -2x_1 - 3x_2 + f$$

$$\dot{x} = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} x + \begin{bmatrix} 0 \\ 1 \end{bmatrix} f, \qquad y = \begin{bmatrix} 1 & 0 \end{bmatrix} x$$

**Doğrulama:**
$$G(s) = C(sI-A)^{-1}B = \frac{1}{s^2+3s+2} \quad \checkmark$$

---

## Çözümlü Örnek 2: RLC Devre (Ders Notları)

**Devre:** $L = 1$, $R = 3$, $C = 0.5$ (seri RLC, $v_C$ çıkış)

Laplace yerine direkt türev:
$$L\frac{di}{dt} = -Ri - \frac{q}{C} + v_{in}$$
$$\frac{dq}{dt} = i$$

**Durum değişkenleri:** $x_1 = q$ (yük), $x_2 = i$ (akım)

$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -1/(LC) & -R/L \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 1/L \end{bmatrix} v_{in}$$

Değerleri yerleştir:
$$A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

Çıkış $v_C = q/C = x_1/0.5$: $C_{mat} = \begin{bmatrix} 2 & 0 \end{bmatrix}$

---

## Çözümlü Örnek 3: İki Kütleli Sistem (Ders Notları)

<svg width="400" height="140" xmlns="http://www.w3.org/2000/svg">
  <!-- Wall left -->
  <rect x="10" y="20" width="8" height="100" fill="#a9b1d6"/>
  <!-- Spring k1 -->
  <path d="M18,50 L35,50 L40,35 L50,65 L60,35 L70,65 L80,35 L90,65 L95,50 L110,50" fill="none" stroke="#9ece6a" stroke-width="2"/>
  <text x="60" y="25" text-anchor="middle" font-size="11" fill="#9ece6a">k₁</text>
  <!-- m1 box -->
  <rect x="110" y="35" width="50" height="30" fill="#1a1b26" stroke="#7dcfff" stroke-width="2"/>
  <text x="135" y="55" text-anchor="middle" font-size="13" fill="#7dcfff">m₁</text>
  <!-- Spring k2 -->
  <path d="M160,50 L175,50 L180,35 L190,65 L200,35 L210,65 L220,35 L225,50 L240,50" fill="none" stroke="#9ece6a" stroke-width="2"/>
  <text x="205" y="25" text-anchor="middle" font-size="11" fill="#9ece6a">k₂</text>
  <!-- m2 box -->
  <rect x="240" y="35" width="50" height="30" fill="#1a1b26" stroke="#7dcfff" stroke-width="2"/>
  <text x="265" y="55" text-anchor="middle" font-size="13" fill="#7dcfff">m₂</text>
  <!-- Force arrow -->
  <line x1="290" y1="50" x2="330" y2="50" stroke="#e0af68" stroke-width="2" marker-end="url(#arr)"/>
  <text x="335" y="55" font-size="11" fill="#e0af68">f(t)</text>
  <!-- b1 damper -->
  <line x1="135" y1="65" x2="135" y2="90" stroke="#a9b1d6" stroke-width="1.5"/>
  <rect x="118" y="90" width="34" height="14" fill="none" stroke="#bb9af7" stroke-width="2"/>
  <text x="155" y="102" font-size="10" fill="#bb9af7">b₁</text>
  <line x1="135" y1="104" x2="135" y2="120" stroke="#a9b1d6" stroke-width="1.5"/>
  <line x1="10" y1="120" x2="390" y2="120" stroke="#a9b1d6" stroke-width="1.5"/>
  <!-- Labels -->
  <text x="135" y="133" text-anchor="middle" font-size="10" fill="#a9b1d6">x₁</text>
  <text x="265" y="133" text-anchor="middle" font-size="10" fill="#a9b1d6">x₂</text>
  <defs>
    <marker id="arr" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#e0af68"/>
    </marker>
  </defs>
</svg>

**Denklemler:**
$$m_1\ddot{x}_1 = -k_1 x_1 - k_2(x_1-x_2) - b_1\dot{x}_1$$
$$m_2\ddot{x}_2 = -k_2(x_2-x_1) + f$$

**4. dereceden durum uzayı:** $[x_1, \dot{x}_1, x_2, \dot{x}_2]^T$

$$A = \begin{bmatrix} 0 & 1 & 0 & 0 \\ -(k_1+k_2)/m_1 & -b_1/m_1 & k_2/m_1 & 0 \\ 0 & 0 & 0 & 1 \\ k_2/m_2 & 0 & -k_2/m_2 & 0 \end{bmatrix}$$

$$B = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1/m_2 \end{bmatrix}$$

---

## SS Örnek 1 — Mekanik Sistem State-Space

*Sistem: Kütle $m$, yay $k$, sönümleyici $b$, giriş $f(t)$*

<svg width="320" height="200" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ss1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#1a1a2e"/>
    </marker>
    <marker id="arrf-ss1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#a93226"/>
    </marker>
    <marker id="arrx-ss1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#1e7a4a"/>
    </marker>
  </defs>
  <line x1="20" y1="40" x2="20" y2="170" stroke="#1a1a2e" stroke-width="3"/>
  <line x1="20" y1="40"  x2="8"  y2="55"  stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="20" y1="60"  x2="8"  y2="75"  stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="20" y1="80"  x2="8"  y2="95"  stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="20" y1="100" x2="8"  y2="115" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="20" y1="120" x2="8"  y2="135" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="20" y1="140" x2="8"  y2="155" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="20" y1="160" x2="8"  y2="175" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="20" y1="70" x2="48" y2="70" stroke="#1a1a2e" stroke-width="1.8"/>
  <polyline points="48,70 54,70 57,58 63,82 69,58 75,82 81,58 87,82 93,58 99,82 102,70 128,70"
    fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="72" y="52" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">k</text>
  <line x1="20" y1="130" x2="70" y2="130" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="70" y1="116" x2="70" y2="144" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="70" y="116" width="32" height="28" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="102" y1="130" x2="128" y2="130" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="84" y="113" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">b</text>
  <rect x="128" y="75" width="72" height="72" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="164" y="116" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="20" font-style="italic" fill="#1a1a2e">m</text>
  <line x1="200" y1="111" x2="248" y2="111" stroke="#a93226" stroke-width="2.2" marker-end="url(#arrf-ss1)"/>
  <text x="256" y="116" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#a93226">f(t)</text>
  <line x1="148" y1="50" x2="190" y2="50" stroke="#1e7a4a" stroke-width="1.6" marker-end="url(#arrx-ss1)"/>
  <text x="144" y="44" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1e7a4a">x(t)</text>
</svg>

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

$$A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -24 & -26 & -9 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ 24 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix}, \quad D = 0$$

**$G(s) = C(sI-A)^{-1}B$:**

$sI-A = \begin{bmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 24 & 26 & s+9 \end{bmatrix}$

**Determinant:**
$$\Delta = s\bigl[s(s+9)+26\bigr] + 24 = s^3+9s^2+26s+24$$

**Adjugate × B:** $C \cdot \text{adj}(sI-A) \cdot B = 24$

$$\boxed{G(s) = \frac{24}{s^3+9s^2+26s+24} = \frac{24}{(s+2)(s+3)(s+4)}}$$

Tüm kutuplar sol yarı düzlemde → **asimptotik kararlı** ✓

---

## SS Örnek 3 — İki Kütleli Sistem State-Space

<svg width="520" height="140" viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ss3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#1a1a2e"/>
    </marker>
    <marker id="arru-ss3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#a93226"/>
    </marker>
  </defs>
  <line x1="18" y1="30" x2="18" y2="110" stroke="#1a1a2e" stroke-width="3"/>
  <line x1="8" y1="40" x2="18" y2="30" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="60" x2="18" y2="50" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="80" x2="18" y2="70" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="100" x2="18" y2="90" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="18" y1="70" x2="56" y2="70" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="56" y1="58" x2="56" y2="82" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="56" y="58" width="30" height="24" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="86" y1="70" x2="108" y2="70" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="70" y="52" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">b</text>
  <rect x="108" y="45" width="65" height="55" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="140" y="78" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="18" font-style="italic" fill="#1a1a2e">m₁</text>
  <line x1="173" y1="70" x2="198" y2="70" stroke="#1a1a2e" stroke-width="1.8"/>
  <polyline points="198,70 202,70 205,58 211,82 217,58 223,82 229,58 235,82 238,70 262,70"
    fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="230" y="52" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">k</text>
  <rect x="262" y="45" width="65" height="55" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="294" y="78" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="18" font-style="italic" fill="#1a1a2e">m₂</text>
  <line x1="327" y1="70" x2="370" y2="70" stroke="#a93226" stroke-width="2.2" marker-end="url(#arru-ss3)"/>
  <text x="376" y="76" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#a93226">u</text>
  <line x1="118" y1="28" x2="162" y2="28" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ss3)"/>
  <text x="113" y="22" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">y₁</text>
  <line x1="272" y1="28" x2="316" y2="28" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ss3)"/>
  <text x="267" y="22" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">y₂</text>
</svg>

**Hareket denklemleri:**

$$m_1\ddot{y}_1 + b\dot{y}_1 + ky_1 = ky_2 \implies \ddot{y}_1 = -\frac{k}{m_1}y_1 - \frac{b}{m_1}\dot{y}_1 + \frac{k}{m_1}y_2$$

$$m_2\ddot{y}_2 + ky_2 = ky_1 + u \implies \ddot{y}_2 = \frac{k}{m_2}y_1 - \frac{k}{m_2}y_2 + \frac{1}{m_2}u$$

**Durum değişkenleri:** $x = [y_1,\ y_2,\ \dot{y}_1,\ \dot{y}_2]^T$

$$\boxed{A = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -\frac{k}{m_1} & \frac{k}{m_1} & -\frac{b}{m_1} & 0 \\ \frac{k}{m_2} & -\frac{k}{m_2} & 0 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ 0 \\ \frac{1}{m_2} \end{bmatrix}}$$

$y = y_2$ için $C = \begin{bmatrix} 0 & 1 & 0 & 0 \end{bmatrix}$, $D = 0$

---

## SS Örnek 4 — RLC Devre State-Space

<svg width="500" height="240" viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ss4a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1e7a4a"/>
    </marker>
  </defs>
  <line x1="60" y1="50" x2="60" y2="90" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="60" cy="118" r="28" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M48,118 C50,107 53,107 57,118 C61,129 64,129 68,118" fill="none" stroke="#1a1a2e" stroke-width="1.6" stroke-linecap="round"/>
  <text x="60" y="106" text-anchor="middle" font-family="'Helvetica Neue',sans-serif" font-size="11" font-weight="700" fill="#1a1a2e">+</text>
  <text x="60" y="134" text-anchor="middle" font-family="'Helvetica Neue',sans-serif" font-size="13" font-weight="700" fill="#1a1a2e">−</text>
  <text x="24" y="113" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">u</text>
  <text x="24" y="128" font-family="'Helvetica Neue',sans-serif" font-size="10" fill="#888">(t)</text>
  <line x1="60" y1="146" x2="60" y2="195" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="60" y1="50" x2="110" y2="50" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="110" y1="50" x2="110" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="88" y1="104" x2="132" y2="104" stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="88" y1="116" x2="132" y2="116" stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="110" y1="116" x2="110" y2="195" stroke="#1a1a2e" stroke-width="2"/>
  <text x="140" y="113" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">C</text>
  <text x="76" y="96" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a5a9a">V_C</text>
  <circle cx="110" cy="50" r="4" fill="#1a1a2e"/>
  <line x1="110" y1="50" x2="160" y2="50" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M160,50 C160,38 176,38 176,50" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M176,50 C176,38 192,38 192,50" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M192,50 C192,38 208,38 208,50" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M208,50 C208,38 224,38 224,50" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="224" y1="50" x2="280" y2="50" stroke="#1a1a2e" stroke-width="2"/>
  <text x="192" y="30" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">L</text>
  <line x1="168" y1="64" x2="198" y2="64" stroke="#1e7a4a" stroke-width="1.8" marker-end="url(#arr-ss4a)"/>
  <text x="183" y="78" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1e7a4a">i_L</text>
  <line x1="280" y1="50" x2="280" y2="88" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="280,88 267,92 293,98 267,104 293,110 267,116 293,122 280,126"
    fill="none" stroke="#1a1a2e" stroke-width="2" stroke-linejoin="round"/>
  <line x1="280" y1="126" x2="280" y2="195" stroke="#1a1a2e" stroke-width="2"/>
  <text x="298" y="112" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">R</text>
  <line x1="60" y1="195" x2="280" y2="195" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="280" y1="58" x2="350" y2="58" stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="280" y1="187" x2="350" y2="187" stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="350" y1="58" x2="350" y2="187" stroke="#a93226" stroke-width="1.8"/>
  <text x="342" y="70" font-family="'Helvetica Neue',sans-serif" font-size="12" font-weight="700" fill="#a93226">+</text>
  <text x="342" y="185" font-family="'Helvetica Neue',sans-serif" font-size="14" font-weight="700" fill="#a93226">−</text>
  <text x="364" y="127" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#a93226">V_o</text>
  <circle cx="280" cy="50" r="4" fill="#1a1a2e"/>
  <circle cx="60" cy="195" r="4" fill="#1a1a2e"/>
  <circle cx="280" cy="195" r="4" fill="#1a1a2e"/>
</svg>

**Durum değişkenleri:** $x_1 = V_C$ (kondansatör gerilimi), $x_2 = i_L$ (bobin akımı)

Çıkış: $V_o = i_L \cdot R = Rx_2$

**Devre denklemleri (KCL):**

$$\dot{x}_1 = \frac{u(t)}{C} - \frac{x_2}{C}, \qquad \dot{x}_2 = \frac{x_1}{L} - \frac{R}{L}x_2$$

$$\boxed{\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} 0 & -\dfrac{1}{C} \\ \dfrac{1}{L} & -\dfrac{R}{L} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} \dfrac{1}{C} \\ 0 \end{bmatrix} u, \quad y = \begin{bmatrix} 0 & R \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}}$$

---

## SS Örnek 5 — $C(sI-A)^{-1}B$ Adım Adım

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

<svg width="520" height="260" viewBox="0 0 520 260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ss6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1e7a4a"/>
    </marker>
  </defs>
  <line x1="55" y1="45"  x2="55" y2="88"  stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="55" cy="114" r="26" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M44,114 C46,104 49,104 52,114 C55,124 58,124 61,114" fill="none" stroke="#1a1a2e" stroke-width="1.6" stroke-linecap="round"/>
  <text x="55" y="104" text-anchor="middle" font-family="'Helvetica Neue',sans-serif" font-size="10" font-weight="700" fill="#1a1a2e">+</text>
  <text x="55" y="128" text-anchor="middle" font-family="'Helvetica Neue',sans-serif" font-size="13" font-weight="700" fill="#1a1a2e">−</text>
  <text x="22" y="110" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">V_i</text>
  <line x1="55" y1="140" x2="55" y2="215" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="55" y1="45" x2="130" y2="45" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="130" y1="45"  x2="130" y2="90"  stroke="#1a1a2e" stroke-width="2"/>
  <line x1="108" y1="94"  x2="152" y2="94"  stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="108" y1="106" x2="152" y2="106" stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="130" y1="106" x2="130" y2="215" stroke="#1a1a2e" stroke-width="2"/>
  <text x="160" y="102" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">C₁</text>
  <circle cx="130" cy="45" r="4" fill="#1a1a2e"/>
  <line x1="130" y1="45" x2="185" y2="45" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="185,45 189,45 192,33 198,57 204,33 210,57 216,33 222,57 225,45 260,45"
    fill="none" stroke="#1a1a2e" stroke-width="2" stroke-linejoin="round"/>
  <text x="207" y="28" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">R</text>
  <line x1="196" y1="58" x2="222" y2="58" stroke="#1e7a4a" stroke-width="1.8" marker-end="url(#arr-ss6)"/>
  <text x="209" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-style="italic" fill="#1e7a4a">i_L</text>
  <line x1="260" y1="45" x2="290" y2="45" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M290,45 C290,33 306,33 306,45" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M306,45 C306,33 322,33 322,45" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M322,45 C322,33 338,33 338,45" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="338" y1="45" x2="380" y2="45" stroke="#1a1a2e" stroke-width="2"/>
  <text x="314" y="24" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">L</text>
  <circle cx="380" cy="45" r="4" fill="#1a1a2e"/>
  <line x1="380" y1="45"  x2="380" y2="90"  stroke="#1a1a2e" stroke-width="2"/>
  <line x1="358" y1="94"  x2="402" y2="94"  stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="358" y1="106" x2="402" y2="106" stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="380" y1="106" x2="380" y2="215" stroke="#1a1a2e" stroke-width="2"/>
  <text x="410" y="102" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">C₂</text>
  <line x1="380" y1="53"  x2="460" y2="53"  stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="380" y1="207" x2="460" y2="207" stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="460" y1="53"  x2="460" y2="207" stroke="#a93226" stroke-width="1.8"/>
  <text x="472" y="135" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#a93226">V_o</text>
  <line x1="55" y1="215" x2="380" y2="215" stroke="#1a1a2e" stroke-width="2"/>
</svg>

**Durum değişkenleri** (3 depolama elemanı → $n=3$):

$$x_1 = V_{C_1}, \quad x_2 = i_L, \quad x_3 = V_{C_2}$$

**KCL ve KVL'den türetilen durum denklemleri:**

$$\dot{x}_1 = -\frac{1}{RC_1}x_1 + \frac{1}{C_1}x_2 - \frac{1}{RC_1}x_3 + \frac{1}{RC_1}V_i$$

$$\dot{x}_2 = -\frac{1}{L}x_1 + \frac{1}{L}V_i$$

$$\dot{x}_3 = -\frac{1}{RC_2}x_1 - \frac{1}{RC_2}x_3 + \frac{1}{RC_2}V_i$$

$$\boxed{A = \begin{bmatrix} -\frac{1}{RC_1} & \frac{1}{C_1} & -\frac{1}{RC_1} \\ -\frac{1}{L} & 0 & 0 \\ -\frac{1}{RC_2} & 0 & -\frac{1}{RC_2} \end{bmatrix}, \quad B = \begin{bmatrix} \frac{1}{RC_1} \\ \frac{1}{L} \\ \frac{1}{RC_2} \end{bmatrix}}$$

$y = V_o = V_{C_2} = x_3$ için $C_{mat} = [0\ 0\ 1]$, $D=0$
