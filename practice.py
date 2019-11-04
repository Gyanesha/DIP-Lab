import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def find_freq(img):
    val =[0]*256
    x,y = img.shape
    for i in range(x):
        for j in range(y):
            v = img[i][j]
            val[v] = val[v]+1
    total = x*y
    cumu =[0]*256
    cumu[0] = val[0]/total
    for i in range(1,256):
        cumu[i] = (val[i]/total)+cumu[i-1]
    return (val,cumu)

def histogram_equilization(img):
    fre,cfre = find_freq(img)
    cdf = [0]*256
    for i in range(256):
        cdf[i] = (int)(255*cfre[i])
    x,y = img.shape
    n_img = img.copy()
    for i in range(x):
        for j in range(y):
            v = img[i][j]
            f = fre[v]
            inten = cdf[v]
            n_img[i][j] = inten
    cv2.imshow("normal",img)
    cv2.imshow("equalized",n_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def histogram_specialisation(img1,img2):
    fre1,cum1= find_freq(img1)
    fre2,cum2= find_freq(img2)
    plt.hist(fre1,bins=100)
    plt.ylabel("Frequency")
    plt.show()
    val1= [0]*256
    val2= [0]*256
    for i in range(256):
        val1[i]= int(cum1[i]*255)

    for i in range(256):
        val2[i]= int(cum2[i]*255)

    mapping= [0]*256

    for i in range(256):
        val=val1[i]
        dif = 256
        index = 0
        for j in range(256):
            h = abs(val-val2[j])
            if(h> dif):
                mapping[i]=index
                break
            else:
                dif=h
                index=j
    n_img = img1.copy()
    x,y = img1.shape
    for i in range(x):
        for j in range(y):
            val=img1[i][j]
            n_img[i][j] = mapping[val]
    cv2.imshow("target image",img2)
    cv2.imshow("specialised image",n_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def negative_intensity(img):
    n_img = img.copy()
    x,y = n_img.shape
    for i in range(x):
        for j in range(y):
            n_img[i][j] = 255-n_img[i][j]
    return n_img

def gamma(img,n):
    n_img = img.copy()
    x,y = n_img.shape
    for i in range(x):
        for j in range(y):
            v = img[i][j]
            f = v/255
            n_img[i][j] = int(255*(f**n))
            # n_img[i][j] = int((img[i][j]**(1.1)))
    return n_img

def logar(img):
    n_img = img.copy()
    x,y = n_img.shape
    for i in range(x):
        for j in range(y):
            v = img[i][j]
            f = v/255
            n_img[i][j] = int(25*math.log(1+v))
            # n_img[i][j] = int((img[i][j]**(1.1)))
    return n_img

def piece_wise(img):
    n_img = img.copy()
    x,y = img.shape
    for i in range(x):
        for j in range(y):
            if(img[i][j]>=128):
                n_img[i][j]=255
            else:
                n_img[i][j]=0
    return n_img

img1 = cv2.imread("/home/gp/Desktop/DP/img1.jpg",0)
img = piece_wise(img1)
# print(img)
img2 = cv2.imread("/home/gp/Desktop/DP/img2.jpeg",0)
# img = histogram_specialisation(img2,img1)
# # cv2.imshow("img1",img1)
# # cv2.imshow("img2",img2)

# img2 = img1.copy()
# img3 = img1.copy()
# img4 = img1.copy()


# img2[:, :, 1] = 0
# img2[:, :, 2] = 0


# img3[:, :, 0] = 0
# img3[:, :, 2] = 0

# img4[:, :, 0] = 0
# img4[:, :, 1] = 0
# img2 = img2+img3+img4
cv2.imshow("img",img)
# cv2.imshow("nimg",img)
# cv2.imshow("img3",img3)
# cv2.imshow("img4",img4)


cv2.waitKey(0)
cv2.destroyAllWindows()