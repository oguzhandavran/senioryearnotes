---
tags: [mst, kök-yer-eğrisi, kompansatör, pd, pi, lead-lag, kontrol-tasarımı, konu-anlatımı]
---

# 05 — Kök Yer Eğrisi ve Kompansasyon

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/05 Kök Yer Eğrisi Örnekleri|05 Kök Yer Eğrisi Örnekleri]]

> [!link] Temel KYE Teorisi
> KYE çizim kuralları ve çözümlü örnekler için: **[[../Otomatik Kontrol/04 Kök Yer Eğrisi|OK — KYE]]**
> Bu notta MST perspektifinden **kompansatör tasarımı** ağırlıklıdır.

---

## Tasarım Hedefleri

Kapalı çevrim sistem tasarımında tipik hedefler:

| Hedef | Parametre |
|-------|----------|
| Belirli aşım oranı | $\%OS \to \zeta$ |
| Belirli yerleşme süresi | $T_s \to \sigma = \zeta\omega_n$ |
| Belirli yükselme süresi | $T_r \to \omega_d$ |
| Sıfır kararlı hal hatası | Sistem tipi arttır |
| Belirli kazanç payı | Bode PM/GM |

---

## Kompansatör Türleri

<svg width="480" height="330" viewBox="0 0 480 330" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mst05a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Root node -->
  <rect x="130" y="10" width="220" height="36" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="240" y="33" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="white">Kompansatör Türleri</text>
  <!-- Lines from root bottom (240,46) to 6 children -->
  <line x1="240" y1="46" x2="120" y2="90" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05a)"/>
  <line x1="240" y1="46" x2="360" y2="90" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05a)"/>
  <line x1="240" y1="46" x2="120" y2="175" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05a)"/>
  <line x1="240" y1="46" x2="360" y2="175" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05a)"/>
  <line x1="240" y1="46" x2="120" y2="258" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05a)"/>
  <line x1="240" y1="46" x2="360" y2="258" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05a)"/>
  <!-- Row 1 Left: PD -->
  <rect x="35" y="92" width="170" height="52" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="120" y="112" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="#1a1a2e">PD (türevsel)</text>
  <text x="120" y="128" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">sıfır ekler → hız artar</text>
  <text x="120" y="140" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">T_s azaltır, %OS kontrolü</text>
  <!-- Row 1 Right: Lead -->
  <rect x="275" y="92" width="170" height="52" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="360" y="112" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="#1a1a2e">Lead (faz öncüsü)</text>
  <text x="360" y="128" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">sıfır + kutup, faz arttırır</text>
  <text x="360" y="140" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">PM artar, BW artar</text>
  <!-- Row 2 Left: PI -->
  <rect x="35" y="177" width="170" height="52" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="120" y="197" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="#1a1a2e">PI (integral)</text>
  <text x="120" y="213" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">kutup ekler → tip artar</text>
  <text x="120" y="225" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">kararlı hal hatası → 0</text>
  <!-- Row 2 Right: Lag -->
  <rect x="275" y="177" width="170" height="52" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="360" y="197" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="#1a1a2e">Lag (faz gericisi)</text>
  <text x="360" y="213" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">kazancı artırır (DC'de)</text>
  <text x="360" y="225" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">geçici yanıt az değişir</text>
  <!-- Row 3 Left: PID -->
  <rect x="35" y="260" width="170" height="52" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="120" y="280" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="#1a1a2e">PID</text>
  <text x="120" y="296" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">PD + PI kombinasyonu</text>
  <text x="120" y="308" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">hız + hata kontrolü</text>
  <!-- Row 3 Right: Lead-Lag -->
  <rect x="275" y="260" width="170" height="52" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="360" y="280" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="#1a1a2e">Lead-Lag</text>
  <text x="360" y="296" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Lead + Lag birleşimi</text>
  <text x="360" y="308" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">hız + kararlı hal iyileştirme</text>
</svg>

---

## PD Kompansatörü

$$G_c(s) = K_c(s + z_c)$$

- Kapalı çevrim karakteristik denklemine **sıfır ekler**
- KYE'yi **sola çeker** (daha hızlı yanıt)
- Gürültüye duyarlı (frekans artışı)

**Tasarım yöntemi:**
1. $\%OS$'tan $\zeta$ hesapla: $\zeta = \dfrac{-\ln(\%OS/100)}{\sqrt{\pi^2+\ln^2(\%OS/100)}}$
2. $T_s$'ten $\sigma = \zeta\omega_n$ hesapla: $\sigma = 4/T_s$ (%2 kriter)
3. İstenen baskın kutup: $s_d = -\sigma \pm j\omega_d$ ($\omega_d = \omega_n\sqrt{1-\zeta^2}$)
4. Açı şartını sağlayan $z_c$ bul
5. Genlik şartından $K_c$ bul

**Açı şartı:**
$$\angle G_c(s_d) G_p(s_d) = \pm 180°$$

**Geometrik yöntem ($z_c$ bulma):**

$s_d = -\sigma + j\omega_d$ için, $z_c$ henüz bilinmiyor:

$$\sum\angle\text{sıfırlar} - \sum\angle\text{kutuplar} = 180°(2k+1)$$

Sıfır $z_c$ açısı: $\theta_{z_c} = \angle(s_d + z_c) = \arctan\!\dfrac{\omega_d}{z_c - \sigma}$

Gerekli açıyı diğer kutup/sıfır açılarından hesapla, sonra:

$$\tan(\theta_{z_c}) = \frac{\omega_d}{z_c - \sigma} \implies z_c = \sigma + \frac{\omega_d}{\tan(\theta_{z_c})}$$

*"tan(β Pisagor)" yöntemi: baskın kutuptan yatay eksen açısı $\beta = \arccos(\zeta)$, sıfır konumunu Pisagor geometrisiyle bul.*

---

## Lead Kompansatörü

$$G_{lead}(s) = K_c \frac{s + z_c}{s + p_c}, \quad z_c < p_c$$

- **Faz öncüsü** ekler (faz artar)
- PM'i iyileştirir
- Bant genişliğini artırır

**Kural:** $\dfrac{p_c}{z_c} \approx 10$ genellikle yeterli

**Maksimum faz katkısı:**

$$\phi_{max} = \arcsin\left(\frac{1-\alpha}{1+\alpha}\right), \quad \alpha = \frac{z_c}{p_c} < 1$$

**Frekans:** $\omega_{max} = \dfrac{\sqrt{p_c z_c}}{1}$ (geometrik ortalama)

---

## Lag Kompansatörü

$$G_{lag}(s) = K_c \frac{s + z_c}{s + p_c}, \quad z_c > p_c$$

- **Kazanç artırır** (düşük frekansta)
- Hız hatasını azaltır, kararlı hal hassasiyetini artırır
- Geçici yanıtı bozmaz (kutup-sıfır orijine yakın yerleştirilir)

**Kural:** $p_c \approx z_c/10$, orijine yakın tut

---

## PI Kompansatörü

$$G_{PI}(s) = K_p + \frac{K_i}{s} = \frac{K_p s + K_i}{s}$$

- Sistem tipini arttırır (1 kutup orijinde ekler)
- Basamak hatası → sıfır
- KYE'ye orijine çok yakın sıfır ekler

> [!warning]
> PI eklenmesi geçici yanıtı yavaşlatabilir. Dikkatli tasarım gerekir.

---

## PID Kompansatörü

$$G_{PID}(s) = K_p + \frac{K_i}{s} + K_d s = \frac{K_d s^2 + K_p s + K_i}{s}$$

PD + PI kombinasyonu:
- PD → hız ve aşım kontrolü
- PI → kararlı hal hatası sıfırlama

**Ziegler-Nichols (ön bilgi):**

Limit kararlılık: $K = K_u$, $T = T_u$ ($\omega = 2\pi/T_u$)

| Kontrolör | $K_p$ | $T_i$ | $T_d$ |
|-----------|-------|-------|-------|
| P | $0.5K_u$ | — | — |
| PI | $0.45K_u$ | $T_u/1.2$ | — |
| PID | $0.6K_u$ | $T_u/2$ | $T_u/8$ |

---

## Lead-Lag Kompansatörü

$$G_{LL}(s) = K_c \frac{(s+z_1)(s+z_2)}{(s+p_1)(s+p_2)}$$

$p_1 < z_1 < z_2 < p_2$ (lag + lead birleşimi):
- Lag kısmı: kazanç ve kararlı hal hassasiyetini artırır
- Lead kısmı: geçici yanıtı iyileştirir

---

## KYE ile Tasarım Özeti

<svg width="460" height="390" viewBox="0 0 460 390" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mst05b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Step 1 -->
  <rect x="90" y="10" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="230" y="32" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">1. İstenen specs: %OS, T_s, e_ss</text>
  <line x1="230" y1="44" x2="230" y2="60" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst05b)"/>
  <!-- Step 2 -->
  <rect x="90" y="62" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="230" y="84" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">2. ζ, ω_n hesapla</text>
  <line x1="230" y1="96" x2="230" y2="112" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst05b)"/>
  <!-- Step 3 -->
  <rect x="90" y="114" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="230" y="136" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">3. Baskın kutup s_d hesapla</text>
  <line x1="230" y1="148" x2="230" y2="164" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst05b)"/>
  <!-- Step 4 -->
  <rect x="90" y="166" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="230" y="188" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">4. Kompansatörsüz açı hesapla</text>
  <line x1="230" y1="200" x2="230" y2="214" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst05b)"/>
  <!-- Diamond: Açı farkı? -->
  <polygon points="230,216 298,244 230,272 162,244" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <text x="230" y="240" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Açı farkı?</text>
  <text x="230" y="256" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e">(kompansatör gerekli mi?)</text>
  <!-- Left branch label -->
  <text x="108" y="240" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">&lt; 60°</text>
  <!-- Left branch line from diamond left (162,244) → down to x=90, y=290 -->
  <line x1="162" y1="244" x2="90" y2="244" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="90" y1="244" x2="90" y2="290" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05b)"/>
  <!-- Left branch: Lead Kompansatör -->
  <rect x="5" y="292" width="170" height="30" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="90" y="312" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Lead Kompansatör seç</text>
  <line x1="90" y1="322" x2="90" y2="338" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05b)"/>
  <!-- Açı şartından z_c -->
  <rect x="5" y="340" width="170" height="30" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="90" y="360" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Açı şartından z_c bul</text>
  <line x1="90" y1="370" x2="90" y2="383" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05b)"/>
  <!-- Doğrula (dark box) at very bottom left -->
  <!-- Right branch label -->
  <text x="360" y="240" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Kazanç yeterli</text>
  <!-- Right branch line from diamond right (298,244) → down to x=370, y=290 -->
  <line x1="298" y1="244" x2="370" y2="244" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="370" y1="244" x2="370" y2="290" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05b)"/>
  <!-- Right branch: Sadece K -->
  <rect x="285" y="292" width="170" height="30" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="370" y="312" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Sadece K ayarı yeterli</text>
  <!-- Genlik şartından K_c (shared / converging) -->
  <line x1="370" y1="322" x2="370" y2="355" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="370" y1="355" x2="285" y2="355" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="285" y1="355" x2="230" y2="355" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05b)"/>
  <line x1="90" y1="386" x2="175" y2="386" stroke="#1a1a2e" stroke-width="1.5"/>
  <line x1="175" y1="386" x2="185" y2="386" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst05b)"/>
  <!-- Final box: Doğrula -->
  <rect x="185" y="348" width="120" height="44" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="245" y="367" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">Genlik şartı</text>
  <text x="245" y="383" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">K_c bul ✓</text>
</svg>

---

> [!sinav] Sınav İpucu
> - PD sıfır ekler → KYE sol tarafa kayar → daha hızlı sistem
> - Lead: PM artırır, bant genişliği artar
> - Lag: kararlı hal kazancı artar, geçici yanıt minimal değişir
> - PI = lag'ın özel hali (sıfır orijine yakın, kutup tam orijinde)
> - PD = lead'in özel hali (sadece sıfır, kutup yok)
> - Tasarımda her zaman: açı şartı → konumu bul, genlik şartı → K bul

---

## Op-Amp ile Kompansatör Gerçekleme (Hocanın Notu)

Kompansatörler op-amp devreleri ile fiziksel olarak gerçeklenir. Genel yapı:

$$G(s) = -\frac{Z_2(s)}{Z_1(s)}$$

| Fonksiyon | $Z_1$ | $Z_2$ | Transfer Fonksiyonu |
|-----------|-------|-------|-------------------|
| **Kazanç** | $R_1$ | $R_2$ | $-R_2/R_1$ |
| **İntegral** | $R$ | $C$ | $-\dfrac{1}{RCs}$ |
| **Türev** | $C$ | $R$ | $-RCs$ |
| **PI kontrolör** | $R_1$ | $R_2 \parallel C$ | $-\dfrac{R_2}{R_1}\!\left(s+\dfrac{1}{R_2C}\right)\dfrac{1}{s}$ |
| **PD kontrolör** | $R_1 \parallel C_1$ | $R_2$ | $-R_2C_1\!\left(s+\dfrac{1}{R_1C_1}\right)$ |
| **PID kontrolör** | $R_1 \parallel C_1$ | $R_2 \parallel C_2$ (seri) | $-\dfrac{R_2C_1\!\left(s+\frac{1}{R_1C_1}\right)\!\left(s+\frac{1}{R_2C_2}\right)}{s}$ |

> [!sinav] PD Tasarımından Devreye Geçiş
> PD sıfırunu $z_c$ bulduktan sonra:
> - $G_{PD}(s) = -R_2C_1(s + z_c)$ formunda eşitleyin
> - $z_c = 1/(R_1C_1)$ → $R_1C_1$ sabitini belirler
> - $R_2C_1 = 1$ seçilirse kazanç $K_c$ ile $R_2$ belirlenir

**İlgili:** [[../Otomatik Kontrol/04 Kök Yer Eğrisi|OK — Kök Yer Eğrisi]]
