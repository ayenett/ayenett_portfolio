import sys
from PIL import Image

def analyze(img_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()
    width, height = img.size
    print(f"Size: {width}x{height}")
    
    green_pixels = []
    for y in range(height):
        for x in range(width):
            item = datas[y * width + x]
            # Is it transparent?
            if item[3] == 0:
                green_pixels.append((x, y))
                
    if not green_pixels:
        print("No transparent pixels.")
        return
        
    tl = min(green_pixels, key=lambda p: p[0] + p[1])
    br = max(green_pixels, key=lambda p: p[0] + p[1])
    tr = max(green_pixels, key=lambda p: p[0] - p[1])
    bl = min(green_pixels, key=lambda p: p[0] - p[1])
    print(f"TL: {tl}, TR: {tr}, BR: {br}, BL: {bl}")
    
    min_x = min(p[0] for p in green_pixels)
    max_x = max(p[0] for p in green_pixels)
    min_y = min(p[1] for p in green_pixels)
    max_y = max(p[1] for p in green_pixels)
    print(f"Bounding box: left={min_x}, right={max_x}, top={min_y}, bottom={max_y}")

analyze('assets/nova_finance_mockup_transparent.png')
