import cv2
import numpy as np
import copy

def threshold(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j]>126:
                image[i][j]=255
            else:
                image[i][j]=0
    return image

def erode(image):

    movements=[[0,0],[1,0],[0,1],[1,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]]

    nimage=copy.deepcopy(image)
    rows=image.shape[0]
    cols=image.shape[1]
    for i in range(rows):
        for j in range(cols):
            flag=1

            for k in range(8):
                imagex=i+movements[k][0]
                imagey=j+movements[k][1]

                if (imagey<cols and imagey>=0) and (imagex<rows and imagex>=0):
                    if image[imagex][imagey]==0:
                        flag=0
                        break

            nimage[i][j]=flag*255

    return nimage


def dilate(image):
    movements = [[0, 0], [1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]

    nimage = copy.deepcopy(image)
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

def bounds(dilated, eroded):
    result = dilated[:]

    rows=dilated.shape[0]
    cols=dilated.shape[1]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = max(0, dilated[i][j] - eroded[i][j])
    return result

img=cv2.imread("/home/gp/Desktop/DP/list_two/img2.jpeg",0)
img=threshold(img)

cv2.imshow("original",img)
#
newimage=erode(img)
cv2.imshow("eroded",newimage)
# cv2.imshow('cv2Erosion', img_erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

dilimage=dilate(img)
cv2.imshow("dilated",dilimage)
# cv2.imshow('cv2dilation', img_dilation)


openingImage=dilate(erode(img))
cv2.imshow("opening",openingImage)


er_image=erode(img)
dil_image=dilate(img)

boundaryimage=bounds(img,er_image)
cv2.imshow("boundary",boundaryimage)
cv2.waitKey(0)
cv2.destroyAllWindows()