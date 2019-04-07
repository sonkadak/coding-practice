#!/bin/python3
# bribe count 

# Complete the minimumBribes function below.
#def minimumBribes(q):
def minimumBribes(a):
    moves = 0
    for i, p in enumerate(q):
        #  현재 위치(i), 원래 위치(p) 비교
        if p - (i + 1) > 2:
            print("Too chaotic")
            return
        # 비교 대상(처음 사람의 원래 위치 부터 현재 위치까지)와 원래 위치(p)와 비교하여 이동이 있을 경우 카운트
        for j in range(max(p-2, 0), i):
            if q[j] > p:
                moves += 1
            
    return print (moves)
