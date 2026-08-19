from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

# We will look for the black bezel. The bezel is very dark (r,g,b < 20).
# The screen is inside the bezel.
screen_pixels = []

for y in range(h//4, 3*h//4):
    for x in range(w//4, 3*w//4):
        r, g, b = img.getpixel((x, y))
        # The bezel is dark. The right side of the screen is dark grey (around 40,40,40).
        # So anything brighter than the bezel is the screen!
        if r > 20 or g > 20 or b > 20:
            # Also exclude the pegboard background (which is purple/blue)
            # The pegboard is on the outside.
            pass

# A better way is to just use a flood fill from the center of the screen!
# The center of the screen is at w//2, h//2.
# Let's do a simple BFS to find all pixels connected to the center that are NOT bezel.

visited = set()
queue = [(w//2, h//2)]
visited.add((w//2, h//2))
screen_pixels = []

while queue:
    x, y = queue.pop(0)
    screen_pixels.append((x, y))
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
            r, g, b = img.getpixel((nx, ny))
            # Stop if we hit the dark bezel
            if r < 18 and g < 18 and b < 18:
                continue
            # Stop if we hit the purple pegboard (just in case the bezel is broken)
            # Pegboard is blue-ish
            if b > r * 2 and b > g * 2 and b > 50:
                continue
            visited.add((nx, ny))
            queue.append((nx, ny))

print(f"Found {len(screen_pixels)} screen pixels.")
if screen_pixels:
    tl = min(screen_pixels, key=lambda p: p[0] + p[1])
    br = max(screen_pixels, key=lambda p: p[0] + p[1])
    tr = max(screen_pixels, key=lambda p: p[0] - p[1])
    bl = min(screen_pixels, key=lambda p: p[0] - p[1])
    print(f"TL: {tl}, TR: {tr}, BR: {br}, BL: {bl}")
