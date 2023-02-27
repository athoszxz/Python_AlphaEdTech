import cv2
import zipfile
import requests
import matplotlib.pyplot as plt
import os
import io
import numpy as np

if os.path.isdir('standard_test_images') is False:
    print('downloading images')

    url = ("http://www.imageprocessingplace.com/downloads_V3/"
           "root_downloads/image_databases/standard_test_images.zip")

    zipName = url.split('database/')

    r = requests.get(url, stream=True)

    z = zipfile.ZipFile(io.BytesIO(r.content))

    z.extractall()

files = ['cameraman.tif', 'peppers_color.tif', 'mandril_color.tif']

images = []
count = 0

for file in files:
    count += 1
    filename, file_extension = os.path.splitext(file)

    if file_extension == '.tif':
        img = cv2.imread(f'./standard_test_images/{file}')
        images.append(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(4, 4))
        plt.title(filename)
        plt.imsave('output/PI03-EX01_{}.jpg'.format(count), img)

imgCinza = np.array(cv2.cvtColor(images[0], cv2.COLOR_BGR2GRAY))
print(f'média níveis cinza "cameraman.tif": {np.average(imgCinza)}')

imgColorida = np.array(cv2.cvtColor(images[1], cv2.COLOR_BGR2RGB))
print(
    f'média faixa vermelho "peppers_color.tif": \
      {np.average(imgColorida[:,:,0])}')
print(
    f'média faixa verde "peppers_color.tif": {np.average(imgColorida[:,:,1])}')
print(
    f'média faixa azul "peppers_color.tif": {np.average(imgColorida[:,:,2])}')

cv2.imwrite("recorteimg.tif", imgColorida[170:240, 200:300])

recortada = cv2.imread("recorteimg.tif")
plt.figure(figsize=(4, 4))
plt.title("recorteimg.tif")
plt.imsave("recorte1.jpg", recortada)

print(f'imagem recortada info:{recortada.shape}')
