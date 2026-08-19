from PIL import Image

img = Image.open('assets/nova_finance_mockup.png').convert("RGB")
w, h = img.size

# Let's check pixels from x=1300 to x=1400 at y=500 to see what the laptop bezel looks like.
print("Checking y=500 from 1340 to 1380:")
for x in range(1340, 1380):
    px = img.getpixel((x, 500))
    print(f"x={x}: {px}")
