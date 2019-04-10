# Complete the checkMagazine function below.
# 파이썬 컨테이너(리스트, 딕셔너리, 세트 등)의 동일한 데이터가 몇 개인지 파악하는 모듈로, 결과 값을 딕셔너리 형태(값: 개수)로 리턴
from collections import Counter

def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}:
        return print('Yes')
    else:
        return print('No')
