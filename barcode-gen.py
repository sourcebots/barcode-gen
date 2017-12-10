#!/usr/bin/env python3
import time
import argparse
import re
import os
import sys

import code128

parser = argparse.ArgumentParser()
parser.add_argument('codes', metavar='NNNNNNNN', nargs='+', help="list of codes to generate (with or without dashes)")
parser.add_argument('-L', '--no-logo', dest="with_logo", default=True, action="store_false", help="don't include the logo on the label")
args = parser.parse_args()

# sanitise codes, so we can support both with and without dashes.
codes = [re.sub(r'[^0-9]','',code) for code in args.codes]
dashed_codes = ["-".join([code[0:2],code[2:4],code[4:6],code[6:8]]) for code in codes]

for code in codes:
    if len(code) != 8:
        raise Exception("Invalid code length: {}, should be 8 digits long".format(code))

if args.with_logo:
    logo_file = os.path.join(os.path.dirname(__file__), "art", "SourceBots.svg")
    if not os.path.exists(logo_file):
        print("could not find logo SVG at {}".format(logo_file), file=sys.stderr)
        print("(have you run `git submodule update --init`?)", file=sys.stderr)
        sys.exit(1)
    with open(logo_file, "r") as f:
        logo_content = "".join(line for line in f if not line.strip().startswith(("<?", "<!")))
else:
    logo_content = ""

template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg
  PUBLIC '-//W3C//DTD SVG 1.1//EN'
  'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
<svg height="29.000mm" version="1.1" width="90.300mm" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(-10,0) scale(0.7, 1.2)">
{bar}
</g>
<g transform="translate(215,15) scale(0.35,0.35)">
{logo}
</g>
<g>
<text
x="255"
y="85"
style="fill:black;font-size:16pt;text-anchor:middle;"
>
{code}
</text>
</g>
</svg>"""
for (dashed_code, code) in zip(dashed_codes, codes):
    out_file = code+".svg"
    svg = code128.svg(code)

    with open(out_file,'w') as o:
        svg_content = "\n".join(svg.split("\n")[3:-2])
        print(template.format(bar=svg_content,code=dashed_code,logo=logo_content),file=o)
