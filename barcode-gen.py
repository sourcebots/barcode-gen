#!/usr/bin/env python3
import time
import argparse
import re
import subprocess

import code128

parser = argparse.ArgumentParser()
parser.add_argument('codes', metavar='NNNNNNNN', nargs='+', help="list of codes to generate (with or without dashes)")
args = parser.parse_args()

# sanitise codes, so we can support both with and without dashes.
codes = [re.sub(r'[^0-9]','',code) for code in args.codes]
dashed_codes = ["-".join([code[0:2],code[2:4],code[4:6],code[6:8]]) for code in codes]

for code in codes:
    if len(code) != 8:
        raise Exception("Invalid code length: {}, should be 8 digits long".format(code))

template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg
  PUBLIC '-//W3C//DTD SVG 1.1//EN'
  'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
<svg height="29.000mm" version="1.1" width="90.300mm" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(-10,0) scale(0.7, 1.2)">
{bar}
</g>
<g>
<text
x="255"
y="61"
style="fill:black;font-size:16pt;text-anchor:middle;"
>
{code}
</text>
</g>
</svg>"""
for (dashed_code, code) in zip(dashed_codes, codes):
    svg_file = code+'.svg'
    png_file = code+'.png'
    svg = code128.svg(code)

    # Generate the svg
    with open(svg_file,'w') as file:
        svg_content = "\n".join(svg.split("\n")[3:-2])
        print(template.format(bar=svg_content,code=dashed_code),file=file)

    # Convert to png
    subprocess.check_call(['inkscape', svg_file, '--export-png='+png_file, '--export-width=991', '--export-height=306']);
