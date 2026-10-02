"""
مثال ۶: ساخت جفت چرخ‌دنده درگیر

هدف: محاسبه‌ی فاصله‌ی مرکز و ساخت دو چرخ‌دنده که درگیر شوند
"""

import cadquery as cq
from cq_gears import SpurGear

# ============ پارامترها ============
m = 2.0           # ماژول (mm)
z1 = 20           # تعداد دندانه‌های چرخ‌دنده ۱
z2 = 40           # تعداد دندانه‌های چرخ‌دنده ۲
width = 10.0      # عرض (mm)
bore1 = 8.0
bore2 = 12.0

# ============ محاسبات طبق DIN 867 ============
d1 = m * z1
d2 = m * z2
a = (d1 + d2) / 2

print(f"قطر گام ۱: {d1} mm")
print(f"قطر گام ۲: {d2} mm")
print(f"فاصله مرکز تا مرکز: {a} mm")

# ============ ساخت ============
gear1 = SpurGear(module=m, teeth_number=z1, width=width, bore_d=bore1)
gear2 = SpurGear(module=m, teeth_number=z2, width=width, bore_d=bore2)

solid1 = cq.Workplane("XY").gear(gear1)
solid2 = cq.Workplane("XY").center(a, 0).gear(gear2)

# ============ ترکیب ============
result = solid1.union(solid2)

cq.exporters.export(result, "gear_pair.stl")
print("جفت چرخ‌دنده ساخته شد!")
