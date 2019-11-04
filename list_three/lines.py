import cv2
import numpy as np
from scipy import ndimage
from math import sqrt

def threshold(img3,T):
    for i in range(len(img3)):
        for j in range(len(img3[0])):
            if img3[i][j] > T:
                img3[i][j] = 255
            else:
                img[i][j] = 0

    return img3

def magnitude(img1,img2):
    newimage=img1[:]
    for i in range(img1.shape[0]):
        for j in range(img.shape[1]):
            newimage[i][j]=sqrt((img1[i][j]**2+img2[i][j]**2))

    return newimage

img=cv2.imread("/home/gp/Desktop/DP/list_two/img1.jpeg",0)
# cv2.imshow("original",img)

vertical_kernel=np.array([[-1,0,1],
                            [-2,0,2],
                            [-1,0,1]])
horizontal_kernel=np.array([[-1,-2,-1],
                         [0,0,0],
                         [1,2,1]])
laplacian_kernel=np.array([[-1,-1,-1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
# img1=np.sum(np.multiply(img, vertical_kernel))
img1=ndimage.convolve(img, vertical_kernel, mode="constant", cval=0)
img2=ndimage.convolve(img, horizontal_kernel, mode="constant", cval=0)
img3=ndimage.convolve(img,laplacian_kernel,mode="constant",cval=0)
cv2.imshow("original",img)
cv2.imshow("vertical",img1)
cv2.imshow("horizontal",img2)

# img4=(img1*img1+img2*img2)**0.5
img4=magnitude(img1,img2)
cv2.imshow("edge",img3)

img3=threshold(img3,5)
cv2.imshow("point",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()