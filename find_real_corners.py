from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

screen_pixels = []
for y in range(50, h-50):
    for x in range(50, w-50):
        r, g, b = img.getpixel((x, y))
        # Exclude dark pixels (bezel) and purple background
        if not (r < 30 and g < 30 and b < 30) and not (r < 50 and g < 20 and b > 100):
            # Maybe the screen is somewhat bright.
            if r + g + b > 150:
                screen_pixels.append((x, y))

if screen_pixels:
    tl = min(screen_pixels, key=lambda p: p[0] + p[1])
    br = max(screen_pixels, key=lambda p: p[0] + p[1])
    tr = max(screen_pixels, key=lambda p: p[0] - p[1])
    bl = min(screen_pixels, key=lambda p: p[0] - p[1])
    print(f"TL: {tl}, TR: {tr}, BR: {br}, BL: {bl}")
else:
    print("No screen pixels found")
