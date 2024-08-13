from PIL import Image

WHITE = (255,255,255)
RED = (188,0,45)

def japao(largura):
    altura = (2*largura)//3
    img = Image.new("RGB", (largura, altura),WHITE)
    raio = 3*altura//10
    centro = (largura//2, altura//2)
    a = centro[0]
    b = centro[1]

    for x in range(a-raio, a+raio):
        for y in range(b-raio, b+raio):
            if (raio**2 >= (y-b)**2 + (x-a)**2):
                img.putpixel((x,y), RED)


    return img

japao(900).show()