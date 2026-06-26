---
tags: [emd, bütünleme, yansıma, kırılma, örnek-sorular]
---

# 04 — Yansıma ve Sınır Koşulları Örnekleri

← [[EMD Ana Sayfa]] | Teori: [[../Konu Anlatımları/04 Yansıma ve Sınır Koşulları]]

---

## Soru 1 — Silindirik Koordinatlarda Dalga Denklemi

> [!note]- Semboller
> - $(r,\phi,z)$: silindirik koordinatlar; $\bar E=\hat a_r E$: yalnız radyal bileşenli alan
> - Kaynaksız ortam: $\nabla\cdot\bar E=0$, $\rho_v=0$
> - Silindirik diverjans: $\nabla\cdot\bar E=\frac1r\frac{\partial(rE_r)}{\partial r}+\frac1r\frac{\partial E_\phi}{\partial\phi}+\frac{\partial E_z}{\partial z}$
> - $\nabla^2$ (silindirik, $\phi$-bağımsız): $\frac{\partial^2}{\partial r^2}+\frac1r\frac{\partial}{\partial r}+\frac{\partial^2}{\partial z^2}$; $\mu\varepsilon$: ortam çarpanı

**Problem:** $(r,\phi,z)$ silindirik koordinatlar; kaynak içermeyen basit ortamda EM dalganın elektrik alanı $\bar{E}=\hat{a}_r E(r,\phi,z)$ olarak verilmiştir. $E$'nin $\phi$'ye bağlı olmadığını belirle. Ortamda $E$'nin sağladığı denklemi yaz.

**Çözüm:**

Kaynak içermeyen: $\nabla\cdot\bar{E}=0$, $\nabla\cdot\bar{B}=0$, $\rho_v=0$

Silindirik koordinatlarda diverjans ($E_\phi=0$, $E_z=0$ çünkü sadece $\hat{a}_r$ bileşeni var):
$$\nabla\cdot\bar{E} = \frac{1}{r}\frac{\partial(rE_r)}{\partial r} + \frac{1}{r}\frac{\partial E_\phi}{\partial\phi} + \frac{\partial E_z}{\partial z}$$

$E_\phi=0$, $E_z=0$ yerine: $\nabla\cdot\bar{E} = \frac{1}{r}\frac{\partial(rE)}{\partial r} = 0$

Kaynak yoksa: $\frac{1}{r}\frac{\partial(rE)}{\partial r}=0$ → **$E$, $\phi$'ye bağlı değildir**

Dalga denklemi ($\nabla^2\bar{E} - \mu\varepsilon\dfrac{\partial^2\bar{E}}{\partial t^2}=0$), $\partial/\partial\phi=0$ ile:

$$\boxed{\frac{\partial^2 E}{\partial r^2} + \frac{1}{r}\frac{\partial E}{\partial r} + \frac{\partial^2 E}{\partial z^2} - \mu\varepsilon\frac{\partial^2 E}{\partial t^2} = 0}$$

---

## Soru 2 — Düzlemsel Dalga ve $\lambda/4$ Mesafe

> [!note]- Semboller
> - $\omega$: açısal frekans; $f=\omega/2\pi$; $\lambda=c/f$: dalga boyu; $\beta=2\pi/\lambda$: faz sabiti
> - $t_1=(\lambda/4)/c=T/4$: çeyrek dalga ilerleme süresi *(ayrıntılı çözüm: [[03 Dalga Yayılması Örnekleri#Soru 2 — Düzlemsel Dalga Anlık Görüntü|03 Soru 2]])*

**Problem:** Serbest uzayda $\bar{E}=\hat{a}_y 20\sin(4\pi\times10^8 t - \beta z)$ V/m. $\beta$ ve $\lambda$ hesapla; $\lambda/4$ mesafe için $t_1$'i bul.

**Çözüm:**

$$\omega = 4\pi\times10^8 \;\text{rad/s}, \quad f = 200 \;\text{MHz}$$
$$\lambda = c/f = 1.5 \;\text{m}, \quad \beta = 4\pi/3 \;\text{rad/m}$$
$$t_1 = \frac{\lambda/4}{c} = \boxed{1.25 \;\text{ns}}$$

---

## Sınır Koşulları — Dielektrik Örnekleri

> [!note]- Semboller
> - $\varepsilon_{r1},\varepsilon_{r2}$: bağıl geçirgenlikler; sınır $y=0$ → normal yön $\hat a_y$
> - Teğetsel ($E_x,E_z$): sürekli ($E_{1t}=E_{2t}$)
> - Normal ($E_y$): $\varepsilon_1E_{1n}=\varepsilon_2E_{2n}$ (yüzey yükü yoksa)
> - $\alpha_1,\alpha_2$: alanların normalle yaptığı açılar; $\rho_s$: yüzey yük yoğunluğu
> - Yüzey yükü varsa: $\varepsilon_2E_{2n}-\varepsilon_1E_{1n}=\rho_s$

**Örnek (sayfa 11):** $\varepsilon_{r1}=3$, $\varepsilon_{r2}=2$, sınır $y=0$, $\bar{E}_1$ bileşenleriyle verilmiş. Açılar:

$$\cos\alpha_1 = \frac{E_{1n}}{|E_1|}, \quad \cos\alpha_2 = \frac{E_{2n}}{|E_2|}$$

Normal bileşen dönüşümü: $E_{2n} = \dfrac{\varepsilon_{r1}}{\varepsilon_{r2}}E_{1n}$

**Örnek (sayfa 12):** $\bar{E}_2=2\hat{a}_x-3\hat{a}_y+3\hat{a}_z$, $\varepsilon_1=2\varepsilon_0$, $\varepsilon_2=8\varepsilon_0$, sınır $y=0$

- Teğetsel: $E_{1x}=E_{2x}=2$, $E_{1z}=E_{2z}=3$
- Normal ($y$ ekseni): $\varepsilon_1 E_{1n} = \varepsilon_2 E_{2n}$ → $2\varepsilon_0 E_{1y} = 8\varepsilon_0\times(-3)$ → $E_{1y}=-12$

$$\bar{E}_1 = 2\hat{a}_x - 12\hat{a}_y + 3\hat{a}_z \;\text{V/m}$$

**Yüzey yükü ($\rho_s$) varken:**
$$D_{2n}-D_{1n}=\rho_s \implies \varepsilon_2 E_{2n}-\varepsilon_1 E_{1n}=\rho_s$$
