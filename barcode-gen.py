import code128
import time
filename = "/tmp/temp"

codes = ["20883877",
"61494426",
"16258484",
"44428990",
"33843214",
"30889372",
"16963560",
"92719895",
"49698370",
"58312542"]

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
for code in codes:
    out_file = code+".svg"
    code_with_dashes = "-".join([code[0:2],code[2:4],code[4:6],code[6:8]])
    svg = code128.svg(code)

    with open(out_file,'w') as o:
        svg_content = "\n".join(svg.split("\n")[3:-2])
        print(template.format(bar=svg_content,code=code_with_dashes),file=o)
