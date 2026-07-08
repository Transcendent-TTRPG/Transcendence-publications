#!/usr/bin/env bash
# ============================================================
#  Transcendence Techniques Compendium — PDF Build Script
#  Usage:  ./build-techniques.sh [en|es] ["Book Title"]
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLICATIONS_DIR="$(dirname "$SCRIPT_DIR")"
BOOK_DIR="$PUBLICATIONS_DIR/core-books/transcendence-techniques"
OUTPUT_DIR="$SCRIPT_DIR/output"
STYLES_DIR="$SCRIPT_DIR/styles"
TEMPLATES_DIR="$SCRIPT_DIR/templates"
ASSETS_DIR="$SCRIPT_DIR/assets"
SCRIPTS_DIR="$SCRIPT_DIR/scripts"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PYTHON_BIN="$PUBLICATIONS_DIR/../.venv/bin/python"

LANG="${1:-es}"
TITLE="${2:-Compendio de Técnicas}"
AUTHOR="${3:-}"

mkdir -p "$OUTPUT_DIR"
HTML_OUT="$OUTPUT_DIR/transcendence-techniques-${LANG}.html"
PDF_DEST="$BOOK_DIR/98-layout-export/${LANG}"
PDF_OUT="$PDF_DEST/transcendence-techniques-${LANG}.pdf"
PDF_RAW="${TMPDIR:-/tmp}/transcendence-techniques-${LANG}.raw.pdf"
PAPER_BACKGROUND="$ASSETS_DIR/corebook-paper-background.jpg"
mkdir -p "$PDF_DEST"
TECH_COMPILED="$(mktemp /tmp/techniques-compiled-XXXXXX.md)"
trap 'rm -f "$PDF_RAW" "${TECH_COMPILED:-}"' EXIT

echo "============================================"
echo "  Building Transcendence Techniques Compendium"
echo "  Language : $LANG"
echo "  Title    : $TITLE"
echo "============================================"
echo ""

TECH_DIR="$BOOK_DIR/$LANG"
if [ ! -d "$TECH_DIR" ]; then
  echo "ERROR: No content found for language '$LANG' at $TECH_DIR"
  exit 1
fi

echo "Preprocessing technique files..."
"$PYTHON_BIN" "$SCRIPTS_DIR/preprocess-techniques.py" \
  "$TECH_DIR" \
  "$TECH_COMPILED" \
  "$LANG"
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
  "$TECH_COMPILED" \
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
