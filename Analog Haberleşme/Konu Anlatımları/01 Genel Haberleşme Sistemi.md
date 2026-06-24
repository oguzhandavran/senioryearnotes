---
tags: [analog-haberleşme, haberleşme-sistemi, modülasyon, blok-diyagram, konu-anlatımı]
---

# 01 — Genel Haberleşme Sistemi

← [[../AH Ana Sayfa]] | Sonraki: [[02 Fourier Analizi]]

---

## Haberleşme Sistemi Blok Diyagramı

<svg width="480" height="130" viewBox="0 0 480 130" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ah01a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Kaynak -->
  <rect x="5" y="38" width="80" height="54" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="45" y="61" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e">Kaynak</text>
  <text x="45" y="78" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">x(t)</text>
  <line x1="85" y1="65" x2="103" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ah01a)"/>
  <!-- Verici -->
  <rect x="105" y="38" width="90" height="54" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="150" y="57" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e">Verici</text>
  <text x="150" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Modülatör</text>
  <line x1="195" y1="65" x2="213" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ah01a)"/>
  <text x="204" y="58" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">x_c(t)</text>
  <!-- Kanal -->
  <rect x="215" y="28" width="100" height="74" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="265" y="52" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e">Kanal</text>
  <text x="265" y="68" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">h(t) + n(t)</text>
  <text x="265" y="84" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#c0392b">(gürültü)</text>
  <line x1="315" y1="65" x2="333" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ah01a)"/>
  <text x="324" y="58" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">r(t)</text>
  <!-- Alıcı -->
  <rect x="335" y="38" width="90" height="54" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="380" y="57" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-weight="bold" fill="#1a1a2e">Alıcı</text>
  <text x="380" y="72" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Demodülatör</text>
  <line x1="425" y1="65" x2="443" y2="65" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ah01a)"/>
  <!-- Hedef -->
  <rect x="445" y="38" width="30" height="54" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="460" y="61" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-weight="bold" fill="#1a1a2e">He-</text>
  <text x="460" y="75" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-weight="bold" fill="#1a1a2e">def</text>
  <text x="460" y="89" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">x̂(t)</text>
</svg>

| Blok | Görev |
|------|-------|
| **Kaynak** | İletilecek bilgi — ses, görüntü, veri |
| **Verici (Modülatör)** | Mesajı taşıyıcıya bindirip iletim kanalına uygun hale getirir |
| **Kanal** | Fiziksel ortam — kablo, hava, fiber; gürültü ve parazit ekler |
| **Alıcı (Demodülatör)** | Kanaldan gelen sinyali işleyip mesajı geri çıkarır |
| **Hedef** | Alınan mesajın tüketicisi |

---

## Modülasyon Nedir?

> [!tanim] Modülasyon
> Mesaj sinyalinin $x(t)$ bilgisini yüksek frekanslı bir **taşıyıcı sinyal** üzerine bindirme işlemidir.
> $$x_c(t) = f\bigl(x(t),\; A_c\cos(2\pi f_c t)\bigr)$$

---

## Modülasyon Neden Gerekli?

> [!sinav] 3 Temel Neden — Sınavda sorulur!

**1. Uzak mesafe iletimi:**
- Düşük frekanslı ses sinyalleri (~300 Hz – 3 kHz) havada hızla söner
- Yüksek frekanslı elektromanyetik dalgalar ($f_c$ MHz – GHz) çok daha uzağa gider
- $\lambda = c/f$: frekans arttıkça dalga boyu kısalır → anten boyutu küçülür

**2. Kanal paylaşımı (Frekans Çoklama / FDM):**
- Farklı yayıncılar farklı taşıyıcı frekanslarına ($f_{c1}, f_{c2}, \ldots$) yerleşir
- Her biri $B_T$ bant genişliği kaplar → kanallar çakışmaz
- Radyo, TV, cep telefonu hepsi aynı havayı paylaşır

**3. Gürültüye karşı direnç:**
- Uygun modülasyon türü seçilerek gürültü etkisi azaltılır
- FM ve PM, AM'e göre gürültüde daha başarılıdır

---

## Temel Büyüklükler

| Sembol | İsim | Tipik değer |
|--------|------|-------------|
| $x(t)$ | Mesaj (modüle edici) işaret | Bant sınırlı: $\|f\| \leq W$ |
| $A_c$ | Taşıyıcı genliği | Sabit |
| $f_c$ | Taşıyıcı frekansı | $f_c \gg W$ |
| $W$ | Mesaj bant genişliği | Hz cinsinden |
| $B_T$ | İletim bant genişliği | $B_T = 2W$ (AM için) |

---

## Modülasyon Türleri

<svg width="480" height="290" viewBox="0 0 480 290" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ah01b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Root -->
  <rect x="155" y="10" width="170" height="34" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="240" y="32" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-weight="bold" fill="white">Modülasyon</text>
  <!-- 3 branches: AM, FM, PM -->
  <line x1="240" y1="44" x2="100" y2="80" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ah01b)"/>
  <line x1="240" y1="44" x2="240" y2="78" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ah01b)"/>
  <line x1="240" y1="44" x2="380" y2="80" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-ah01b)"/>
  <!-- AM box (left) -->
  <rect x="20" y="82" width="160" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="100" y="100" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Genlik Mod. (AM)</text>
  <!-- FM box (center) -->
  <rect x="170" y="80" width="140" height="38" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="240" y="97" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Frekans Mod.</text>
  <text x="240" y="112" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">(FM/PM)</text>
  <!-- PM box (right) -->
  <rect x="320" y="82" width="140" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="390" y="100" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="#1a1a2e">Açı Mod. (PM)</text>
  <!-- AM sub-branches: Standart, DSB-SC, SSB, VSB -->
  <line x1="100" y1="116" x2="50" y2="155" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-ah01b)"/>
  <line x1="100" y1="116" x2="100" y2="153" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-ah01b)"/>
  <line x1="100" y1="116" x2="150" y2="155" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-ah01b)"/>
  <!-- Standart AM -->
  <rect x="5" y="157" width="88" height="42" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="49" y="174" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Standart AM</text>
  <text x="49" y="188" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">ÇYB + taşıyıcı</text>
  <!-- DSB-SC -->
  <rect x="57" y="157" width="88" height="42" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="101" y="174" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">DSB-SC</text>
  <text x="101" y="188" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">ÇYB taşıyıcısız</text>
  <!-- SSB -->
  <rect x="110" y="157" width="88" height="42" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="154" y="174" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">SSB</text>
  <text x="154" y="188" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" font-style="italic" fill="#1a1a2e">Tek yan bant</text>
  <!-- VSB note -->
  <text x="100" y="224" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e" font-style="italic">VSB/AYB: artık yan bant</text>
  <!-- FM note -->
  <text x="240" y="150" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">s_FM(t) = A_c cos(2πf_c t + 2πk_f ∫x dτ)</text>
  <!-- PM note -->
  <text x="390" y="135" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">s_PM(t) = A_c cos(2πf_c t + k_p x(t))</text>
</svg>

> [!warning] Kapsam
> Bu derste **Standart AM** ve **DSB-SC** ağırlıklı. FM/PM kapsam dışı.

---

> [!sinav] Sınav İpucu
> - Verici çıkışı: $x_c(t)$ → modüle edilmiş işaret
> - Kanal çıkışı: $r(t) = x_c(t) * h(t) + n(t)$
> - Modülasyonun amacını 3 maddede bilmek yeterli
