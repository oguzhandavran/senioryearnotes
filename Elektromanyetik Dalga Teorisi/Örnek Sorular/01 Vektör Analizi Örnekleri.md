---
tags: [emd, bütünleme, vektör-analizi, örnek-sorular]
---

# 01 — Vektör Analizi Örnekleri

← [[EMD Ana Sayfa]] | Teori: [[../Konu Anlatımları/01 Vektör Analizi ve del Operatörü]]

---

## Küresel Koordinatlarda Hacim İntegrali

> [!example] Problem
> Yarıçapları 2 ve 5 cm olan iki küre arasındaki bölgede yük yoğunluğu $\rho_v=\dfrac{-3\times10^{-8}}{R^4}\cos^2\phi\;\text{C/m}^3$. Bölgedeki toplam yükü $Q=\iiint\rho_v\,dV$ ile bul.

> [!note]- Semboller
> - $R$: küresel yarıçap (m); sınırlar $0.02\le R\le0.05$ (cm → m)
> - $\theta$: kutup açısı ($0\to\pi$); $\phi$: azimut açısı ($0\to2\pi$)
> - $dV=R^2\sin\theta\,dR\,d\theta\,d\phi$: küresel hacim elemanı
> - $\rho_v$: hacim yük yoğunluğu (C/m³); $Q$: toplam yük (C)
> - İntegral ayrışır çünkü çarpan $R$, $\theta$, $\phi$ değişkenlerine ayrı ayrı bağlı

**Çözüm.** $dV=R^2\sin\theta\,dR\,d\theta\,d\phi$ koy; $R^{-4}\cdot R^2=R^{-2}$:

$$Q = \int_0^{2\pi}\!\int_0^{\pi}\!\int_{0.02}^{0.05}\!\frac{-3\times10^{-8}}{R^4}\cos^2\phi\cdot R^2\sin\theta\,dR\,d\theta\,d\phi$$

$$= -3\times10^{-8}\left(\int_0^{2\pi}\cos^2\phi\,d\phi\right)\!\left(\int_0^{\pi}\sin\theta\,d\theta\right)\!\left(\int_{0.02}^{0.05}R^{-2}dR\right)$$

Üç integrali tek tek hesapla:

$$\int_0^{2\pi}\cos^2\phi\,d\phi = \pi,\qquad \int_0^{\pi}\sin\theta\,d\theta = [-\cos\theta]_0^\pi = 2,\qquad \int_{0.02}^{0.05}R^{-2}dR = \left[-\tfrac1R\right]_{0.02}^{0.05} = 50-20 = 30$$

Çarp:

$$\boxed{Q = -3\times10^{-8}\cdot\pi\cdot2\cdot30 = -180\pi\times10^{-8} \approx -5{,}65\times10^{-6}\ \text{C} = -5{,}65\ \mu\text{C}}$$

---

## Çizgi İntegrali

> [!note]- Semboller
> - $\bar A$: vektör alan; $\hat a_x,\hat a_y,\hat a_z$: Kartezyen birim vektörler
> - $d\bar l=dx\,\hat a_x+dy\,\hat a_y+dz\,\hat a_z$: yol elemanı; $\bar A\cdot d\bar l$: skaler çarpım
> - Parametrizasyon $t\in[0,1]$: doğru yolu tek değişkene indirger
> - $P_1\to P_2$ düz çizgi: $x=2t,\,y=t,\,z=t$ (uç noktaları sağlar)

**Problem:** $\bar{A} = (2y+3)\hat{a}_x + xz\hat{a}_y + (yz-x)\hat{a}_z$, $P_1(0,0,0)$'dan $P_2(2,1,1)$'e direk yol için $\int\bar A\cdot d\bar l$.

Parametre: $x=2t,\;y=t,\;z=t$, $0\leq t\leq1$ → $dx=2dt$, $dy=dz=dt$

$$\int_{P_1}^{P_2}\bar{A}\cdot d\bar{l} = \int_0^1\!\left[(2t+3)(2) + (2t)(t) + (t^2-2t)\right]dt$$

$$= \int_0^1(4t+6+2t^2+t^2-2t)\,dt = \int_0^1(3t^2+2t+6)\,dt$$

$$= \left[t^3+t^2+6t\right]_0^1 = 1+1+6 = \boxed{8}$$

---

## Stokes Teoremi — Doğrulama

> [!note]- Semboller
> - Stokes: $\iint_S(\nabla\times\bar A)\cdot d\bar S = \oint_C\bar A\cdot d\bar l$ (yüzey ↔ sınır eğrisi)
> - Silindirik: $\hat a_r,\hat a_\phi,\hat a_z$ birim vektörler; $r$: eksenel uzaklık, $\phi$: açı, $z$: yükseklik
> - Sınır: silindir yüzeyi $r=2$, $\phi\in[\phi_0,\pi/2]$, $z\in[0,3]$ → $d\bar S=r\,d\phi\,dz\,\hat a_r$
> - $\bar B=\frac{\cos\phi}{r}\hat a_z$: yalnız $\hat a_z$ bileşenli alan

$$\iint_S(\nabla\times\bar{A})\cdot d\bar{S} = \oint_C\bar{A}\cdot d\bar{l}$$

**Örnek:** Silindirik koordinatlarda $\bar{B} = \dfrac{\cos\phi}{r}\hat{a}_z$, silindir yüzeyi $r=2$, $\phi\in[\phi_0,\pi/2]$, $0\leq z\leq3$.

**Adım 1 — Rotasyonel (silindirik).** Yalnız $A_z=\frac{\cos\phi}{r}$ bileşeni var; $\nabla\times\bar B = \frac1r\frac{\partial A_z}{\partial\phi}\hat a_r - \frac{\partial A_z}{\partial r}\hat a_\phi$:

$$\nabla\times\bar{B} = -\frac{\sin\phi}{r^2}\hat{a}_r + \frac{\cos\phi}{r^2}\hat{a}_\phi$$

**Adım 2 — Yüzey integrali.** $d\bar S=r\,d\phi\,dz\,\hat a_r$ ile yalnız $\hat a_r$ bileşeni katkı verir; $r=2$:

$$\iint_S(\nabla\times\bar{B})\cdot d\bar{S} = \int_0^3\!\!\int_{\phi_0}^{\pi/2}\!\left(-\frac{\sin\phi}{r^2}\right) r\,d\phi\,dz = -\frac1r\int_0^3\!dz\int_{\phi_0}^{\pi/2}\!\sin\phi\,d\phi$$

$$= -\frac{1}{2}\cdot 3\cdot\underbrace{[-\cos\phi]_{\phi_0}^{\pi/2}}_{=\,0+\cos\phi_0\,=\,\cos\phi_0} = \boxed{-\frac{3}{2}\cos\phi_0}$$

**Adım 3 — Çizgi integrali ile doğrulama.** $\bar B$ yalnız $\hat a_z$ yönünde; $\oint\bar B\cdot d\bar l$ yalnız $z$-kenarlarından katkı alır. $\phi=\pi/2$ kenarında $\cos(\pi/2)=0$, sadece $\phi=\phi_0$ kenarı kalır:

$$\oint_C\bar B\cdot d\bar l = \int_{3}^{0}\frac{\cos\phi_0}{2}\,dz = -\frac{3}{2}\cos\phi_0 \quad\checkmark$$

(Eski nottaki "$17/4$" değeri hatalıydı; doğru sonuç $-\tfrac32\cos\phi_0$.)

> [!sinav] Stokes Uygulaması
> Kapalı eğri → açık yüzey ile değiştir (veya tersi).
> $\nabla\times\bar{A}$ rotasyoneli önce bulun, $d\bar{S}$ yönünü sağ el kuralıyla seçin.
