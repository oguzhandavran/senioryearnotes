---
tags: [otomatik-kontrol, blok-diyagram, mason, transfer-fonksiyonu]
---

# 01 — Giriş, Kapalı Çevrim ve Blok Diyagramlar

← [[OK Ana Sayfa]]

## Temel Tanımlar

> [!tanim] Otomatik Kontrol
> Kontrol için gerekli tüm işlemlerin bir algoritma ile insana gerek duyulmadan gerçekleştirilmesi.

```mermaid
graph LR
    subgraph Açık Çevrim
        R1[R Giriş] --> C1[Kontrolör] --> P1[Proses] --> Y1[Çıkış]
    end
    subgraph Kapalı Çevrim
        R2[R Giriş] --> sum((+/-)) --> C2[Kontrolör] --> P2[Proses] --> Y2[Çıkış]
        Y2 --> H[Sensör] --> sum
    end
```

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

```mermaid
flowchart LR
    subgraph Toplama noktası ileriye taşıma
        A1[G] --> sum1((+)) --> B1
        subgraph original
        end
    end
```

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

```mermaid
flowchart TD
    A[İşaret akış diyagramını çiz] --> B[İleri yolları bul: P_k]
    B --> C[Tüm döngü kazançlarını bul: L_i]
    C --> D[Temassız döngü çiftleri: L_i L_j]
    D --> E[Δ = 1 - ΣLi + ΣLiLj - ...]
    E --> F[Her ileri yol için Δ_k hesapla]
    F --> G[T = ΣPkΔk / Δ]
```

### Örnek — Mason Formülü

Sistem: $G_1 \to G_2 \to G_3$, geri besleme $H_1$ (iç), $H_2$ (dış)

**İleri yollar:** $P_1 = G_1 G_2 G_3$

**Döngüler:** $L_1 = -G_2 H_1$, $L_2 = -G_1 G_2 G_3 H_2$

**Determinant:** $\Delta = 1 - (L_1 + L_2) = 1 + G_2 H_1 + G_1 G_2 G_3 H_2$

**$\Delta_1$:** $P_1$ ile temas eden döngü yok → $\Delta_1 = 1$

$$\boxed{T = \frac{G_1 G_2 G_3}{1 + G_2 H_1 + G_1 G_2 G_3 H_2}}$$

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

## Ödev-1 — Çok Çevrimli Blok Diyagram (Y/U = ?)

**Verilen:**
$$G_1=\frac{1}{s+1},\quad G_2=\frac{s+0.2}{s},\quad G_3=\frac{5}{s+2},\quad G_4=2,\quad G_5=\frac{10}{s+10},\quad G_6=3$$

**Topoloji:** $U \to G_1 \to \Sigma_1 \to G_2 \to \Sigma_2 \to G_3 \to G_6 \to Y$
- İç geri besleme: $G_3$ çıkışı $\to G_4 \to \Sigma_2$ (negatif)
- Dış geri besleme: $Y \to G_5 \to \Sigma_1$ (negatif)

```mermaid
flowchart LR
    U["U"] --> G1["G1=1/(s+1)"]
    G1 --> S1((" +- "))
    S1 --> G2["G2=(s+0.2)/s"]
    G2 --> S2((" +- "))
    S2 --> G3["G3=5/(s+2)"]
    G3 --> G6["G6=3"]
    G6 --> Y["Y"]
    G3 --> G4["G4=2"]
    G4 --> S2
    Y --> G5["G5=10/(s+10)"]
    G5 --> S1
```

**Çözüm (iç çevrimden dışa):**

**Adım 1 — İç çevrim** ($\Sigma_2, G_3, G_4$):

$$A(s) = \frac{G_3}{1+G_3 G_4} = \frac{\frac{5}{s+2}}{1+\frac{10}{s+2}} = \frac{5}{s+12}$$

**Adım 2 — Dış çevrim** ($\Sigma_1, G_2, A, G_6, G_5$):

$$\frac{Y}{U} = \frac{G_1 \cdot G_2 \cdot A(s) \cdot G_6}{1 + G_2 \cdot A(s) \cdot G_6 \cdot G_5}$$

Numeratör: $G_1 G_2 A G_6 = \dfrac{1}{s+1}\cdot\dfrac{s+0.2}{s}\cdot\dfrac{5}{s+12}\cdot 3 = \dfrac{15(s+0.2)}{s(s+1)(s+12)}$

Paydada $G_2 A G_6 G_5$: $\dfrac{s+0.2}{s}\cdot\dfrac{5}{s+12}\cdot 3\cdot\dfrac{10}{s+10} = \dfrac{150(s+0.2)}{s(s+12)(s+10)}$

$$\boxed{\frac{Y}{U} = \frac{15(s+0.2)}{s(s+1)(s+12) + 150(s+0.2)\frac{s+1}{s+10}}\cdot\frac{1}{1}}$$

> [!sinav] Hızlı Yaklaşım
> İç çevrim sadeleştir → dış çevrim uygula. Negatif geri besleme her zaman: $\frac{G}{1+GH}$

---

## Ödev-2 — İkili Negatif Geri Besleme (Y/U = ?)

**Verilen:**
$$G_1=\frac{s+1}{s},\quad G_2=\frac{s+2}{s+1},\quad G_3=1,\quad G_4=\frac{1}{s^2+s+1},\quad G_5=\frac{10}{s+10}$$

**Topoloji:** $U \to \Sigma_1 \to G_1 \to \Sigma_2 \to G_2 \to \Sigma_3 \to G_4 \to Y$
- 1. iç geri besleme: $G_2$ çıkışı $\to G_3=1 \to \Sigma_2$ (negatif)
- Dış geri besleme: $Y \to G_5 \to \Sigma_1$ (negatif)

```mermaid
flowchart LR
    U["U"] --> S1((" +- "))
    S1 --> G1["G1=(s+1)/s"]
    G1 --> S2((" +- "))
    S2 --> G2["G2=(s+2)/(s+1)"]
    G2 --> S3((" +- "))
    S3 --> G4["G4=1/(s2+s+1)"]
    G4 --> Y["Y"]
    G2 --> G3["G3=1"]
    G3 --> S2
    Y --> G5["G5=10/(s+10)"]
    G5 --> S1
```

**Adım 1 — İç çevrim** ($\Sigma_2, G_2, G_3=1$):

$$B(s) = \frac{G_2}{1+G_2 G_3} = \frac{G_2}{1+G_2} = \frac{\frac{s+2}{s+1}}{1+\frac{s+2}{s+1}} = \frac{s+2}{s+1+s+2} = \frac{s+2}{2s+3}$$

**Adım 2 — Dış çevrim:**

$$\frac{Y}{U} = \frac{G_1 \cdot B(s) \cdot G_4}{1 + G_1 \cdot B(s) \cdot G_4 \cdot G_5}$$

$$G_1 B G_4 = \frac{s+1}{s}\cdot\frac{s+2}{2s+3}\cdot\frac{1}{s^2+s+1}$$

$$\boxed{\frac{Y}{U} = \frac{(s+1)(s+2)}{s(2s+3)(s^2+s+1) + (s+1)(s+2)\cdot\frac{10}{s+10}\cdot s(2s+3)/(s(2s+3))}}$$

---

← [[OK Ana Sayfa]] | → [[02 Kararlılık ve Routh-Hurwitz]]
