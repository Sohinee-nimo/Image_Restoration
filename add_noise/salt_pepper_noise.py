import random
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#function to add noise
def add_noise(img):
 
    # Getting the dimensions of the image
    row , col = img.shape
     
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    #number_of_pixels = random.randint(128, 16384)
    number_of_pixels = 1638
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to white
        img[y_coord][x_coord] = 255
         
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    #number_of_pixels = random.randint(128, 16384)
    number_of_pixels = 1638 
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to black
        img[y_coord][x_coord] = 0
         
    return img
 
#Read the image
img = cv2.imread('rayleigh.jpg',
                 cv2.IMREAD_GRAYSCALE)
#Display Image
cv2.imshow('sample image',img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()
#Adding the noise
img2 = cv2.imwrite('noised.tif',
            add_noise(img))


cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()
#display noised image
img3 = cv2.imread('noised.tif')
cv2.imshow('noised',img3)
cv2.waitKey(0)
