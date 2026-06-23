---
tags: [mst, elektrik, rlc, kvl, kcl, transfer-fonksiyonu, op-amp]
---

# 02 — Elektrik Sistemleri

← [[MST Ana Sayfa]]

## Temel Elemanlar

| Eleman | Simge | $v$-$i$ İlişkisi | Empedans $Z(s)$ | Admitans $Y(s)$ |
|--------|-------|-----------------|-----------------|-----------------|
| Direnç $R$ | — | $v = Ri$ | $R$ | $1/R$ |
| Kapasitör $C$ | — | $i = C\dfrac{dv}{dt}$ | $1/(Cs)$ | $Cs$ |
| İndüktör $L$ | — | $v = L\dfrac{di}{dt}$ | $Ls$ | $1/(Ls)$ |

---

## Kirchhoff Kanunları

**KVL (Voltaj):** $\sum v = 0$ (kapalı çevrede toplam voltaj sıfır)

**KCL (Akım):** $\sum i = 0$ (düğümde giren = çıkan akım)

---

## RLC Seri Devre

<svg width="700" height="380" xmlns="http://www.w3.org/2000/svg">
  <!-- Arka plan -->
  <rect width="700" height="380" fill="white"/>

  <!-- Ana kablo (üst) -->
  <line x1="80" y1="150" x2="620" y2="150" stroke="black" stroke-width="2.5"/>

  <!-- Voltaj kaynağı (V_in) -->
  <circle cx="80" cy="150" r="28" fill="none" stroke="black" stroke-width="2.5"/>
  <text x="80" y="158" font-size="16" font-weight="bold" text-anchor="middle">+</text>
  <text x="80" y="195" font-size="13" text-anchor="middle" font-weight="bold">V_in(t)</text>

  <!-- Direnç R (kare kutu) -->
  <rect x="140" y="128" width="50" height="44" fill="white" stroke="black" stroke-width="2.5" rx="2"/>
  <text x="165" y="159" font-size="16" font-weight="bold" text-anchor="middle">R</text>

  <!-- Bobin L (sarmal) -->
  <g id="coil">
    <path d="M 260 150 Q 272 132 284 150 Q 296 168 308 150"
          fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  <text x="284" y="195" font-size="16" font-weight="bold" text-anchor="middle">L</text>

  <!-- Kondansatör C (iki paralel çizgi) -->
  <line x1="375" y1="120" x2="375" y2="180" stroke="black" stroke-width="2.5"/>
  <line x1="390" y1="120" x2="390" y2="180" stroke="black" stroke-width="2.5"/>
  <text x="382" y="205" font-size="16" font-weight="bold" text-anchor="middle">C</text>

  <!-- Çıkış V_c (sağ üst) -->
  <text x="620" y="135" font-size="13" font-weight="bold">V_c</text>

  <!-- Alt kablo (GND) -->
  <line x1="80" y1="260" x2="620" y2="260" stroke="black" stroke-width="2.5"/>

  <!-- Dikey bağlantılar -->
  <line x1="80" y1="178" x2="80" y2="260" stroke="black" stroke-width="2.5"/>
  <line x1="620" y1="150" x2="620" y2="260" stroke="black" stroke-width="2.5"/>

  <!-- Ara bağlantı kabloları -->
  <line x1="190" y1="150" x2="260" y2="150" stroke="black" stroke-width="2.5"/>
  <line x1="308" y1="150" x2="375" y2="150" stroke="black" stroke-width="2.5"/>
  <line x1="390" y1="150" x2="620" y2="150" stroke="black" stroke-width="2.5"/>

  <!-- GND sembolü (üç çizgi) -->
  <line x1="350" y1="260" x2="350" y2="280" stroke="black" stroke-width="2.5"/>
  <line x1="330" y1="280" x2="370" y2="280" stroke="black" stroke-width="2.5"/>
  <line x1="340" y1="290" x2="360" y2="290" stroke="black" stroke-width="2.5"/>
  <line x1="345" y1="300" x2="355" y2="300" stroke="black" stroke-width="2.5"/>
  <text x="350" y="325" font-size="12" font-weight="bold" text-anchor="middle">GND</text>

  <!-- Düğüm noktaları (siyah daireler) -->
  <circle cx="165" cy="150" r="3.5" fill="black"/>
  <circle cx="260" cy="150" r="3.5" fill="black"/>
  <circle cx="308" cy="150" r="3.5" fill="black"/>
  <circle cx="375" cy="150" r="3.5" fill="black"/>
  <circle cx="390" cy="150" r="3.5" fill="black"/>

  <!-- Başlık -->
  <text x="350" y="30" font-size="18" font-weight="bold" text-anchor="middle">RLC Seri Devresi</text>

  <!-- Açıklama metni -->
  <text x="350" y="360" font-size="11" text-anchor="middle" fill="#666">KVL: v_in = v_R + v_L + v_C</text>
</svg>

**KVL:** $v_{in} = v_R + v_L + v_C = Ri + L\dfrac{di}{dt} + \dfrac{1}{C}\int i\,dt$

Çıkış $v_C$ için ($q = \int i\,dt$):

$$L\ddot{q} + R\dot{q} + \frac{1}{C}q = v_{in}$$

$$\boxed{G(s) = \frac{V_C(s)}{V_{in}(s)} = \frac{1/LC}{s^2 + (R/L)s + 1/(LC)}}$$

> [!tip] Mekanik Analoji
> $L \leftrightarrow m$, $R \leftrightarrow b$, $1/C \leftrightarrow k$, $v_{in} \leftrightarrow f$, $q \leftrightarrow x$

---

## RLC Paralel Devre

**KCL:** $i_{in} = i_R + i_L + i_C = \dfrac{v}{R} + \dfrac{1}{L}\int v\,dt + C\dfrac{dv}{dt}$

Diferansiyel denklem:

$$C\ddot{v} + \frac{1}{R}\dot{v} + \frac{1}{L}v = \dot{i}_{in}$$

$$G(s) = \frac{V(s)}{I_{in}(s)} = \frac{s/C}{s^2 + s/(RC) + 1/(LC)}$$

---

## Empedans Yöntemi (Laplace Uzayında)

Laplace'ta direkt empedans kullanarak çözüm:

**Seri:** $Z_{toplam} = Z_1 + Z_2 + \ldots$

**Paralel:** $\dfrac{1}{Z_{toplam}} = \dfrac{1}{Z_1} + \dfrac{1}{Z_2} + \ldots$

**Gerilim bölücü:**
$$V_2(s) = V_{in}(s) \cdot \frac{Z_2}{Z_1 + Z_2}$$

---

## Çözümlü Örnek 1: R-L-R₂-C Mesh Devresi

<svg width="660" height="310" viewBox="0 0 660 310" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-m1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1e7a4a"/>
    </marker>
    <marker id="arr-m2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1a5a9a"/>
    </marker>
  </defs>
  <text x="290" y="22" text-anchor="middle" font-family="'Helvetica Neue',sans-serif" font-size="14" font-weight="700" fill="#1a1a2e">R₁-L-R₂-C  İki Mesh Devresi</text>
  <line x1="60" y1="65" x2="60" y2="105" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="60" cy="133" r="28" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M46,133 C48,119 54,119 58,133 C62,147 66,147 70,133" fill="none" stroke="#1a1a2e" stroke-width="1.6" stroke-linecap="round"/>
  <text x="60" y="122" text-anchor="middle" font-family="Helvetica,sans-serif" font-size="10" font-weight="700" fill="#1a1a2e">+</text>
  <text x="60" y="148" text-anchor="middle" font-family="Helvetica,sans-serif" font-size="13" font-weight="700" fill="#1a1a2e">−</text>
  <text x="22" y="131" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">V_in</text>
  <line x1="60" y1="161" x2="60" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="60" y1="65" x2="105" y2="65" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="105,65 109,65 112,53 118,77 124,53 130,77 136,53 142,77 145,65 190,65" fill="none" stroke="#1a1a2e" stroke-width="2" stroke-linejoin="round"/>
  <text x="125" y="44" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">R₁</text>
  <line x1="113" y1="82" x2="141" y2="82" stroke="#1e7a4a" stroke-width="1.8" marker-end="url(#arr-m1)"/>
  <text x="127" y="97" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1e7a4a">i₁</text>
  <line x1="190" y1="65" x2="280" y2="65" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="280" cy="65" r="4.5" fill="#1a1a2e"/>
  <line x1="280" y1="65" x2="280" y2="100" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,100 C264,100 264,120 280,120" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,120 C264,120 264,140 280,140" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,140 C264,140 264,160 280,160" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="280" y1="160" x2="280" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <text x="248" y="133" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">L</text>
  <line x1="280" y1="65" x2="325" y2="65" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="325,65 329,65 332,53 338,77 344,53 350,77 356,53 362,77 365,65 410,65" fill="none" stroke="#1a1a2e" stroke-width="2" stroke-linejoin="round"/>
  <text x="345" y="44" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="15" font-style="italic" fill="#1a1a2e">R₂</text>
  <line x1="333" y1="82" x2="361" y2="82" stroke="#1a5a9a" stroke-width="1.8" marker-end="url(#arr-m2)"/>
  <text x="347" y="97" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a5a9a">i₂</text>
  <line x1="410" y1="65" x2="490" y2="65" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="490" cy="65" r="4.5" fill="#1a1a2e"/>
  <line x1="490" y1="65" x2="490" y2="152" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="458" y1="152" x2="522" y2="152" stroke="#1a1a2e" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="458" y1="170" x2="522" y2="170" stroke="#1a1a2e" stroke-width="3.5" stroke-linecap="round"/>
  <text x="534" y="165" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">C</text>
  <line x1="490" y1="170" x2="490" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="490" y1="73"  x2="580" y2="73"  stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="490" y1="247" x2="580" y2="247" stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="580" y1="73"  x2="580" y2="247" stroke="#a93226" stroke-width="1.8"/>
  <text x="592" y="165" font-family="'STIX Two Math','Times New Roman',serif" font-size="17" font-style="italic" fill="#a93226">V_C</text>
  <line x1="60" y1="255" x2="490" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="60"  cy="65"  r="4.5" fill="#1a1a2e"/>
  <circle cx="60"  cy="255" r="4.5" fill="#1a1a2e"/>
  <circle cx="280" cy="255" r="4.5" fill="#1a1a2e"/>
  <circle cx="490" cy="255" r="4.5" fill="#1a1a2e"/>
  <line x1="280" y1="255" x2="280" y2="272" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="258" y1="272" x2="302" y2="272" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="266" y1="282" x2="294" y2="282" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="274" y1="292" x2="286" y2="292" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="175" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1e7a4a" opacity="0.55">Mesh 1</text>
  <text x="385" y="175" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a5a9a" opacity="0.55">Mesh 2</text>
</svg>

**Mesh 1** ($i_1$): $R_1 i_1 + L s (i_1 - i_2) = V_{in}$

**Mesh 2** ($i_2$): $Ls(i_2 - i_1) + R_2 i_2 + \dfrac{1}{Cs}i_2 = 0$

**Matris biçimi:**

$$\begin{bmatrix} R_1 + Ls & -Ls \\ -Ls & Ls + R_2 + 1/(Cs) \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} V_{in} \\ 0 \end{bmatrix}$$

**Cramer kuralı:** $I_2 = \dfrac{\Delta_2}{\Delta}$, çıkış voltajı: $V_C = \dfrac{I_2}{Cs}$

---

## Çözümlü Örnek 2: Transfer Fonksiyonu

**Devre:** $R_1 = 1\,\Omega$, $L = 1\,\text{H}$, $R_2 = 1\,\Omega$, $C = 1\,\text{F}$

Mesh denklemleri:

$$\begin{bmatrix} 1+s & -s \\ -s & s + 1 + 1/s \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} V_{in} \\ 0 \end{bmatrix}$$

$\Delta = (1+s)(s+1+1/s) - s^2 = (1+s)(s+1+1/s) - s^2$

$= s + 1 + 1/s + s^2 + s + 1 - s^2 = s^2/s + 2s + 2 + 1/s$

Payı ayarla: $\Delta = (s^2 + 2s^2 + 2s + 1)/s$... (say. hesabına göre)

$$G(s) = \frac{V_C(s)}{V_{in}(s)} = \frac{1}{s^3 + 2s^2 + 2s + 1}$$

---

## Op-Amp Devreleri

**İdeal Op-Amp Varsayımları:**
- $v_+ = v_-$ (negatif geri beslemeli)
- $i_+ = i_- = 0$ (giriş akımı yok)

### Ters Çevirici (Inverting Amplifier)

$$\frac{V_{out}}{V_{in}} = -\frac{Z_f}{Z_{in}}$$

### Türevleyici (Differentiator)

$Z_{in} = R$, $Z_f = 1/(Cs)$:
$$G(s) = -\frac{1/(Cs)}{R} = -\frac{1}{RCs}$$

### Entegratör (Integrator)

$Z_{in} = R$, $Z_f = 1/(Cs)$:
$$G(s) = -\frac{1/(Cs)}{R} = -\frac{1}{RCs}$$

---

## Düğüm Gerilim Yöntemi (Node Voltage)

**Adım 1:** Her düğüme voltaj ata ($v_1$, $v_2$, ...)
**Adım 2:** KCL uygula: her düğümde $\sum \dfrac{v_k - v_j}{Z_{kj}} = i_{kaynaklar}$
**Adım 3:** Çöz, transfer fonksiyonu bul

---

> [!sinav] Sınav İpucu
> - Empedans = Laplace uzayında devre analizi
> - Kapasitör: $1/(Cs)$ → yüksek frekansta kısa devre, alçakta açık devre
> - İndüktör: $Ls$ → alçak frekansta kısa devre, yüksekte açık devre
> - Mesh için KVL, düğüm için KCL
> - Başlangıç koşulları sıfır alındığında $V=ZI$ direkt kullanılır

---

---

## Çözümlü Örnekler (Dataset)

### Elektrik Örnek 1 — R₁-L-R₂-C Mesh Devresi

*Devre: İki mesh, $R_1$ ve $L$ sol mesh; $R_2$ ve $C$ sağ mesh; $L$ ortak eleman. Giriş $V_i$, çıkış $V_o = V_C$.*

<svg width="620" height="300" viewBox="0 0 620 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-el1g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1e7a4a"/>
    </marker>
    <marker id="arr-el1b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1a5a9a"/>
    </marker>
  </defs>
  <line x1="80" y1="80"  x2="80" y2="133" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="80" cy="167" r="34" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M65,167 C67,154 71,154 75,167 C79,180 83,180 87,167" fill="none" stroke="#1a1a2e" stroke-width="1.6" stroke-linecap="round"/>
  <text x="80" y="152" text-anchor="middle" font-family="'Helvetica Neue',sans-serif" font-size="11" font-weight="700" fill="#1a1a2e">+</text>
  <text x="80" y="188" text-anchor="middle" font-family="'Helvetica Neue',sans-serif" font-size="14" font-weight="700" fill="#1a1a2e">−</text>
  <text x="36" y="162" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="17" font-style="italic" fill="#1a1a2e">V</text>
  <text x="47" y="168" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">i</text>
  <line x1="80" y1="201" x2="80" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="80" y1="80" x2="118" y2="80" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="118,80 126,80 131,66 141,94 151,66 161,94 171,66 181,94 191,66 201,94 206,80 242,80"
    fill="none" stroke="#1a1a2e" stroke-width="2" stroke-linejoin="round"/>
  <line x1="242" y1="80" x2="280" y2="80" stroke="#1a1a2e" stroke-width="2"/>
  <text x="164" y="54" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">R₁</text>
  <line x1="90" y1="68" x2="116" y2="68" stroke="#1e7a4a" stroke-width="1.8" marker-end="url(#arr-el1g)"/>
  <text x="103" y="58" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1e7a4a">i₁</text>
  <line x1="280" y1="80" x2="318" y2="80" stroke="#1a1a2e" stroke-width="2"/>
  <polyline points="318,80 326,80 331,66 341,94 351,66 361,94 371,66 381,94 391,66 401,94 406,80 442,80"
    fill="none" stroke="#1a1a2e" stroke-width="2" stroke-linejoin="round"/>
  <line x1="442" y1="80" x2="490" y2="80" stroke="#1a1a2e" stroke-width="2"/>
  <text x="364" y="54" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">R₂</text>
  <line x1="292" y1="68" x2="316" y2="68" stroke="#1a5a9a" stroke-width="1.8" marker-end="url(#arr-el1b)"/>
  <text x="304" y="58" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a5a9a">i₂</text>
  <line x1="80" y1="255" x2="490" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="280" y1="80" x2="280" y2="112" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,112 C262,112 262,130 280,130" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,130 C262,130 262,148 280,148" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,148 C262,148 262,166 280,166" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,166 C262,166 262,184 280,184" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M280,184 C262,184 262,202 280,202" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="280" y1="202" x2="280" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <text x="246" y="162" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">L</text>
  <line x1="490" y1="80"  x2="490" y2="152" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="458" y1="156" x2="522" y2="156" stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="458" y1="170" x2="522" y2="170" stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>
  <line x1="490" y1="170" x2="490" y2="255" stroke="#1a1a2e" stroke-width="2"/>
  <text x="532" y="167" font-family="'STIX Two Math','Times New Roman',serif" font-size="16" font-style="italic" fill="#1a1a2e">C</text>
  <circle cx="80"  cy="80"  r="4.5" fill="#1a1a2e"/>
  <circle cx="280" cy="80"  r="4.5" fill="#1a1a2e"/>
  <circle cx="490" cy="80"  r="4.5" fill="#1a1a2e"/>
  <circle cx="80"  cy="255" r="4.5" fill="#1a1a2e"/>
  <circle cx="280" cy="255" r="4.5" fill="#1a1a2e"/>
  <circle cx="490" cy="255" r="4.5" fill="#1a1a2e"/>
  <line x1="490" y1="88"  x2="563" y2="88"  stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="490" y1="247" x2="563" y2="247" stroke="#a93226" stroke-width="1.4" stroke-dasharray="5,3"/>
  <line x1="563" y1="88"  x2="563" y2="247" stroke="#a93226" stroke-width="1.8"/>
  <text x="574" y="172" font-family="'STIX Two Math','Times New Roman',serif" font-size="18" font-style="italic" fill="#a93226">V_o</text>
</svg>

**KVL — Mesh 1 ($i_1$):** $V_i = R_1 I_1 + Ls(I_1 - I_2)$ → $V_i = (R_1+Ls)I_1 - Ls\,I_2$

**KVL — Mesh 2 ($i_2$):** $Ls(I_2-I_1) + R_2 I_2 + \dfrac{1}{Cs}I_2 = 0$ → $-Ls\,I_1 + \left(Ls+R_2+\dfrac{1}{Cs}\right)I_2 = 0$

Denk. (2)'den $I_1 = \dfrac{Ls+R_2+1/(Cs)}{Ls}I_2$ alıp (1)'e koy; $V_o = I_2/(Cs)$:

$$\boxed{\frac{V_o(s)}{V_i(s)} = \frac{Ls}{(R_1+R_2)LCs^2 + (R_1R_2C+L)s + R_1}}$$

*Bant geçiren davranış: $s\to0$ → $V_o\to0$ (C açık devre), $s\to\infty$ → $V_o\to0$ (L açık devre)*

---

### Elektrik Örnek 2 — Ters Çevirici Op-Amp (R₁,C₁ giriş; R₂,C₂ geri besleme)

**İdeal op-amp → sanal toprak** ($V_-=0$), $i_1=i_2$

Giriş empedansı: $Z_1 = R_1 + \dfrac{1}{C_1s} = \dfrac{R_1C_1s+1}{C_1s}$

Geri besleme empedansı: $Z_2 = \dfrac{R_2}{R_2C_2s+1}$ ($R_2 \parallel C_2$)

**İnverting TF:** $V_o/V_i = -Z_2/Z_1$

$$\boxed{\frac{V_o(s)}{V_i(s)} = -\frac{R_2 C_1 s}{(R_1C_1s+1)(R_2C_2s+1)}}$$

**Sayısal ($C_1=C_2=1$ F, $R_1=2\,\Omega$, $R_2=3\,\Omega$, $V_i=1$ V DC):**

$$\frac{V_o(s)}{V_i(s)} = -\frac{3s}{(2s+1)(3s+1)} = -\frac{3s}{6s^2+5s+1}$$

$V_i(s)=1/s$ için:

$$V_o(s) = -\frac{3}{6s^2+5s+1} = \frac{3}{s+\frac{1}{2}} - \frac{3}{s+\frac{1}{3}}$$

Kısmi kesir: $A = -6/(−1/6) \cdot (-1/2) \Rightarrow$ doğrudan:

$$\boxed{V_o(t) = 3e^{-t/2} - 3e^{-t/3}, \quad t\geq0}$$

*Kontrol: $V_o(0^+)=0$ ✓, $V_o(\infty)=0$ ✓ (C1 DC'yi bloke eder)*

---

### Elektrik Örnek 3 — Ters Çevirmeyen Op-Amp (Non-Inverting)

*Devre: $V_i$ → $R_1$, $R_2$ bölücü → op-amp $(+)$ giriş; $R_f$ ve $C_1$ (−) girişten çıkışa geri besleme, $C_1$ $(−)$'den GND'ye*

**Adım 1 — $(+)$ giriş:** $V_+ = V_i \cdot \dfrac{R_2}{R_1+R_2}$

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

### Elektrik Örnek 4 — Elektromekanik Sistem (RL + Kütle-Yay-Sönümleyici)

*$RL$ bobininin oluşturduğu manyetik kuvvet $F_m = K_m i$; mekanik sistem: kütle $m$, yay $k$, sönümleyici $b$*

**Elektrik devresi (KVL):**
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

---

← [[01 Mekanik Sistemler]] | [[MST Ana Sayfa]] | → [[03 Durum Uzayı]]
