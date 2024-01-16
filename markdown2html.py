#!/usr/bin/env python3
"""
Markdown to HTML Converter
"""

import argparse
import pathlib
import re
import sys

def convert_md_to_html(input_md, output_html):
    with open(input_md, encoding='utf-8') as md_file:
        md_lines = md_file.readlines()

    html_lines = []
    for line in md_lines:
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            h_level = len(match.group(1))
            h_content = match.group(2)
            html_lines.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_lines.append(line)

    with open(output_html, 'w', encoding='utf-8') as html_file:
        html_file.writelines(html_lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Minimal Markdown to HTML')
    parser.add_argument('input_md', help='Input Markdown file path')
    parser.add_argument('output_html', help='Output HTML file path')
    args = parser.parse_args()

    input_path = pathlib.Path(args.input_md)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    convert_md_to_html(args.input_md, args.output_html)
