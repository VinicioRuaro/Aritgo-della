import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

#leitura da Imagem
img = cv2.imread('7.png',)


#tranformar em cinza
imgcinza = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

#treshHold
ret,efe1 = cv2.threshold(imgcinza,127,255,cv2.THRESH_BINARY)
ret,efe2 = cv2.threshold(imgcinza,127,255,cv2.THRESH_BINARY_INV)

#Print
titles = ['Imagem Original','Binário','Binário Invertido']
images = [img, efe2, efe1]
for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()