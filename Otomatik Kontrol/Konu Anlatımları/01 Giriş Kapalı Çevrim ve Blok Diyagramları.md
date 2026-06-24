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

---

← [[OK Ana Sayfa]] | Örnekler: [[../Örnek Sorular/01 Blok Diyagram Örnekleri]]
