---
tags: [ssi, dsp, filtre, fir, iir, butterworth, konu-anlatımı]
---

# 04 — Sayısal Filtre Tasarımı (Teori)

← [[SSI Ana Sayfa]] | Örnekler: [[../Örnek Sorular/04 Filtre Tasarımı Örnekleri]]

## Özet

> FIR: sonlu impuls yanıtı, her zaman kararlı. IIR: sonsuz, analog filtreyi dönüştürerek tasarla. Bilineer dönüşüm: analog → sayısal.

---

## 0. İdeal Sayısal Filtreler (Arş. Gör. Ecmel TERZİ Ders Notları)

### Alçak Geçiren (Low Pass — LP)

$$H_{LP}(e^{j\omega}) = \begin{cases}1, & |\omega| < \omega_c \\ 0, & \omega_c < |\omega| \leq \pi\end{cases}$$

İmpuls yanıtı: $h_{LP}[n] = \dfrac{\sin(\omega_c n)}{\pi n} = \dfrac{\omega_c}{\pi}\operatorname{sinc}(\omega_c n)$

### Yüksek Geçiren (High Pass — HP)

$$H_{HP}(e^{j\omega}) = \begin{cases}0, & |\omega| < \omega_c \\ 1, & \omega_c < |\omega| \leq \pi\end{cases}$$

$$H_{HP}(e^{j\omega}) = 1 - H_{LP}(e^{j\omega})$$

$$h_{HP}[n] = \delta[n] - \frac{\sin(\omega_c n)}{\pi n}$$

### Bant Geçiren (Band Pass — BP)

Pasaband: $\omega_a < |\omega| < \omega_b$

$$H_{BP}(e^{j\omega}) = H_{HP}^{(\omega_a)}(e^{j\omega}) \cdot H_{LP}^{(\omega_b)}(e^{j\omega})$$

$$h_{BP}[n] = h_{HP}[n] * h_{LP}[n]$$

Gerçekleme: $x[n] \to \boxed{h_{HP}[n]} \to \boxed{h_{LP}[n]} \to y[n]$

### Bant Söndüren (Band Stop — BS / Notch)

Stopband: $\omega_a < |\omega| < \omega_b$

$$H_{BS}(e^{j\omega}) = 1 - H_{BP}(e^{j\omega})$$

| Filtre | Pasaband | Stopband | İlişki |
|--------|---------|----------|--------|
| LP | $\|\omega\| < \omega_c$ | $\omega_c < \|\omega\| \leq \pi$ | — |
| HP | $\omega_c < \|\omega\| \leq \pi$ | $\|\omega\| < \omega_c$ | $1 - H_{LP}$ |
| BP | $\omega_a < \|\omega\| < \omega_b$ | Dışarısı | $H_{HP} \cdot H_{LP}$ |
| BS | Dışarısı | $\omega_a < \|\omega\| < \omega_b$ | $1 - H_{BP}$ |

> [!sinav] İdeal Filtreler Sınavda
> - İdeal LP impuls yanıtı sonsuzdur → gerçeklenemez → penceleleme (windowing) gerekir
> - $h_{LP}[n] = \omega_c/\pi \cdot \operatorname{sinc}(\omega_c n)$: çift simetrik, tüm $n$'de tanımlı
> - HP = $\delta[n] - LP$ ilişkisi sınavda çıkar

---

## 1. FIR vs IIR Karşılaştırması

| Özellik | FIR | IIR |
|---------|-----|-----|
| İmpuls yanıtı | Sonlu ($N$ terim) | Sonsuz |
| Kararlılık | Her zaman kararlı ✅ | Kutuplar tasarımla belirlenir |
| Faz | Doğrusal faz mümkün ✅ | Doğrusal faz zor |
| Verimlilik | Daha fazla katsayı | Daha az katsayı |
| Geri besleme | Yok | Var |
| Tasarım | Pencere metodu, Parks-McClellan | Analog prototip dönüşümü |

---

## 2. FIR Filtre Tasarımı — Pencere Metodu

İstenen ideal frekans yanıtı $H_d(e^{j\omega})$ verildiğinde:

1. İdeal impuls yanıtı hesapla: $h_d[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi}H_d(e^{j\omega})e^{j\omega n}d\omega$
2. $h[n] = h_d[n] \cdot w[n]$ (pencele)

**İdeal Alçak Geçiren Filtre:**

$$h_d[n] = \frac{\sin(\omega_c n)}{\pi n}, \quad h_d[0] = \frac{\omega_c}{\pi}$$

**FIR Doğrusal Faz Koşulu:** $h[n] = h[N-1-n]$ (simetrik)

---

## 3. IIR Filtre Tasarımı

### Analog Prototip → Sayısal

<svg width="480" height="110" viewBox="0 0 480 110" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ssi04" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Step 1: Digital Specs -->
  <rect x="5" y="30" width="100" height="50" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="55" y="52" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Sayısal</text>
  <text x="55" y="68" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Specs</text>
  <line x1="105" y1="55" x2="123" y2="55" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ssi04)"/>
  <!-- Step 2: Prewarping -->
  <rect x="125" y="20" width="108" height="70" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="179" y="42" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Frekans önceden</text>
  <text x="179" y="57" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">düzeltme</text>
  <text x="179" y="73" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">(prewarping)</text>
  <line x1="233" y1="55" x2="251" y2="55" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ssi04)"/>
  <!-- Step 3: Analog Prototype -->
  <rect x="253" y="20" width="108" height="70" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="307" y="42" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Analog Prototip</text>
  <text x="307" y="57" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">H_a(s)</text>
  <text x="307" y="73" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">Butterworth / Cheby.</text>
  <line x1="361" y1="55" x2="379" y2="55" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ssi04)"/>
  <!-- Step 4: Bilinear → H(z) -->
  <rect x="381" y="20" width="94" height="70" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="428" y="42" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="white">Bilineer Dön.</text>
  <text x="428" y="57" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#aac4e8">s → z</text>
  <text x="428" y="75" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="white">H(z) ✓</text>
</svg>

### Bilineer Dönüşüm

$$s = \frac{2}{T}\cdot\frac{1-z^{-1}}{1+z^{-1}} = \frac{2}{T}\cdot\frac{z-1}{z+1}$$

veya (normalize edilmiş): $s \leftarrow \frac{1-z^{-1}}{1+z^{-1}}$

**Frekans ilişkisi:**
$$\Omega_{analog} = \frac{2}{T}\tan\left(\frac{\omega_{digital}}{2}\right)$$

> [!warning] Frekans Bükülmesi (Warping)
> Bilineer dönüşüm frekansları doğrusal olmayan şekilde eşler. Tasarımda hedef frekansları **önceden** düzelt (prewarping):
> $$\Omega_c = \frac{2}{T}\tan\left(\frac{\omega_c}{2}\right)$$

---

## 4. Butterworth Filtre

**Özellikler:** Geçiş bandında maximally flat (tüm kutuplar $s$ düzleminde birim çember üzerinde eşit aralıklı).

**Büyüklük yanıtı:**
$$|H_a(j\Omega)|^2 = \frac{1}{1+(\Omega/\Omega_c)^{2N}}$$

**Derecesi:**
$$N \geq \frac{\log\left[\dfrac{10^{0.1A_s}-1}{10^{0.1A_p}-1}\right]}{2\log(\Omega_s/\Omega_p)}$$

**Kutup konumları** ($N$. dereceden):
$$s_k = \Omega_c e^{j\pi(2k-1)/(2N)}, \quad k=1,...,N$$

---

## 5. Yüksek/Alçak/Band Geçiren Dönüşümler

| Dönüşüm | Formül |
|---------|--------|
| LP → LP | $s \leftarrow s/\Omega_p$ |
| LP → HP | $s \leftarrow \Omega_p/s$ |
| LP → BP | $s \leftarrow \frac{s^2+\Omega_0^2}{Bs}$ |
| LP → BS | $s \leftarrow \frac{Bs}{s^2+\Omega_0^2}$ |

---

## 6. Pratik Filtre Özellikleri

**Alçak geçiren filtre specs:**
- $A_p$: geçiş bandı dalgalanması (dB), $\omega_p$: geçiş frekansı
- $A_s$: durdurma bandı zayıflatma (dB), $\omega_s$: durdurma frekansı

> [!sinav] FIR Filtre Uzunluğu (Kural)
> Dikdörtgen pencere: $N \approx \dfrac{8\pi}{\Delta\omega}$ ($\Delta\omega = \omega_s - \omega_p$)
> Hamming pencere: $N \approx \dfrac{8\pi}{\Delta\omega}$ (yaklaşık)

---

## Bağlantılı Notlar

- [[03 DFT ve FFT]]
- [[02 Z-Dönüşümü]]
- [[../Örnek Sorular/04 Filtre Tasarımı Örnekleri]]
- [[SSI Formül Sayfası]]
