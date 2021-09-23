import os
import colorgram

LOCAL = os.path.dirname(os.path.abspath(__file__))

extraction = colorgram.extract(os.path.join(LOCAL, "demo.jpg"), 100)
colors = []

for color in extraction:
    data = (color.rgb.r, color.rgb.g, color.rgb.b)
    colors.append(data)
