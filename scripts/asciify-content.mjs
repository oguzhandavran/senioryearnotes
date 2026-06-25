// ──────────────────────────────────────────────────────────────
// content/ klasöründeki dosya/klasör adlarını ve link HEDEFLERİNİ
// ASCII'ye çevirir → temiz URL slug'ları (ör. /sinyaller-ve-sistemler/).
//
// Sadece BUILD KOPYASINI (content/) etkiler; kaynak vault'taki Türkçe
// adlara ve not metinlerine dokunulmaz. Görünen link metinleri Türkçe
// korunur; yalnızca dosya adları ve link hedef yolları ASCII olur.
//
// Hem dosya adları hem link hedefleri AYNI dönüşümden geçtiği için
// [[wiki-link]]'ler tutarlı kalır.
// ──────────────────────────────────────────────────────────────
import fs from "node:fs"
import path from "node:path"

const ROOT = "content"

const MAP = {
  İ: "I", ı: "i", Ş: "S", ş: "s", Ğ: "G", ğ: "g",
  Ç: "C", ç: "c", Ö: "O", ö: "o", Ü: "U", ü: "u",
  Â: "A", â: "a", Î: "I", î: "i", Û: "U", û: "u",
}
const tr = (s) => s.replace(/[İıŞşĞğÇçÖöÜüÂâÎîÛû]/g, (c) => MAP[c] ?? c)
const hasTR = (s) => /[İıŞşĞğÇçÖöÜüÂâÎîÛû]/.test(s)

// ── Link hedeflerini düzelt (görünen metni koruyarak) ──
function fixWikilinks(text) {
  return text.replace(/\[\[([^\]]+)\]\]/g, (m, inner) => {
    const pipe = inner.indexOf("|")
    if (pipe >= 0) {
      // [[hedef|görünen]] → hedef ASCII, görünen aynen
      const target = inner.slice(0, pipe)
      const display = inner.slice(pipe) // "|görünen"
      return `[[${tr(target)}${display}]]`
    }
    // [[hedef]] veya [[hedef#başlık]] → görünen metin yoksa, Türkçe olanı
    // koru: ASCII hedef + orijinal son segmenti görünen metin yap.
    const hash = inner.indexOf("#")
    const targetPath = hash >= 0 ? inner.slice(0, hash) : inner
    const anchor = hash >= 0 ? inner.slice(hash) : ""
    const asciiInner = tr(targetPath) + tr(anchor)
    if (hasTR(targetPath) || hasTR(anchor)) {
      const lastSeg = targetPath.split("/").pop()
      return `[[${asciiInner}|${lastSeg}${anchor}]]`
    }
    return `[[${asciiInner}]]`
  })
}

function fixMarkdownLinks(text) {
  // [metin](yol) ve ![alt](yol) → yalnızca dahili yolları ASCII'ye çevir
  return text.replace(/(!?\[[^\]]*\])\(([^)]+)\)/g, (m, label, url) => {
    if (/^(https?:|mailto:|tel:|#|data:|\/\/)/i.test(url)) return m
    return `${label}(${tr(url)})`
  })
}

// ── 1. Tüm .md dosyalarında linkleri düzelt ──
function rewriteLinks(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, e.name)
    if (e.isDirectory()) rewriteLinks(full)
    else if (e.name.toLowerCase().endsWith(".md")) {
      const orig = fs.readFileSync(full, "utf8")
      const next = fixMarkdownLinks(fixWikilinks(orig))
      if (next !== orig) fs.writeFileSync(full, next)
    }
  }
}

// ── 2. Dosya ve klasör adlarını ASCII'ye çevir (derinden yüzeye) ──
let renamed = 0
function renameEntries(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, e.name)
    if (e.isDirectory()) renameEntries(full)
    const ascii = tr(e.name)
    if (ascii !== e.name) {
      fs.renameSync(full, path.join(dir, ascii))
      renamed++
    }
  }
}

rewriteLinks(ROOT)
renameEntries(ROOT)
console.log(`✓ content/ ASCII slug'a dönüştürüldü (${renamed} dosya/klasör yeniden adlandırıldı)`)
