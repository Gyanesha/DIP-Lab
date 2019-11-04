import cv2
import numpy as np 
import cmath

def take_input():
    print("Enter the shape of matrix")
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    print("Enter the matrix")
    l = []
    for i in range(x):
        k = input().split(" ")
        l.append(k)
    for i in range(x):
        for j in range(y):
            l[i][j] = int(l[i][j])
    return (x,y,l)

def calculate_DFFT(X,Y,arr):
    fft = np.empty(shape=(X,Y), dtype= np.complex128)
    for x in range(X):
        for y in range(Y):
            hold = 0
            for i in range(X):
                for j in range(Y):
                    hold = hold +cmath.rect(arr[i][j],(-2*(22/7)*((i/X)*x+(j/Y)*y)))
            fft[x][y] = hold
            print(fft[x][y])
    return fft

def main():
    # x,y,l = take_input()
    img = cv2.imread('/home/gp/Desktop/DP/houghlines3.jpg',0)
    print(img)
    print(img.shape)
    cv2.imshow('Image', img)
    scale_percent = 20 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('Resize',resized)
    img = resized
    ans = calculate_DFFT(height,width,img)
    print('Resized Dimensions : ',resized.shape)
    
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # ans = calculate_DFFT(x,y,l)
    # print(ans)

if __name__ == '__main__':
    main()

