import numpy as np
import cv2
from obpng import write_png, read_png


# Zadanie na ocenę dostateczną
def renew_pictures():

    # ---------------
    # Do uzupełnienia
    # ---------------
    im_1 = cv2.imread('figures/crushed.png',0)

    kernel = np.zeros((3,3),np.uint8)    
    kernel[1,1] = 1
    kernel[1,2] = 1
    kernel[1,0] = 1
    kernel[0,1] = 1
    kernel[2,1] = 1
    im_1 = cv2.erode(im_1, kernel, iterations = 1)

    write_png(im_1, 'results/crushed.png')

    im_2 = cv2.imread('figures/crushed2.png',0)
    im_2 = cv2.dilate(im_2,kernel,iterations = 1)
    im_2 = cv2.erode(im_2, kernel, iterations = 2)
    kernel[1,1] = 1
    kernel[1,2] = 1
    kernel[1,0] = 1
    kernel[0,1] = 0
    kernel[2,1] = 0
    im_2 = cv2.erode(im_2, kernel, iterations = 1)

    write_png(im_2, 'results/crushed2.png')

    im_3 = cv2.imread('figures/crushed3.png',0)

    kernel[1,1] = 1
    kernel[1,2] = 1
    kernel[1,0] = 1
    kernel[0,1] = 1
    kernel[2,1] = 1    

    im_3 = cv2.morphologyEx(im_3, cv2.MORPH_OPEN, kernel)
    im_3 = cv2.morphologyEx(im_3, cv2.MORPH_CLOSE, kernel)
    im_3 = cv2.erode(im_3, kernel, iterations = 2)

    write_png(im_3, 'results/crushed3.png')


    im_4 = cv2.imread('figures/crushed4.png',0)

    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_CLOSE, kernel)

    kernel = np.zeros((3,3),np.uint8)    
    kernel[1,1] = 1
    kernel[1,2] = 1
    kernel[1,0] = 1
    kernel[0,1] = 1
    kernel[2,1] = 1

    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_OPEN, kernel)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_CLOSE, kernel)
    im_4 = cv2.erode(im_4, kernel, iterations = 2)
    im_4 = cv2.dilate(im_4,kernel,iterations = 1)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_CLOSE, kernel)
    im_4 = cv2.dilate(im_4,kernel,iterations = 1)
    im_4 = cv2.erode(im_4, kernel, iterations = 1)
    im_4 = cv2.erode(im_4, kernel, iterations = 2)
    im_4 = cv2.dilate(im_4,kernel,iterations = 1)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_OPEN, kernel)
    im_4 = cv2.morphologyEx(im_4, cv2.MORPH_OPEN, kernel)
    im_4 = cv2.dilate(im_4,kernel,iterations = 1)

    write_png(im_4, 'results/crushed4.png')

    pass


# Zadanie na ocenę dobrą
def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)

    kernel = np.array([[0, 1, 0],
                       [1, 1, 1],
                       [0, 1, 0]])

    x = image.shape[0]
    y = image.shape[1]

    for i in range (0, x):
        for j in range (0, y):
            if i>0 and i < x-1 and j>0 and j<y-1:
                if image[i, j-1] != 0 and image[i, j+1] != 0 and image[i-1,j] != 0 and image[i+1,j] != 0 and image[i,j] != 0:
                    new_image[i,j] = 255
                else:
                    new_image[i,j] = 0
            else:
                if i == 0 and j == 0:
                    if image[0,1] != 0 and image[1,0] != 0 and image[0,0] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0
                elif i == 0 and j == y-1:
                    if image[0,y-2] != 0 and image[1, y-1] != 0 and image[i,j] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0
                elif i == x-1 and j == 0:
                    if image[x-2,0] != 0 and image[x-1,1] != 0 and image[i,j] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0
                elif i == x-1 and j == y-1:
                    if image[x-1, y-2] != 0 and image[x-2, y-1] != 0 and image[i,j] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0
                elif i == 0:
                    if image[i, j-1] != 0 and image[i+1, j] != 0 and image[i, j+1] != 0 and image[i,j] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0
                elif i == x-1:
                    if image[i, j-1] != 0 and image[i-1, j] != 0 and image[i, j+1] != 0 and image[i,j] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0
                elif j == 0:
                    if image[i-1, j] != 0 and image[i+1, j] != 0 and image[i, j+1] != 0 and image[i,j] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0
                elif j == y-1:
                    if image[i-1, j] != 0 and image[i+1, j] != 0 and image[i, j-1] != 0 and image[i,j] != 0:
                        new_image[i,j] = 255
                    else:
                        new_image[i,j] = 0                                                                           
                    


    return new_image


# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])

    # ---------------
    # Do uzupełnienia
    # ---------------

    return new_image
