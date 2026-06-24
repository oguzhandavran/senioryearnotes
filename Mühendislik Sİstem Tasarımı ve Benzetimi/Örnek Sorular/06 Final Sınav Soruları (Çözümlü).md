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

---

### Adım 1 — Sıfır ve Kutup Sayıları (1p)

- **Sıfırlar:** yok → $n = 0$
- **Kutuplar:** $s = -1,\,-2,\,-3$ → $m = 3$

---

### Adım 2 — Kök Yer Eğrisi Taslağı (1p)

<svg width="420" height="340" viewBox="0 0 420 340" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-kye" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
    <clipPath id="clip-kye"><rect x="10" y="10" width="400" height="320"/></clipPath>
  </defs>
  <rect x="10" y="10" width="400" height="320" fill="#fafbff" stroke="#1a1a2e" stroke-width="1.2" rx="2"/>
  <line x1="30" y1="10" x2="30" y2="330" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="68" y1="10" x2="68" y2="330" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="106" y1="10" x2="106" y2="330" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="144" y1="10" x2="144" y2="330" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="182" y1="10" x2="182" y2="330" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="220" y1="10" x2="220" y2="330" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="258" y1="10" x2="258" y2="330" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="327" x2="410" y2="327" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="289" x2="410" y2="289" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="251" x2="410" y2="251" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="213" x2="410" y2="213" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="137" x2="410" y2="137" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="99" x2="410" y2="99" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="61" x2="410" y2="61" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="10" y1="23" x2="410" y2="23" stroke="#e0e0e0" stroke-width="0.5"/>
  <line x1="220" y1="10" x2="220" y2="330" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-kye)"/>
  <line x1="10" y1="175" x2="410" y2="175" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-kye)"/>
  <text x="226" y="18" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-style="italic" fill="#1a1a2e">j&#969;</text>
  <text x="402" y="189" font-family="'STIX Two Math','Times New Roman',serif" font-size="12" font-style="italic" fill="#1a1a2e">&#963;</text>
  <text x="30" y="189" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#777">-5</text>
  <text x="68" y="189" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#777">-4</text>
  <text x="106" y="189" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#777">-3</text>
  <text x="144" y="189" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#777">-2</text>
  <text x="182" y="189" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#777">-1</text>
  <text x="258" y="189" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#777">1</text>
  <text x="214" y="293" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#777">-3j</text>
  <text x="214" y="217" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#777">-1j</text>
  <text x="214" y="141" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#777">1j</text>
  <text x="214" y="65" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="#777">3j</text>
  <line x1="144.0" y1="175.0" x2="248.5" y2="-6.0" stroke="#888" stroke-width="1" stroke-dasharray="5,4" clip-path="url(#clip-kye)"/>
  <line x1="144.0" y1="175.0" x2="-65.0" y2="175.0" stroke="#888" stroke-width="1" stroke-dasharray="5,4" clip-path="url(#clip-kye)"/>
  <line x1="144.0" y1="175.0" x2="248.5" y2="356.0" stroke="#888" stroke-width="1" stroke-dasharray="5,4" clip-path="url(#clip-kye)"/>
  <line x1="182" y1="175" x2="144" y2="175" stroke="#c0392b" stroke-width="3" opacity="0.6"/>
  <line x1="106" y1="175" x2="12" y2="175" stroke="#c0392b" stroke-width="3" opacity="0.6"/>
  <path d="M106.0,175.0 L101.2,175.0 L97.6,175.0 L94.6,175.0 L91.9,175.0 L89.6,175.0 L87.5,175.0 L85.5,175.0 L83.7,175.0 L82.0,175.0 L80.5,175.0 L79.0,175.0 L77.5,175.0 L76.2,175.0 L74.9,175.0 L73.6,175.0 L72.4,175.0 L71.2,175.0 L70.1,175.0 L69.0,175.0 L68.0,175.0 L67.0,175.0 L66.0,175.0 L65.0,175.0 L64.1,175.0 L63.1,175.0 L62.2,175.0 L61.4,175.0 L60.5,175.0 L59.7,175.0 L58.8,175.0 L58.0,175.0 L57.3,175.0 L56.5,175.0 L55.7,175.0 L55.0,175.0 L54.2,175.0 L53.5,175.0 L52.8,175.0 L52.1,175.0 L51.4,175.0 L50.8,175.0 L50.1,175.0 L49.4,175.0 L48.8,175.0 L48.2,175.0 L47.5,175.0 L46.9,175.0 L46.3,175.0 L45.7,175.0 L45.1,175.0 L44.5,175.0 L43.9,175.0 L43.4,175.0 L42.8,175.0 L42.2,175.0 L41.7,175.0 L41.1,175.0 L40.6,175.0 L40.1,175.0 L39.5,175.0 L39.0,175.0 L38.5,175.0 L38.0,175.0 L37.5,175.0 L37.0,175.0 L36.5,175.0 L36.0,175.0 L35.5,175.0 L35.0,175.0 L34.5,175.0 L34.1,175.0 L33.6,175.0 L33.1,175.0 L32.7,175.0 L32.2,175.0 L31.7,175.0 L31.3,175.0 L30.8,175.0 L30.4,175.0 L30.0,175.0 L29.5,175.0 L29.1,175.0 L28.7,175.0 L28.2,175.0 L27.8,175.0 L27.4,175.0 L27.0,175.0 L26.6,175.0 L26.1,175.0 L25.7,175.0 L25.3,175.0 L24.9,175.0 L24.5,175.0 L24.1,175.0 L23.7,175.0 L23.3,175.0 L23.0,175.0 L22.6,175.0 L22.2,175.0 L21.8,175.0 L21.4,175.0 L21.0,175.0 L20.7,175.0 L20.3,175.0 L19.9,175.0 L19.6,175.0 L19.2,175.0 L18.8,175.0 L18.5,175.0 L18.1,175.0 L17.8,175.0 L17.4,175.0 L17.1,175.0 L16.7,175.0 L16.4,175.0 L16.0,175.0 L15.7,175.0 L15.3,175.0 L15.0,175.0 L14.6,175.0 L14.3,175.0 L14.0,175.0 L13.6,175.0 L13.3,175.0 L13.0,175.0 L12.6,175.0 L12.3,175.0 L12.0,175.0 L11.7,175.0 L11.3,175.0 L11.0,175.0 L10.7,175.0 L10.4,175.0 L10.1,175.0" fill="none" stroke="#1a1a2e" stroke-width="2" clip-path="url(#clip-kye)"/>
  <path d="M144.0,175.0 L156.9,175.0 L167.2,161.9 L168.7,155.3 L170.0,150.7 L171.2,147.2 L172.3,144.2 L173.2,141.5 L174.1,139.2 L175.0,137.1 L175.8,135.2 L176.5,133.4 L177.2,131.8 L177.9,130.2 L178.6,128.7 L179.2,127.3 L179.8,126.0 L180.4,124.7 L180.9,123.5 L181.5,122.4 L182.0,121.2 L182.5,120.2 L183.0,119.1 L183.5,118.1 L184.0,117.1 L184.4,116.2 L184.9,115.3 L185.3,114.4 L185.7,113.5 L186.2,112.6 L186.6,111.8 L187.0,111.0 L187.4,110.2 L187.8,109.4 L188.1,108.7 L188.5,107.9 L188.9,107.2 L189.2,106.5 L189.6,105.8 L189.9,105.1 L190.3,104.4 L190.6,103.8 L190.9,103.1 L191.3,102.5 L191.6,101.8 L191.9,101.2 L192.2,100.6 L192.5,100.0 L192.8,99.4 L193.1,98.8 L193.4,98.3 L193.7,97.7 L194.0,97.1 L194.3,96.6 L194.6,96.0 L194.9,95.5 L195.2,95.0 L195.4,94.4 L195.7,93.9 L196.0,93.4 L196.2,92.9 L196.5,92.4 L196.7,91.9 L197.0,91.4 L197.3,90.9 L197.5,90.5 L197.8,90.0 L198.0,89.5 L198.3,89.1 L198.5,88.6 L198.7,88.1 L199.0,87.7 L199.2,87.3 L199.4,86.8 L199.7,86.4 L199.9,85.9 L200.1,85.5 L200.4,85.1 L200.6,84.7 L200.8,84.3 L201.0,83.8 L201.2,83.4 L201.5,83.0 L201.7,82.6 L201.9,82.2 L202.1,81.8 L202.3,81.4 L202.5,81.0 L202.7,80.7 L202.9,80.3 L203.1,79.9 L203.3,79.5 L203.5,79.1 L203.7,78.8 L203.9,78.4 L204.1,78.0 L204.3,77.7 L204.5,77.3 L204.7,76.9 L204.9,76.6 L205.1,76.2 L205.3,75.9 L205.5,75.5 L205.7,75.2 L205.8,74.8 L206.0,74.5 L206.2,74.2 L206.4,73.8 L206.6,73.5 L206.8,73.2 L206.9,72.8 L207.1,72.5 L207.3,72.2 L207.5,71.8 L207.6,71.5 L207.8,71.2 L208.0,70.9 L208.2,70.6 L208.3,70.2 L208.5,69.9 L208.7,69.6 L208.8,69.3 L209.0,69.0 L209.2,68.7 L209.3,68.4 L209.5,68.1 L209.7,67.8 L209.8,67.5 L210.0,67.2 L210.2,66.9 L210.3,66.6 L210.5,66.3 L210.6,66.0 L210.8,65.7 L211.0,65.4 L211.1,65.1 L211.3,64.8 L211.4,64.6 L211.6,64.3 L211.7,64.0 L211.9,63.7 L212.0,63.4 L212.2,63.2 L212.3,62.9 L212.5,62.6 L212.6,62.3 L212.8,62.1 L212.9,61.8 L213.1,61.5 L213.2,61.2 L213.4,61.0 L213.5,60.7 L213.7,60.4 L213.8,60.2 L214.0,59.9 L214.1,59.7 L214.3,59.4 L214.4,59.1 L214.5,58.9 L214.7,58.6 L214.8,58.4 L215.0,58.1 L215.1,57.9 L215.2,57.6 L215.4,57.4 L215.5,57.1 L215.7,56.9 L215.8,56.6 L215.9,56.4 L216.1,56.1 L216.2,55.9 L216.3,55.6 L216.5,55.4 L216.6,55.1 L216.7,54.9 L216.9,54.7 L217.0,54.4 L217.1,54.2 L217.3,53.9 L217.4,53.7 L217.5,53.5 L217.6,53.2 L217.8,53.0 L217.9,52.8 L218.0,52.5 L218.2,52.3 L218.3,52.1 L218.4,51.8 L218.5,51.6 L218.7,51.4 L218.8,51.1 L218.9,50.9 L219.0,50.7 L219.2,50.5 L219.3,50.2 L219.4,50.0 L219.5,49.8 L219.7,49.6 L219.8,49.4 L219.9,49.1 L220.0,49.0 L221.0,47.1 L222.0,45.4 L223.0,43.6 L223.9,41.9 L224.8,40.3 L225.7,38.7 L226.6,37.1 L227.5,35.5 L228.3,34.0 L229.1,32.6 L229.9,31.1 L230.7,29.7 L231.5,28.3 L232.3,26.9 L233.0,25.6 L233.7,24.3 L234.5,23.0 L235.2,21.7 L235.9,20.4 L236.6,19.2 L237.3,18.0 L237.9,16.8 L238.6,15.6 L239.3,14.4 L239.9,13.3 L240.5,12.2 L241.2,11.1 L241.8,10.0" fill="none" stroke="#1a1a2e" stroke-width="2" clip-path="url(#clip-kye)"/>
  <path d="M182.0,175.0 L173.9,175.0 L167.2,188.1 L168.7,194.7 L170.0,199.3 L171.2,202.8 L172.3,205.8 L173.2,208.5 L174.1,210.8 L175.0,212.9 L175.8,214.8 L176.5,216.6 L177.2,218.2 L177.9,219.8 L178.6,221.3 L179.2,222.7 L179.8,224.0 L180.4,225.3 L180.9,226.5 L181.5,227.6 L182.0,228.8 L182.5,229.8 L183.0,230.9 L183.5,231.9 L184.0,232.9 L184.4,233.8 L184.9,234.7 L185.3,235.6 L185.7,236.5 L186.2,237.4 L186.6,238.2 L187.0,239.0 L187.4,239.8 L187.8,240.6 L188.1,241.3 L188.5,242.1 L188.9,242.8 L189.2,243.5 L189.6,244.2 L189.9,244.9 L190.3,245.6 L190.6,246.2 L190.9,246.9 L191.3,247.5 L191.6,248.2 L191.9,248.8 L192.2,249.4 L192.5,250.0 L192.8,250.6 L193.1,251.2 L193.4,251.7 L193.7,252.3 L194.0,252.9 L194.3,253.4 L194.6,254.0 L194.9,254.5 L195.2,255.0 L195.4,255.6 L195.7,256.1 L196.0,256.6 L196.2,257.1 L196.5,257.6 L196.7,258.1 L197.0,258.6 L197.3,259.1 L197.5,259.5 L197.8,260.0 L198.0,260.5 L198.3,260.9 L198.5,261.4 L198.7,261.9 L199.0,262.3 L199.2,262.7 L199.4,263.2 L199.7,263.6 L199.9,264.1 L200.1,264.5 L200.4,264.9 L200.6,265.3 L200.8,265.7 L201.0,266.2 L201.2,266.6 L201.5,267.0 L201.7,267.4 L201.9,267.8 L202.1,268.2 L202.3,268.6 L202.5,269.0 L202.7,269.3 L202.9,269.7 L203.1,270.1 L203.3,270.5 L203.5,270.9 L203.7,271.2 L203.9,271.6 L204.1,272.0 L204.3,272.3 L204.5,272.7 L204.7,273.1 L204.9,273.4 L205.1,273.8 L205.3,274.1 L205.5,274.5 L205.7,274.8 L205.8,275.2 L206.0,275.5 L206.2,275.8 L206.4,276.2 L206.6,276.5 L206.8,276.8 L206.9,277.2 L207.1,277.5 L207.3,277.8 L207.5,278.2 L207.6,278.5 L207.8,278.8 L208.0,279.1 L208.2,279.4 L208.3,279.8 L208.5,280.1 L208.7,280.4 L208.8,280.7 L209.0,281.0 L209.2,281.3 L209.3,281.6 L209.5,281.9 L209.7,282.2 L209.8,282.5 L210.0,282.8 L210.2,283.1 L210.3,283.4 L210.5,283.7 L210.6,284.0 L210.8,284.3 L211.0,284.6 L211.1,284.9 L211.3,285.2 L211.4,285.4 L211.6,285.7 L211.7,286.0 L211.9,286.3 L212.0,286.6 L212.2,286.8 L212.3,287.1 L212.5,287.4 L212.6,287.7 L212.8,287.9 L212.9,288.2 L213.1,288.5 L213.2,288.8 L213.4,289.0 L213.5,289.3 L213.7,289.6 L213.8,289.8 L214.0,290.1 L214.1,290.3 L214.3,290.6 L214.4,290.9 L214.5,291.1 L214.7,291.4 L214.8,291.6 L215.0,291.9 L215.1,292.1 L215.2,292.4 L215.4,292.6 L215.5,292.9 L215.7,293.1 L215.8,293.4 L215.9,293.6 L216.1,293.9 L216.2,294.1 L216.3,294.4 L216.5,294.6 L216.6,294.9 L216.7,295.1 L216.9,295.3 L217.0,295.6 L217.1,295.8 L217.3,296.1 L217.4,296.3 L217.5,296.5 L217.6,296.8 L217.8,297.0 L217.9,297.2 L218.0,297.5 L218.2,297.7 L218.3,297.9 L218.4,298.2 L218.5,298.4 L218.7,298.6 L218.8,298.9 L218.9,299.1 L219.0,299.3 L219.2,299.5 L219.3,299.8 L219.4,300.0 L219.5,300.2 L219.7,300.4 L219.8,300.6 L219.9,300.9 L220.0,301.0 L221.0,302.9 L222.0,304.6 L223.0,306.4 L223.9,308.1 L224.8,309.7 L225.7,311.3 L226.6,312.9 L227.5,314.5 L228.3,316.0 L229.1,317.4 L229.9,318.9 L230.7,320.3 L231.5,321.7 L232.3,323.1 L233.0,324.4 L233.7,325.7 L234.5,327.0 L235.2,328.3 L235.9,329.6" fill="none" stroke="#1a1a2e" stroke-width="2" clip-path="url(#clip-kye)"/>
  <line x1="176.0" y1="169.0" x2="188.0" y2="181.0" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="188.0" y1="169.0" x2="176.0" y2="181.0" stroke="#1a1a2e" stroke-width="2.5"/>
  <text x="190.0" y="171.0" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">-1</text>
  <line x1="138.0" y1="169.0" x2="150.0" y2="181.0" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="150.0" y1="169.0" x2="138.0" y2="181.0" stroke="#1a1a2e" stroke-width="2.5"/>
  <text x="152.0" y="171.0" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">-2</text>
  <line x1="100.0" y1="169.0" x2="112.0" y2="181.0" stroke="#1a1a2e" stroke-width="2.5"/>
  <line x1="112.0" y1="169.0" x2="100.0" y2="181.0" stroke="#1a1a2e" stroke-width="2.5"/>
  <text x="114.0" y="171.0" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">-3</text>
  <circle cx="176.6" cy="175.0" r="4" fill="white" stroke="#c0392b" stroke-width="1.8"/>
  <text x="176.6" y="191.0" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#c0392b">-1.142</text>
  <circle cx="122.2" cy="175.0" r="4" fill="white" stroke="#c0392b" stroke-width="1.8"/>
  <text x="122.2" y="191.0" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#c0392b">-2.574</text>
  <circle cx="220.0" cy="49.0" r="4" fill="white" stroke="#27ae60" stroke-width="1.8"/>
  <text x="226.0" y="53.0" font-family="Arial,sans-serif" font-size="8" fill="#27ae60">+3.317j</text>
  <circle cx="220.0" cy="301.0" r="4" fill="white" stroke="#27ae60" stroke-width="1.8"/>
  <text x="226.0" y="305.0" font-family="Arial,sans-serif" font-size="8" fill="#27ae60">-3.317j</text>
  <circle cx="144.0" cy="175" r="3.5" fill="#888"/>
  <text x="144.0" y="167" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#888">&#963;_a=-2</text>
  <line x1="18" y1="18" x2="38" y2="18" stroke="#c0392b" stroke-width="3" opacity="0.6"/>
  <text x="42" y="22" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">Reel eksen KYE</text>
  <line x1="18" y1="32" x2="38" y2="32" stroke="#888" stroke-width="1" stroke-dasharray="5,4"/>
  <text x="42" y="36" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">Asimptot (60°,180°,300°)</text>
  <text x="210" y="330" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">KYE: G(s) = K/[(s+1)(s+2)(s+3)]</text>
</svg>

3 dal, 3 kutuptan çıkar, 3 asimptota gider.

---

### Adım 3 — Asimptot Sayısı (1p)

$$m - n = 3 - 0 = \boxed{3 \text{ adet}}$$

---

### Adım 4 — Asimptot Açıları (1p)

$$\beta = \frac{180°(2k+1)}{m-n} = \frac{180°(2k+1)}{3} \Rightarrow \boxed{60°,\ 180°,\ 300°}$$

---

### Adım 5 — Asimptotların Reel Ekseni Kestiği Nokta (1p)

$$\sigma_a = \frac{\sum\text{kutuplar} - \sum\text{sıfırlar}}{m-n} = \frac{(-1-2-3) - 0}{3} = \frac{-6}{3} = \boxed{-2}$$

---

### Adım 6 — Ayrılma-Birleşme Noktası (1p)

$$\left(\frac{1}{G(s)}\right)' = 0 \Rightarrow \left(\frac{(s+1)(s+2)(s+3)}{K}\right)' = 0$$

Açılırsa:
$$(s^2+3s+2)(s+3) = s^3+6s^2+11s+6$$

$$(s^3+6s^2+11s+6)' = 3s^2+12s+11 = 0$$

$$s = \frac{-12 \pm \sqrt{144-132}}{6} = \frac{-12 \pm \sqrt{12}}{6}$$

$$\boxed{s_1 = -1{,}142 \quad (\text{reel eksende, geçerli})}$$
$$s_2 = -2{,}57 \quad (\text{reel eksende, geçerli})$$

---

### Adım 7 — Sönüm Oranı (%20 aşım için) (1p)

$$\zeta = \frac{-\ln(\%OS)}{\sqrt{\pi^2 + \ln^2(\%OS)}} = \frac{-\ln(0{,}20)}{\sqrt{\pi^2 + \ln^2(0{,}20)}} = \frac{1{,}609}{\sqrt{9{,}870 + 2{,}590}} = \boxed{0{,}456}$$

---

### Adım 8 — Sönüm Açısı (1p)

$$\beta = \cos^{-1}(\zeta) = \cos^{-1}(0{,}456) = \boxed{62{,}87°}$$

---

### Adım 9 — İstenen Kutup Konumu ve K Kritik (her biri 1p)

$s_d = 1{,}8594\angle 117{,}26°$:
$$s_d = 1{,}8594(\cos 117{,}26° + j\sin 117{,}26°) = -0{,}866 + j1{,}169$$

Kutuplardan uzaklıklar:
$$\ell_1 = \sqrt{(3-0{,}866)^2 + 1{,}169^2} = 2{,}72$$
$$\ell_2 = \sqrt{(2-0{,}866)^2 + 1{,}169^2} = 2{,}035$$
$$\ell_3 = \sqrt{(1-0{,}866)^2 + 1{,}169^2} = 1{,}695$$

$$\boxed{K = \frac{\prod\text{kutup uzaklıkları}}{\prod\text{sıfır uzaklıkları}} = \ell_1 \cdot \ell_2 \cdot \ell_3 = 2{,}72 \times 2{,}035 \times 1{,}695 = 8{,}33}$$

---

### Adım 10 — Kararlı Durum Hatası (1p + 1p)

**Tip 0** sistem (açık çevrimde serbest integratör yok):

$$K_p = \lim_{s\to 0} G(s) = \frac{8{,}33}{(1)(2)(3)} = 1{,}565$$

$$\boxed{e_{ss} = \frac{1}{1+K_p} = \frac{1}{2{,}565} = 0{,}39}$$

---

### Adım 11 — İmajiner Ekseni Kesme Noktası (Routh-Hurwitz) (1p)

Kapalı çevrim karakteristik polinomu:
$$s^3 + 6s^2 + 11s + (6+K) = 0$$

| $s^3$ | 1 | 11 |
|--------|---|-----|
| $s^2$ | 6 | $6+K$ |
| $s^1$ | $\frac{66-(6+K)}{6} = \frac{60-K}{6}$ | 0 |
| $s^0$ | $6+K$ | — |

Kararlılık koşulu: $60 - K > 0$ ve $6+K > 0$ → $\boxed{-6 < K < 60}$

$K = 60$ olursa imajiner eksen kesimi: $s^3 + 6s^2 + 11s + 66 = 0$

Çözüm: $s_1 = -6$, $s_{2,3} = \pm j3{,}317$

---

### Adım 12 — Yerleşme Süresi ve PD Tasarımı (her biri 1p)

**Mevcut sistem için:**
$$t_s = \frac{4}{\zeta\omega_n} = \frac{4}{0{,}866} = 4{,}62 \text{ s}$$

**İstenen yerleşme süresi** (4 kat iyileştirme):
$$t_{s,\text{yeni}} = \frac{4{,}62}{4} = 1{,}155 \text{ s}$$

**İstenen $\omega_n$:**
$$\omega_{ny} = \frac{4}{\zeta \cdot t_{s,\text{yeni}}} = \frac{4}{0{,}456 \times 1{,}155} = 7{,}59 \text{ rad/s}$$

$$\alpha_y = \omega_{ny}\cdot\zeta = 7{,}59 \times 0{,}456 = 3{,}46$$
$$\omega_y = \tan(62{,}87°) \times 3{,}46 = 6{,}75$$

**İstenen kutup:** $s_y = -3{,}46 + j6{,}75$

**PD sıfırının bulunması** (açı koşulu):
$$\theta_1 - (\theta_2 + \theta_3 + \theta_4) = -180°$$
$$\theta_1 - (83{,}9° + 102{,}2° + 110{,}02°) = -180°$$
$$\theta_1 = 126{,}12° \Rightarrow \theta_1' = 180° - 126{,}12° = 53{,}88°$$

$$\tan(53{,}88°) = \frac{6{,}75}{3{,}46 - x} \Rightarrow 1{,}37 = \frac{6{,}75}{3{,}46-x} \Rightarrow \boxed{z_c = x = 3{,}32}$$

**PD transfer fonksiyonu:**
$$G_{PD}(s) = -R_2 C\!\left(s + \frac{1}{R_1 C}\right)$$

Tasarım kısıtları:
$$\frac{1}{R_1 C} = 3{,}32, \quad R_2 C = 1$$

---

## Soru 2 — Doğrusal Olmayan Sistem: Denge ve Kararlılık

**Verilen:**
$$\dot{x} = x^2 - y - 1 \equiv f_1(x,y)$$
$$\dot{y} = y(x-2) \equiv f_2(x,y)$$

---

### 2a — Denge Noktaları (2p + 2p + 2p)

$\dot{x} = 0$, $\dot{y} = 0$ koşulu:

$$0 = x^2 - y - 1 \quad \Rightarrow \quad x^2 = y+1$$
$$0 = y(x-2) \quad \Rightarrow \quad y = 0 \text{ veya } x = 2$$

**$y = 0$ için:** $x^2 = 1$ → $x = \pm 1$ → **(−1, 0)** ve **(1, 0)**

**$x = 2$ için:** $y = 4-1 = 3$ → **(2, 3)**

$$\boxed{\text{Denge noktaları: } (-1,0),\ (1,0),\ (2,3)}$$

---

### 2b — Jacobian Matrisi (3p)

$$J = \begin{bmatrix} \dfrac{\partial f_1}{\partial x} & \dfrac{\partial f_1}{\partial y} \\[8pt] \dfrac{\partial f_2}{\partial x} & \dfrac{\partial f_2}{\partial y} \end{bmatrix} = \begin{bmatrix} 2x & -1 \\ y & x-2 \end{bmatrix}$$

---

### 2c — Her Denge Noktasında Kararlılık (her biri 3p)

#### (−1, 0) noktası:

$$J_{(-1,0)} = \begin{bmatrix} -2 & -1 \\ 0 & -3 \end{bmatrix}$$

$$\det(\lambda I - J) = (\lambda+2)(\lambda+3) = 0 \Rightarrow \lambda_1 = -2,\ \lambda_2 = -3$$

✅ Her iki özdeğer negatif reel → **Kararlı nokta (Stable Point)**

---

#### (1, 0) noktası:

$$J_{(1,0)} = \begin{bmatrix} 2 & -1 \\ 0 & -1 \end{bmatrix}$$

$$(\lambda - 2)(\lambda + 1) = 0 \Rightarrow \lambda_1 = +2,\ \lambda_2 = -1$$

⚠️ Özdeğerler zıt işaretli → **Eyer Noktası (Saddle Point)**

---

#### (2, 3) noktası:

$$J_{(2,3)} = \begin{bmatrix} 4 & -1 \\ 3 & 0 \end{bmatrix}$$

$$\lambda(\lambda-4) + 3 = 0 \Rightarrow \lambda^2 - 4\lambda + 3 = 0 \Rightarrow (\lambda-3)(\lambda-1) = 0$$
$$\lambda_1 = 3,\ \lambda_2 = 1$$

❌ Her iki özdeğer pozitif → **Kararsız Nokta (Unstable)**

---

### Faz Portresi Yorumu (3p)

| Denge Noktası | Tür | Davranış |
|---|---|---|
| (−1, 0) | Kararlı düğüm | Yörüngeler bu noktaya yaklaşır |
| (1, 0) | Eyer noktası | Bir yönde yaklaşır, diğerinde uzaklaşır |
| (2, 3) | Kararsız düğüm | Yörüngeler bu noktadan uzaklaşır |

---

## Soru 3 — Doğrusal Olmayan Elektrik Devresi Doğrusallaştırma

**Verilen devre:** Gerilim kaynağı $u(t)$, $L=1\text{H}$ endüktör, doğrusal olmayan direnç $V_r = 2i^2(t)$, DC kaynak $5\text{V}$.

---

### 3a — Sistem Denklemi (5p)

KVL uygulayınca:
$$\boxed{u(t) = \frac{di(t)}{dt} + 2i^2(t) - 5}$$

---

### 3b — Çalışma Noktası (5p)

DC kararlı durumda $\dot{i} = 0$, $u(t) = 0$:
$$0 = 0 + 2i_0^2 - 5 \Rightarrow i_0^2 = 2{,}5 \Rightarrow \boxed{i_0 = 1{,}58\text{ A}}$$

---

### 3c — Taylor Serisi ile Doğrusallaştırma (5p)

$f(i) = 2i^2$ için:
$$f(i) \approx f(i_0) + \left.\frac{df}{di}\right|_{i_0}(i - i_0) = 5 + 4i_0\cdot\delta i(t) = 5 + 6{,}32\,\delta i(t)$$

$i(t) = i_0 + \delta i(t)$ yerine koyunca:
$$u(t) = \frac{d(\delta i)}{dt} + 5 + 6{,}32\,\delta i(t) - 5$$

$$\boxed{u(t) = \frac{d(\delta i)}{dt} + 6{,}32\,\delta i(t)}$$

---

### 3d — Laplace Dönüşümü ve Transfer Fonksiyonu (5p + 5p)

$$U(s) = s\,\Delta I(s) + 6{,}32\,\Delta I(s) = \Delta I(s)(s + 6{,}32)$$

$$\Delta I(s) = \frac{U(s)}{s + 6{,}32}$$

Direnç gerilimi için: $V_r(s) = 4i_0\,\Delta I(s) = 6{,}32\,\Delta I(s)$

$$\boxed{\frac{V_r(s)}{U(s)} = \frac{6{,}32}{s + 6{,}32}}$$

---

## Soru 4 — Yay-Kütle Sistemi: Faz Portresi

**Verilen:** $k=1$, $m=1$, sönümsüz yay-kütle sistemi.

---

### 4a — Hareket Denklemi (5p)

$$F_{net} = ma \Rightarrow -kx = m\ddot{x}$$
$$\boxed{\ddot{x} + x = 0}$$

---

### 4b — Özdeğerler (5p)

Durum değişkenleri: $x_1 = x$, $\dot{x}_1 = \lambda$, $\ddot{x}_1 = \lambda^2$:

$$\lambda^2 + 1 = 0 \Rightarrow \lambda^2 = -1 \Rightarrow \boxed{\lambda = \pm j}$$

Saf sanal özdeğerler → **Merkez noktası (Center)**

---

### 4c — Genel Çözüm (3p + 2p)

$$x_1(t) = A\sin t + B\cos t$$
$$x_2(t) = \dot{x}_1 = A\cos t - B\sin t$$

---

### 4d — Faz Portresi (5p)

$$x_1^2 + x_2^2 = (A\sin t + B\cos t)^2 + (A\cos t - B\sin t)^2$$
$$= A^2(\sin^2 t + \cos^2 t) + B^2(\cos^2 t + \sin^2 t) = A^2 + B^2 = r^2$$

$$\boxed{x_1^2 + x_2^2 = r^2 = \text{sabit}}$$

→ Faz düzleminde **iç içe daireler** — sistem ne kararlı ne kararsız, **Lyapunov anlamında kararlı**.

<svg width="320" height="280" viewBox="0 0 320 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-fp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1a1a2e"/>
    </marker>
    <marker id="arr-fp-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2980b9"/>
    </marker>
  </defs>
  <rect x="5" y="5" width="310" height="270" fill="#fafbff" stroke="#1a1a2e" stroke-width="1.2" rx="2"/>
  <line x1="160" y1="8" x2="160" y2="272" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-fp)"/>
  <line x1="8" y1="140" x2="312" y2="140" stroke="#1a1a2e" stroke-width="1.2" marker-end="url(#arr-fp)"/>
  <text x="166" y="20" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">x&#8322;</text>
  <text x="300" y="154" font-family="'STIX Two Math','Times New Roman',serif" font-size="13" font-style="italic" fill="#1a1a2e">x&#8321;</text>
  <circle cx="160" cy="140" r="25" fill="none" stroke="#2980b9" stroke-width="1.8"/>
  <line x1="152" y1="115" x2="162" y2="115" stroke="#2980b9" stroke-width="1.8" marker-end="url(#arr-fp-b)"/>
  <circle cx="160" cy="140" r="50" fill="none" stroke="#27ae60" stroke-width="1.8"/>
  <line x1="152" y1="90" x2="162" y2="90" stroke="#27ae60" stroke-width="1.8"/>
  <circle cx="160" cy="140" r="75" fill="none" stroke="#e67e22" stroke-width="1.8"/>
  <line x1="152" y1="65" x2="162" y2="65" stroke="#e67e22" stroke-width="1.8"/>
  <circle cx="160" cy="140" r="100" fill="none" stroke="#c0392b" stroke-width="1.8"/>
  <line x1="152" y1="40" x2="162" y2="40" stroke="#c0392b" stroke-width="1.8"/>
  <circle cx="160" cy="140" r="118" fill="none" stroke="#8e44ad" stroke-width="1.8"/>
  <line x1="152" y1="22" x2="162" y2="22" stroke="#8e44ad" stroke-width="1.8"/>
  <circle cx="160" cy="140" r="4" fill="#1a1a2e"/>
  <text x="166" y="136" font-family="Arial,sans-serif" font-size="9" fill="#1a1a2e">Merkez (0,0)</text>
  <text x="215" y="90" font-family="Arial,sans-serif" font-size="8" fill="#666">⟳ saat yönü</text>
  <text x="160" y="272" text-anchor="middle" font-family="'STIX Two Math','Times New Roman',serif" font-size="10" fill="#1a1a2e">x&#8321;&#178; + x&#8322;&#178; = r&#178; = sabit</text>
</svg>

**Yorum:** Başlangıç koşulları ($A$, $B$) yarıçapı belirler. Sistem salınım yapar, enerji korunur, yörüngeler kapalı.
