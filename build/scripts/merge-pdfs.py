#!/usr/bin/env python3
"""Merge multiple PDF files into one, in the order given.
Usage: merge-pdfs.py input1.pdf input2.pdf ... output.pdf
"""
import sys
import pymupdf


def merge(inputs, output):
    merged = pymupdf.open()
    for path in inputs:
        doc = pymupdf.open(path)
        merged.insert_pdf(doc)
        doc.close()
    merged.save(output)
    merged.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: merge-pdfs.py input1.pdf [input2.pdf ...] output.pdf")
        sys.exit(1)
    *inputs, output = sys.argv[1:]
    merge(inputs, output)
    print(f"  Merged {len(inputs)} PDF(s) → {output}")
