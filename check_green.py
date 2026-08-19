from PIL import Image

img = Image.open('assets/nova_finance_mockup.png').convert("RGB")
w, h = img.size

# Let's sample a pixel near the middle-right of the screen to see its color
# E.g. x=1350, y=500
px1 = img.getpixel((1350, 500))
px2 = img.getpixel((1200, 500))
px3 = img.getpixel((1000, 500))
print(f"Pixel at 1350,500: {px1}")
print(f"Pixel at 1200,500: {px2}")
print(f"Pixel at 1000,500: {px3}")
