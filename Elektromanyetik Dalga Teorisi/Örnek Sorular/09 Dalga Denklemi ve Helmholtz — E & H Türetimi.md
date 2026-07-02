---
tags: [emd, bütünleme, dalga-denklemi, helmholtz, maxwell, fasor, türetim, çözümlü]
---

# 09 — Dalga Denklemi & Helmholtz · E ve H için Tam Türetim

← [[EMD Ana Sayfa]]  ·  Formül tablosu: [[08 Vize & Final — Tüm Formüller Tablosu]]

> [!warning] Hoca bütünleme sınavına bunu çıkaracağını söyledi
> Kaynak: arkadaş notu (WhatsApp, 02.07.2026 02:17)
> Konu: **Kaynak-sız ortamda E ve H için dalga denklemi + Helmholtz denklemi türetimi**

> [!abstract] Bu türetim neyi gösteriyor?
> Maxwell'in 4 denklemi birleştirilince E ve H'nin boş uzayda (veya kaynak-sız dielektrikte) **dalgalar** gibi davrandığı çıkıyor. Türetimin özü: Faraday'ın rotasyonunu al → Ampere'yi içine koy → vektör kimliğini kullan → dalga denklemi çıkar. H için aynısını Ampere'den başlayarak yap.
>
> | Sembol | Açılım |
> |---|---|
> | **kaynak-sız** | $\rho_v = 0$, $\mathbf{J} = 0$, $\sigma = 0$ |
> | $k$ | Dalga sayısı (rad/m): $k = \omega\sqrt{\mu\varepsilon}$ — kayıpsız ortamda $k = \beta$ |
> | $\mathbf{E}_s$, $\mathbf{H}_s$ | Fasor (karmaşık genlik) gösterimi: $\partial/\partial t \to j\omega$ |
> | $\nabla^2\mathbf{A}$ | Vektör Laplacian: $\nabla^2\mathbf{A} = \nabla(\nabla\cdot\mathbf{A}) - \nabla\times(\nabla\times\mathbf{A})$ |

---

## Adım 0 — Kaynak-sız Ortamda Maxwell Denklemleri

Ortam: $\sigma = 0$ (iletken değil), $\rho_v = 0$ (serbest yük yok), $\mathbf{J} = 0$ (serbest akım yok).

Bu durumda 4 Maxwell denklemi şöyle sadeleşir:

| # | Denklem | Sadeleşme |
|---|---|---|
| M1 | $\nabla\cdot\mathbf{D} = \rho_v$ | $\nabla\cdot\mathbf{E} = 0$ |
| M2 | $\nabla\cdot\mathbf{B} = 0$ | $\nabla\cdot\mathbf{H} = 0$ |
| M3 | $\nabla\times\mathbf{E} = -\mu\dfrac{\partial\mathbf{H}}{\partial t}$ | (değişmez) |
| M4 | $\nabla\times\mathbf{H} = \mathbf{J} + \varepsilon\dfrac{\partial\mathbf{E}}{\partial t}$ | $\nabla\times\mathbf{H} = \varepsilon\dfrac{\partial\mathbf{E}}{\partial t}$ |

> [!note]- Neden ∇·E = 0?
> $\nabla\cdot\mathbf{D} = \rho_v$ ve $\mathbf{D}=\varepsilon\mathbf{E}$, homojen ortamda $\varepsilon$ sabit olduğundan $\varepsilon\,\nabla\cdot\mathbf{E} = \rho_v$. Kaynak-sız bölgede $\rho_v = 0$ → $\nabla\cdot\mathbf{E} = 0$. Bu "E'nin kaynak-lavabosu yok" demek — E alan çizgileri kapalı halkalar oluşturur.

---

## Adım 1 — Vektör Kimliği (Çift Rotasyon)

Türetimin kalbi şu vektör kimliğidir — **mutlaka ezberle:**

$$\boxed{\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}}$$

**Kaynak-sız ortamda E için:** $\nabla\cdot\mathbf{E} = 0$ olduğundan:

$$\nabla\times(\nabla\times\mathbf{E}) = \underbrace{\nabla(\nabla\cdot\mathbf{E})}_{=\,\nabla(0)\,=\,\mathbf{0}} - \nabla^2\mathbf{E} = -\nabla^2\mathbf{E}$$

**Kaynak-sız ortamda H için:** $\nabla\cdot\mathbf{H} = 0$ olduğundan:

$$\nabla\times(\nabla\times\mathbf{H}) = \underbrace{\nabla(\nabla\cdot\mathbf{H})}_{=\,\mathbf{0}} - \nabla^2\mathbf{H} = -\nabla^2\mathbf{H}$$

---

## Adım 2 — E için Dalga Denklemi Türetimi

### 2.1 — Faraday'ın her iki tarafının rotasyonunu al

$$\nabla\times(\nabla\times\mathbf{E}) = \nabla\times\!\left(-\mu\frac{\partial\mathbf{H}}{\partial t}\right)$$

Sağ tarafta $\mu$ sabittir, $\nabla\times$ ile $\partial/\partial t$ yer değiştirebilir (Schwarz teoremi):

$$\nabla\times(\nabla\times\mathbf{E}) = -\mu\frac{\partial}{\partial t}(\nabla\times\mathbf{H}) \qquad\cdots(1)$$

### 2.2 — Ampere-Maxwell'i (1)'e koy

$$\nabla\times\mathbf{H} = \varepsilon\frac{\partial\mathbf{E}}{\partial t}$$

Bunu (1)'e yaz:

$$\nabla\times(\nabla\times\mathbf{E}) = -\mu\frac{\partial}{\partial t}\!\left(\varepsilon\frac{\partial\mathbf{E}}{\partial t}\right) = -\mu\varepsilon\frac{\partial^2\mathbf{E}}{\partial t^2} \qquad\cdots(2)$$

### 2.3 — Vektör kimliğini sol tarafa uygula (Adım 1'den)

$$\nabla\times(\nabla\times\mathbf{E}) = -\nabla^2\mathbf{E} \qquad\cdots(3)$$

### 2.4 — (2) ve (3)'ü eşitle

$$-\nabla^2\mathbf{E} = -\mu\varepsilon\frac{\partial^2\mathbf{E}}{\partial t^2}$$

$$\boxed{\nabla^2\mathbf{E} - \mu\varepsilon\frac{\partial^2\mathbf{E}}{\partial t^2} = 0}$$

Bu **E alanı için homojen dalga denklemi**dir. Dalga hızı: $v = 1/\sqrt{\mu\varepsilon}$.

---

## Adım 3 — H için Dalga Denklemi Türetimi

Aynı yöntemi, bu sefer **Ampere-Maxwell'den başlayarak** uygula:

### 3.1 — Ampere-Maxwell'in rotasyonunu al

$$\nabla\times(\nabla\times\mathbf{H}) = \nabla\times\!\left(\varepsilon\frac{\partial\mathbf{E}}{\partial t}\right) = \varepsilon\frac{\partial}{\partial t}(\nabla\times\mathbf{E}) \qquad\cdots(4)$$

### 3.2 — Faraday'ı (4)'e koy

$$\nabla\times\mathbf{E} = -\mu\frac{\partial\mathbf{H}}{\partial t}$$

$$\varepsilon\frac{\partial}{\partial t}\!\left(-\mu\frac{\partial\mathbf{H}}{\partial t}\right) = -\mu\varepsilon\frac{\partial^2\mathbf{H}}{\partial t^2} \qquad\cdots(5)$$

### 3.3 — Vektör kimliğini sol tarafa uygula

$$\nabla\times(\nabla\times\mathbf{H}) = -\nabla^2\mathbf{H} \qquad\cdots(6)$$

### 3.4 — (5) ve (6)'yı eşitle

$$\boxed{\nabla^2\mathbf{H} - \mu\varepsilon\frac{\partial^2\mathbf{H}}{\partial t^2} = 0}$$

> [!tip] Kural: E gördüğün yere H, H gördüğün yere E yaz
> İki denklem **tamamen simetrik** — biri diğerinden E↔H değiştirilerek elde edilir. Hoca da tam bunu söylemiş: "aynı formül, E gördüğün yere H yaz."

---

## Adım 4 — Fasor Formuna Geçiş

Zaman bağımlılığı $e^{j\omega t}$ varsayılırsa:

$$\frac{\partial}{\partial t} \to j\omega \qquad \frac{\partial^2}{\partial t^2} \to (j\omega)^2 = -\omega^2$$

**E için:**

$$\nabla^2\mathbf{E}_s - \mu\varepsilon(-\omega^2)\mathbf{E}_s = 0$$

$$\boxed{\nabla^2\mathbf{E}_s + \mu\varepsilon\omega^2\mathbf{E}_s = 0}$$

**H için:**

$$\boxed{\nabla^2\mathbf{H}_s + \mu\varepsilon\omega^2\mathbf{H}_s = 0}$$

---

## Adım 5 — Helmholtz Denklemi

**Dalga sayısı $k$ tanımı:**

$$k^2 = \mu\varepsilon\omega^2 \implies k = \omega\sqrt{\mu\varepsilon}$$

> [!note]- k ile β arasındaki ilişki
> **Kayıpsız ortamda** ($\sigma=0$): $k = \beta$ — ikisi aynı şey, sadece farklı sembol.
> **Kayıplı ortamda** ($\sigma\neq0$): $k$ **karmaşık** sayı olur: $k = \beta - j\alpha$ (veya $\tilde{k}$ yazılır). Gerçek kısmı faz sabitini, sanal kısmı zayıflamayı verir.

Fasor denklemlerini $k^2$ ile yeniden yaz:

$$\boxed{\nabla^2\mathbf{E}_s + k^2\mathbf{E}_s = 0} \qquad \text{(Helmholtz — E)}$$

$$\boxed{\nabla^2\mathbf{H}_s + k^2\mathbf{H}_s = 0} \qquad \text{(Helmholtz — H)}$$

Bu, **Helmholtz denklemi** veya **vektör Helmholtz denklemi** olarak adlandırılır.

---

## Özet — Tüm Adımlar Bir Arada

```
KAYNAK-SIZ MAXWELL
  ∇·E = 0,  ∇·H = 0
  ∇×E = -μ ∂H/∂t          ... (Faraday)
  ∇×H =  ε ∂E/∂t          ... (Ampere-Maxwell, J=0)

E İÇİN:
  ∇×(∇×E)  =  -μ ∂/∂t (∇×H)     [Faraday rot al]
            =  -με ∂²E/∂t²        [Ampere koy]
  ∇×(∇×E)  =  -∇²E               [∇·E=0 → vektör kimliği]
  ⟹  ∇²E - με ∂²E/∂t² = 0       [Dalga denklemi]
  ⟹  ∇²Eₛ + μεω²Eₛ = 0          [Fasor]
  ⟹  ∇²Eₛ + k²Eₛ = 0            [Helmholtz, k=ω√(με)]

H İÇİN: (Ampere'den başla, Faraday koy → aynı adımlar)
  ⟹  ∇²H - με ∂²H/∂t² = 0
  ⟹  ∇²Hₛ + k²Hₛ = 0
```

---

## Sınavda Nasıl Yazılır? (Adım sayısı = puan)

> [!success] Tam puan için gereken adımlar
> 1. Kaynak-sız Maxwell'i yaz (∇·E=0, ∇×E ve ∇×H ifadeleri)
> 2. Faraday'ın rotasyonunu al: $\nabla\times(\nabla\times\mathbf{E}) = -\mu\,\partial_t(\nabla\times\mathbf{H})$
> 3. Ampere'yi sağ tarafa koy: $= -\mu\varepsilon\,\partial^2_t\mathbf{E}$
> 4. Vektör kimliği + $\nabla\cdot\mathbf{E}=0$: sol taraf $= -\nabla^2\mathbf{E}$
> 5. İkisini eşitle → **dalga denklemi**
> 6. Fasor dönüşümü ($\partial_t^2 \to -\omega^2$) → **fasor form**
> 7. $k^2 = \mu\varepsilon\omega^2$ tanımla → **Helmholtz**
> 8. "H için aynısı" de, E↔H yap → **H Helmholtz**

---

## Bağlantı: k, β ve Dalga Çözümü

Helmholtz'un 1D çözümü ($z$ yönünde yayılma):

$$\mathbf{E}_s(z) = E_0\,e^{-jkz}\,\hat{a}_x$$

Zaman bağımlı forma dön ($e^{j\omega t}$ çarp, gerçel kısmı al):

$$\mathbf{E}(z,t) = E_0\cos(\omega t - kz)\,\hat{a}_x$$

Kayıpsız ortamda $k = \beta$ olduğundan bu, vize S3'teki düzlem dalga ifadesinin ta kendisi:

$$\mathbf{E}(z,t) = E_0\cos(\omega t - \beta z)\,\hat{a}_x \qquad \checkmark$$

**Yani dalga denklemi → Helmholtz → düzlem dalga çözümü** zinciri kapanıyor.
