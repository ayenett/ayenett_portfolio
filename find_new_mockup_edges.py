from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size
print(f"Image size: {w}x{h}")

# We know the laptop screen is roughly in the middle.
# Let's scan horizontally at y=150, 300, 450 to find the left and right edges.
# The screen is relatively bright (green on left, blue on right) compared to the black bezel.

def find_edges(y):
    left_edge = -1
    right_edge = -1
    for x in range(w//2, 0, -1):
        r, g, b = img.getpixel((x, y))
        # Bezel is very dark
        if r < 20 and g < 20 and b < 20:
            left_edge = x
            break
    for x in range(w//2, w):
        r, g, b = img.getpixel((x, y))
        if r < 20 and g < 20 and b < 20:
            right_edge = x
            break
    return left_edge, right_edge

print("y=150:", find_edges(150))
print("y=300:", find_edges(300))
print("y=450:", find_edges(450))
print("y=500:", find_edges(500))

# Scan vertically at x=400 to find top and bottom edges
def find_v_edges(x):
    top_edge = -1
    bottom_edge = -1
    for y in range(h//2, 0, -1):
        r, g, b = img.getpixel((x, y))
        if r < 20 and g < 20 and b < 20:
            top_edge = y
            break
    for y in range(h//2, h):
        r, g, b = img.getpixel((x, y))
        if r < 20 and g < 20 and b < 20:
            bottom_edge = y
            break
    return top_edge, bottom_edge

print("x=300:", find_v_edges(300))
print("x=500:", find_v_edges(500))

