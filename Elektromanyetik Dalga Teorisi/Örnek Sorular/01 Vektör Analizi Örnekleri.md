---
tags: [emd, bütünleme, vektör-analizi, örnek-sorular]
---

# 01 — Vektör Analizi Örnekleri

← [[EMD Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Vektör Analizi ve del Operatörü]]

---

## Küresel Koordinatlarda Hacim İntegrali

**Problem:** Yarıçapları 2 ve 5 cm olan iki küre arasındaki bölgede elektron bulutu yük yoğunluğu:
$$\rho_v = \frac{-3\times10^{-8}}{R^4}\cos^2\phi \;\text{C/m}^3$$

Toplam yükü bul: $Q = \iiint\rho_v\,dV$

Küresel koordinatlarda $dV = R^2\sin\theta\,dR\,d\theta\,d\phi$:

$$Q = \int_0^{2\pi}\!\int_0^{\pi}\!\int_{0.02}^{0.05}\!\frac{-3\times10^{-8}}{R^4}\cos^2\phi\cdot R^2\sin\theta\,dR\,d\theta\,d\phi$$

$$= -3\times10^{-8}\left(\int_0^{2\pi}\cos^2\phi\,d\phi\right)\!\left(\int_0^{\pi}\sin\theta\,d\theta\right)\!\left(\int_{0.02}^{0.05}R^{-2}dR\right)$$

Yardımcı: $\displaystyle\int\cos^2 x\,dx = \frac{x+\sin 2x/2}{2}$, $\displaystyle\int_0^{2\pi}\cos^2\phi\,d\phi = \pi$

---

## Çizgi İntegrali

**Problem:** $\bar{A} = (2y+3)\hat{a}_x + xz\hat{a}_y + (yz-x)\hat{a}_z$, $P_1(0,0,0)$'dan $P_2(2,1,1)$'e direk yol.

Parametre: $x=2t,\;y=t,\;z=t$, $0\leq t\leq1$ → $dx=2dt$, $dy=dz=dt$

$$\int_{P_1}^{P_2}\bar{A}\cdot d\bar{l} = \int_0^1\!\left[(2t+3)(2) + (2t)(t) + (t^2-2t)\right]dt$$

$$= \int_0^1(4t+6+2t^2+t^2-2t)\,dt = \int_0^1(3t^2+2t+6)\,dt$$

$$= \left[t^3+t^2+6t\right]_0^1 = 1+1+6 = \boxed{8}$$

---

## Stokes Teoremi — Doğrulama

$$\iint_S(\nabla\times\bar{A})\cdot d\bar{S} = \oint_C\bar{A}\cdot d\bar{l}$$

**Örnek:** Silindirik koordinatlarda $\bar{B} = \dfrac{\cos\phi}{r}\hat{a}_z$, $r=2$, $\phi\in[\phi_0,\pi/2]$, $0\leq z\leq3$

Rotasyonel (silindirik):
$$\nabla\times\bar{A} = \frac{1}{r}\begin{vmatrix}\hat{a}_r & r\hat{a}_\phi & \hat{a}_z \\ \partial_r & \partial_\phi & \partial_z \\ A_r & rA_\phi & A_z\end{vmatrix}$$

Hesap: $\nabla\times\bar{B} = -\dfrac{\sin\phi}{r^2}\hat{a}_r + \dfrac{\cos\phi}{r^2}\hat{a}_\phi$

Yüzey integrali ($\phi=\phi_0$ düzlemi):
$$\iint_S(\nabla\times\bar{B})\cdot d\bar{S} = \int\frac{\cos\phi_0}{r^2}\cdot r\,dr\,dz = \frac{17}{4}\!\left(0-\frac{3}{2}\right) = -\frac{3\times17}{8}$$

Kontrol: $\oint_C\bar{B}\cdot d\bar{l}$ üç parça üzerinden → aynı sonuç ✓

> [!sinav] Stokes Uygulaması
> Kapalı eğri → açık yüzey ile değiştir (veya tersi).
> $\nabla\times\bar{A}$ rotasyoneli önce bulun, $d\bar{S}$ yönünü sağ el kuralıyla seçin.
