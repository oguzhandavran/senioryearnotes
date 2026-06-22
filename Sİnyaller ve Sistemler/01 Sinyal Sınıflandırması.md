---
tags: [ss, sinyal, sınıflandırma]
---

# 01 — Sinyal Sınıflandırması

← [[SS Ana Sayfa]]

## Özet

> Sinyaller zamanın türüne (CT/DT) ve genlik özelliklerine göre sınıflandırılır. Sınav için: enerji/güç hesabı, çift/tek simetri, temel sinyaller kritik.

---

## 1. CT vs DT Sinyaller

> [!tanim] Tanım
> - **CT (Sürekli-Zaman):** $x(t)$, $t \in \mathbb{R}$ — her anda tanımlı
> - **DT (Ayrık-Zaman):** $x[n]$, $n \in \mathbb{Z}$ — sadece tam sayılarda tanımlı

| Özellik | CT $x(t)$ | DT $x[n]$ |
|---------|-----------|-----------|
| Tanım kümesi | $t \in \mathbb{R}$ | $n \in \mathbb{Z}$ |
| Gösterim | Yuvarlak parantez | Köşeli parantez |
| Matematik araç | İntegral, türev | Toplam, fark |
| $x(2.5)$ | Tanımlı ✅ | Tanımsız ❌ |
| Örnekleme | $x[n] = x(nT)$ | doğal |

> [!warning] Dikkat
> Sınıflandırma **zaman eksenine** göredir, genliğe değil! Genlik sürekli olsa bile DT sinyal olabilir.

---

## 2. Enerji ve Güç

### CT Sinyaller

$$E_\infty = \int_{-\infty}^{\infty} |x(t)|^2 \, dt$$

$$P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 \, dt$$

### DT Sinyaller

$$E_\infty = \sum_{n=-\infty}^{\infty} |x[n]|^2$$

$$P_\infty = \lim_{N \to \infty} \frac{1}{2N+1} \sum_{n=-N}^{N} |x[n]|^2$$

### Sınıflandırma Kuralı

| Koşul | Sinyal Türü |
|-------|------------|
| $E_\infty < \infty$ | **Enerji sinyali** (→ $P_\infty = 0$) |
| $0 < P_\infty < \infty$ | **Güç sinyali** (→ $E_\infty = \infty$) |
| $E_\infty = \infty$ ve $P_\infty = \infty$ | Ne enerji ne güç |

> [!sinav] Sınav İpucu
> - Periyodik sinyaller → **güç sinyali** (enerji sonsuz)
> - Sonlu süreli sinyaller → **enerji sinyali**
> - $x[n] = a^n u[n]$: $|a|<1$ → enerji, $|a|>1$ → ikisi de değil

**Örnek:** $x[n] = (1/2)^n u[n]$

$$E_\infty = \sum_{n=0}^{\infty} \left(\frac{1}{4}\right)^n = \frac{1}{1-1/4} = \frac{4}{3} < \infty \Rightarrow \text{Enerji sinyali}$$

---

## 3. Periyodik Sinyaller

**CT:** $x(t) = x(t+T)$, temel periyot $T_0$ (en küçük pozitif $T$)

**DT:** $x[n] = x[n+N]$, temel periyot $N$ (en küçük pozitif **tam sayı** $N$)

> [!warning] DT Periyodiklik Dikkat
> $x[n] = e^{j\omega_0 n}$ periyodik olması için $\omega_0 / (2\pi)$ **rasyonel** olmalı.
> 
> Örnek: $\cos(0.3\pi n)$ → periyodik ($N = 20$) ✅
> $\cos(n)$ → **periyodik değil** ($1/(2\pi)$ irrasyonel) ❌

---

## 4. Çift ve Tek Sinyaller

> [!tanim] Tanım
> - **Çift (Even):** $x(-t) = x(t)$ veya $x[-n] = x[n]$
> - **Tek (Odd):** $x(-t) = -x(t)$ veya $x[-n] = -x[n]$

Her sinyal ayrıştırılabilir:

$$x(t) = \underbrace{\frac{x(t)+x(-t)}{2}}_{x_e(t) \text{ çift}} + \underbrace{\frac{x(t)-x(-t)}{2}}_{x_o(t) \text{ tek}}$$

> [!sinav] Özellikler
> - Çift × çift = çift; tek × tek = çift; çift × tek = tek
> - $\int_{-T}^{T} x_o(t)\,dt = 0$ (tek fonksiyonun simetrik integrali sıfır)

---

## 5. Temel Sinyaller

### Birim Dürtü (Impuls)

**DT:** $\delta[n] = \begin{cases}1 & n=0 \\ 0 & n\neq 0\end{cases}$

**CT:** $\delta(t)$ — Dirac delta (sifting özelliği):
$$\int_{-\infty}^{\infty} x(t)\,\delta(t-t_0)\,dt = x(t_0)$$

### Birim Basamak

$$u[n] = \begin{cases}1 & n \geq 0 \\ 0 & n < 0\end{cases} \qquad u(t) = \begin{cases}1 & t > 0 \\ 0 & t < 0\end{cases}$$

**İlişki:** $\delta[n] = u[n] - u[n-1]$ ve $u[n] = \sum_{k=-\infty}^{n}\delta[k]$

CT'de: $\delta(t) = \frac{d}{dt}u(t)$

### Üstel Sinyal

$$x(t) = C e^{at}, \quad x[n] = C \alpha^n$$

- $a$ veya $\alpha$ reel: büyüme/sönüm
- $a$ veya $\alpha$ karmaşık: sinüzoidal × üstel

### Sinüzoidal

$$x(t) = A\cos(\omega_0 t + \phi) \qquad x[n] = A\cos(\Omega_0 n + \phi)$$

---

## 6. Ders Tahtası — Arş. Gör. Ecmel TERZİ

### Sinyal Analizi Çalışılan Örnekler

#### Örnek DT Sinyal — Tam Özellik Analizi

Verilen: $x[n]$ yalnızca $n \in \{-2, -1, 0, 1, 2, 5\}$ noktalarında sıfırdan farklı, değer kümesi $x[n] \in \{1, 2, 3\}$

| Özellik | Test | Sonuç |
|---------|------|-------|
| Zaman türü | $n$ tam sayı indeks | **Ayrık zamanlı (DT)** |
| Genlik türü | Değerler sıfır ve pozitif tam sayılar | **Ayrık değer → Sayısal (Dijital)** |
| Sınırlılık | $|x[n]| \leq 3 < \infty$ | **Sınırlı** |
| Periyodiklik | Sonlu destek → $x[n] \neq x[n+N]$ | **Aperiyodik** |
| Simetri | $x[-n] = x[n]$? (kontrol: $x[5] \neq x[-5]$) | **Çift değil** |
| Enerji | $E = \sum\|x[n]\|^2 = 13 < \infty$ | **Enerji sinyali**, $P = 0$ |

Enerji hesabı — sıfırdan farklı noktaların kareleri toplamı:
$$E_\infty = \sum_{n \in \{-2,-1,0,1,2,5\}} |x[n]|^2 = 13$$

**Dijital bit derinliği:** $|x[n]|_{\max} = 3 < 2^2 = 4$ → en az 2-bit çözünürlük gerekli

**Dikdörtgen pencere gösterimi ile:**
$$y[n] = u[n-1] - u[n-4] = \begin{cases}1 & 1 \leq n \leq 3 \\ 0 & \text{diğer}\end{cases}$$

#### Örnek CT Sinyal — Tam Özellik Analizi

Verilen: $x(t)$ sinüzoidal benzeri, $t \in (-2,\, 6)$, $x(t) \in (-2,\, 5)$

| Özellik | Test | Sonuç |
|---------|------|-------|
| Zaman türü | $t \in \mathbb{R}$ | **Sürekli zamanlı (CT)** |
| Genlik türü | Sürekli aralık | **Sürekli değer → Analog** |
| Sınırlılık | $|x(t)| \leq 5 < \infty$ | **Sınırlı** |
| Simetri | $x(t) \neq x(-t)$ | **Asimetrik (ne çift ne tek)** |
| Periyodiklik | Sonlu destek $(t \notin (-2,6))$ | **Aperiyodik** |
| Enerji | $\int_{-2}^{6} |x(t)|^2\,dt \leq B_x < \infty$ | **Enerji sinyali** |

---

### Delta Fonksiyonu ile Örnekleme Özelliği

Herhangi bir ayrık sinyal delta dizisi cinsinden:
$$z[n] = \sum_{k=-\infty}^{\infty} z[k]\,\delta[n-k]$$

**Sızdırma (sifting) özelliği:** $z[n] \cdot \delta[n-k_0] = z[k_0]\cdot\delta[n-k_0]$

Örnek: $z[n] = 2\delta[n] + 1\cdot\delta[n-2] + 2\cdot\delta[n-3]$ için:
$$w[n] = z[n]\cdot\delta[n-2] = z[2]\cdot\delta[n-2] = 1\cdot\delta[n-2]$$

---

### DT Konvolüsyon — Problem 5

$$x[n] = \delta[n] + 2\delta[n-1] - \delta[n-3], \qquad h[n] = 2\delta[n+1] + 2\delta[n-1]$$

Süperpozisyon ilkesi ile konvolüsyon:
$$y[n] = x[n]*h[n] = 1\cdot h[n] + 2\cdot h[n-1] + (-1)\cdot h[n-3]$$

Her terimi hesapla:
$$h[n] = 2\delta[n+1] + 2\delta[n-1]$$
$$2h[n-1] = 2\bigl(2\delta[n]+2\delta[n-2]\bigr) = 4\delta[n]+4\delta[n-2]$$
$$-h[n-3] = -\bigl(2\delta[n-2]+2\delta[n-4]\bigr) = -2\delta[n-2]-2\delta[n-4]$$

Topla (aynı gecikmedeki katsayıları birleştir):
$$\boxed{y[n] = 2\delta[n+1] + 4\delta[n] + 2\delta[n-1] + (4-2)\delta[n-2] - 2\delta[n-4]}$$
$$= 2\delta[n+1] + 4\delta[n] + 2\delta[n-1] + 2\delta[n-2] - 2\delta[n-4]$$

| $n$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|-----|------|------|-----|-----|-----|-----|-----|
| $y[n]$ | $0$ | $2$ | $4$ | $2$ | $2$ | $0$ | $-2$ |

> [!sinav] DT Konvolüsyon Kural
> $x[n] = \sum_k a_k\,\delta[n-n_k]$ ise $y[n] = \sum_k a_k\,h[n-n_k]$
> Her delta terimi için $h[n]$'yi kaydır ve ölçekle, sonra topla.

### CT Konvolüsyon — Üçgen × Dikdörtgen (Problem 4)

$$x(t) = \begin{cases}t+1, & 0 \leq t \leq 1 \\ 2-t, & 1 < t \leq 2 \\ 0, & \text{diğer}\end{cases}, \qquad h(t) = u(t+2) - u(t-5)$$

$h(t)$ genişliği 7 olan dikdörtgen pencere $[-2,\,5]$ üzerinde.

$y(t) = x(t)*h(t)$: kayan pencere yöntemiyle bölgeler halinde hesaplanır.

$h(t-\tau) = 1$ koşulu: $t-5 \leq \tau \leq t+2$; $x(\tau) \neq 0$ koşulu: $0 \leq \tau \leq 2$

**Bölgesel hesap:**

| Bölge | Kesişim sınırları | $y(t)$ |
|-------|-------------------|--------|
| $t < -2$ | Kesişim yok | $0$ |
| $-2 \leq t < 0$ | $[0,\,t+2]$ | $\int_0^{t+2}(\tau+1)\,d\tau = \tfrac{(t+2)^2}{2} + (t+2) - \tfrac{(t+2)^2}{2}$ |
| $0 \leq t < 1$ | $[0,\,t]$ (kısmen) ve $[t,\,t+2]$ | $\int_0^{t}(\tau+1)\,d\tau = \tfrac{t^2}{2}+t$ (yükselen bölge) |
| $1 \leq t < 2$ | Tepe geçildi, alçalan bölge dahil | Parçalı integral |
| $2 \leq t < 5$ | Tam $x(\tau)$ içinde | $\int_0^2 x(\tau)\,d\tau = \tfrac{3}{2}$ (sabit) |
| $5 \leq t < 7$ | $[t-5,\,2]$ daralıyor | Alçalan integral |
| $t \geq 7$ | Kesişim yok | $0$ |

*Detaylı hesap: [[02 LTI Sistemler ve Konvolüsyon]]*

---

## Bağlantılı Notlar

- [[02 LTI Sistemler ve Konvolüsyon]]
- [[../Sayısal Sinyal İşleme/01 Ayrık Zaman Sinyalleri ve Örnekleme|SSİ: Ayrık Zaman Sinyalleri]]
