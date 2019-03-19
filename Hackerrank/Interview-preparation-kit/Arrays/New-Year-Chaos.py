#!/bin/python3
# bribe count 

# Complete the minimumBribes function below.
#def minimumBribes(q):
def minimumBribes(a):
    cnt = 0
    for i in a:
        if (i-1) - (a.index(i)) > 2:
            return print ("Too chaotic")
        elif (i-1) - (a.index(i)) == 2:
            cnt += 2
        elif (i-1) - (a.index(i)) == 1:
            cnt += 1
            
    return print (cnt)
