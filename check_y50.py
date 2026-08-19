from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
for x in range(600, 800, 10):
    print(f"x={x}, y=50: {img.getpixel((x, 50))}")
