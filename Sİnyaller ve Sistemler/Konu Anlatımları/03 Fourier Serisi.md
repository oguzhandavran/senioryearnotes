---
tags: [ss, fourier-serisi, ctfs, dtfs, konu-anlatımı]
---

# 03 — Fourier Serisi

← [[SS Ana Sayfa]]  |  Örnekler: [[../Örnek Sorular/03 Fourier Serisi Örnekleri]]

## Özet

> Periyodik sinyalleri harmonik sinüzoidlerin toplamı olarak yaz. CTFS: sürekli zaman periyodik → karmaşık üstel katsayılar. DTFS: ayrık periyodik → sonlu N-terimli toplam.

> [!abstract] 🔰 Sıfırdan: Kısaltmalar, Semboller, Sezgi
> **Ana fikir:** Her periyodik sinyal, temel frekansın **katları (harmonikleri)** olan sinüzoidlerin toplamıdır. Fourier serisi bu toplamın "tarifini" verir.
>
> | Kısaltma / sembol | Açılım (İng.) | Türkçe / anlamı |
> |---|---|---|
> | **CTFS** | Continuous-Time Fourier Series | **Sürekli-zaman Fourier serisi** |
> | **DTFS** | Discrete-Time Fourier Series | **Ayrık-zaman Fourier serisi** |
> | $a_k,\ c_k$ | Fourier coefficient | $k.$ harmoniğin **karmaşık ağırlığı** |
> | $\omega_0$ | fundamental frequency | **temel açısal frekans** $=2\pi/T$ (rad/s) |
> | $T$ , $N$ | period | **periyot** (CT için $T$, DT için tam sayı $N$) |
> | $k$ | harmonic index | **harmonik numarası** ($k=0$ DC/ortalama) |
> | $e^{jk\omega_0 t}$ | complex exponential | $k.$ **harmonik** (dönen birim vektör) |
>
> **Analiz denklemi nereden? ($a_k=\frac1T\int_T x\,e^{-jk\omega_0 t}dt$)** Harmonikler **ortogonaldir**: $\frac1T\int_T e^{jk\omega_0 t}e^{-jm\omega_0 t}dt = 1$ (eğer $k=m$), $0$ (aksi halde). Sentez denklemini $e^{-jm\omega_0 t}$ ile çarpıp bir periyot boyunca integral alırsan, $k=m$ dışındaki tüm terimler sıfırlanır → geriye yalnız $a_m$ kalır. Yani analiz formülü = "$m.$ harmonik kadar olanı süzme" işlemidir.
>
> **Pratik kısayol:** Sinyal zaten $\sin/\cos$ toplamıysa integral alma — **Euler** ile üstele aç ($\cos\theta=\tfrac12(e^{j\theta}+e^{-j\theta})$), katsayıları doğrudan **oku**.

---

## 1. Sürekli Zaman Fourier Serisi (CTFS)

### Sentez ve Analiz Denklemleri

$$\boxed{x(t) = \sum_{k=-\infty}^{\infty} a_k\, e^{jk\omega_0 t}, \quad \omega_0 = \frac{2\pi}{T}}$$

$$\boxed{a_k = \frac{1}{T} \int_T x(t)\, e^{-jk\omega_0 t}\, dt}$$

Burada integral herhangi bir $T$ uzunluğundaki tam periyot üzerinden alınır.

### Trigonometrik Form (Gerçek Sinyaller için)

Eğer $x(t)$ gerçek değerliyse:
$$x(t) = a_0 + 2\sum_{k=1}^{\infty}\left[A_k \cos(k\omega_0 t) - B_k\sin(k\omega_0 t)\right]$$

Burada $a_k = A_k - jB_k$.

---

## 2. Ayrık Zaman Fourier Serisi (DTFS / DFS) — Bölüm 3.6

### Sentez ve Analiz Denklemleri

$$\boxed{x[n] = \sum_{k=\langle N\rangle} a_k\, e^{jk(2\pi/N) n}}$$

$$\boxed{a_k = \frac{1}{N} \sum_{n=\langle N\rangle} x[n]\, e^{-jk(2\pi/N) n}}$$

> [!warning] CT vs DT Farkı
> - CTFS: sonsuz sayıda $k$ (sonsuz harmonik)
> - DTFS: yalnızca **N tane** bağımsız katsayı, $a_{k+N} = a_k$ (periyodik katsayılar)

---

## 3. Fourier Serisi Özellikleri

| Özellik | CT | DT |
|---------|----|----|
| Doğrusallik | $ax(t)+by(t) \leftrightarrow aa_k+bb_k$ | aynı |
| Zaman kayması | $x(t-t_0) \leftrightarrow a_k e^{-jk\omega_0 t_0}$ | $x[n-n_0] \leftrightarrow a_k e^{-jk(2\pi/N) n_0}$ |
| Frekans kayması | $e^{jM\omega_0 t}x(t) \leftrightarrow a_{k-M}$ | aynı |
| Zaman ters çevirme | $x(-t) \leftrightarrow a_{-k}$ | $x[-n] \leftrightarrow a_{-k}$ |
| Konjugat | $x^*(t) \leftrightarrow a^*_{-k}$ | aynı |
| Çarpma (modülasyon) | $x(t)y(t) \leftrightarrow \sum_l a_l b_{k-l}$ | periyodik evrişim |
| **Parseval** | $\frac{1}{T}\int_T \|x\|^2 dt = \sum_k \|a_k\|^2$ | $\frac{1}{N}\sum_{\langle N\rangle}\|x[n]\|^2 = \sum_{\langle N\rangle}\|a_k\|^2$ |

### Simetri Özellikleri

| Sinyal | Katsayı $a_k$ |
|--------|--------------|
| Gerçek $x(t)$ | $a_{-k} = a_k^*$ (Hermitian simetri) |
| Gerçek + çift | $a_k$ gerçek ve çift |
| Gerçek + tek | $a_k$ saf sanal ve tek |

---

## 4. Parseval Teoremi

**Ortalama güç = katsayıların karelerinin toplamı:**

$$P = \frac{1}{T}\int_T |x(t)|^2 dt = \sum_{k=-\infty}^{\infty} |a_k|^2$$

> [!sinav] Sınav İpucu
> Fourier serisini bilmeden sadece $|a_k|^2$ toplamı ile güç hesaplanabilir!

---

## Bağlantılı Notlar

- [[../Örnek Sorular/03 Fourier Serisi Örnekleri|Örnek Sorular — Fourier Serisi]]
- [[02 LTI Sistemler ve Konvolüsyon]]
- [[04 Fourier Dönüşümü]]
