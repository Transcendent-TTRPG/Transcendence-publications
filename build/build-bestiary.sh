#!/usr/bin/env bash
# ============================================================
#  Transcendence Bestiary — PDF Build Script
#  Usage:  ./build-bestiary.sh [en|es] ["Book Title"]
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLICATIONS_DIR="$(dirname "$SCRIPT_DIR")"
BOOK_DIR="$PUBLICATIONS_DIR/core-books/transcendence-bestiary"
OUTPUT_DIR="$SCRIPT_DIR/output"
STYLES_DIR="$SCRIPT_DIR/styles"
TEMPLATES_DIR="$SCRIPT_DIR/templates"
ASSETS_DIR="$SCRIPT_DIR/assets"
SCRIPTS_DIR="$SCRIPT_DIR/scripts"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PYTHON_BIN="$PUBLICATIONS_DIR/../.venv/bin/python"

LANG="${1:-es}"
TITLE="${2:-Bestiario}"
AUTHOR="${3:-}"

mkdir -p "$OUTPUT_DIR"
HTML_OUT="$OUTPUT_DIR/transcendence-bestiary-${LANG}.html"
PDF_DEST="$BOOK_DIR/98-layout-export/${LANG}"
PDF_OUT="$PDF_DEST/transcendence-bestiary-${LANG}.pdf"
PDF_RAW="${TMPDIR:-/tmp}/transcendence-bestiary-${LANG}.raw.pdf"
PAPER_BACKGROUND="$ASSETS_DIR/corebook-paper-background.jpg"
mkdir -p "$PDF_DEST"
trap 'rm -f "$PDF_RAW"' EXIT

echo "============================================"
echo "  Building Transcendence Bestiary"
echo "  Language : $LANG"
echo "  Title    : $TITLE"
echo "============================================"
echo ""

CONTENT_DIR="$BOOK_DIR/$LANG"
if [ ! -d "$CONTENT_DIR" ]; then
  echo "ERROR: No content found for language '$LANG' at $CONTENT_DIR"
  exit 1
fi

CHAPTERS=()
while IFS= read -r -d '' f; do
  [[ "$(basename "$f")" == "README.md" ]] && continue
  CHAPTERS+=("$f")
done < <(find "$CONTENT_DIR" -maxdepth 1 -name "*.md" -print0 | sort -z)

if [ ${#CHAPTERS[@]} -eq 0 ]; then
  echo "ERROR: No .md files found in $CONTENT_DIR"; exit 1
fi

echo "Found ${#CHAPTERS[@]} file(s):"
for f in "${CHAPTERS[@]}"; do echo "  $(basename "$f")"; done
echo ""

META_ARGS=(--metadata "title=$TITLE" --metadata "lang=$LANG")
[ -n "$AUTHOR" ] && META_ARGS+=(--metadata "author=$AUTHOR")

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

echo "Step 2/2 — Printing to PDF with Chrome..."
if [ ! -f "$CHROME" ]; then
  echo "ERROR: Chrome not found at: $CHROME"; exit 1
fi
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="$PDF_RAW" \
  --print-to-pdf-no-header \
  --no-pdf-header-footer \
  "file://$HTML_OUT" 2>/dev/null

if [ -f "$PAPER_BACKGROUND" ] && [ -x "$PYTHON_BIN" ]; then
  "$PYTHON_BIN" "$SCRIPTS_DIR/apply-pdf-background.py" \
    "$PDF_RAW" "$PAPER_BACKGROUND" "$PDF_OUT"
else
  cp "$PDF_RAW" "$PDF_OUT"
fi

echo "  PDF ready: $PDF_OUT"
echo ""
echo "Done!"
