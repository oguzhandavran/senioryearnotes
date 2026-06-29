---
tags: [mst, final, sınav-soruları, çözümlü, kök-yer-eğrisi, doğrusallaştırma, faz-portresi, denge-noktası]
---

# 06 — MST&B Final Sınav Soruları (Çözümlü)

← [[MST Ana Sayfa]]

> Kaynak PDF: `DATASET/Mühendislik Sistem Tasarımı ve Benzetimi/MST_Final_Cevap_Anahtari.pdf`

---

## Soru 1 — Kök Yer Eğrisi ve PD Denetleyici Tasarımı

**Verilen:**
$$G(s) = \frac{K}{(s+1)(s+2)(s+3)}$$

Sistemin kök yer eğrisini çizin ve tasarım adımlarını gerçekleştirin.

> [!note]- Semboller
> - $G(s)$: açık çevrim transfer fonksiyonu; $K$: değişken kazanç
> - $m,n$: kutup ve sıfır sayıları; asimptot sayısı $=m-n$
> - $\beta$: asimptot açısı (Adım 4) / sönüm açısı $\cos^{-1}\zeta$ (Adım 8) — bağlama dikkat
> - $\sigma_a$: asimptotların reel ekseni kestiği nokta; ayrılma noktası: $(1/G)'=0$
> - $\%OS$: yüzde aşım; $\zeta$: sönüm oranı; $\omega_n$: doğal frekans; $s_d$: baskın kutup
> - $\ell_i$: $s_d$'den kutuplara uzaklıklar; genlik kriteri $K=\prod\ell_{\text{kutup}}/\prod\ell_{\text{sıfır}}$
> - $K_p=\lim_{s\to0}G$: konum hata sabiti (Tip 0); $e_{ss}=1/(1+K_p)$: basamak hatası
> - $t_s=4/(\zeta\omega_n)$: yerleşme süresi; $z_c$: PD sıfırı; $R_1,R_2,C$: op-amp elemanları

> [!info]- **Kök yer eğrisi nedir — neden çiziyoruz?**
> Kapalı çevrim sistemde $K$ değiştikçe kutuplar (yani sistemin doğal frekansları) değişir. Kök yer eğrisi, $K: 0\to\infty$ aralığında kutupların s-düzleminde çizdiği yolu gösterir.
>
> **Neden önemli?** Kutupların konumu sistemin davranışını belirler:
> - Sol yarı düzlem → kararlı sistem
> - Sanal eksen yakını → salınımlı yanıt
> - Reel eksen → üstel (salınımsız) yanıt
>
> Kök yer eğrisiyle "$K$ ne olursa sistem istediğim davranışı gösterir?" sorusunu yanıtlıyoruz.

---

### Adım 1 — Sıfır ve Kutup Sayıları (1p)

- **Sıfırlar:** $G(s)$ payında $s$ içeren terim yok → $n = 0$
- **Kutuplar:** paydayı sıfır yapan değerler → $s = -1,\,-2,\,-3$ → $m = 3$

> [!info]- **Kutup ve sıfır nedir?**
> - **Kutup:** $G(s)$'yi sonsuz yapan $s$ değeri — paydanın kökleri. Kök yer eğrisi **kutuplardan başlar** ($K=0$).
> - **Sıfır:** $G(s)$'yi sıfır yapan $s$ değeri — payın kökleri. Kök yer eğrisi **sıfırlarda biter** ($K\to\infty$).
> - Burada sıfır yok, bu yüzden 3 dal da sonunda asimptotlara gider (sonsuzluğa kaçar).

---

### Adım 2 — Kök Yer Eğrisi Taslağı (1p)

![[mst06-kye.png]]

> [!note]- Python kaynağı — `_assets/scripts/mst06-kye.py`
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
>
> poles = [-1, -2, -3]
> Ks = np.concatenate([np.linspace(0, 6, 800), np.linspace(6, 300, 2000)])
> roots = np.array([np.roots([1, 6, 11, 6 + K]) for K in Ks])  # s³+6s²+11s+(6+K)
>
> fig, ax = plt.subplots(figsize=(6, 5))
> allr = roots.flatten()
> ax.scatter(allr.real, allr.imag, s=2, color="#1a1a2e")
> ax.plot(poles, [0, 0, 0], "x", color="#c0392b", ms=11, mew=2)
> ax.axhline(0, color="0.6", lw=0.8); ax.axvline(0, color="0.6", lw=0.8)
> ax.set_xlim(-6, 2); ax.set_ylim(-4, 4)
> plt.show()   # σ_a=-2, asimptotlar 60°/180°/300°
> ```

3 dal, 3 kutuptan çıkar, 3 asimptota gider.

---

### Adım 3 — Asimptot Sayısı (1p)

$$m - n = 3 - 0 = \boxed{3 \text{ adet}}$$

> [!info]- **Neden $m-n$ adet asimptot?**
> $K\to\infty$ olunca dallar ya sıfırlara gider ya da sonsuzluğa kaçar. Elimizde $n=0$ sıfır var, $m=3$ dal var. Sıfıra gidecek dal yok → 3 dal da sonsuzluğa gider → 3 asimptot.
>
> Genel kural: **asimptot sayısı = kutup sayısı − sıfır sayısı = $m-n$**.

---

### Adım 4 — Asimptot Açıları (1p)

$$\beta = \frac{180°(2k+1)}{m-n} = \frac{180°(2k+1)}{3} \Rightarrow \boxed{60°,\ 180°,\ 300°}$$

> [!info]- **Bu formül nereden geliyor?**
> Kök yer eğrisinin koşulu: $\angle G(s) = \pm 180°(2k+1)$ (açı koşulu).
> $s\to\infty$ sınırında bu koşul asimptot yönlerini verir. $k=0,1,2$ için:
> - $k=0$: $\frac{180°\cdot1}{3}=60°$
> - $k=1$: $\frac{180°\cdot3}{3}=180°$
> - $k=2$: $\frac{180°\cdot5}{3}=300°$
>
> 300° = −60° olduğundan eğri simetrik çıkar (reel eksen etrafında simetri her zaman geçerlidir).

---

### Adım 5 — Asimptotların Reel Ekseni Kestiği Nokta (1p)

$$\sigma_a = \frac{\sum\text{kutuplar} - \sum\text{sıfırlar}}{m-n} = \frac{(-1-2-3) - 0}{3} = \frac{-6}{3} = \boxed{-2}$$

> [!info]- **Neden bu formül? (Ağırlık merkezi)**
> Asimptotlar tek bir noktadan çıkar — bu nokta kutupların ve sıfırların "ağırlık merkezi" gibi düşünülebilir. Kutuplar sol tarafa, sıfırlar sağa katkı yapar. Sıfır yoksa sadece kutupların ortalaması alınır: $(-1-2-3)/3 = -2$.

---

### Adım 6 — Ayrılma-Birleşme Noktası (1p)

$$\left(\frac{1}{G(s)}\right)' = 0 \Rightarrow \left(\frac{(s+1)(s+2)(s+3)}{K}\right)' = 0$$

Açılırsa:
$$(s^2+3s+2)(s+3) = s^3+6s^2+11s+6$$

$$(s^3+6s^2+11s+6)' = 3s^2+12s+11 = 0$$

$$s = \frac{-12 \pm \sqrt{144-132}}{6} = \frac{-12 \pm \sqrt{12}}{6}$$

$$\boxed{s_1 = -1{,}423 \quad (\text{reel eksende, geçerli})}$$
$$s_2 = -2{,}577 \quad (\text{reel eksende, geçerli})$$

> [!info]- **Ayrılma noktası nedir, neden $(1/G)'=0$?**
> İki dal reel eksende ilerlerken bir noktada **ayrılır** (biri yukarı biri aşağı gider — karmaşık düzleme iner). Bu noktada $K$'nın $s$'ye göre türevi sıfırdır.
>
> $K = -1/G(s)$ (kapalı çevrim koşulundan), dolayısıyla $dK/ds = 0$ → $(1/G)' = 0$.
>
> Bulunan kökler reel eksende ve iki kutup arasında mı? → Geçerli ayrılma noktası.
> - $s_1 = -1{,}423$: $-1$ ile $-2$ arasında ✓ (ayrılma)
> - $s_2 = -2{,}577$: $-2$ ile $-3$ arasında ✓ (birleşme)

---

### Adım 7 — Sönüm Oranı (%20 aşım için) (1p)

$$\zeta = \frac{-\ln(\%OS/100)}{\sqrt{\pi^2 + \ln^2(\%OS/100)}} = \frac{-\ln(0{,}20)}{\sqrt{\pi^2 + \ln^2(0{,}20)}} = \frac{1{,}609}{\sqrt{9{,}870 + 2{,}590}} = \boxed{0{,}456}$$

> [!info]- **Bu formül nereden geliyor?**
> İkinci derece sistem için yüzde aşım ile sönüm oranı arasındaki bağıntı:
> $$\%OS = 100\cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$
> Her iki tarafın logaritması alınıp $\zeta$ için çözülünce yukarıdaki formül elde edilir.
>
> **Pratik değerler:** $\%OS=5\%\to\zeta=0{,}69$; $\%OS=10\%\to\zeta=0{,}59$; $\%OS=20\%\to\zeta=0{,}46$; $\%OS=50\%\to\zeta=0{,}22$

---

### Adım 8 — Sönüm Açısı (1p)

$$\beta = \cos^{-1}(\zeta) = \cos^{-1}(0{,}456) = \boxed{62{,}87°}$$

> [!info]- **Neden $\beta = \cos^{-1}(\zeta)$?**
> İkinci derece sistemin baskın kutupları $s_{1,2}=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}$ formundadır.
> Bu kutbun orijine göre açısı:
> $$\cos\beta = \frac{\zeta\omega_n}{|s_d|} = \zeta$$
> Yani s-düzleminde kutbu orijine bağlayan doğrunun reel eksenle yaptığı açı $\beta = \cos^{-1}\zeta$ olur. Bu açıdaki tüm noktalar aynı $\zeta$'ya sahiptir → bu doğru üzerinde istenen kutup aranır.

---

### Adım 9 — İstenen Kutup Konumu ve K (her biri 1p)

$|s_d| = 1{,}8594$ ve $\beta = 117{,}26°$ (= $180° - 62{,}87°$, 2. bölge):
$$s_d = 1{,}8594(\cos 117{,}26° + j\sin 117{,}26°) = -0{,}866 + j1{,}169$$

> [!info]- **$s_d$ nasıl bulundu?**
> $\zeta$ oranı 2. bölgedeki bir çizgiyi tanımlar (reel eksen ile $180°-62{,}87°=117{,}26°$). Bu çizginin kök yer eğrisiyle kesiştiği nokta $s_d$'dir.
> Genlik: $|s_d|=\omega_n$, açı: $117{,}26°$. Kartezyen:
> $\sigma = -|s_d|\cos(62{,}87°) = -0{,}866$, $\omega = |s_d|\sin(62{,}87°) = 1{,}169$

Kutuplardan uzaklıklar (her kutuptan $s_d$'ye olan Öklid uzaklığı):
$$\ell_1 = |s_d - (-3)| = \sqrt{(3-0{,}866)^2 + 1{,}169^2} = \sqrt{4{,}554+1{,}367} = 2{,}72$$
$$\ell_2 = |s_d - (-2)| = \sqrt{(2-0{,}866)^2 + 1{,}169^2} = \sqrt{1{,}286+1{,}367} = 2{,}035$$
$$\ell_3 = |s_d - (-1)| = \sqrt{(1-0{,}866)^2 + 1{,}169^2} = \sqrt{0{,}018+1{,}367} = 1{,}695$$

$$\boxed{K = \frac{\prod\text{kutup uzaklıkları}}{\prod\text{sıfır uzaklıkları}} = \ell_1 \cdot \ell_2 \cdot \ell_3 = 2{,}72 \times 2{,}035 \times 1{,}695 = 8{,}33}$$

> [!info]- **Genlik kriteri nedir?**
> Kök yer eğrisi koşulu: $|KG(s_d)| = 1$.
> Yani: $K\cdot\dfrac{1}{\ell_1\ell_2\ell_3} = 1 \Rightarrow K = \ell_1\ell_2\ell_3$.
> Sıfır olsaydı payda sıfıra olan uzaklıklar gelirdi (burada sıfır yok → payda 1).

---

### Adım 10 — Kararlı Durum Hatası (1p + 1p)

**Tip 0** sistem — açık çevrimde serbest integratör ($1/s$ terimi) yok:

$$K_p = \lim_{s\to 0} G(s) = \frac{8{,}33}{(0+1)(0+2)(0+3)} = \frac{8{,}33}{6} = 1{,}565$$

$$\boxed{e_{ss} = \frac{1}{1+K_p} = \frac{1}{1+1{,}565} = \frac{1}{2{,}565} = 0{,}39}$$

> [!info]- **Sistem tipi ve kararlı durum hatası**
> Açık çevrimde kaç tane $1/s$ faktörü var? → Sistem tipi.
>
> | Sistem Tipi | Basamak giriş $e_{ss}$ | Rampa $e_{ss}$ |
> |---|---|---|
> | Tip 0 | $\dfrac{1}{1+K_p}$ | $\infty$ |
> | Tip 1 | $0$ | $\dfrac{1}{K_v}$ |
> | Tip 2 | $0$ | $0$ |
>
> Burada $G(s)=K/[(s+1)(s+2)(s+3)]$ → paydada serbest $s$ yok → **Tip 0** → basamak girişe sonlu hata, rampa girişe sonsuz hata.

---

### Adım 11 — İmajiner Ekseni Kesme Noktası (Routh-Hurwitz) (1p)

Kapalı çevrim karakteristik polinomu:
$$1 + G(s) = 0 \Rightarrow s^3 + 6s^2 + 11s + (6+K) = 0$$

> [!info]- **Karakteristik polinom nasıl elde edildi?**
> Kapalı çevrim TF: $\frac{G}{1+G}$. Payda $1+G(s)=0$:
> $$1 + \frac{K}{(s+1)(s+2)(s+3)} = 0 \Rightarrow (s+1)(s+2)(s+3) + K = 0$$
> Açılınca: $s^3+6s^2+11s+6+K=0$.

Routh tablosu:

| $s^3$ | $1$ | $11$ |
|--------|---|-----|
| $s^2$ | $6$ | $6+K$ |
| $s^1$ | $\dfrac{6\cdot11 - 1\cdot(6+K)}{6} = \dfrac{60-K}{6}$ | $0$ |
| $s^0$ | $6+K$ | — |

> [!info]- **Routh tablosu nasıl doldurulur?**
> 1. satır: $s^n$ katsayıları, 2. satır: $s^{n-1}$ katsayıları (tek ve çift indisler ayrı sütun)
> Sonraki satır: $-\frac{1}{\text{sol üst}}\det\begin{bmatrix}\text{2 satır, 2 sütun}\end{bmatrix}$
> $s^1$ satırı: $\frac{6\times11 - 1\times(6+K)}{6} = \frac{60-K}{6}$
>
> **Kararlılık koşulu:** 1. sütunun tüm elemanları pozitif olmalı:
> - $6 > 0$ ✓
> - $\frac{60-K}{6} > 0 \Rightarrow K < 60$
> - $6+K > 0 \Rightarrow K > -6$

Kararlılık koşulu: $\boxed{-6 < K < 60}$

$K = 60$ olursa imajiner eksen kesimi: $s^3 + 6s^2 + 11s + 66 = 0$

Yardımcı polinom ($s^2$ satırından): $6s^2 + 66 = 0 \Rightarrow s^2 = -11 \Rightarrow s_{2,3} = \pm j3{,}317$

Çözüm: $s_1 = -6$, $s_{2,3} = \pm j3{,}317$

---

### Adım 12 — Yerleşme Süresi ve PD Tasarımı (her biri 1p)

**Mevcut sistem için:**
$$t_s = \frac{4}{\zeta\omega_n} = \frac{4}{0{,}456 \times 1{,}8594} = \frac{4}{0{,}848} \approx 4{,}72 \text{ s}$$

> [!info]- **Yerleşme süresi formülü nereden geliyor?**
> $t_s = 4/(\zeta\omega_n)$: kapalı çevrim yanıtının $\pm 2\%$ bandına girme süresi. $\zeta\omega_n$ baskın kutbun reel kısmıdır — ne kadar büyükse (reel eksenden ne kadar uzaksa) o kadar hızlı söner.

**İstenen yerleşme süresi** (4 kat iyileştirme):
$$t_{s,\text{yeni}} = \frac{4{,}72}{4} = 1{,}18 \text{ s}$$

**İstenen $\omega_n$:**
$$\omega_{ny} = \frac{4}{\zeta \cdot t_{s,\text{yeni}}} = \frac{4}{0{,}456 \times 1{,}18} = 7{,}43 \text{ rad/s}$$

$$\alpha_y = \zeta\cdot\omega_{ny} = 0{,}456 \times 7{,}43 = 3{,}39, \qquad \omega_y = \omega_{ny}\sqrt{1-\zeta^2} = 7{,}43\times0{,}890 = 6{,}61$$

**İstenen kutup:** $s_y = -3{,}39 + j6{,}61$

**PD sıfırının bulunması — açı koşulu:**

$$\sum\angle_{\text{kutuplar}} - \sum\angle_{\text{sıfırlar}} = -180°$$

> [!info]- **Açı koşulu nedir?**
> $s_y$ noktasının kök yer eğrisi üzerinde olması için $\angle G(s_y) = -180°$ olmalı. Mevcut kutupların $s_y$'ye olan açıları toplandığında $-180°$'yi vermiyor — PD sıfırı bu açı farkını kapatmak için eklenir.

$$\theta_1 - (83{,}9° + 102{,}2° + 110{,}02°) = -180°$$
$$\theta_1 = -180° + 296{,}12° = 116{,}12° \Rightarrow \theta_1' = 180° - 116{,}12° = 63{,}88°$$

$$\tan(63{,}88°) = \frac{6{,}61}{3{,}39 - x} \Rightarrow 2{,}04 = \frac{6{,}61}{3{,}39-x} \Rightarrow \boxed{z_c \approx 0{,}15}$$

**PD transfer fonksiyonu:**
$$G_{PD}(s) = -R_2 C\!\left(s + \frac{1}{R_1 C}\right)$$

Tasarım kısıtları:
$$\frac{1}{R_1 C} = z_c, \quad R_2 C = 1$$

> [!info]- **PD denetleyici neden bu formu alıyor?**
> PD denetleyici türev etkisi ekler: hızlı değişime daha çabuk tepki verir, yerleşme süresini kısaltır. $s+z_c$ formu bir sıfır ekler — bu sıfır $s_y$ noktasını kök yer eğrisine çeker. Op-amp devresinde $R_1,R_2,C$ değerleri istenen $z_c$ ve kazanca göre seçilir.

---

## Soru 2 — Doğrusal Olmayan Sistem: Denge ve Kararlılık

**Verilen:**
$$\dot{x} = x^2 - y - 1 \equiv f_1(x,y)$$
$$\dot{y} = y(x-2) \equiv f_2(x,y)$$

> [!note]- Semboller
> - $x,y$: durum değişkenleri; $\dot x,\dot y$: türevleri
> - $f_1,f_2$: durum türev fonksiyonları
> - Denge noktası: $f_1=f_2=0$ olan $(x,y)$ noktaları
> - $J=[\partial f_i/\partial x_j]$: Jacobian matrisi; her dengede ayrı değerlendirilir
> - $\lambda$: özdeğer — iki negatif → kararlı düğüm; zıt işaret → eyer; iki pozitif → kararsız

> [!info]- **Doğrusal olmayan sistem nedir — neden farklı analiz gerekir?**
> Lineer sistemlerde $\dot{x}=Ax$ vardı, tek bir davranış tipi. Doğrusal olmayan sistemlerde birden fazla denge noktası olabilir ve her birinin etrafındaki davranış farklıdır.
>
> **Strateji:** Her denge noktasında sistemi **Jacobian ile doğrusallaştır** → doğrusallaştırılmış sistemin özdeğerlerini incele → kararlılık tipi belirle.

---

### 2a — Denge Noktaları (2p + 2p + 2p)

Denge noktası için $\dot{x}=0$ ve $\dot{y}=0$ koşulunu eş zamanlı çöz:

$$0 = x^2 - y - 1 \quad \Rightarrow \quad y = x^2 - 1 \quad \cdots(1)$$
$$0 = y(x-2) \quad \Rightarrow \quad y = 0 \text{ veya } x = 2 \quad \cdots(2)$$

> [!info]- **Neden $\dot{x}=\dot{y}=0$?**
> Denge (denge noktası): sistemin hareketsiz kaldığı nokta. Hareket yoksa hız da yok → türevler sıfır. Çözüm birden fazla nokta verirse her biri ayrı bir denge noktasıdır.

**Durum 1 — $y = 0$:** $(1)$'e koy → $x^2-1=0$ → $x=\pm1$
$$\Rightarrow \mathbf{(-1,\,0)} \text{ ve } \mathbf{(1,\,0)}$$

**Durum 2 — $x = 2$:** $(1)$'e koy → $y = 4-1 = 3$
$$\Rightarrow \mathbf{(2,\,3)}$$

$$\boxed{\text{Denge noktaları: } (-1,0),\ (1,0),\ (2,3)}$$

---

### 2b — Jacobian Matrisi (3p)

$$J = \begin{bmatrix} \dfrac{\partial f_1}{\partial x} & \dfrac{\partial f_1}{\partial y} \\[8pt] \dfrac{\partial f_2}{\partial x} & \dfrac{\partial f_2}{\partial y} \end{bmatrix}$$

Her terimi hesapla:
- $\dfrac{\partial f_1}{\partial x} = \dfrac{\partial}{\partial x}(x^2-y-1) = 2x$
- $\dfrac{\partial f_1}{\partial y} = \dfrac{\partial}{\partial y}(x^2-y-1) = -1$
- $\dfrac{\partial f_2}{\partial x} = \dfrac{\partial}{\partial x}(y(x-2)) = y$
- $\dfrac{\partial f_2}{\partial y} = \dfrac{\partial}{\partial y}(y(x-2)) = x-2$

$$\boxed{J = \begin{bmatrix} 2x & -1 \\ y & x-2 \end{bmatrix}}$$

> [!info]- **Jacobian nedir — neden hesaplıyoruz?**
> Doğrusal olmayan sistemi bir denge noktası $(x_0,y_0)$ etrafında doğrusallaştırmak için kullanılır. Tıpkı tek değişkenli Taylor serisinde $f'(x_0)$ gibi, çok değişkenli türevi matris olarak yazar.
>
> Fiziksel anlam: $J$ matrisi, denge noktasına küçük bir sapma verildiğinde sistemin nasıl tepki verdiğini gösterir. $J$ bu yüzden her denge noktasında farklı değer alır — her noktada ayrı değerlendirilir.

---

### 2c — Her Denge Noktasında Kararlılık (her biri 3p)

#### (−1, 0) noktası:

$$J_{(-1,0)} = \begin{bmatrix} 2(-1) & -1 \\ 0 & (-1)-2 \end{bmatrix} = \begin{bmatrix} -2 & -1 \\ 0 & -3 \end{bmatrix}$$

Üçgen matris — özdeğerler köşegen elemanlarıdır:
$$\lambda_1 = -2,\quad \lambda_2 = -3$$

> [!info]- **Üçgen matrisin özdeğerleri neden köşegendir?**
> $\det(\lambda I - J) = (\lambda+2)(\lambda+3) = 0$ — alt sol eleman $0$ olduğundan determinant çarpanlara doğrudan ayrılır.

✅ Her iki özdeğer **negatif reel** → **Kararlı Düğüm** — yörüngeler bu noktaya yaklaşır.

---

#### (1, 0) noktası:

$$J_{(1,0)} = \begin{bmatrix} 2(1) & -1 \\ 0 & (1)-2 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ 0 & -1 \end{bmatrix}$$

$$\lambda_1 = 2,\quad \lambda_2 = -1$$

⚠️ Özdeğerler **zıt işaretli** → **Eyer Noktası (Saddle Point)** — bir yönde yaklaşır, diğer yönde uzaklaşır.

---

#### (2, 3) noktası:

$$J_{(2,3)} = \begin{bmatrix} 2(2) & -1 \\ 3 & (2)-2 \end{bmatrix} = \begin{bmatrix} 4 & -1 \\ 3 & 0 \end{bmatrix}$$

$$\det(\lambda I - J) = \lambda(\lambda-4) - (-1)(3) = \lambda^2 - 4\lambda + 3 = (\lambda-3)(\lambda-1) = 0$$
$$\lambda_1 = 3,\quad \lambda_2 = 1$$

> [!info]- **Bu özdeğer denklemi nasıl kuruldu?**
> $\det(\lambda I - J) = \det\begin{bmatrix}\lambda-4 & 1\\-3 & \lambda\end{bmatrix} = \lambda(\lambda-4)-1\cdot(-3) = \lambda^2-4\lambda+3$
> Kökler: $(\lambda-3)(\lambda-1)=0 \Rightarrow \lambda=3,\,1$

❌ Her iki özdeğer **pozitif** → **Kararsız Düğüm** — yörüngeler bu noktadan uzaklaşır.

---

### Faz Portresi Yorumu (3p)

| Denge Noktası | Özdeğerler | Tür | Davranış |
|---|---|---|---|
| $(-1,\,0)$ | $-2,\,-3$ | Kararlı düğüm | Yörüngeler bu noktaya yaklaşır |
| $(1,\,0)$ | $+2,\,-1$ | Eyer noktası | Bir yönde yaklaşır, diğerinde uzaklaşır |
| $(2,\,3)$ | $+3,\,+1$ | Kararsız düğüm | Yörüngeler bu noktadan uzaklaşır |

> [!info]- **Özdeğer işaret tablosu — özet**
> | Özdeğer durumu | Nokta tipi | Kararlı mı? |
> |---|---|---|
> | İkisi de negatif reel | Kararlı düğüm | ✅ Evet |
> | İkisi de pozitif reel | Kararsız düğüm | ❌ Hayır |
> | Zıt işaretli reel | Eyer noktası | ⚠️ Hayır |
> | Negatif reel + sanal | Kararlı sarmal | ✅ Evet |
> | Pozitif reel + sanal | Kararsız sarmal | ❌ Hayır |
> | Saf sanal | Merkez | ➰ Lyapunov kararlı |

---

## Soru 3 — Doğrusal Olmayan Elektrik Devresi: Doğrusallaştırma

**Verilen devre:** Gerilim kaynağı $u(t)$, $L=1\text{ H}$ endüktör, doğrusal olmayan direnç $V_r = 2i^2(t)$, DC kaynak $5\text{ V}$.

> [!note]- Semboller
> - $u(t)$: kaynak gerilimi — giriş (V); $i(t)$: akım (A)
> - $L=1$ H: indüktans; $V_r=2i^2$: doğrusal olmayan direnç gerilimi (V)
> - $i_0$: çalışma (denge) akımı; $\delta i$: küçük sapma
> - Taylor: $f(i)\approx f(i_0)+f'(i_0)\delta i$; $f'(i)=4i$ → dengede $4i_0$ eğimi
> - $\Delta I(s)$: $\delta i$'nin Laplace dönüşümü; $V_r(s)/U(s)$: aranan TF

> [!info]- **Doğrusallaştırma neden gerekli?**
> $V_r=2i^2$ doğrusal değil — $i$'nin karesi var. Laplace alınamaz, transfer fonksiyonu yazılamaz. Çözüm: **bir çalışma noktası seç, o noktanın küçük çevresinde sistemi lineer kabul et**. Bu küçük sapmalar için geçerli bir TF verir.

---

### 3a — Sistem Denklemi (5p)

Devrede KVL (gerilimler toplamı = 0):
$$u(t) - L\frac{di}{dt} - V_r + 5 = 0$$

$L=1$ ve $V_r=2i^2$ yerine:

$$\boxed{u(t) = \frac{di(t)}{dt} + 2i^2(t) - 5}$$

> [!info]- **KVL nasıl uygulandı?**
> Çevrim boyunca voltaj yükselişleri = voltaj düşüşleri:
> - $u(t)$: kaynak gerilimi (yükseliş)
> - $L\,di/dt$: endüktör gerilimi (düşüş)
> - $2i^2$: doğrusal olmayan direnç (düşüş)
> - $5\text{ V}$: DC kaynak (yükseliş → sağ tarafa taşınınca $-5$ olur)

---

### 3b — Çalışma Noktası (5p)

DC kararlı durumda: $\dot{i}=0$ (akım değişmiyor), $u(t)=0$ (giriş yok):
$$0 = 0 + 2i_0^2 - 5 \Rightarrow i_0^2 = 2{,}5 \Rightarrow \boxed{i_0 = \sqrt{2{,}5} \approx 1{,}58\text{ A}}$$

> [!info]- **Çalışma noktası neden bu koşullarda bulunur?**
> "DC kararlı durum" = sistem uzun süre çalıştıktan sonra değişkenlerin sabit kaldığı an.
> - $\dot{i}=0$: akım artık değişmiyor → türevi sıfır
> - $u=0$: denge, girişin olmadığı doğal konumu
>
> Bu koşullar altında denklem sadece $i_0$'a bağlı kalır ve çözülür.

---

### 3c — Taylor Serisi ile Doğrusallaştırma (5p)

$i(t) = i_0 + \delta i(t)$ yaz ($i_0$ sabit çalışma noktası, $\delta i$ küçük sapma):

$f(i) = 2i^2$ için Taylor açılımı (sadece 1. derecede kes):
$$f(i_0+\delta i) \approx f(i_0) + f'(i_0)\cdot\delta i = 2i_0^2 + 4i_0\cdot\delta i = 5 + 4(1{,}58)\,\delta i = 5 + 6{,}32\,\delta i$$

> [!info]- **Taylor serisi burada nasıl çalışıyor?**
> $f(x) \approx f(x_0) + f'(x_0)(x-x_0)$ — fonksiyonun $x_0$ etrafındaki teğet çizgisi.
> $f(i)=2i^2$ → $f'(i)=4i$ → $f'(i_0)=4\times1{,}58=6{,}32$
> $f(i_0)=2\times(1{,}58)^2=5$ (zaten denge koşulundan biliyorduk)
> Büyük sapmalarda bu yaklaşım bozulur; küçük $\delta i$ için geçerlidir.

$i=i_0+\delta i$ ana denkleme koy:
$$u(t) = \frac{d(i_0+\delta i)}{dt} + (5 + 6{,}32\,\delta i) - 5$$

$i_0$ sabit → $di_0/dt=0$, $5-5$ iptal:
$$\boxed{u(t) = \frac{d(\delta i)}{dt} + 6{,}32\,\delta i(t)}$$

Bu artık **lineer** bir denklem — Laplace alınabilir.

---

### 3d — Laplace Dönüşümü ve Transfer Fonksiyonu (5p + 5p)

Laplace al (sıfır başlangıç koşulu):
$$U(s) = s\,\Delta I(s) + 6{,}32\,\Delta I(s) = \Delta I(s)(s + 6{,}32)$$

$$\boxed{\Delta I(s) = \frac{U(s)}{s + 6{,}32}}$$

Direnç gerilimine çevir: $V_r = 2i^2$, doğrusallaştırılmış hali $\delta V_r = 4i_0\cdot\delta i = 6{,}32\,\delta i$

$$V_r(s) = 6{,}32\,\Delta I(s) = 6{,}32 \cdot \frac{U(s)}{s+6{,}32}$$

$$\boxed{\frac{V_r(s)}{U(s)} = \frac{6{,}32}{s + 6{,}32}}$$

> [!info]- **Bu transfer fonksiyonu hangi sisteme benziyor?**
> $\frac{K}{s+a}$ formu → **birinci dereceden sistem** (tek kutuplu, $s=-6{,}32$).
> - Zaman sabiti: $\tau = 1/6{,}32 \approx 0{,}158$ s
> - Basamak yanıtı: $v_r(t) = (1-e^{-6{,}32t})u(t)$ (doğrusallaştırılmış)
> - DC kazancı: $V_r/U\big|_{s=0} = 6{,}32/6{,}32 = 1$

---

## Soru 4 — Yay-Kütle Sistemi: Faz Portresi

**Verilen:** $k=1$, $m=1$, sönümsüz yay-kütle sistemi.

> [!note]- Semboller
> - $k=1$: yay sabiti (N/m); $m=1$: kütle (kg); sönüm yok
> - $x_1=x$: konum, $x_2=\dot x$: hız durumları
> - $\lambda$: özdeğer; saf sanal ($\pm j$) → **Merkez** (center)
> - $A,B$: başlangıç koşullarından gelen sabitler; $r=\sqrt{A^2+B^2}$: yörünge yarıçapı
> - Faz portresi: $x_1^2+x_2^2=r^2$ → iç içe daireler (enerji korunur, Lyapunov kararlı)

> [!info]- **Faz portresi nedir?**
> Sistemin zamanı dışarıda bırakarak **konum ($x_1$) ve hız ($x_2$) düzlemindeki yörüngesini** gösterir. Her başlangıç koşulu farklı bir yörünge çizer. Sistemin genel davranışı tek grafikte görülür.

---

### 4a — Hareket Denklemi (5p)

Newton 2. yasası ($F=ma$, yay kuvveti geri yükleyen):
$$-kx = m\ddot{x} \Rightarrow m\ddot{x} + kx = 0$$

$k=m=1$:
$$\boxed{\ddot{x} + x = 0}$$

> [!info]- **Neden $-kx$?**
> Yay, kütleyi her zaman denge konumuna (orijine) doğru iter. Kütle sağa giderse ($x>0$) kuvvet sola ($F<0$), sola giderse kuvvet sağa. Yani $F=-kx$ — geri yükleyen (restoring) kuvvet.

---

### 4b — Özdeğerler (5p)

$x(t)=e^{\lambda t}$ çözüm biçimini varsay, denkleme koy:
$$\lambda^2 e^{\lambda t} + e^{\lambda t} = 0 \Rightarrow e^{\lambda t}(\lambda^2 + 1) = 0$$

$e^{\lambda t} \neq 0$ olduğundan:
$$\lambda^2 + 1 = 0 \Rightarrow \lambda^2 = -1 \Rightarrow \boxed{\lambda = \pm j}$$

Saf sanal özdeğerler → **Merkez noktası (Center)**

> [!info]- **$\lambda=\pm j$ ne anlama geliyor?**
> $e^{jt} = \cos t + j\sin t$ — sönümsüz salınım. Ne sönüyor ne büyüyor, sonsuza kadar devam ediyor.
>
> | Özdeğer | Yanıt |
> |---|---|
> | $\lambda = -a \pm j\omega$ ($a>0$) | Sönümlü salınım (spiral içe) |
> | $\lambda = \pm j\omega$ | Sonsuz salınım (merkez, daire) |
> | $\lambda = +a \pm j\omega$ ($a>0$) | Büyüyen salınım (spiral dışa) |

---

### 4c — Genel Çözüm (3p + 2p)

$\lambda = \pm j$ → $e^{jt}$ ve $e^{-jt}$ → Euler ile $\sin$ ve $\cos$:
$$x_1(t) = A\sin t + B\cos t$$

Hız (türev):
$$x_2(t) = \dot{x}_1 = A\cos t - B\sin t$$

> [!info]- **$A$ ve $B$ nasıl belirlenir?**
> Başlangıç koşullarından: $x_1(0) = B$ → $B = x(0)$; $x_2(0) = A$ → $A = \dot{x}(0)$.
> Her farklı başlangıç koşulu farklı bir $(A,B)$ çifti verir → farklı bir yörünge büyüklüğü $r=\sqrt{A^2+B^2}$.

---

### 4d — Faz Portresi (5p)

$x_1^2 + x_2^2$ hesapla:
$$x_1^2 + x_2^2 = (A\sin t + B\cos t)^2 + (A\cos t - B\sin t)^2$$
$$= A^2\sin^2t + 2AB\sin t\cos t + B^2\cos^2 t + A^2\cos^2 t - 2AB\cos t\sin t + B^2\sin^2 t$$
$$= A^2(\sin^2 t + \cos^2 t) + B^2(\cos^2 t + \sin^2 t) = A^2 + B^2$$

$$\boxed{x_1^2 + x_2^2 = A^2 + B^2 = r^2 = \text{sabit}}$$

> [!info]- **Bu neden daire?**
> $x_1^2+x_2^2=r^2$ bir dairenin denklemi! Sistem konum-hız düzleminde dairesel yörünge çiziyor. $r$ başlangıç koşuluna göre belirleniyor; farklı başlangıçlar → farklı yarıçaplarda iç içe daireler.
>
> Fiziksel yorum: **Enerji korunur**. $E = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}kx^2 = \frac{1}{2}(x_2^2+x_1^2) = \frac{r^2}{2}$ = sabit.

→ Faz düzleminde **iç içe daireler** — sistem ne kararlı ne kararsız, **Lyapunov anlamında kararlı**.

![[mst06-faz-portresi.png]]

> [!note]- Python kaynağı — `_assets/scripts/mst06-faz-portresi.py`
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
>
> th = np.linspace(0, 2*np.pi, 400)
> renkler = ["#2980b9", "#27ae60", "#e67e22", "#c0392b", "#8e44ad"]
> fig, ax = plt.subplots(figsize=(5, 5))
> for r, c in zip([1, 2, 3, 4, 4.7], renkler):
>     ax.plot(r*np.cos(th), r*np.sin(th), color=c, lw=1.8)
> ax.set_aspect("equal"); ax.axhline(0, color="#1a1a2e", lw=0.8); ax.axvline(0, color="#1a1a2e", lw=0.8)
> plt.show()   # iç içe daireler → Lyapunov anlamında kararlı
> ```

**Yorum:** Başlangıç koşulları ($A$, $B$) yarıçapı belirler. Sistem sonsuza kadar salınım yapar, enerji korunur, yörüngeler kapalı.
