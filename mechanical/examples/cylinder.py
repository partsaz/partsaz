"""
مثال ۲: ساخت استوانه

هدف: آشنایی با cylinder و پارامترهای آن
"""

import cadquery as cq

# پارامترها
radius = 5     # شعاع
height = 20    # ارتفاع

# ساخت استوانه
result = cq.Workplane("XY").cylinder(height, radius)

# ذخیره به STL
cq.exporters.export(result, "cylinder.stl")

print(f"استوانه با شعاع {radius} و ارتفاع {height} ساخته شد!")
