from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
for x in range(600, 800, 10):
    print(f"x={x}: {img.getpixel((x, 300))}")
