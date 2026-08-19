from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

# Scan y=300 from x=100 to 800 and print all pixels
print(f"Image size: {w}x{h}")
for x in range(100, 800, 20):
    print(f"x={x}: {img.getpixel((x, 300))}")
