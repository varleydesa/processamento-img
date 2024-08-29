from PIL import Image

img = Image.open("mulher.jpg")

histograma_r = [0]*256
histograma_g = [0]*256
histograma_b = [0]*256
# divide a imagem em 3 imgs. 1 pra cada banda.
img_r, img_g, img_b = img.split()
img_r.show()
pixels_r = list(img_r.getdata())
pixels_g = list(img_g.getdata())
pixels_b = list(img_b.getdata())

for pixel in pixels_r:
    histograma_r[pixel] +=1

for pixel in pixels_g:
    histograma_g[pixel] +=1

for pixel in pixels_b:
    histograma_b[pixel] +=1


# pip install matplotlib
import matplotlib.pyplot as plot

plot.figure(figsize=(10, 4))

plot.subplot(133)
plot.bar(range(256), histograma_r, color="red")
plot.xlabel("Intensidade")
plot.ylabel("Frequência")
plot.title("Histograma dos tons de vermelho")

plot.subplot(132)
plot.bar(range(256), histograma_g, color="green")
plot.xlabel("Intensidade")
plot.ylabel("Frequência")
plot.title("Histograma dos tons de verde")

plot.subplot(131)
plot.bar(range(256), histograma_b, color="blue")
plot.xlabel("Intensidade")
plot.ylabel("Frequência")
plot.title("Histograma dos tons de azul")
plot.tight_layout()
plot.show()