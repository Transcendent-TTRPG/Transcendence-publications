#!/usr/bin/env bash
# ============================================================
#  Transcendence Bestiary — PDF Build Script
#  Usage:  ./build-bestiary.sh [en|es] ["Book Title"]
#
#  Pipeline:
#    1. Intro chapters (01–06 .md) → Pandoc → HTML → Chrome → intro PDF
#    2. Creature cards (cards/$LANG/*.html) → Chrome → one PDF per card
#    3. PyMuPDF merges intro PDF + card PDFs → final PDF
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
export PATH="/opt/homebrew/bin:$PATH"

LANG="${1:-es}"
TITLE="${2:-Bestiario}"
AUTHOR="${3:-}"

mkdir -p "$OUTPUT_DIR"
HTML_OUT="$OUTPUT_DIR/transcendence-bestiary-${LANG}-intro.html"
PDF_INTRO="${TMPDIR:-/tmp}/transcendence-bestiary-${LANG}.intro.pdf"
PDF_DEST="$BOOK_DIR/98-layout-export/${LANG}"
PDF_OUT="$PDF_DEST/transcendence-bestiary-${LANG}.pdf"
PAPER_BACKGROUND="$ASSETS_DIR/corebook-paper-background.jpg"
mkdir -p "$PDF_DEST"

CARD_DIR="$BOOK_DIR/cards/$LANG"

TEMP_FILES=("$PDF_INTRO")
trap 'rm -f "${TEMP_FILES[@]}" 2>/dev/null' EXIT

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

# ─── Collect intro chapters (skip 07+) ────────────────────
CHAPTERS=()
while IFS= read -r -d '' f; do
  base="$(basename "$f")"
  [[ "$base" == "README.md" ]] && continue
  prefix="${base%%[-_]*}"
  if [[ "$prefix" =~ ^[0-9]+$ ]] && [ "$prefix" -ge 7 ]; then
    echo "  Skipping (creature): $base"
    continue
  fi
  CHAPTERS+=("$f")
done < <(find "$CONTENT_DIR" -maxdepth 1 -name "*.md" -print0 | sort -z)

# ─── Collect creature card HTML files ─────────────────────
CARD_FILES=()
if [ -d "$CARD_DIR" ]; then
  while IFS= read -r -d '' f; do
    CARD_FILES+=("$f")
  done < <(find "$CARD_DIR" -maxdepth 1 -name "*.html" -print0 | sort -z)
fi

echo ""
echo "Intro chapters : ${#CHAPTERS[@]} file(s)"
for f in "${CHAPTERS[@]}"; do echo "  $(basename "$f")"; done
echo "Creature cards : ${#CARD_FILES[@]} file(s)"
for f in "${CARD_FILES[@]}"; do echo "  $(basename "$f")"; done
echo ""

# ─── Step 1: Intro chapters → HTML via Pandoc ─────────────
if [ ${#CHAPTERS[@]} -gt 0 ]; then
  echo "Step 1/3 — Converting intro chapters to HTML (Pandoc)..."
  META_ARGS=(--metadata "title=$TITLE" --metadata "lang=$LANG")
  [ -n "$AUTHOR" ] && META_ARGS+=(--metadata "author=$AUTHOR")

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

  echo "Step 2/3 — Printing intro chapters to PDF (Chrome)..."
  if [ ! -f "$CHROME" ]; then
    echo "ERROR: Chrome not found at: $CHROME"; exit 1
  fi
  "$CHROME" \
    --headless=new \
    --disable-gpu \
    --no-sandbox \
    --print-to-pdf="$PDF_INTRO" \
    --print-to-pdf-no-header \
    --no-pdf-header-footer \
    "file://$HTML_OUT" 2>/dev/null

  if [ -f "$PAPER_BACKGROUND" ] && [ -x "$PYTHON_BIN" ]; then
    PDF_INTRO_BG="${TMPDIR:-/tmp}/transcendence-bestiary-${LANG}.intro.bg.pdf"
    TEMP_FILES+=("$PDF_INTRO_BG")
    "$PYTHON_BIN" "$SCRIPTS_DIR/apply-pdf-background.py" \
      "$PDF_INTRO" "$PAPER_BACKGROUND" "$PDF_INTRO_BG"
    PDF_INTRO="$PDF_INTRO_BG"
  fi
  echo "  Intro PDF ready."
  echo ""
else
  echo "Step 1-2/3 — No intro chapters, skipping."
  PDF_INTRO=""
fi

# ─── Step 3: Creature cards → PDF + merge ─────────────────
if [ ${#CARD_FILES[@]} -gt 0 ]; then
  echo "Step 3/3 — Printing creature cards and merging..."
  if [ ! -f "$CHROME" ]; then
    echo "ERROR: Chrome not found at: $CHROME"; exit 1
  fi

  CARD_PDFS=()
  for f in "${CARD_FILES[@]}"; do
    card_name=$(basename "$f" .html)
    card_pdf="$OUTPUT_DIR/card-${card_name}-${LANG}.pdf"
    TEMP_FILES+=("$card_pdf")
    echo "  Printing: $(basename "$f")..."
    "$CHROME" \
      --headless=new \
      --disable-gpu \
      --no-sandbox \
      --print-to-pdf="$card_pdf" \
      --print-to-pdf-no-header \
      --no-pdf-header-footer \
      "file://$f" 2>/dev/null
    CARD_PDFS+=("$card_pdf")
  done

  MERGE_INPUTS=()
  [ -n "$PDF_INTRO" ] && MERGE_INPUTS+=("$PDF_INTRO")
  MERGE_INPUTS+=("${CARD_PDFS[@]}")

  "$PYTHON_BIN" "$SCRIPTS_DIR/merge-pdfs.py" "${MERGE_INPUTS[@]}" "$PDF_OUT"
  echo ""
elif [ -n "$PDF_INTRO" ]; then
  echo "Step 3/3 — No creature cards, copying intro PDF as final output."
  cp "$PDF_INTRO" "$PDF_OUT"
else
  echo "ERROR: Nothing to build."
  exit 1
fi

echo "PDF ready: $PDF_OUT"
echo ""
echo "Done!"
