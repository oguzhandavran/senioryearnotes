---
tags: [mst, durum-uzayı, state-space, matris, özdeğer, kontrol, konu-anlatımı]
---

# 03 — Durum Uzayı (State Space)

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/03 Durum Uzayı Örnekleri|03 Durum Uzayı Örnekleri]]

---

## Neden Durum Uzayı?

Transfer fonksiyonu yöntemiyle sistemleri modelleyebiliyoruz:

$$Y(s) = G(s) \cdot U(s)$$

Ama bu yöntem **tek giriş — tek çıkış** sistemlerde işe yarar ve sistemin **iç durumu** hakkında hiçbir şey söylemez.

**Durum uzayı** bize şunları sağlar:
- Birden fazla giriş/çıkış (MIMO sistemler)
- Sistemin içindeki her değişkeni takip etme
- Doğrusal olmayan sistemleri de yazabilme
- Bilgisayar simülasyonu için hazır form

---

## Durum Değişkeni Nedir?

> [!tanim] Durum Değişkeni
> Bir sistemin o anki **iç durumunu tamamen** tarif eden minimum sayıdaki değişken kümesidir. Genellikle **x** ile gösterilir.
>
> Yani: giriş `u(t)` ve başlangıç durumu `x(0)` biliniyorsa, sistemin geleceği tamamen belirlenir.

**Fiziksel kural:** Sistemde kaç tane enerji depolayan eleman varsa, o kadar durum değişkeni gerekir.

| Eleman | Durum değişkeni |
|--------|----------------|
| Kondansatör | $V_C$ (gerilim) |
| Bobin (endüktans) | $i_L$ (akım) |
| Yay (mekanik) | $x$ (konum) |
| Kütle | $v$ (hız) |

---

## Genel Form

Her sistem bu iki denklemle yazılır:

$$\boxed{\dot{x}(t) = Ax(t) + Bu(t)}$$
$$\boxed{y(t) = Cx(t) + Du(t)}$$

| Sembol | Boyut | Ne anlama gelir |
|--------|-------|----------------|
| $x$ | $n \times 1$ | Durum vektörü (iç durum) |
| $u$ | $r \times 1$ | Giriş vektörü |
| $y$ | $m \times 1$ | Çıkış vektörü |
| $A$ | $n \times n$ | Sistem matrisi — sistemin kendi dinamiği |
| $B$ | $n \times r$ | Giriş matrisi — girişin duruma etkisi |
| $C$ | $m \times n$ | Çıkış matrisi — durumdan çıkışa geçiş |
| $D$ | $m \times r$ | İletim matrisi — çoğu fiziksel sistemde **0** |

> [!tip] Sezgi
> $A$ matrisi: "Sistem kendi başına nasıl davranır?"
> $B$ matrisi: "Giriş uyguladığımda sistemi nasıl iter?"
> $C$ matrisi: "Durumun hangi kombinasyonu ölçülebilir?"

---

## RC Devresi — Adım Adım Türetme

```
u(t) → [C][R(t)] → y(t)
        ↑kondansatör
```

**Adım 1 — Durum değişkenini seç:**
$x = V_C$ (kondansatör gerilimi, devrenin "hafızası")

**Adım 2 — KVL yaz:**
$$u(t) = V_C(t) + R(t) \cdot i(t)$$

**Adım 3 — $i = C\dot{V}_C$ koyarak $\dot{x}$'i bul:**

Kondansatörde akım-gerilim ilişkisi: $i = C\dot{V}_C = C\dot{x}$

Bunu Adım 2'deki KVL'ye koy:
$$u(t) = x + R \cdot C \cdot \dot{x}$$

$\dot{x}$'i yalnız bırak (her iki taraftan $x$'i çıkar, $RC$'ye böl):
$$R \cdot C \cdot \dot{x} = u - x$$

$$\boxed{\dot{x}(t) = \frac{u(t)}{RC} - \frac{x(t)}{RC}}$$

> [!tip] Sezgi
> - $+\dfrac{u}{RC}$ → giriş kondansatörü **doldurur**
> - $-\dfrac{x}{RC}$ → zaten doluysa dolma hızı **yavaşlar** (negatif geri besleme)
>
> Bu, $\dot{x} = Ax + Bu$ formunun ta kendisi: $A = -\dfrac{1}{RC}$, $B = \dfrac{1}{RC}$

**Adım 4 — Çıkış denklemi:**
$$y(t) = u(t) - V_C(t) = -x(t) + u(t)$$

Matris formunda:

$$A = \left[\frac{-1}{RC}\right], \quad B = \left[\frac{1}{RC}\right], \quad C = [-1], \quad D = [1]$$

---

## RLC Devresi — 2 Durum Değişkeni

İki enerji depolayan eleman var → 2 durum değişkeni gerekir:

$$x_1 = V_C \quad \text{(kondansatör gerilimi)}$$
$$x_2 = i_L \quad \text{(bobin akımı)}$$

Türetilen state denklemleri:

$$\dot{x}_1 = \frac{x_2}{C}  \tag{1}$$

$$\dot{x}_2 = \frac{u(t)}{L} - \frac{x_1}{L} - \frac{R}{L} x_2  \tag{2}$$

Matris formunda yazarsak:

$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} 0 & \frac{1}{C} \\ -\frac{1}{L} & -\frac{R}{L} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ \frac{1}{L} \end{bmatrix} u$$

Bu tam olarak $\dot{x} = Ax + Bu$ formudur.

---

## Doğrusal Olmayan Sistemlerde State Space

### Neden farklı?

Şimdiye kadar gördüğümüz $\dot{x} = Ax + Bu$ formunda $A$ ve $B$ **sabit** matrislerdi — sistem her noktada aynı şekilde davranıyordu.

Gerçek dünyada çoğu sistem doğrusal değildir: sarkaç, uçak, robot kolu… Bunlarda $A$ ve $B$ yok, onların yerine **genel fonksiyonlar** var:

$$\dot{x}(t) = f(x,\, u,\, t) \qquad \text{(durum denklemi)}$$
$$y(t) = h(x,\, u,\, t) \qquad \text{(çıkış denklemi)}$$

> [!info] Ne anlama geliyor?
> - $f$ ve $h$ herhangi bir fonksiyon olabilir: $\sin$, $x^2$, çarpımlar…
> - Matris yok, sabit katsayı yok — her durum noktasında sistem farklı davranır.
> - $t$ argümanı varsa sistem **zamana bağımlı** (time-varying); yoksa **zamanla değişmeyen** (time-invariant, LTI).

---

### Somut Örnek: Sarkaç

Bir sarkacın hareketi:
$$ml^2\ddot{\theta} + b\dot{\theta} + mgl\sin\theta = \tau$$

**Adım 1 — Durum değişkenlerini seç:**

İki türev var ($\theta$ ve $\dot{\theta}$) → 2 durum değişkeni:
$$x_1 = \theta \quad \text{(açı)}, \qquad x_2 = \dot{\theta} \quad \text{(açısal hız)}$$

**Adım 2 — $\dot{x}$'leri yaz:**

$$\dot{x}_1 = x_2$$

$$\dot{x}_2 = \frac{\tau}{ml^2} - \frac{b}{ml^2}x_2 - \frac{g}{l}\sin x_1$$

**Adım 3 — Vektör formuna dök:**

$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} x_2 \\ \dfrac{\tau}{ml^2} - \dfrac{b}{ml^2}x_2 - \dfrac{g}{l}\sin x_1 \end{bmatrix}$$

Bu $f(x, u)$ fonksiyonudur. $\sin x_1$ terimi yüzünden **doğrusal değil** → $A$ matrisi yazılamaz.

**Adım 4 — Ne yapılır?**

Denge noktası bul (örn. $\theta = 0$, $\dot{\theta} = 0$) → orada **doğrusallaştır**:
$$\sin\theta \approx \theta \quad \text{(küçük açı için)}$$

Böylece tekrar $\dot{x} = Ax + Bu$ formuna dönülür ve klasik analiz yapılır.

> [!warning] Genel Kural
> Doğrusal olmayan sistem gelirse:
> 1. Durum değişkenlerini seç ($n$ tane türev varsa $n$ tane $x$)
> 2. Her $\dot{x}_i$'yi sistemi tanımlayan denklemden yaz
> 3. Vektör formuna dök → $\dot{x} = f(x, u)$
> 4. Analiz için denge noktasında doğrusallaştır → bkz. [[04 Doğrusallaştırma]]

---

### Zamana Bağlı Olmayan Form (Time-Invariant)

Eğer $f$ ve $h$ içinde **$t$ açıkça geçmiyorsa** — yani sistem parametreleri zamanla değişmiyorsa — $t$ argümanı düşer:

$$\dot{x} = f(x,\, u), \qquad y = h(x,\, u)$$

> [!example] Fark nedir?
> | | Zamana bağımlı | Zamana bağımsız |
> |---|---|---|
> | **Örnek** | $\dot{x} = -\frac{x}{R(t)C}$ — $R$ zamanla değişiyor | $\dot{x} = -\frac{x}{RC}$ — $R$, $C$ sabit |
> | **$t$ argümanı** | $f(x, u, \mathbf{t})$ | $f(x, u)$ |
> | **Analiz** | Zor, genel çözüm yok | Laplace, matris üstelleri kullanılabilir |
>
> **Kural:** Sarkacın $m$, $l$, $g$ sabitleri değişmiyorsa → time-invariant. RC devresi sabit dirençle → time-invariant.

---

## State-Space → Transfer Fonksiyonu

Laplace dönüşümü ($x(0) = 0$):

$$sX(s) = AX(s) + BU(s) \implies X(s) = (sI - A)^{-1}BU(s)$$

$$\boxed{G(s) = C(sI - A)^{-1}B + D}$$

> [!sinav] Sınav İpucu
> $sI - A$ matrisinin tersini alıp $C$ ile soldan, $B$ ile sağdan çarp, $D$ ekle — bu formül sınavda çok çıkar.

---

## Transfer Fonksiyonu → State-Space (Kontrolör Kanonik Form)

$$G(s) = \frac{b_{n-1}s^{n-1} + \ldots + b_1 s + b_0}{s^n + a_{n-1}s^{n-1} + \ldots + a_1 s + a_0}$$

**Durum değişkenleri:** $x_1 = y$, $x_2 = \dot{y}$, ..., $x_n = y^{(n-1)}$

$$A = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}$$

$$C = \begin{bmatrix} b_0 & b_1 & \cdots & b_{n-1} \end{bmatrix}, \quad D = 0$$

> [!tip] Ezber Kolaylığı
> $A$ matrisinin **son satırı** = paydanın katsayıları eksi işaretle: $[-a_0, -a_1, \ldots, -a_{n-1}]$
> Geri kalan satırlar: birim matrisin bir sağa kaymış hali.

---

## Özdeğer Analizi (Kararlılık)

Sistemin özdeğerleri = $A$ matrisinin özdeğerleri = transfer fonksiyonunun **kutupları**

$$\det(\lambda I - A) = 0 \quad \text{(karakteristik denklem)}$$

| Özdeğer konumu | Sistem davranışı |
|----------------|-----------------|
| Tüm $\text{Re}(\lambda) < 0$ | **Kararlı** — sönümlenir |
| Herhangi $\text{Re}(\lambda) > 0$ | **Kararsız** — büyür |
| $\text{Re}(\lambda) = 0$ | Sınır — salınır |

---

## Kontrol Edilebilirlik ve Gözlenebilirlik

**Kontrol edilebilirlik:** Her duruma giriş aracılığıyla ulaşılabilir mi?

$$\mathcal{C} = \begin{bmatrix} B & AB & A^2B & \cdots & A^{n-1}B \end{bmatrix}$$

Kontrol edilebilir $\iff \text{rank}(\mathcal{C}) = n$

**Gözlenebilirlik:** Her iç durum, çıkışı ölçerek anlaşılabilir mi?

$$\mathcal{O} = \begin{bmatrix} C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1} \end{bmatrix}$$

Gözlenebilir $\iff \text{rank}(\mathcal{O}) = n$

---

## Özet: Türetme Adımları

<svg width="340" height="346" viewBox="0 0 340 346" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mst03" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <rect x="30" y="10" width="280" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="28" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">1. Sistemi tanımla</text>
  <text x="170" y="44" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">(elektrik devre, mekanik sistem…)</text>
  <line x1="170" y1="52" x2="170" y2="68" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst03)"/>
  <rect x="30" y="70" width="280" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="88" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">2. Enerji depolayan elemanları say</text>
  <text x="170" y="104" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">→ kaç durum değişkeni gerekiyor?</text>
  <line x1="170" y1="112" x2="170" y2="128" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst03)"/>
  <rect x="30" y="130" width="280" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="148" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">3. Durum değişkenlerini seç</text>
  <text x="170" y="164" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">V_C, i_L, x(t), v(t) …</text>
  <line x1="170" y1="172" x2="170" y2="188" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst03)"/>
  <rect x="30" y="190" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="212" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">4. KVL / KCL / Newton yasası yaz</text>
  <line x1="170" y1="224" x2="170" y2="240" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst03)"/>
  <rect x="30" y="242" width="280" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="260" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">5. ẋ = f(x, u) formuna sok</text>
  <text x="170" y="276" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">(her denklem: türev = …)</text>
  <line x1="170" y1="284" x2="170" y2="300" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst03)"/>
  <rect x="30" y="302" width="280" height="34" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="316" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">6. Matris formuna yaz ✓</text>
  <text x="170" y="330" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#aac4e8">ẋ = Ax + Bu,   y = Cx + Du</text>
</svg>

---

> [!sinav] Sınav İpucu
> - $G(s) = C(sI-A)^{-1}B + D$ → sınavda mutlaka çıkar
> - Özdeğerler → $\det(\lambda I-A) = 0$ → kararlılık
> - Faz değişkenleri: son satır $= [-a_0, -a_1, \ldots, -a_{n-1}]$
> - Elektrik sistemlerde durum değişkenleri = **kondansatör gerilimleri** + **bobin akımları**
> - Mekanik sistemlerde = **konum** + **hız**
> - SS ve TF aynı sistemi tarif eder — özdeğerler = kutuplar
