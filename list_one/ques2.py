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
    return fft

def main():
    x,y,l = take_input()
    ans = calculate_DFFT(x,y,l)
    print(ans)

if __name__ == '__main__':
    main()

