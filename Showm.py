from cv2 import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mp
import numpy as np
import os

path = "./LPL/"
img_num = len(os.listdir(path))
for i in range(img_num):
    img_name = path + str(i+1) + ".jpg"
    img = cv2.imread(img_name)
    img = cv2.resize(img, (128,128))
    plt.subplot(3,4,i+1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()