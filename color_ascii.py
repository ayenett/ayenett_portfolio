from PIL import Image

img = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
w, h = img.size

# Let's print ASCII art using colors! Python can output ANSI color codes.
# This will be in the log.
out = ""
for y in range(250, 350, 5):
    for x in range(550, 700, 5):
        r, g, b = img.getpixel((x, y))
        # Use simple ANSI 24-bit color
        out += f"\033[48;2;{r};{g};{b}m  \033[0m"
    out += "\n"
print(out)
