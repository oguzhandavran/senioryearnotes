---
tags: [ssi, dsp, final, bitirme, sınav-soruları, çözümlü, transfer-fonksiyonu, fourier, parseval, dtft, filtre, z-dönüşümü, roc]
---

# 06 — Final (Bitirme) Soruları (Çözümlü · Sıfırdan Öğretici)

← [[SSI Ana Sayfa]]  ·  Vize için: [[05 Vize Sınav Soruları (Çözümlü)]]

> Kaynak: `_dataset/Sayısal Sinyal İşleme/SSI Bitirme Sınavı.jpeg` — Sayısal Sinyal İşleme · 5 soru (toplam 100p)

> [!abstract] Bu sınav neyi ölçüyor? (önce büyük resim)
> Final **frekans-domeni ağırlıklı**: $h[n]$ + sistem özellikleri (S1), **DT Fourier serisi spektrumu + Parseval gücü** (S2), **DTFT** anti-nedensel sinyal (S3), **alçak geçiren filtreleme + kesim frekansı tasarımı** (S4), **iki-taraflı Z-dönüşümü + ROC** (S5). Ortak fikir: sinyali frekans/$z$ bileşenlerine ayır, sistemi orada uygula, geri dön.
>
> | Kısaltma / sembol | Açılım (İng. → Tür.) |
> |---|---|
> | **DTFS** | Discrete-Time Fourier Series → **ayrık-zaman Fourier serisi** (periyodik $x[n]$) |
> | **DTFT** | Discrete-Time Fourier Transform → **ayrık-zaman Fourier dönüşümü** $X(e^{j\omega})$ |
> | **MA / LPF** | Moving Average / Low-Pass Filter → **hareketli ortalama / alçak geçiren filtre** |
> | **ROC** | Region of Convergence → **yakınsama bölgesi** ($Z$ toplamının yakınsadığı $|z|$ aralığı) |
> | $a_k,\,c_k$ | Fourier series coefficient → **Fourier serisi katsayısı** ($k.$ harmoniğin ağırlığı) |
> | $\omega_c$ | cutoff frequency → **kesim frekansı** (filtrenin geçirme sınırı) |
> | $H(e^{j\omega})$ | frequency response → **frekans yanıtı** (her frekansa kazanç/faz) |
> | $u[-n-1]$ | anti-causal (left-sided) step → **anti-nedensel** (sol-taraflı) basamak: yalnız $n\le-1$'de 1 |
>
> **Neden Parseval?** Periyodik bir sinyalin ortalama gücü, zaman ortalaması yerine **katsayıların karelerinin toplamı** ile bulunabilir: $P=\sum_k|a_k|^2$. **Neden ROC?** İki-taraflı bir sinyalde her terimin yakınsama koşulu farklıdır; ortak $|z|$ aralığı (kesişim) dönüşümün geçerli olduğu bölgedir; birim çember bu aralıktaysa DTFT vardır.

---

## Soru 1 — Eşdeğer $h[n]$ + Kararlılık/Nedensellik (20p)

> [!question] 📝 Soru metni (sınavda sorulan)
> Aşağıda diyagramı verilen sistemin ($h_1[n]=\delta[n]+0.5\,\delta[n-1]$ ile $h_3[n]=\delta[n]-0.5\,\delta[n-2]$ **seri/üst kol**, $h_2[n]=-0.2\,\delta[n+1]$ **paralel/alt kol**),
> **a)** Transfer fonksiyonunu, $h[n]$ elde ediniz. (15p)
> **b)** Kararlılık ve nedensellik açısından tanımlayınız. (5p)

> [!note]- Semboller
> - Üst kol seri: $h_1*h_3$ (konvolüsyon) · alt kol paralel: $+h_2$
> - $\delta[n-k]\leftrightarrow z^{-k}$, $\;\delta[n+k]\leftrightarrow z^{+k}$ ($+$ gelecek = nedensel değil)
> - FIR (sonlu $h$) → daima kararlı; $\sum|h|<\infty$
> - $h[n+1]$ türü ileri terim → nedensellik bozulur

> [!tip] 📘 Önce kavram — aynı kalıp, sayılar farklı
> [[05 Vize Sınav Soruları (Çözümlü)|Vize S3]] ile birebir aynı yapı: **seri kol konvolüsyon, paralel kol toplama**. Tek fark, bloklar artık $\delta$-toplamları olduğundan konvolüsyonu $z$-domeninde polinom çarpımı olarak yapmak daha hızlı.

**Blok şeması** (üst kol seri $h_1\!\to\!h_3$, alt kol paralel $h_2$, sonra toplanır):

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,font=\footnotesize,
  blk/.style={draw,rounded corners,minimum height=0.95cm,align=center}]
\node (xin) at (-0.3,0) {$x[n]$};
\coordinate (split) at (1.1,0);
\node[blk,minimum width=3.4cm] (h1) at (3.5,1.5) {$h_1[n]=\delta[n]+0.5\,\delta[n-1]$};
\node[blk,minimum width=3.4cm] (h3) at (7.5,1.5) {$h_3[n]=\delta[n]-0.5\,\delta[n-2]$};
\node[blk,minimum width=3.4cm] (h2) at (3.5,-1.5) {$h_2[n]=-0.2\,\delta[n+1]$};
\node[draw,circle,inner sep=1.5pt] (sum) at (9.9,0) {\large$+$};
\node (yout) at (11.3,0) {$y[n]$};
\draw[->] (xin) -- (split);
\fill (split) circle (1.6pt);
\draw[->] (split) |- (h1.west);
\draw[->] (h1.east) -- (h3.west);
\draw[->] (h3.east) -| (sum.north);
\draw[->] (split) |- (h2.west);
\draw[->] (h2.east) -| (sum.south);
\draw[->] (sum.east) -- (yout);
\end{tikzpicture}
\end{document}
```

**Çözüm.**

> [!example]- $\delta[n-k]\leftrightarrow z^{-k}$ kuralı nereden geliyor? (sıfırdan)
> $z$-dönüşümünün tanımı $X(z)=\sum_n x[n]z^{-n}$. Kaydırılmış dürtü $x[n]=\delta[n-k]$ yalnız $n=k$'de $1$, başka yerde $0$. Toplamda tek terim hayatta kalır:
> $$\mathcal Z\{\delta[n-k]\}=\sum_n \delta[n-k]\,z^{-n}=z^{-k}$$
> Yani $k$ örneklik **gecikme** $=z^{-k}$ (negatif üs = geçmiş). Tersine $\delta[n+k]$ ($k$ örneklik **ileri/gelecek**) $=z^{+k}$ — pozitif üs çıkması "nedensel değil"in işaretidir.

**a) $z$-domeninde:** (her $\delta[n\mp k]\to z^{\mp k}$)
$$H_1(z)=1+0.5z^{-1},\qquad H_3(z)=1-0.5z^{-2},\qquad H_2(z)=-0.2\,z^{+1}$$

Üst kol (seri = çarpım):
$$H_1H_3=(1+0.5z^{-1})(1-0.5z^{-2})=1+0.5z^{-1}-0.5z^{-2}-0.25z^{-3}$$

Paralel kol ekle:
$$\boxed{H(z)=-0.2\,z+1+0.5z^{-1}-0.5z^{-2}-0.25z^{-3}}$$

Ters dönüşüm (her $z^{-k}\to\delta[n-k]$):
$$\boxed{h[n]=-0.2\,\delta[n+1]+\delta[n]+0.5\,\delta[n-1]-0.5\,\delta[n-2]-0.25\,\delta[n-3]}$$

| $n$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|
| $h[n]$ | $-0.2$ | $1$ | $0.5$ | $-0.5$ | $-0.25$ |

![[ssi-f-s1-h.png]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-f-s1-h.py` — `np.convolve(h1,h3)` + $h_2$ ($n=-1$).

**b) Özellikler:**

| Özellik         | Karar          | Gerekçe                                                                         |
| --------------- | -------------- | ------------------------------------------------------------------------------- |
| **Nedensellik** | ❌ Değil        | $h[-1]=-0.2\neq0$ → $n<0$'da değer ($h_2=\delta[n+1]$ bir örnek geleceğe bakar) |
| **Kararlılık**  | ✅ BIBO kararlı | $\sum h=0.2+1+0.5+0.5+0.25=2.45<\infty$ (FIR → daima kararlı)                   |


> [!success] 🎯 Çıkarım
> $z$-domeninde polinom çarpımı, elle konvolüsyondan hızlıdır. $\delta[n+1]$ gibi **artı-indeksli** terim gördüğünde otomatik "nedensel değil" de; FIR olduğu için kararlılık zaten garantidir.

---

## Soru 2 — Fourier Serisi Spektrumu + Parseval Gücü (20p)

> [!question] 📝 Soru metni (sınavda sorulan)
> $x[n]=3\cos\!\left(\dfrac{\pi}{4}n\right)+2\sin\!\left(\dfrac{\pi}{2}n\right)$ sinyalinin,
> **a)** Genlik ve faz spektrumlarını çiziniz? (15p)
> **b)** Parseval teoremini kullanarak sinyalin toplam gücünü hesaplayınız. (5p)

> [!note]- Semboller
> - Euler: $\cos\theta=\tfrac12(e^{j\theta}+e^{-j\theta})$, $\;\sin\theta=\tfrac{1}{2j}(e^{j\theta}-e^{-j\theta})$
> - $\tfrac{1}{j}=-j=e^{-j\pi/2}$ → $\sin$ terimleri $\mp\tfrac{\pi}{2}$ faz taşır
> - Spektrum çizgileri $\omega=k\omega_0$'da; genlik $=|c_k|$, faz $=\angle c_k$
> - Parseval (DT periyodik): $P=\sum_k|c_k|^2$

> [!tip] 📘 Önce kavram — sinüsleri üstel çizgilere çevir
> Her $\cos/\sin$, $\pm\omega$'da iki kompleks üstel çizgiye ayrılır. Genlik spektrumu bu çizgilerin boyları, faz spektrumu açılarıdır. $\cos$ simetrik (faz 0); $\sin$ ise $\tfrac{1}{j}=-j$ çarpanı yüzünden $\mp90°$ faz taşır. Gerçel sinyalde daima $c_{-k}=c_k^*$ (genlik çift, faz tek).

**Çözüm.**

### 2a — Genlik ve Faz Spektrumu (15p)

**Büyük resim — DTFS nedir, "$a_k$" formülü nereden geliyor?**

*Bak periyot CTFT de $T_0$ idi, DTFT de ise şimdi $N$*

Periyodu $N$ olan ayrık-zaman bir sinyali, frekansları **temel frekans** $\omega_0=\tfrac{2\pi}{N}$'in tam katları olan dönen kompleks üstellerin toplamı olarak yazabiliriz — buna **ayrık-zaman Fourier serisi (DTFS)** denir:

$$x[n]=\sum_{k=\langle N\rangle} a_k\, e^{jk\omega_0 n},\qquad \omega_0=\frac{2\pi}{N}$$

> **SS dersindeki CTFS'den** (Continuous-Time Fourier Series → sürekli-zaman Fourier serisi) **tek farkı:** CT'de $\sum_{n=-\infty}^{\infty}$ (sonsuz harmonik) vardı; DT'de frekanslar $2\pi$'de tekrar ettiği için yalnızca **$N$ tane** ayrı harmonik olur ($\langle N\rangle$ = ardışık $N$ değer). $a_k$ → $k.$ harmoniğin ağırlığı (kompleks: genlik + faz).

Görevimiz: verilen $x[n]$'i bu forma sokup her $a_k$'yı **okumak**. Sinyal zaten $\cos+\sin$ toplamı olduğundan integral/analiz formülüne ($a_k=\tfrac1N\sum_n x[n]e^{-jk\omega_0 n}$) gerek yok — **Euler** ile doğrudan çevireceğiz.

---

**① Temel frekansı (ve $N$'i) bul**

Her bileşenin $\omega$'sını oku, $N=\tfrac{2\pi}{\omega}$'dan periyodunu bul:

| Terim | $\omega$ | $N=\tfrac{2\pi}{\omega}$ |
|---|---|---|
| $3\cos\!\left(\tfrac{\pi}{4}n\right)$ | $\omega_1=\tfrac{\pi}{4}$ | $N_1=8$ |
| $2\sin\!\left(\tfrac{\pi}{2}n\right)$ | $\omega_2=\tfrac{\pi}{2}$ | $N_2=4$ |

İkisi birlikte ne zaman tekrarlar? $N=\text{EKOK}(8,4)=8$:

$$\omega_0=\frac{2\pi}{N}=\frac{2\pi}{8}=\frac{\pi}{4}$$

> $\omega_1=1\cdot\omega_0$ → 1. harmonik ($k=\pm1$); $\omega_2=2\cdot\omega_0$ → 2. harmonik ($k=\pm2$).

---

**② Euler araç kutusu** (her şey buradan türeyecek)

$$\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}{2}\qquad\qquad \sin\theta=\frac{e^{j\theta}-e^{-j\theta}}{2j}$$

Pratik not: $\dfrac{1}{j}=-j$ (çünkü $j\cdot(-j)=-j^2=+1$), yani $\dfrac{1}{2j}=\dfrac{-j}{2}$.

---

**③ $\cos$ terimini çevir: $3\cos\!\left(\tfrac{\pi}{4}n\right)$**

Euler'de $\theta=\tfrac{\pi}{4}n=\omega_0 n$ al:

$$3\cos\!\left(\omega_0 n\right)=3\cdot\frac{e^{j\omega_0 n}+e^{-j\omega_0 n}}{2}=\underbrace{\tfrac32}_{a_1}\,e^{j\omega_0 n}+\underbrace{\tfrac32}_{a_{-1}}\,e^{-j\omega_0 n}$$

Oku: $a_1=a_{-1}=\tfrac32$ → genlik $1.5$, faz $0$ (gerçel-pozitif). $\cos$ simetrik olduğu için faz taşımaz.

---

**④ $\sin$ terimini çevir: $2\sin\!\left(\tfrac{\pi}{2}n\right)$**

Euler'de $\theta=\tfrac{\pi}{2}n=2\omega_0 n$, ve $\tfrac{1}{j}=-j$ kullan:

$$2\sin\!\left(2\omega_0 n\right)=2\cdot\frac{e^{j2\omega_0 n}-e^{-j2\omega_0 n}}{2j}=\frac{1}{j}\big(e^{j2\omega_0 n}-e^{-j2\omega_0 n}\big)=\underbrace{(-j)}_{a_2}\,e^{j2\omega_0 n}+\underbrace{(+j)}_{a_{-2}}\,e^{-j2\omega_0 n}$$

Oku: $a_2=-j$ → genlik $|-j|=1$, faz $\angle(-j)=-\tfrac{\pi}{2}$; $a_{-2}=+j$ → genlik $1$, faz $+\tfrac{\pi}{2}$. İşte $\sin$'in $\mp\tfrac{\pi}{2}$ fazı buradan, $\tfrac1j=-j$ çarpanından geliyor.

> Kontrol: $a_{-1}=a_1^*$ ve $a_{-2}=a_2^*$ ✓ (gerçel sinyal → genlik çift, faz tek).

---

**Tüm katsayılar:**

| $\omega$             | $-\tfrac{\pi}{2}$ | $-\tfrac{\pi}{4}$ | $+\tfrac{\pi}{4}$ | $+\tfrac{\pi}{2}$ |
| -------------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| $a_k$                | $+j$              | $\tfrac32$        | $\tfrac32$        | $-j$              |
| **Genlik** $\|a_k\|$ | $1$               | $1.5$             | $1.5$             | $1$               |
| **Faz** $\angle a_k$ | $+\tfrac{\pi}{2}$ | $0$               | $0$               | $-\tfrac{\pi}{2}$ |

![[ssi-f-s2-spektrum.png]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-f-s2-spektrum.py` — sol: genlik (kırmızı), sağ: faz (mavi). Genlik çift, faz tek simetrik.

---

### 2b — Parseval ile Güç (5p)

**Parseval teoremi nereden geliyor? (sıfırdan türetim)**

Periyodik bir sinyalin **ortalama gücü**nün tanımı, bir periyot boyunca $|x[n]|^2$'nin ortalamasıdır:

$$P=\frac{1}{N}\sum_{n=\langle N\rangle}|x[n]|^2$$

Şimdi $x[n]=\sum_k a_k e^{jk\omega_0 n}$'i yerine koy ve $|x|^2=x\cdot x^*$ yaz:

$$P=\frac{1}{N}\sum_{n}\Big(\sum_k a_k e^{jk\omega_0 n}\Big)\Big(\sum_\ell a_\ell^* e^{-j\ell\omega_0 n}\Big)=\sum_k\sum_\ell a_k a_\ell^*\underbrace{\frac{1}{N}\sum_{n}e^{j(k-\ell)\omega_0 n}}_{\text{diklik}}$$

Anahtar — **diklik (orthogonality):** üstellerin bir periyot üzerindeki ortalaması, yalnız $k=\ell$ iken $1$, aksi halde $0$'dır:

$$\frac{1}{N}\sum_{n=\langle N\rangle}e^{j(k-\ell)\omega_0 n}=\begin{cases}1,& k=\ell\\ 0,& k\neq\ell\end{cases}$$

Bu yüzden tüm **çapraz terimler** ($k\neq\ell$) ölür, geriye yalnız $k=\ell$ kalır:

$$\boxed{P=\sum_{k=\langle N\rangle}|a_k|^2}$$

İşte Parseval teoremi — "zaman ekseninde güç = katsayıların kareleri toplamı". Şimdi uygula:

$$P=\sum_k|a_k|^2=\underbrace{1.5^2+1.5^2}_{\pm\pi/4}+\underbrace{1^2+1^2}_{\pm\pi/2}=2.25+2.25+1+1=\boxed{6.5}$$

**Kontrol (zaman domeni):** her sinüzoidin gücü $\tfrac{A^2}{2}$ → $\tfrac{3^2}{2}+\tfrac{2^2}{2}=4.5+2=6.5$ ✓

> [!success] 🎯 Çıkarım
> DTFS: periyodik DT sinyali $N$ harmoniğin toplamı olarak yaz, Euler ile katsayıları **oku**. $\cos\to$ faz 0, $\sin\to$ faz $\mp\tfrac{\pi}{2}$ ($\tfrac1j=-j$ yüzünden). Parseval ($\sum|a_k|^2$) **diklikten** doğar; sinüzoid başına $\tfrac{A^2}{2}$ ile kontrol et — ikisi aynı çıkar.

---

## Soru 3 — Anti-nedensel Sinyalin DTFT'si (20p)

> [!question] 📝 Soru metni (sınavda sorulan)
> $x[n]=\left(\dfrac{1}{2}\right)^{-n+1}u[-n]$ sinyalinin Ayrık-Zamanlı Fourier Dönüşümünü, $X(e^{j\omega})$ alınız? (20p)

> [!note]- Semboller
> - $u[-n]$: yalnız $n\le0$ → **sol-taraflı (anti-nedensel)** sinyal
> - $\left(\tfrac12\right)^{-n+1}=\tfrac12\cdot 2^{\,n}$ → $n\to-\infty$'da söner (DTFT yakınsar)
> - Değişken değişimi $m=-n$ ile toplamı standart geometrik seriye çevir
> - $\sum_{m=0}^{\infty}r^m=\tfrac{1}{1-r}$, $|r|<1$

> [!tip] 📘 Önce kavram — sol-taraflıyı sağ-taraflıya çevir
> Toplam $n\le0$ üzerinde. $m=-n$ koyunca $m\ge0$ üzerinde tanıdık geometrik seri çıkar. Önce $\left(\tfrac12\right)^{-n+1}$'i sadeleştir: bu aslında $\tfrac12\cdot 2^{n}$'dir — $n\to-\infty$'da $2^n\to0$ olduğundan sinyal sola doğru söner ve DTFT yakınsar.

**Çözüm.**

**Büyük resim — DTFT formülü $X(e^{j\omega})=\sum_n x[n]e^{-j\omega n}$ nereden geliyor?**

Fikir, SS dersindeki Fourier dönüşümünün ayrık karşılığıdır: bir sinyali farklı frekanslardaki $e^{j\omega n}$ "dönen vektörlerine" ayırıp her frekansın **ne kadar var olduğunu** ölçmek. Bir $\omega$ frekansının ağırlığını bulmak için sinyali o frekansın **eşleniğiyle** ($e^{-j\omega n}$) çarpıp tüm $n$ üzerinde toplarız (eşleşen frekans güçlenir, eşleşmeyenler ortalamada söner):

$$X(e^{j\omega})\;\triangleq\;\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}$$

Bu, $z$-dönüşümünün $z=e^{j\omega}$ (birim çember) üzerine indirgenmiş hâlidir. Toplamın **yakınsaması** sinyalin sönmesine bağlıdır — onu kontrol etmek şart.

Tanımı uygula ($u[-n]$ yüzünden yalnız $n\le0$ terimleri var):
$$X(e^{j\omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n}=\sum_{n=-\infty}^{0}\left(\tfrac12\right)^{-n+1}e^{-j\omega n}$$

$m=-n$ ($n=-m$, $\;n:-\infty\to0 \Rightarrow m:\infty\to0$), ve $e^{-j\omega n}=e^{-j\omega(-m)}=e^{+j\omega m}$:
$$=\sum_{m=0}^{\infty}\left(\tfrac12\right)^{m+1}e^{\,j\omega m}=\tfrac12\sum_{m=0}^{\infty}\left(\tfrac12 e^{\,j\omega}\right)^{m}$$

> [!example]- Geometrik seri $\sum_{m=0}^{\infty}r^m=\tfrac{1}{1-r}$ nereden geliyor? (sıfırdan)
> Sonlu toplamı $S_M=1+r+r^2+\dots+r^{M-1}$ yazalım. İki numara: $S_M$'i $r$ ile çarp, çıkar:
> $$S_M-rS_M=(1+r+\dots+r^{M-1})-(r+r^2+\dots+r^{M})=1-r^{M}$$
> $$\Rightarrow S_M=\frac{1-r^{M}}{1-r}$$
> $|r|<1$ iken $M\to\infty$'da $r^{M}\to0$, dolayısıyla $\displaystyle\sum_{m=0}^{\infty}r^m=\frac{1}{1-r}$. Burada $r=\tfrac12 e^{j\omega}$, $|r|=\tfrac12<1$ → yakınsar.

Ortak oran $r=\tfrac12 e^{j\omega}$ ($|r|=\tfrac12<1$):
$$=\tfrac12\cdot\frac{1}{1-\tfrac12 e^{\,j\omega}}$$

$$\boxed{X(e^{j\omega})=\frac{1/2}{\,1-\tfrac12 e^{\,j\omega}\,}=\frac{1}{\,2-e^{\,j\omega}\,}}$$

> [!success] 🎯 Çıkarım
> Sol-taraflı sinyalde refleks: $m=-n$ değişimiyle sağ-taraflı geometrik seriye çevir. Dikkat — üs pozitif $e^{+j\omega m}$ çıkar (çünkü $e^{-j\omega n}=e^{+j\omega m}$). Önce üssü sadeleştirmek ($\left(\tfrac12\right)^{-n+1}=\tfrac12\cdot2^n$) yakınsamayı görmeyi kolaylaştırır.

---

## Soru 4 — Alçak Geçiren Filtreleme + Kesim Tasarımı (20p)

> [!question] 📝 Soru metni (sınavda sorulan)
> $x[n]$ sinyali $N=5$ ile periyodik olup Fourier katsayıları $a_k=1,\;\forall k\in\{-2,-1,0,1,2\}$ şeklinde verilmiştir. Bu sinyalin $\omega_c=\dfrac{\pi}{2}$ kesim frekansına sahip bir hareketli ortalama (MA) alan bir alçak geçiren filtreden geçmesi durumunda,
> **a)** $y[n]$ çıkış sinyalini elde ediniz. (10p)
> **b)** Kesim frekansını küçültmek için yeni tasarlanacak filtrede ne gibi bir değişiklik yapılması gerekmektedir. (10p)

> [!note]- Semboller
> - $x[n]=\sum_{k=-2}^{2}a_k e^{jk\omega_0 n}$, $\omega_0=\tfrac{2\pi}{5}$ → harmonikler $\omega=k\cdot\tfrac{2\pi}{5}$
> - LPF: $|\omega|\le\omega_c$ harmoniklerini geçirir, ötesini bastırır
> - $\omega_c=\tfrac{\pi}{2}=0.5\pi$ ile harmonikleri karşılaştır
> - MA filtre uzunluğu $M$ ↔ kesim $\omega_c\approx\tfrac{2\pi}{M}$ (ters orantı)

> [!tip] 📘 Önce kavram — hangi harmonik geçer?
> Filtre frekans-domeninde **kapı** gibidir: $|\omega|\le\omega_c$ olan harmonikler geçer, büyük olanlar silinir. O yüzden her harmoniğin frekansını ($k\omega_0$) hesaplayıp $\omega_c$ ile kıyaslamak yeter.

**Çözüm.**

**a)** Harmonik frekansları $\omega_0=\tfrac{2\pi}{5}=0.4\pi$:

| $k$ | $0$ | $\pm1$ | $\pm2$ |
|---|---|---|---|
| $\|\omega\|=\|k\|\omega_0$ | $0$ | $0.4\pi$ | $0.8\pi$ |
| $\omega_c=0.5\pi$ ile | $\le$ → **geçer** | $0.4\pi<0.5\pi$ → **geçer** | $0.8\pi>0.5\pi$ → **bastırılır** |

Yani $k=0,\pm1$ geçer, $k=\pm2$ silinir (ideal geçirme bandı kazancı 1):
$$y[n]=a_0+a_1e^{j\omega_0 n}+a_{-1}e^{-j\omega_0 n}=1+e^{j2\pi n/5}+e^{-j2\pi n/5}$$
$$\boxed{y[n]=1+2\cos\!\left(\tfrac{2\pi}{5}n\right)}$$

**b) Kesim frekansını küçültmek:** MA filtresinin kesim frekansı uzunluğuyla **ters orantılıdır**: $\omega_c\approx\dfrac{2\pi}{M}$. Daha küçük $\omega_c$ için → **filtre uzunluğunu $M$ artır** (daha çok örneği ortala). Daha uzun pencere = daha dar ana lob = daha düşük kesim = daha güçlü düzleştirme.
**$M$-nokta MA filtresinin genel formülü:**
$$y[n]=\frac{1}{M}\sum_{k=0}^{M-1}x[n-k],\qquad h[n]=\frac1M\big(u[n]-u[n-M]\big)=\frac1M\{\underbrace{1,1,\dots,1}_{M}\}_{n=0\dots M-1}$$
(son $M$ örneğin ortalaması; bkz. [[05 Vize Sınav Soruları (Çözümlü)|Vize S5]] — orada aynı formül $N=3$ ile somutlaştırılmıştı.) Dürtü yanıtı uzunluk-$M$ dikdörtgen olduğundan ana lobu $\propto\dfrac{2\pi}{M}$ genişliktedir, kesim frekansı da kabaca bununla orantılıdır:
$$\boxed{\omega_c\downarrow \iff M\uparrow\;(\text{ortalanan örnek sayısını / filtre tap sayısını artır})}$$

> [!success] 🎯 Çıkarım
> Filtreleme = "harmoniği frekansına göre geçir veya sil". MA filtresinde **uzunluk ↔ kesim ters orantı**: daha dar bant (daha çok yumuşatma) istiyorsan pencereyi uzat. Bkz. [[05 Vize Sınav Soruları (Çözümlü)|Vize S5]] (MA = düzleştirme).

---

## Soru 5 — İki-taraflı Z-Dönüşümü + ROC (20p)

> [!question] 📝 Soru metni (sınavda sorulan)
> $x[n]=(0.4)^{n}u[n]+(-2)^{n}u[-n-1]$ sinyalinin,
> **a)** Z-dönüşümünü işlemleri göstererek alınız. (10p)
> **b)** Çözüm bölgesini (ROC) bulunuz. (10p)

> [!note]- Semboller
> - $u[n]$: sağ-taraflı (nedensel); $u[-n-1]$: sol-taraflı (anti-nedensel)
> - Çift 1: $a^n u[n]\leftrightarrow\dfrac{1}{1-az^{-1}}$, ROC $|z|>|a|$ (dışarısı)
> - Çift 2: $a^n u[-n-1]\leftrightarrow\dfrac{-1}{1-az^{-1}}$, ROC $|z|<|a|$ (içerisi)
> - İki-taraflı → ROC iki bölgenin **kesişimi** = **halka**

> [!tip] 📘 Önce kavram — sağ ↔ dışarısı, sol ↔ içerisi
> Sağ-taraflı (nedensel) terim, en büyük kutbunun **dışında** yakınsar ($|z|>|a|$); sol-taraflı (anti-nedensel) terim kutbunun **içinde** ($|z|<|a|$). İki-taraflı sinyalin ROC'u bu ikisinin kesişimidir; kesişim boş değilse bir **halka** (annulus) çıkar ve dönüşüm geçerlidir.

**Çözüm.**

**a) Terim terim:**

*Terim 1* (nedensel): $z$-tanımını uygula, $(0.4)^n z^{-n}=(0.4z^{-1})^n$ diye topla → ortak oran $r=0.4z^{-1}$ olan geometrik seri:
$$(0.4)^n u[n]\;\xrightarrow{\;\mathcal Z\;}\;\sum_{n=0}^{\infty}(0.4z^{-1})^{n}\overset{\text{geo.}}{=}\dfrac{1}{1-0.4z^{-1}},\qquad\text{yakınsama }|0.4z^{-1}|<1\Rightarrow|z|>0.4.$$
($\sum_0^\infty r^n=\tfrac{1}{1-r}$ türetimi yukarıda **S3'teki geometrik seri kutusunda** verildi.)

*Terim 2* (anti-nedensel): $(-2)^n u[-n-1]$. $m=-n$ ile
$$\sum_{n=-\infty}^{-1}(-2)^n z^{-n}=\sum_{m=1}^{\infty}(-2)^{-m}z^{m}=\sum_{m=1}^{\infty}\left(\tfrac{z}{-2}\right)^m=\frac{z/(-2)}{1-z/(-2)}=\frac{-1}{1-(-2)z^{-1}}=\frac{-1}{1+2z^{-1}}$$
yakınsama $\left|\tfrac{z}{-2}\right|<1\Rightarrow|z|<2$.

Topla:
$$\boxed{X(z)=\frac{1}{1-0.4z^{-1}}-\frac{1}{1+2z^{-1}}}$$

Kutuplar: $z=0.4$ (Terim 1) ve $z=-2$ (Terim 2).

**b) ROC:** iki koşulun kesişimi:
$$|z|>0.4\quad\text{VE}\quad|z|<2\;\Longrightarrow\;\boxed{0.4<|z|<2}$$

Bu bir **halka**dır. $0.4<2$ olduğundan kesişim boş değil → $X(z)$ var. Birim çember ($|z|=1$) halkanın içinde → **DTFT de var**.

![[ssi-f-s5-roc.png]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-f-s5-roc.py` — kutuplar $\times$ ($0.4$, $-2$), yeşil halka ROC, noktalı birim çember içeride.

> [!success] 🎯 Çıkarım
> Nedensel terim → kutbun **dışı**, anti-nedensel → **içi**; iki-taraflı sinyalde ROC bir **halka**dır. Halka birim çemberi içeriyorsa sistem kararlıdır / DTFT vardır. Anti-nedensel çiftin işaretine ($-1$) ve $u[-n-1]$'in $n\le-1$ desteğine dikkat.

---

## Soru Tipini Tanıma Rehberi (Final)

| Görünce...                      | Yöntem                           | Anahtar formül/kural                                                       |
| ------------------------------- | -------------------------------- | -------------------------------------------------------------------------- |
| seri/paralel $\delta$ blokları  | $z$-domeninde polinom çarp+topla | seri $\to\times$, paralel $\to+$; $\delta[n+k]\to z^{+k}$                  |
| $\cos/\sin$ toplamı, "spektrum" | Euler → çizgiler                 | $\cos$ faz 0, $\sin$ faz $\mp\tfrac\pi2$; $c_{-k}=c_k$                     |
| "Parseval ile güç"              | $\sum                            | c_k^2$$=\sum\tfrac{A_i^2}{2}$ (sinüzoid kontrolü)                          |
| $u[-n]$ / $u[-n-1]$ + DTFT/Z    | $m=-n$ değişimi                  | sol-taraflı → geometrik seri; üs $e^{+j\omega m}$                          |
| "LPF'den geçir", $a_k$ verili   | harmoniği $\omega_c$ ile kıyasla | $\|k\omega_0\|\le\omega_c$ → geçer                                         |
| "kesimi küçült" (MA)            | uzunluğu artır                   | $\omega_c\approx\tfrac{2\pi}{M}$, $M\uparrow\Rightarrow\omega_c\downarrow$ |
| iki-taraflı $x[n]$ + ROC        | terim terim + kesişim            | nedensel→dışı, anti→içi; ROC = halka                                       |

---

## Bağlantılı Notlar

- [[05 Vize Sınav Soruları (Çözümlü)]]
- [[../Konu Anlatımları/02 Z-Dönüşümü]]
- [[../Konu Anlatımları/03 DFT ve FFT]]
- [[../Konu Anlatımları/04 Sayısal Filtre Tasarımı]]
- [[02 Z-Dönüşümü Örnekleri]]
