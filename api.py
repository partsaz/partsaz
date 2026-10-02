"""
پارت‌ساز API - نسخه ۱

FastAPI backend برای ساخت قطعات مکانیکی پارامتریک
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
import cadquery as cq
from cq_gears import SpurGear

app = FastAPI(title="Partsaz API", version="0.1.0")


@app.get("/")
def home():
    return {
        "message": "پارت‌ساز API - خوش آمدید!",
        "version": "0.1.0",
        "endpoints": {
            "/gear": "ساخت چرخ‌دنده پارامتریک",
            "/docs": "مستندات API"
        }
    }


@app.get("/gear")
def make_gear(
    module: float = 2.0,
    teeth: int = 20,
    width: float = 10.0,
    bore: float = 8.0
):
    """ساخت چرخ‌دنده پارامتریک و برگرداندن فایل STL"""
    
    gear = SpurGear(
        module=module,
        teeth_number=teeth,
        width=width,
        bore_d=bore
    )
    solid = cq.Workplane("XY").gear(gear)
    
    filename = f"gear_m{module}_z{teeth}.stl"
    cq.exporters.export(solid, filename)
    
    return FileResponse(
        filename,
        media_type="application/octet-stream",
        filename=filename
    )
