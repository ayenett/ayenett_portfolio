from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

# The center of the green screen is around x=400, y=300
cx, cy = 400, 300

# Let's cast rays from the center to find the black bezel
# The black bezel is very dark: r,g,b < 20
def is_bezel(x, y):
    if x < 0 or x >= w or y < 0 or y >= h: return True
    r, g, b = img.getpixel((x, y))
    return r < 18 and g < 18 and b < 18

corners = []
# Top-Left: cast ray up-left
for d in range(1000):
    x, y = cx - d, cy - d
    if is_bezel(x, y):
        print(f"Hit bezel at top-left: ({x}, {y})")
        break

# Let's just do a proper scan. We know the screen is a bright quadrilateral surrounded by black.
# We can find the top-left corner by finding the first non-bezel pixel from the top-left of the image?
# No, there might be other things.

# Let's scan horizontally and vertically around the screen.
# We know the screen center is roughly (400, 300).
# Let's trace the top edge by moving up from (400, 300) until we hit bezel.
ty = cy
while not is_bezel(400, ty): ty -= 1
print(f"Top edge at x=400 is y={ty}")

# Trace bottom edge
by = cy
while not is_bezel(400, by): by += 1
print(f"Bottom edge at x=400 is y={by}")

# Trace left edge at y=300
lx = cx
while not is_bezel(lx, 300): lx -= 1
print(f"Left edge at y=300 is x={lx}")

# Trace right edge at y=300
rx = cx
while not is_bezel(rx, 300): rx += 1
print(f"Right edge at y=300 is x={rx}")

# Now follow the left edge UP to find the Top-Left corner
# From (lx+1, 300), move UP and adjust LEFT/RIGHT to stay on the edge
curr_x, curr_y = lx + 1, 300
while curr_y > 0:
    curr_y -= 1
    # Check if we are inside or outside
    while is_bezel(curr_x, curr_y): curr_x += 1
    while not is_bezel(curr_x - 1, curr_y): curr_x -= 1
    # If the top edge is reached, curr_x will suddenly jump right?
    # Actually, the corner is the point with the minimum (x + y)?
    # Let's just collect all edge points!
