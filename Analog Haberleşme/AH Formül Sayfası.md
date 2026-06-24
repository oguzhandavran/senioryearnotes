---
tags: [analog-haberleşme, formül, özet, hızlı-erişim]
---

# AH — Formül Sayfası

← [[AH Ana Sayfa]]

---

## Fourier Dönüşümü (f-Konvansiyonu)

$$\boxed{X(f) = \int_{-\infty}^{\infty} x(t)\,e^{-j2\pi ft}\,dt}$$
$$\boxed{x(t) = \int_{-\infty}^{\infty} X(f)\,e^{j2\pi ft}\,df}$$

---

## Temel FT Çiftleri

| $x(t)$ | $X(f)$ |
|--------|--------|
| $\delta(t)$ | $1$ |
| $\delta(t-t_0)$ | $e^{-j2\pi ft_0}$ |
| $1$ | $\delta(f)$ |
| $e^{j2\pi f_0 t}$ | $\delta(f-f_0)$ |
| $\cos(2\pi f_0 t)$ | $\tfrac{1}{2}[\delta(f-f_0)+\delta(f+f_0)]$ |
| $\sin(2\pi f_0 t)$ | $\tfrac{1}{2j}[\delta(f-f_0)-\delta(f+f_0)]$ |
| $A\,\Pi(t/\tau)$ | $A\tau\,\text{sinc}(f\tau)$ |
| $A\tau\,\text{sinc}(\tau t)$ | $A\,\Pi(f/\tau)$ |
| $e^{-at}u(t)$, $a>0$ | $\dfrac{1}{a+j2\pi f}$ |
| $e^{-a|t|}$, $a>0$ | $\dfrac{2a}{a^2+(2\pi f)^2}$ |
| $u(t)$ | $\tfrac{1}{2}\delta(f)+\dfrac{1}{j2\pi f}$ |

---

## FT Özellikleri

| Özellik          | Zaman                 | Frekans               |        |              |     |        |
| ---------------- | --------------------- | --------------------- | ------ | ------------ | --- | ------ |
| Doğrusallık      | $ax+by$               | $aX+bY$               |        |              |     |        |
| Zaman kaydırma   | $x(t-t_0)$            | $e^{-j2\pi ft_0}X(f)$ |        |              |     |        |
| Frekans kaydırma | $x(t)e^{j2\pi f_0 t}$ | $X(f-f_0)$            |        |              |     |        |
| Ölçekleme        | $x(at)$               | $                     | a      | ^{-1}X(f/a)$ |     |        |
| Konvülüsyon      | $x(t)*h(t)$           | $X(f)H(f)$            |        |              |     |        |
| Çarpma           | $x(t)h(t)$            | $X(f)*H(f)$           |        |              |     |        |
| Türev            | $x^{(n)}(t)$          | $(j2\pi f)^nX(f)$     |        |              |     |        |
| Parseval         | $\int                 | x                     | ^2 dt$ | $\int        | X   | ^2 df$ |
| Dualite          | $X(t)$                | $x(-f)$               |        |              |     |        |

---

## Fourier Serisi

$$x(t) = \sum_{n=-\infty}^{\infty} c_n\,e^{jn\omega_0 t}, \qquad \omega_0 = 2\pi/T_0$$

$$\boxed{c_n = \frac{1}{T_0}\int_0^{T_0} x(t)\,e^{-jn\omega_0 t}\,dt}$$

**Kare dalga:** $c_n = \dfrac{A\tau}{T_0}\,\text{sinc}\!\left(\dfrac{n\tau}{T_0}\right)$

**Periyodik işaret FD:** $X(f) = \displaystyle\sum_{n} c_n\,\delta\!\left(f - \dfrac{n}{T_0}\right)$

---

## Sinc Fonksiyonu

$$\boxed{\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}, \qquad \text{sinc}(0) = 1}$$

Sıfırları: $x = \pm 1, \pm 2, \pm 3, \ldots$

---

## Güç ve Enerji

| Tür | Koşul | Formül |
|-----|-------|--------|
| Enerji işareti | $E < \infty$ | $E = \int x^2 dt = \int |X|^2 df$ |
| Güç işareti | $P < \infty$ | $P = \lim\frac{1}{T}\int_{-T/2}^{T/2}x^2 dt$ |
| $\cos(\omega_0 t)$ gücü | — | $P = 1/2$ |
| $A$ sabit gücü | — | $P = A^2$ |

**Özilişki:** $R(\tau) = \lim\frac{1}{T}\int x(t)x(t+\tau)dt$, $R(0)=P$

**PSD:** $G(f) = \mathcal{F}\{R(\tau)\}$, $\quad S_y(f) = |H(f)|^2 S_x(f)$

---

## Genlik Modülasyonu

### Standart AM

$$\boxed{x_c(t) = A_c[1+m\,x(t)]\cos(2\pi f_c t)}$$

$$X_c(f) = \frac{A_c}{2}[\delta(f-f_c)+\delta(f+f_c)] + \frac{A_c m}{2}[X(f-f_c)+X(f+f_c)]$$

$$\boxed{m = \frac{C_{\max}-C_{\min}}{C_{\max}+C_{\min}}}$$

**Güç:** $P_T = \dfrac{A_c^2}{2}\!\left(1 + \dfrac{m^2}{2}\right)$ (tek ton, $A_m=1$)

**Verimlilik:** $\eta = \dfrac{m^2/2}{1+m^2/2}$ → $m=1$: $\eta = 1/3$

### DSB-SC

$$\boxed{x_{DSB}(t) = A_c\,x(t)\cos(2\pi f_c t)}$$

$$P_{DSB} = \frac{A_c^2}{2}\langle x^2\rangle, \qquad \eta = 1$$

### SSB (Tek Yan Bant)

$$x_c(t) = \frac{A_c}{2}\,x(t)\cos(2\pi f_c t) \mp \frac{A_c}{2}\,\hat{x}(t)\sin(2\pi f_c t)$$

- $-$: USB (Üst Yan Bant), $+$: LSB (Alt Yan Bant)
- $\hat{x}(t)$: Hilbert dönüşümü ($\sin\to-\cos$, $\cos\to\sin$)
- $B_{SSB} = W$ (AM/DSB'nin yarısı)

### Modülasyon Karşılaştırma

| Tür | $C_1$ | $C_2$ | $g(t)$ | $BW$ | $\eta$ |
|-----|-------|-------|--------|------|--------|
| AM | $A_c$ | $mA_c$ | $0$ | $2W$ | $<1$ |
| DSB-SC | $0$ | $A_c$ | $0$ | $2W$ | $1$ |
| SSB | $0$ | $A_c/2$ | $\pm\hat{x}$ | $W$ | $1$ |

### Bant Genişlikleri

| Mod | $B_T$ |
|-----|-------|
| AM, DSB-SC | $2W$ |
| SSB | $W$ |

---

## Süzgeçler

| Tür | Geçiren | $H(f)$ |
|-----|---------|--------|
| AGS (LPF) | $|f| \leq f_2$ | $k\,e^{-j2\pi ft_0}$ |
| BGS (BPF) | $f_2 \leq |f| \leq f_{\ddot{u}}$ | $k\,e^{-j2\pi ft_0}$ |
| YGF (HPF) | $|f| \geq f_2$ | $k\,e^{-j2\pi ft_0}$ |

**Bozulmasız iletim:** $|H(f)| = k$ sabit, $\angle H(f) = -2\pi ft_0$ doğrusal

---

## Soru Çözme Sırası

<svg width="492" height="332" viewBox="0 0 492 332" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ahfs" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <polygon points="246,12 376,52 246,92 116,52" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="246" y="57" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">İşaret periyodik mi?</text>
  <text x="100" y="82" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">Evet</text>
  <text x="380" y="44" text-anchor="start" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">Hayır</text>
  <line x1="116" y1="52" x2="92" y2="110" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ahfs)"/>
  <line x1="376" y1="52" x2="402" y2="110" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ahfs)"/>
  <rect x="15" y="112" width="155" height="72" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="92" y="132" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Fourier Serisi</text>
  <text x="92" y="149" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">cₙ katsayılarını hesapla</text>
  <text x="92" y="166" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">X(f) = Σ cₙ δ(f − n/T₀)</text>
  <rect x="322" y="112" width="158" height="48" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="401" y="132" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Fourier Dönüşümü</text>
  <text x="401" y="149" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">FT tablosu + özellikler</text>
  <line x1="401" y1="160" x2="308" y2="188" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ahfs)"/>
  <line x1="401" y1="160" x2="432" y2="188" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ahfs)"/>
  <rect x="238" y="190" width="130" height="44" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="303" y="209" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Zaman kaydırma?</text>
  <text x="303" y="225" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">× e^{−j2πft₀}</text>
  <rect x="372" y="190" width="110" height="44" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="427" y="209" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Modülasyon?</text>
  <text x="427" y="225" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">X(f ± fc) / 2</text>
  <line x1="92" y1="184" x2="92" y2="276" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ahfs)"/>
  <line x1="303" y1="234" x2="303" y2="276" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ahfs)"/>
  <line x1="427" y1="234" x2="427" y2="276" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ahfs)"/>
  <rect x="68" y="278" width="390" height="44" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="263" y="297" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">Genlik/Faz spektrumu çiz ✓</text>
  <text x="263" y="314" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#aac4e8">|X(f)| ve ∠X(f) grafiğini çiz</text>
</svg>
