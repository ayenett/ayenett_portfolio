from PIL import Image

def remove_green():
    img = Image.open('assets/happy_ring_mockup.png').convert("RGBA")
    datas = img.getdata()

    newData = []
    # Find typical green screen colors: high G, lower R and B
    for item in datas:
        # item is (R, G, B, A)
        if item[1] > 100 and item[1] > item[0] * 1.5 and item[1] > item[2] * 1.5:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("assets/happy_ring_mockup_transparent.png", "PNG")
    print("Done")

remove_green()
