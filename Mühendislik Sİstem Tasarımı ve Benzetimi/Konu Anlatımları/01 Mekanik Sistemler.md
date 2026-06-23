---
tags: [mst, mekanik, newton, lagrange, transfer-fonksiyonu, dc-motor, disli, konu-anlatımı]
---

# 01 — Mekanik Sistemler

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/01 Mekanik Sistemler Örnekleri|01 Mekanik Sistemler Örnekleri]]

> Newton 2. Yasası ile mekanik sistemlerin Laplace domeninde modellenmesi; DC motor ve dişli sistemleri.

---

## Temel Mekanik Elemanlar

| Eleman | Simge | Kuvvet-Hareket İlişkisi | Laplace Empedansı |
|--------|-------|------------------------|--------------------|
| Kütle $m$ | $M$ | $F = m\ddot{x}$ | $ms^2$ |
| Yay $k$ | $\wedge\wedge\wedge$ | $F = kx$ | $k$ |
| Sönümleyici $b$ | $\dashv\vdash$ | $F = b\dot{x}$ | $bs$ |

---

## Newton 2. Yasası Yöntemi

**Adım 1:** Her kütle için Serbest Cisim Diyagramı (FBD) çiz
**Adım 2:** Her kuvveti topla → $\sum F = m\ddot{x}$
**Adım 3:** Laplace dönüşümü al → transfer fonksiyonu

---

## Tek Kütleli Sistem (Yay-Kütle-Sönümleyici)

<svg width="380" height="180" viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrm1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#a93226"/>
    </marker>
    <marker id="arrx1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#1e7a4a"/>
    </marker>
  </defs>
  <!-- Wall -->
  <line x1="20" y1="30" x2="20" y2="160" stroke="#1a1a2e" stroke-width="3"/>
  <line x1="8" y1="40" x2="20" y2="30" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="60" x2="20" y2="50" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="80" x2="20" y2="70" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="100" x2="20" y2="90" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="120" x2="20" y2="110" stroke="#1a1a2e" stroke-width="1.3"/>
  <line x1="8" y1="140" x2="20" y2="130" stroke="#1a1a2e" stroke-width="1.3"/>
  <!-- Spring top -->
  <line x1="20" y1="60" x2="48" y2="60" stroke="#1a1a2e" stroke-width="1.8"/>
  <polyline points="48,60 53,60 57,48 63,72 69,48 75,72 81,48 87,72 93,48 99,72 102,60 128,60"
    fill="none" stroke="#1a1a2e" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="72" y="44" text-anchor="middle" font-family="serif" font-size="15" font-style="italic" fill="#1a1a2e">k</text>
  <!-- Damper bottom -->
  <line x1="20" y1="125" x2="65" y2="125" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="65" y1="112" x2="65" y2="138" stroke="#1a1a2e" stroke-width="1.8"/>
  <rect x="65" y="112" width="30" height="26" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.8"/>
  <line x1="95" y1="125" x2="128" y2="125" stroke="#1a1a2e" stroke-width="1.8"/>
  <text x="79" y="108" text-anchor="middle" font-family="serif" font-size="15" font-style="italic" fill="#1a1a2e">b</text>
  <!-- Mass -->
  <rect x="128" y="65" width="75" height="72" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="165" y="108" text-anchor="middle" font-family="serif" font-size="20" font-style="italic" fill="#1a1a2e">m</text>
  <!-- Force -->
  <line x1="203" y1="100" x2="255" y2="100" stroke="#a93226" stroke-width="2.2" marker-end="url(#arrm1)"/>
  <text x="265" y="106" font-family="serif" font-size="16" font-style="italic" fill="#a93226">f(t)</text>
  <!-- x -->
  <line x1="148" y1="45" x2="192" y2="45" stroke="#1e7a4a" stroke-width="1.6" marker-end="url(#arrx1)"/>
  <text x="142" y="40" font-family="serif" font-size="14" font-style="italic" fill="#1e7a4a">x(t)</text>
</svg>

**Hareket denklemi:**

$$m\ddot{x}(t) + b\dot{x}(t) + kx(t) = f(t)$$

**Laplace'ta (sıfır başlangıç koşulları):**

$$\boxed{G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}}$$

> [!tanim] İkinci Dereceden Standart Form
> - **Doğal Frekans**: $\omega_n = \sqrt{\frac{k}{m}}$
> - **Sönüm Oranı**: $\zeta = \frac{b}{2\sqrt{mk}}$

---

## İki Kütleli Sistem

**$m_1$ için FBD:**
$$m_1\ddot{x}_1 + b_1\dot{x}_1 + k_1 x_1 + k_2(x_1-x_2) + b_2(\dot{x}_1-\dot{x}_2) = f(t)$$

**$m_2$ için FBD:**
$$m_2\ddot{x}_2 + k_2(x_2-x_1) + b_2(\dot{x}_2-\dot{x}_1) = 0$$

**Laplace domeninde** ($x(0)=0$, $\dot{x}(0)=0$):

$$Y_1(s)\bigl(m_1s^2 + b_1s + k_1 + b_2s + k_2\bigr) - Y_2(s)(k_2+b_2s) = F(s)$$
$$-Y_1(s)(k_2+b_2s) + Y_2(s)\bigl(m_2s^2 + b_2s + k_2\bigr) = 0$$

Transfer fonksiyonu $\dfrac{Y_2(s)}{F(s)}$, matris yöntemiyle:

$$Y_1(s)\bigl(m_1s^2+b_1s+k_1+k_2+b_2s\bigr) - X_1(s)(k_2+b_2s) = F(s)$$

$$Y_2(s)(m_2s^2+b_2s+k_2) = Y_1(s)(k_2+b_2s)$$

$$\frac{Y_1(s)}{F(s)} = \frac{m_2s^2 + b_2s + k_2}{\Delta(s)}, \qquad \frac{Y_2(s)}{F(s)} = \frac{k_2+b_2s}{\Delta(s)}$$

---

## Lagrange Yöntemi

<span style="color:rgb(255, 255, 0)">Daha karmaşık sistemlerde Newton yerine kullanılır.</span>

$$\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{q}_i}\right) - \frac{\partial \mathcal{L}}{\partial q_i} + \frac{\partial D}{\partial \dot{q}_i} = Q_i$$

Burada $\mathcal{L} = T - V$ (Lagrangian):

| Eleman | Kinetik $T$ | Potansiyel $V$ | Sönümleme $D$ |
|--------|------------|----------------|---------------|
| Kütle $m$ | $\frac{1}{2}m\dot{x}^2$ | — | — |
| Yay $k$ | — | $\frac{1}{2}kx^2$ | — |
| Sönümleyici $b$ | — | — | $\frac{1}{2}b\dot{x}^2$ |
| Dönel $J$ | $\frac{1}{2}J\dot{\theta}^2$ | — | — |

---

## Dönel Mekanik Sistemler

| Öteleme | Dönel Karşılık |
|---------|----------------|
| Kütle $m$ | Atalet momenti $J$ |
| Sönümleyici $b$ | Dönel sönüm $B$ |
| Yay $k$ | Dönel yay $K$ |
| Kuvvet $F$ | Tork $T$ |

$$J\ddot{\theta} + B\dot{\theta} + K\theta = T(t) \quad\longrightarrow\quad G(s) = \frac{\Theta(s)}{T(s)} = \frac{1}{Js^2+Bs+K}$$

---

## DC Motor Modeli (Armatür Kontrolü)

<svg width="560" height="220" viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arria" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,1 L9,5 L0,9 Z" fill="#1e7a4a"/>
    </marker>
  </defs>
  <!-- Voltage source Va -->
  <line x1="55" y1="50" x2="55" y2="90" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="55" cy="115" r="25" fill="white" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M44,115 C46,105 50,105 53,115 C56,125 60,125 62,115" fill="none" stroke="#1a1a2e" stroke-width="1.6" stroke-linecap="round"/>
  <text x="55" y="105" text-anchor="middle" font-family="Helvetica,sans-serif" font-size="10" font-weight="700" fill="#1a1a2e">+</text>
  <text x="55" y="130" text-anchor="middle" font-family="Helvetica,sans-serif" font-size="13" font-weight="700" fill="#1a1a2e">−</text>
  <text x="22" y="110" font-family="serif" font-size="14" font-style="italic" fill="#1a1a2e">V_a</text>
  <line x1="55" y1="140" x2="55" y2="185" stroke="#1a1a2e" stroke-width="2"/>
  <!-- Top wire -->
  <line x1="55" y1="50" x2="100" y2="50" stroke="#1a1a2e" stroke-width="2"/>
  <!-- Ra -->
  <polyline points="100,50 104,50 107,38 113,62 119,38 125,62 131,38 137,62 140,50 170,50"
    fill="none" stroke="#1a1a2e" stroke-width="2" stroke-linejoin="round"/>
  <text x="120" y="30" text-anchor="middle" font-family="serif" font-size="13" font-style="italic" fill="#1a1a2e">R_a</text>
  <!-- ia arrow -->
  <line x1="108" y1="65" x2="136" y2="65" stroke="#1e7a4a" stroke-width="1.8" marker-end="url(#arria)"/>
  <text x="122" y="80" text-anchor="middle" font-family="serif" font-size="12" font-style="italic" fill="#1e7a4a">i_a</text>
  <!-- La -->
  <path d="M170,50 C170,38 186,38 186,50" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M186,50 C186,38 202,38 202,50" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <path d="M202,50 C202,38 218,38 218,50" fill="none" stroke="#1a1a2e" stroke-width="2"/>
  <line x1="218" y1="50" x2="260" y2="50" stroke="#1a1a2e" stroke-width="2"/>
  <text x="194" y="30" text-anchor="middle" font-family="serif" font-size="13" font-style="italic" fill="#1a1a2e">L_a</text>
  <!-- Back EMF eb -->
  <line x1="260" y1="50" x2="260" y2="90" stroke="#1a1a2e" stroke-width="2"/>
  <circle cx="260" cy="112" r="22" fill="#fffbe8" stroke="#1a1a2e" stroke-width="2"/>
  <text x="260" y="108" text-anchor="middle" font-family="serif" font-size="12" font-style="italic" fill="#8b6914">e_b</text>
  <text x="260" y="100" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="700" fill="#1a1a2e">+</text>
  <text x="260" y="128" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="700" fill="#1a1a2e">−</text>
  <line x1="260" y1="134" x2="260" y2="185" stroke="#1a1a2e" stroke-width="2"/>
  <!-- Bottom wire -->
  <line x1="55" y1="185" x2="260" y2="185" stroke="#1a1a2e" stroke-width="2"/>
  <!-- Shaft -->
  <line x1="260" y1="112" x2="330" y2="112" stroke="#1a1a2e" stroke-width="2.5" stroke-dasharray="6,4"/>
  <!-- Motor block -->
  <ellipse cx="360" cy="112" rx="30" ry="35" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="360" y="108" text-anchor="middle" font-family="serif" font-size="13" font-style="italic" fill="#1a1a2e">J_m</text>
  <text x="360" y="125" text-anchor="middle" font-family="serif" font-size="11" fill="#1a1a2e">B_m</text>
  <!-- Output -->
  <line x1="390" y1="112" x2="450" y2="112" stroke="#1a1a2e" stroke-width="3"/>
  <path d="M410 85 A28 28 0 0 1 440 99" fill="none" stroke="#a93226" stroke-width="2" marker-end="url(#arria)"/>
  <text x="450" y="85" font-family="serif" font-size="14" font-style="italic" fill="#a93226">Θ_m</text>
</svg>

**Üç temel denklem:**

**1) KVL (Armatür Devresi):**
$$V_a(s) = (R_a + L_a s)\,I_a(s) + K_b s\,\Theta_m(s)$$

**2) Tork:** $T_m(s) = K_t\,I_a(s)$

**3) Mekanik:** $T_m(s) = s(J_m s + B_m)\,\Theta_m(s)$

**Transfer Fonksiyonu ($L_a \approx 0$ yaklaşımı):**

$$\boxed{\frac{\Theta_m(s)}{V_a(s)} = \frac{K_t/R_a J_m}{s\!\left(s + \dfrac{R_a B_m + K_b K_t}{R_a J_m}\right)}}$$

---

## Dişli (Gear) Sistemi

<svg width="300" height="160" viewBox="0 0 300 160" xmlns="http://www.w3.org/2000/svg">
  <!-- Small gear -->
  <circle cx="80" cy="80" r="35" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="80" y="76" text-anchor="middle" font-family="serif" font-size="12" fill="#1a1a2e">N₁,r₁</text>
  <text x="80" y="92" text-anchor="middle" font-family="serif" font-size="11" fill="#1a1a2e">T₁,θ₁</text>
  <!-- Large gear -->
  <circle cx="195" cy="80" r="60" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="195" y="76" text-anchor="middle" font-family="serif" font-size="12" fill="#1a1a2e">N₂,r₂</text>
  <text x="195" y="92" text-anchor="middle" font-family="serif" font-size="11" fill="#1a1a2e">T₂,θ₂</text>
  <!-- Contact point -->
  <circle cx="115" cy="80" r="4" fill="#a93226"/>
  <!-- Labels -->
  <text x="150" y="155" text-anchor="middle" font-family="Helvetica,sans-serif" font-size="11" fill="#555">N₂ &gt; N₁ → Yavaş, yüksek tork</text>
</svg>

**Dişli oranı formülleri:**

$$\frac{T_1}{T_2} = \frac{r_1}{r_2} = \frac{N_1}{N_2}, \qquad \frac{\theta_2}{\theta_1} = \frac{N_1}{N_2}$$

> [!info] Dişli Formülü Terimleri
> - **T**: Tork (moment)
> - **r**: Dişli yarıçapı
> - **N**: Diş sayısı
> - **θ**: Dönme açısı

**Yük yansıtma (motor miline):**

$$J_t = J_a + J_L\!\left(\frac{N_1}{N_2}\right)^{\!2}, \qquad D_t = D_a + D_L\!\left(\frac{N_1}{N_2}\right)^{\!2}$$

> [!info] Yük Yansıtma Terimleri
> - **J_t**: Toplam eylemsizlik (motor + yük)
> - **J_a**: Motor eylemsizliği
> - **J_L**: Yük eylemsizliği
> - **D_t**: Toplam sönüm
> - **D_a**: Motor sönümü
> - **D_L**: Yük sönümü

---

## Mekanik ↔ Elektrik Analogisi

| Mekanik | Elektrik (hız-voltaj) |
|---------|----------------------|
| Kuvvet $F$ | Voltaj $v$ |
| Hız $\dot{x}$ | Akım $i$ |
| Kütle $m$ | İndüktör $L$ |
| Sönümleyici $b$ | Direnç $R$ |
| Yay $k$ | $1/C$ |

> [!sinav] Sınav İpuçları
> - FBD çiz → her kuvveti tek tek yaz → Newton 2. Yasası
> - Laplace'ta $\ddot{x} \to s^2 X(s)$, $\dot{x} \to sX(s)$ (sıfır başlangıç şartıyla)
> - İki kütle → iki denklem → matris veya yerine koyma ile çöz
> - DC motorda $L_a \approx 0$ sıkça kullanılır → sistem 2. dereceden 1. dereceye iner
> - Dişli: $J$ ve $D$ değerleri $(N_1/N_2)^2$ ile motor miline yansıtılır
