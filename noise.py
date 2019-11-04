import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("/home/gp/Desktop/DP/img4.jpeg",0)
row,col= image.shape
mean = 0
var = 1
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col))
gauss = gauss.reshape(row,col)
noisy = image + gauss
smooth_part = noisy[:100, :100]

cv2.imshow("image",image)
cv2.imshow("corner",smooth_part)
cv2.imshow("gaussian",noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(smooth_part.ravel(),256,[0,256])
plt.show()