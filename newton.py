
import math

max_list = []
N, R = input().split(" ")
array = list(map(int, input().split(" ")))
temp  = array
for i in range(1,int(R)+1):
    for j in range(0,int(N)):
        temp = array
        print("array ", array, temp)
        temp[j] = i
        print("After",temp)
