#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dups = set()  # for duplicated values in 'ar'
    cnts = []     # for duplicated value count
    
    # find duplication
    for i in ar:
        if i not in dups:
            dups.add(i)
    
    # counting each values
    for d in dups:
        cnt = 0
        for i in ar:
            if d == i:
                cnt += 1
        cnts.append(cnt)

    res = 0
    for cnt in cnts:
        if cnt > 1:
            # find value with pairs
            res += int(cnt / 2)
    return res
