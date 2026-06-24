---
tags: [otomatik-kontrol, bode, frekans-analizi, faz-payı, kazanç-payı, konu-anlatımı]
---

# 05 — Frekans Analizi ve Bode Diyagramı

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/05 Bode Diyagramı Örnekleri]]

## Frekans Yanıtı

$s = j\omega$ ile transfer fonksiyonu değerlendirilir:

$$G(j\omega) = |G(j\omega)| \angle G(j\omega)$$

**Bode diyagramı:**
- **Kazanç (dB):** $20\log_{10}|G(j\omega)|$ vs $\log_{10}(\omega)$
- **Faz (derece):** $\angle G(j\omega)$ vs $\log_{10}(\omega)$

---

## Bode Grafiği Temel Elemanlar

### 1. Sabit Kazanç $K$

| | Kazanç | Faz |
|-|--------|-----|
| Eğri | $20\log K$ dB (düz çizgi) | 0° (ya da 180°, $K<0$) |

### 2. İntegratör / Türevleyici $s^{\pm N}$

| | Kazanç Eğimi | Faz |
|-|-------------|-----|
| $1/s^N$ | $-20N$ dB/dekad | $-90N°$ |
| $s^N$ | $+20N$ dB/dekad | $+90N°$ |

### 3. Birinci Derece Faktör $(1 + s/\omega_1)$

| Frekans | Kazanç | Faz |
|---------|--------|-----|
| $\omega \ll \omega_1$ | 0 dB | 0° |
| $\omega = \omega_1$ | 3 dB | 45° |
| $\omega \gg \omega_1$ | $+20$ dB/dekad eğimi | 90° |

**Pay'da:** +20 dB/dekad, +90° faz artışı (sıfır)
**Payda'da:** -20 dB/dekad, -90° faz azalışı (kutup)

### 4. İkinci Derece Faktör (Kompleks Kutup)

$$\frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

| Frekans | Kazanç | Faz |
|---------|--------|-----|
| $\omega \ll \omega_n$ | 0 dB | 0° |
| $\omega = \omega_n$ | $-20\log(2\zeta)$ dB (rezonans) | -90° |
| $\omega \gg \omega_n$ | -40 dB/dekad | -180° |

---

## Faz Payı (PM) ve Kazanç Payı (GM)

<svg width="460" height="200" viewBox="0 0 460 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok05" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Header: Bode Diyagramı -->
  <rect x="140" y="10" width="180" height="32" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="230" y="31" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="white">Bode Diyagramı</text>
  <!-- Fan lines from bottom of header -->
  <line x1="230" y1="42" x2="115" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok05)"/>
  <line x1="230" y1="42" x2="345" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok05)"/>
  <!-- Left column: PM -->
  <rect x="10" y="80" width="210" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="115" y="98" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Kazanç Kesişim Frekansı ω_gc</text>
  <text x="115" y="114" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">|G(jω_gc)| = 0 dB</text>
  <line x1="115" y1="122" x2="115" y2="140" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok05)"/>
  <!-- PM result box (green tint) -->
  <rect x="10" y="142" width="210" height="40" rx="2" fill="#e8f5e9" stroke="#1a1a2e" stroke-width="2"/>
  <text x="115" y="158" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e">Faz Payı (PM)</text>
  <text x="115" y="175" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">PM = 180° + ∠G(jω_gc)</text>
  <!-- Right column: GM -->
  <rect x="240" y="80" width="210" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="345" y="98" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Faz Kesişim Frekansı ω_pc</text>
  <text x="345" y="114" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">∠G(jω_pc) = −180°</text>
  <line x1="345" y1="122" x2="345" y2="140" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok05)"/>
  <!-- GM result box (blue tint) -->
  <rect x="240" y="142" width="210" height="40" rx="2" fill="#e3f2fd" stroke="#1a1a2e" stroke-width="2"/>
  <text x="345" y="158" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e">Kazanç Payı (GM)</text>
  <text x="345" y="175" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">GM = −20 log|G(jω_pc)| dB</text>
</svg>

$$\text{PM} = 180° + \angle G(j\omega_{gc}) \quad \text{(kazanç kesişiminde)}$$

$$\text{GM} = -20\log_{10}|G(j\omega_{pc})| \text{ dB} \quad \text{(faz kesişiminde)}$$

**Kararlı sistem:** PM > 0 **ve** GM > 0

Tipik tasarım hedefleri: **PM ≈ 45°–60°**, **GM ≈ 6–20 dB**

---

## Sayısal Örnek — Hesaplanmış Bode Plot

$$G(s) = \frac{10}{s(s+1)(s+5)} \quad \text{[Tip 1, 3. derece]}$$

<svg width="520" height="322" viewBox="0 0 520 322" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-bode" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
    <clipPath id="clip-mag"><rect x="58" y="22" width="444" height="120"/></clipPath>
    <clipPath id="clip-ph"><rect x="58" y="180" width="444" height="120"/></clipPath>
  </defs>
  <text x="260" y="14" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10.5" font-weight="bold" fill="#1a1a2e">G(s) = 10 / [s(s+1)(s+5)]  —  Bode Diyagramı</text>
  <rect x="58" y="22" width="444" height="120" fill="#fafbff" stroke="#1a1a2e" stroke-width="1.2"/>
  <line x1="58" y1="39.1" x2="502" y2="39.1" stroke="#ccc" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="54" y="43.1" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">40</text>
  <line x1="58" y1="56.3" x2="502" y2="56.3" stroke="#ccc" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="54" y="60.3" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">20</text>
  <line x1="58" y1="73.4" x2="502" y2="73.4" stroke="#1a1a2e" stroke-width="0.9"/>
  <text x="54" y="77.4" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">0</text>
  <line x1="58" y1="90.6" x2="502" y2="90.6" stroke="#ccc" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="54" y="94.6" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">−20</text>
  <line x1="58" y1="107.7" x2="502" y2="107.7" stroke="#ccc" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="54" y="111.7" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">−40</text>
  <line x1="58" y1="124.9" x2="502" y2="124.9" stroke="#ccc" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="54" y="128.9" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">−60</text>
  <text x="10" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e" transform="rotate(-90,10,82)">dB</text>
  <rect x="58" y="180" width="444" height="120" fill="#fafbff" stroke="#1a1a2e" stroke-width="1.2"/>
  <line x1="58" y1="220.0" x2="502" y2="220.0" stroke="#ccc" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="54" y="224.0" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">−90°</text>
  <line x1="58" y1="260.0" x2="502" y2="260.0" stroke="#c0392b" stroke-width="0.9" stroke-dasharray="3,2"/>
  <text x="54" y="264.0" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">−180°</text>
  <line x1="58" y1="300.0" x2="502" y2="300.0" stroke="#ccc" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="54" y="304.0" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">−270°</text>
  <text x="10" y="244" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e" transform="rotate(-90,10,240)">faz (°)</text>
  <line x1="169.0" y1="22" x2="169.0" y2="300" stroke="#ddd" stroke-width="0.6" stroke-dasharray="2,3"/>
  <line x1="169.0" y1="142" x2="169.0" y2="146" stroke="#1a1a2e" stroke-width="1"/>
  <line x1="169.0" y1="300" x2="169.0" y2="304" stroke="#1a1a2e" stroke-width="1"/>
  <text x="169.0" y="314" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">0.1</text>
  <line x1="280.0" y1="22" x2="280.0" y2="300" stroke="#ddd" stroke-width="0.6" stroke-dasharray="2,3"/>
  <line x1="280.0" y1="142" x2="280.0" y2="146" stroke="#1a1a2e" stroke-width="1"/>
  <line x1="280.0" y1="300" x2="280.0" y2="304" stroke="#1a1a2e" stroke-width="1"/>
  <text x="280.0" y="314" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">1</text>
  <line x1="391.0" y1="22" x2="391.0" y2="300" stroke="#ddd" stroke-width="0.6" stroke-dasharray="2,3"/>
  <line x1="391.0" y1="142" x2="391.0" y2="146" stroke="#1a1a2e" stroke-width="1"/>
  <line x1="391.0" y1="300" x2="391.0" y2="304" stroke="#1a1a2e" stroke-width="1"/>
  <text x="391.0" y="314" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">10</text>
  <line x1="502.0" y1="22" x2="502.0" y2="300" stroke="#ddd" stroke-width="0.6" stroke-dasharray="2,3"/>
  <line x1="502.0" y1="142" x2="502.0" y2="146" stroke="#1a1a2e" stroke-width="1"/>
  <line x1="502.0" y1="300" x2="502.0" y2="304" stroke="#1a1a2e" stroke-width="1"/>
  <text x="502.0" y="314" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">100</text>
  <text x="290" y="322" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">&#969; (rad/s)</text>
  <path d="M58.0,34.0 L59.5,34.2 L61.0,34.4 L62.4,34.7 L63.9,34.9 L65.4,35.1 L66.9,35.4 L68.4,35.6 L69.9,35.8 L71.3,36.0 L72.8,36.3 L74.3,36.5 L75.8,36.7 L77.3,37.0 L78.8,37.2 L80.2,37.4 L81.7,37.6 L83.2,37.9 L84.7,38.1 L86.2,38.3 L87.6,38.6 L89.1,38.8 L90.6,39.0 L92.1,39.2 L93.6,39.5 L95.1,39.7 L96.5,39.9 L98.0,40.2 L99.5,40.4 L101.0,40.6 L102.5,40.9 L104.0,41.1 L105.4,41.3 L106.9,41.5 L108.4,41.8 L109.9,42.0 L111.4,42.2 L112.9,42.5 L114.3,42.7 L115.8,42.9 L117.3,43.1 L118.8,43.4 L120.3,43.6 L121.7,43.8 L123.2,44.1 L124.7,44.3 L126.2,44.5 L127.7,44.8 L129.2,45.0 L130.6,45.2 L132.1,45.4 L133.6,45.7 L135.1,45.9 L136.6,46.1 L138.1,46.4 L139.5,46.6 L141.0,46.8 L142.5,47.0 L144.0,47.3 L145.5,47.5 L146.9,47.7 L148.4,48.0 L149.9,48.2 L151.4,48.4 L152.9,48.7 L154.4,48.9 L155.8,49.1 L157.3,49.3 L158.8,49.6 L160.3,49.8 L161.8,50.0 L163.3,50.3 L164.7,50.5 L166.2,50.7 L167.7,51.0 L169.2,51.2 L170.7,51.4 L172.2,51.7 L173.6,51.9 L175.1,52.1 L176.6,52.4 L178.1,52.6 L179.6,52.8 L181.0,53.0 L182.5,53.3 L184.0,53.5 L185.5,53.7 L187.0,54.0 L188.5,54.2 L189.9,54.5 L191.4,54.7 L192.9,54.9 L194.4,55.2 L195.9,55.4 L197.4,55.6 L198.8,55.9 L200.3,56.1 L201.8,56.3 L203.3,56.6 L204.8,56.8 L206.2,57.1 L207.7,57.3 L209.2,57.5 L210.7,57.8 L212.2,58.0 L213.7,58.3 L215.1,58.5 L216.6,58.8 L218.1,59.0 L219.6,59.2 L221.1,59.5 L222.6,59.7 L224.0,60.0 L225.5,60.2 L227.0,60.5 L228.5,60.7 L230.0,61.0 L231.4,61.3 L232.9,61.5 L234.4,61.8 L235.9,62.0 L237.4,62.3 L238.9,62.6 L240.3,62.8 L241.8,63.1 L243.3,63.4 L244.8,63.6 L246.3,63.9 L247.8,64.2 L249.2,64.5 L250.7,64.8 L252.2,65.0 L253.7,65.3 L255.2,65.6 L256.7,65.9 L258.1,66.2 L259.6,66.5 L261.1,66.8 L262.6,67.1 L264.1,67.4 L265.5,67.7 L267.0,68.1 L268.5,68.4 L270.0,68.7 L271.5,69.0 L273.0,69.4 L274.4,69.7 L275.9,70.0 L277.4,70.4 L278.9,70.7 L280.4,71.1 L281.9,71.4 L283.3,71.8 L284.8,72.2 L286.3,72.5 L287.8,72.9 L289.3,73.3 L290.7,73.7 L292.2,74.0 L293.7,74.4 L295.2,74.8 L296.7,75.2 L298.2,75.6 L299.6,76.0 L301.1,76.4 L302.6,76.8 L304.1,77.3 L305.6,77.7 L307.1,78.1 L308.5,78.5 L310.0,79.0 L311.5,79.4 L313.0,79.8 L314.5,80.3 L315.9,80.7 L317.4,81.2 L318.9,81.6 L320.4,82.1 L321.9,82.6 L323.4,83.0 L324.8,83.5 L326.3,84.0 L327.8,84.5 L329.3,84.9 L330.8,85.4 L332.3,85.9 L333.7,86.4 L335.2,86.9 L336.7,87.4 L338.2,87.9 L339.7,88.4 L341.2,89.0 L342.6,89.5 L344.1,90.0 L345.6,90.5 L347.1,91.1 L348.6,91.6 L350.0,92.1 L351.5,92.7 L353.0,93.2 L354.5,93.8 L356.0,94.3 L357.5,94.9 L358.9,95.5 L360.4,96.0 L361.9,96.6 L363.4,97.2 L364.9,97.8 L366.4,98.4 L367.8,99.0 L369.3,99.5 L370.8,100.1 L372.3,100.7 L373.8,101.3 L375.2,101.9 L376.7,102.6 L378.2,103.2 L379.7,103.8 L381.2,104.4 L382.7,105.0 L384.1,105.7 L385.6,106.3 L387.1,106.9 L388.6,107.5 L390.1,108.2 L391.6,108.8 L393.0,109.5 L394.5,110.1 L396.0,110.8 L397.5,111.4 L399.0,112.0 L400.5,112.7 L401.9,113.4 L403.4,114.0 L404.9,114.7 L406.4,115.3 L407.9,116.0 L409.3,116.6 L410.8,117.3 L412.3,118.0 L413.8,118.6 L415.3,119.3 L416.8,120.0 L418.2,120.6 L419.7,121.3 L421.2,122.0 L422.7,122.6 L424.2,123.3 L425.7,124.0 L427.1,124.7 L428.6,125.3 L430.1,126.0 L431.6,126.7 L433.1,127.4 L434.5,128.0 L436.0,128.7 L437.5,129.4 L439.0,130.1 L440.5,130.8 L442.0,131.4 L443.4,132.1 L444.9,132.8 L446.4,133.5 L447.9,134.2 L449.4,134.8 L450.9,135.5 L452.3,136.2 L453.8,136.9 L455.3,137.6 L456.8,138.3 L458.3,138.9 L459.7,139.6 L461.2,140.3 L462.7,141.0 L464.2,141.7 L465.7,142.0 L467.2,142.0 L468.6,142.0 L470.1,142.0 L471.6,142.0 L473.1,142.0 L474.6,142.0 L476.1,142.0 L477.5,142.0 L479.0,142.0 L480.5,142.0 L482.0,142.0 L483.5,142.0 L485.0,142.0 L486.4,142.0 L487.9,142.0 L489.4,142.0 L490.9,142.0 L492.4,142.0 L493.8,142.0 L495.3,142.0 L496.8,142.0 L498.3,142.0 L499.8,142.0 L501.3,142.0" fill="none" stroke="#1a1a2e" stroke-width="2.2" clip-path="url(#clip-mag)"/>
  <path d="M58.0,220.3 L59.5,220.3 L61.0,220.3 L62.4,220.3 L63.9,220.3 L65.4,220.4 L66.9,220.4 L68.4,220.4 L69.9,220.4 L71.3,220.4 L72.8,220.4 L74.3,220.4 L75.8,220.4 L77.3,220.5 L78.8,220.5 L80.2,220.5 L81.7,220.5 L83.2,220.5 L84.7,220.5 L86.2,220.5 L87.6,220.6 L89.1,220.6 L90.6,220.6 L92.1,220.6 L93.6,220.6 L95.1,220.7 L96.5,220.7 L98.0,220.7 L99.5,220.7 L101.0,220.7 L102.5,220.8 L104.0,220.8 L105.4,220.8 L106.9,220.8 L108.4,220.9 L109.9,220.9 L111.4,220.9 L112.9,221.0 L114.3,221.0 L115.8,221.0 L117.3,221.0 L118.8,221.1 L120.3,221.1 L121.7,221.1 L123.2,221.2 L124.7,221.2 L126.2,221.3 L127.7,221.3 L129.2,221.3 L130.6,221.4 L132.1,221.4 L133.6,221.5 L135.1,221.5 L136.6,221.6 L138.1,221.6 L139.5,221.7 L141.0,221.7 L142.5,221.8 L144.0,221.8 L145.5,221.9 L146.9,221.9 L148.4,222.0 L149.9,222.1 L151.4,222.1 L152.9,222.2 L154.4,222.3 L155.8,222.3 L157.3,222.4 L158.8,222.5 L160.3,222.5 L161.8,222.6 L163.3,222.7 L164.7,222.8 L166.2,222.9 L167.7,223.0 L169.2,223.1 L170.7,223.2 L172.2,223.3 L173.6,223.4 L175.1,223.5 L176.6,223.6 L178.1,223.7 L179.6,223.8 L181.0,223.9 L182.5,224.0 L184.0,224.2 L185.5,224.3 L187.0,224.4 L188.5,224.5 L189.9,224.7 L191.4,224.8 L192.9,225.0 L194.4,225.1 L195.9,225.3 L197.4,225.5 L198.8,225.6 L200.3,225.8 L201.8,226.0 L203.3,226.2 L204.8,226.3 L206.2,226.5 L207.7,226.7 L209.2,226.9 L210.7,227.1 L212.2,227.4 L213.7,227.6 L215.1,227.8 L216.6,228.0 L218.1,228.3 L219.6,228.5 L221.1,228.8 L222.6,229.1 L224.0,229.3 L225.5,229.6 L227.0,229.9 L228.5,230.2 L230.0,230.5 L231.4,230.8 L232.9,231.1 L234.4,231.4 L235.9,231.7 L237.4,232.1 L238.9,232.4 L240.3,232.8 L241.8,233.1 L243.3,233.5 L244.8,233.9 L246.3,234.3 L247.8,234.7 L249.2,235.1 L250.7,235.5 L252.2,235.9 L253.7,236.3 L255.2,236.7 L256.7,237.2 L258.1,237.6 L259.6,238.1 L261.1,238.6 L262.6,239.0 L264.1,239.5 L265.5,240.0 L267.0,240.5 L268.5,241.0 L270.0,241.5 L271.5,242.0 L273.0,242.5 L274.4,243.0 L275.9,243.6 L277.4,244.1 L278.9,244.6 L280.4,245.2 L281.9,245.7 L283.3,246.3 L284.8,246.8 L286.3,247.4 L287.8,247.9 L289.3,248.5 L290.7,249.1 L292.2,249.6 L293.7,250.2 L295.2,250.8 L296.7,251.3 L298.2,251.9 L299.6,252.5 L301.1,253.1 L302.6,253.6 L304.1,254.2 L305.6,254.8 L307.1,255.4 L308.5,256.0 L310.0,256.5 L311.5,257.1 L313.0,257.7 L314.5,258.3 L315.9,258.9 L317.4,259.5 L318.9,180.0 L320.4,180.0 L321.9,180.0 L323.4,180.0 L324.8,180.0 L326.3,180.0 L327.8,180.0 L329.3,180.0 L330.8,180.0 L332.3,180.0 L333.7,180.0 L335.2,180.0 L336.7,180.0 L338.2,180.0 L339.7,180.0 L341.2,180.0 L342.6,180.0 L344.1,180.0 L345.6,180.0 L347.1,180.0 L348.6,180.0 L350.0,180.0 L351.5,180.0 L353.0,180.0 L354.5,180.0 L356.0,180.0 L357.5,180.0 L358.9,180.0 L360.4,180.0 L361.9,180.0 L363.4,180.0 L364.9,180.0 L366.4,180.0 L367.8,180.0 L369.3,180.0 L370.8,180.0 L372.3,180.0 L373.8,180.0 L375.2,180.0 L376.7,180.0 L378.2,180.0 L379.7,180.0 L381.2,180.0 L382.7,180.0 L384.1,180.0 L385.6,180.0 L387.1,180.0 L388.6,180.0 L390.1,180.0 L391.6,180.0 L393.0,180.0 L394.5,180.0 L396.0,180.0 L397.5,180.0 L399.0,180.0 L400.5,180.0 L401.9,180.0 L403.4,180.0 L404.9,180.0 L406.4,180.0 L407.9,180.0 L409.3,180.0 L410.8,180.0 L412.3,180.0 L413.8,180.0 L415.3,180.0 L416.8,180.0 L418.2,180.0 L419.7,180.0 L421.2,180.0 L422.7,180.0 L424.2,180.0 L425.7,180.0 L427.1,180.0 L428.6,180.0 L430.1,180.0 L431.6,180.0 L433.1,180.0 L434.5,180.0 L436.0,180.0 L437.5,180.0 L439.0,180.0 L440.5,180.0 L442.0,180.0 L443.4,180.0 L444.9,180.0 L446.4,180.0 L447.9,180.0 L449.4,180.0 L450.9,180.0 L452.3,180.0 L453.8,180.0 L455.3,180.0 L456.8,180.0 L458.3,180.0 L459.7,180.0 L461.2,180.0 L462.7,180.0 L464.2,180.0 L465.7,180.0 L467.2,180.0 L468.6,180.0 L470.1,180.0 L471.6,180.0 L473.1,180.0 L474.6,180.0 L476.1,180.0 L477.5,180.0 L479.0,180.0 L480.5,180.0 L482.0,180.0 L483.5,180.0 L485.0,180.0 L486.4,180.0 L487.9,180.0 L489.4,180.0 L490.9,180.0 L492.4,180.0 L493.8,180.0 L495.3,180.0 L496.8,180.0 L498.3,180.0 L499.8,180.0 L501.3,180.0" fill="none" stroke="#c0392b" stroke-width="2.2" clip-path="url(#clip-ph)"/>
  <line x1="290.0" y1="22" x2="290.0" y2="300" stroke="#2980b9" stroke-width="1" stroke-dasharray="4,3"/>
  <circle cx="290.0" cy="73.4" r="4" fill="#2980b9" stroke="white" stroke-width="1.2"/>
  <circle cx="290.0" cy="248.8" r="4" fill="#2980b9" stroke="white" stroke-width="1.2"/>
  <text x="293.0" y="30.0" font-family="Arial,sans-serif" font-size="8" fill="#2980b9">&#969;_gc=1.23</text>
  <line x1="290.0" y1="260.0" x2="290.0" y2="253.8" stroke="#2980b9" stroke-width="1.5" marker-end="url(#arr-bode)"/>
  <text x="294.0" y="258.4" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="#2980b9">PM=25°</text>
  <line x1="318.2" y1="22" x2="318.2" y2="300" stroke="#27ae60" stroke-width="1" stroke-dasharray="4,3"/>
  <circle cx="318.2" cy="81.4" r="4" fill="#27ae60" stroke="white" stroke-width="1.2"/>
  <circle cx="318.2" cy="260.0" r="4" fill="#27ae60" stroke="white" stroke-width="1.2"/>
  <text x="321.2" y="30.0" font-family="Arial,sans-serif" font-size="8" fill="#27ae60">&#969;_pc=2.21</text>
  <line x1="318.2" y1="73.4" x2="318.2" y2="86.4" stroke="#27ae60" stroke-width="1.5" marker-end="url(#arr-bode)"/>
  <text x="322.2" y="81.4" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="#27ae60">GM=9.3dB</text>
</svg>

> [!info] Okuma Kılavuzu
> - **Mavi kesikli** → ω_gc = 1.23 rad/s (kazanç kesişimi, |G|=0 dB). PM = **25°** (yetersiz — tasarım hedefi ≥ 45°)
> - **Yeşil kesikli** → ω_pc = 2.21 rad/s (faz kesişimi, ∠G=−180°). GM = **9.3 dB** (kabul edilebilir)
> - **Kırmızı yatay** → −180° sınırı (kararlılık sınırı)
> - **Sonuç:** Bu sistem PM açısından sınırda kararlı — Lead kompansatör ile PM artırılabilir.

---

## Tipik Bode Çizim Prosedürü

**Adım 1:** $G(s)$'i standart biçime getir

$$G(s) = \frac{K\prod(1 + s/z_i)}{s^N \prod(1 + s/p_j)}$$

**Adım 2:** Kazanç diyagramı
1. Düşük frekansta: $20\log K$'dan başla, $-20N$ dB/dekad eğimi
2. Her sıfırda ($\omega = z_i$): eğim +20 dB/dekad artır
3. Her kutupda ($\omega = p_j$): eğim -20 dB/dekad azalt

**Adım 3:** Faz diyagramı
- Frekans on katı değiştiğinde faz değişimi tamamlanır
- $\omega_c/10$ ile $10\omega_c$ arasında lineer geçiş varsay

---

## Frekans-Alan ve Zaman-Alan İlişkileri

| Zaman Alan | Frekans Alan |
|-----------|-------------|
| $T_s \approx 4/(\zeta\omega_n)$ | $\omega_{gc} \approx \omega_n\sqrt{1-2\zeta^2}$ |
| $\%OS \leftrightarrow \zeta$ | $PM \approx 100\zeta$ (küçük $\zeta$ için) |
| Hız yanıtı | Bant genişliği $\omega_{BW}$ |

## Kapalı Çevrim ↔ Bode İlişkileri

| Zaman Alan | Frekans Alan Karşılığı |
|-----------|----------------------|
| $\%OS$ azalt | $PM$ artır → $\zeta$ artır |
| $T_s$ azalt | $\omega_{gc}$ artır |
| Kararlılık | $PM > 0$, $GM > 0$ |
| Faz payı ≈ | $PM \approx 100\zeta$ (kaba tahmin) |

---

> [!sinav] Sınav İpucu
> - Kazanç payı = kutup > sıfır frekansında kazanç
> - Faz payı = kazanç = 0 dB noktasındaki faz marjı
> - PM > 0 → kararlı; PM < 0 → kararsız
> - Birinci derece kutup: kesim frekansında -45°, on kat sonra -90°
> - İntegratör: Bode başlangıcını -20 dB/dekad yapar, başlangıç fazı -90°

---

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/05 Bode Diyagramı Örnekleri]]
