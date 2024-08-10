from PIL import Image

BLUE = (0, 87, 184)
YELLOW = (255, 215, 0)
RED = (240, 0, 0)

img = Image.new("RGB",(600,400),BLUE)

for x in range(0, img.width):
    for y in range(img.height//2,img.height):
        img.putpixel((x,y),YELLOW)

img.show()

img2 = Image.new("RGB",(200,140),)
umterco = img2.width//3
for x in range(umterco,img2.width):
    for y in range(img2.height):
        img2.putpixel((x,y),RED)
img2.show()