import cv2
import numpy as np 
import cmath

def take_input():
    print("Enter the number of elements in the list")
    n = int(input())
    l = input().split(" ")
    for i in range(n):
        l[i] = int(l[i])
    return (n,l)

def calculate_DFFT(arr):
    n = len(arr)
    fft = [0]*n
    for i in range(n):
        hold = 0
        for j in range(n):
            hold = hold + cmath.rect(arr[j],(2*22*j*i)/(n*7))
        fft[i] = hold
    return fft

def main():
    n,l = take_input()
    ans = calculate_DFFT(l)
    print(n)
    print(ans)

if __name__ == '__main__':
    main()

