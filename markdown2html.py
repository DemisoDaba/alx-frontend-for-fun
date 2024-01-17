#!/usr/bin/python3
"""Markdown to HTML Converter"""

import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(md_file):
        print(f'Missing {md_file}', file=sys.stderr)
        exit(1)

    with open(md_file) as md:
        with open(html_file, 'w') as html:
            in_ul, in_ol, in_p = False, False, False

            for line in md:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)

                # md5
                md5_match = re.findall(r'\[\[.+?\]\]', line)
                md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
                if md5_match:
                    line = line.replace(md5_match[0], hashlib.md5(md5_inside[0].encode()).hexdigest())

                # removing the letter C
                remove_c_match = re.findall(r'\(\(.+?\)\)', line)
                remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
                if remove_c_match:
                    remove_c_more = ''.join(c for c in remove_c_more[0] if c not in 'Cc')
                    line = line.replace(remove_c_match[0], remove_c_more)

                length = len(line)
                h_match = line.lstrip('#')
                h_num = length - len(h_match)
                ul_item = line.lstrip('-')
                ul_num = length - len(ul_item)
                ol_item = line.lstrip('*')
                ol_num = length - len(ol_item)

                # headings and lists
                if 1 <= h_num <= 6:
                    line = f'<h{h_num}>{h_match.strip()}</h{h_num}>\n'

                if ul_num:
                    if not in_ul:
                        html.write('<ul>\n')
                        in_ul = True
                    line = f'<li>{ul_item.strip()}</li>\n'
                if in_ul and not ul_num:
                    html.write('</ul>\n')
                    in_ul = False

                if ol_num:
                    if not in_ol:
                        html.write('<ol>\n')
                        in_ol = True
                    line = f'<li>{ol_item.strip()}</li>\n'
                if in_ol and not ol_num:
                    html.write('</ol>\n')
                    in_ol = False

                if not (h_num or in_ul or in_ol):
                    if not in_p and length > 1:
                        html.write('<p>\n')
                        in_p = True
                    elif length > 1:
                        html.write('<br/>\n')
                    elif in_p:
                        html.write('</p>\n')
                        in_p = False

                if length > 1:
                    html.write(line)

            if in_ul:
                html.write('</ul>\n')
            if in_ol:
                html.write('</ol>\n')
            if in_p:
                html.write('</p>\n')

    exit(0)
