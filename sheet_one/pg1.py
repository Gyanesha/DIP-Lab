import cv2
import numpy as np 

def input_image(address):
    img = cv2.imread(address,0)
    return img

def print_image(text,img):
    cv2.imshow(text,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize_image(per,img,x,y):
    scale_percent = per 
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    
    if (per == 0):
        height = x
        width = y

    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

def add_image(img1,img2,x,y):
    n_img1 = resize_image(0,img1,x,y)
    n_img2 = resize_image(0,img2,x,y)
    for i in range(x):
        for j in range(y):
            n_img1[i][j]=n_img1[i][j]+n_img2[i][j]
    
    return n_img1

def eight_level(img):
    x,y = img.shape
    hold = img.copy()
    for i in range(x):
        for j in range(y):
            hold[i][j]=hold[i][j]/32

    for i in range(1,9):
        h1 = hold
        for p in range(x):
            for q in range(y):
                h1[p][q]=(h1[p][q]*i)%256
        tex = (str)(i)+" image"
        print_image(tex,h1)

def reduce_to(n,img):
    d = 256/n
    x,y = img.shape
    hold = img.copy()
    for i in range(x):
        for j in range(y):
            hold[i][j]=((int)(hold[i][j]/d))*d
    tex = (str)(n)+" image"
    print_image(tex,hold)

def zooming(img,n):
    x,y = img.shape
    n_img = img.copy()
    n_img = resize_image(0,img,n*x,n*y)
    for i in range(n*x):
        for j in range(n*y):
            n_img[i][j] = img[i//n][j//n]
    
    return n_img

def shrinking(img,n):
    x,y = img.shape
    n_img = img.copy()
    n_img = resize_image(0,img,x//n,y//n)
    for i in range(x//n):
        for j in range(y//n):
            n_img[i][j]=img[i*n][j*n]
    
    return n_img

def main():
    img1=input_image("/home/gp/Desktop/DP/img1.jpg")
    # img2=input_image("/home/gp/Desktop/DP/img4.jpeg")
    print_image("First image",img1)
    # img3=add_image(img1,img2,600,1200)
    # print_image("added image",img3)
    eight_level(img1)
    # k =2
    # for i in range(8):
    #     reduce_to(k,img1)
    #     k=k*2
    # print_image("image",img1)
    # z_img= zooming(img1,2)
    # print_image("zoomed image",z_img)
    # s_img= shrinking(img1,2)
    # print_image("shrinked image",s_img)


if __name__=='__main__':
    main()