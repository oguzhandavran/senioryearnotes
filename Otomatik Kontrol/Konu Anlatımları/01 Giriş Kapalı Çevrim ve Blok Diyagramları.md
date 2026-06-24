---
tags: [otomatik-kontrol, blok-diyagram, mason, transfer-fonksiyonu, konu-anlatımı]
---

# 01 — Giriş, Kapalı Çevrim ve Blok Diyagramlar

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/01 Blok Diyagram Örnekleri]]

## Temel Tanımlar

> [!tanim] Otomatik Kontrol
> Kontrol için gerekli tüm işlemlerin bir algoritma ile insana gerek duyulmadan gerçekleştirilmesi.

<svg width="488" height="258" viewBox="0 0 488 258" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok01a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <text x="244" y="18" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e" letter-spacing="2">AÇIK ÇEVRİM</text>
  <text x="10" y="65" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">R(s)</text>
  <line x1="44" y1="61" x2="74" y2="61" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <rect x="74" y="45" width="90" height="32" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="119" y="66" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">Kontrolör</text>
  <line x1="164" y1="61" x2="196" y2="61" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <rect x="196" y="45" width="68" height="32" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="230" y="66" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">G(s)</text>
  <line x1="264" y1="61" x2="300" y2="61" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <text x="303" y="65" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">C(s)</text>
  <line x1="8" y1="96" x2="480" y2="96" stroke="#1a1a2e" stroke-width="1" stroke-dasharray="5,4" opacity="0.3"/>
  <text x="244" y="114" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e" letter-spacing="2">KAPALI ÇEVRİM</text>
  <text x="10" y="174" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">R(s)</text>
  <line x1="44" y1="170" x2="62" y2="170" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <circle cx="76" cy="170" r="12" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="76" y="166" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">+</text>
  <text x="72" y="177" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#c0392b">−</text>
  <line x1="88" y1="170" x2="110" y2="170" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <rect x="110" y="154" width="90" height="32" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="155" y="175" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">Kontrolör</text>
  <line x1="200" y1="170" x2="232" y2="170" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <rect x="232" y="154" width="68" height="32" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="266" y="175" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">G(s)</text>
  <line x1="300" y1="170" x2="340" y2="170" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <text x="343" y="174" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">C(s)</text>
  <circle cx="338" cy="170" r="3" fill="#1a1a2e"/>
  <line x1="338" y1="170" x2="338" y2="222" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="338" y1="222" x2="282" y2="222" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
  <rect x="212" y="208" width="70" height="28" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="247" y="227" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">H(s)</text>
  <line x1="212" y1="222" x2="76" y2="222" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="76" y1="222" x2="76" y2="182" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01a)"/>
</svg>

| Özellik | Açık Çevrim | Kapalı Çevrim |
|---------|------------|--------------|
| Geri besleme | Yok | Var |
| Bozucu etki | Düzeltemez | Düzeltebilir |
| Karmaşıklık | Basit | Karmaşık |
| Kararlılık | Her zaman kararlı | Tasarıma bağlı |

---

## Transfer Fonksiyonu

Doğrusal, zamanla değişmeyen (LTI) n. dereceden sistem:

$$a_n y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_0 y = b_m u^{(m)} + \cdots + b_0 u$$

Başlangıç şartları sıfır → Laplace dönüşümü:

$$G(s) = \frac{Y(s)}{U(s)} = \frac{b_m s^m + \cdots + b_0}{a_n s^n + \cdots + a_0}$$

> [!warning] Koşul
> Fiziksel sistemlerde $m \leq n$ (düzgün sistem)

---

## Blok Diyagram Kuralları

### Temel Bağlantılar

| Bağlantı | Kural | Transfer Fonksiyonu |
|---------|-------|-------------------|
| Seri (Kaskad) | $G_1 \to G_2$ | $G_1(s) \cdot G_2(s)$ |
| Paralel | $G_1 \parallel G_2$ | $G_1(s) \pm G_2(s)$ |
| **Kapalı Çevrim (negatif)** | $G$ + H geri besleme | $\dfrac{G(s)}{1 + G(s)H(s)}$ |
| Kapalı Çevrim (pozitif) | $G$ + H geri besleme | $\dfrac{G(s)}{1 - G(s)H(s)}$ |

### Öteleme Kuralları

<svg width="460" height="185" viewBox="0 0 460 185" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok01b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <text x="8" y="62" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">R(s)</text>
  <line x1="42" y1="58" x2="60" y2="58" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01b)"/>
  <circle cx="74" cy="58" r="12" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="74" y="54" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">+</text>
  <text x="70" y="65" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#c0392b">−</text>
  <text x="92" y="50" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">E(s)</text>
  <line x1="86" y1="58" x2="130" y2="58" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01b)"/>
  <rect x="130" y="42" width="80" height="32" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="63" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">G(s)</text>
  <line x1="210" y1="58" x2="258" y2="58" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01b)"/>
  <text x="261" y="62" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">C(s)</text>
  <circle cx="258" cy="58" r="3" fill="#1a1a2e"/>
  <line x1="258" y1="58" x2="258" y2="108" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="258" y1="108" x2="200" y2="108" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01b)"/>
  <rect x="120" y="94" width="80" height="28" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="160" y="113" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="14" font-style="italic" fill="#1a1a2e">H(s)</text>
  <line x1="120" y1="108" x2="74" y2="108" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="74" y1="108" x2="74" y2="70" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01b)"/>
  <line x1="8" y1="138" x2="452" y2="138" stroke="#1a1a2e" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.3"/>
  <text x="230" y="158" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">G_CL(s) = G(s) / [1 + G(s)H(s)]</text>
  <text x="230" y="176" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">H(s) = 1 (unity geri besleme)  →  G(s) / [1 + G(s)]</text>
</svg>

| Hareket | Kural |
|---------|-------|
| Toplama noktasını G'nin önüne al | G'nin tersini ekle: $1/G$ |
| Toplama noktasını G'nin arkasına al | G'yi ekle |
| Dağılma noktasını G'nin önüne al | G'yi çıkar |
| Dağılma noktasını G'nin arkasına al | $1/G$'yi çıkar |

---

## Mason Kazanç Formülü

$$\frac{Y(s)}{R(s)} = \frac{\sum_k P_k \Delta_k}{\Delta}$$

**Terimler:**
- $P_k$: $k$. ileri yolun kazancı
- $\Delta = 1 - \sum L_i + \sum L_i L_j - \sum L_i L_j L_k + \cdots$ (determinant)
- $\Delta_k$: $k$. ileri yolun determinantı (o yol ile temas etmeyen döngüler)

### Mason Adımları

<svg width="340" height="390" viewBox="0 0 340 390" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ok01c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <rect x="30" y="15" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="37" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">1. İşaret akış diyagramını çiz</text>
  <line x1="170" y1="49" x2="170" y2="67" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01c)"/>
  <rect x="30" y="69" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="91" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">2. İleri yolları bul: P_k</text>
  <line x1="170" y1="103" x2="170" y2="121" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01c)"/>
  <rect x="30" y="123" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="145" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">3. Tüm döngü kazançlarını bul: L_i</text>
  <line x1="170" y1="157" x2="170" y2="175" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01c)"/>
  <rect x="30" y="177" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="199" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">4. Temassız döngü çiftleri: L_i · L_j</text>
  <line x1="170" y1="211" x2="170" y2="229" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01c)"/>
  <rect x="30" y="231" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="253" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">5. Δ = 1 − ΣL_i + ΣL_iL_j − …</text>
  <line x1="170" y1="265" x2="170" y2="283" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01c)"/>
  <rect x="30" y="285" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="307" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">6. Her ileri yol için Δ_k hesapla</text>
  <line x1="170" y1="319" x2="170" y2="337" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ok01c)"/>
  <rect x="30" y="339" width="280" height="34" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="361" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="white">7. T = ΣP_k Δ_k / Δ</text>
</svg>

---

## Geçici Yanıt Parametreleri (2. Derece Sistem)

$$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

| Parametre | Formül | Açıklama |
|-----------|--------|---------|
| $T_r$ (yükselme süresi) | $\approx \dfrac{1.8}{\omega_n}$ | %0 → %100 |
| $T_p$ (tepe süresi) | $\dfrac{\pi}{\omega_d}$, $\omega_d=\omega_n\sqrt{1-\zeta^2}$ | İlk tepe |
| $T_s$ (yerleşme süresi) | $\dfrac{4}{\zeta\omega_n}$ (%2 kriteri) | |
| $\%OS$ (aşım) | $100 e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ | |
| $\zeta$ (sönüm oranı) | $\zeta = \cos\theta$ | $\theta$: kutup açısı |

> [!sinav] Sınav Tüyosu
> - $\%OS \leftrightarrow \zeta$: Aşım verilince $\zeta = \dfrac{-\ln(\%OS/100)}{\sqrt{\pi^2 + \ln^2(\%OS/100)}}$
> - $\zeta\omega_n$ sabit ise $T_s$ sabit kalır!
> - Baskın kutuplar: Gerçek kısmı diğerlerinin en az 5 katı olan kutuplar ihmal edilir.

### Birim Adım Yanıtı — Sönüm Oranı Karşılaştırması

<svg width="480" height="280" viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg">
  <rect x="50" y="20" width="410" height="220" fill="#fafbff" stroke="#1a1a2e" stroke-width="1.2"/>
  <line x1="50" y1="227.8" x2="460" y2="227.8" stroke="#ddd" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="46" y="231.8" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">0</text>
  <line x1="50" y1="166.7" x2="460" y2="166.7" stroke="#ddd" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="46" y="170.7" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">0.5</text>
  <line x1="50" y1="105.6" x2="460" y2="105.6" stroke="#1a1a2e" stroke-width="0.8"/>
  <text x="46" y="109.6" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">1.0</text>
  <line x1="50" y1="44.4" x2="460" y2="44.4" stroke="#ddd" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="46" y="48.4" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#555">1.5</text>
  <line x1="141.1" y1="20" x2="141.1" y2="240" stroke="#ddd" stroke-width="0.6" stroke-dasharray="3,3"/>
  <line x1="141.1" y1="240" x2="141.1" y2="244" stroke="#1a1a2e" stroke-width="1"/>
  <text x="141.1" y="254" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">1</text>
  <line x1="232.2" y1="20" x2="232.2" y2="240" stroke="#ddd" stroke-width="0.6" stroke-dasharray="3,3"/>
  <line x1="232.2" y1="240" x2="232.2" y2="244" stroke="#1a1a2e" stroke-width="1"/>
  <text x="232.2" y="254" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">2</text>
  <line x1="323.3" y1="20" x2="323.3" y2="240" stroke="#ddd" stroke-width="0.6" stroke-dasharray="3,3"/>
  <line x1="323.3" y1="240" x2="323.3" y2="244" stroke="#1a1a2e" stroke-width="1"/>
  <text x="323.3" y="254" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">3</text>
  <line x1="414.4" y1="20" x2="414.4" y2="240" stroke="#ddd" stroke-width="0.6" stroke-dasharray="3,3"/>
  <line x1="414.4" y1="240" x2="414.4" y2="244" stroke="#1a1a2e" stroke-width="1"/>
  <text x="414.4" y="254" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">4</text>
  <text x="255" y="278" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">t (s)   [&#969;_n = 5 rad/s]</text>
  <text x="10" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e" transform="rotate(-90,10,130)">y(t)</text>
  <text x="255" y="14" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-weight="bold" fill="#1a1a2e">Birim Ad&#305;m Yan&#305;t&#305; — &#969;_n=5 rad/s</text>
  <defs><clipPath id="clip-step"><rect x="50" y="20" width="410" height="220"/></clipPath></defs>
  <path d="M50.0,227.8 L52.1,227.0 L54.1,224.8 L56.2,221.2 L58.2,216.3 L60.3,210.2 L62.3,203.1 L64.4,195.1 L66.4,186.4 L68.5,177.0 L70.6,167.2 L72.6,157.0 L74.7,146.6 L76.7,136.2 L78.8,125.9 L80.8,115.7 L82.9,105.9 L84.9,96.5 L87.0,87.7 L89.0,79.4 L91.1,71.9 L93.2,65.1 L95.2,59.1 L97.3,53.9 L99.3,49.6 L101.4,46.2 L103.4,43.7 L105.5,42.0 L107.5,41.3 L109.6,41.3 L111.7,42.2 L113.7,43.8 L115.8,46.1 L117.8,49.0 L119.9,52.5 L121.9,56.5 L124.0,61.0 L126.0,65.8 L128.1,70.9 L130.2,76.2 L132.2,81.6 L134.3,87.1 L136.3,92.5 L138.4,97.9 L140.4,103.2 L142.5,108.2 L144.5,113.0 L146.6,117.5 L148.6,121.6 L150.7,125.4 L152.8,128.7 L154.8,131.6 L156.9,134.1 L158.9,136.1 L161.0,137.6 L163.0,138.7 L165.1,139.3 L167.1,139.4 L169.2,139.2 L171.3,138.5 L173.3,137.4 L175.4,136.0 L177.4,134.3 L179.5,132.3 L181.5,130.1 L183.6,127.6 L185.6,125.0 L187.7,122.2 L189.7,119.4 L191.8,116.5 L193.9,113.6 L195.9,110.8 L198.0,108.0 L200.0,105.3 L202.1,102.7 L204.1,100.3 L206.2,98.0 L208.2,95.9 L210.3,94.1 L212.4,92.4 L214.4,91.0 L216.5,89.9 L218.5,89.0 L220.6,88.3 L222.6,87.9 L224.7,87.7 L226.7,87.8 L228.8,88.0 L230.9,88.5 L232.9,89.2 L235.0,90.0 L237.0,91.0 L239.1,92.1 L241.1,93.4 L243.2,94.7 L245.2,96.1 L247.3,97.6 L249.3,99.1 L251.4,100.6 L253.5,102.2 L255.5,103.6 L257.6,105.1 L259.6,106.5 L261.7,107.8 L263.7,109.0 L265.8,110.2 L267.8,111.2 L269.9,112.1 L272.0,112.9 L274.0,113.6 L276.1,114.1 L278.1,114.5 L280.2,114.8 L282.2,114.9 L284.3,115.0 L286.3,114.9 L288.4,114.7 L290.5,114.3 L292.5,113.9 L294.6,113.5 L296.6,112.9 L298.7,112.3 L300.7,111.6 L302.8,110.8 L304.8,110.1 L306.9,109.3 L308.9,108.5 L311.0,107.7 L313.1,106.9 L315.1,106.1 L317.2,105.4 L319.2,104.7 L321.3,104.0 L323.3,103.4 L325.4,102.8 L327.4,102.3 L329.5,101.9 L331.6,101.5 L333.6,101.2 L335.7,100.9 L337.7,100.8 L339.8,100.6 L341.8,100.6 L343.9,100.6 L345.9,100.7 L348.0,100.8 L350.1,101.0 L352.1,101.3 L354.2,101.6 L356.2,101.9 L358.3,102.2 L360.3,102.6 L362.4,103.0 L364.4,103.4 L366.5,103.8 L368.5,104.3 L370.6,104.7 L372.7,105.1 L374.7,105.5 L376.8,105.9 L378.8,106.2 L380.9,106.6 L382.9,106.9 L385.0,107.2 L387.0,107.4 L389.1,107.6 L391.2,107.8 L393.2,107.9 L395.3,108.0 L397.3,108.1 L399.4,108.2 L401.4,108.2 L403.5,108.1 L405.5,108.1 L407.6,108.0 L409.6,107.9 L411.7,107.7 L413.8,107.6 L415.8,107.4 L417.9,107.2 L419.9,107.0 L422.0,106.8 L424.0,106.6 L426.1,106.3 L428.1,106.1 L430.2,105.9 L432.3,105.7 L434.3,105.5 L436.4,105.3 L438.4,105.1 L440.5,104.9 L442.5,104.8 L444.6,104.6 L446.6,104.5 L448.7,104.4 L450.8,104.3 L452.8,104.3 L454.9,104.2 L456.9,104.2 L459.0,104.2" fill="none" stroke="#c0392b" stroke-width="2" clip-path="url(#clip-step)"/>
  <path d="M50.0,227.8 L52.1,227.0 L54.1,224.9 L56.2,221.6 L58.2,217.2 L60.3,211.9 L62.3,206.0 L64.4,199.4 L66.4,192.5 L68.5,185.2 L70.6,177.8 L72.6,170.2 L74.7,162.7 L76.7,155.3 L78.8,148.1 L80.8,141.2 L82.9,134.6 L84.9,128.3 L87.0,122.4 L89.0,117.0 L91.1,112.0 L93.2,107.4 L95.2,103.3 L97.3,99.7 L99.3,96.5 L101.4,93.8 L103.4,91.5 L105.5,89.7 L107.5,88.2 L109.6,87.0 L111.7,86.3 L113.7,85.8 L115.8,85.6 L117.8,85.7 L119.9,86.0 L121.9,86.5 L124.0,87.2 L126.0,88.1 L128.1,89.0 L130.2,90.1 L132.2,91.2 L134.3,92.4 L136.3,93.6 L138.4,94.8 L140.4,96.0 L142.5,97.2 L144.5,98.4 L146.6,99.6 L148.6,100.6 L150.7,101.7 L152.8,102.7 L154.8,103.6 L156.9,104.4 L158.9,105.1 L161.0,105.8 L163.0,106.4 L165.1,106.9 L167.1,107.4 L169.2,107.8 L171.3,108.1 L173.3,108.4 L175.4,108.5 L177.4,108.7 L179.5,108.8 L181.5,108.8 L183.6,108.8 L185.6,108.8 L187.7,108.7 L189.7,108.6 L191.8,108.4 L193.9,108.3 L195.9,108.1 L198.0,107.9 L200.0,107.7 L202.1,107.5 L204.1,107.3 L206.2,107.1 L208.2,106.9 L210.3,106.7 L212.4,106.6 L214.4,106.4 L216.5,106.2 L218.5,106.1 L220.6,105.9 L222.6,105.8 L224.7,105.6 L226.7,105.5 L228.8,105.4 L230.9,105.3 L232.9,105.3 L235.0,105.2 L237.0,105.1 L239.1,105.1 L241.1,105.1 L243.2,105.0 L245.2,105.0 L247.3,105.0 L249.3,105.0 L251.4,105.0 L253.5,105.0 L255.5,105.1 L257.6,105.1 L259.6,105.1 L261.7,105.1 L263.7,105.2 L265.8,105.2 L267.8,105.2 L269.9,105.3 L272.0,105.3 L274.0,105.3 L276.1,105.4 L278.1,105.4 L280.2,105.4 L282.2,105.4 L284.3,105.5 L286.3,105.5 L288.4,105.5 L290.5,105.5 L292.5,105.6 L294.6,105.6 L296.6,105.6 L298.7,105.6 L300.7,105.6 L302.8,105.6 L304.8,105.6 L306.9,105.6 L308.9,105.6 L311.0,105.6 L313.1,105.6 L315.1,105.6 L317.2,105.6 L319.2,105.6 L321.3,105.6 L323.3,105.6 L325.4,105.6 L327.4,105.6 L329.5,105.6 L331.6,105.6 L333.6,105.6 L335.7,105.6 L337.7,105.6 L339.8,105.6 L341.8,105.6 L343.9,105.6 L345.9,105.6 L348.0,105.6 L350.1,105.6 L352.1,105.6 L354.2,105.6 L356.2,105.6 L358.3,105.6 L360.3,105.6 L362.4,105.6 L364.4,105.5 L366.5,105.5 L368.5,105.5 L370.6,105.5 L372.7,105.5 L374.7,105.5 L376.8,105.5 L378.8,105.5 L380.9,105.5 L382.9,105.5 L385.0,105.5 L387.0,105.5 L389.1,105.5 L391.2,105.5 L393.2,105.5 L395.3,105.5 L397.3,105.5 L399.4,105.5 L401.4,105.5 L403.5,105.5 L405.5,105.5 L407.6,105.5 L409.6,105.6 L411.7,105.6 L413.8,105.6 L415.8,105.6 L417.9,105.6 L419.9,105.6 L422.0,105.6 L424.0,105.6 L426.1,105.6 L428.1,105.6 L430.2,105.6 L432.3,105.6 L434.3,105.6 L436.4,105.6 L438.4,105.6 L440.5,105.6 L442.5,105.6 L444.6,105.6 L446.6,105.6 L448.7,105.6 L450.8,105.6 L452.8,105.6 L454.9,105.6 L456.9,105.6 L459.0,105.6" fill="none" stroke="#e67e22" stroke-width="2" clip-path="url(#clip-step)"/>
  <path d="M50.0,227.8 L52.1,227.0 L54.1,225.0 L56.2,221.8 L58.2,217.8 L60.3,213.0 L62.3,207.6 L64.4,201.8 L66.4,195.8 L68.5,189.5 L70.6,183.2 L72.6,176.9 L74.7,170.7 L76.7,164.6 L78.8,158.7 L80.8,153.1 L82.9,147.7 L84.9,142.6 L87.0,137.8 L89.0,133.4 L91.1,129.2 L93.2,125.4 L95.2,121.9 L97.3,118.8 L99.3,115.9 L101.4,113.3 L103.4,111.0 L105.5,109.0 L107.5,107.3 L109.6,105.7 L111.7,104.4 L113.7,103.3 L115.8,102.4 L117.8,101.7 L119.9,101.1 L121.9,100.6 L124.0,100.3 L126.0,100.1 L128.1,100.0 L130.2,99.9 L132.2,100.0 L134.3,100.1 L136.3,100.2 L138.4,100.4 L140.4,100.6 L142.5,100.9 L144.5,101.1 L146.6,101.4 L148.6,101.7 L150.7,102.0 L152.8,102.3 L154.8,102.6 L156.9,102.8 L158.9,103.1 L161.0,103.4 L163.0,103.6 L165.1,103.8 L167.1,104.1 L169.2,104.3 L171.3,104.5 L173.3,104.6 L175.4,104.8 L177.4,104.9 L179.5,105.1 L181.5,105.2 L183.6,105.3 L185.6,105.4 L187.7,105.5 L189.7,105.5 L191.8,105.6 L193.9,105.7 L195.9,105.7 L198.0,105.7 L200.0,105.8 L202.1,105.8 L204.1,105.8 L206.2,105.8 L208.2,105.8 L210.3,105.8 L212.4,105.8 L214.4,105.8 L216.5,105.8 L218.5,105.8 L220.6,105.8 L222.6,105.8 L224.7,105.8 L226.7,105.7 L228.8,105.7 L230.9,105.7 L232.9,105.7 L235.0,105.7 L237.0,105.7 L239.1,105.7 L241.1,105.7 L243.2,105.6 L245.2,105.6 L247.3,105.6 L249.3,105.6 L251.4,105.6 L253.5,105.6 L255.5,105.6 L257.6,105.6 L259.6,105.6 L261.7,105.6 L263.7,105.6 L265.8,105.6 L267.8,105.6 L269.9,105.6 L272.0,105.6 L274.0,105.6 L276.1,105.5 L278.1,105.5 L280.2,105.5 L282.2,105.5 L284.3,105.5 L286.3,105.5 L288.4,105.5 L290.5,105.5 L292.5,105.5 L294.6,105.5 L296.6,105.5 L298.7,105.5 L300.7,105.5 L302.8,105.5 L304.8,105.5 L306.9,105.5 L308.9,105.5 L311.0,105.5 L313.1,105.5 L315.1,105.5 L317.2,105.5 L319.2,105.6 L321.3,105.6 L323.3,105.6 L325.4,105.6 L327.4,105.6 L329.5,105.6 L331.6,105.6 L333.6,105.6 L335.7,105.6 L337.7,105.6 L339.8,105.6 L341.8,105.6 L343.9,105.6 L345.9,105.6 L348.0,105.6 L350.1,105.6 L352.1,105.6 L354.2,105.6 L356.2,105.6 L358.3,105.6 L360.3,105.6 L362.4,105.6 L364.4,105.6 L366.5,105.6 L368.5,105.6 L370.6,105.6 L372.7,105.6 L374.7,105.6 L376.8,105.6 L378.8,105.6 L380.9,105.6 L382.9,105.6 L385.0,105.6 L387.0,105.6 L389.1,105.6 L391.2,105.6 L393.2,105.6 L395.3,105.6 L397.3,105.6 L399.4,105.6 L401.4,105.6 L403.5,105.6 L405.5,105.6 L407.6,105.6 L409.6,105.6 L411.7,105.6 L413.8,105.6 L415.8,105.6 L417.9,105.6 L419.9,105.6 L422.0,105.6 L424.0,105.6 L426.1,105.6 L428.1,105.6 L430.2,105.6 L432.3,105.6 L434.3,105.6 L436.4,105.6 L438.4,105.6 L440.5,105.6 L442.5,105.6 L444.6,105.6 L446.6,105.6 L448.7,105.6 L450.8,105.6 L452.8,105.6 L454.9,105.6 L456.9,105.6 L459.0,105.6" fill="none" stroke="#2980b9" stroke-width="2" clip-path="url(#clip-step)"/>
  <path d="M50.0,227.8 L52.1,227.1 L54.1,225.1 L56.2,222.2 L58.2,218.5 L60.3,214.3 L62.3,209.7 L64.4,204.9 L66.4,199.9 L68.5,194.8 L70.6,189.7 L72.6,184.8 L74.7,179.9 L76.7,175.1 L78.8,170.5 L80.8,166.2 L82.9,162.0 L84.9,158.0 L87.0,154.2 L89.0,150.6 L91.1,147.3 L93.2,144.1 L95.2,141.1 L97.3,138.4 L99.3,135.8 L101.4,133.4 L103.4,131.2 L105.5,129.1 L107.5,127.2 L109.6,125.4 L111.7,123.7 L113.7,122.2 L115.8,120.8 L117.8,119.5 L119.9,118.3 L121.9,117.2 L124.0,116.2 L126.0,115.3 L128.1,114.4 L130.2,113.7 L132.2,113.0 L134.3,112.3 L136.3,111.7 L138.4,111.2 L140.4,110.7 L142.5,110.2 L144.5,109.8 L146.6,109.4 L148.6,109.0 L150.7,108.7 L152.8,108.4 L154.8,108.2 L156.9,107.9 L158.9,107.7 L161.0,107.5 L163.0,107.3 L165.1,107.2 L167.1,107.0 L169.2,106.9 L171.3,106.8 L173.3,106.6 L175.4,106.5 L177.4,106.5 L179.5,106.4 L181.5,106.3 L183.6,106.2 L185.6,106.2 L187.7,106.1 L189.7,106.1 L191.8,106.0 L193.9,106.0 L195.9,105.9 L198.0,105.9 L200.0,105.9 L202.1,105.8 L204.1,105.8 L206.2,105.8 L208.2,105.8 L210.3,105.7 L212.4,105.7 L214.4,105.7 L216.5,105.7 L218.5,105.7 L220.6,105.7 L222.6,105.7 L224.7,105.6 L226.7,105.6 L228.8,105.6 L230.9,105.6 L232.9,105.6 L235.0,105.6 L237.0,105.6 L239.1,105.6 L241.1,105.6 L243.2,105.6 L245.2,105.6 L247.3,105.6 L249.3,105.6 L251.4,105.6 L253.5,105.6 L255.5,105.6 L257.6,105.6 L259.6,105.6 L261.7,105.6 L263.7,105.6 L265.8,105.6 L267.8,105.6 L269.9,105.6 L272.0,105.6 L274.0,105.6 L276.1,105.6 L278.1,105.6 L280.2,105.6 L282.2,105.6 L284.3,105.6 L286.3,105.6 L288.4,105.6 L290.5,105.6 L292.5,105.6 L294.6,105.6 L296.6,105.6 L298.7,105.6 L300.7,105.6 L302.8,105.6 L304.8,105.6 L306.9,105.6 L308.9,105.6 L311.0,105.6 L313.1,105.6 L315.1,105.6 L317.2,105.6 L319.2,105.6 L321.3,105.6 L323.3,105.6 L325.4,105.6 L327.4,105.6 L329.5,105.6 L331.6,105.6 L333.6,105.6 L335.7,105.6 L337.7,105.6 L339.8,105.6 L341.8,105.6 L343.9,105.6 L345.9,105.6 L348.0,105.6 L350.1,105.6 L352.1,105.6 L354.2,105.6 L356.2,105.6 L358.3,105.6 L360.3,105.6 L362.4,105.6 L364.4,105.6 L366.5,105.6 L368.5,105.6 L370.6,105.6 L372.7,105.6 L374.7,105.6 L376.8,105.6 L378.8,105.6 L380.9,105.6 L382.9,105.6 L385.0,105.6 L387.0,105.6 L389.1,105.6 L391.2,105.6 L393.2,105.6 L395.3,105.6 L397.3,105.6 L399.4,105.6 L401.4,105.6 L403.5,105.6 L405.5,105.6 L407.6,105.6 L409.6,105.6 L411.7,105.6 L413.8,105.6 L415.8,105.6 L417.9,105.6 L419.9,105.6 L422.0,105.6 L424.0,105.6 L426.1,105.6 L428.1,105.6 L430.2,105.6 L432.3,105.6 L434.3,105.6 L436.4,105.6 L438.4,105.6 L440.5,105.6 L442.5,105.6 L444.6,105.6 L446.6,105.6 L448.7,105.6 L450.8,105.6 L452.8,105.6 L454.9,105.6 L456.9,105.6 L459.0,105.6" fill="none" stroke="#27ae60" stroke-width="2" clip-path="url(#clip-step)"/>
  <rect x="298" y="24" width="162" height="80" rx="3" fill="white" stroke="#ccc" stroke-width="0.8"/>
  <line x1="302" y1="38" x2="324" y2="38" stroke="#c0392b" stroke-width="2.2"/>
  <text x="328" y="42" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">&#950;=0.2 (%OS=52%)</text>
  <line x1="302" y1="56" x2="324" y2="56" stroke="#e67e22" stroke-width="2.2"/>
  <text x="328" y="60" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">&#950;=0.5 (%OS=16%)</text>
  <line x1="302" y1="74" x2="324" y2="74" stroke="#2980b9" stroke-width="2.2"/>
  <text x="328" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">&#950;=0.7 (%OS=5%)</text>
  <line x1="302" y1="92" x2="324" y2="92" stroke="#27ae60" stroke-width="2.2"/>
  <text x="328" y="96" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">&#950;=1.0 (kritik)</text>
</svg>

---

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/01 Blok Diyagram Örnekleri]]
