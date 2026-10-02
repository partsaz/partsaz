"""
مثال ۱: ساخت مکعب ساده

این اولین مثال CadQuery است.
هدف: آشنایی با Workplane و box
"""

import cadquery as cq

# پارامترها
length = 10  # طول (X)
width = 20   # عرض (Y)
height = 30  # ارتفاع (Z)

# ساخت مکعب
result = cq.Workplane("XY").box(length, width, height)

# ذخیره به STL
cq.exporters.export(result, "cube.stl")

print(f"مکعب {length}×{width}×{height} ساخته شد!")
print("فایل cube.stl ذخیره شد.")
