from PIL import Image

img = Image.open('assets/frame.jpg').convert("RGB")
w, h = img.size
for x in range(w-20, w):
    print(f"x={x}: {img.getpixel((x, h//2))}")
