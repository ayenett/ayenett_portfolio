from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

# We will print a 40x20 ASCII art of the image
ascii_chars = " .:-=+*#%@"
out = ""
for y in range(0, h, h//20):
    for x in range(0, w, w//40):
        r, g, b = img.getpixel((x, y))
        brightness = (r + g + b) / (3 * 255)
        char_idx = int(brightness * (len(ascii_chars) - 1))
        out += ascii_chars[char_idx]
    out += "\n"
print(out)
