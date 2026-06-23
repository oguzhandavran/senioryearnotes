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

```mermaid
graph TD
    A["Smith Çizimi\n(Normalized Impedance)"] --> B["r=1 Dairesi\n→ Γ çemberi"]
    A --> C["x=const Dairesi\n→ Reaktans eğrisi"]
    B --> D["Merkez: uyumlu nokta\nΓ=0, Z=Z₀"]
    C --> E["Dış halka: |Γ|=1\nTam yansıma"]
```

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
