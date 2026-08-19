from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

# We know the laptop screen top edge passes through (193, 151) and (628, 148).
# It's a straight line. Let's trace it to the right until it hits the black bezel.
# We also know the bottom edge passes through (166, 430) and (616, 455).

def is_bezel(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return True
    r, g, b = img.getpixel((x, int(y)))
    return r < 20 and g < 20 and b < 20

# Trace top edge
top_slope = (148 - 151) / (628 - 193)
top_y = lambda x: 151 + top_slope * (x - 193)

top_right_x = 628
while top_right_x < w and not is_bezel(top_right_x, top_y(top_right_x)):
    top_right_x += 1

print(f"Top right corner: ({top_right_x}, {top_y(top_right_x)})")

# Trace bottom edge
bottom_slope = (455 - 430) / (616 - 166)
bottom_y = lambda x: 430 + bottom_slope * (x - 166)

bottom_right_x = 616
while bottom_right_x < w and not is_bezel(bottom_right_x, bottom_y(bottom_right_x)):
    bottom_right_x += 1

print(f"Bottom right corner: ({bottom_right_x}, {bottom_y(bottom_right_x)})")
