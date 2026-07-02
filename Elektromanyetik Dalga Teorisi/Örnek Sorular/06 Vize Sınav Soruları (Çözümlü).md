---
tags: [emd, vize, sınav-soruları, çözümlü, faraday, maxwell, düzlem-dalga, dalga-denklemi, sınır-koşulları]
---

# 06 — Vize Sınav Soruları (Çözümlü · Sıfırdan Öğretici)

← [[EMD Ana Sayfa]]

> Kaynak: `Masaüstü/EMD Vize.jpeg`

> [!abstract] Bu sınav neyi ölçüyor? (önce büyük resim)
> Vize **elektromanyetik temeller** ağırlıklı: Faraday indüksiyon (S1) + Maxwell denklemleri integral form (S2) + düzlem dalga H ve β (S3) + skaler potansiyel dalga denklemi türetme (S4) + sınır koşulları (S5). Tüm sorular **4 Maxwell denkleminden** türer — bunları ezberlemek değil, her birinin fiziksel kökenini anlamak yeterli.
>
> | Sembol | Açılım |
> |---|---|
> | **EMF** | Elektromotor kuvvet — indüklenen gerilim (V) |
> | **Φ** | Manyetik akı (Wb) |
> | **β** | Faz sabiti (rad/m); $\beta = \omega\sqrt{\mu\varepsilon}$ |
> | **η** | Öz empedans — dalganın "direnci" (Ω) |
> | **v_p** | Faz hızı $= \omega/\beta = c/\sqrt{\mu_r\varepsilon_r}$ (m/s) |
> | **∇×E** | E alanının rotasyonu (curl); Faraday diferansiyel formu |
> | **J_s** | Yüzey akım yoğunluğu (A/m); **ρ_s** = yüzey yük yoğunluğu (C/m²) |

---

## Soru 1 — Faraday İndüksiyon · Sabit Çubuk (20p)

**Verilen:**
$$\mathbf{B} = \hat{a}_z \cdot 30\sin(10^4 t)\,\text{T}$$

- İletken çubuk: y eksenine paralel, **x = 5 cm'de sabit duruyor**
- Ray çifti: x ekseni boyunca; a (üst) ve b (alt) uçları arası **3 cm**
- Devre: 5 cm × 3 cm dikdörtgen (x: 0 → 5 cm, y: 0 → 3 cm)

**Devre şeması:**

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[scale=3.2, font=\small]

  % Eksenler
  \draw[-{Stealth}] (-0.15,0) -- (2.1,0) node[right] {$x$};
  \draw[-{Stealth}] (0,-0.15) -- (0,1.3) node[above] {$y$};
  \node[below left] at (0,0) {$0$};

  % Alt ray (y=0, x: 0 → 1.6)
  \draw[thick] (0,0) -- (1.6,0);
  % Üst ray (y=1.0 ≡ 3 cm, x: 0 → 1.6)
  \draw[thick] (0,1.0) -- (1.6,1.0);
  % Sol bağlantı (x=0, y ekseni boyunca)
  \draw[thick] (0,0) -- (0,1.0);
  % İletken çubuk (x=1.6 ≡ 5 cm, kalın)
  \draw[line width=2.5pt] (1.6,0) -- (1.6,1.0);

  % B alanı nokta sembolleri (sayfadan dışarı çıkıyor, ⊙)
  \foreach \xi in {0.28, 0.65, 1.02, 1.38} {
    \foreach \yi in {0.22, 0.55, 0.82} {
      \draw (\xi,\yi) circle (0.07);
      \fill (\xi,\yi) circle (0.02);
    }
  }

  % B etiketi (orta)
  \node at (0.80, 0.50) [above=0.35cm, font=\footnotesize] {$\mathbf{B}$};

  % 3 cm ölçü oku (sol taraf)
  \draw[|<->|] (-0.28,0) -- (-0.28,1.0) node[midway, left] {$3\,\text{cm}$};

  % a ve b etiketleri (çubuğun sol kenarı)
  \node[left, font=\normalsize\bfseries] at (1.6,1.0) {$a$};
  \node[left, font=\normalsize\bfseries] at (1.6,0.0) {$b$};

  % x=5 cm kesik çizgi + etiket
  \draw[dashed, thin, gray] (1.6,-0.05) -- (1.6,-0.2);
  \node[below] at (1.6,-0.18) {$x=5\,\text{cm}$};

  % İletken çubuk etiketi (sağ)
  \node[right] at (1.65,0.50) {\textbf{İletken çubuk}};

\end{tikzpicture}
\end{document}
```

> [!question] 📝 Soru metni (sınavda sorulan)
> Yandaki şekilden görüldüğü üzere y eksenine paralel bir iletken çubuk $\mathbf{B} = \hat{a}_z 30\sin(10^4t)$ T ile verilen manyetik alanı içinde yer alan iletken ray çifti üzerinde x = 5 cm konumunda **durmaktadır**. Buna göre a ve b uçları arasında indüklenen gerilimi bulunuz. **(20p)**

> [!note]- Semboller
> - $\hat{a}_z$: z-yönü birim vektörü; B z-yönünde (sayfadan dışarı, ⊙ sembolleri)
> - $\Phi = \iint \mathbf{B}\cdot d\mathbf{S}$: kapalı devreden geçen manyetik akı (Wb)
> - EMF $= -d\Phi/dt$: Faraday kanunu (negatif işaret: Lenz kuralı)
> - Çubuk **sabit** durduğundan (v = 0): hareket EMF'si = 0; sadece zamana bağlı B → "dönüşüm EMF'si" doğar

---

### Çözüm

**Adım 1 — Yüzey alanı:**

Devre dikdörtgeni: $x \in [0,\,0.05\text{ m}]$, $y \in [0,\,0.03\text{ m}]$

$$A = 0.05 \times 0.03 = 1.5 \times 10^{-3}\,\text{m}^2$$

**Adım 2 — Manyetik akı (tam yüzey integrali):**

Akının **tanımı** her zaman bir yüzey integralidir, hiçbir zaman doğrudan çarpımla başlamaz:

$$\Phi = \iint_S \mathbf{B}\cdot d\mathbf{S}$$

Devre düzlemi sabit $xy$-düzleminde olduğundan yüzey elemanı $d\mathbf S = dA\,\hat a_z$ seçilir (B ile aynı yönde, dışarı doğru). Bu integralin **tek bir çarpıma** indirgenmesi için iki ayrı koşulun **aynı anda** sağlanması gerekir:

1. **B**, yüzey üzerindeki konuma ($x,y$) bağlı değil — yalnızca zamana bağlı: $\mathbf B(t)=\hat a_z\,30\sin(10^4t)$. O yüzden integralin dışına **sabit gibi** çıkarılabilir.
2. **B** tamamen $\hat a_z$ yönünde ve seçilen $d\mathbf S$ de $\hat a_z$ yönünde → aralarındaki açı $0°$, $\mathbf B\cdot d\mathbf S = B(t)\cos0°\,dA = B(t)\,dA$.

Bu iki koşul birlikte sağlandığından:

$$\Phi = \iint_S \mathbf{B}\cdot d\mathbf{S} = \iint_S B(t)\,dA = B(t)\underbrace{\iint_S dA}_{=\,A} = B(t)\cdot A$$

Sayısal olarak:
$$\Phi = 30\sin(10^4t) \times 1.5\times10^{-3}$$

$$\boxed{\Phi = 0.045\sin(10^4t)\,\text{Wb}}$$

> [!warning] Bu sadeleşme her zaman bu kadar kolay değil — sınavda ayrı puan
> Eğer **B** yüzey üzerinde konuma göre değişseydi (ör. $B(x)$, homojen değil) **ya da** devre düzlemine **açılı** olsaydı (normal ile B arasında $\theta\neq0$), gerçek bir $\iint_S B(x,y)\cos\theta\,dA$ hesabı gerekirdi. Burada $\Phi=\mathbf B\cdot A$ yazabilmemizin sebebi, "B homojen" **ve** "B $\parallel$ yüzey normali" koşullarının **ikisinin birden** doğru olması — hoca bu gerekçeyi (adım 2'nin kendisini) ayrı puanla değerlendirebilir, sonucu yazmak tek başına yeterli sayılmayabilir.

**Adım 3 — Faraday kanunu:**

$$\text{EMF} = -\frac{d\Phi}{dt} = -0.045 \times 10^4\,\cos(10^4t)$$

$$\boxed{V_{ab} = -450\cos(10^4t)\,\text{V}}$$

> [!tip] Fiziksel yorum
> Genlik 450 V, frekans $f = 10^4/(2\pi) \approx 1592\,\text{Hz}$. Çubuk sabit olduğu için motörsel EMF yoktur; tüm gerilim zamana bağlı **B**'den kaynaklanır (Faraday → dönüşüm EMF'si). Lenz kuralına göre negatif işaret, indüklenen akımın değişen akıya karşı koyacağı yönde olduğunu gösterir.

---

## Soru 2 — Maxwell Denklemleri İntegral Biçim (20p)

> [!question] 📝 Soru metni (sınavda sorulan)
> Maxwell Denklemlerinin integral biçimlerini yazınız ve her bir denklemi uygun deneysel yasa ile tanımlayınız. **(20p)**

> [!note]- Semboller
> - $\oint_S$: Kapalı yüzey integrali; $\oint_C$: Kapalı çizgi (kontur) integrali
> - $Q_{enc}$: Kapalı yüzey içindeki toplam serbest yük (C)
> - $\rho_v$: Hacimsel yük yoğunluğu (C/m³)
> - $\mathbf{D} = \varepsilon\mathbf{E}$: Elektrik akı yoğunluğu; $\mathbf{B} = \mu\mathbf{H}$: Manyetik akı yoğunluğu

---

### 4 Maxwell Denklemi — İntegral Form

**Denklem 1 — Gauss Kanunu (Elektrik):**

$$\oint_S \mathbf{D}\cdot d\mathbf{S} = Q_{enc} = \int_V \rho_v\,dV$$

Kapalı yüzeyden çıkan toplam elektrik akısı = yüzey içindeki serbest yük. Pozitif yükler **D** alanının "kaynağı", negatifler "lavabosu"dur.

> **Deneysel yasa:** **Coulomb Yasası** (Charles-Augustin de Coulomb, 1785). Coulomb, burulma terazisiyle iki nokta yük arasındaki kuvveti ölçüp $F\propto q_1q_2/r^2$ (ters-kare) bağıntısını deneysel olarak buldu. Gauss, bu ters-kare kuvvet alanını **herhangi bir kapalı yüzeye** genelleştirerek (küre, küp, keyfi şekil — hepsinde aynı toplam akı) matematiksel Gauss Kanunu'nu elde etti; yani denklem 1, Coulomb'un ölçtüğü kuvvet yasasının integral/akı diliyle yeniden ifadesidir.

---

**Denklem 2 — Gauss Kanunu (Manyetik):**

$$\oint_S \mathbf{B}\cdot d\mathbf{S} = 0$$

Herhangi kapalı yüzeyden net manyetik akı sıfırdır. Manyetik alan çizgileri her zaman kapalıdır; izole manyetik monopol (tek kutup) gözlemlenmemiştir.

> **Deneysel yasa:** **Manyetik monopolün yokluğu** (deneysel gözlem, formal "kanun adı" yok — bazen "Gauss'un Manyetizma Yasası" denir). Bir çubuk mıknatısı ne kadar bölerseniz bölün, her parça yine bir N-S çifti olarak çıkar; hiçbir deneyde tek başına N veya tek başına S kutbu (monopol) izole edilememiştir. Bu evrensel deneysel gözlem, manyetik alan çizgilerinin **daima kapalı halkalar** oluşturduğu (kaynağı/lavabosu olmadığı) sonucuna götürür — denklem 2 bunun matematiksel ifadesidir.

---

**Denklem 3 — Faraday İndüksiyon Kanunu:**

$$\oint_C \mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{S}$$

Değişen manyetik akı, kapalı çevrim boyunca EMF (elektromotor kuvvet) indükler. Transformatörler ve jeneratörler bu denkleme dayanır.

> **Deneysel yasa:** **Faraday'ın İndüksiyon Yasası** (Michael Faraday, 1831). Faraday, bir bobine mıknatısı yaklaştırıp-uzaklaştırdığında veya komşu bir bobindeki akımı açıp-kapattığında, ikinci bobinde (fiziksel temas olmadan) bir akımın indüklendiğini galvanometreyle gözlemledi. Deneysel bulgu: indüklenen EMF, çevrimden geçen manyetik akının **değişim hızıyla** orantılıdır — negatif işaret (Lenz Kuralı, Heinrich Lenz 1834) indüklenen akımın kendini oluşturan değişime **karşı koyacak** yönde olduğunu belirtir.

---

**Denklem 4 — Ampere-Maxwell Kanunu:**

$$\oint_C \mathbf{H}\cdot d\mathbf{l} = \int_S \mathbf{J}\cdot d\mathbf{S} + \frac{d}{dt}\int_S \mathbf{D}\cdot d\mathbf{S}$$

İletim akımı (**J**) ve değişen elektrik akısı (yer değiştirme akımı $\partial\mathbf{D}/\partial t$) manyetik alan oluşturur. Maxwell'in eklediği $\partial\mathbf{D}/\partial t$ terimi, EM dalgaların var olmasını öngörür.

> **Deneysel yasa — iki ayrı köken:** (1) **Oersted'in gözlemi** (Hans Christian Ørsted, 1820): akım taşıyan bir telin yakınındaki pusula iğnesinin saptığını fark etti — akımın manyetik alan yarattığının ilk deneysel kanıtı. **Ampère** (1820'ler) bunu iki paralel akımlı tel arasındaki kuvveti ölçerek niceliksel hale getirdi → klasik **Ampère Devre Yasası** ($\oint\mathbf H\cdot d\mathbf l=I_{enc}$, yalnız $\mathbf J$ terimi). (2) $\partial\mathbf D/\partial t$ (**yer değiştirme akımı**) terimi ise bir deneyden değil, **Maxwell'in (1861-62) teorik tutarlılık düzeltmesinden** gelir: şarj olan bir kapasitörün plakaları arasında iletim akımı ($\mathbf J$) yokken bile devrenin geri kalanında akım aktığından, orijinal Ampère yasası süreklilik denklemiyle çelişiyordu. Maxwell bu tutarsızlığı gidermek için $\partial\mathbf D/\partial t$ terimini **ekledi** — bu terim daha sonra Hertz'in (1887) elektromanyetik dalgaları deneysel olarak üretip algılamasıyla doğrulandı.

---

### Özet Tablo

| #   | Diferansiyel                                                      | İntegral                                                | Deneysel Yasa                               | Deney/Gözlem                                                                     | Kim / Ne zaman                                   |
| --- | ----------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------ |
| 1   | $\nabla\cdot\mathbf{D}=\rho_v$                                    | $\oint_S\mathbf{D}\cdot d\mathbf{S}=Q_{enc}$            | Coulomb Yasası                              | Burulma terazisiyle ölçülen $1/r^2$ kuvvet yasası                                | Coulomb, 1785                                    |
| 2   | $\nabla\cdot\mathbf{B}=0$                                         | $\oint_S\mathbf{B}\cdot d\mathbf{S}=0$                  | Manyetik monopol yokluğu                    | Mıknatıs bölünse de her zaman N-S çifti çıkar                                    | (sürekli deneysel gözlem)                        |
| 3   | $\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t$           | $\oint_C\mathbf{E}\cdot d\mathbf{l}=-d\Phi_B/dt$        | Faraday İndüksiyon Yasası                   | Hareketli mıknatıs/bobinle indüklenen akımın galvanometreyle gözlenmesi          | Faraday, 1831                                    |
| 4   | $\nabla\times\mathbf{H}=\mathbf{J}+\partial\mathbf{D}/\partial t$ | $\oint_C\mathbf{H}\cdot d\mathbf{l}=I_{enc}+d\Phi_D/dt$ | Ampère Devre Yasası + Maxwell'in düzeltmesi | Akımlı telin pusulayı saptırması; kapasitör süreklilik paradoksu (teorik ekleme) | Oersted 1820 / Ampère 1820'ler / Maxwell 1861-62 |

---

## Soru 3 — Düzlem Dalga: H Alanı ve β (20p)

**Verilen:**
- Yapısal parametreler: $\varepsilon_r = 4,\;\mu_r = 1,\;\sigma = 0\,\text{S/m}$ → kayıpsız dielektrik
- Elektrik alanı: $\mathbf{E}(z,t) = \hat{a}_x\cdot120\cos(9\pi\times10^8 t - \beta z)\,\text{V/m}$

> [!question] 📝 Soru metni (sınavda sorulan)
> Yapısal parametreleri $\varepsilon_r = 4$, $\mu_r = 1$ ve $\sigma = 0$ S/m olarak verilen bir dielektrik ortamda yayılmakta olan elektromanyetik dalganın elektrik alanı $\overline{E}(z,t) = \hat{a}_x\cdot120\cos(9\pi\times10^8 t - \beta z)$ V/m olarak verilmektedir. Buna göre ilgili manyetik alanın anlık ifadesini ve β değerini hesaplayınız. **(20p)**

> [!note]- Semboller (hızlı bakış)
> - $\omega = 9\pi\times10^8$ rad/s (açısal frekans); $c = 3\times10^8$ m/s (boşlukta ışık hızı)
> - Kayıpsız ortam: $\alpha=0$ (sönüm sabiti sıfır), $\beta = \omega\sqrt{\mu\varepsilon} = (\omega/c)\sqrt{\mu_r\varepsilon_r}$ (faz sabiti)
> - $\eta = \sqrt{\mu/\varepsilon} = \eta_0/\sqrt{\varepsilon_r}$ (öz empedans); $\eta_0 = 120\pi\approx377\,\Omega$ (boşluk değeri)
> - Düzlem dalga ilişkisi: $\mathbf{H} = \frac{1}{\eta}(\hat{a}_k\times\mathbf{E})$; yayılma yönü × E → H yönü (sağ el kuralı)

---

### Çözüm

**Adım 0 — Verilen dalga ifadesini ve ortam sabitlerini oku:**

$$\mathbf E(z,t)=\hat a_x\cdot120\cos(9\pi\times10^8\,t-\beta z)$$

Bu bir **düzlem dalga**dır — tek bir eksen boyunca (burada $z$) ilerleyen, o eksene dik düzlemin (xy) her noktasında aynı değeri alan bir dalga. Parça parça:
- **$120$**: E'nin genliği (V/m).
- **$\hat a_x$**: E'nin salındığı yön (**polarizasyon**) — burada x ekseni.
- **$9\pi\times10^8$**: bu $\omega$, **açısal frekans** (rad/s) — E'nin **zamanda** ne hızla salındığı ($\omega=2\pi f$).
- **$\beta$** (bilinmeyen, bulunacak): **faz sabiti** (rad/m) — E'nin **uzayda** ne hızla faz değiştirdiği ($\beta=2\pi/\lambda$).
- **$(\omega t-\beta z)$**: dalganın **fazı**. Bu ifade sabit kalacak şekilde $t$ artarken $z$ de artmalı (çünkü $-\beta z$, $\omega t$'yi dengeliyor) → dalga **$+z$ yönünde** ilerliyor. Fazın ilerleme hızına **faz hızı $v_p=dz/dt=\omega/\beta$** denir.

Ortamı tanımlayan sabitler:
- **$\varepsilon_r=4$** (bağıl elektrik geçirgenliği): ortamın elektrik alana tepkisini boşluğa göre kaç kat büyüttüğü (boyutsuz); gerçek değer $\varepsilon=\varepsilon_r\varepsilon_0$.
- **$\mu_r=1$** (bağıl manyetik geçirgenlik): aynı mantık, manyetik alan için — burada boşlukla aynı ($1$), yani ortam manyetik açıdan "sıradan".
- **$\sigma=0$** (iletkenlik, S/m): ortam akımı iletmiyor → **kayıpsız**: dalga sönümlenmeden, genliği sabit kalarak ilerler. ($\sigma\neq0$ olsaydı genlik $z$ arttıkça üstel azalırdı.)

**İstenen:** $\beta$ ve $\mathbf H(z,t)$.

---

### 3a — Faz Sabiti β

Önce **faz hızını** bul: boşlukta ışık hızı $c=1/\sqrt{\mu_0\varepsilon_0}$ idi; bir ortamda aynı formül gerçek $\mu,\varepsilon$ ile yazılır:
$$v_p=\frac{1}{\sqrt{\mu\varepsilon}}=\frac{1}{\sqrt{\mu_r\mu_0\,\varepsilon_r\varepsilon_0}}=\frac{c}{\sqrt{\mu_r\varepsilon_r}}$$
($\sqrt{\mu_r\varepsilon_r}$ dalgayı boşluğa göre kaç kat yavaşlattığını gösteriyor — burada $\sqrt4=2$ kat.)

$$v_p = \frac{c}{\sqrt{\mu_r\varepsilon_r}} = \frac{3\times10^8}{\sqrt{1\times4}} = 1.5\times10^8\,\text{m/s}\;(=c/2)$$

Şimdi Adım 0'da tanımlanan $v_p=\omega/\beta$ ilişkisini $\beta$ için çöz:
$$\beta = \frac{\omega}{v_p} = \frac{9\pi\times10^8}{1.5\times10^8}$$

$$\boxed{\beta = 6\pi \approx 18.85\,\text{rad/m}}$$

### 3b — Öz Empedans η

$\eta$ (**öz empedans / dalga empedansı**, Ω), ortamın dalgaya gösterdiği "direnç"tir — devre teorisindeki $R=V/I$'nin dalga karşılığı: $\eta=E_0/H_0$ (E genliğinin H genliğine oranı). Genel formül $\eta=\sqrt{\mu/\varepsilon}$; boşluk değeri $\eta_0=\sqrt{\mu_0/\varepsilon_0}=120\pi\approx377\,\Omega$'dur. Ortamda:
$$\eta=\eta_0\sqrt{\frac{\mu_r}{\varepsilon_r}}\xrightarrow{\mu_r=1}\eta=\frac{\eta_0}{\sqrt{\varepsilon_r}}$$

$$\eta = \frac{\eta_0}{\sqrt{\varepsilon_r}} = \frac{120\pi}{\sqrt{4}} = \frac{120\pi}{2} = 60\pi \approx 188.5\,\Omega$$

### 3c — H Alanının Anlık İfadesi

**Yön mantığı:** Düzlem dalgada **E, H ve yayılma yönü $\hat a_k$ birbirine diktir** — üçü $x,y,z$ eksenleri gibi bir sağ-el üçlüsü oluşturur. Önce yayılma yönünü bul: $\mathbf E$'nin argümanı $(\omega t-\beta z)$ biçiminde — argümandaki işaret **eksi** olduğundan dalga $+z$ yönünde ilerliyor (eğer $+\beta z$ olsaydı $-z$ yönü olurdu, Adım 0'da açıklandığı gibi). O yüzden $\hat a_k=\hat a_z$. H'nin yönü, sağ el kuralıyla $\hat a_k\times\hat a_x$ çapraz çarpımından çıkar:
3
$$\hat{a}_z \times \hat{a}_x = \hat{a}_y$$

**Genlik mantığı:** $\eta=E_0/H_0$ tanımından $H_0=E_0/\eta$ (empedans E'yi H'ye çevirir — $I=V/R$'nin dalga karşılığı). Yön ve genliği düzlem dalga formülünde birleştir: 

$$\mathbf H = \dfrac1\eta(\hat a_k\times\mathbf E) \Rightarrow H_0=E_0/\eta,\;$$

yön $\hat a_y$.

$$\mathbf{H}(z,t) = \frac{E_0}{\eta}\,\hat{a}_y\,\cos(\omega t - \beta z) = \frac{120}{60\pi}\,\hat{a}_y\,\cos(9\pi\times10^8 t - 6\pi z)$$

$$\boxed{\mathbf{H}(z,t) = \frac{2}{\pi}\,\hat{a}_y\,\cos(9\pi\times10^8 t - 6\pi z) \approx 0.637\,\hat{a}_y\,\cos(9\pi\times10^8 t - 6\pi z)\,\text{A/m}}$$

> [!warning] Neden argüman ($\omega t-\beta z$) aynen korunuyor? — genel durumda korunmaz
> $\mathbf H$'nin **fazı** E ile birebir aynı kaldı (aynı $\cos(\omega t-\beta z)$), çünkü ortam **kayıpsız** ($\sigma=0$) → $\eta=\eta_0/\sqrt{\varepsilon_r}$ **tamamen reel** bir sayı (faz açısı $0°$). Eğer $\sigma\neq0$ olsaydı $\eta=|\eta|\angle\theta_\eta$ **karmaşık** çıkardı ve $\mathbf H$'nin fazı E'ninkinden $\theta_\eta$ kadar **kayardı**: $\mathbf H(z,t)=\frac{E_0}{|\eta|}\hat a_y\cos(\omega t-\beta z-\theta_\eta)$. Bu adımı atlayıp doğrudan "aynı argüman" yazmak, örtük olarak "$\eta$ reel" varsayımını kullanıyor — sınavda bu gerekçeyi (kayıpsız ⇒ reel η ⇒ fazlar aynı) yazmak ayrı puan getirir.

### Özet Tablosu

| Büyüklük | Değer |
|---|---|
| $\omega$ | $9\pi\times10^8$ rad/s |
| $\beta$ | $6\pi \approx 18.85$ rad/m |
| $\lambda = 2\pi/\beta$ | $1/3\,\text{m} \approx 33.3\,\text{cm}$ |
| $v_p$ | $1.5\times10^8$ m/s $= c/2$ |
| $\eta$ | $60\pi \approx 188.5\,\Omega$ |
| $\|H_0\|$ | $2/\pi \approx 0.637$ A/m |

---

## Soru 4 — V Skaler Potansiyeli için Dalga Denklemi Türetimi (20p)

**Verilen:**
- İletken olmayan ortam: $\sigma = 0$
- Kaynaklar mevcut: $\rho_v \neq 0$
- Basit ortam: lineer, izotropik, homojen

> [!question] 📝 Soru metni (sınavda sorulan)
> İletken olmayan, kaynakların bulunduğu basit bir ortamda V skaler elektrik potansiyeli için dalga denklemini elde ediniz. **(20p)**

> [!note]- Semboller
> - $V$: skaler elektrik potansiyeli (V)
> - $\mathbf{A}$: vektör manyetik potansiyel (Wb/m)
> - **Lorenz ölçümü:** $\nabla\cdot\mathbf{A} = -\mu\varepsilon\,\partial V/\partial t$ — denklemleri birbirinden ayırır
> - $\nabla^2 V$: V'nin Laplacian'ı; $\nabla^2 V = \partial^2V/\partial x^2 + \partial^2V/\partial y^2 + \partial^2V/\partial z^2$

---

### Türetim Adımları

**Adım 1 — Potansiyel tanımları:**

$$\mathbf{E} = -\nabla V - \frac{\partial\mathbf{A}}{\partial t}, \qquad \mathbf{B} = \nabla\times\mathbf{A}$$

**Adım 2 — Gauss-Elektrik yasasını uygula:**

$$\nabla\cdot\mathbf{D} = \rho_v \implies \nabla\cdot\mathbf{E} = \frac{\rho_v}{\varepsilon}$$

E tanımını koy:

$$\nabla\cdot\!\left(-\nabla V - \frac{\partial\mathbf{A}}{\partial t}\right) = \frac{\rho_v}{\varepsilon}$$

$$-\nabla^2 V - \frac{\partial}{\partial t}(\nabla\cdot\mathbf{A}) = \frac{\rho_v}{\varepsilon} \qquad\cdots(*)$$

> [!warning] Gizli varsayım: $\nabla\cdot(\partial\mathbf A/\partial t) = \partial(\nabla\cdot\mathbf A)/\partial t$
> Yukarıdaki satırda uzaysal türev ($\nabla\cdot$) ile zaman türevi ($\partial/\partial t$) **yer değiştirdi**. Bu, alanların yeterince düzgün (sürekli, iki kez türevlenebilir) olduğu varsayımıyla geçerlidir (karışık kısmi türevlerin sırası önemsiz — Schwarz/Clairaut teoremi). Fizik derslerinde genelde otomatik kabul edilir ama adımın kendisi bu yüzden " $=$ " değil, örtük bir varsayıma dayanıyor; sınavda bu geçişi belirtmek istersen tek cümle yeterli.

**Adım 3 — Lorenz ölçümünü uygula:**

$$\nabla\cdot\mathbf{A} = -\mu\varepsilon\frac{\partial V}{\partial t}$$

Bunu $(\ast)$'e koy:

$$-\nabla^2 V - \frac{\partial}{\partial t}\!\left(-\mu\varepsilon\frac{\partial V}{\partial t}\right) = \frac{\rho_v}{\varepsilon}$$

$$-\nabla^2 V + \mu\varepsilon\frac{\partial^2 V}{\partial t^2} = \frac{\rho_v}{\varepsilon}$$

$$\boxed{\nabla^2 V - \mu\varepsilon\frac{\partial^2 V}{\partial t^2} = -\frac{\rho_v}{\varepsilon}}$$

> [!info] Fiziksel anlam
> - Sol: $\nabla^2 V$ uzaysal yayılma; $\mu\varepsilon\,\partial^2V/\partial t^2$ zamansal değişim → **dalga karakteri**
> - Sağ: $-\rho_v/\varepsilon$ kaynak terimi (yük dağılımı)
> - Dalga hızı: $v = 1/\sqrt{\mu\varepsilon}$
> - **Kaynak olmayan bölge** ($\rho_v = 0$): $\nabla^2 V = \mu\varepsilon\,\partial^2 V/\partial t^2$ (homojen dalga denklemi)
> - Statik durumda ($\partial/\partial t = 0$): $\nabla^2 V = -\rho_v/\varepsilon$ → Poisson denklemi

---

## Soru 5 — Elektromanyetik Sınır Koşulları (20p)

**Verilen:**
- Ortam 1 ($\varepsilon_1,\,\mu_1$) ve Ortam 2 ($\varepsilon_2,\,\mu_2$): kayıpsız lineer
- Serbest yüzey yükü yok: $\rho_s = 0$
- Yüzey akımı yok: $\mathbf{J}_s = \mathbf{0}$
- Zamanla değişen alanlar

> [!question] 📝 Soru metni (sınavda sorulan)
> $\varepsilon$ elektrik geçirgenliği ve $\mu$ manyetik geçirgenliğine sahip kayıpsız lineer iki ortam arasındaki arayüzeyde serbest yük ve yüzey akımları bulunmamaktadır. Buna göre zamanla değişen alanlar için bu iki ortam arasındaki elektromanyetik sınır şartlarını elde ediniz ve sonucu bir cümle ile yorumlayınız. **(20p)**

> [!note]- Semboller
> - $\hat{n}_{12}$: Ortam 1'den 2'ye bakan arayüzey normali
> - **Tanjansiyel (t)**: yüzeye paralel bileşen; **Normal (n)**: yüzeye dik bileşen
> - $\Delta w$: dikdörtgen çevrimin genişliği; $\Delta S$: Gauss kutusunun yüzey alanı
> - Her koşul: kapalı çizgi veya kapalı yüzey integralinin $h \to 0$ limiti

---

### 4 Sınır Koşulu Türetimi

#### SC1 — Tanjansiyel **E** sürekliliği (Faraday)

**Kurulum:** Arayüzeye **paralel**, tanjansiyel yönde genişliği $\Delta w$ olan küçük dikdörtgen bir kontur $C$ seç; konturun üst kenarı ortam 1'de, alt kenarı ortam 2'de, iki dikey kenarının uzunluğu (arayüzeye **dik** yönde) $h$ olsun ve $h\to0$ alınacak.

**Kapalı çevrim integralini 4 kenara ayır** (üst → sağ dikey → alt → sol dikey, kapalı yönde dolaşarak):
$$\oint_C\mathbf E\cdot d\mathbf l = \underbrace{E_{1t}\,\Delta w}_{\text{üst kenar (ortam 1)}} \;\underbrace{-\,E_{2t}\,\Delta w}_{\text{alt kenar (ortam 2), ters yönde}} \;+\;\underbrace{(\text{iki dikey kenar})}_{\text{uzunluğu}\propto h}$$

Üst ve alt kenarlar zıt yönde dolaşıldığı için (kapalı çevrim) işaretleri **ters**; bu yüzden fark ($E_{1t}-E_{2t}$) çıkıyor, toplam değil.

**$h\to0$ limitinde iki şey birden sıfıra gider:**
- Dikey kenarların katkısı $\to0$ (uzunlukları $h\to0$, alan sonlu kaldığı sürece).
- Sağ taraftaki akı da $\to0$: çevrilen alan $\Delta S\approx h\,\Delta w\to0$ ve **B** sonlu kabul edildiğinden $-d\Phi_B/dt\to0$.

$$\oint_C\mathbf{E}\cdot d\mathbf{l} = -\frac{d\Phi_B}{dt} \xrightarrow{h\to0} E_{1t}\,\Delta w - E_{2t}\,\Delta w = 0$$

$$\boxed{\hat{n}_{12}\times(\mathbf{E}_1 - \mathbf{E}_2) = 0 \implies E_{1t} = E_{2t}}$$

---

#### SC2 — Tanjansiyel **H** sürekliliği (Ampere-Maxwell, $J_s = 0$)

**Kurulum:** SC1 ile birebir aynı dikdörtgen kontur ($\Delta w$ genişlik, $h\to0$ yükseklik), bu kez Ampere-Maxwell yasasına uygulanıyor.

**Sağ taraftaki iki terimin limitte davranışı farklıdır — bu ayrım önemli:**
- $\dfrac{d}{dt}\displaystyle\int_S\mathbf D\cdot d\mathbf S\to0$: SC1'deki $\Phi_B$ ile aynı sebep, $\Delta S\to0$ ve **D** sonlu.
- $\displaystyle\int_S\mathbf J\cdot d\mathbf S$: eğer **J** sıradan (sonlu) bir **hacimsel** akım yoğunluğuysa, $\Delta S\to0$ ile bu da $0$'a gider. **Ama** arayüzeyde gerçek bir **yüzey akımı** $\mathbf J_s$ (A/m, ideal olarak sonsuz yoğunluklu ince tabaka) varsa, bu terim limitte **sıfıra gitmez**, $J_s\Delta w$ olarak hayatta kalır — genel sınır koşulu ($\boxed{\cdot}$ içindeki $=\mathbf J_s$) işte bu yüzden sıfır değil, $\mathbf J_s$'e eşit yazılır. Bu soruda $\mathbf J_s=\mathbf 0$ **verildiği için** o terim de sıfırlanıyor.

$$\oint_C\mathbf{H}\cdot d\mathbf{l} = \underbrace{\int_S\mathbf{J}\cdot d\mathbf{S}}_{\to\,J_s\Delta w=0} + \underbrace{\frac{d}{dt}\int_S\mathbf{D}\cdot d\mathbf{S}}_{\to 0} \xrightarrow{h\to0} H_{1t}\,\Delta w - H_{2t}\,\Delta w = 0$$

$$\boxed{\hat{n}_{12}\times(\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s = \mathbf{0} \implies H_{1t} = H_{2t}}$$

---

#### SC3 — Normal **B** sürekliliği (Gauss-Manyetik)

**Kurulum:** Arayüzeyi kapsayan küçük bir **Gauss kutusu** (silindirik "hap kutusu"): üst taban alanı $\Delta S$ ortam 1'de (dışa dönük normali $\hat n_{12}$), alt taban alanı $\Delta S$ ortam 2'de (dışa dönük normali $-\hat n_{12}$), yan yüzeyin yüksekliği $h\to0$.

**Kapalı yüzey integralini 3 parçaya ayır** (üst taban + alt taban + yan yüzey):
$$\oint_S\mathbf B\cdot d\mathbf S = \underbrace{B_{1n}\,\Delta S}_{\text{üst taban}} \;\underbrace{-\,B_{2n}\,\Delta S}_{\text{alt taban (normal ters)}} \;+\;\underbrace{(\text{yan yüzey})}_{\text{alanı}\propto h\to0}$$

Yan yüzeyin alanı $h\to0$ ile birlikte sıfıra gittiğinden o katkı düşer; Gauss-manyetik yasası sağ tarafı zaten $0$ olduğundan:

$$\oint_S\mathbf{B}\cdot d\mathbf{S} = 0 \xrightarrow{h\to0} B_{1n}\,\Delta S - B_{2n}\,\Delta S = 0$$

$$\boxed{\hat{n}_{12}\cdot(\mathbf{B}_1 - \mathbf{B}_2) = 0 \implies B_{1n} = B_{2n}}$$

---

#### SC4 — Normal **D** sürekliliği (Gauss-Elektrik, $\rho_s = 0$)

**Kurulum:** SC3 ile birebir aynı Gauss kutusu, bu kez Gauss-elektrik yasasına uygulanıyor.

**İçerdiği yük terimi de SC2'deki $J_s$ ile aynı mantıkla ayrılmalı:** kutunun içindeki toplam serbest yük $Q_{enc}=\int_V\rho_v\,dV$. Eğer $\rho_v$ sıradan (sonlu) bir **hacimsel** yük yoğunluğuysa, kutunun hacmi $\propto h\Delta S\to0$ ile bu da $0$'a gider. **Ama** arayüzeyde gerçek bir **yüzey yükü** $\rho_s$ (C/m², ince tabakada yoğunlaşmış) varsa, o limitte sıfıra gitmez, $\rho_s\Delta S$ olarak kalır — genel sınır koşulu bu yüzden $\rho_s$'e eşit yazılır. Bu soruda $\rho_s=0$ **verildiği için** sıfırlanıyor.

$$\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{enc}=\rho_s\,\Delta S = 0 \xrightarrow{h\to0} D_{1n}\,\Delta S - D_{2n}\,\Delta S = 0$$

$$\boxed{\hat{n}_{12}\cdot(\mathbf{D}_1 - \mathbf{D}_2) = \rho_s = 0 \implies D_{1n} = D_{2n}}$$

---

### Özet Tablo

| Koşul | İfade | Kaynak Maxwell Denklemi |
|---|---|---|
| **E tanjansiyel** | $E_{1t} = E_{2t}$ | Faraday |
| **H tanjansiyel** | $H_{1t} = H_{2t}$ ($J_s = 0$) | Ampere-Maxwell |
| **B normal** | $B_{1n} = B_{2n}$ | Gauss-Manyetik |
| **D normal** | $D_{1n} = D_{2n}$ ($\rho_s = 0$) | Gauss-Elektrik |

> [!success] Sonuç ve **yorum** (soru bunu ayrıca istiyor)
> **Sonuç (tekrar, dört koşul):** Kayıpsız, serbest yüksüz iki lineer ortam arasında tanjansiyel $E,H$ ile normal $B,D$ bileşenleri süreklidir.
>
> **Yorum (bir cümle):** Bu dört koşul aslında **tek bir fiziksel ilkenin** dört farklı bileşene yansımasıdır — *serbest yük/akım olmayan bir arayüzeyde alanlar ani bir sıçrama yapamaz, çünkü öyle bir sıçrama Faraday ve Ampère-Maxwell yasalarının integral hâlini ($\oint\to0$ limitinde) ihlal ederdi*; yalnızca **normal $E,H$** ve **tanjansiyel $D,B$** bileşenlerinin (kaynak yokluğunda bile) $\varepsilon,\mu$ farkı yüzünden **süreksiz olmasına izin verilir** — dalganın arayüzeyde kısmen yansıyıp kısmen kırılmasının (Snell yasası, Fresnel katsayıları) fiziksel kökeni tam olarak bu izin verilen süreksizliktir.
