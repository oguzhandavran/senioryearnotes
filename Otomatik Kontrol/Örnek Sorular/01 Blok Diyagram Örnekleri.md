---
tags: [otomatik-kontrol, blok-diyagram, mason, transfer-fonksiyonu, örnek-sorular]
---

# 01 — Blok Diyagram Örnekleri

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Giriş Kapalı Çevrim ve Blok Diyagramları]]

---

## Ödev-1 — Çok Çevrimli Blok Diyagram (Y/U = ?)

**Verilen:**
$$G_1=\frac{1}{s+1},\quad G_2=\frac{s+0.2}{s},\quad G_3=\frac{5}{s+2},\quad G_4=2,\quad G_5=\frac{10}{s+10},\quad G_6=3$$

**Topoloji:** $U \to G_1 \to \Sigma_1 \to G_2 \to \Sigma_2 \to G_3 \to G_6 \to Y$
- İç geri besleme: $G_3$ çıkışı $\to G_4 \to \Sigma_2$ (negatif)
- Dış geri besleme: $Y \to G_5 \to \Sigma_1$ (negatif)

<svg width="560" height="230" viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok-ex1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- U label -->
  <text x="5" y="69" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">U</text>
  <line x1="22" y1="65" x2="40" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex1)"/>
  <!-- G1 -->
  <rect x="42" y="51" width="88" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="86" y="70" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₁=1/(s+1)</text>
  <line x1="130" y1="65" x2="148" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex1)"/>
  <!-- Σ1 -->
  <circle cx="162" cy="65" r="13" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="162" y="60" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">+</text>
  <text x="158" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#c0392b">−</text>
  <line x1="175" y1="65" x2="192" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex1)"/>
  <!-- G2 -->
  <rect x="194" y="51" width="100" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="244" y="70" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₂=(s+0.2)/s</text>
  <line x1="294" y1="65" x2="314" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex1)"/>
  <!-- Σ2 -->
  <circle cx="328" cy="65" r="13" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="328" y="60" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">+</text>
  <text x="324" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#c0392b">−</text>
  <line x1="341" y1="65" x2="358" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex1)"/>
  <!-- G3 -->
  <rect x="360" y="51" width="76" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="398" y="70" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₃=5/(s+2)</text>
  <!-- Branch point after G3 -->
  <circle cx="437" cy="65" r="3" fill="#1a1a2e"/>
  <line x1="436" y1="65" x2="454" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex1)"/>
  <!-- G6 -->
  <rect x="456" y="51" width="44" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="478" y="70" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₆=3</text>
  <!-- Branch point before Y -->
  <circle cx="512" cy="65" r="3" fill="#1a1a2e"/>
  <line x1="500" y1="65" x2="530" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex1)"/>
  <text x="534" y="69" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">Y</text>
  <!-- Inner feedback: G4 from G3 output to Σ2 -->
  <line x1="437" y1="65" x2="437" y2="135" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="437" y1="135" x2="406" y2="135" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex1)"/>
  <rect x="360" y="121" width="46" height="28" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="383" y="140" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₄=2</text>
  <line x1="360" y1="135" x2="328" y2="135" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="328" y1="135" x2="328" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex1)"/>
  <!-- Outer feedback: G5 from Y to Σ1 -->
  <line x1="512" y1="65" x2="512" y2="185" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="512" y1="185" x2="260" y2="185" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex1)"/>
  <rect x="200" y="171" width="60" height="28" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="230" y="188" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e">G₅=10/(s+10)</text>
  <line x1="200" y1="185" x2="162" y2="185" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="162" y1="185" x2="162" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex1)"/>
</svg>

**Çözüm (iç çevrimden dışa):**

**Adım 1 — İç çevrim** ($\Sigma_2, G_3, G_4$):

$$A(s) = \frac{G_3}{1+G_3 G_4} = \frac{\frac{5}{s+2}}{1+\frac{10}{s+2}} = \frac{5}{s+12}$$

**Adım 2 — Dış çevrim** ($\Sigma_1, G_2, A, G_6, G_5$):

$$\frac{Y}{U} = \frac{G_1 \cdot G_2 \cdot A(s) \cdot G_6}{1 + G_2 \cdot A(s) \cdot G_6 \cdot G_5}$$

Numeratör: $G_1 G_2 A G_6 = \dfrac{1}{s+1}\cdot\dfrac{s+0.2}{s}\cdot\dfrac{5}{s+12}\cdot 3 = \dfrac{15(s+0.2)}{s(s+1)(s+12)}$

Paydada $G_2 A G_6 G_5$: $\dfrac{s+0.2}{s}\cdot\dfrac{5}{s+12}\cdot 3\cdot\dfrac{10}{s+10} = \dfrac{150(s+0.2)}{s(s+12)(s+10)}$

$$\boxed{\frac{Y}{U} = \frac{15(s+0.2)}{s(s+1)(s+12) + 150(s+0.2)\frac{s+1}{s+10}}\cdot\frac{1}{1}}$$

> [!sinav] Hızlı Yaklaşım
> İç çevrim sadeleştir → dış çevrim uygula. Negatif geri besleme her zaman: $\frac{G}{1+GH}$

---

## Ödev-2 — İkili Negatif Geri Besleme (Y/U = ?)

**Verilen:**
$$G_1=\frac{s+1}{s},\quad G_2=\frac{s+2}{s+1},\quad G_3=1,\quad G_4=\frac{1}{s^2+s+1},\quad G_5=\frac{10}{s+10}$$

**Topoloji:** $U \to \Sigma_1 \to G_1 \to \Sigma_2 \to G_2 \to \Sigma_3 \to G_4 \to Y$
- 1. iç geri besleme: $G_2$ çıkışı $\to G_3=1 \to \Sigma_2$ (negatif)
- Dış geri besleme: $Y \to G_5 \to \Sigma_1$ (negatif)

<svg width="560" height="230" viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok-ex2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <text x="5" y="69" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">U</text>
  <line x1="22" y1="65" x2="40" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex2)"/>
  <!-- Σ1 -->
  <circle cx="54" cy="65" r="13" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="54" y="60" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">+</text>
  <text x="50" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#c0392b">−</text>
  <line x1="67" y1="65" x2="82" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex2)"/>
  <!-- G1 -->
  <rect x="84" y="51" width="90" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="129" y="70" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₁=(s+1)/s</text>
  <line x1="174" y1="65" x2="190" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex2)"/>
  <!-- Σ2 -->
  <circle cx="203" cy="65" r="13" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="203" y="60" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">+</text>
  <text x="199" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#c0392b">−</text>
  <line x1="216" y1="65" x2="232" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex2)"/>
  <!-- G2 -->
  <rect x="234" y="51" width="100" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="284" y="70" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₂=(s+2)/(s+1)</text>
  <!-- Branch after G2 -->
  <circle cx="335" cy="65" r="3" fill="#1a1a2e"/>
  <line x1="334" y1="65" x2="356" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex2)"/>
  <!-- Σ3 -->
  <circle cx="370" cy="65" r="13" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="370" y="60" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">+</text>
  <text x="366" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#c0392b">−</text>
  <line x1="383" y1="65" x2="400" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex2)"/>
  <!-- G4 -->
  <rect x="402" y="51" width="100" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="452" y="70" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e">G₄=1/(s²+s+1)</text>
  <!-- Branch before Y -->
  <circle cx="514" cy="65" r="3" fill="#1a1a2e"/>
  <line x1="502" y1="65" x2="532" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok-ex2)"/>
  <text x="536" y="69" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">Y</text>
  <!-- Inner feedback G3=1: G2 out → G3 → Σ2 -->
  <line x1="335" y1="65" x2="335" y2="135" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="335" y1="135" x2="222" y2="135" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex2)"/>
  <rect x="258" y="121" width="64" height="28" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="290" y="140" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">G₃ = 1</text>
  <line x1="203" y1="135" x2="203" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex2)"/>
  <!-- Outer feedback G5: Y → G5 → Σ1 -->
  <line x1="514" y1="65" x2="514" y2="185" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="514" y1="185" x2="94" y2="185" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex2)"/>
  <rect x="230" y="171" width="60" height="28" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="260" y="188" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e">G₅=10/(s+10)</text>
  <line x1="54" y1="185" x2="54" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok-ex2)"/>
</svg>

**Adım 1 — İç çevrim** ($\Sigma_2, G_2, G_3=1$):

$$B(s) = \frac{G_2}{1+G_2 G_3} = \frac{G_2}{1+G_2} = \frac{\frac{s+2}{s+1}}{1+\frac{s+2}{s+1}} = \frac{s+2}{s+1+s+2} = \frac{s+2}{2s+3}$$

**Adım 2 — Dış çevrim:**

$$\frac{Y}{U} = \frac{G_1 \cdot B(s) \cdot G_4}{1 + G_1 \cdot B(s) \cdot G_4 \cdot G_5}$$

$$G_1 B G_4 = \frac{s+1}{s}\cdot\frac{s+2}{2s+3}\cdot\frac{1}{s^2+s+1}$$

$$\boxed{\frac{Y}{U} = \frac{(s+1)(s+2)}{s(2s+3)(s^2+s+1) + (s+1)(s+2)\cdot\frac{10}{s+10}\cdot s(2s+3)/(s(2s+3))}}$$

---

### Mason Formülü Örneği

Sistem: $G_1 \to G_2 \to G_3$, geri besleme $H_1$ (iç), $H_2$ (dış)

**İleri yollar:** $P_1 = G_1 G_2 G_3$

**Döngüler:** $L_1 = -G_2 H_1$, $L_2 = -G_1 G_2 G_3 H_2$

**Determinant:** $\Delta = 1 - (L_1 + L_2) = 1 + G_2 H_1 + G_1 G_2 G_3 H_2$

**$\Delta_1$:** $P_1$ ile temas eden döngü yok → $\Delta_1 = 1$

$$\boxed{T = \frac{G_1 G_2 G_3}{1 + G_2 H_1 + G_1 G_2 G_3 H_2}}$$

---

← [[OK Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Giriş Kapalı Çevrim ve Blok Diyagramları]]
