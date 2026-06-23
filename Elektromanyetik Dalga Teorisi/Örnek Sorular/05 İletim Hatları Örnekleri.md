---
tags: [emd, bütünleme, iletim-hatları, örnek-sorular]
---

# 05 — İletim Hatları Örnekleri

← [[EMD Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 İletim Hatları]]

---

## Sınır Koşulları — Ek Örnekler (Elektrostatik)

*Not: Bu örnekler dersin temel elektrostatik bölümünden alınmıştır.*

**Örnek (sayfa 11):** $\varepsilon_{r1}=3$, $\varepsilon_{r2}=2$, sınır $y=0$, $\bar{E}_1$ bileşenleriyle verilmiş. Açılar:

$$\cos\alpha_1 = \frac{E_{1n}}{|E_1|}, \quad \cos\alpha_2 = \frac{E_{2n}}{|E_2|}$$

Normal bileşen dönüşümü: $E_{2n} = \dfrac{\varepsilon_{r1}}{\varepsilon_{r2}}E_{1n}$

**Örnek (sayfa 12):** $\bar{E}_2=2\hat{a}_x-3\hat{a}_y+3\hat{a}_z$, $\varepsilon_1=2\varepsilon_0$, $\varepsilon_2=8\varepsilon_0$, sınır $y=0$

- Teğetsel: $E_{1x}=E_{2x}=2$, $E_{1z}=E_{2z}=3$
- Normal ($y$ ekseni): $\varepsilon_1 E_{1n} = \varepsilon_2 E_{2n}$ → $2\varepsilon_0 E_{1y} = 8\varepsilon_0\times(-3)$ → $E_{1y}=-12$

$$\bar{E}_1 = 2\hat{a}_x - 12\hat{a}_y + 3\hat{a}_z \;\text{V/m}$$

**Yüzey yükü ($\rho_s$) varken:**
$$D_{2n}-D_{1n}=\rho_s \implies \varepsilon_2 E_{2n}-\varepsilon_1 E_{1n}=\rho_s$$

---

## Kapasitans Formülleri ve Hesapları

> [!formul] Temel Kapasitans Hesabı
> 1. Gauss yasasıyla $\bar{E}$ bul
> 2. $V = -\int\bar{E}\cdot d\bar{l}$ ile voltaj hesapla
> 3. $C = Q/V$

**Paralel Plakalı Kapasitör:** Alan $S$, aralık $d$, dielektrik $\varepsilon$

$$\rho_s = \frac{Q}{S}, \quad \bar{E} = \frac{\rho_s}{\varepsilon}(-\hat{a}_y) = -\frac{Q}{\varepsilon S}\hat{a}_y$$

$$V_{12} = -\int_0^d\bar{E}\cdot d\bar{l} = \frac{Qd}{\varepsilon S}$$

$$\boxed{C = \frac{Q}{V_{12}} = \frac{\varepsilon S}{d}}$$

**Silindirik Kapasitör:** İç yarıçap $a$, dış yarıçap $b$, uzunluk $L$, dielektrik $\varepsilon$

Gauss (silindirik yüzey): $E_r\cdot r\cdot2\pi L = Q/\varepsilon$ → $E_r = \dfrac{Q}{2\pi r L\varepsilon}$

$$V = -\int_a^b E_r\,dr = \frac{Q}{2\pi L\varepsilon}\ln\!\left(\frac{b}{a}\right)$$

$$\boxed{C = \frac{Q}{V} = \frac{2\pi L\varepsilon}{\ln(b/a)}}$$

> [!sinav] Kapasitör Türleri
> - Paralel plaka: $C=\varepsilon S/d$ — en basit, uniform alan
> - Silindirik: $C=2\pi L\varepsilon/\ln(b/a)$ — koaksiyel kablo modeli
> - Küresel: $C=4\pi\varepsilon/(1/a-1/b)$ — benzer türetim
