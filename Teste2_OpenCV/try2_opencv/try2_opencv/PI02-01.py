import cv2
# import matplotlib.pyplot as plt
from skimage import io
# from PIL import Image

urls = ["https://iiif.lib.ncsu.edu/iiif/0052574/full/800,/0/default.jpg",
        "https://iiif.lib.ncsu.edu/iiif/0016007/full/800,/0/default.jpg",
        "https://placekitten.com/800/571"]
count = 0
for url in urls:
    count += 1
    image = io.imread(url)
    image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    final_frame = cv2.hconcat((image, image_2))
    # cv2_imshow(final_frame)
    cv2.imwrite('output/PI02-01_{}.png'.format(count), final_frame)
