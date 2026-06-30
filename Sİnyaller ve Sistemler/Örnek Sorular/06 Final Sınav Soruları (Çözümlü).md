---
tags: [ss, final, sınav-soruları, çözümlü, fourier-serisi, fourier-dönüşümü, frekans-yanıtı, konvolüsyon]
---

# 06 — Final Sınav Soruları (Çözümlü · Sıfırdan Öğretici)

← [[SS Ana Sayfa]]  ·  Ek çözümlü örnekler & grafikler: [[08 Çalışma Kağıdı — Çözümlü Soru Bankası]]

> Kaynak: `_dataset/Sinyaller Ve Sistemler/SS_Final.pdf` · resmi çözüm `SS Çalışma Kağıdı 3–8.jpeg`

> [!abstract] Bu sınav neyi ölçüyor? (önce büyük resim)
> Final **Fourier ağırlıklı**: konvolüsyon (S1) + Fourier serisi (S2) + Fourier dönüşümü (S3) + frekans yanıtıyla çıkış (S4). Ortak fikir: **sinyali frekans bileşenlerine ayır, sistemi orada çarp, geri dön**.
>
> | Kısaltma / sembol | Açılım (İng. → Tür.) |
> |---|---|
> | **CTFS** | Continuous-Time Fourier Series → **Sürekli-zaman Fourier serisi** (periyodik sinyaller) |
> | **CTFT** | Continuous-Time Fourier Transform → **Sürekli-zaman Fourier dönüşümü** (her sinyal) |
> | $c_n,\,a_k$ | Fourier serisi katsayısı → $n.$ **harmoniğin ağırlığı** |
> | $X(j\omega)$ | spektrum → sinyalin **frekans içeriği** |
> | $\omega_0$ | fundamental frequency → **temel açısal frekans** $=2\pi/T_0$ |
> | $H(j\omega)$ | frequency response → **frekans yanıtı** (sistemin her frekansa kazancı/fazı) |
>
> **Nereden geliyor?** Bir LTI sistemde karmaşık üstel $e^{j\omega t}$ **özfonksiyondur**: çıkış aynı frekansta, sadece $H(j\omega)$ ile çarpılmış. Bu yüzden $Y(j\omega)=H(j\omega)X(j\omega)$ — tüm Fourier yöntemi buradan doğar. Euler köprüsü ($\cos,\sin\to e^{\pm j\theta}$) ise sinüsleri bu üstellere çevirmemizi sağlar.

---

## Soru 1 — Sistem Özellikleri ve Konvolüsyon (25p)

**Verilen:**
$$x(t) = \begin{cases} 1, & 0 < t < 1 \\ -1, & 1 < t < 2 \\ 0, & \text{diğer} \end{cases}$$
$$h(t) = u(t) - u(t-2) = \begin{cases} 1, & 0 \leq t \leq 2 \\ 0, & \text{diğer} \end{cases}$$

> [!question] 📝 Soru metni (sınavda sorulan)
> $x(t)$ sinyali transfer fonksiyonu $h(t)=u(t)-u(t-2)$ olan bir sisteme girmektedir.
> **a)** Sistem özelliklerini; nedensellik, hafıza ve kararlılık açısından sebepleri ile yazınız? **(9p)**
> **b)** Sistem çıkışını $y(t)=x(t)*h(t)$ konvolüsyon işlemini yaparak elde ediniz? **(16p)**

> [!note]- Semboller
> - $x(t)$: giriş (±1 darbe çifti); $h(t)$: $[0,2]$ kapısı (dürtü yanıtı, genişlik 2)
> - $u(t)$: birim basamak; nedensellik: $h(t)=0,\ t<0$
> - BIBO: $\int|h|dt<\infty$; $\tau$: konvolüsyon değişkeni
> - $y(t)=\int_{t-2}^{t}x(\tau)d\tau$: genişliği 2 olan kayan pencere

---

### 1a — Sistem Özellikleri (9p)

| Özellik | Karar | Gerekçe |
|---------|-------|---------|
| **Nedensellik** | ✅ Nedensel | $h(t) = 0$ için $t < 0$ — sistem geleceği kullanmıyor |
| **Hafıza** | Hafızalı | $h(t) \neq \delta(t)$ — çıkış geçmiş girişlere bağımlı |
| **Kararlılık** | ✅ BIBO Kararlı | $\int_{-\infty}^{\infty}\|h(t)\|dt = \int_{0}^{2}1\,dt = 2 < \infty$ |

---

### 1b — Konvolüsyon y(t) (16p)

$$y(t) = \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$$

$h(t-\tau)=1$ için $0 \leq t-\tau \leq 2$, yani $t-2 \leq \tau \leq t$:

$$y(t) = \int_{t-2}^{t} x(\tau)\,d\tau$$

**Bölge analizi:**

**Bölge 1:** $t \leq 0$ → pencere tamamen sola → $y(t) = 0$

**Bölge 2:** $0 < t \leq 1$
Pencere $[t-2, t]$, $t-2 < 0$, kesişim $[0, t]$ ile $x=1$:
$$y(t) = \int_{0}^{t}1\,d\tau = t$$

**Bölge 3:** $1 < t \leq 2$
Pencere $[t-2, t]$, $t-2 \in (-1,0)$, kesişim $[0,1]$ ve $[1,t]$:
$$y(t) = \int_{0}^{1}1\,d\tau + \int_{1}^{t}(-1)\,d\tau = 1-(t-1) = 2-t$$

**Bölge 4:** $2 < t \leq 3$
Pencere $[t-2, t]$, $t-2 \in (0,1)$, $t > 2$ (x=0 için $\tau>2$):
$$y(t) = \int_{t-2}^{1}1\,d\tau + \int_{1}^{2}(-1)\,d\tau = (1-(t-2)) + (-1) = 2-t$$

**Bölge 5:** $3 < t \leq 4$
Pencere $[t-2, t]$, $t-2 \in (1,2)$, sadece $x=-1$ bölgesi:
$$y(t) = \int_{t-2}^{2}(-1)\,d\tau = -(2-(t-2)) = t-4$$

**Bölge 6:** $t > 4$ → $y(t) = 0$

$$\boxed{y(t) = \begin{cases} 0, & t \leq 0 \\ t, & 0 < t \leq 1 \\ 2-t, & 1 < t \leq 3 \\ t-4, & 3 < t \leq 4 \\ 0, & t > 4 \end{cases}}$$

**Grafik (numpy — "yansıt-kaydır-çarp-topla" 5 adımı, panel 5 = $y(t)$):**

![[ss-konv-kayan-pencere.png]]

**Süreklilik kontrolü:** $t=1$: $1=1$ ✓ | $t=3$: $2-3=-1=3-4$ ✓ | $t=4$: $0$ ✓

---

## Soru 2 — Fourier Serisi (25p)

**Verilen:**
$$x(t) = 2\sin\!\left(\frac{\pi}{4}t + \frac{\pi}{8}\right) + \cos\!\left(\frac{\pi}{2}t + \frac{\pi}{4}\right) - 1$$

> [!question] 📝 Soru metni (sınavda sorulan)
> Yukarıdaki $x(t)$ sinyalinin,
> **a)** Fourier seri açılımını yaparak katsayılarını bulunuz? **(15p)**
> **b)** Genlik ve faz spektrumlarını çiziniz? **(10p)**

> [!note]- Semboller
> - $\omega_1,\omega_2$: bileşen frekansları; $T_0=\text{OKK}(T_1,T_2)$: ortak periyot; $\omega_0=2\pi/T_0$: temel frekans
> - $c_n$: karmaşık Fourier katsayısı ($x=\sum_n c_n e^{jn\omega_0 t}$); $n$: harmonik indeksi
> - Euler: $\sin\theta=\frac{1}{2j}(e^{j\theta}-e^{-j\theta})$, $\cos\theta=\frac12(e^{j\theta}+e^{-j\theta})$
> - $-j=e^{-j\pi/2}$ → faz kaydırır; gerçel sinyalde $c_{-n}=c_n^*$ (|·| çift, ∠ tek)

---

### 2a — Fourier Seri Katsayıları (15p)

**Büyük resim:** Fourier serisi bir periyodik sinyali dönen kompleks üstellerin toplamı olarak yazar:

$$x(t) = \sum_{n=-\infty}^{\infty} c_n\, e^{jn\omega_0 t}$$

$c_n$ → $n.$ harmoniğin ağırlığı. Görevimiz: verilen $x(t)$'yi bu forma sokmak ve her $c_n$'i okumak. Sinyal zaten sinüs+kosinüs toplamı olduğundan Euler formülleriyle direkt dönüştüreceğiz.

---

**① Temel frekansı bul**

Her bileşenin $\omega$'sını oku, $T = 2\pi/\omega$'dan periyodunu bul:

| Terim | $\omega$ | $T = 2\pi/\omega$ |
|---|---|---|
| $\sin\!\left(\frac{\pi}{4}t+\ldots\right)$ | $\omega_1 = \pi/4$ | $T_1 = 8$ |
| $\cos\!\left(\frac{\pi}{2}t+\ldots\right)$ | $\omega_2 = \pi/2$ | $T_2 = 4$ |

İkisi birlikte ne zaman tekrarlar? $T_0 = \text{OKK(EKOK)}(8,4) = 8$

$$\omega_0 = \frac{2\pi}{T_0} = \frac{2\pi}{8} = \frac{\pi}{4}$$

> $\omega_1 = 1\cdot\omega_0$ → 1. harmonik; $\omega_2 = 2\cdot\omega_0$ → 2. harmonik. Yani $n=\pm1$ ve $n=\pm2$'de terimler olacak.

---

**② Euler formülleri — araç kutusu**

$$\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2} \qquad \sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$$

Pratik not: $\dfrac{1}{j} = -j$ (çünkü $j \cdot (-j) = -j^2 = 1$). Bunu kullanarak $\dfrac{1}{2j} = \dfrac{-j}{2}$ yazar.

---

**③ 1. terimi dönüştür: $2\sin\!\left(\omega_0 t + \frac{\pi}{8}\right)$**

Euler'deki $\theta = \omega_0 t + \pi/8$ al:

$$2\sin\!\left(\omega_0 t + \tfrac{\pi}{8}\right) = 2\cdot\frac{e^{j(\omega_0 t+\pi/8)}-e^{-j(\omega_0 t+\pi/8)}}{2j}$$

2'ler sadeleşir, $\frac{1}{j} = -j$, üstelleri ayır:

$$= -j\left[e^{j\omega_0 t}\cdot e^{j\pi/8} - e^{-j\omega_0 t}\cdot e^{-j\pi/8}\right]$$

$$= \underbrace{(-j\,e^{j\pi/8})}_{c_1}\cdot e^{j\omega_0 t} + \underbrace{(+j\,e^{-j\pi/8})}_{c_{-1}}\cdot e^{-j\omega_0 t}$$

Katsayıları oku:
- $c_1 = -j\,e^{j\pi/8}$ → genlik: $|-j|\cdot|e^{j\pi/8}| = 1\cdot1 = 1$ → faz: $\angle(-j)+\angle(e^{j\pi/8}) = -\frac{\pi}{2}+\frac{\pi}{8} = -\frac{3\pi}{8}$
- $c_{-1} = j\,e^{-j\pi/8}$ → genlik: $1$ → faz: $+\frac{\pi}{2}-\frac{\pi}{8} = +\frac{3\pi}{8}$

> Kontrol: $c_{-1} = c_1^*$ ✓ (gerçel sinyal özelliği)

---

**④ 2. terimi dönüştür: $\cos\!\left(2\omega_0 t + \frac{\pi}{4}\right)$**

Euler'de $\theta = 2\omega_0 t + \pi/4$:

$$\cos\!\left(2\omega_0 t + \tfrac{\pi}{4}\right) = \frac{e^{j(2\omega_0 t+\pi/4)}+e^{-j(2\omega_0 t+\pi/4)}}{2}$$

$$= \underbrace{\frac{1}{2}e^{j\pi/4}}_{c_2}\cdot e^{j2\omega_0 t} + \underbrace{\frac{1}{2}e^{-j\pi/4}}_{c_{-2}}\cdot e^{-j2\omega_0 t}$$

Katsayıları oku:
- $c_2 = \frac{1}{2}e^{j\pi/4}$ → genlik: $1/2$ → faz: $+\pi/4$
- $c_{-2} = \frac{1}{2}e^{-j\pi/4}$ → genlik: $1/2$ → faz: $-\pi/4$

---

**⑤ DC terim: $-1$**

$-1$ sabit (frekansı yok) → $n=0$ terimi → $c_0 = -1$

Genlik: $|-1| = 1$. Faz: $\angle(-1) = \pi$ (negatif gerçel sayı $\pi$ rad döndürülmüş)

---

**Tüm katsayılar:**

| $n$ | $c_n$ | $\|c_n\|$ | $\angle c_n$ |
|---|---|---|---|
| $0$ | $-1$ | $1$ | $\pi$ rad |
| $+1$ | $-je^{j\pi/8} = e^{-j3\pi/8}$ | $1$ | $-3\pi/8$ rad |
| $-1$ | $je^{-j\pi/8} = e^{+j3\pi/8}$ | $1$ | $+3\pi/8$ rad |
| $+2$ | $\frac{1}{2}e^{j\pi/4}$ | $1/2$ | $+\pi/4$ rad |
| $-2$ | $\frac{1}{2}e^{-j\pi/4}$ | $1/2$ | $-\pi/4$ rad |
| diğer | $0$ | — | — |

---

### 2b — Genlik ve Faz Spektrumları (10p)

**Nedir bu spektrumlar?**

- **Genlik spektrumu** $|c_n|$: hangi harmonik ne kadar güçlü — $n$ ekseninde dikey çizgiler
- **Faz spektrumu** $\angle c_n$: her harmoniğin faz kayması

**Simetri özellikleri** (gerçel sinyal → her zaman geçerli):

$$|c_{-n}| = |c_n| \quad \text{(genlik çift simetrik)}$$
$$\angle c_{-n} = -\angle c_n \quad \text{(faz tek simetrik)}$$

**Genlik ve Faz Spektrumu:**

![[ss-q5-spektrum.png|637]]

---

## Soru 3 — Fourier Dönüşümü (25p)

**Verilen:**
$$x(t) = e^{1+t}u(1-t)$$

> [!question] 📝 Soru metni (sınavda sorulan)
> $x(t)=e^{1+t}u(1-t)$ sinyalinin Fourier dönüşümünü alınız? **(25p)**

> [!tip] 📘 Önce kavram — bu soru neden farklı?
> Buradaki tuzak $u(1-t)$: **aynalanmış basamak**. $u(1-t)=1$ koşulu $1-t>0$, yani $t<1$ demek → sinyal **sola** uzanır (sağ tarafı kesilmiş). Çoğu tablo çifti sağa uzanan ($u(t)$) sinyaller için. Bu yüzden tabloyu körlemesine kullanamayız; **tanımdan integral** alırız: $X(j\omega)=\int x(t)e^{-j\omega t}dt$. Yakınsama, üstelin $t\to-\infty$'da sönmesine bağlıdır — onu kontrol etmek şart.

> [!note]- Semboller
> - $u(1-t)$: $t\le1$'de 1 olan **yansımış** basamak (sağ tarafı keser)
> - $x(t)=e^{1+t}$ ($t\le1$): sola doğru sönen üstel; destek $(-\infty,1]$
> - $X(j\omega)=\int x(t)e^{-j\omega t}dt$: CTFT
> - Yakınsama: $\mathrm{Re}(1-j\omega)=1>0$ → integral $-\infty$'da sıfıra gider
> - $|X|$: genlik, $\angle X$: faz spektrumu

**① $u(1-t)$ nedir? — tuzak burada**

Normal $u(t) = 1$ iken $t \geq 0$. Ama $u(1-t)$'de argüman $(1-t)$:
$$u(1-t) = 1 \iff 1-t > 0 \iff t < 1$$

Yani $t \leq 1$'de 1, $t > 1$'de 0 → normal basamağın **aynası**, sağ tarafı $t=1$'de kesilmiş.

**② Sinyalin şekli:**

$$x(t) = \begin{cases} e^{1+t}, & t \leq 1 \\ 0, & t > 1 \end{cases}$$

- $t=1$'de tepe: $e^{1+1} = e^2 \approx 7.39$
- $t \to -\infty$'da $e^{1+t} \to 0$ → sinyal **sola** doğru sönüyor
- Tablo çiftleri $u(t)$ (sağa uzanan) için → **tanımdan integral almak gerekiyor**

**③ İntegral kurulumu — neden $-\infty$'dan $1$'e?**

$u(1-t)$ yüzünden $t > 1$'de $x(t) = 0$, üst sınır $\infty$ değil $1$:

$$X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}\,dt = \int_{-\infty}^{1} e^{1+t}\,e^{-j\omega t}\,dt$$

$e^{1+t} = e \cdot e^t$ diye ayır, sabit $e$'yi dışarı çek, üstelleri birleştir:

$$= e\int_{-\infty}^{1} e^{t}\,e^{-j\omega t}\,dt = e\int_{-\infty}^{1} e^{(1-j\omega)t}\,dt$$

**④ Yakınsama kontrolü — alt sınır sorunsuz mu?**

Alt sınır $-\infty$; $t \to -\infty$'da $e^{(1-j\omega)t}$ ne yapar?

$$\left|e^{(1-j\omega)t}\right| = e^{\,\mathrm{Re}(1-j\omega)\cdot t} = e^{1\cdot t} = e^t \xrightarrow{t\to-\infty} 0 \checkmark$$

$\mathrm{Re}(1-j\omega) = 1 > 0$ → katsayı pozitif, $t$ negatif gittikçe üstel sönüyor. İntegral yakınsar.

**⑤ İntegrali hesapla:**

$$e\int_{-\infty}^{1} e^{(1-j\omega)t}\,dt = e\left[\frac{e^{(1-j\omega)t}}{1-j\omega}\right]_{-\infty}^{1}$$

- **Alt sınır** ($t\to-\infty$): $e^{(1-j\omega)t} \to 0$ → katkısı yok
- **Üst sınır** ($t=1$): $e^{(1-j\omega)\cdot 1} = e^{1}\cdot e^{-j\omega}$

$$= e \cdot \frac{e^{1}\cdot e^{-j\omega} - 0}{1-j\omega} = \frac{e^2\, e^{-j\omega}}{1-j\omega}$$

$$\boxed{X(j\omega) = \frac{e^2\, e^{-j\omega}}{1-j\omega}}$$

**Sonucu oku:**

| Terim | Nereden geliyor | Ne anlama gelir |
|---|---|---|
| $e^2$ | $e\cdot e^1$ (üst sınırdan) | düz büyüklük ölçeği |
| $e^{-j\omega}$ | $t=1$'de kesim | faz kayması ($t=1$ gecikmesi gibi) |
| $\dfrac{1}{1-j\omega}$ | üstelin şekli | frekans zarfı, $\omega$ büyüdükçe küçülür |

**Genlik ve faz:**

$$|X(j\omega)| = \frac{e^2}{\sqrt{1+\omega^2}}, \qquad \angle X(j\omega) = -\omega + \arctan(\omega)$$

> $e^{-j\omega}$ faza $-\omega$ katar. $\angle(1-j\omega) = -\arctan\omega$ (dördüncü çeyrek) → payda fazı tersine çevirir: $+\arctan\omega$.

---

## Soru 4 — Frekans Yanıtı ile Sistem Çıkışı (25p)

**Verilen:**
$$H(j\omega) = \frac{j\omega+4}{2-\omega^2+3j\omega}$$
$$x(t) = e^{-4(t-2)}u(t-2)$$

> [!question] 📝 Soru metni (sınavda sorulan)
> Frekans yanıtı $H(j\omega)=\dfrac{j\omega+4}{2-\omega^2+3j\omega}$ olan bir sisteme $x(t)=e^{-4(t-2)}u(t-2)$ sinyali verilmektedir. Sistem çıkışında oluşan $y(t)$ sinyalini elde ediniz? **(25p)**

> [!tip] 📘 Önce kavram — strateji
> "Sisteme giriş verilmiş, çıkışı bul" = frekansta **çarp**: $Y(j\omega)=H(j\omega)\,X(j\omega)$, sonra ters dönüşümle $y(t)$. İki anahtar hamle: **(1)** paydadaki $2-\omega^2+3j\omega$'yı $s=j\omega$ koyarak $s^2+3s+2$ gibi çarpanlarına ayır (kutupları gör); **(2)** $X$'i bilinen çift + zaman kaydırma ile yaz. Sonunda **kısmi kesirler** her terimi tabloya indirger.

> [!note]- Semboller
> - $H(j\omega)$: frekans yanıtı; $s=j\omega$ ile $-\omega^2+3j\omega+2 = s^2+3s+2$
> - $x(t)$: 2 birim gecikmeli üstel; zaman kaydırma $f(t-2)\leftrightarrow e^{-2j\omega}F(j\omega)$
> - $Y=H\cdot X$: çıkış spektrumu; $A,B$: kısmi kesir katsayıları
> - Ters çift: $\frac{1}{j\omega+a}\leftrightarrow e^{-at}u(t)$; kutuplar $-1,-2$ → kararlı

---

### Adım 1 — Paydayı Çarpanlara Ayır

$s = j\omega$ yerine koyunca:
$$2 - \omega^2 + 3j\omega = s^2 + 3s + 2 = (s+1)(s+2) = (j\omega+1)(j\omega+2)$$

$$\boxed{H(j\omega) = \frac{j\omega+4}{(j\omega+1)(j\omega+2)}}$$

---

### Adım 2 — X(jω) Bul

$x(t) = e^{-4(t-2)}u(t-2)$: $f(t) = e^{-4t}u(t)$'nin 2 birim gecikmesi.

**① $f(t) = e^{-4t}u(t)$'nin dönüşümü — tanımdan:**

$$F(j\omega) = \int_{-\infty}^{\infty} e^{-4t}u(t)\,e^{-j\omega t}\,dt = \int_{0}^{\infty} e^{-(4+j\omega)t}\,dt$$

$$= \left[\frac{e^{-(4+j\omega)t}}{-(4+j\omega)}\right]_0^{\infty} = 0 - \frac{1}{-(4+j\omega)}$$

$$\mathcal{F}\{e^{-4t}u(t)\} = \frac{1}{j\omega+4}$$

> $t\to\infty$'da $e^{-4t}\to 0$ ($4>0$ şartı), üst sınır sıfırlanır.

**② Zaman kaydırma teoremi:** $x(t) = f(t-2) \Rightarrow X(j\omega) = F(j\omega)\,e^{-2j\omega}$

> **Neden?** Tanımda $\tau = t-2$ koy → $e^{-j\omega(\tau+2)}d\tau = e^{-2j\omega}\cdot e^{-j\omega\tau}d\tau$; $e^{-2j\omega}$ sabit olarak dışarı çıkar.

$$X(j\omega) = \frac{e^{-2j\omega}}{j\omega+4}$$

---

### Adım 3 — Y(jω) Hesapla

$$Y(j\omega) = H(j\omega)\,X(j\omega) = \frac{j\omega+4}{(j\omega+1)(j\omega+2)} \cdot \frac{e^{-2j\omega}}{j\omega+4}$$

$$Y(j\omega) = \frac{e^{-2j\omega}}{(j\omega+1)(j\omega+2)}$$

---

### Adım 4 — Kısmi Kesirler (Cover-Up Yöntemi)

Hedef: $\dfrac{1}{(j\omega+1)(j\omega+2)}$ ifadesini tablodan okuyabileceğimiz basit kesirlere ayırmak.

$$\frac{1}{(j\omega+1)(j\omega+2)} = \frac{A}{j\omega+1} + \frac{B}{j\omega+2}$$

Her iki tarafı $(j\omega+1)(j\omega+2)$ ile çarp → özdeşlik elde et:

$$1 = A(j\omega+2) + B(j\omega+1)$$

**A için:** $j\omega = -1$ koy → $B$ terimi düşer:

$$1 = A\underbrace{(-1+2)}_{=\,1} + B\cdot 0 \implies \boxed{A = 1}$$

> Kural: hangi kutbu arıyorsan o kutbun paydakesrini "ört" (cover-up), geri kalanı değerlendir.
> $A$ için $(j\omega+1)$'i ört → $\dfrac{1}{j\omega+2}\big|_{j\omega=-1} = \dfrac{1}{1} = 1$

**B için:** $j\omega = -2$ koy → $A$ terimi düşer:

$$1 = A\cdot 0 + B\underbrace{(-2+1)}_{=\,-1} \implies \boxed{B = -1}$$

> $(j\omega+2)$'yi ört → $\dfrac{1}{j\omega+1}\big|_{j\omega=-2} = \dfrac{1}{-1} = -1$

$$Y(j\omega) = e^{-2j\omega}\left[\frac{1}{j\omega+1} - \frac{1}{j\omega+2}\right]$$

---

### Adım 5 — Ters Fourier

**Temel çift** (ezbere / tablodan):

$$\frac{1}{j\omega+a} \;\xleftrightarrow{\;\mathcal{F}^{-1}\;}\; e^{-at}u(t)$$

Her terimi ayrı ayrı uygula:

$$\mathcal{F}^{-1}\!\left\{\frac{1}{j\omega+1}\right\} = e^{-t}u(t) \qquad (a=1)$$

$$\mathcal{F}^{-1}\!\left\{\frac{1}{j\omega+2}\right\} = e^{-2t}u(t) \qquad (a=2)$$

Şimdi önde $e^{-2j\omega}$ var — bu **zaman kaydırma** demek:

$$e^{-2j\omega} \cdot F(j\omega) \;\xleftrightarrow{\;\mathcal{F}^{-1}\;}\; f(t-2)$$

> Her $e^{-at}u(t)$'yi $f(t)$ say, $e^{-2j\omega}$ faktörü $t$'yi $(t-2)$ yapar, $u(t)$'yi $u(t-2)$ yapar.

İkisini birden uygula:

$$e^{-2j\omega}\cdot\frac{1}{j\omega+1} \;\to\; e^{-(t-2)}u(t-2)$$

$$e^{-2j\omega}\cdot\frac{1}{j\omega+2} \;\to\; e^{-2(t-2)}u(t-2)$$

Süperpozisyon (A=1, B=−1):

$$\boxed{y(t) = \left[e^{-(t-2)} - e^{-2(t-2)}\right]u(t-2)}$$

**Yorum:**
- $t < 2$: $y(t) = 0$ (sistem nedensel, giriş $t=2$'de başlıyor)
- $t \geq 2$: çıkış iki üstel bileşenin farkı; $e^{-(t-2)}$ daha yavaş söner
- Uzun vadede: $y(t) \to 0$ (kararlı sistem, $\text{Re}(p_{1,2}) < 0$)
