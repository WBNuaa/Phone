from cv2 import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mp
import numpy as np
import os

path = "./LPL/"
img_num = len(os.listdir(path))
img1= [[],[]]*12
for i in range(img_num):
    img_name = path + str(i+1) + ".jpg"
    img = cv2.imread(img_name)
    img = cv2.resize(img, (256,256))
    img1[i] = img
    '''
    cv2.imshow("Result",img)
    cv2.waitKey(1000)
    plt.subplot(3,4,i+1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    '''
imgs = np.hstack([img1])
cv2.imshow("Result",imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()

