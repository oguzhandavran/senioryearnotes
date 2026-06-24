---
tags: [emd, bütünleme, iletim-hatları, konu-anlatımı]
---

# 05 — İletim Hatları

← [[EMD Ana Sayfa]] | Örnekler: [[../Örnek Sorular/05 İletim Hatları Örnekleri]]

> **Özet:** Dağıtık parametreli sistemler. Telegraf denklemleri → dalga çözümü → empedans hesabı → Smith çizimi.

---

## İletim Hattı Modeli

Dağıtık devre parametreleri (birim uzunluk başına):

| Parametre | Sembol | Birim |
|-----------|--------|-------|
| Direnç | $R'$ | Ω/m |
| Endüktans | $L'$ | H/m |
| Kapasitans | $C'$ | F/m |
| İletkenlik | $G'$ | S/m |

---

## Telegraf Denklemleri

$$\frac{\partial V(z,t)}{\partial z} = -R'I - L'\frac{\partial I}{\partial t}$$

$$\frac{\partial I(z,t)}{\partial z} = -G'V - C'\frac{\partial V}{\partial t}$$

Harmonik durumda (fazör):

$$\frac{d^2V_s}{dz^2} = \gamma^2 V_s, \qquad \frac{d^2I_s}{dz^2} = \gamma^2 I_s$$

---

## Yayılma Sabiti

> [!formul] Yayılma Sabiti
> $$\gamma = \alpha + j\beta = \sqrt{(R'+j\omega L')(G'+j\omega C')}$$

Kayıpsız hat ($R'=G'=0$):
$$\gamma = j\beta = j\omega\sqrt{L'C'}, \quad \alpha=0$$

---

## Karakteristik Empedans

> [!formul] Karakteristik Empedans $Z_0$
> $$Z_0 = \sqrt{\frac{R'+j\omega L'}{G'+j\omega C'}}$$
> Kayıpsız: $Z_0 = \sqrt{L'/C'}$ (gerçel, Ω)

---

## Genel Hat Çözümü

$$V_s(z) = V_0^+ e^{-\gamma z} + V_0^- e^{+\gamma z}$$
$$I_s(z) = \frac{V_0^+}{Z_0}e^{-\gamma z} - \frac{V_0^-}{Z_0}e^{+\gamma z}$$

---

## Yük Empedansı ve Yansıma Katsayısı

Hat uzunluğu $\ell$, yük $Z_L$ (z=0'da):

> [!formul] Yük Yansıma Katsayısı
> $$\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}$$

**Özel durumlar:**

| Yük | $Z_L$ | $\Gamma_L$ | Sonuç |
|-----|-------|-----------|-------|
| Kısa devre | 0 | -1 | Tam yansıma, 180° faz |
| Açık devre | ∞ | +1 | Tam yansıma |
| Uyumlu | $Z_0$ | 0 | Yansıma yok |

---

## Giriş Empedansı

Hat girişindeki empedans ($z=-\ell$):

> [!formul] Giriş Empedansı
> $$Z_{in} = Z_0\frac{Z_L + Z_0\tanh(\gamma\ell)}{Z_0 + Z_L\tanh(\gamma\ell)}$$
> Kayıpsız ($\gamma=j\beta$):
> $$Z_{in} = Z_0\frac{Z_L + jZ_0\tan(\beta\ell)}{Z_0 + jZ_L\tan(\beta\ell)}$$

**Özel uzunluklar (kayıpsız):**

| Uzunluk | $Z_L=0$ (kısa) | $Z_L=\infty$ (açık) |
|---------|----------------|---------------------|
| $\ell=\lambda/4$ | $Z_{in}=Z_0^2/Z_L \to \infty$ | $Z_{in}=0$ |
| $\ell=\lambda/2$ | $Z_{in}=0$ | $Z_{in}=\infty$ |

**$\lambda/4$ dönüştürücü:** $Z_{in}=Z_0^2/Z_L$ → empedans dönüşümü için kullanılır.

---

## Duran Dalga Oranı (SWR / VSWR)

> [!formul] Gerilim Duran Dalga Oranı
> $$\text{SWR} = \frac{V_{max}}{V_{min}} = \frac{1+|\Gamma_L|}{1-|\Gamma_L|}$$

- Uyumlu hat: SWR = 1
- Tam yansıma: SWR = ∞

---

## Güç İletimi

$$P_{av} = \frac{|V_0^+|^2}{2Z_0}\left(1-|\Gamma_L|^2\right)$$

**İletim verimliliği:** $1-|\Gamma_L|^2$

---

## Smith Çizimi (Kavramsal)

<svg width="420" height="250" viewBox="0 0 420 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-emd05" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Root -->
  <rect x="100" y="10" width="220" height="40" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="210" y="27" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">Smith Çizimi</text>
  <text x="210" y="43" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#aac4e8">(Normalize empedans)</text>
  <!-- Fan lines -->
  <line x1="210" y1="50" x2="110" y2="90" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-emd05)"/>
  <line x1="210" y1="50" x2="310" y2="90" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-emd05)"/>
  <!-- Left branch: r=1 circles -->
  <rect x="10" y="92" width="190" height="44" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="105" y="110" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">r = sabit daireler</text>
  <text x="105" y="127" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">Direnç çemberleri</text>
  <!-- Right branch: x circles -->
  <rect x="220" y="92" width="190" height="44" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="315" y="110" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">x = sabit yaylar</text>
  <text x="315" y="127" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">Reaktans eğrileri</text>
  <!-- Sub-branches -->
  <line x1="105" y1="136" x2="105" y2="162" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-emd05)"/>
  <rect x="10" y="164" width="190" height="44" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="105" y="182" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Merkez: Γ = 0</text>
  <text x="105" y="198" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">Z = Z₀ (uyumlu)</text>
  <line x1="315" y1="136" x2="315" y2="162" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-emd05)"/>
  <rect x="220" y="164" width="190" height="44" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="1.5"/>
  <text x="315" y="182" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">Dış halka: |Γ| = 1</text>
  <text x="315" y="198" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#c0392b">Tam yansıma</text>
  <!-- Note -->
  <text x="210" y="236" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="9" fill="#1a1a2e" font-style="italic">Saat yönü → yüke doğru (WTL)  |  Tersi → generatöre (WTG)  |  λ/4 = 180°</text>
</svg>

Smith çiziminde:
- Saat yönü → Yük'e doğru (WTL)
- Saat yönünün tersi → Generatöre doğru (WTG)
- $\lambda/4$ → 180° dönüş

---

> [!sinav] Sınav İpuçları
> - **$Z_0 = \sqrt{L'/C'}$** kayıpsız hat için gerçel
> - **$\Gamma_L = (Z_L-Z_0)/(Z_L+Z_0)$** — pay-payda sırası Maxwell ile aynı mantık
> - **$Z_{in}$ formülünü kayıpsız formda kullan** — sınavda büyük ihtimalle $\alpha=0$
> - **$\lambda/4$ dönüştürücü:** $Z_{in}Z_L = Z_0^2$ — empedans eşleme
> - **SWR = (1+|Γ|)/(1-|Γ|)** — uyumlu hat SWR=1
> - Smith çiziminde **sağ** = yüksek direnç, **sol** = düşük direnç

---

**Bağlantılar:** [[04 Yansıma Kırılma ve Sınır Koşulları]] | [[03 Dalga Yayılması ve Düzlemsel Dalgalar]] | [[EMD Formül Sayfası]]
