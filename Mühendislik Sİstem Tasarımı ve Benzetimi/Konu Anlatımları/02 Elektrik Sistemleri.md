---
tags: [mst, elektrik, rlc, kvl, kcl, transfer-fonksiyonu, op-amp, konu-anlatımı]
---

# 02 — Elektrik Sistemleri

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/02 Elektrik Sistemleri Örnekleri|02 Elektrik Sistemleri Örnekleri]]

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
