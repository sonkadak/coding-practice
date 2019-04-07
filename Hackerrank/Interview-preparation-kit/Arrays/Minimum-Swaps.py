#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # 정렬된 배열
    ref_arr = sorted(arr)
    # 값: 값의 현재 위치를 나타내는 딕셔너리
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0
    
    for i,v in enumerate(arr):
        # 현재 값의 정렬 완료 위치
        correct_value = ref_arr[i]
        # 현재 값과 정렬된 위치의 값이 다르면
        if v != correct_value:
            # 스왑 할 위치는 현재 값의 정렬된 위치
            to_swap_ix = index_dict[correct_value]
            # 스왑 실행
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
            # 스왑 완료 후 현재 값의 위치는 스왑 된 위치로 수정
            index_dict[v] = to_swap_ix
            # 스왑 된 위치로 수정
            index_dict[correct_value] = i
            # 스왑 카운트
            swaps += 1
            
    return swaps
