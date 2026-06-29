---
tags: [mst, vize, sınav-soruları, resmi-sınav, çözümlü, sismograf, lagrange, dişli, dc-motor, durum-uzayı]
---

# 09 — MST&B Resmi Vize Sınavı (Cevap Anahtarlı)

← [[MST Ana Sayfa]] | İlgili: [[08 Vize Soruları ve Hoca Örnekleri]] · [[01 Mekanik Sistemler Örnekleri]] · [[03 Durum Uzayı Örnekleri]]

> Kaynak: **Resmi Ara Sınav + puanlı cevap anahtarı** (`Vize soru cevap.pdf`, 7 sf., MSÜ Hava Harp Okulu). Bu, derslerin **gerçek vize sınavı** ve resmi çözüm anahtarıdır — en otoriter çalışma kaynağı. Tüm sonuçlar bağımsız olarak yeniden doğrulandı; el yazısı taramadaki birkaç özensiz ara satır temiz biçimde yeniden türetildi.

> [!tip] Hoca örnekleriyle ilişki
> Bu resmi sınav, [[08 Vize Soruları ve Hoca Örnekleri]] dosyasındaki Quiz ve Hoca Örnekleriyle **aynı konuları ve yöntemleri** işler (taban-tahrikli kütle-yay-sönüm, iki-kütle Lagrange+Newton, dişli+DC motor, RC durum-uzayı) ama **somut sorular ve sayılar farklıdır**. Önce burayı (gerçek sınav formatı), sonra `08`'i (yöntem deposu) çalış.

> [!sinav] Sınav Künyesi
> Millî Savunma Üniversitesi · Hava Harp Okulu · 2025–2026 EÖY 1. Yarıyıl · 3. Sınıf Elektronik Mühendisliği · **Mühendislik Sistem Tasarımı ve Benzetimi — Ara Sınav** · 120 dk · 4 soru · hesap makinesi serbest. Aşağıdaki çözümler resmi cevap anahtarına (kırmızı kalem puanlamasına) birebir uygundur.

---

## Soru 1 — Sismograf (Taban Tahrikli Kütle-Yay-Sönüm) · 25p

**Soru:** Bir sismograf düzeneği, gövdesinin eylemsizlik boşluğuna göre yer değiştirmesini gösterir; deprem süresince yerin yer değiştirmesini ölçmek için kullanılır.
- $x_i$ = gövdenin eylemsizlik uzayında yer değiştirmesi
- $x_0$ = $m$ kütlesinin eylemsizlik uzayında yer değiştirmesi
- $y=x_0-x_i$ = $m$ kütlesinin gövdeye göre yer değiştirmesi

**(a)** Sistemin transfer fonksiyonu $\dfrac{Y(s)}{X_i(s)}$'i bulun. (15p)
**(b)** $m=2\,\text{kg}$, $f=6\,\text{kN/m/s}$ (sönüm), $k=4\,\text{kN/m}$ ve gövde yer değiştirmesi $x_i=(1-e^{-3t})u(t)$ olan bir deprem için $m$ kütlesinin yer değiştirmesi $x_0(t)$ (eşdeğer olarak $y(t)$) zaman domeninde nasıl olur? (10p)

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={coil, aspect=0.5, segment length=2.4mm, amplitude=1.7mm}}]
% Gövde (çerçeve)
\draw[thick] (-2,0) rectangle (2,4);
% Kütle m içeride
\draw[thick, fill=gray!15] (-0.8,2.0) rectangle (0.8,2.9); \node at (0,2.45) {$m$};
% Yay (sol-alt) ve sönüm (sağ-alt) kütleyi çerçeve tabanına bağlar
\draw[spring] (-0.5,2.0) -- (-0.5,0.4); \node at (-0.95,1.2) {$k$};
\draw[thick] (0.5,2.0)--(0.5,1.35); \draw[thick](0.28,1.35)rectangle(0.72,0.85);
\draw[thick](0.5,0.85)--(0.5,0.4); \node at (0.98,1.2) {$f$};
% Yer hattı (hatch) tabanın altında
\draw[thick] (-2,0)--(2,0);
\foreach \x in {-1.8,-1.4,...,1.8}{\draw (\x,0)--(\x-0.25,-0.3);}
% x_i (gövde) ve x_0 (kütle) okları
\draw[->] (2.0,3.3)--(2.9,3.3) node[right]{$x_i$ (gövde)};
\draw[->] (0,2.9)--(0,3.5) node[above]{$x_0$};
\end{tikzpicture}
\end{document}
```

> [!note]- Semboller
> - $x_i,x_0$: gövdenin ve $m$ kütlesinin **mutlak** (eylemsizlik uzayındaki) yer değiştirmeleri (m)
> - $y=x_0-x_i$: kütlenin **gövdeye göre** (bağıl) yer değiştirmesi — sismografın gerçekte okuduğu büyüklük (m)
> - $m$: sarkaç kütlesi (kg); $k$: yay (N/m); $f$: viskoz sönüm (N·s/m)
> - Yay ve sönüm kuvvetleri **bağıl** harekete bağlıdır: $k(x_0-x_i)$, $f\frac{d}{dt}(x_0-x_i)$ → bu yüzden $-ms^2$ payı çıkar (taban tahriki)

**Çözüm:**

**(a)** Kütleye Newton 2. yasası — kütlenin mutlak ivmesi $\ddot x_0$, yay/sönüm bağıl yer değiştirmeye etki eder:
$$m\ddot x_0 + f(\dot x_0-\dot x_i) + k(x_0-x_i)=0$$
$y=x_0-x_i\Rightarrow x_0=y+x_i$ koy:
$$m(\ddot y+\ddot x_i)+f\dot y+ky=0 \;\Rightarrow\; m\ddot y+f\dot y+ky=-m\ddot x_i$$
Laplace (sıfır başlangıç koşulu):
$$Y(s)(ms^2+fs+k)=-ms^2X_i(s)$$
$$\boxed{\dfrac{Y(s)}{X_i(s)}=\dfrac{-ms^2}{ms^2+fs+k}=\dfrac{-s^2}{s^2+\frac{f}{m}s+\frac{k}{m}}}$$

**(b)** Değerleri yerleştir ($\frac{f}{m}=\frac{6}{2}=3$, $\frac{k}{m}=\frac{4}{2}=2$):
$$\dfrac{Y(s)}{X_i(s)}=\dfrac{-s^2}{s^2+3s+2}=\dfrac{-s^2}{(s+1)(s+2)}$$

> [!info]- **Adım 1 — Neden (s+1)(s+2)?**
> Paydayı çarpanlara ayır: $s^2+3s+2=0$ denkleminin kökleri $s=\frac{-3\pm\sqrt{9-8}}{2}=\frac{-3\pm1}{2}$, yani $s=-1$ ve $s=-2$.
> Bu yüzden $s^2+3s+2=(s+1)(s+2)$.

Giriş $x_i=(1-e^{-3t})u(t)$ → $X_i(s)=\dfrac1s-\dfrac1{s+3}=\dfrac{3}{s(s+3)}$

> [!info]- **Adım 2 — Girişin Laplace dönüşümü nasıl yapıldı?**
> Standart çiftler: $\mathcal{L}\{u(t)\}=\frac{1}{s}$ ve $\mathcal{L}\{e^{-at}u(t)\}=\frac{1}{s+a}$
>
> Yani $\mathcal{L}\{1\cdot u(t)\}=\frac{1}{s}$ ve $\mathcal{L}\{e^{-3t}u(t)\}=\frac{1}{s+3}$
>
> Ortak paydaya getirme:
> $$\frac{1}{s}-\frac{1}{s+3}=\frac{(s+3)-s}{s(s+3)}=\frac{3}{s(s+3)}$$

O hâlde:
$$Y(s)=\underbrace{\frac{-s^2}{(s+1)(s+2)}}_{\text{TF}}\cdot\underbrace{\frac{3}{s(s+3)}}_{X_i(s)}=\frac{-3s^2}{s\cdot(s+1)(s+2)(s+3)}$$

> [!info]- **Adım 3 — $s$ sadeleşmesi**
> Paydada $s$ var, payde $s^2$; bir tane sadeleşir:
> $$\frac{-3s^{\cancel{2}}}{\cancel{s}\cdot(s+1)(s+2)(s+3)}=\frac{-3s}{(s+1)(s+2)(s+3)}$$

$$Y(s)=\frac{-3s}{(s+1)(s+2)(s+3)}=\frac{A}{s+1}+\frac{B}{s+2}+\frac{C}{s+3}$$

> [!info]- **Adım 4 — Kısmi kesir açılımı neden böyle?**
> Pay 1. dereceden ($-3s$), payda 3. dereceden → gerçek kesir. Payda üç ayrı reel kök içeriyor ($(s+1),(s+2),(s+3)$), bu yüzden her köke karşılık bir sabit terim yazılır.

Kalıntılar (örtme/cover-up yöntemi — o kutbu $(s+k)$ ile çarp, sonra $s=-k$ koy):

$$A=\left.\frac{-3s}{(s+2)(s+3)}\right|_{s=-1}=\frac{-3\cdot(-1)}{(-1+2)(-1+3)}=\frac{3}{(1)(2)}=\boxed{\tfrac32}$$

$$B=\left.\frac{-3s}{(s+1)(s+3)}\right|_{s=-2}=\frac{-3\cdot(-2)}{(-2+1)(-2+3)}=\frac{6}{(-1)(1)}=\boxed{-6}$$

$$C=\left.\frac{-3s}{(s+1)(s+2)}\right|_{s=-3}=\frac{-3\cdot(-3)}{(-3+1)(-3+2)}=\frac{9}{(-2)(-1)}=\boxed{\tfrac92=4{,}5}$$

> [!info]- **Adım 5 — Kalıntı (cover-up) yöntemi nasıl çalışır?**
> $A$'yı bulmak için: $Y(s)\cdot(s+1)$ çarp → $\frac{-3s}{(s+2)(s+3)}$ kalır, $s=-1$ koy.
> $B$'yi bulmak için: $Y(s)\cdot(s+2)$ çarp → $\frac{-3s}{(s+1)(s+3)}$ kalır, $s=-2$ koy.
> $C$ için de aynı şekilde $s=-3$ koymak yeterli.
>
> Mantık: $s=-1$ koyunca $B$ ve $C$'nin terimleri $\frac{B}{0+\text{bir şey}}+\frac{C}{0+\text{bir şey}}$ olarak sıfırlanmaz ama $(s+1)$ ile çarpınca $A$ yalnız kalır.

Ters Laplace ($\frac{K}{s+a}\leftrightarrow Ke^{-at}u(t)$):
$$\boxed{y(t)=x_0(t)=\Big(\tfrac32 e^{-t}-6e^{-2t}+4{,}5\,e^{-3t}\Big)u(t)}$$

> [!info]- **Adım 6 — Ters Laplace nasıl alındı?**
> Her terim standart çift: $\mathcal{L}^{-1}\!\left\{\frac{K}{s+a}\right\}=K\,e^{-at}u(t)$
>
> | $s$-domenindeki terim | Zaman domenindeki karşılığı |
> |---|---|
> | $\dfrac{3/2}{s+1}$ | $\tfrac{3}{2}e^{-t}u(t)$ |
> | $\dfrac{-6}{s+2}$ | $-6\,e^{-2t}u(t)$ |
> | $\dfrac{4{,}5}{s+3}$ | $4{,}5\,e^{-3t}u(t)$ |
>
> Hepsini topla → sonuç kutu içindeki ifade.

---

## Soru 2 — İki Kütleli Öteleme Sistemi: $X_1(s)/F(s)$ · 25p

**Soru:** Şekildeki sistemde $m_1$ kütlesine bağlı transfer fonksiyonunu **(a) Lagrange yöntemiyle (10p)**, **(b) Newton 2. yasasıyla (15p)** bulun. Veriler:
$$K_1=4\,\tfrac{\text N}{\text m},\;K_2=5\,\tfrac{\text N}{\text m},\;M_1=1\,\text{kg},\;M_2=2\,\text{kg},\;f_{v1}=3,\;f_{v2}=3,\;f_{v3}=2\;\tfrac{\text{N·s}}{\text m}$$
Kuvvet $f(t)$ $M_2$'ye, $K_1$ ve $f_{v1}$ duvardan $M_1$'e, $K_2$ ve $f_{v2}$ iki kütle arasında, $f_{v3}$ $M_2$'den duvara bağlı.

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing, arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.2mm]}, font=\small,
  spring/.style={decorate, decoration={zigzag, pre length=1.5mm, post length=1.5mm, segment length=2mm, amplitude=1.6mm}}]
% Sol duvar
\draw[very thick] (0,-1)--(0,1.4);
\foreach \y in {-0.8,-0.4,...,1.2}{\draw (0,\y)--(-0.22,\y+0.18);}
% K1 (üst) ve fv1 (alt) duvardan M1'e
\draw[spring] (0,0.7)--(2.2,0.7); \node at (1.1,1.1){$K_1$};
\draw[thick](0,-0.5)--(0.9,-0.5);\draw[thick](0.9,-0.7)rectangle(1.4,-0.3);\draw[thick](1.4,-0.5)--(2.2,-0.5);
\node at (1.1,-0.95){$f_{v1}$};
% M1
\draw[thick,fill=gray!12] (2.2,-0.8) rectangle (3.4,0.9); \node at (2.8,0.05){$M_1$};
\draw[->](2.8,1.15)--(3.5,1.15) node[right]{$x_1$};
% K2 (üst) ve fv2 (alt) M1->M2
\draw[spring] (3.4,0.7)--(5.6,0.7); \node at (4.5,1.1){$K_2$};
\draw[thick](3.4,-0.5)--(4.3,-0.5);\draw[thick](4.3,-0.7)rectangle(4.8,-0.3);\draw[thick](4.8,-0.5)--(5.6,-0.5);
\node at (4.5,-0.95){$f_{v2}$};
% M2
\draw[thick,fill=gray!12] (5.6,-0.8) rectangle (6.8,0.9); \node at (6.2,0.05){$M_2$};
\draw[->](6.2,1.15)--(6.9,1.15) node[right]{$x_2$};
\draw[->,thick](6.8,0.05)--(7.9,0.05) node[right]{$f(t)$};
% fv3 M2->sağ duvar
\draw[thick](6.8,-0.5)--(7.7,-0.5);\draw[thick](7.7,-0.7)rectangle(8.2,-0.3);\draw[thick](8.2,-0.5)--(8.8,-0.5);
\node at (7.75,-0.95){$f_{v3}$};
\draw[very thick] (8.8,-1)--(8.8,0.0);
\foreach \y in {-0.8,-0.4,...,-0.0}{\draw (8.8,\y)--(9.02,\y+0.18);}
\end{tikzpicture}
\end{document}
```

> [!note]- Semboller
> - $x_1,x_2$: $M_1,M_2$ kütlelerinin konumları (m); $f(t)$: $M_2$'ye uygulanan kuvvet (N)
> - $K_1,K_2$: yay sabitleri (N/m); $f_{v1},f_{v2},f_{v3}$: sönüm katsayıları (N·s/m)
> - **Lagrange:** $KE=\frac12\sum M\dot x^2$, $PE=\frac12\sum K(\Delta x)^2$, sönüm fonk. $D=\frac12\sum f_v(\Delta\dot x)^2$
> - Denklem: $\frac{d}{dt}\frac{\partial KE}{\partial \dot x_i}-\frac{\partial KE}{\partial x_i}+\frac{\partial PE}{\partial x_i}+\frac{\partial D}{\partial \dot x_i}=F_i$
> - İki kütle arasındaki $K_2,f_{v2}$ her iki denklemde **fark** $(x_2-x_1)$ olarak → çapraz $-(3s+5)$ terimi

**Çözüm:**

**(a) Lagrange.**

> [!info]- **Lagrange formülü nedir, ne anlama gelir?**
> Klasik Lagrange hareket denklemi her koordinat $x_i$ için şöyle yazılır:
> $$\frac{d}{dt}\!\left(\frac{\partial KE}{\partial \dot x_i}\right)-\frac{\partial KE}{\partial x_i}+\frac{\partial PE}{\partial x_i}+\frac{\partial D}{\partial \dot x_i}=F_i$$
>
> | Terim | Fiziksel anlamı |
> |---|---|
> | $\frac{d}{dt}\!\left(\frac{\partial KE}{\partial \dot x_i}\right)$ | $x_i$'ye bağlı **atalet kuvveti** ($M\ddot x$'e eşdeğer) |
> | $-\frac{\partial KE}{\partial x_i}$ | KE konuma bağlıysa katkı (öteleme sistemlerde **genellikle sıfır**) |
> | $\frac{\partial PE}{\partial x_i}$ | $x_i$'nin uzadığı yay kuvvetleri (geri yükleyen) |
> | $\frac{\partial D}{\partial \dot x_i}$ | $\dot x_i$'ye bağlı sönüm kuvvetleri |
> | $F_i$ | Dışarıdan $x_i$ yönünde uygulanan **genelleştirilmiş kuvvet** |
>
> **$F_i = 0$ ne demek?** O koordinata dışarıdan hiçbir kuvvet uygulanmıyor demek. Burada $f(t)$ yalnızca $M_2$'ye uygulandığından $F_1=0$, $F_2=f(t)$.

**Enerji ve sönüm fonksiyonlarını yaz** (sistemdeki tüm elemanları tara):

$$KE=\tfrac12 M_1\dot x_1^2+\tfrac12 M_2\dot x_2^2$$
$$PE=\tfrac12 K_1x_1^2+\tfrac12 K_2(x_2-x_1)^2$$
$$D=\tfrac12 f_{v1}\dot x_1^2+\tfrac12 f_{v2}(\dot x_2-\dot x_1)^2+\tfrac12 f_{v3}\dot x_2^2$$

> [!info]- **Neden $(x_2-x_1)$ ve $(\dot x_2-\dot x_1)$ yazıyoruz?**
> $K_2$ ve $f_{v2}$ **iki kütle arasında**. Yay ne kadar uzuyor? İki ucun farkı kadar: $(x_2-x_1)$. Sönüm de hız farkına bakıyor: $(\dot x_2-\dot x_1)$. Duvarla bağlantılı elemanlarda ise duvar sabit ($x=0$) olduğu için sadece $x_1$ ya da $\dot x_1$ yazılır.

---

**$x_1$ koordinatına Lagrange formülünü uygula** ($F_1=0$, $M_1$'e dışarıdan kuvvet yok):

*Terim 1 — kinetik enerji türevi:*
$$\frac{\partial KE}{\partial \dot x_1}=M_1\dot x_1=1\cdot\dot x_1 \;\xrightarrow{\frac{d}{dt}}\; M_1\ddot x_1=\ddot x_1$$

*Terim 2 — $-\partial KE/\partial x_1$:*
$$KE\text{ içinde } x_1 \text{ yok (sadece } \dot x_1\text{ var)} \;\Rightarrow\; \frac{\partial KE}{\partial x_1}=0$$

*Terim 3 — potansiyel enerji türevi:*
$$PE=\tfrac12 K_1 x_1^2+\tfrac12 K_2(x_2-x_1)^2$$
$$\frac{\partial PE}{\partial x_1}=K_1x_1+K_2(x_2-x_1)\cdot(-1)=K_1x_1-K_2x_2+K_2x_1=(K_1+K_2)x_1-K_2x_2$$
$$=(4+5)x_1-5x_2=9x_1-5x_2$$

*Terim 4 — sönüm fonksiyonu türevi:*
$$D=\tfrac12 f_{v1}\dot x_1^2+\tfrac12 f_{v2}(\dot x_2-\dot x_1)^2+\ldots$$
$$\frac{\partial D}{\partial \dot x_1}=f_{v1}\dot x_1+f_{v2}(\dot x_2-\dot x_1)\cdot(-1)=f_{v1}\dot x_1-f_{v2}\dot x_2+f_{v2}\dot x_1=(f_{v1}+f_{v2})\dot x_1-f_{v2}\dot x_2$$
$$=(3+3)\dot x_1-3\dot x_2=6\dot x_1-3\dot x_2$$

*Hepsini $F_1=0$'a eşitle:*
$$\underbrace{\ddot x_1}_{\text{atalet}}+\underbrace{(9x_1-5x_2)}_{\text{yaylar}}+\underbrace{(6\dot x_1-3\dot x_2)}_{\text{sönüm}}=0$$
$$\boxed{\ddot x_1+6\dot x_1+9x_1-3\dot x_2-5x_2=0}$$

Laplace al ($\dot x\to sX$, $\ddot x\to s^2X$, sıfır başlangıç):
$$s^2X_1+6sX_1+9X_1-3sX_2-5X_2=0\;\Rightarrow\; \boxed{X_1(s^2+6s+9)-X_2(3s+5)=0}$$

---

**$x_2$ koordinatına Lagrange formülünü uygula** ($F_2=f(t)$, kuvvet $M_2$'ye uygulanıyor):

*Terim 1:*
$$\frac{d}{dt}\!\left(\frac{\partial KE}{\partial \dot x_2}\right)=M_2\ddot x_2=2\ddot x_2$$

*Terim 2:* $\partial KE/\partial x_2=0$ (yine sadece $\dot x_2$ var)

*Terim 3 — $\partial PE/\partial x_2$:*
$$\frac{\partial PE}{\partial x_2}=K_2(x_2-x_1)\cdot(+1)=K_2x_2-K_2x_1=5x_2-5x_1$$

*Terim 4 — $\partial D/\partial \dot x_2$:*
$$\frac{\partial D}{\partial \dot x_2}=f_{v2}(\dot x_2-\dot x_1)\cdot(+1)+f_{v3}\dot x_2=(f_{v2}+f_{v3})\dot x_2-f_{v2}\dot x_1=(3+2)\dot x_2-3\dot x_1=5\dot x_2-3\dot x_1$$

*Hepsini $F_2=f(t)$'ye eşitle:*
$$\underbrace{2\ddot x_2}_{\text{atalet}}+\underbrace{(5x_2-5x_1)}_{\text{yaylar}}+\underbrace{(5\dot x_2-3\dot x_1)}_{\text{sönüm}}=f(t)$$
$$\boxed{2\ddot x_2+(5\dot x_2-3\dot x_1)+(5x_2-5x_1)=f(t)}$$

Laplace al:
$$2s^2X_2+5sX_2+5X_2-3sX_1-5X_1=F(s)\;\Rightarrow\;\boxed{-X_1(3s+5)+X_2(2s^2+5s+5)=F(s)}$$

> [!info]- **$X_1/F(s)$ neden isteniyor — iki denklemde iki bilinmeyenden nasıl çıkarılıyor?**
> İki denklem var, iki bilinmeyen ($X_1,X_2$). "Giriş" $F(s)$, "çıkış" $X_1(s)$. $X_2$'yi elimine edip $X_1/F$ oranını bulmamız lazım.
> Bunu Cramer kuralıyla yapıyoruz (matris yöntemi, aşağıda).

**(b) Newton 2. yasası.** Her kütleye serbest cisim diyagramı — $M_1$'e etkiyen kuvvetler (duvar yay/sönüm + arabağ yay/sönüm) ve $M_2$'ye etkiyenler aynı denklemleri verir (yöntem farklı, sonuç özdeş):
$$M_1\ddot x_1+(f_{v1}+f_{v2})\dot x_1+(K_1+K_2)x_1-f_{v2}\dot x_2-K_2x_2=0$$
$$M_2\ddot x_2+(f_{v2}+f_{v3})\dot x_2+K_2x_2-f_{v2}\dot x_1-K_2x_1=f(t)$$

**Matris formu ve determinant:**

İki Laplace denklemini matrise yaz — $X_1$ ve $X_2$ bilinmeyenlerin katsayıları sol tarafa:
$$\begin{bmatrix}s^2+6s+9 & -(3s+5)\\ -(3s+5) & 2s^2+5s+5\end{bmatrix}\begin{bmatrix}X_1\\X_2\end{bmatrix}=\begin{bmatrix}0\\F(s)\end{bmatrix}$$

> [!info]- **Neden sağ taraf $[0,\; F(s)]^T$?**
> 1. denklem (x₁ için): sağ taraf $F_1=0$ → matrisin sağ tarafına $0$
> 2. denklem (x₂ için): sağ taraf $F_2=f(t)$ → Laplace'ı $F(s)$
> $X_1$ ve $X_2$ bilinmeyen; $F(s)$ giriş (bilinen). Transfer fonksiyonu = çıkış/giriş = $X_1/F$.

Ana determinant $\Delta$ (2×2 matrisin determinantı = çapraz çarpım farkı):
$$\Delta=(s^2+6s+9)(2s^2+5s+5)-(-(3s+5))(-(3s+5))$$
$$=(s^2+6s+9)(2s^2+5s+5)-(3s+5)^2 = 2s^4+17s^3+44s^2+45s+20$$

**Cramer ile $X_1$** — 1. sütunu sağ tarafla ($[0,F]^T$) değiştir, yeni determinantı $\Delta$'ya böl:
$$X_1=\frac{1}{\Delta}\det\begin{bmatrix}0 & -(3s+5)\\ F & 2s^2+5s+5\end{bmatrix}=\frac{(3s+5)F(s)}{\Delta}$$
$$\boxed{\dfrac{X_1(s)}{F(s)}=\dfrac{3s+5}{2s^4+17s^3+44s^2+45s+20}}$$
(Bonus — cevap anahtarında: $\dfrac{X_2(s)}{F(s)}=\dfrac{s^2+6s+9}{2s^4+17s^3+44s^2+45s+20}$.)

---

## Soru 3 — İki Kademeli Dişli + DC Motor: Yük Açısı · 25p

**Soru:** Verilen motor sisteminin transfer fonksiyonunu bulun. Motorun tork-hız grafiği $100\,\text V$ giriş voltajı altında $T_m=-8\omega_m+200$ denklemiyle çizilmiştir. $e_a(t)=20\delta(t)\,\text V$ olursa $J_L$ yükünün yer değiştirmesi zaman domeninde **kaç radyan** olur?

Veriler: $J_a=1\,\text{kg·m}^2$, $D_a=5\,\tfrac{\text{N·m·s}}{\text{rad}}$, $N_1=20$, $N_2=100$, $N_3=25$, $N_4=100$, $J_L=400\,\text{kg·m}^2$, $D_L=800\,\tfrac{\text{N·m·s}}{\text{rad}}$.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\small, >={Stealth[length=2mm]}]
% Motor bloğu + ea
\draw (-1.6,1.3) node[left]{$e_a(t)$};
\draw[->](-1.6,1.2)--(-0.7,1.2);
\draw[thick] (-0.7,0.6) rectangle (0.7,1.8); \node at (0,1.2){Motor};
\node[align=left] at (0,-0.1){$J_a{=}1$\\$D_a{=}5$};
% N1 (motor mili) -> N2
\draw[thick] (0.7,1.2)--(1.6,1.2);
\draw[thick,fill=gray!10] (1.6,1.2) circle (0.22); \node at (1.6,1.75){$N_1{=}20$};
\draw[thick,fill=gray!10] (1.6,0.55) circle (0.43); \node at (2.55,0.55){$N_2{=}100$};
% Ara mil: N2 ile N3 aynı milde
\draw[thick] (1.6,0.55)--(3.4,0.55);
% N3 -> N4
\draw[thick,fill=gray!10] (3.4,0.55) circle (0.27); \node at (3.4,1.1){$N_3{=}25$};
\draw[thick,fill=gray!10] (3.4,-0.4) circle (0.55); \node at (4.4,-0.4){$N_4{=}100$};
% Yük mili
\draw[thick] (3.4,-0.4)--(5.0,-0.4);
\draw[thick,fill=gray!18] (5.0,-0.4) ellipse (0.3 and 0.55); \node at (5.0,-1.25){$J_L{=}400$};
\node at (5.0,0.35){$\theta_L$};
% DL duvara
\draw[thick](5.3,-0.4)--(6.0,-0.4); \draw[thick](6.0,-0.65)rectangle(6.5,-0.15);
\draw[thick](6.5,-0.4)--(7.0,-0.4); \node at (6.25,0.15){$D_L{=}800$};
\draw[very thick](7.0,-1.0)--(7.0,0.2);
\foreach \y in {-0.8,-0.4,...,0.0}{\draw (7.0,\y)--(7.22,\y+0.18);}
\end{tikzpicture}
\end{document}
```

> [!note]- Semboller
> - $J_a,D_a$: motor (armatür) eylemsizliği/sönümü; $J_L,D_L$: yük eylemsizliği/sönümü
> - $N_1{\to}N_2$ ve $N_3{\to}N_4$: iki dişli kademesi; toplam oran $\dfrac{\theta_L}{\theta_m}=\dfrac{N_1}{N_2}\cdot\dfrac{N_3}{N_4}$
> - **İndirgeme:** yük elemanlarını motor miline taşırken $\left(\frac{N_1}{N_2}\cdot\frac{N_3}{N_4}\right)^2$ ile çarp
> - Tork-hız doğrusundan: durma torku $T_{stall}=T_m(\omega{=}0)$, boş hız $\omega_{nl}=\omega_m(T_m{=}0)$
> - $\dfrac{K_t}{R_a}=\dfrac{T_{stall}}{e_a}$, $\;K_b=\dfrac{e_a}{\omega_{nl}}$

**Çözüm:**

**1) Dişli indirgemesi** (toplam oran $\frac{N_1}{N_2}\cdot\frac{N_3}{N_4}=\frac{20}{100}\cdot\frac{25}{100}=\frac15\cdot\frac14=\frac{1}{20}$, kare $=\frac{1}{400}$):
$$J_m=J_a+J_L\Big(\tfrac15\cdot\tfrac14\Big)^2=1+400\cdot\tfrac1{400}=2,\qquad D_m=D_a+D_L\Big(\tfrac15\cdot\tfrac14\Big)^2=5+800\cdot\tfrac1{400}=7$$

**2) Tork-hız doğrusundan motor sabitleri** ($T_m=-8\omega_m+200$, $e_a=100\,\text V$):
$$\omega_m=0\Rightarrow T_{stall}=200,\qquad T_m=0\Rightarrow \omega_{nl}=\tfrac{200}{8}=25$$
$$\frac{K_t}{R_a}=\frac{T_{stall}}{e_a}=\frac{200}{100}=2,\qquad K_b=\frac{e_a}{\omega_{nl}}=\frac{100}{25}=4$$

**3) Motor transfer fonksiyonu** ($L_a\approx0$):
$$\frac{\theta_m(s)}{E_a(s)}=\frac{\frac{K_t}{R_aJ_m}}{s\Big(s+\frac1{J_m}\big(D_m+\frac{K_tK_b}{R_a}\big)\Big)}=\frac{\frac{2}{2}}{s\big(s+\frac12(7+2\cdot4)\big)}=\frac{1}{s\big(s+\frac{15}{2}\big)}$$

**4) Yük açısına geç** ($\frac{\theta_L}{\theta_m}=\frac1{20}$):
$$\frac{\theta_L(s)}{E_a(s)}=\frac{1/20}{s\big(s+\frac{15}{2}\big)}$$

**5) Giriş $e_a(t)=20\delta(t)\Rightarrow E_a(s)=20$:**
$$\theta_L(s)=20\cdot\frac{1/20}{s\big(s+\frac{15}{2}\big)}=\frac{1}{s\big(s+\frac{15}{2}\big)}=\frac{A}{s}+\frac{B}{s+\frac{15}{2}}$$
$$A=\left.\frac{1}{s+\frac{15}{2}}\right|_{s=0}=\frac{2}{15},\qquad B=\left.\frac1s\right|_{s=-\frac{15}{2}}=-\frac{2}{15}$$
$$\boxed{\theta_L(t)=\Big(\tfrac{2}{15}-\tfrac{2}{15}e^{-\frac{15}{2}t}\Big)u(t)}$$
Kalıcı durumda ($t\to\infty$) yük yer değiştirmesi $\theta_L(\infty)=\dfrac{2}{15}\approx 0{,}133\,\text{rad}$.

---

## Soru 4 — RC Merdiven Devre: Durum-Uzayı ve Dürtü Yanıtı · 25p

**Soru:** Verilen elektrik devresinin 
**(a)** durum-uzayı modelini çıkarın (15p). 
**(b)** Durum-uzayı modelini kullanarak transfer fonksiyonunu bulun; $R=1\,\Omega$ ve $C=1\,\text F$ olan sistemde $u(t)=\delta(t)$ ise $y(t)$ nedir? (10p)

<span style="color:rgb(0, 176, 240)"><span style="color:rgb(0, 176, 240)">Devre: giriş $u(t)$ → seri $R$ → $v<i>1$ düğümü (toprağa $C$) → seri $R$ → $v</i>2$ düğümü (toprağa $C$) → çıkış $y=v_2$.</span></span>

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$u$] (0,3);
\draw (0,3) to[R=$R$, i>_=$i_1$] (2.5,3) coordinate(v1);
\draw (v1) to[C=$C$, i=$i_3$] (2.5,0);
\draw (v1) to[R=$R$, i>_=$i_2$] (5,3) coordinate(v2);
\draw (v2) to[C=$C$, i=$i_4$] (5,0);
\draw (5,3) to[short, *-o] (6,3) node[right]{$y$};
\draw (0,0) -- (5,0);
\draw (5,0) to[short, -o] (6,0);
\node[above] at (2.5,3.1){$v_1$};
\node[above] at (5,3.1){$v_2$};
\end{circuitikz}
\end{document}
```

---

### 🧠 Önce Kavramlar: Durum-Uzayı Nedir?

> [!info]- **Durum değişkeni neden kapasitör gerilimi?**
> Kapasitör enerji depolar: $E=\frac{1}{2}Cv^2$. Sistemin "durumu" = şu an depolanan enerji miktarı.
> Kaç kapasitör varsa o kadar durum değişkeni olur.
> Burada **2 kapasitör** → **2 durum** → $x_1=v_1$, $x_2=v_2$.
>
> Aynı mantık mekanikte: yay (potansiyel enerji) → konum durum değişkeni, kütle (kinetik enerji) → hız durum değişkeni.

> [!info]- **Durum-uzayı modeli ne demek?**
> Sistemi şu formda yazıyoruz:
> $$\dot{\mathbf{x}} = A\mathbf{x} + Bu \qquad \text{(durum denklemi)}$$
> $$y = C\mathbf{x} + Du \qquad \text{(çıkış denklemi)}$$
>
> | Matris | Boyut | Ne anlama gelir |
> |---|---|---|
> | $A$ | $n\times n$ | Durumların birbirini nasıl etkilediği |
> | $B$ | $n\times 1$ | Girişin durumları nasıl etkilediği |
> | $C$ | $1\times n$ | Hangi durum(lar) çıkışa gidiyor |
> | $D$ | $1\times 1$ | Direkt giriş→çıkış bağlantısı (çoğu fiziksel sistemde $0$) |
>
> Burada: $n=2$ (2 durum), giriş $u$, çıkış $y=v_2=x_2$.

> [!info]- **Kapasitör denklemi — KCL'ye nasıl giriyor?**
> Kapasitörden geçen akım: $i_C = C\dfrac{dv_C}{dt}$
> Bunu $\dot{x}$ için çözersek: $\dfrac{dv_C}{dt} = \dfrac{i_C}{C}$
>
> Yani KCL ile "düğüme giren = düğümden çıkan" yazınca kapasitör akımını bulduk, onu $C$'ye böldük → $\dot{x}$ elde ettik. İşte bu yüzden KCL yazıyoruz.

---

### **(a) Durum Denklemlerini Çıkar**

**Adım 1 — Devredeki akımları tanımla:**

$$i_1 = \frac{u - v_1}{R} \quad \text{(sol dirençten gelen akım)}$$
$$i_2 = \frac{v_1 - v_2}{R} \quad \text{(sağ dirençten geçen akım)}$$
$$i_3 = C\frac{dv_1}{dt} \quad \text{(sol kapasitörün akımı)}$$
$$i_4 = C\frac{dv_2}{dt} \quad \text{(sağ kapasitörün akımı)}$$

---

**Adım 2 — $v_1$ düğümünde KCL** (giren = çıkan):

$$i_1 = i_3 + i_2$$
$$\frac{u-v_1}{R} = C\frac{dv_1}{dt} + \frac{v_1-v_2}{R}$$

> [!info]- **Bu eşitlik nereden geliyor?**
> $v_1$ düğümüne soldan $i_1$ giriyor. Bu akım iki yere gidiyor: ya kapasitöre ($i_3$) ya da sağa doğru ($i_2$). KCL der ki "giren = çıkan".

$\dfrac{dv_1}{dt}$'yi yalnız bırak — her şeyi $C$'ye böl, sağ tarafı sola taşı:

$$C\frac{dv_1}{dt} = \frac{u-v_1}{R} - \frac{v_1-v_2}{R} = \frac{u - v_1 - v_1 + v_2}{R} = \frac{u - 2v_1 + v_2}{R}$$

$$\frac{dv_1}{dt} = \frac{-2v_1}{RC} + \frac{v_2}{RC} + \frac{u}{RC}$$

$$\boxed{\dot x_1 = -\frac{2}{RC}x_1 + \frac{1}{RC}x_2 + \frac{1}{RC}u}$$

> [!info]- **Neden $-2v_1$ çıktı?**
> Sol dirençte gerilim farkı $(u-v_1)$, sağ dirençte $(v_1-v_2)$. İkisinde de $v_1$ var: soldaki $-v_1$, sağdaki $-v_1$ → toplam $-2v_1$.

---

**Adım 3 — $v_2$ düğümünde KCL** (giren = çıkan):

$$i_2 = i_4$$
$$\frac{v_1 - v_2}{R} = C\frac{dv_2}{dt}$$

$\dfrac{dv_2}{dt}$'yi yalnız bırak:

$$\frac{dv_2}{dt} = \frac{v_1 - v_2}{RC}$$

$$\boxed{\dot x_2 = \frac{1}{RC}x_1 - \frac{1}{RC}x_2}$$

> [!info]- **$v_2$ denkleminde neden giriş $u$ yok?**
> Giriş $u$ sadece sol tarafta. $v_2$ düğümüne $u$ doğrudan bağlı değil — $v_1$ üzerinden geliyor. Dolayısıyla $v_2$'nin denklemi yalnızca $v_1$ ve $v_2$'ye bağlı.

---

**Adım 4 — Matris formuna yaz** ($y = v_2 = x_2$):

$$\underbrace{\begin{bmatrix}\dot x_1\\\dot x_2\end{bmatrix}}_{\dot{\mathbf{x}}}=\underbrace{\begin{bmatrix}-\dfrac{2}{RC}&\dfrac{1}{RC}\\[6pt]\dfrac{1}{RC}&-\dfrac{1}{RC}\end{bmatrix}}_{A}\underbrace{\begin{bmatrix}x_1\\x_2\end{bmatrix}}_{\mathbf{x}}+\underbrace{\begin{bmatrix}\dfrac{1}{RC}\\[6pt]0\end{bmatrix}}_{B}u$$

$$y=\underbrace{\begin{bmatrix}0&1\end{bmatrix}}_{C}\begin{bmatrix}x_1\\x_2\end{bmatrix}$$

> [!info]- **$B$ matrisinde neden alt eleman sıfır?**
> $\dot x_1$ denkleminde $u$ var ($+\frac{u}{RC}$) → $B$'nin ilk elemanı $\frac{1}{RC}$.
> $\dot x_2$ denkleminde $u$ yok → $B$'nin ikinci elemanı $0$.

> [!info]- **$C=[0\;1]$ neden?**
> Çıkış $y=x_2$. Yani $y = 0\cdot x_1 + 1\cdot x_2$. Bunu $[0\;1]\begin{bmatrix}x_1\\x_2\end{bmatrix}$ olarak yazıyoruz.

---

### **(b) Transfer Fonksiyonu ve Dürtü Yanıtı**

$R=C=1$ koy → $RC=1$:
$$A=\begin{bmatrix}-2&1\\1&-1\end{bmatrix},\quad B=\begin{bmatrix}1\\0\end{bmatrix},\quad C=[0\;1],\quad D=0$$

**Transfer fonksiyonu formülü:** $G(s)=C(sI-A)^{-1}B$

> [!info]- **Bu formül nereden geliyor?**
> Durum denkleminin Laplace dönüşümünü al (sıfır başlangıç):
> $sX(s) = AX(s) + BU(s)$
> $(sI-A)X(s) = BU(s)$
> $X(s) = (sI-A)^{-1}BU(s)$
> Çıkış: $Y(s) = CX(s) = C(sI-A)^{-1}B\cdot U(s)$
> Yani $G(s)=Y(s)/U(s) = C(sI-A)^{-1}B$.

---

**Adım 1 — $(sI-A)$ hesapla:**

$$sI - A = s\begin{bmatrix}1&0\\0&1\end{bmatrix}-\begin{bmatrix}-2&1\\1&-1\end{bmatrix}=\begin{bmatrix}s+2&-1\\-1&s+1\end{bmatrix}$$

> [!info]- **$sI-A$ nasıl hesaplanır?**
> $sI$ = $s$ ile çarpılmış birim matris = köşegene $s$ yaz, geri kalan sıfır.
> Sonra $A$'yı çıkar: her elemanın işareti değişir.
> $A_{11}=-2$ → $-(−2)=+2$ → $(s+2)$; $A_{12}=1$ → $-1$; $A_{21}=1$ → $-1$; $A_{22}=-1$ → $-(−1)=+1$ → $(s+1)$.

---

**Adım 2 — Determinantı hesapla:**

$$\det(sI-A) = (s+2)(s+1)-(-1)(-1) = s^2+3s+2-1 = s^2+3s+1$$

---

**Adım 3 — Matris tersini hesapla:**

2×2 matris tersi formülü: $\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1} = \dfrac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$

$$\begin{bmatrix}s+2&-1\\-1&s+1\end{bmatrix}^{-1} = \frac{1}{s^2+3s+1}\begin{bmatrix}s+1&1\\1&s+2\end{bmatrix}$$

> [!info]- **Ters matris formülü ne yapıyor?**
> 4 işlem: köşegenleri yer değiştir ($a\leftrightarrow d$), diğer ikisinin işaretini değiştir ($b\to -b$, $c\to -c$), sonucu determinanta böl.
> Burada: $(s+2)\leftrightarrow(s+1)$ yer değiştirdi, $(-1)\to(+1)$ oldu, determinant $s^2+3s+1$.

---

**Adım 4 — $G(s) = C(sI-A)^{-1}B$ çarp:**

Önce $C\cdot(sI-A)^{-1}$:
$$[0\;1]\cdot\frac{1}{s^2+3s+1}\begin{bmatrix}s+1&1\\1&s+2\end{bmatrix} = \frac{1}{s^2+3s+1}\underbrace{[0\cdot(s+1)+1\cdot1\;,\; 0\cdot1+1\cdot(s+2)]}_{=[1,\;s+2]}$$

Sonra $B$ ile çarp:
$$G(s)=\frac{1}{s^2+3s+1}\,[1\;,\;s+2]\begin{bmatrix}1\\0\end{bmatrix}=\frac{1\cdot1+(s+2)\cdot0}{s^2+3s+1}=\frac{1}{s^2+3s+1}$$

$$\boxed{\dfrac{Y(s)}{U(s)}=\dfrac{1}{s^2+3s+1}}$$

---

**Adım 5 — Dürtü yanıtı** ($u(t)=\delta(t)\Rightarrow U(s)=1$):

$$Y(s)=\frac{1}{s^2+3s+1}$$

**Kökleri bul** — ikinci dereceden denklem $s^2+3s+1=0$, kökleri şu formülle:
$$s_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}=\frac{-3\pm\sqrt{3^2-4\cdot1\cdot1}}{2\cdot1}=\frac{-3\pm\sqrt{9-4}}{2}=\frac{-3\pm\sqrt{5}}{2}$$
$$s_1=\frac{-3+2{,}24}{2}\approx-0{,}38,\qquad s_2=\frac{-3-2{,}24}{2}\approx-2{,}62$$

Her ikisi de **reel** (karmaşık değil) ve **negatif** (sol yarı düzlemde) → sistem kararlı ve **aşırı sönümlü**.

> [!info]- **Sönüm türü nasıl belirleniyor? — Diskriminant ve $\zeta$ yöntemi**
> **Yöntem 1 — Diskriminant ($\Delta = b^2-4ac$):**
>
> | Diskriminant | Kök tipi | Sönüm türü |
> |---|---|---|
> | $\Delta > 0$ | 2 farklı reel kök | **Aşırı sönümlü** ($\zeta > 1$) → $\sinh$ |
> | $\Delta = 0$ | 1 tekrar eden reel kök | **Kritik sönümlü** ($\zeta = 1$) → $te^{-at}$ |
> | $\Delta < 0$ | 2 karmaşık eşlenik kök | **Az sönümlü** ($\zeta < 1$) → $e^{-at}\sin(\omega t)$ |
>
> Burada $\Delta = 9-4 = 5 > 0$ → **aşırı sönümlü**.
>
> **Yöntem 2 — Standart form karşılaştırması:**
> Standart ikinci derece sistem: $s^2 + 2\zeta\omega_n s + \omega_n^2$
> Bunu $s^2+3s+1$ ile karşılaştır:
> $$\omega_n^2 = 1 \Rightarrow \omega_n = 1\,\text{rad/s}$$
> $$2\zeta\omega_n = 3 \Rightarrow \zeta = \frac{3}{2\cdot1} = 1{,}5$$
> $\zeta = 1{,}5 > 1$ → **aşırı sönümlü** ✓

Kareyi tamamla:
$$s^2+3s+1 = \left(s+\frac{3}{2}\right)^2 - \frac{9}{4}+1 = (s+1{,}5)^2-1{,}25$$

$\sinh$ Laplace çifti: $\mathcal{L}^{-1}\!\left\{\dfrac{b}{(s+a)^2-b^2}\right\}=e^{-at}\sinh(bt)$

> [!info]- **Neden $\sinh$ kullanıyoruz, $\sin$ değil?**
> $\sin$ kullanmak için paydanın $(s+a)^2+\omega^2$ formunda olması gerekir — yani karekök içi **pozitif** olmalı.
> Burada $(s+1{,}5)^2 - 1{,}25$ → karekök içi **negatif** → bu **reel kökler** demek → $\sinh$ (hiperbolik sinüs) kullanılır.
> $\sinh(bt)=\frac{e^{bt}-e^{-bt}}{2}$, yani iki üstel terimin farkı.

$b=\sqrt{1{,}25}\approx1{,}12$ ile:
$$Y(s)=\frac{1}{(s+1{,}5)^2-1{,}12^2}=\frac{1}{1{,}12}\cdot\frac{1{,}12}{(s+1{,}5)^2-1{,}12^2}$$

$$\boxed{y(t)=\frac{1}{1{,}12}\,e^{-1{,}5t}\sinh(1{,}12\,t)\approx 0{,}89\,e^{-1{,}5t}\sinh(1{,}12\,t)}$$

> [!tip] Sınav notu
> Cevap anahtarındaki taslakta $Y/U$ bir ara satırda $\frac{-s}{s^2+3s+1}$ olarak görünüyor; doğru ve nihai matris hesabı **$\frac{1}{s^2+3s+1}$** verir (çıkış kapasitör gerilimi, dürtüye karşı pozitif $\sinh$ yanıtı). Yöntem aynı, sonuç bu kutudaki gibidir.

---

> [!sinav] Vize Gecesi — Hızlı Hatırlatma (bu 4 soru)
> - **S1 Sismograf:** taban tahriki → $-ms^2$ payı; $y=x_0-x_i$ ile $x_0$'ı yok et
> - **S2 İki kütle:** Lagrange (enerji+sönüm fonk.) ve Newton (SCD) aynı denkleme çıkar → Cramer
> - **S3 Dişli+motor:** iki kademe → $(N_1N_3)/(N_2N_4)$ oranı; durma torku → $K_t/R_a$, boş hız → $K_b$
> - **S4 RC merdiven:** her kapasitör bir durum; düğüm KCL → $\dot x$; $G=C(sI-A)^{-1}B$
