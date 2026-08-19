from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size
print(f"Size: {w}x{h}")

# Let's sample some pixels in the middle of the image, where the screen probably is
print("Center pixel:", img.getpixel((w//2, h//2)))
print("Left side of screen?:", img.getpixel((w//3, h//2)))
print("Right side of screen?:", img.getpixel((2*w//3, h//2)))
