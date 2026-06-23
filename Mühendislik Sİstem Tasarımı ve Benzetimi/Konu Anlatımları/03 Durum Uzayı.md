---
tags: [mst, durum-uzayı, state-space, matris, özdeğer, kontrol, konu-anlatımı]
---

# 03 — Durum Uzayı (State Space)

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/03 Durum Uzayı Örnekleri|03 Durum Uzayı Örnekleri]]

## Durum Uzayı Gösterimi

$$\boxed{\dot{x}(t) = Ax(t) + Bu(t)}$$
$$\boxed{y(t) = Cx(t) + Du(t)}$$

| Sembol | Boyut | Açıklama |
|--------|-------|---------|
| $x$ | $n \times 1$ | Durum vektörü |
| $u$ | $r \times 1$ | Giriş vektörü |
| $y$ | $m \times 1$ | Çıkış vektörü |
| $A$ | $n \times n$ | Sistem matrisi (dinamikler) |
| $B$ | $n \times r$ | Giriş matrisi |
| $C$ | $m \times n$ | Çıkış matrisi |
| $D$ | $m \times r$ | İletim matrisi |

---

## State-Space → Transfer Fonksiyonu

Laplace dönüşümü ($x(0)=0$):

$$sX(s) = AX(s) + BU(s) \implies X(s) = (sI - A)^{-1}BU(s)$$

$$\boxed{G(s) = C(sI - A)^{-1}B + D}$$

---

## Transfer Fonksiyonu → State-Space

### Kontrolör Canonical Form (Faz Değişkenleri)

$$G(s) = \frac{b_{n-1}s^{n-1} + \ldots + b_1 s + b_0}{s^n + a_{n-1}s^{n-1} + \ldots + a_1 s + a_0}$$

**Durum değişkenleri:** $x_1 = y$, $x_2 = \dot{y}$, ..., $x_n = y^{(n-1)}$

$$A = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}$$

$$C = \begin{bmatrix} b_0 & b_1 & \cdots & b_{n-1} \end{bmatrix}, \quad D = 0 \text{ (proper)}$$

---

## Özdeğer Analizi (Kararlılık)

Sistemin özdeğerleri = $A$ matrisinin özdeğerleri = karakteristik polinomun kökleri

$$\det(sI - A) = 0 \quad \text{(karakteristik denklem)}$$

| Özdeğer konumu | Sistem davranışı |
|----------------|-----------------|
| Tüm özdeğerler $\text{Re}(s) < 0$ | **Kararlı** |
| Herhangi $\text{Re}(s) > 0$ | **Kararsız** |
| $\text{Re}(s) = 0$ | Sınır durumu |

**Özdeğer hesabı:**
$$\lambda_i: \quad \det(\lambda I - A) = 0$$

---

## Kontrol Edilebilirlik ve Gözlenebilirlik

**Kontrol Edilebilirlik Matrisi:**
$$\mathcal{C} = \begin{bmatrix} B & AB & A^2B & \cdots & A^{n-1}B \end{bmatrix}$$

Sistem kontrol edilebilir $\iff \text{rank}(\mathcal{C}) = n$

**Gözlenebilirlik Matrisi:**
$$\mathcal{O} = \begin{bmatrix} C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1} \end{bmatrix}$$

Sistem gözlenebilir $\iff \text{rank}(\mathcal{O}) = n$

---

> [!sinav] Sınav İpucu
> - $G(s) = C(sI-A)^{-1}B + D$ → sınav sorusu olmaya devam eder!
> - Özdeğerler → $\det(\lambda I-A) = 0$ → kararlılık kontrolü
> - Faz değişkenleri: son satır $= [-a_0, -a_1, ..., -a_{n-1}]$
> - Durum değişkeni seçimi özgür ama fiziksel anlam kolaylaştırır
> - SS ve TF aynı sistem için eşdeğer — özdeğerler = kutuplar
> - Elektrik sistemlerde durum değişkenleri = **kondansatör gerilimleri** + **bobin akımları**
