---
tags: [ss, sinyal, sınıflandırma, konu-anlatımı]
---

# 01 — Sinyal Sınıflandırması

← [[SS Ana Sayfa]]  |  Örnekler: [[../Örnek Sorular/01 Sinyal Örnekleri]]

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

### Birim Dürtü (İmpuls)

**DT:** $\delta[n] = \begin{cases}1 & n=0 \\ 0 & n\neq 0\end{cases}$

**CT:** $\delta(t)$ — Dirac delta (sifting özelliği):
$$\int_{-\infty}^{\infty} x(t)\,\delta(t-t_0)\,dt = x(t_0)$$

### Birim Basamak

$$u[n] = \begin{cases}1 & n \geq 0 \\ 0 & n < 0\end{cases} \qquad u(t) = \begin{cases}1 & t > 0 \\ 0 & t < 0\end{cases}$$

**İlişki:** $\delta[n] = u[n] - u[n-1]$ ve $u[n] = \sum_{k=-\infty}^{n}\delta[k]$

CT'de: $\delta(t) = \dfrac{d}{dt}u(t)$

### Üstel Sinyal

$$x(t) = C e^{at}, \quad x[n] = C \alpha^n$$

- $a$ veya $\alpha$ reel: büyüme/sönüm
- $a$ veya $\alpha$ karmaşık: sinüzoidal × üstel

### Sinüzoidal

$$x(t) = A\cos(\omega_0 t + \phi) \qquad x[n] = A\cos(\Omega_0 n + \phi)$$

---

## Bağlantılı Notlar

- [[../Örnek Sorular/01 Sinyal Örnekleri|Örnek Sorular — Sinyal Sınıflandırması]]
- [[02 LTI Sistemler ve Konvolüsyon]]
