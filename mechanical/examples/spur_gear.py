"""
مثال ۵: ساخت چرخ‌دنده ساده طبق استاندارد DIN 867

هدف: آشنایی با cq_gears و استانداردهای آلمانی
"""

import cadquery as cq
from cq_gears import SpurGear

# ============ پارامترها (DIN 867) ============
module = 2.0        # ماژول (mm)
teeth = 20          # تعداد دندانه
width = 10.0        # عرض (mm)
bore = 8.0          # قطر سوراخ (mm)

# ============ ساخت ============
gear = SpurGear(module=module, teeth_number=teeth, width=width, bore_d=bore)
solid = cq.Workplane("XY").gear(gear)

# ============ محاسبات DIN 867 ============
d = module * teeth
da = d + 2 * module
df = d - 2.5 * module

print("=" * 40)
print("📐 محاسبات چرخ‌دنده (DIN 867)")
print("=" * 40)
print(f"ماژول: {module} mm")
print(f"تعداد دندانه: {teeth}")
print(f"قطر گام (d): {d} mm")
print(f"قطر سر (da): {da} mm")
print(f"قطر پای (df): {df} mm")
print("=" * 40)

# ============ خروجی ============
cq.exporters.export(solid, "spur_gear_din.stl")
print("✅ چرخ‌دنده ساخته شد!")
