from PIL import Image
import sys

img = Image.open('assets/project_1.png').convert("RGB")
w, h = img.size

# The screen is relatively bright compared to the black bezel.
# Let's find the bounding box of pixels with R+G+B > 50
screen_pixels = []
for y in range(h):
    for x in range(w):
        r, g, b = img.getpixel((x, y))
        # The laptop screen has a bright blue chart
        if b > 50 and r < 100 and g < 150:
            screen_pixels.append((x, y))

if not screen_pixels:
    print("No screen pixels found")
    sys.exit()

# This is a rough estimation. A better way is to find the corners of the quadrilateral.
# Let's print out the extreme points of the screen.
top = min(screen_pixels, key=lambda p: p[1])
bottom = max(screen_pixels, key=lambda p: p[1])
left = min(screen_pixels, key=lambda p: p[0])
right = max(screen_pixels, key=lambda p: p[0])

print(f"Top: {top}")
print(f"Bottom: {bottom}")
print(f"Left: {left}")
print(f"Right: {right}")

# Let's find corners
tl = min(screen_pixels, key=lambda p: p[0] + p[1])
br = max(screen_pixels, key=lambda p: p[0] + p[1])
tr = max(screen_pixels, key=lambda p: p[0] - p[1])
bl = min(screen_pixels, key=lambda p: p[0] - p[1])

print(f"TL: {tl}")
print(f"TR: {tr}")
print(f"BR: {br}")
print(f"BL: {bl}")
