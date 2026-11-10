"""Draw numbered red boxes on screenshots and save them to fig/.

Coordinates are in the screenshot's own pixels (1440x900). Run from ux-test/:
    python scripts/annotate.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RED = (214, 40, 40)
OUT_WIDTH = 1200

# figure name -> (source screenshot, [boxes as (x1, y1, x2, y2)])
FIGURES = {  # example entries; replace per report
    "bug01-signout-crash": ("59-visitor-signout.png", [(437, 60, 1440, 822), (437, 826, 1440, 868)]),
    "bug02-timezone-visitor": ("58b-visitor-timezone-bug.png", [(1170, 66, 1268, 100), (795, 522, 1112, 554)]),
    "bug02-timezone-expense": ("79d-expense-october.png", [(980, 138, 1172, 176), (570, 568, 722, 830)]),
    "bug04-card-does-nothing": ("52-visitor-card-click.png", [(613, 495, 827, 745)]),
    "bug05-06-duplicate-and-price": ("40-dog-appt-after-sys.png", [(15, 170, 1424, 265), (54, 345, 1386, 405), (54, 727, 1386, 763)]),
    "bug07-salary-missing": ("78-expense-income-nocat.png", [(1060, 80, 1416, 133), (740, 498, 1138, 534)]),
    "bug08-sample-data": ("79d-expense-october.png", [(515, 255, 800, 310), (515, 775, 1415, 830)]),
    "bug10-plans": ("88-plan-options.png", [(496, 206, 944, 274), (796, 796, 946, 832)]),
    "bug12-fake-preview": ("73-expense-done.png", [(437, 60, 1440, 860)]),
    "bug13-wheel": ("21-es-child-grid.png", [(54, 680, 1386, 733)]),
    "bug14-errors-on-load": ("17-es-add-pedido.png", [(54, 240, 1386, 318), (54, 420, 1386, 585)]),
    "bug15-untranslated": ("15-es-runtime-home.png", [(10, 55, 240, 85), (400, 55, 600, 85)]),
    "bug19-option-text": ("12-es-split-option-bug.png", [(61, 529, 461, 579)]),
    "bug23-status-display": ("27-es-dashboard-detail.png", [(410, 528, 533, 566), (1195, 700, 1262, 735)]),
    "bug25-sys-column": ("43-dog-dashboard-with-data.png", [(25, 192, 225, 280)]),
}


def font(size: int):
    for name in ("segoeuib.ttf", "arialbd.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def annotate(src: Path, boxes, dest: Path) -> None:
    im = Image.open(src).convert("RGB")
    draw = ImageDraw.Draw(im)
    label_font = font(22)
    for n, (x1, y1, x2, y2) in enumerate(boxes, start=1):
        draw.rounded_rectangle((x1, y1, x2, y2), radius=8, outline=RED, width=5)
        cx, cy, r = x2 - 4, y1 + 4, 17
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=RED)
        draw.text((cx, cy), str(n), fill="white", font=label_font, anchor="mm")
    scale = OUT_WIDTH / im.width
    im = im.resize((OUT_WIDTH, round(im.height * scale)), Image.LANCZOS)
    im.save(dest.with_suffix(".jpg"), quality=85, optimize=True)


if __name__ == "__main__":
    out = Path("fig")
    out.mkdir(exist_ok=True)
    for name, (src, boxes) in FIGURES.items():
        annotate(Path(src), boxes, out / f"{name}.png")
        print(name)
