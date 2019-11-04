import cv2
import numpy as np

img = cv2.imread('/home/gp/Desktop/DP/list_three/img3.jpeg',0)
dim = (img.shape)

laplacian = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]


new = np.zeros((dim[0],dim[1]))

for x in range(1,dim[0]-1) :
  for y in range(1,dim[1]-1) :
    pixel_x = ((laplacian[0][0] * img[x-1][y-1]) + (laplacian[0][1] * img[x][y-1]) +(laplacian[0][2] * img[x+1][y-1])+
              (laplacian[1][0] * img[x-1][y])   + (laplacian[1][1] * img[x][y]) + (laplacian[1][2] * img[x+1][y]) +
              (laplacian[2][0] * img[x-1][y+1])   + (laplacian[2][1] * img[x][y+1]) + (laplacian[2][2] * img[x+1][y+1]) )

    val = pixel_x
    new[x,y] = np.ceil(val)


cv2.imshow('Image', new)
cv2.waitKey(0)
cv2.destroyAllWindows()
