import cv2
#import numpy as np

# Leitura de imagem
img = cv2.imread('7.png')

# Aplicação de filtos 
#median = cv2.medianBlur(img, 1)
#median = cv2.medianBlur(median, 3)

#  Mostrar imagens
cv2.imshow('Imagen Original', img)
#cv2.imshow('Imagem Com Filtros', median)

cv2.waitKey(0)
cv2.destroyAllWindows