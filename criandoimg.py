from PIL import Image

img = Image.new("RGB",(400,400))

for x in range(0,img.width):
    for y in range(0, img.height):
        if x <= y:
            img.putpixel((x,y),(255,0,0))

img.show()