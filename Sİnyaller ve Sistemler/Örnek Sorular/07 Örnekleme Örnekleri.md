---
tags: [ss, ornekleme, sampling, ornek-sorular, bolum7]
---

# 07 Örnekleme Örnekleri (Bölüm 7)

← [[SS Ana Sayfa]] | Teori: [[../Konu Anlatımları/05 Örnekleme|05 Örnekleme]]

---

## Temel Sorular (7.8–7.20)

### 7.8 — Fourier Serisi + Örnekleme

$x(t) = \sum_{k=-\infty}^{\infty}\!\left(\tfrac{1}{2}\right)^k\!\sin(k\pi t)$ sinyali gerçek, tek ve periyodik olsun. $T = 0.2$ ile dürtü-katarı örneklemesi yapılıyor.

**(a)** Örnekleme $x(t)$'de örtüşme oluşturur mu?

**(b)** $\pi/T$ kesim, $T$ geçirme kazançlı ideal LPF'den geçirilirse $g(t)$'nin Fourier serisi nedir?

---

### 7.9 — Örnekleme Frekansı Seçimi

$$x(t) = \left(\frac{\sin 50\pi t}{\pi t}\right)^2$$

$G(j\omega)$ dönüşümlü $g(t)$ elde etmek için $\omega_s = 150\pi$ örnekleme kullanılıyor.

Şu eşitliği gerçekleştiren $\omega_s$'nin en yüksek değerini bulun:

$$|\omega| \leq \omega_s \text{ için } G(j\omega) = 75X(j\omega)$$

---

### 7.10 — Doğru / Yanlış

Aşağıdakilerin doğru mu yanlış mı olduğunu belirleyin:

**(a)** $x(t) = u(t+T_0) - u(t-T_0)$; örnekleme $T \leq 2T_0$ ise örtüşmesiz.

**(b)** $X(j\omega) = u(\omega+\omega_0) - u(\omega-\omega_0)$; örnekleme $T < \pi/\omega_0$ ise örtüşmesiz.

**(c)** $X(j\omega) = u(\omega-\omega_0)$; $T < 2\pi/\omega_0$ ise dürtü-katarı örneklemesi ile geçirilebilir.

---

### 7.11 — Ayrık Zaman Sinyali Özellikleri

$|\omega| \geq 2000\pi$ için $X_d(j\omega) = 0$ olan sürekli sinyal örnekleniyor:

$$x_d[n] = x_c\!\left(n \times 0.5\times10^{-3}\right)$$

Aşağıdakilerden hangisi doğru/yanlış?

**(a)** $X_d(e^{j\omega})$ gerçektir.
**(b)** Tüm $\omega$ için $|X_d(e^{j\omega})|$ en yüksek değeri 1'dir.
**(c)** $3\pi/4 \leq |\omega| \leq \pi$ için $X_d(e^{j\omega}) = 0$.
**(d)** $X_d(e^{j\omega}) = X_d(e^{j(\omega+\pi)})$.

---

### 7.12 — Yeniden Oluşturma Sıfırları

$X_d(e^{j\omega}) = 0$ için $3\pi/4 \leq |\omega| \leq \pi$ özelliğiyle ayrık zaman sinyali $x_d[n]$.

$T = 10^{-3}$ ile sürekli zaman sinyaline dönüştürülmüş $x_c(t)$'nin Fourier dönüşümünün sıfır olacağı tüm $\omega$ değerlerini bulunuz.

---

### 7.13 — Filtre Tasarımı (Şekil 7.24)

Filtre yaklaşımı: periyot $T$, giriş bant sınırlı; $|\omega| \geq \pi/T$ için $X_d(e^{j\omega}) = 0$.

Tüm sistem $y_c(t) = x_c(t-2T)$ özelliğine sahipse $h[n]$ atım tepkisini belirle.

---

### 7.15 — Etki Örneklemesi

$x[n]$'in etki örneklemesi şu yaklaşımla yapılıyor:

$$g[n] = \sum_{k=-\infty}^{\infty} x[n]\,\delta[n-kN]$$

$3\pi/7 \leq |\omega| \leq \pi$ için $X(e^{j\omega}) = 0$ ise, örtüşme oluşmaksızın $x[n]$'in $g[n]$'den elde edilebileceği $N$'nin en büyük değerini belirleyin.

---

## Temel Problemler (7.21–7.35)

### 7.21 — Örnekleme Teoremi Koşulları

$X(j\omega)$ Fourier dönüşümlü $x(t)$; dürtü-katar örnekleme, $T = 10^{-4}$.

$$x_p(t) = \sum_{n=-\infty}^{\infty} x[nT]\,\delta(t-nT)$$

Verilen koşullar için (a)–(f) örnekleme teoremi uygulanabilirliğini sorgula.

---

### 7.22 — Bant Sınırlı Evrişim

$y(t) = x_1(t) * x_2(t)$; $x_1(t)$ bant sınırlı ($|X_1(j\omega)| = 0$ için $|\omega| > 1000\pi$) ve $x_2(t)$ bant sınırlı ($|X_2(j\omega)| = 0$ için $|\omega| > 2000\pi$).

Örtüşmesiz dürtü-katar örneklemesini $y(t)$'de gerçekleştirmek için en büyük $T$ değerini bulun.

---

### 7.23 — Periyodik Çarpan ile Örnekleme

Şekil P7.23: giriş $x(t)$, $X(j\omega)$ verilen; $-\omega_M \leq \omega \leq \omega_M$ bant.

**(a)** $\Delta < \pi/(2\omega_M)$ için $x_p(t)$ ve $y(t)$'nin Fourier dönüşümünü çiz.
**(b)** $\Delta < \pi/(2\omega_M)$ için $x_p(t)$'den $x(t)$'yi elde edecek sistemi belirle.
**(c)** $\Delta < \pi/(2\omega_M)$ için $x(t)$'den $y(t)$'yi elde edecek sistemi belirle.
**(d)** $x(t)$'yi $x_p(t)$'den elde edecek en büyük $\Delta$ değeri ($\omega_M$ cinsinden)?

---

### 7.24 — Periyodik Kare Dalga Örneklemesi

Periyodik kare dalgası ile çarpılmış giriş $x(t)$; $s(t)$ periyotu $T$, $|X(j\omega)| = 0$ için $|\omega| \geq \omega_M$.

**(a)** $\Delta = T/3$ için: $X(j\omega)$'nin $W(j\omega)$ içindeki çoğaltmalarının örtüşmediği durumlarda $\omega_M$ için en büyük $T$ nedir?

**(b)** $\Delta = T/4$ için aynı analiz.

---

### 7.25 — Yeniden Oluşturma Formülü

Şekil P7.25: $x(t)$'yi $x_p(t)$'den yeniden oluşturmak için ideal alçak geçirgenli filtre. $\omega_c = 2\pi T$, $\omega_c = \omega_s/2$, $x_r(kT) = x(kT)$.

$\omega_c = \omega_s/2$ için:

$$x_r(t) = \sum_{n=-\infty}^{\infty} x[nT]\,\frac{\sin\!\left[\frac{\pi}{T}(t-nT)\right]}{\frac{\pi}{T}(t-nT)} \tag{P7.25-1}$$

Kısıtlama olmadan tüm $k$ tam sayı için $x_r(kT) = x(kT)$ olduğunu göster.

---

### 7.26 — Bant-Geçiş Örneklemesi

Şekil P7.26: $x(t)$ bant-geçiş sinyali, $\omega_1 < |\omega| < \omega_2$ aralığında. $X_r(t) = x(t)$ olmak üzere $\omega_1, \omega_2, \omega_0, A$ sabitlerini kullanarak örtüşmesiz örnekleme için maksimum $T$ değerini bulun.

---

### 7.28 — Periyodik Sinyal + Düşük Geçirgenli Filtre

$x(t)$ girdi periyotu $0.1$ s; Fourier serisi katsayıları $a_k = (1/2)^{|k|}$. Örnekleme $T = 5 \times 10^{-3}$ s.

**(a)** $x[n]$'in periyodik dizi olduğunu göster ve periyodunu bul.

**(b)** $x[n]$'in Fourier serisi katsayılarını bul.

---

### 7.30 — Numuneleyici + LTI Sistem

Şekil P7.30: $x_c(t)$ girdisi birim atımlı $\delta(t)$. Sürekli-zaman LTI sistemi:

$$\frac{dy_c(t)}{dt} + y_c(t) = x_c(t)$$

**(a)** $y_c(t)$'yi bulun.

**(b)** $W[n] = \delta[n]$ olacak şekilde $H(e^{j\omega})$ frekans tepkisini ve $h[n]$ atılım tepkisini bulun.

---

### 7.32 — Üst Örnekleme

$x[n]$ sinyali: $X(e^{j\omega}) = 0$ için $\pi/4 \leq |\omega| \leq \pi$. Başka bir sinyal:

$$g[n] = x[n] \sum_{k=-\infty}^{\infty}\delta[n-1-4k]$$

$g[n]$ girildiğinde $x[n]$ çıkışı veren düşük geçirgenli bir filtrenin $H(e^{j\omega})$ frekans tepkisini bulun.

---

## İleri Seviyeli Problemler (7.36–7.51, seçmeler)

### 7.37 — Band-Sınırlı Yeniden Yapılanma

$|t| < W$ bant genişliğinde sınırlı sinyal. Şekil P7.37:

- $X(j\omega) = 0$, $|\omega| > W$
- $p(t)$ değişgen uzamlı periyodik darbe serisi
- $H_1(j\omega)$: 90° fazlı bir yer değiştirici; $f(t)$ ikili zincirine çarpıldığında $f(0) = a$ ve $f(\Delta) = b$

Parametreler $a, b, \Delta$ değerleri için bul.

---

### 7.41 — Eko Giderme

Şekil P7.41: $s(t) = x(t) + \alpha x(t - T_0)$, $|\alpha| < 1$.

**(a)** $\pi/\omega_M \leq T_0 \leq 2\pi/\omega_M$ ise digital $h[n]$ fark denklemini belirle.

**(b)** Bölüm (a)'yı farz ederek ideal alçak geçirgenli filtrelerin $A$ artışını belirle.

---

### 7.42 — Örnekleme Enerjisi

Şekil P7.42: Nyquist oranından daha yüksek örneklenmiş $x_c(t)$.

$$E_d = \sum_{n=-\infty}^{\infty}|x[n]|^2, \quad E_c = \int_{-\infty}^{\infty}|x_c(t)|^2\,dt$$

$E_d$ sıra enerjisi ile $E_c$ orijinal sinyal enerjisi ve örnekleme $T$ aralığı arasındaki ilişkiyi belirle.

---

### 7.50 — Sıfırcı- ve Birinci-Dereceden Tutma

Şekil P7.50: ZOH ve FOH (birinci dereceden tutma) karşılaştırması.

**(a)** ZOH için $h[n]$ ve $H(e^{j\omega})$'yu belirleyip taslağını çiz.

**(b)** FOH için $H(e^{j\omega})$'yu belirleyip taslağını çiz.

---

> [!warning] Örnekleme Tuzakları (Sınav İçin)
> - $X(j\omega)$ bant genişliği $\omega_M$ → Nyquist: $T < \pi/\omega_M$ (**$\omega$ cinsinden**)
> - Örtüşme sonrası yeniden oluşturma **imkânsız** — sadece önüne geçilir
> - Spektrum kopyaları $\omega_s = 2\pi/T$ aralıkta → $T$ küçüldükçe kopyalar uzaklaşır
> - Yeniden oluşturma filtresi: kazanç $T$, kesim $\omega_c \in [\omega_M, \omega_s - \omega_M]$
> - ZOH'u ideal LPF'den geçirince $T \to 0$ yaklaşık ideal olur

← [[SS Ana Sayfa]] | [[SS Sınav Gecesi]] | Teori: [[../Konu Anlatımları/05 Örnekleme|05 Örnekleme]]
