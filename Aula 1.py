from PIL import Image

img1 = Image.open("einstein.jpg")
img2 = Image.open("einstein.png")

for x in range(img1.width):
    for y in range(img1.height):
        if y == x :
            img1.putpixel((x,y), (255,0,0))


print(img1.getpixel((400,300),))
print(img2.getpixel((400,300)))
img1.show()