import numpy as np
import cv2
from obpng import write_png

# Zadanie na ocenę dostateczną
def renew_pictures():

    im_1 = cv2.imread('figures/crushed.png', 0)
    kernel = np.zeros((3, 3), np.uint8)
    kernel[1, 1] = 1
    kernel[1, 2] = 1
    kernel[1, 0] = 1
    kernel[0, 1] = 1
    kernel[2, 1] = 1

    im_1 = cv2.erode(im_1, kernel, iterations = 1)
    write_png(im_1, 'results/crushed.png')


    im_2 = cv2.imread('figures/crushed2.png', 0)
    im_2 = cv2.dilate(im_2, kernel, iterations = 1)
    im_2 = cv2.erode(im_2, kernel, iterations = 2)
    kernel[1, 1] = 1
    kernel[1, 2] = 1
    kernel[1, 0] = 1
    kernel[0, 1] = 0
    kernel[2, 1] = 0

    im_2 = cv2.erode(im_2, kernel, iterations = 1)
    write_png(im_2, 'results/crushed2.png')


    im_3 = cv2.imread('figures/crushed3.png', 0)
    kernel[1, 1] = 1
    kernel[1, 2] = 1
    kernel[1, 0] = 1
    kernel[0, 1] = 1
    kernel[2, 1] = 1

    im_3 = cv2.morphologyEx(im_3, cv2.MORPH_OPEN, kernel)
    im_3 = cv2.morphologyEx(im_3, cv2.MORPH_CLOSE, kernel)
    im_3 = cv2.erode(im_3, kernel, iterations = 2)

    write_png(im_3, 'results/crushed3.png')
    im_4 = cv2.imread('figures/crushed4.png', 0)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_CLOSE, kernel)

    kernel = np.zeros((3, 3), np.uint8)
    kernel[1, 1] = 1
    kernel[1, 2] = 1
    kernel[1, 0] = 1
    kernel[0, 1] = 1
    kernel[2, 1] = 1

    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_OPEN, kernel)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_CLOSE, kernel)
    im_4 = cv2.erode(im_4, kernel, iterations = 2)
    im_4 = cv2.dilate(im_4, kernel, iterations = 1)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_CLOSE, kernel)
    im_4 = cv2.dilate(im_4, kernel, iterations = 1)
    im_4 = cv2.erode(im_4, kernel, iterations = 1)
    im_4 = cv2.erode(im_4, kernel, iterations = 2)
    im_4 = cv2.dilate(im_4, kernel, iterations = 1)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_OPEN, kernel)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_OPEN, kernel)
    im_4 = cv2.dilate(im_4, kernel, iterations = 1)

    write_png(im_4, 'results/crushed4.png')
    pass


# Zadanie na ocenę dobrą
def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)

    kernel = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ])
    O_y = (kernel.shape[0] - 1) // 2
    O_x = (kernel.shape[1] - 1) // 2

    for (y, x) in np.ndindex(image.shape):
        flag = False
        for ky in range(kernel.shape[0] - 1):
            for kx in range(kernel.shape[1] - 1):
                try:
                    val = image[y - ky + O_y][x - kx + O_x]
                    if val == 0:
                        flag = True
                except:
                    pass
        if flag:
            new_image[y][x] = 0
        else:
            new_image[y][x] = image[y][x]

    return new_image

