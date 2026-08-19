from PIL import Image

img = Image.open('assets/frame.jpg').convert("RGB")
w, h = img.size

# Let's print the colors of a horizontal line across the middle
print("Horizontal line at h//2:")
for x in range(0, w, 100):
    print(f"x={x}: {img.getpixel((x, h//2))}")
