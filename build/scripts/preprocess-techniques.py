#!/usr/bin/env python3
"""
Preprocess technique files for the PDF build.

Reads all .md technique files from <input-dir>, strips frontmatter,
demotes every heading one level (# → ##, ## → ###, etc.), and concatenates
them into a single <output-file>. A chapter-level H1 is prepended so the
chapter appears correctly in the TOC.

Usage:
    preprocess-techniques.py <input-dir> <output-file> [lang]

    lang defaults to 'es'
"""

import re
import sys
from pathlib import Path

CHAPTER_TITLES = {
    'es': 'Técnicas',
    'en': 'Techniques',
}


def strip_frontmatter(content: str) -> str:
    if content.startswith('---\n'):
        end = content.find('\n---\n', 4)
        if end != -1:
            return content[end + 5:]
    return content


def demote_headings(content: str) -> str:
    lines = content.split('\n')
    result = []
    in_code_block = False
    for line in lines:
        if line.rstrip().startswith('```'):
            in_code_block = not in_code_block
        if not in_code_block and re.match(r'^#{1,6}( |$)', line):
            line = '#' + line
        result.append(line)
    return '\n'.join(result)


def main() -> None:
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} <input-dir> <output-file> [lang]', file=sys.stderr)
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    lang = sys.argv[3] if len(sys.argv) > 3 else 'es'

    chapter_title = CHAPTER_TITLES.get(lang, 'Técnicas')

    files = sorted(
        f for f in input_dir.glob('*.md')
        if f.name != 'README.md'
    )

    if not files:
        print(f'No .md files found in {input_dir}', file=sys.stderr)
        sys.exit(1)

    parts = [f'# {chapter_title}\n']

    for f in files:
        content = f.read_text(encoding='utf-8')
        content = strip_frontmatter(content).strip()
        if content:
            parts.append(demote_headings(content))

    output_file.write_text('\n\n'.join(parts) + '\n', encoding='utf-8')
    print(f'  Compiled {len(files)} technique file(s) → {output_file.name}')


if __name__ == '__main__':
    main()
