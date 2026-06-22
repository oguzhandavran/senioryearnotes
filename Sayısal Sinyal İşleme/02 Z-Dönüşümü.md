---
tags: [ssi, dsp, z-dönüşümü, roc, pfd]
---

# 02 — Z-Dönüşümü

← [[SSI Ana Sayfa]]

## Özet

> Z-dönüşümü, Laplace'ın ayrık zamanlı karşılığı. $z = e^{sT}$. ROC kritik. Ters Z için PFD yöntemi kullan.

---

## 1. Tanım

$$\boxed{X(z) = \mathcal{Z}\{x[n]\} = \sum_{n=-\infty}^{\infty} x[n]\, z^{-n}}$$

$z \in \mathbb{C}$ — karmaşık değişken.

**DTFT ile ilişki:** $z = e^{j\omega}$ koyulursa Z-dönüşümü → DTFT olur (ROC birim çemberi içeriyorsa).

**Laplace ile ilişki:** $z = e^{sT}$ — birim çember ($|z|=1$) → $j\omega$ ekseni.

---

## 2. Yakınsama Bölgesi (ROC)

> [!tanim] ROC
> Z-dönüşümünün yakınsadığı (sonsuz serisinin toplandığı) $z$ düzlemindeki bölge.

### ROC Kuralları

| Sinyal Türü                    | ROC                                              |     |                                       |
| ------------------------------ | ------------------------------------------------ | --- | ------------------------------------- |
| Sağ taraflı: $x[n]=0$, $n<N_1$ | $                                                | z   | > r_{max}$ (en büyük kutuptan dışarı) |
| Sol taraflı: $x[n]=0$, $n>N_2$ | $                                                | z   | < r_{min}$ (en küçük kutuptan içeri)  |
| Çift taraflı                   | Halka bölge: $r_1 <                              | z   | < r_2$                                |
| Sonlu uzunluklu                | Tüm $z$ (muhtemelen $z=0$ veya $z=\infty$ hariç) |     |                                       |

### ROC ve Kararlılık

- **Nedensel + kararlı**: ROC birim çemberi içersin ($|z|>$ tüm kutuplar + kutuplar $|z|<1$)
- Birim çember ROC'da ise DTFT mevcut

---

## 3. Temel Z-Dönüşümü Çiftleri

| $x[n]$ | $X(z)$ | ROC |
|--------|--------|-----|
| $\delta[n]$ | $1$ | Tüm $z$ |
| $\delta[n-k]$ | $z^{-k}$ | $z\neq 0$ ($k>0$) veya $z\neq\infty$ ($k<0$) |
| $u[n]$ | $\dfrac{1}{1-z^{-1}} = \dfrac{z}{z-1}$ | $|z|>1$ |
| $a^n u[n]$ | $\dfrac{1}{1-az^{-1}} = \dfrac{z}{z-a}$ | $|z|>|a|$ |
| $-a^n u[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $|z|<|a|$ |
| $na^n u[n]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $|z|>|a|$ |
| $\cos(\omega_0 n)u[n]$ | $\dfrac{1-\cos(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ | $|z|>1$ |
| $\sin(\omega_0 n)u[n]$ | $\dfrac{\sin(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ | $|z|>1$ |

---

## 4. Z-Dönüşümü Özellikleri

| Özellik | $x[n] \xleftrightarrow{Z} X(z)$ |
|---------|--------------------------------|
| Doğrusallik | $ax[n]+by[n] \leftrightarrow aX(z)+bY(z)$ |
| Zaman kayması | $x[n-k] \leftrightarrow z^{-k}X(z)$ |
| Ölçekleme | $a^n x[n] \leftrightarrow X(z/a)$ |
| Zaman ters çevirme | $x[-n] \leftrightarrow X(1/z)$ |
| Konvolüsyon | $x[n]*h[n] \leftrightarrow X(z)\cdot H(z)$ |
| Çarpma | $nx[n] \leftrightarrow -z\dfrac{dX(z)}{dz}$ |
| **Başlangıç değer** | $x[0] = \lim_{z\to\infty}X(z)$ |
| **Son değer** | $x[\infty] = \lim_{z\to 1}(z-1)X(z)$ (kararlı sistemler) |

---

## 5. Ters Z-Dönüşümü — PFD Yöntemi

**Adımlar:**
1. $X(z)/z$ ya da doğrudan $X(z)$'yi kısmi kesirlere ayır
2. Katsayıları hesapla
3. Z çiftlerini kullan

### Örnek 1 (Sınav Sorusundan)

$$X(z) = \frac{1}{1-\frac{1}{2}z^{-1}-\frac{1}{6}z^{-2}}$$

Pay: 1. Payda'yı çarpanla: $(1-\frac{1}{3}z^{-1})(1+\frac{1}{2}z^{-1}) \cdot\ldots$ — dikkatli çarpanla.

Genel yöntem: $z^{-1} = x$ koy →

$$X = \frac{1}{(1-\frac{1}{3}z^{-1})(1+\frac{1}{2}z^{-1})} = \frac{A}{1-\frac{1}{3}z^{-1}} + \frac{B}{1+\frac{1}{2}z^{-1}}$$

$A = \left.(1-\frac{1}{3}z^{-1})X(z)\right|_{z^{-1}=3} = \frac{1}{1+\frac{3}{2}} = \frac{2}{5}$

$B = \left.(1+\frac{1}{2}z^{-1})X(z)\right|_{z^{-1}=-2} = \frac{1}{1+\frac{2}{3}} = \frac{3}{5}$

$$x[n] = \frac{2}{5}\left(\frac{1}{3}\right)^n u[n] + \frac{3}{5}\left(-\frac{1}{2}\right)^n u[n]$$

### Örnek 1b — Tam Çözüm: ROC ile Doğru Ters Z

$$X(z) = \frac{z^2}{(z-1)(z-2)}, \quad \text{ROC: } |z|>2 \text{ (nedensel)}$$

$X(z)/z = z/[(z-1)(z-2)] = A/(z-1) + B/(z-2)$

$A = (z-1)\cdot X(z)/z\big|_{z=1} = 1/(1-2) = -1$

$B = (z-2)\cdot X(z)/z\big|_{z=2} = 2/(2-1) = 2$

$X(z)/z = -1/(z-1) + 2/(z-2) \implies X(z) = \frac{-z}{z-1} + \frac{2z}{z-2}$

$$\boxed{x[n] = -u[n] + 2\cdot2^n u[n] = (-1+2^{n+1})u[n]}$$

*ROC $|z|<1$ olsaydı: $x[n] = u[-n-1] - 2\cdot2^n u[-n-1]$ (sol taraflı sinyal)*

### Örnek 2 — Birim Gecikme İspatı (Sınav Sorusu)

$$X(z) = \sum_{n=-\infty}^{\infty}x[n]z^{-n}$$

Gecikmiş: $\mathcal{Z}\{x[n-1]\} = \sum_{n}x[n-1]z^{-n}$. $m = n-1$ koy:

$$= \sum_{m}x[m]z^{-(m+1)} = z^{-1}\sum_m x[m]z^{-m} = z^{-1}X(z)$$ ✅

---

## 6. Transfer Fonksiyonu (Z domeninde)

Fark denklemi:
$$\sum_{k=0}^{N}a_k y[n-k] = \sum_{k=0}^{M}b_k x[n-k]$$

Z-dönüşümü:
$$H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{k=0}^{M}b_k z^{-k}}{\sum_{k=0}^{N}a_k z^{-k}}$$

### Kutup-Sıfır Diyagramı

- **Kutuplar** ($D(z)=0$): $|$kutup$| < 1$ ise kararlı nedensel
- **Sıfırlar** ($N(z)=0$): genlik sıfırladığı frekanslar

> [!sinav] Kararlılık
> Nedensel sistem kararlı ↔ tüm kutuplar **birim çemberin içinde** ($|p_k| < 1$)

---

## 7. Ders Tahtası — Pratik Filtre Özellikleri

*Not: Bu ders içeriği [[04 Sayısal Filtre Tasarımı]] ile doğrudan bağlantılıdır.*

Pratik filtrelerde ideal dikdörtgen frekans yanıtı gerçeklenemez. Gerçek filtre özellikleri:

| Bölge | İdeal | Gerçek |
|-------|-------|--------|
| Geçiş bandı | $\|H\| = 1$ (düz) | Salınımlı (ripple) |
| Geçiş aralığı | Anlık kesim | Geçiş bandı ($\Delta\omega$) |
| Söndürme bandı | $\|H\| = 0$ | Küçük ama sıfır değil |

**Genlik bozumu** → Genlik spektrumundan kaynaklanır
**Faz bozumu** → Faz spektrumundan kaynaklanır

Filtre türleri arası ilişkiler:
$$H_{HP}(e^{j\omega}) = 1 - H_{LP}(e^{j\omega})$$
$$H_{BS}(e^{j\omega}) = 1 - H_{BP}(e^{j\omega})$$
$$H_{BP}(e^{j\omega}) = H_{HP}(e^{j\omega}) \cdot H_{LP}(e^{j\omega})$$

---

## Bağlantılı Notlar

- [[01 Ayrık Zaman Sinyalleri ve Örnekleme]]
- [[03 DFT ve FFT]]
- [[../Sİnyaller ve Sistemler/05 Laplace Dönüşümü|SS: Laplace Dönüşümü]]
