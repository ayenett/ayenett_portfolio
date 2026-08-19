from PIL import Image

img = Image.open('assets/nova_finance_mockup.png').convert("RGB")
w, h = img.size

# Scan right from 1300 at y=500
for x in range(1300, 1440):
    px = img.getpixel((x, h//2))
    is_green = px[1] > 90 and px[1] > px[0] * 1.3 and px[1] > px[2] * 1.3
    if not is_green:
        print(f"Edge found at x={x}: color {px}")
        break
