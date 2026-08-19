from PIL import Image

img = Image.open('assets/happy_ring_mockup_transparent.png').convert("RGBA")
width, height = img.size
min_x, max_x = width, 0
min_y, max_y = height, 0

found = False
for y in range(height):
    for x in range(width):
        if img.getpixel((x, y))[3] == 0:  # transparent
            found = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if found:
    print(f"BBox: Left={min_x}, Top={min_y}, Right={max_x}, Bottom={max_y}")
    print(f"Width={max_x - min_x}, Height={max_y - min_y}")
else:
    print("No transparent pixels found")
