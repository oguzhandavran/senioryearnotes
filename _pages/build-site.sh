#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────
# Bütünleme Dönemi → Quartz statik site derleyici
#
# Vault'taki ders notlarını (yalnızca yayınlanacak markdown + görseller)
# content/ klasörüne hazırlar ve Quartz ile public/ altında site üretir.
#
# Kullanım:
#   ./build-site.sh           # siteyi public/ altına derle
#   ./build-site.sh --serve   # yerel önizleme sunucusu (http://localhost:8080)
# ──────────────────────────────────────────────────────────────
set -euo pipefail

# ROOT  = bu script'in bulunduğu Pages klasörü (_pages/)
# VAULT = ders notlarının bulunduğu depo kökü (_pages'in bir üstü)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT="$(cd "$ROOT/.." && pwd)"
cd "$ROOT"

echo "→ content/ klasörü hazırlanıyor..."
rm -rf content
mkdir -p content

# Vault kökündeki markdown notları (-p: zaman damgalarını koru → doğru "son güncelleme")
find "$VAULT" -maxdepth 1 -type f -name '*.md' -exec cp -p {} content/ \;

# Ders klasörleri (vault kökündeki görünür klasörler; kaynak/sistem/çıktı hariç).
# Gizli klasörler (.git, .obsidian, .claude ...) zaten */ globuna girmez.
for d in "$VAULT"/*/; do
  name="$(basename "$d")"
  case "$name" in
    _pages|node_modules|public|content|quartz|scripts|_dataset|_compiled_courses|compiled_courses|_templates|Chats)
      continue ;;
  esac
  cp -rp "$d" "content/$name"
done

# HOME.md → site ana sayfası (index.md). Linkler için HOME.md de korunur.
if [ -f content/HOME.md ]; then
  cp content/HOME.md content/index.md
fi

# Türkçe karakterli dosya/klasör adlarını ve link hedeflerini ASCII'ye çevir
# → temiz URL slug'ları (yalnızca content/ kopyasını etkiler, kaynak vault'a dokunmaz)
echo "→ Temiz URL'ler için içerik ASCII'ye dönüştürülüyor..."
node scripts/asciify-content.mjs

echo "→ Quartz eklentileri kuruluyor (ilk seferde indirir)..."
npx quartz plugin install

echo "→ Quartz derleniyor..."
if [ "${1:-}" = "--serve" ]; then
  npx quartz build --serve
else
  npx quartz build
  echo "✓ Tamamlandı. Çıktı: public/"
  echo "  Yerel önizleme için: ./build-site.sh --serve"
fi
