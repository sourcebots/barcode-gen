#!/usr/bin/env python3
import time
import argparse
import re

import code128

parser = argparse.ArgumentParser()
parser.add_argument('codes', metavar='NNNNNNNN', nargs='+', help="list of codes to generate (with or without dashes)")
args = parser.parse_args()

# sanitise codes, so we can support both with and without dashes.
codes = [re.sub(r'[^0-9]','',code) for code in args.codes]
dashed_codes = ["sb-"+"-".join([code[0:2],code[2:4],code[4:6],code[6:8]]) for code in codes]

for code in codes:
    if len(code) != 8:
        raise Exception("Invalid code length: {}, should be 8 digits long".format(code))

template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg
  PUBLIC '-//W3C//DTD SVG 1.1//EN'
  'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
<svg height="7mm" version="1.1" width="62mm" xmlns="http://www.w3.org/2000/svg">
<text
x="10"
y="20"
style="fill:black;font-size:13pt;text-anchor:left;"
>
{code}
</text>
</svg>"""
for (dashed_code, code) in zip(dashed_codes, codes):
    out_file = code+".svg"
    svg = code128.svg(code)

    with open(out_file,'w') as o:
        svg_content = "\n".join(svg.split("\n")[3:-2])
        print(template.format(code=dashed_code),file=o)
