from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

# Let's check a horizontal line at y=300
print("Scanning y=300:")
for x in range(100, 800, 50):
    px = img.getpixel((x, 300))
    is_green = px[1] > 90 and px[1] > px[0] * 1.2 and px[1] > px[2] * 1.2
    print(f"x={x}: color {px}, is_green={is_green}")
