#!/bin/python3

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(0, d):
        tmp = a[0]
        a.pop(0)
        a.append(tmp)

    return a
