#!/usr/bin/env bash
# ============================================================
#  Transcendence Corebook — PDF Build Script
#  Usage:  ./build-pdf.sh [en|es] ["Book Title"] ["Author"]
#  Example: ./build-pdf.sh en "Transcendence Corebook" "Your Name"
# ============================================================
set -euo pipefail

# --- Paths ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLICATIONS_DIR="$(dirname "$SCRIPT_DIR")"
COREBOOK_DIR="$PUBLICATIONS_DIR/core-books/transcendence-corebook"
OUTPUT_DIR="$SCRIPT_DIR/output"
STYLES_DIR="$SCRIPT_DIR/styles"
TEMPLATES_DIR="$SCRIPT_DIR/templates"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# --- Arguments ---
LANG="${1:-en}"
TITLE="${2:-Transcendence Corebook}"
AUTHOR="${3:-}"

# --- Output files ---
mkdir -p "$OUTPUT_DIR"
HTML_OUT="$OUTPUT_DIR/transcendence-corebook-${LANG}.html"
PDF_DEST="$COREBOOK_DIR/98-layout-export/${LANG}"
PDF_OUT="$PDF_DEST/transcendence-corebook-${LANG}.pdf"
mkdir -p "$PDF_DEST"

echo "============================================"
echo "  Building Transcendence Corebook"
echo "  Language : $LANG"
echo "  Title    : $TITLE"
echo "============================================"
echo ""

# --- Collect markdown files in chapter order ---
echo "Collecting chapters..."
CHAPTERS=()

for chapter_dir in \
  "$COREBOOK_DIR"/01-* \
  "$COREBOOK_DIR"/02-* \
  "$COREBOOK_DIR"/03-* \
  "$COREBOOK_DIR"/04-* \
  "$COREBOOK_DIR"/05-* \
  "$COREBOOK_DIR"/06-* \
  "$COREBOOK_DIR"/07-* \
  "$COREBOOK_DIR"/08-* \
  "$COREBOOK_DIR"/09-* \
  "$COREBOOK_DIR"/10-* \
  "$COREBOOK_DIR"/11-* \
  "$COREBOOK_DIR"/12-* \
  "$COREBOOK_DIR"/13-* \
  "$COREBOOK_DIR"/14-* \
  "$COREBOOK_DIR"/15-* \
  "$COREBOOK_DIR"/16-* \
  "$COREBOOK_DIR"/17-*
do
  [ -d "$chapter_dir/$LANG" ] || continue

  while IFS= read -r -d '' f; do
    [[ "$(basename "$f")" == "README.md" ]] && continue
    CHAPTERS+=("$f")
  done < <(find "$chapter_dir/$LANG" -maxdepth 1 -name "*.md" -print0 | sort -z)
done

if [ ${#CHAPTERS[@]} -eq 0 ]; then
  echo "ERROR: No content files found for language '$LANG'."
  echo "  Make sure chapters have .md files (not only README.md) in their $LANG/ folders."
  exit 1
fi

echo "Found ${#CHAPTERS[@]} content file(s):"
for f in "${CHAPTERS[@]}"; do
  chapter=$(basename "$(dirname "$(dirname "$f")")")
  echo "  [$chapter] $(basename "$f")"
done
echo ""

# --- Build Pandoc metadata args ---
META_ARGS=(
  --metadata "title=$TITLE"
  --metadata "lang=$LANG"
)
if [ -n "$AUTHOR" ]; then
  META_ARGS+=(--metadata "author=$AUTHOR")
fi

# --- Step 1: Markdown → HTML ---
echo "Step 1/2 — Converting Markdown to HTML..."
pandoc \
  --from markdown \
  --to html5 \
  --standalone \
  --embed-resources \
  --template "$TEMPLATES_DIR/corebook.html" \
  --css "$STYLES_DIR/corebook.css" \
  --toc \
  --toc-depth=2 \
  "${META_ARGS[@]}" \
  "${CHAPTERS[@]}" \
  --output "$HTML_OUT"

echo "  HTML ready: $HTML_OUT"
echo ""

# --- Step 2: HTML → PDF via Chrome headless ---
echo "Step 2/2 — Printing to PDF with Chrome..."

if [ ! -f "$CHROME" ]; then
  echo "ERROR: Chrome not found at:"
  echo "  $CHROME"
  echo "Update the CHROME variable in this script if it's in a different location."
  exit 1
fi

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="$PDF_OUT" \
  --print-to-pdf-no-header \
  --no-pdf-header-footer \
  "file://$HTML_OUT" 2>/dev/null

echo "  PDF ready: $PDF_OUT"
echo ""
echo "Done!"
