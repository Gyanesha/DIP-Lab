import cv2
import numpy as np 

def convo(img,l,b,mask):
	image = np.zeros((l,b,1), np.uint8)
	for i in range(b):
		for j in range(l):
			x,y = (i,j)
			val = 0
			for X in range(x-1,x+2):
				for Y in range(Y-1,Y+2):
					val = 0
					if(X>=0 && X<b && Y>=0 && Y<l):
						val = val + mask[X-x+1][Y-y+1]*img[X][Y]
			if(val > 128):
				image[x][y] = 255
			else:
				image[x][y] = 0
	return image

image= cv2. 
