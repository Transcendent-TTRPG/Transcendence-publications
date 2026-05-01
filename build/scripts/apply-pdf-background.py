#!/usr/bin/env python3
"""Stamp a full-page background image behind every page of a PDF."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


def apply_background(input_pdf: Path, background_image: Path, output_pdf: Path) -> None:
    doc = fitz.open(input_pdf)
    image_xref = 0

    for page in doc:
        if image_xref:
            page.insert_image(page.rect, xref=image_xref, overlay=False, keep_proportion=False)
        else:
            image_xref = page.insert_image(
                page.rect,
                filename=background_image,
                overlay=False,
                keep_proportion=False,
            )

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_pdf, garbage=4, deflate=True)
    doc.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("background_image", type=Path)
    parser.add_argument("output_pdf", type=Path)
    args = parser.parse_args()

    apply_background(args.input_pdf, args.background_image, args.output_pdf)


if __name__ == "__main__":
    main()
