---
tags: [ssi, dsp, vize, sınav-soruları, çözümlü, enerji, seyreltme, konvolüsyon, lti, dtft, transfer-fonksiyonu]
---

# 05 — Vize (Ara Sınav) Soruları (Çözümlü · Sıfırdan Öğretici)

← [[SSI Ana Sayfa]]  ·  Final için: [[06 Final Sınav Soruları (Çözümlü)]]

> Kaynak: `_dataset/Sayısal Sinyal İşleme/SSI Ara Sınavı.pdf` — MSÜ HHO, 3. Sınıf Elektronik Müh., Sayısal Sinyal İşleme · 7 soru · 120 dk · hesap makinesi serbest

> [!abstract] Bu sınav neyi ölçüyor? (önce büyük resim)
> Vize **temel ayrık-zaman araçları**nı yokluyor: dizi çizme + **enerji** (S1), **seyreltme/örnekleme** (S2), **konvolüsyon + sistem özellikleri** (S3), **LTI testi** (S4), **hareketli ortalama filtresi** (S5), **DTFT özelliği** (S6), **frekans yanıtı → transfer fonksiyonu** (S7). Ortak fikir: bir sistemi tamamen **dürtü yanıtı $h[n]$** (veya transfer fonksiyonu $H(z)$) belirler.
>
> | Kısaltma / sembol | Açılım (İng. → Tür.) |
> |---|---|
> | **DT** | Discrete-Time → **ayrık-zaman** ($x[n]$, yalnız tam sayı $n$) |
> | **LTI** | Linear Time-Invariant → **doğrusal & zamanla-değişmez** |
> | **MA** | Moving Average → **hareketli ortalama** (basit alçak geçiren filtre) |
> | **DTFT** | Discrete-Time Fourier Transform → **ayrık-zaman Fourier dönüşümü** $X(e^{j\omega})$ |
> | **BIBO** | Bounded-Input Bounded-Output → **sınırlı giriş→sınırlı çıkış** (kararlılık) |
> | $u[n]$ | unit step → **birim basamak** ($n\ge 0$ için 1) |
> | $\delta[n]$ | unit impulse → **birim dürtü** ("iğne", yalnız $n=0$'da 1) |
> | $h[n]$ | impulse response → **dürtü yanıtı**; $H(z)=\mathcal Z\{h[n]\}$ transfer fonk. |
> | $*$ | convolution → **konvolüsyon (evrişim)** |
>
> **Neden enerji $=\sum |x[n]|^2$?** Elektrikte $1\,\Omega$ dirençte anlık güç $|x|^2$; toplam enerji bunun toplamıdır. **Neden konvolüsyon?** LTI sistem her girişi kaydırılmış dürtülere ayırır ($x[n]=\sum_k x[k]\delta[n-k]$), her birinin yanıtını ($x[k]\,h[n-k]$) toplar → $y=x*h$.

---

## Soru 1 — Dizi Çizimi ve Enerji (10p)

> [!question] 📝 Soru metni (sınavda sorulan)
> $x[n]=\left(\dfrac{1}{2}\right)^{n}u[n]$ sinyalini **çiziniz** ve **enerjisini hesaplayınız?** (10p)

> [!note]- Semboller
> - $u[n]$: birim basamak → sinyal yalnız $n\ge0$'da var, $n<0$'da sıfır
> - $\left(\tfrac12\right)^n$: her adımda yarıya inen üstel sönüm
> - $E_\infty=\sum_n |x[n]|^2$: toplam enerji; sönen sinyal → sonlu enerji (enerji sinyali)
> - Geometrik seri: $\sum_{n=0}^{\infty} r^n=\dfrac{1}{1-r}$, $|r|<1$ iken

> [!tip] 📘 Önce kavram — geometrik seri toplamı
> Sönen üstel bir sinyalin enerjisi her zaman bir **geometrik seriye** dönüşür. Kareyi aldığımızda taban da karelenir: $\left(\tfrac12\right)^n$ → kare → $\left(\tfrac14\right)^n$. Oran $r=\tfrac14<1$ olduğu için seri yakınsar ve toplam $\dfrac{1}{1-r}$ ile bulunur. Bu, "sönen sinyal = enerji sinyali" kuralının somut halidir.

**Çözüm.**

**Çizim:** $n=0,1,2,\dots$ için değerler $1,\ \tfrac12,\ \tfrac14,\ \tfrac18,\dots$ — sıfırdan başlayıp hızla sönen pozitif iğneler ($n<0$'da hiç yok).

![[ssi-v-s1-enerji.png]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-v-s1-enerji.py` — gri ×'ler $|x[n]|^2$ (enerji katkıları).

> [!example]- Geometrik seri $\sum_{n=0}^{\infty}r^n=\tfrac{1}{1-r}$ nereden geliyor? (sıfırdan)
> Sonlu toplam $S_M=1+r+\dots+r^{M-1}$. $S_M$'i $r$ ile çarpıp çıkar: $S_M-rS_M=1-r^{M}$ → $S_M=\dfrac{1-r^{M}}{1-r}$. $|r|<1$ iken $M\to\infty$'da $r^M\to0$, dolayısıyla $\displaystyle\sum_{n=0}^{\infty}r^n=\frac{1}{1-r}$. Aşağıda $r=\tfrac14<1$.

**Enerji:** ($|x[n]|^2$'de taban da karelenir: $\left(\tfrac12\right)^{2n}=\left(\tfrac14\right)^n$, oran $r=\tfrac14$)
$$E_\infty=\sum_{n=-\infty}^{\infty}|x[n]|^2=\sum_{n=0}^{\infty}\left(\tfrac12\right)^{2n}=\sum_{n=0}^{\infty}\left(\tfrac14\right)^{n}=\frac{1}{1-\tfrac14}=\boxed{\frac{4}{3}}$$

> [!success] 🎯 Çıkarım
> Sonlu enerji ($E_\infty=\tfrac43<\infty$) → **enerji sinyali**, dolayısıyla ortalama gücü $P_\infty=0$. Sönen her üstel diziyi $\sum r^n=\tfrac{1}{1-r}$ kalıbıyla bitirirsin.

> [!info] Bu Parseval teoremi mi? (adı + ham formülleri)
> Hayır — yukarıdaki $E_\infty=\sum_n|x[n]|^2$ hesabı **enerjinin doğrudan tanımı** (sadece zaman ekseninde). **Parseval teoremi** (Fransız matematikçi **Marc-Antoine Parseval**, 1799), bu zaman-ekseni toplamını **frekans ekseni** karşılığına eşitleyen *ayrı* bir sonuçtur — adı ve ham formülleri:
>
> - **DTFT (sonsuz/aperiyodik dizi) — Parseval/Plancherel ilişkisi:**
>   $$\sum_{n=-\infty}^{\infty}|x[n]|^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}\big|X(e^{j\omega})\big|^2\,d\omega$$
> - **DFT (sonlu, $N$ örneklik dizi) — Parseval ilişkisi:**
>   $$\sum_{n=0}^{N-1}|x[n]|^2=\frac{1}{N}\sum_{k=0}^{N-1}\big|X[k]\big|^2$$
> - **Fourier serisi (periyodik sürekli sinyal) — Parseval / ortalama güç:**
>   $$\frac{1}{T_0}\int_{T_0}|x(t)|^2\,dt=\sum_{k=-\infty}^{\infty}|a_k|^2$$
>
> Buradaki $\tfrac43$ sonucu sadece zaman-ekseni tanımıyla bulundu. Parseval'i kullansaydık, önce $x[n]=(\tfrac12)^n u[n]$'in DTFT'sini $X(e^{j\omega})=\dfrac{1}{1-\tfrac12 e^{-j\omega}}$ olarak alır, sonra $\frac{1}{2\pi}\int_{-\pi}^{\pi}|X(e^{j\omega})|^2\,d\omega$'yu hesaplardık — aynı $\tfrac43$ sonucunu verir, ama yol farklıdır.

---

## Soru 2 — Seyreltme (Decimation) ve Çizim (15p)

> [!question] 📝 Soru metni (sınavda sorulan)
> $x[n]=5\cos\!\left(\dfrac{2\pi}{6}n\right)$ sinyalini kullanarak, $y[n]=x[4n]$ sinyalini $-10\le n<10$ örnek aralığı için **çiziniz / elde ediniz?** (15p)

> [!note]- Semboller
> - $x[4n]$: **seyreltme (decimation)** — her 4 örnekten birini al ($n\to4n$)
> - $\omega_0=\tfrac{2\pi}{6}=\tfrac{\pi}{3}$: $x$'in açısal frekansı → periyot $N=\tfrac{2\pi}{\omega_0}=6$
> - Aliasing: DT frekans $2\pi$ ile periyodik; $\tfrac{4\pi}{3}$ aynı $\tfrac{2\pi}{3}$'tür (çünkü $\tfrac{4\pi}{3}-2\pi=-\tfrac{2\pi}{3}$, $\cos$ çift)

> [!tip] 📘 Önce kavram — "$n\to4n$" ne yapar?
> $y[n]=x[4n]$, $x$'in **4'te bir** örneklerini seçer (zamanı sıkıştırır). Frekans dört katına çıkar: $\omega_0=\tfrac{\pi}{3}\to 4\omega_0=\tfrac{4\pi}{3}$. Ama DT'de frekanslar $2\pi$'de katlanır: $\tfrac{4\pi}{3}$, $\big|\tfrac{4\pi}{3}-2\pi\big|=\tfrac{2\pi}{3}$ ile **aynı görünür**. Bu, seyreltmenin neden aliasing (takma ad) doğurabileceğinin kalbidir.

**Çözüm.**

$\omega_0=\tfrac{2\pi}{6}=\tfrac{\pi}{3}$, yani $x[n]=5\cos\!\left(\tfrac{\pi}{3}n\right)$ (temel periyot $N=6$).

$$y[n]=x[4n]=5\cos\!\left(\tfrac{\pi}{3}\cdot4n\right)=5\cos\!\left(\tfrac{4\pi}{3}n\right)=5\cos\!\left(\tfrac{2\pi}{3}n\right)$$

Son eşitlik $\tfrac{4\pi}{3}\equiv\tfrac{2\pi}{3}$ katlanmasından gelir → $y[n]$'in temel periyodu $N=\tfrac{2\pi}{2\pi/3}=3$.

**Değer tablosu (bir periyot):** $y[0]=5\cos 0=5$, $\;y[1]=5\cos\tfrac{2\pi}{3}=-2.5$, $\;y[2]=5\cos\tfrac{4\pi}{3}=-2.5$ → ardından $5,-2.5,-2.5,\dots$ (periyot 3).

![[ssi-v-s2-decimation.png]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-v-s2-decimation.py` — üst: $x[n]$ (periyot 6), alt: $y[n]=x[4n]$ (periyot 3).

> [!success] 🎯 Çıkarım
> 4 kat seyreltme, periyot-6 kosinüsü periyot-3 kosinüse çevirdi. Sınavda anahtar adımlar: (1) $\omega_0$'ı oku, (2) $4n$ koy, (3) frekansı $2\pi$ aralığına katla, (4) periyodu yaz, (5) bir periyot değer hesaplayıp tekrarla.

---

## Soru 3 — Eşdeğer Transfer Fonksiyonu + Sistem Özellikleri (15p)

**Blok şeması** ($S_4$ — üst kol seri $h_1\!\to\!h_3$, alt kol paralel $h_2$, sonra toplanır):

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,font=\footnotesize,
  blk/.style={draw,rounded corners,minimum height=0.95cm,align=center}]
\node (xin) at (-0.3,0) {$x[n]$};
\coordinate (split) at (1.1,0);
\node[blk,minimum width=3.0cm] (h1) at (3.3,1.5) {$h_1[n]=u[n]-u[n-5]$};
\node[blk,minimum width=3.0cm] (h3) at (7.0,1.5) {$h_3[n]=u[n]-u[n-2]$};
\node[blk,minimum width=3.0cm] (h2) at (3.3,-1.5) {$h_2[n]=\delta[n+2]$};
\node[draw,circle,inner sep=1.5pt] (sum) at (9.2,0) {\large$+$};
\node (yout) at (10.6,0) {$y[n]$};
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

> [!question] 📝 Soru metni (sınavda sorulan)
> Yukarıdaki blok şeması verilen $S_4$ sisteminde $h_1[n]=u[n]-u[n-5]$, $h_2[n]=\delta[n+2]$ ve $h_3[n]=u[n]-u[n-2]$ olmak üzere sistemin **eşdeğer transfer fonksiyonunu** $\big(h_4[n]\big)$ bulunuz? Sistemin **nedensellik, hafıza ve kararlılık** açısından özelliklerini $h_4[n]$ üzerinden sebepleri ile yazınız? (15p)

> [!note]- Semboller
> - Blok yapı: $h_1\!\to\!h_3$ **seri** (üst kol), $h_2$ **paralel** (alt kol), sonra toplanır
> - Seri bağlantı → dürtü yanıtları **konvolüsyon**la birleşir: $h_1*h_3$
> - Paralel bağlantı → dürtü yanıtları **toplanır**: $(\cdot)+h_2$
> - $u[n]-u[n-L]$: $n=0\dots L-1$ arası **dikdörtgen darbe** (uzunluk $L$)

> [!tip] 📘 Önce kavram — seri = konvolüsyon, paralel = toplam
> Birden çok LTI blok birbirine bağlanırsa, **tek bir eşdeğer $h_4[n]$** elde edilir. Aynı sinyalden geçen ardışık (seri) bloklar konvolüsyonla; aynı girişi paylaşıp çıkışları toplanan (paralel) bloklar toplamayla birleşir. Şema: $h_4=(h_1*h_3)+h_2$.

**Çözüm.**

**Adım 1 — Darbeleri aç:**
- $h_1[n]=u[n]-u[n-5]=\{1,1,1,1,1\}$, $\;n=0\dots4$ (uzunluk 5)
- $h_3[n]=u[n]-u[n-2]=\{1,1\}$, $\;n=0,1$ (uzunluk 2)
- $h_2[n]=\delta[n+2]$ → yalnız $n=-2$'de değeri 1

**Adım 2 — Üst kol (seri): $h_1*h_3$.** Uzunluk $5+2-1=6$, $n=0\dots5$:

> [!example]- Neden uzunluk 6 ve neden değerler 1,2,2,2,2,1? (adım adım)
> **Uzunluk neden $5+2-1=6$ (niye $-1$ var?):**
> $h_1$'in ilk dolu örneği $n=0$'da, $h_3$'ünki de $n=0$'da → ikisi çakıştığında toplamın **ilk** dolu örneği $n=0+0=0$'da çıkar. $h_1$'in **son** dolu örneği $n=4$'te, $h_3$'ünki $n=1$'de → toplamın son dolu örneği $n=4+1=5$'te çıkar. Yani çıktı $n=0$'dan $n=5$'e kadar sürüyor: $5-0+1=6$ örnek.
> Genel formülde de aynı mantık var: son indeks $=(L_1-1)+(L_2-1)$, buna ilk örneği ($n=0$) de sayınca toplam uzunluk $(L_1-1)+(L_2-1)+1=L_1+L_2-1$. "$-1$" işte bu yüzden — iki dizinin "son+son" ve "ilk+ilk" noktaları arasındaki örnek **sayısı**, uzunlukların toplamından bir eksiktir (ilk örnek iki kere sayılmasın diye).
>
> **Değerler neden 1,2,2,2,2,1:**
> Konvolüsyon tanımı $y[n]=\sum_k h_1[k]\,h_3[n-k]$. $h_3$ yalnızca $m=0,1$'de 1 olduğundan $h_3[n-k]\neq0$ sadece $k=n$ veya $k=n-1$ iken gerçekleşir. O yüzden toplam sadece iki terime iner:
> $$y[n] = h_1[n] + h_1[n-1]$$
> ($h_1[n]$, $0\le n\le4$ dışında 0 kabul edilir — yani $h_1[-1]=h_1[5]=0$.) Bu, $h_3=\{1,1\}$ ile konvolüsyonun aslında $h_1$ üzerinde **2 örnekli kayan (ardışık ikili) toplam** olduğu anlamına gelir:
>
> | $n$ | $h_1[n-1]$ | $h_1[n]$ | $y[n]=$ toplam |
> |---|---|---|---|
> | 0 | 0 (sınır dışı) | 1 | **1** |
> | 1 | 1 | 1 | **2** |
> | 2 | 1 | 1 | **2** |
> | 3 | 1 | 1 | **2** |
> | 4 | 1 | 1 | **2** |
> | 5 | 1 | 0 (sınır dışı) | **1** |
>
> Uçlarda ($n=0,5$) toplanan iki terimden biri $h_1$'in tanımlı olduğu $0..4$ aralığının dışına düşüp 0 olduğu için sonuç **1**; ortada ($n=1..4$) her iki terim de aralığın içinde (=1) olduğu için sonuç **2** çıkıyor.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $(h_1*h_3)[n]$ | 1 | 2 | 2 | 2 | 2 | 1 |

(Kayan toplam: kenarda 1, ortada iki darbe çakıştığı için 2.)

![[ssi-v-s3-konv-animasyon.gif]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-v-s3-konv-animasyon.py` — "yansıt-kaydır-çarp-topla" animasyonu: üstte $h_1[k]$ sabit, $h_3[n-k]$ kayıyor; ortada anlık çarpım; altta biriken $y[n]=(h_1*h_3)[n]$ izi. CT örneğindeki (SS dersi `ss-q2-konv-animasyon.py`) aynı mantığın ayrık-zaman (stem plot) versiyonu.

**Adım 3 — Paralel kol ekle: $h_4=(h_1*h_3)+h_2$:**

$$\boxed{h_4[n]=\delta[n+2]+\{\,\underbrace{1,2,2,2,2,1}_{n=0\dots5}\,\}}$$

yani $h_4[-2]=1$; $h_4[0..5]=1,2,2,2,2,1$; diğer her yerde 0.

![[ssi-v-s3-h4.png]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-v-s3-h4.py` — `np.convolve` ile $h_1*h_3$, üzerine $h_2$ eklendi.

**Adım 4 — Özellikler ($h_4$ üzerinden):**

| Özellik         | Karar                | Gerekçe ($h_4$ üzerinden)                                                  |
| --------------- | -------------------- | -------------------------------------------------------------------------- |
| **Nedensellik** | ❌ Nedensel **değil** | $h_4[-2]=1\neq0$ → $n<0$'da değer var ($h_2=\delta[n+2]$ geleceğe bakıyor) |
| **Hafıza**      | Hafızalı             | $h_4[n]\neq c\,\delta[n]$ → çıkış birden çok giriş örneğine bağlı          |
| **Kararlılık**  | ✅ BIBO kararlı       | $\sum_nh_4[n]=1+1+2+2+2+2+1=11<\infty$ (sonlu → FIR daima kararlı)         |


> [!success] 🎯 Çıkarım
> Bağlantı tipini görür görmez: **seri → konvolüsyon, paralel → toplama**. Özellikleri her zaman birleşik $h_4$ üzerinden oku: $n<0$'da değer = nedensel değil, $\sum|h|<\infty$ = kararlı.

---

## Soru 4 — LTI Testi: $y[n]=n\,x[n]$ (15p)

> [!question] 📝 Soru metni (sınavda sorulan)
> Giriş-çıkış ilişkisi $y[n]=n\cdot x[n]$ olan bir sistem doğrusal zamanla değişmez (LTI) bir sistem midir? **Gösteriniz?** (15p)

> [!note]- Semboller
> - Doğrusallık (linearity): $T\{a x_1+b x_2\}=a\,T\{x_1\}+b\,T\{x_2\}$ (süperpozisyon)
> - Zamanla-değişmezlik (TI): girişi $n_0$ kaydır → çıkış da aynen $n_0$ kayar
> - Buradaki tehlike: katsayıda **bağımsız $n$** çarpanı var → genelde TI'yı bozar

> [!tip] 📘 Önce kavram — iki testi ayrı ayrı yap
> LTI = **Doğrusal** VE **Zamanla-değişmez**. İkisini ayrı kanıtla. Doğrusallık için iki girişin ağırlıklı toplamını koy. Zamanla-değişmezlik için "önce kaydır sonra sistemden geçir" ile "önce sistemden geçir sonra kaydır" sonuçlarını karşılaştır; eşit değillerse TI bozulur.

> [!abstract]- 📘 Sıfırdan: Doğrusallık, Zamanla-Değişmezlik ve LTI İspat Tarifi (konu anlatımı)
> **1. Sistem ve $T\{\cdot\}$ gösterimi.** Ayrık-zaman bir sistem, giriş dizisini $x[n]$ çıkış dizisine $y[n]$ dönüştüren bir kuraldır: $y[n]=T\{x[n]\}$. $T\{\cdot\}$ sembolü "bu girişi sistemin kuralından geçir" demek. Örn. bu soruda $T\{x[n]\}=n\,x[n]$.
>
> **2. LTI = Doğrusal (L) VE Zamanla-Değişmez (TI) — ikisi de ayrı kanıtlanır.** Biri sağlanıp diğeri sağlanmayabilir; "LTI değil" demek için tek birinin çökmesi yeter.
>
> - **Doğrusallık (süperpozisyon ilkesi):** sistem toplamayı ve ölçeklemeyi korumalı —
>   $$T\{a\,x_1[n]+b\,x_2[n]\} = a\,T\{x_1[n]\}+b\,T\{x_2[n]\}\quad\forall\,a,b,x_1,x_2$$
>   Bu tek koşul iki alt özelliği birden içerir: **katkılılık** ($a=b=1$: $T\{x_1+x_2\}=T\{x_1\}+T\{x_2\}$) ve **homojenlik/ölçeklenebilirlik** ($x_2=0$: $T\{a\,x_1\}=a\,T\{x_1\}$). Hızlı eleme testi: $a=0$ koy → $T\{0\}=0$ çıkmalı; çıkmıyorsa (sabit terim varsa) **kesin doğrusal değildir**.
>
> - **Zamanla-değişmezlik (TI):** girişi kaydırırsan çıkış da **şeklini bozmadan aynı miktarda** kaymalı —
>   $$x[n]\xrightarrow{T}y[n] \;\Rightarrow\; x[n-n_0]\xrightarrow{T}y[n-n_0]\quad\forall\,n_0$$
>   Yani sistemin davranışı *hangi zaman anında* uygulandığına bağlı olmamalı.
>
> **3. Genel ispat iskeleti (her soruda aynı adımlar):**
>
> > [!tip] Doğrusallık testi — 4 adım
> > 1. İki keyfi giriş seç: $x_1[n],x_2[n]$; çıkışlarını yaz: $y_1[n]=T\{x_1[n]\}$, $y_2[n]=T\{x_2[n]\}$.
> > 2. Bileşik (ağırlıklı toplam) giriş kur: $x_3[n]=a\,x_1[n]+b\,x_2[n]$ ($a,b$ keyfi skaler).
> > 3. Sistem kuralını $x_3$'e **doğrudan** uygula → $y_3[n]=T\{x_3[n]\}$'i hesapla.
> > 4. $y_3[n]$'i $a\,y_1[n]+b\,y_2[n]$ ile karşılaştır. Cebirsel olarak birebir eşitse → **doğrusal**. Bir çapraz terim, kare, mutlak değer ya da bağımsız sabit yüzünden eşitlik bozuluyorsa → **doğrusal değil**.
>
> > [!tip] Zamanla-değişmezlik testi — 3 adım
> > 1. Kaydırılmış giriş tanımla: $x_2[n]=x[n-n_0]$.
> > 2. **Yol A (önce kaydır → sonra sistemden geçir):** $x_2[n]$'i sistem kuralına sok, $y_2[n]=T\{x_2[n]\}$'i $n$ cinsinden yaz.
> > 3. **Yol B (önce sistemden geçir → sonra kaydır):** bilinen $y[n]=T\{x[n]\}$ ifadesinde $n\to n-n_0$ yaz, $y[n-n_0]$'ı bul.
> > Sonuç: $y_2[n]=y[n-n_0]$ **tüm** $n_0$ için sağlanıyorsa → **TI**; sağlanmıyorsa (genelde denklemde $n_0$ "yalnız"/eşleşmemiş kalır) → **TI değil**.
>
> **4. Hızlı tanı tablosu — hangi ifade hangi özelliği bozar?**
>
> | Sistem kuralı (örnek) | Doğrusal mı? | TI mi? | Neden |
> |---|---|---|---|
> | $y[n]=x[n-n_d]$ (sabit gecikme) | ✅ | ✅ | Gerçek LTI — toplama/ölçek korunur, kayma sabit ve tek tip |
> | $y[n]=n\,x[n]$ *(bu soru)* | ✅ | ❌ | Katsayı $n$ **zamana bağlı** → kaydırınca çarpan eski yerinde kalır, kaymıyor |
> | $y[n]=\cos(n)\,x[n]$, $y[n]=a^n x[n]$ | ✅ | ❌ | Aynı sebep: katsayıda açık/bağımsız $n$ var |
> | $y[n]=x^2[n]$, $\;y[n]=\lvert x[n]\rvert$ | ❌ | ✅ (genelde) | Süperpozisyonda çapraz terim çıkar: $(x_1{+}x_2)^2\neq x_1^2+x_2^2$ |
> | $y[n]=x[n]+5$ | ❌ | ✅ | $T\{0\}=5\neq0$ → homojenlik (ve dolayısıyla doğrusallık) çöker |
> | $y[n]=x[-n]$ (zaman ters çevirme) | ✅ | ❌ | Kaydırma kaydırırken yön de tersine döner: $x[n-n_0]\to x[-n-n_0]\neq x[-n+n_0]$ |
> | $y[n]=x[2n]$ (downsampling) | ✅ | ❌ | Yalnız **çift** $n_0$ kaymalarında değişmez kalır, genel/tek $n_0$'da bozulur |
>
> **5. Bu soruya uygulanışı:** $y[n]=n\,x[n]$ → tablodaki 2. satır, "doğrusal ama TI değil" klasiği. Aşağıdaki **① Doğrusallık** ve **② Zamanla-değişmezlik** adımları, yukarıdaki 4+3 adımlık tarifi harfiyen bu soruya uyguluyor — karşılaştıra karşılaştıra oku.

**Çözüm.**

**① Doğrusallık.** Girişler $x_1,x_2$, çıkışlar $y_i[n]=n\,x_i[n]$. Bileşik giriş $x_3[n]=a\,x_1[n]+b\,x_2[n]$:
$$y_3[n]=n\,x_3[n]=n\big(a\,x_1[n]+b\,x_2[n]\big)=a\,(n\,x_1[n])+b\,(n\,x_2[n])=a\,y_1[n]+b\,y_2[n]\;\checkmark$$
→ **Doğrusal.**

**② Zamanla-değişmezlik.** Kaydırılmış giriş $x_2[n]=x[n-n_0]$.
- Sistemden geçir: $\;y_2[n]=n\,x_2[n]=n\,x[n-n_0]$
- Çıkışı kaydır: $\;y[n-n_0]=(n-n_0)\,x[n-n_0]$

$$n\,x[n-n_0]\;\neq\;(n-n_0)\,x[n-n_0]\quad(n_0\neq0\text{ için})$$
→ **Zamanla değişir** (TI değil). Sebep: katsayıdaki **$n$ çarpanı** sabit değil, indekse bağlı.

$$\boxed{\text{Doğrusal ✓, Zamanla-değişmez ✗ } \Rightarrow \text{ LTI DEĞİL (doğrusal ama zamanla değişen sistem)}}$$

> [!success] 🎯 Çıkarım
> Katsayıda yalın $n$ (veya $\cos n$, $a^n$ gibi $n$'ye açık bağımlılık) görürsen → **zamanla değişir**. $x^2[n]$, $|x[n]|$, sabit ekleme görürsen → **doğrusal değil**. $y[n]=n\,x[n]$ klasik "doğrusal ama TI değil" tuzağı.

---

## Soru 5 — Hareketli Ortalama (MA - Moving Average) Filtresi (15p)

> [!question] 📝 Soru metni (sınavda sorulan)
> $y[n]=\dfrac{1}{N}\displaystyle\sum_{k=0}^{N-1}x[n-k]$ giriş-çıkış ilişkisi verilen bir LTI sistemin **hangi işlevi gördüğünü** yazınız? $N=3$ için $x[n]=\left(\dfrac{1}{3}\right)^{n}u[n]$ girişine sistemin **çıkışını bulunuz?** (15p)

> [!note]- Semboller
> - $\frac1N\sum_{k=0}^{N-1}x[n-k]$: son $N$ örneğin **ortalaması** → hareketli ortalama
> - Dürtü yanıtı $h[n]=\frac1N\{1,1,\dots,1\}$ (uzunluk $N$ dikdörtgen) → **FIR alçak geçiren**
> - Çıkış: $y=x*h$ veya doğrudan tanımı uygula

> [!tip] 📘 Önce kavram — MA = yumuşatma = alçak geçiren
> Komşu örnekleri ortalamak **gürültüyü/ani değişimleri** bastırır, yavaş (düşük frekanslı) bileşeni geçirir. Bu yüzden MA bir **alçak geçiren (düzleştirme/smoothing) filtresidir**. Dürtü yanıtı uzunluk-$N$ dikdörtgendir; $N$ büyüdükçe daha çok yumuşatır (kesim frekansı düşer — bkz. [[06 Final Sınav Soruları (Çözümlü)|Final S4b]]).

**Çözüm.**

**İşlev:** Sistem bir **hareketli ortalama (alçak geçiren / düzleştirme) filtresidir**; $h[n]=\tfrac1N(u[n]-u[n-N])$.

**$N=3$ için:** $y[n]=\tfrac13\big(x[n]+x[n-1]+x[n-2]\big)$, $\;x[n]=\left(\tfrac13\right)^n u[n]$.

**Başlangıç (geçici rejim):**
- $y[0]=\tfrac13\big(x[0]\big)=\tfrac13(1)=\dfrac{1}{3}$
- $y[1]=\tfrac13\big(x[1]+x[0]\big)=\tfrac13\big(\tfrac13+1\big)=\dfrac{4}{9}$
- $y[2]=\tfrac13\big(x[2]+x[1]+x[0]\big)=\tfrac13\big(\tfrac19+\tfrac13+1\big)=\tfrac13\cdot\tfrac{13}{9}=\dfrac{13}{27}$

**$n\ge2$ kalıcı kalıp:** üç terim de tam dolu:
$$y[n]=\tfrac13\Big[\big(\tfrac13\big)^n+\big(\tfrac13\big)^{n-1}+\big(\tfrac13\big)^{n-2}\Big]=\tfrac13\big(\tfrac13\big)^{n-2}\underbrace{\Big(\tfrac19+\tfrac13+1\Big)}_{=13/9}=\frac{13}{27}\left(\tfrac13\right)^{n-2}$$

$$\boxed{y[n]=\begin{cases}\dfrac13, & n=0\\[4pt]\dfrac49, & n=1\\[4pt]\dfrac{13}{27}\left(\dfrac13\right)^{n-2}, & n\ge2\\[4pt]0,& n<0\end{cases}}$$

![[ssi-v-s5-ma.png]]

> [!note]- 🐍 Python kaynağı
> `_assets/scripts/ssi-v-s5-ma.py` — gri ×: giriş $x[n]$, mor: çıkış $y[n]$ (yumuşatılmış, tepe gecikmiş).

> [!success] 🎯 Çıkarım
> İlk $N-1$ örnek **geçici rejimdir** (pencere henüz dolmamış); pencere dolunca sinyal kendi sönme hızıyla $\left(\tfrac13\right)^n$ devam eder. MA çıkışı girişten daha yumuşak ve tepe biraz gecikmelidir.

---

## Soru 6 — DTFT'nin $2\pi$ Periyodikliği (İspat) (15p)

> [!question] 📝 Soru metni (sınavda sorulan)
> Ayrık-zamanlı Fourier dönüşümünün $2\pi$ ile **periyodik** olduğunu **ispatlayınız.** (15p)

> [!note]- Semboller
> - $X(e^{j\omega})=\sum_n x[n]e^{-j\omega n}$: DTFT tanımı
> - $e^{-j2\pi n}=1$ (her **tam sayı** $n$ için) → ispatın anahtarı
> - "Periyodik $2\pi$" demek: $X(e^{j(\omega+2\pi)})=X(e^{j\omega})$

> [!tip] 📘 Önce kavram — neden $2\pi$?
> CT'de farklı frekanslar hep farklıdır, ama DT'de zaman indeksi $n$ **tam sayıdır**; $e^{-j2\pi n}=1$ olduğundan $\omega$'yı $2\pi$ ötelemek hiçbir örnek değerini değiştirmez. Bu yüzden DT frekans ekseni $2\pi$'de kendini tekrar eder — tüm DT spektrumlar doğal olarak $2\pi$ periyodiktir.

**İspat.**

$$X(e^{j(\omega+2\pi)})=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j(\omega+2\pi)n}=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}\underbrace{e^{-j2\pi n}}_{=\,1}$$

$n\in\mathbb{Z}$ için $e^{-j2\pi n}=\cos(2\pi n)-j\sin(2\pi n)=1-0=1$. Dolayısıyla

$$X(e^{j(\omega+2\pi)})=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}=X(e^{j\omega})\qquad\blacksquare$$

> [!success] 🎯 Çıkarım
> İspatın tamamı tek gerçeğe dayanır: **$e^{-j2\pi n}=1$, çünkü $n$ tam sayı.** Bu yüzden DTFT'yi yalnız bir $2\pi$'lik aralıkta (örn. $-\pi\le\omega<\pi$) çizmek yeter.

---

## Soru 7 — Frekans Yanıtı → Transfer Fonksiyonu (15p)

> [!question] 📝 Soru metni (sınavda sorulan)
> Frekans yanıtı $H(e^{j\omega})=\dfrac{1-0.2e^{-j\omega}+0.4e^{-2j\omega}}{1-0.3e^{-j\omega}}$ şeklinde verilen bir sistemin **transfer fonksiyonunu** bulunuz? (15p)

> [!note]- Semboller
> - $H(e^{j\omega})$: frekans yanıtı (birim çember üstündeki $H$)
> - $H(z)$: transfer fonksiyonu (tüm $z$-düzlemi); $H(e^{j\omega})=H(z)\big|_{z=e^{j\omega}}$
> - Köprü: $e^{-j\omega}\;\longleftrightarrow\;z^{-1}$ (birim gecikme)

> [!tip] 📘 Önce kavram — $e^{-j\omega}\to z^{-1}$
> Frekans yanıtı, transfer fonksiyonunun **birim çember üzerine** ($z=e^{j\omega}$) sınırlandırılmış halidir. Tersine gitmek için her $e^{-j\omega}$ yerine $z^{-1}$ yazmak yeter — başka işlem yok. Çünkü her $e^{-j\omega k}$ terimi $k$ örneklik bir gecikmeyi, yani $z^{-k}$'yi temsil eder.

**Çözüm.**

$e^{-j\omega}\to z^{-1}$ koy:

$$\boxed{H(z)=\frac{1-0.2\,z^{-1}+0.4\,z^{-2}}{1-0.3\,z^{-1}}}$$

**Karşılık gelen fark denklemi** (kontrol için, $H=Y/X$'ten çapraz çarpım):
$$y[n]-0.3\,y[n-1]=x[n]-0.2\,x[n-1]+0.4\,x[n-2]$$

Payda $z^{-1}$ içerdiği için (geri besleme var) → **IIR** sistem; tek kutup $z=0.3$ → $|0.3|<1$ → kararlı.

> [!success] 🎯 Çıkarım
> $H(e^{j\omega})\leftrightarrow H(z)$ dönüşümü tek kuraldır: $e^{-j\omega}\equiv z^{-1}$. Paydada $z^{-1}$ varsa IIR (geri besleme); yoksa FIR. Kutbu kontrol et: $|z_{\text{kutup}}|<1$ → kararlı.

---

## Soru Tipini Tanıma Rehberi (Vize)

| Görünce...                 | Yöntem                   | Anahtar formül/kural                                                         |
| -------------------------- | ------------------------ | ---------------------------------------------------------------------------- |
| "çiz + enerji" sönen üstel | geometrik seri           | $\sum_{0}^{\infty}r^n=\tfrac1{1-r}$, kare → taban karelenir                  |
| $x[Mn]$ / $x[n/M]$         | seyreltme/genişletme     | frekansı $\times M$, $2\pi$'ye katla, periyodu yeniden bul                   |
| seri/paralel blok          | $h$ birleştir            | seri $\to *$, paralel $\to +$                                                |
| "$h$ üzerinden özellik"    | tek tabloya bak          | $n<0$'da değer? (nedensellik) · $\sum<\infty$? (kararlılık)                  |
| "LTI midir?"               | 2 ayrı test              | süperpozisyon (doğrusallık) + kaydır-karşılaştır (TI); $n\cdot x$ → TI değil |
| $\frac1N\sum x[n-k]$       | MA filtresi              | alçak geçiren; $y=x*h$, ilk $N-1$ örnek geçici rejim                         |
| "DTFT $2\pi$ periyodik"    | tanıma $\omega+2\pi$ koy | $e^{-j2\pi n}=1$                                                             |
| $H(e^{j\omega})$ verili    | $e^{-j\omega}\to z^{-1}$ | IIR/FIR ve kutup→kararlılık                                                  |

---

## Bağlantılı Notlar

- [[06 Final Sınav Soruları (Çözümlü)]]
- [[../Konu Anlatımları/01 Ayrık Zaman Sinyalleri ve Örnekleme]]
- [[../Konu Anlatımları/02 Z-Dönüşümü]]
- [[02 Z-Dönüşümü Örnekleri]]
