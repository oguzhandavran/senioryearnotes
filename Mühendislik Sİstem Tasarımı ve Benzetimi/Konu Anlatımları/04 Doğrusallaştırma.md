---
tags: [mst, doğrusallaştırma, linearization, taylor, jacobian, denge-noktası, konu-anlatımı]
---

# 04 — Doğrusallaştırma

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/04 Doğrusallaştırma Örnekleri|04 Doğrusallaştırma Örnekleri]]

## Neden Doğrusallaştırma?

Gerçek sistemler genellikle **doğrusal olmayan** diferansiyel denklemlerle tanımlanır:

$$\dot{x} = f(x, u)$$

Kontrol teorisi araçları (KYE, Bode, Routh) sadece **lineer** sistemler için çalışır.

**Çözüm:** Bir çalışma noktası (denge noktası) çevresinde Taylor serisi açılımı → lineer yaklaşım.

---

## Denge Noktası (Equilibrium Point)

> [!tanim] Denge Noktası
> $x_e$, $u_e$ değerlerinde sistem değişmiyorsa:
> $$f(x_e, u_e) = 0$$

**Bulma adımları:**
1. $\dot{x} = f(x, u)$ yaz
2. $\dot{x} = 0$ koy (denge şartı)
3. $x_e$, $u_e$ bul (birden fazla denge noktası olabilir)

---

## Taylor Serisi Doğrusallaştırma

Küçük sapmalar tanımla:
$$\delta x = x - x_e, \quad \delta u = u - u_e, \quad \delta\dot{x} = \dot{x} - \dot{x}_e = \dot{x}$$

Tek değişkenli Taylor serisi:
$$f(x) \approx f(x_e) + \left.\frac{df}{dx}\right|_{x_e} (x - x_e) + \ldots$$

Çok değişkenli sistem için:

$$\delta\dot{x} \approx \underbrace{\left.\frac{\partial f}{\partial x}\right|_{x_e, u_e}}_{A} \delta x + \underbrace{\left.\frac{\partial f}{\partial u}\right|_{x_e, u_e}}_{B} \delta u$$

$$\boxed{\delta\dot{x} = A\,\delta x + B\,\delta u}$$

---

## Jacobian Matrisleri

**Sistem matrisi** $A$ (Jacobian $f$'e göre $x$):

$$A = \left.\frac{\partial f}{\partial x}\right|_{x_e, u_e} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots \\ \vdots & & \ddots \end{bmatrix}_{x_e, u_e}$$

**Giriş matrisi** $B$ (Jacobian $f$'e göre $u$):

$$B = \left.\frac{\partial f}{\partial u}\right|_{x_e, u_e}$$

---

## Jacobian Özdeğer → Denge Nokta Tipi

| Özdeğer | Nokta Tipi | Davranış |
|---------|-----------|---------|
| $\lambda = \pm j\omega$ (saf sanal) | **Center Point** (Merkez) | $x(t) = A\sin t + B\cos t$ — kapalı yörüngeler |
| $\lambda_{1,2}$ gerçel, zıt işaret | **Saddle Point** | Kararsız — bir yönde çekici, diğerinde itici |
| $\text{Re}(\lambda) < 0$ karmaşık | **Stable Spiral** | İçe sarılan spiral |
| $\text{Re}(\lambda) > 0$ karmaşık | **Unstable Spiral** | Dışa sarılan spiral |
| $\lambda_{1,2}$ gerçel, negatif | **Stable Node** | Doğrudan denge noktasına yaklaşma |
| $\lambda_{1,2}$ gerçel, pozitif | **Unstable Node** | Doğrudan uzaklaşma |

> [!sinav] Sınav İpucu
> Saf sanal özdeğer → center point (salınım, NE kararlı NE kararsız — sınır kararlı)  
> Zıt işaretli gerçel → saddle point (her zaman kararsız!)

---

## Lyapunov ile Kararlılık (Giriş)

Lineerleştirilmiş sistemin özdeğerleri:

| Özdeğer | Kararlılık |
|---------|-----------|
| $\text{Re}(\lambda_i) < 0$ tümü | Lokal asimptotik kararlı |
| $\text{Re}(\lambda_i) > 0$ herhangi biri | Lokal kararsız |
| $\text{Re}(\lambda_i) = 0$ birkaçı | Belirsiz (doğrusal analiz yetersiz) |

> [!warning] Önemli
> Lineerleştirilmiş analizin geçerliliği yalnızca denge noktasının **yakınında** geçerlidir!
> Büyük sapmalar için orijinal doğrusal olmayan sistem incelenmelidir.

---

## Faz Düzlemi Analizi

> Doğrusal olmayan, 2. dereceden, zamandan bağımsız sistemleri **grafik** olarak incelemenin yolu.

**Durum uzayı gösterimi:** $x_1 = x$, $x_2 = \dot{x}$ alınarak $(\dot{x}_1, \dot{x}_2)$ faz düzleminde çizilir.

| Özdeğer | Nokta Tipi | Grafik |
|---------|-----------|--------|
| $\lambda = \pm j\omega$ (saf sanal) | **Merkez** (Center) | İç içe daireler — salınım |
| $\text{Re}(\lambda)<0$, karmaşık | **Kararlı Odak** (Stable Focus) | İçe sarılan spiral |
| $\text{Re}(\lambda)>0$, karmaşık | **Kararsız Odak** | Dışa sarılan spiral |
| $\lambda_{1,2}$ gerçel, negatif | **Kararlı Düğüm** | Doğrusal yaklaşma |
| $\lambda_{1,2}$ gerçel, pozitif | **Kararsız Düğüm** | Doğrusal uzaklaşma |
| $\lambda_1>0$, $\lambda_2<0$ | **Eyer (Saddle)** | Bir yön çekici, diğer itici |

> [!sinav] Sınav İpucu — Yay-Kütle ($k=1, m=1$)
> $\ddot{x}+x=0$ → $\lambda=\pm j$ → **Merkez noktası** → $x_1^2+x_2^2=r^2$ (daireler)

**Örnek — ẍ + 0.6ẋ + 3x + x² = 0:**

Durum uzayı: $\dot{x}_1=x_2$, $\dot{x}_2=-0{,}6x_2-3x_1-x_1^2$

Denge noktaları ($\dot{x}_1=\dot{x}_2=0$): $(0,0)$ ve $(-3,0)$

| Nokta | Jacobian | Özdeğerler | Tür |
|-------|---------|-----------|-----|
| $(0,0)$ | $\begin{bmatrix}0&1\\-3&-0{,}6\end{bmatrix}$ | $\lambda=-0{,}3\pm j1{,}71$ | **Kararlı Odak** |
| $(-3,0)$ | $\begin{bmatrix}0&1\\3&-0{,}6\end{bmatrix}$ | $\lambda_1=1{,}46,\ \lambda_2=-2{,}06$ | **Eyer Noktası** |

---

## Özet Akış Diyagramı

<svg width="360" height="370" viewBox="0 0 360 370" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-mst04" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
  </defs>
  <!-- Step 1 -->
  <rect x="40" y="10" width="280" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="180" y="28" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">1. Doğrusal Olmayan Sistem</text>
  <text x="180" y="44" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">ẋ = f(x, u)</text>
  <line x1="180" y1="52" x2="180" y2="68" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst04)"/>
  <!-- Step 2 -->
  <rect x="40" y="70" width="280" height="42" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="180" y="88" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">2. Denge Noktası Bul</text>
  <text x="180" y="104" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">f(x_e, u_e) = 0</text>
  <line x1="180" y1="112" x2="180" y2="128" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst04)"/>
  <!-- Step 3 -->
  <rect x="40" y="130" width="280" height="50" rx="2" fill="#eef2f7" stroke="#1a1a2e" stroke-width="2"/>
  <text x="180" y="150" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" fill="#1a1a2e">3. Jacobian Hesapla</text>
  <text x="180" y="166" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" font-style="italic" fill="#1a1a2e">A = ∂f/∂x|_(x_e,u_e),   B = ∂f/∂u|_(x_e,u_e)</text>
  <line x1="180" y1="180" x2="180" y2="196" stroke="#1a1a2e" stroke-width="1.8" marker-end="url(#arr-mst04)"/>
  <!-- Step 4 -->
  <rect x="40" y="198" width="280" height="42" rx="2" fill="#1a1a2e" stroke="#1a1a2e" stroke-width="2"/>
  <text x="180" y="216" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-weight="bold" fill="white">4. Lineer Model ✓</text>
  <text x="180" y="232" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#aac4e8">δẋ = A·δx + B·δu</text>
  <!-- Two output branches -->
  <line x1="120" y1="240" x2="90" y2="270" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst04)"/>
  <line x1="240" y1="240" x2="270" y2="270" stroke="#1a1a2e" stroke-width="1.5" marker-end="url(#arr-mst04)"/>
  <!-- Branch left: Kararlılık -->
  <rect x="5" y="272" width="168" height="42" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="89" y="290" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Kararlılık Analizi</text>
  <text x="89" y="306" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">Re(λ) &lt; 0 → Kararlı</text>
  <!-- Branch right: Kontrol -->
  <rect x="187" y="272" width="168" height="42" rx="2" fill="#d6e0f0" stroke="#1a1a2e" stroke-width="2"/>
  <text x="271" y="290" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="11" fill="#1a1a2e">Kontrol Tasarımı</text>
  <text x="271" y="306" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" font-style="italic" fill="#1a1a2e">KYE, Pole Placement…</text>
</svg>

---

> [!sinav] Sınav İpucu
> - Taylor 1. derece: $f(x) \approx f(x_e) + f'(x_e)(x-x_e)$
> - Jacobian = her $f_i$'yi her $x_j$'ye göre türev al, $x_e$'de değerlendir
> - $\sin x \approx x$, $\cos x \approx 1$ (küçük açı: $x_e = 0$ için)
> - $e^x \approx 1 + x$ (küçük sapmalar için)
> - Sıfır girişte denge: $f(x_e, 0) = 0$'ı çöz
