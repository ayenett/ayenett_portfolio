from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

def is_bezel(x, y):
    if x < 0 or x >= w or y < 0 or y >= h: return True
    r, g, b = img.getpixel((x, y))
    # Bezel is very dark black/gray
    return r < 25 and g < 25 and b < 25

screen_pixels = []
for y in range(50, 600):
    for x in range(50, 800):
        # Center of screen is roughly (400,300), let's just do a flood fill again but stricter
        pass

visited = set()
queue = [(400, 300)]
visited.add((400, 300))

while queue:
    x, y = queue.pop(0)
    screen_pixels.append((x, y))
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
            if not is_bezel(nx, ny):
                # Also exclude the pegboard, which is blue/purple and outside the laptop
                # The pegboard is roughly r<50, g<50, b>50
                r, g, b = img.getpixel((nx, ny))
                if r < 40 and g < 40 and b > 50:
                    continue
                visited.add((nx, ny))
                queue.append((nx, ny))

if not screen_pixels:
    print("Failed to find screen")
else:
    # Find exact corners
    # TL: min(x+y), TR: max(x-y), BR: max(x+y), BL: min(x-y)
    tl = min(screen_pixels, key=lambda p: p[0] + p[1])
    br = max(screen_pixels, key=lambda p: p[0] + p[1])
    tr = max(screen_pixels, key=lambda p: p[0] - p[1])
    bl = min(screen_pixels, key=lambda p: p[0] - p[1])
    
    print(f"TL: {tl}")
    print(f"TR: {tr}")
    print(f"BR: {br}")
    print(f"BL: {bl}")
