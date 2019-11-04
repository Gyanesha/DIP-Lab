import cv2 
import numpy as np

img = cv2.imread("/home/gp/Desktop/DP/img1.jpeg",0)

kernelh = np.array([[-1, 2, -1], 
                    [-1, 2, -1], 
                    [-1, 2, -1]], np.int32)
kernelv = np.array([[-1, -1, -1], 
                    [2, 2, 2], 
                    [-1, -1, -1]], np.int32)
dstimg = cv2.filter2D(img,-1,kernelh)
dst2img = cv2.filter2D(img,-1,kernelv)
cv2.imshow('Input Image' , img)
cv2.imshow('Detection Vertical' , dstimg)
cv2.imshow('Detection Horizontal' , dst2img)
cv2.waitKey(0)
