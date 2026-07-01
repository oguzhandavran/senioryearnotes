---
tags: [ssi, dsp, z-dönüşümü, roc, pfd, konu-anlatımı]
---

# 02 — Z-Dönüşümü (Teori)

← [[SSI Ana Sayfa]] | Örnekler: [[../Örnek Sorular/02 Z-Dönüşümü Örnekleri]]

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

| $x[n]$                 | $X(z)$                                                           | ROC                                          | <mark style="background: #ABF7F7A6;"></mark> |     |     |     |
| ---------------------- | ---------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------- | --- | --- | --- |
| $\delta[n]$            | $1$                                                              | Tüm $z$                                      |                                              |     |     |     |
| $\delta[n-k]$          | $z^{-k}$                                                         | $z\neq 0$ ($k>0$) veya $z\neq\infty$ ($k<0$) |                                              |     |     |     |
| $u[n]$                 | $\dfrac{1}{1-z^{-1}} = \dfrac{z}{z-1}$                           | $                                            | z                                            | >1$ |     |     |
| $a^n u[n]$             | $\dfrac{1}{1-az^{-1}} = \dfrac{z}{z-a}$                          | $                                            | z                                            | >   | a   | $   |
| $-a^n u[-n-1]$         | $\dfrac{1}{1-az^{-1}}$                                           | $                                            | z                                            | <   | a   | $   |
| $na^n u[n]$            | $\dfrac{az^{-1}}{(1-az^{-1})^2}$                                 | $                                            | z                                            | >   | a   | $   |
| $\cos(\omega_0 n)u[n]$ | $\dfrac{1-\cos(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ | $                                            | z                                            | >1$ |     |     |
| $\sin(\omega_0 n)u[n]$ | $\dfrac{\sin(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$   | $                                            | z                                            | >1$ |     |     |

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

## 7. Pratik Filtre Özellikleri (Ders Tahtası)

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
- [[../Örnek Sorular/02 Z-Dönüşümü Örnekleri]]
- [[../../Sİnyaller ve Sistemler/05 Laplace Dönüşümü|SS: Laplace Dönüşümü]]
