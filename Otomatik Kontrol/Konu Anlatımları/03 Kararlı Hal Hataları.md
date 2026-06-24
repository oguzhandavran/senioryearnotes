---
tags: [otomatik-kontrol, kararlı-hal-hatası, hata-sabitleri, tip-sistemi, konu-anlatımı]
---

# 03 — Kararlı Hal Hataları

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/03 Kararlı Hal Hata Örnekleri]]

## Son Değer Teoremi ile Hata

Unity feedback kapalı çevrim:

$$E(s) = \frac{R(s)}{1 + G(s)}$$

Kararlı hal hatası:
$$e(\infty) = \lim_{s \to 0} s E(s) = \lim_{s \to 0} \frac{s\,R(s)}{1 + G(s)}$$

> [!warning] Koşul
> Son değer teoremi ancak sistem **kararlı** ise uygulanabilir!

---

## Hata Sabitleri

| Sabit | Formül | Kullanım |
|-------|--------|---------|
| $K_p$ (konum) | $\displaystyle K_p = \lim_{s\to 0} G(s)$ | Basamak girişi |
| $K_v$ (hız) | $\displaystyle K_v = \lim_{s\to 0} s\,G(s)$ | Rampa girişi |
| $K_a$ (ivme) | $\displaystyle K_a = \lim_{s\to 0} s^2 G(s)$ | Parabol girişi |

---

## Sistem Tipi ve Hata Tablosu

**Sistem Tipi:** Açık çevrim $G(s)$'deki orijin ($s=0$) kutup sayısı

$$G(s) = \frac{K\prod(s+z_i)}{s^N \prod(s+p_j)}$$

$N = $ sistem tipi

| Giriş | Tip 0 | Tip 1 | Tip 2 |
|-------|-------|-------|-------|
| Birim Basamak ($1/s$) | $\dfrac{1}{1+K_p}$ | **0** | **0** |
| Birim Rampa ($1/s^2$) | $\infty$ | $\dfrac{1}{K_v}$ | **0** |
| Birim Parabol ($1/s^3$) | $\infty$ | $\infty$ | $\dfrac{1}{K_a}$ |

<svg width="420" height="280" viewBox="0 0 420 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok03a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Top box: Giriş Türü? -->
  <rect x="145" y="10" width="130" height="32" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="210" y="31" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" fill="white">Giriş Türü?</text>
  <!-- Fan lines from center bottom (210,42) -->
  <line x1="210" y1="42" x2="70" y2="80" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <line x1="210" y1="42" x2="210" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <line x1="210" y1="42" x2="350" y2="80" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <!-- Col1: Basamak (center x=70) -->
  <rect x="10" y="80" width="120" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="70" y="99" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">Basamak</text>
  <line x1="70" y1="108" x2="70" y2="126" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <rect x="10" y="126" width="120" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="70" y="145" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">e_ss = 1/(1+K_p)</text>
  <line x1="70" y1="154" x2="70" y2="172" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <!-- Basamak sub-box 1: Tip 0 -->
  <rect x="5" y="172" width="130" height="26" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="70" y="189" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Tip 0: K_p sonlu</text>
  <line x1="70" y1="198" x2="70" y2="212" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <!-- Basamak sub-box 2: Tip≥1 -->
  <rect x="5" y="212" width="130" height="26" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="70" y="229" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Tip≥1: K_p=∞ → e_ss=0</text>
  <!-- Col2: Rampa (center x=210) -->
  <rect x="150" y="80" width="120" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="210" y="99" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">Rampa</text>
  <line x1="210" y1="108" x2="210" y2="126" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <rect x="150" y="126" width="120" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="210" y="145" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">e_ss = 1/K_v</text>
  <!-- Col3: Parabol (center x=350) -->
  <rect x="290" y="80" width="120" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="350" y="99" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">Parabol</text>
  <line x1="350" y1="108" x2="350" y2="126" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ok03a)"/>
  <rect x="290" y="126" width="120" height="28" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="350" y="145" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">e_ss = 1/K_a</text>
  <!-- Legend note -->
  <line x1="8" y1="256" x2="412" y2="256" stroke="#1a1a2e" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.3"/>
  <text x="210" y="272" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">K_p = lim G(s), K_v = lim s·G(s), K_a = lim s²·G(s)  (s→0)</text>
</svg>

---

## Bozucu Etkinin Yol Açtığı Hata

<svg width="500" height="215" viewBox="0 0 500 215" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok03b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- R(s) -->
  <text x="8" y="83" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">R(s)</text>
  <line x1="42" y1="79" x2="60" y2="79" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok03b)"/>
  <!-- Σ1 -->
  <circle cx="74" cy="79" r="12" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="74" y="75" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">+</text>
  <text x="70" y="86" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#c0392b">−</text>
  <line x1="86" y1="79" x2="108" y2="79" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok03b)"/>
  <!-- G1(s) box -->
  <rect x="108" y="63" width="76" height="32" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="146" y="84" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">G₁(s)</text>
  <line x1="184" y1="79" x2="218" y2="79" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok03b)"/>
  <!-- Σ2 -->
  <circle cx="232" cy="79" r="12" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="232" y="75" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">+</text>
  <text x="236" y="71" text-anchor="start" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">+</text>
  <!-- D(s) from above into Σ2 -->
  <text x="227" y="18" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#c0392b">D(s)</text>
  <line x1="232" y1="28" x2="232" y2="66" stroke="#c0392b" stroke-width="1.8" marker-end="url(#arr-ok03b)"/>
  <line x1="244" y1="79" x2="272" y2="79" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok03b)"/>
  <!-- G2(s) box -->
  <rect x="272" y="63" width="76" height="32" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="310" y="84" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">G₂(s)</text>
  <line x1="348" y1="79" x2="396" y2="79" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok03b)"/>
  <!-- C(s) -->
  <text x="399" y="83" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">C(s)</text>
  <!-- Branch point -->
  <circle cx="394" cy="79" r="3" fill="#1a1a2e"/>
  <!-- Feedback path -->
  <line x1="394" y1="79" x2="394" y2="140" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="394" y1="140" x2="74" y2="140" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="74" y1="140" x2="74" y2="91" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok03b)"/>
  <!-- Formula annotation -->
  <line x1="8" y1="160" x2="492" y2="160" stroke="#1a1a2e" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.3"/>
  <text x="250" y="180" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">e_D(∞) = −1 / [lim(1/G₂(s)) + lim G₁(s)]  (s→0)</text>
  <text x="250" y="200" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">G₁ yüksek kazançlı (entegratör) ise  |e_D(∞)| → 0</text>
</svg>

$$e(\infty) = e_R(\infty) + e_D(\infty)$$

Birim basamak bozucu $D(s) = 1/s$ için:

$$e_D(\infty) = -\frac{1}{\lim_{s\to 0}\frac{1}{G_2(s)} + \lim_{s\to 0}G_1(s)}$$

Eğer $G_1(s)$ yüksek kazançlı (entegratör) ise $e_D(\infty) \to 0$.

> [!sinav] Sınav İpucu
> - Sistem Tipi = paydada orijindeki kutup sayısı
> - Tip ≥ 1 → basamak hatası = 0
> - Tip ≥ 2 → rampa hatası = 0
> - Hata sıfır olmak için gerekli tip ile K aralığı çelişirse → "mümkün değil" de!
> - Son değer teoremi: sadece kararlı sistem için çalışır!

---

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/03 Kararlı Hal Hata Örnekleri]]
