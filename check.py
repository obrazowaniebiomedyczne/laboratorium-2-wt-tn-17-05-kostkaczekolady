from solution import *
import cv2
from obpng import read_png, write_png
# import math

print("- Ocena dostateczna")
renew_pictures()


print("- Ocena dobra")
image = cv2.imread('figures/crushed.png', 0)
erosion = own_simple_erosion(image)
write_png(erosion, 'results/own_simple_erosion.png')
