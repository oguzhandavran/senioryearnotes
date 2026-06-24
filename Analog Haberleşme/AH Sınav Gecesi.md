---
tags: [analog-haberleşme, sınav-gecesi, özet, cheat-sheet]
---

# AH — Sınav Gecesi Özeti

← [[AH Ana Sayfa]]

> [!warning] Bu sayfayı sınav gecesi tarama: En kritik formüller ve yaygın hatalar

---

## HIZLI FORMÜL BLOK

$$X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt \qquad \text{sinc}(x)=\frac{\sin(\pi x)}{\pi x}$$

$$A\Pi(t/\tau)\leftrightarrow A\tau\,\text{sinc}(f\tau) \qquad x(t-t_0)\leftrightarrow e^{-j2\pi ft_0}X(f)$$

$$x(t)e^{j2\pi f_0 t}\leftrightarrow X(f-f_0) \qquad x(t)\cos(2\pi f_0t)\leftrightarrow\tfrac{1}{2}[X(f-f_0)+X(f+f_0)]$$

$$c_n=\frac{1}{T_0}\int_0^{T_0}x(t)e^{-jn\omega_0t}dt \qquad \text{Kare dalga: }c_n=\frac{A\tau}{T_0}\text{sinc}\!\left(\frac{n\tau}{T_0}\right)$$

$$x_c^{AM}=A_c[1+mx(t)]\cos(2\pi f_ct) \qquad x_c^{DSB}=A_cx(t)\cos(2\pi f_ct)$$

$$m=\frac{C_{\max}-C_{\min}}{C_{\max}+C_{\min}} \qquad P_{AM}=\frac{A_c^2}{2}\!\left(1+\frac{m^2}{2}\right) \qquad P_{DSB}=\frac{A_c^2}{2}\langle x^2\rangle$$

---

## SORU TİPİ → YÖNTEM

| Soru türü | Ne yap |
|-----------|--------|
| FT bul — dikdörtgen darbe | $A\Pi(t/\tau)\leftrightarrow A\tau\,\text{sinc}(f\tau)$ + kaydırma |
| FT bul — üstel | $\int e^{(a-j2\pi f)t}dt$, yakınsamayı kontrol et |
| Spektrum çiz | sin→cos(-π/2), tek→çift taraf, genlik /2 |
| Konvülüsyon | Kayan pencere, örtüşme bölge bölge |
| $c_n$ hesabı | $c_n=(1/T_0)\int$ veya kare dalga sinc formülü |
| AM güç | $P_c=A_c^2/2$, $2P_y=A_c^2m^2\langle x^2\rangle/2$ |
| Modülasyon indeksi | Zarftan $C_{\max},C_{\min}$ oku |
| DSB-SC spektrum | $X(f\pm f_c)/2$ — taşıyıcı yok |
| Bant genişliği | AM/DSB: $B_T=2W$ · SSB: $B_T=W$ |

---

## KRİTİK DETAYLAR

> [!sinav] Sık Yapılan Hatalar

**1. Konvansiyon:** Bu derste $f$ (Hz) kullan, $\omega$ (rad/s) değil!
- Türev özelliği: $(j2\pi f)^n$ ← (SS'deki $(j\omega)^n$ değil!)
- Fourier serisi: $c_n = (1/T_0)\int x(t)e^{-jn\omega_0 t}dt$ ($\omega_0 = 2\pi/T_0$ içindedir!)

**2. Zaman kaydırma:** Genlik DEĞİŞMEZ, sadece faz değişir.

$$|e^{-j2\pi ft_0}X(f)| = |X(f)|$$

**3. Frekans kaydırma (modülasyon):** Kosinüs ile çarpmak = $\pm f_c$'ye taşımak **ve** $1/2$ ile çarpmak.

**4. Kare dalga $c_n$ sıfırları:** $\text{sinc}(n\tau/T_0) = 0$ olduğunda harmonik yok.
- $\tau/T_0 = 1/2$: çift harmonikler ($n=\pm2,\pm4,...$) sıfır
- $\tau/T_0 = 1/3$: $n=\pm3,\pm6,...$ sıfır

**5. AM gücü:** Tek tonlu mesaj için $\langle x^2 \rangle = 1/2$.

$$P_T = \frac{A_c^2}{2}\!\left(1 + \frac{m^2 \cdot 1/2}{1}\right) = \frac{A_c^2}{2}\!\left(1+\frac{m^2}{2}\right)$$

**6. DSB-SC:** Taşıyıcı bileşen yoktur → $P_c = 0$ → verimlilik $\eta = 1$.

---

## TEMEL FT ÇİFTLERİ (EZBERLİK)

$$\delta(t) \leftrightarrow 1 \qquad 1 \leftrightarrow \delta(f) \qquad e^{j2\pi f_0t} \leftrightarrow \delta(f-f_0)$$

$$\cos(2\pi f_0t) \leftrightarrow \tfrac{1}{2}[\delta(f-f_0)+\delta(f+f_0)]$$

$$A\Pi(t/\tau) \leftrightarrow A\tau\,\text{sinc}(f\tau) \qquad e^{-at}u(t) \leftrightarrow \frac{1}{a+j2\pi f}$$

---

## KONVÜLÜSYON HATIRLATICI

Dikdörtgen ★ Dikdörtgen = **Trapez** (veya üçgen, eşit genişlikler)

- Başlangıç noktası: $t_{x,başl} + t_{h,başl}$
- Bitiş noktası: $t_{x,bitiş} + t_{h,bitiş}$
- Düz bölge: $|\text{genişlik farkı}|$ kadar sürer
- Max değer: kısa dikdörtgenin alanı × uzun dikdörtgenin genliği

---

## GÜÇ vs ENERJİ

| | Enerji | Güç |
|--|--------|-----|
| Koşul | $E = \int x^2 dt < \infty$ | $P = \lim\frac{1}{T}\int x^2 dt < \infty$ |
| Diğer | $P = 0$ | $E = \infty$ |
| Örnek | Kısa darbe, $e^{-at}u(t)$ | $\cos(\omega_0 t)$, sabit, periyodik |

**Parseval:** $E = \int x^2 dt = \int |X(f)|^2 df$
