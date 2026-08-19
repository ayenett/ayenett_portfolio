from PIL import Image

img = Image.open('assets/project_1.png').convert("RGB")
print("Size of project_1.png:", img.size)
print("Color at 100,300:", img.getpixel((100,300)))
