---
tags: [ss, sinyaller-sistemler, sinav-gecesi, ozet]
---

# SS — Sınav Gecesi Özeti

> Tek sayfa. Fourier'den Laplace'a.

---

## 1 — Sinyal Özellikleri (Hızlı Kontrol)

| Test | Yöntem |
|------|--------|
| Periyodik | $x(t+T_0)=x(t)$, $T_0$ bulunabiliyorsa evet |
| Enerji | $E=\int_{-\infty}^{\infty}\|x(t)\|^2 dt < \infty$ |
| Güç | $P=\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}\|x\|^2 dt < \infty$ |
| Doğrusal | Süperpozisyon + $x=0\Rightarrow y=0$ |
| ZD | Katsayılarda $t$ yok mu? |
| Nedensel | $t<0$ için $h(t)=0$ |
| BIBO kararlı | $\int_{-\infty}^{\infty}\|h(t)\|dt<\infty$ |

---

## 2 — LTI ve Konvolüsyon

$$y(t) = x(t)*h(t) = \int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau$$

**Özellikler:** Komutatif, Asosiyatif, Dağılımlı.

**İmpuls yanıtı:** $h(t) = T\{\delta(t)\}$ — tek sorumlu parametredir.

**Laplace:** $Y(s)=X(s)\cdot H(s)$; **Fourier:** $Y(j\omega)=X(j\omega)\cdot H(j\omega)$

---

## 3 — Fourier Serisi (Periyodik Sinyaller)

$$x(t) = \sum_{k=-\infty}^{\infty}c_k e^{jk\omega_0 t}, \quad \omega_0 = \frac{2\pi}{T_0}$$

$$c_k = \frac{1}{T_0}\int_{T_0} x(t)e^{-jk\omega_0 t}dt$$

**Dik dalga:** $c_k = \frac{A\sin(k\pi/2)}{k\pi/2} \cdot \frac{\tau}{T_0}$ (dikdörtgen, genişlik $\tau$)

**Parseval:** $\frac{1}{T_0}\int|x(t)|^2 dt = \sum_{k=-\infty}^{\infty}|c_k|^2$

---

## 4 — Fourier Dönüşümü (Periyodik Olmayan)

$$X(j\omega) = \int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt, \quad x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}d\omega$$

**Temel çiftler:**

| $x(t)$ | $X(j\omega)$ |
|--------|-------------|
| $\delta(t)$ | $1$ |
| $1$ | $2\pi\delta(\omega)$ |
| $e^{-at}u(t)$, $a>0$ | $\frac{1}{a+j\omega}$ |
| $\text{rect}(t/\tau)$ | $\tau\,\text{sinc}(\omega\tau/2)$ |
| $e^{-a\|t\|}$ | $\frac{2a}{a^2+\omega^2}$ |

**Özellikler:**

| | İşlem | FT |
|-|-------|----|
| Zaman kayması | $x(t-t_0)$ | $e^{-j\omega t_0}X(j\omega)$ |
| Frekans kayması | $e^{j\omega_0 t}x(t)$ | $X(j(\omega-\omega_0))$ |
| Konvolüsyon | $x*h$ | $X\cdot H$ |
| Türev | $dx/dt$ | $j\omega X(j\omega)$ |
| Parseval | $\int\|x\|^2 dt$ | $\frac{1}{2\pi}\int\|X\|^2 d\omega$ |
| Dualite | $X(t)$ | $2\pi x(-\omega)$ |

---

## 5 — Laplace Dönüşümü

$$X(s) = \int_0^{\infty}x(t)e^{-st}dt \quad (s=\sigma+j\omega)$$

**Temel çiftler:**

| $x(t)$ | $X(s)$ | ROC |
|--------|--------|-----|
| $u(t)$ | $1/s$ | $\text{Re}(s)>0$ |
| $e^{-at}u(t)$ | $1/(s+a)$ | $\text{Re}(s)>-a$ |
| $te^{-at}u(t)$ | $1/(s+a)^2$ | $\text{Re}(s)>-a$ |
| $\sin(\omega_0 t)u(t)$ | $\omega_0/(s^2+\omega_0^2)$ | $\text{Re}(s)>0$ |
| $\cos(\omega_0 t)u(t)$ | $s/(s^2+\omega_0^2)$ | $\text{Re}(s)>0$ |

**Özellikler:**
- Gecikme: $x(t-t_0)u(t-t_0) \leftrightarrow e^{-st_0}X(s)$
- Türev: $\mathcal{L}\{dx/dt\} = sX(s)-x(0^-)$
- Son değer: $\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$
- Başlangıç: $x(0^+) = \lim_{s\to\infty}sX(s)$

**Ters Laplace (PFD):** $X(s)/s$ kısmi kesirlere ayır, çiftleri kullan.

---

## 6 — Sistem Analizi (Kararlılık ve Tip)

**Kararlı LTI:** Tüm kutuplar sol yarıda ($\text{Re}(s) < 0$)

**Kapalı çevrim TF:** $T(s) = G(s)/(1+G(s))$ (unity)

---

## Tuzaklar

> [!warning] SS Sınav Tuzakları
> - Sinyal çiftleri: $e^{-at}u(t)$ ≠ $e^{-at}$ (tek taraflı!)
> - Konvolüsyon grafiği: birini çevir ($h(-\tau)$), kaydır, entegre et
> - Fourier: $\delta(\omega)$ sonsuz genlikli ama normalize, anlık olarak Parseval'ı düşün
> - Laplace türev: $sX(s)-x(0^-)$ başlangıç şartı sıfır değilse eklenir
> - Parseval (Fourier): $1/(2\pi)$ faktörü var!
> - Son değer teoremi: önce kararlılık! (Laplace da, Z de)

---

← [[SS Ana Sayfa]] | [[SS Formül Sayfası]]
