#!/bin/python3

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for i in range(0, 16):
        sums.append(0)

    # for sum of 1st line each glasshour
    n = 0
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[i])-2):
            for k in range(j, j+3):
                sums[n] += arr[i][k]
            n += 1
  
    # 2nd line
    n = 0
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[i])-1):
            sums[n] += arr[i][j]
            n += 1

    # 3rd line
    n = 0
    for i in range(2, len(arr)):
        for j in range(0, len(arr[i])-2):
            for k in range(j, j+3):
                sums[n] += arr[i][k]
            n += 1
            
    # return maximum value of list
    return max(sums)
