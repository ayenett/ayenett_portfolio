from PIL import Image
import sys

img1 = Image.open('assets/nova_finance_mockup_new.png').convert("RGB")
img2 = Image.open('assets/project_1.png').convert("RGB")

print("nova_finance_mockup_new.png at 640,300:", img1.getpixel((640, 300)))
print("project_1.png at 640,300:", img2.getpixel((640, 300)))

# Let's print a few more pixels to see if they are the exact same image content
print("nova_finance_mockup_new.png at 100,100:", img1.getpixel((100, 100)))
print("project_1.png at 100,100:", img2.getpixel((100, 100)))
