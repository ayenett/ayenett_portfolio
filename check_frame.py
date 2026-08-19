from PIL import Image

img = Image.open('assets/frame.jpg').convert("RGB")
w, h = img.size
print(f"Frame Size: {w}x{h}")
px1 = img.getpixel((w-10, h//2))
px2 = img.getpixel((w-50, h//2))
print(f"Pixel near right edge (w-10): {px1}")
print(f"Pixel near right edge (w-50): {px2}")
