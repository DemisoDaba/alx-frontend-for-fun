#!/usr/bin/python3
"""This script requires markdown file, and HTML file"""

from sys import argv, stderr
import os


if __name__ == "__main__":
    if (len(argv) <= 2):
        print ('Usage: ./markdown2html.py README.md README.html', file=stderr)
        exit(1)
    elif (not os.path.exists(argv[1])):
        print ('Missing {}'.format(argv[1]), file=stderr)
        exit(1)
    else:
        with open(argv[1], 'r') as md_file:
            lines = md_file.readlines()
        L = []
        unordered_list = []
        ordered_list = []
        paragraphs = []
        p = []
        for i in range(0, len(lines)):
            if lines[i].startswith('#'):
                level = lines[i].count('#')
                if i == len(lines) - 1:
                    L.append('<h{}>{}</h{}>'.format(level,
                                                    lines[i][level+1:],
                                                    level))
                else:
                    L.append('<h{}>{}</h{}>'.format(level,
                                                    lines[i][level+1:-1],
                                                    level))
            elif lines[i].startswith('- '):
                if i == len(lines) - 1:
                    unordered_list.append('<li>{}</li>'.format(lines[i][2:]))
                else:
                    unordered_list.append('<li>{}</li>'.format(lines[i][2:-1]))
            elif lines[i].startswith('* '):
                if i == len(lines) - 1:
                    ordered_list.append('<li>{}</li>'.format(lines[i][2:]))
                else:
                    ordered_list.append('<li>{}</li>'.format(lines[i][2:-1]))
            else:
                paragraphs.append(lines[i])
                s = "".join(paragraphs)
                p = s.split('\n\n')
        if unordered_list != []:
            L.append('<ul>')
            for i in unordered_list:
                L.append('\t'+i)
            L.append('</ul>')

        if ordered_list != []:
            L.append('<ol>')
            for i in ordered_list:
                L.append('\t'+i)
            L.append('</ol>')
        if p != []:
            for item in p:
                if '\n' in item.strip():
                    item = item.replace('\n', '<br />')
                L.append('<p>')
                L.append('\t'+item.strip())
                L.append('</p>')
        with open(argv[2], 'w') as html_file:
            html_file.writelines('\n'.join(L))
        exit(0)
