---
tags: [ss, lti, konvolüsyon, sistem-özellikleri, konu-anlatımı]
---

# 02 — LTI Sistemler ve Konvolüsyon

← [[SS Ana Sayfa]]  |  Örnekler: [[../Örnek Sorular/02 LTI Örnekleri]]

## Özet

> LTI = Doğrusal (Linear) + Zamanla Değişmez (Time-Invariant). Bu iki özellik bir araya gelince sistem tamamen **impuls yanıtı h(t)** ile tanımlanır ve konvolüsyon devreye girer.

---

## 1. Sistem Özellikleri — Hızlı Test Tablosu

| Özellik | Tanım | Test Yöntemi | Bozucu Örnekler |
|---------|-------|--------------|-----------------|
| **Hafızasız** | $y[n]$ sadece $x[n]$'e bağlı | Geçmiş/gelecek terim var mı? | $y[n]=x[n-1]$ → hafızalı |
| **Nedensellik** | $y[n]$ gelecek $x$ değerine bağlı değil | $x[n+k]$, $k>0$ var mı? | $y[n]=x[n+1]$ → nedensel değil |
| **Doğrusallik** | Süperpozisyon: $T\{ax_1+bx_2\}=ay_1+by_2$ | Kare/çarpım terimleri; sıfır girişe sıfır çıkış | $y[n]=x^2[n]$ → doğrusal değil |
| **Zamanla Değişmezlik** | $T\{x[n-n_0]\}=y[n-n_0]$ | Katsayıda bağımsız $n$ var mı? | $y[n]=nx[n]$ → ZD değil |
| **Kararlılık (BIBO)** | $\|x\|<B_x<\infty \Rightarrow \|y\|<B_y<\infty$ | $\sum|h[n]|<\infty$ mı? | Sonsuz birikimli sistem |

> [!sinav] LTI Testi — Sınavda Hızlı Yol
> 1. Sistemde $x[n+k]$ ($k>0$) var mı? → **Nedensel değil**
> 2. Sistemde $n \cdot x[n]$ var mı? → **Zamanla değişir**
> 3. Sistemde $x^2[n]$, $|x[n]|$ var mı? → **Doğrusal değil**
> 4. LTI ise: $\sum_{n=-\infty}^{\infty}|h[n]|<\infty$ → **Kararlı**

---

## 2. Konvolüsyon

### CT Konvolüsyon İntegrali

$$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$$

### DT Konvolüsyon Toplamı

$$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]$$

### Konvolüsyon Adımları (Grafik Yöntem)

<svg width="340" height="298" viewBox="0 0 340 298" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ss02" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <rect x="30" y="10" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="32" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">1. h[k] yaz</text>
  <line x1="170" y1="44" x2="170" y2="60" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ss02)"/>
  <rect x="30" y="62" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="84" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">2. h[−k] al: ters çevir</text>
  <line x1="170" y1="96" x2="170" y2="112" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ss02)"/>
  <rect x="30" y="114" width="280" height="34" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="136" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">3. h[n−k] yaz: n kadar kaydır</text>
  <line x1="170" y1="148" x2="170" y2="164" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ss02)"/>
  <rect x="30" y="166" width="280" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="184" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">4. x[k] ile h[n−k] çarp</text>
  <text x="170" y="200" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">ve k üzerinden topla</text>
  <line x1="170" y1="208" x2="170" y2="224" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-ss02)"/>
  <rect x="30" y="226" width="280" height="34" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="170" y="248" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">5. Her n için tekrar et ✓</text>
  <text x="170" y="280" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e" font-style="italic">y[n] = Σ x[k]·h[n−k]  =  x[n] ∗ h[n]</text>
</svg>

### Önemli Konvolüsyon Özellikleri

| Özellik | İfade |
|---------|-------|
| Değişme | $x*h = h*x$ |
| Birleşme | $(x*h_1)*h_2 = x*(h_1*h_2)$ |
| Dağılma | $x*(h_1+h_2) = x*h_1 + x*h_2$ |
| İmpuls | $x[n]*\delta[n] = x[n]$ |
| Kaydırılmış impuls | $x[n]*\delta[n-n_0] = x[n-n_0]$ |

### Boyut Kuralı

Eğer $x[n]$: $N_1 \le n \le N_2$ ve $h[n]$: $M_1 \le n \le M_2$ aralığında tanımlıysa:

$$y[n] \text{ tanım aralığı: } N_1+M_1 \le n \le N_2+M_2$$
$$\text{Uzunluk: } L_y = L_x + L_h - 1$$

---

## 3. LTI Özdeger (Eigenvalue) Özelliği

LTI sisteme karmaşık üstel sinyal girilirse çıkış **aynı frekans**ta, $H(j\omega)$ ile ölçeklenmiş bir üsteldir:

$$e^{j\omega t} \xrightarrow{\;h(t)\;} H(j\omega)\,e^{j\omega t}$$

$H(j\omega) = \mathcal{F}\{h(t)\}$ sistemin **frekans yanıtı (transfer fonksiyonu)**dır.

Fourier serisi girişi $x(t) = \sum_k a_k e^{jk\omega_0 t}$ için çıkış:

$$y(t) = \sum_{k=-\infty}^{\infty} a_k\,H(jk\omega_0)\,e^{jk\omega_0 t}$$

---

## 4. Seri/Paralel Bağlantılar

**Seri (Cascade):** $h_{toplam}[n] = h_1[n] * h_2[n]$

**Paralel:** $h_{toplam}[n] = h_1[n] + h_2[n]$

---

## 5. Frekans Domeninde Sistem Analizi

$$\boxed{Y(j\omega) = X(j\omega)\cdot H(j\omega)}$$

$H(j\omega) = Y(j\omega)/X(j\omega)$ → sistemin frekans yanıtı.

Fark denkleminden $H$:
- Her gecikme $x[n-k]$ → $e^{-j\omega k}X(e^{j\omega})$
- Denklemdeki tüm terimleri dönüştür, $H = Y/X$ çek.

---

## Bağlantılı Notlar

- [[../Örnek Sorular/02 LTI Örnekleri|Örnek Sorular — LTI ve Konvolüsyon]]
- [[01 Sinyal Sınıflandırması]]
- [[03 Fourier Serisi]]
