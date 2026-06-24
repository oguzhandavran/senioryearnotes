---
tags: [ss, sinyaller-sistemler, sinav-gecesi, ozet]
---

# SS — Sınav Gecesi Özeti

> Kapsam: B1 tam · B2 (2.5 hariç) · B3 (3.6'ya kadar) · B4 (4.5'e kadar) · **B7 Örnekleme**
> **Laplace yok. DTFT yok. Ayrık zamanlı Fourier (DTFT) büt kapsamı dışı — WhatsApp teyit etti (21.06.2026)**

> [!tip] BÜTÜNLEME İPUCU
> 6 soru · Deftere çalış · Tanımsal yerlere ekstra bak · "Kolay olacak" dedi.
> 38 kişi büte kaldı — hoca genel eğilimli not dağılımı yapıyor.

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

## 3.6 — Ayrık Zamanlı Fourier Serisi (DTFS)

Periyodik DT sinyali $x[n]$ (periyot $N$):

$$\boxed{x[n] = \sum_{k=\langle N\rangle} a_k\, e^{jk(2\pi/N)n}}$$

$$\boxed{a_k = \frac{1}{N}\sum_{n=\langle N\rangle} x[n]\, e^{-jk(2\pi/N)n}}$$

> Fark: $a_k$ **periyodik** — $a_{k+N}=a_k$. Yalnızca $N$ tane bağımsız katsayı var.

**CT Fourier Serisi ile Karşılaştırma:**

| | CT ($x(t)$, periyot $T_0$) | DT ($x[n]$, periyot $N$) |
|--|--------------------------|--------------------------|
| Katsayılar | $c_k = \frac{1}{T_0}\int x(t)e^{-jk\omega_0 t}dt$ | $a_k = \frac{1}{N}\sum x[n]e^{-jk(2\pi/N)n}$ |
| Bağımsız katsayı | $\infty$ | $N$ tane |
| Çarpma | $x\cdot y \leftrightarrow \sum_l c_l d_{k-l}$ | $x[n]y[n] \leftrightarrow \sum_l a_l b_{k-l}$ (periyodik) |

---

## 4 — Fourier Dönüşümü CTFT (4.1–4.5)

$$X(j\omega) = \int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt, \quad x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}d\omega$$

**Temel çiftler:**

| $x(t)$ | $X(j\omega)$ |
|--------|-------------|
| $\delta(t)$ | $1$ |
| $1$ | $2\pi\delta(\omega)$ |
| $e^{-at}u(t)$, $a>0$ | $\frac{1}{a+j\omega}$ |
| $e^{-a|t|}$, $a>0$ | $\frac{2a}{a^2+\omega^2}$ |
| $\text{rect}(t/\tau)$ | $\tau\,\text{sinc}(\omega\tau/2)$ |
| $u(t)$ | $\pi\delta(\omega)+\frac{1}{j\omega}$ |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ |
| Periyodik $x(t)$ ($c_k$'li) | $2\pi\sum_k c_k\delta(\omega-k\omega_0)$ |

**Özellikler (4.3):**

| Özellik | İşlem | CTFT |
|---------|-------|------|
| Doğrusallik | $ax+by$ | $aX+bY$ |
| Zaman kayması | $x(t-t_0)$ | $e^{-j\omega t_0}X(j\omega)$ |
| Frekans kayması | $e^{j\omega_0 t}x(t)$ | $X(j(\omega-\omega_0))$ |
| Eşlenik simetri | $x^*(t)$ | $X^*(-j\omega)$ |
| Zaman ölçekleme | $x(at)$ | $\frac{1}{|a|}X(j\omega/a)$ |
| Türev | $dx/dt$ | $j\omega X(j\omega)$ |
| İntegral | $\int x\,dt$ | $\frac{1}{j\omega}X+\pi X(0)\delta(\omega)$ |
| **Evrişim (4.4)** | $x*h$ | $X\cdot H$ |
| **Çarpma (4.5)** | $x(t)\cdot h(t)$ | $\frac{1}{2\pi}X*H$ |
| Parseval | $\int|x|^2 dt$ | $\frac{1}{2\pi}\int|X|^2 d\omega$ |
| Dualite | $X(t)$ | $2\pi x(-\omega)$ |

> [!tip] Çarpma ↔ Evrişim Dualitesi (4.5)
> Zaman domeninde **çarpım** → frekans domeninde **evrişim** (÷2π)
> Zaman domeninde **evrişim** → frekans domeninde **çarpım**
> Bu dualite frekans seçici süzgeçlemenin temelidir.

---

## Tuzaklar

> [!warning] SS Sınav Tuzakları
> - $e^{-at}u(t)$ ≠ $e^{-at}$ — tek taraflı! $t<0$ için sıfır.
> - Konvolüsyon grafiği: $h(-\tau)$ çevir, kaydır, entegre et; sınırları dikkatli kur.
> - **Parseval (CTFT):** $\frac{1}{2\pi}$ faktörü var — unutma!
> - DTFS: $a_k$ periyodik ($a_{k+N}=a_k$), toplam N terim üzerinden.
> - **Çarpma özelliği:** $x\cdot y \leftrightarrow \frac{1}{2\pi}X*Y$ — evrişim ile karıştırma.
> - Periyodik sinyalin CTFT'si: $2\pi\sum c_k\delta(\omega-k\omega_0)$ — impuls dizisi.
> - Doğrusal faz = zaman gecikmesi, sinyali bozmaz.

---

## Sınav Kontrol Listesi

- [ ] Sinyal sınıflandırması: periyodik, enerji/güç, çift/tek
- [ ] CT & DT konvolüsyon integrali/toplamı hesaplayabiliyorum
- [ ] CTFS katsayısı $c_k$ bulabiliyorum + Parseval uygulayabiliyorum
- [ ] DTFS katsayısı $a_k$ bulabiliyorum (N terim, periyodik)
- [ ] CTFT analiz/sentez integrali yapabiliyorum
- [ ] Periyodik sinyalin CTFT'sini yazabiliyorum ($2\pi c_k \delta$)
- [ ] 4.3 özelliklerini (kayma, türev, eşlenik, ölçekleme) uygulayabiliyorum
- [ ] Evrişim özelliği: zaman konv. = frekans çarpım
- [ ] Çarpma özelliği: zaman çarpım = frekans konv./2π

---

← [[SS Ana Sayfa]] | [[SS Formül Sayfası]]
