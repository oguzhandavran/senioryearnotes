---
tags: [mst, elektrik, rlc, kvl, kcl, transfer-fonksiyonu, op-amp, konu-anlatımı]
---

# 02 — Elektrik Sistemleri

← [[MST Ana Sayfa]] | Örnekler: [[../Örnek Sorular/02 Elektrik Sistemleri Örnekleri|02 Elektrik Sistemleri Örnekleri]]

## Temel Elemanlar

| Eleman | Simge | $v$-$i$ İlişkisi | Empedans $Z(s)$ | Admitans $Y(s)$ |
|--------|-------|-----------------|-----------------|-----------------|
| Direnç $R$ | — | $v = Ri$ | $R$ | $1/R$ |
| Kapasitör $C$ | — | $i = C\dfrac{dv}{dt}$ | $1/(Cs)$ | $Cs$ |
| İndüktör $L$ | — | $v = L\dfrac{di}{dt}$ | $Ls$ | $1/(Ls)$ |

---

## Kirchhoff Kanunları

**KVL (Voltaj):** $\sum v = 0$ (kapalı çevrede toplam voltaj sıfır)

**KCL (Akım):** $\sum i = 0$ (düğümde giren = çıkan akım)

---

## RLC Seri Devre

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
\draw (0,0) to[V=$v_{in}(t)$, invert] (0,3);
\draw (0,3) to[R=$R$] (2.5,3) to[L=$L$] (5,3) -- (6.5,3);
\draw (6.5,3) to[C=$C$, v=$v_C$] (6.5,0);
\draw (0,0) -- (6.5,0);
\draw (3.25,0) -- (3.25,-0.4) node[ground]{};
\end{circuitikz}
\end{document}
```

*Çıkış $v_C$, kondansatör üzerinden alınır (R–L seri, C şönt → standart 2. mertebe alçak geçiren).*

**KVL:** $v_{in} = v_R + v_L + v_C = Ri + L\dfrac{di}{dt} + \dfrac{1}{C}\int i\,dt$

Çıkış $v_C$ için ($q = \int i\,dt$):

$$L\ddot{q} + R\dot{q} + \frac{1}{C}q = v_{in}$$

$$\boxed{G(s) = \frac{V_C(s)}{V_{in}(s)} = \frac{1/LC}{s^2 + (R/L)s + 1/(LC)}}$$

> [!tip] Mekanik Analoji
> $L \leftrightarrow m$, $R \leftrightarrow b$, $1/C \leftrightarrow k$, $v_{in} \leftrightarrow f$, $q \leftrightarrow x$

---

## RLC Paralel Devre

**KCL:** $i_{in} = i_R + i_L + i_C = \dfrac{v}{R} + \dfrac{1}{L}\int v\,dt + C\dfrac{dv}{dt}$

Diferansiyel denklem:

$$C\ddot{v} + \frac{1}{R}\dot{v} + \frac{1}{L}v = \dot{i}_{in}$$

$$G(s) = \frac{V(s)}{I_{in}(s)} = \frac{s/C}{s^2 + s/(RC) + 1/(LC)}$$
>[!tip] Davran'ın notu
Saçma bir formatta görünüyor biliyorum ama aslında o ifadeler **zaten sadeleştirilmiş** halleri. İçindeki $1/LC$, $R/L$ gibi "bölümlü" katsayılar bir hata değil, kasıtlı bir **normalizasyon** sonucu. Açıklayayım:

## Ham (sadeleşmemiş) hal

Gerilim bölücüden direkt çıkarırsan, kesirsiz katsayılı temiz formu bu:

**Seri:**
$$\frac{V_C}{V_{in}} = \frac{1/Cs}{Ls + R + 1/Cs} = \frac{1}{LCs^2 + RCs + 1}$$

**Paralel:** $Y = \frac{1}{R} + \frac{1}{Ls} + Cs$ olduğundan
$$Z = \frac{1}{Y} = \frac{Ls}{LCs^2 + \frac{L}{R}s + 1}$$

Gördüğün gibi bu hallerde **iç içe kesir yok** — daha "temiz" duruyor.

## Neden normalize edilmiş hali yazıyoruz?

Pay ve paydayı $LC$'ye bölünce senin formül sayfandaki hale dönüyor:

$$\frac{1/LC}{s^2 + (R/L)s + 1/(LC)}$$

Bunun tek sebebi: paydanın **standart 2. mertebe formuna** oturması →
$$s^2 + 2\zeta\omega_n s + \omega_n^2$$

Bu sayede katsayılara bakar bakmaz okuyabiliyorsun:
- $\omega_n = \dfrac{1}{\sqrt{LC}}$
- Seri: $2\zeta\omega_n = R/L$, Paralel: $2\zeta\omega_n = 1/RC$

Yani $s^2$ katsayısı **1 olsun** diye bilerek kesirli yazılıyor. İki form da matematiksel olarak birebir aynı; sadece biri "$\zeta, \omega_n$ okumak" için, diğeri "temiz katsayı" için uygun.

---

## Empedans Yöntemi (Laplace Uzayında)

Laplace'ta direkt empedans kullanarak çözüm:

**Seri:** $Z_{toplam} = Z_1 + Z_2 + \ldots$

**Paralel:** $\dfrac{1}{Z_{toplam}} = \dfrac{1}{Z_1} + \dfrac{1}{Z_2} + \ldots$

**Gerilim bölücü:**
$$V_2(s) = V_{in}(s) \cdot \frac{Z_2}{Z_1 + Z_2}$$

---

## Op-Amp Devreleri

**İdeal Op-Amp Varsayımları:**
- $v_+ = v_-$ (negatif geri beslemeli)
- $i_+ = i_- = 0$ (giriş akımı yok)

### Ters Çevirici (Inverting Amplifier)

$$\frac{V_{out}}{V_{in}} = -\frac{Z_f}{Z_{in}}$$

### Türevleyici (Differentiator)

$Z_{in} = R$, $Z_f = 1/(Cs)$:
$$G(s) = -\frac{1/(Cs)}{R} = -\frac{1}{RCs}$$

### Entegratör (Integrator)

$Z_{in} = R$, $Z_f = 1/(Cs)$:
$$G(s) = -\frac{1/(Cs)}{R} = -\frac{1}{RCs}$$

---

## Düğüm Gerilim Yöntemi (Node Voltage)

**Adım 1:** Her düğüme voltaj ata ($v_1$, $v_2$, ...)
**Adım 2:** KCL uygula: her düğümde $\sum \dfrac{v_k - v_j}{Z_{kj}} = i_{kaynaklar}$
**Adım 3:** Çöz, transfer fonksiyonu bul

---

> [!sinav] Sınav İpucu
> - Empedans = Laplace uzayında devre analizi
> - Kapasitör: $1/(Cs)$ → yüksek frekansta kısa devre, alçakta açık devre
> - İndüktör: $Ls$ → alçak frekansta kısa devre, yüksekte açık devre
> - Mesh için KVL, düğüm için KCL
> - Başlangıç koşulları sıfır alındığında $V=ZI$ direkt kullanılır
