"""
مثال ۴: ساخت شاتون پارامتریک

هدف: ترکیب چند شکل برای ساخت قطعه‌ی واقعی
شاتون = سر بزرگ + سر کوچک + ساقه
"""

import cadquery as cq

# ============ پارامترها ============
length = 150        # طول کل (mm)
big_end_od = 50     # قطر بیرونی سر بزرگ (mm)
big_end_id = 40     # قطر داخلی سر بزرگ (mm)
small_end_od = 30   # قطر بیرونی سر کوچک (mm)
small_end_id = 20   # قطر داخلی سر کوچک (mm)
shaft_width = 15    # عرض ساقه (mm)
thickness = 20      # ضخامت (mm)
bolt_hole_d = 6     # قطر سوراخ پیچ
bolt_offset = 35    # فاصله‌ی سوراخ پیچ از مرکز

# ============ ساخت ============
# ۱. سر بزرگ
big_end = (
    cq.Workplane("XY")
    .circle(big_end_od / 2)
    .extrude(thickness)
    .faces(">Z")
    .hole(big_end_id)
)

# ۲. سر کوچک
small_end = (
    cq.Workplane("XY")
    .center(0, length)
    .circle(small_end_od / 2)
    .extrude(thickness)
    .faces(">Z")
    .hole(small_end_id)
)

# ۳. ساقه
shaft = (
    cq.Workplane("XY")
    .center(0, length / 2)
    .rect(shaft_width, length)
    .extrude(thickness)
)

# ۴. ترکیب
result = big_end.union(shaft).union(small_end)

# ۵. سوراخ‌های پیچ روی سر بزرگ
result = (
    result
    .faces(">Z")
    .workplane()
    .pushPoints([(-bolt_offset, 0), (bolt_offset, 0)])
    .hole(bolt_hole_d)
)

# ============ خروجی ============
cq.exporters.export(result, "connecting_rod.stl")
print("شاتون ساخته شد!")
print(f"طول: {length} mm")
print(f"قطر سر بزرگ: {big_end_od} mm")
print(f"قطر سر کوچک: {small_end_od} mm")
