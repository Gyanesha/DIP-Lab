import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

def threshold(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j]>126:
                image[i][j]=255
            else:
                image[i][j]=0
    return image

def dilate(image):
    movements = [[0, 0], [1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]

    nimage = image[:]
    rows = image.shape[0]
    cols = image.shape[1]
    for i in range(rows):
        for j in range(cols):
            flag = 0

            for k in range(8):
                imagex = i + movements[k][0]
                imagey = j + movements[k][1]

                if (imagey < cols and imagey >= 0) and (imagex < rows and imagex >= 0):
                    if image[imagex][imagey] == 255:
                        flag = 1
                        break

            nimage[i][j] = flag * 255

    return nimage


img=cv2.imread("/home/gp/Desktop/DP/list_two/img2.jpeg",0)
img=threshold(img)
imagem = cv2.bitwise_not(img)
# plt.imread("img3.jpg",cmap="grey")
plt.imshow(img,cmap='gray')
plt.show()


hole_coors=[[33,27]
            [101,22],
            [202,20],
            [50,88]
            [97,110],
            [140,82],
            [256,76],
            [97,112],
            [56,162],
            [130,171],
            [230,130],
            [211,260],
            [29,248],
            [129,253],
            [220,260]]
hole=img[:]
for i in range(hole.shape[0]):
    for j in range(hole.shape[1]):
        hole[i][j]=0
        if [i,j] in hole_coors:
            hole[i][j]=255
# cv2.imshow("hole",imagem)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
acomp = cv2.bitwise_not(img)

holenew=[[]]
while 1 :
    holenew=dilate(hole)
    holenew=cv2.bitwise_and(holenew,acomp)

    if np.array_equal(hole,holenew):
        break
    hole=holenew

filledimage=cv2.bitwise_or(img,holenew)
cv2.imshow("filled",filledimage)
cv2.waitKey(0)
cv2.destroyAllWindows()