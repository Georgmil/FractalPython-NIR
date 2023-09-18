import numpy as np
import matplotlib.pyplot as plt


def funcija(x1, y1, size, img):
    for x in range(x1, x1+size):
        for y in range(y1, y1+size):
            img[x, y] = 0
    return img


glubina= int(input("Level: "))
size = 3**glubina

img = np.ones((size, size), dtype=np.uint8)

for i in range(1, glubina+1):
    square_size = int(size/(3**i))
    for x in range(0, 3**i, 3):
        x = int((x+1)*square_size)
        for y in range(0, 3**i, 3):
            y = int((y+1)*square_size)
            img = funcija(x, y, square_size, img)


plt.axis('off')
plt.imshow(img, cmap='binary')
plt.imsave('Kover Serpinskogo', img, cmap='binary')
plt.show()