import cv2
# import matplotlib.pyplot as plt
# from PIL import Image

# Ler uma imagem
img = cv2.imread('Fmo6I9FXkAEOdG0.jpg')
# img = Image.open('Fmo6I9FXkAEOdG0.jpg')
# plt.imshow(img)

# Salvar uma imagem sem alterações em uma pasta chamada 'output'
cv2.imwrite('output/Fmo6I9FXkAEOdG0_4.png', img)
# img.save('output/Fmo6I9FXkAEOdG0_salva5.png')
# plt.imsave('output/Fmo6I9FXkAEOdG0_salva4.png', img)

# Salvar uma imagem em escala de cinza
# plt.imsave('Fmo6I9FXkAEOdG0_salva_cinza.png', img, cmap='gray')
