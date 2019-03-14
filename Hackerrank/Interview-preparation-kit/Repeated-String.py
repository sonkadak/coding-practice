#!/bin/python3

# Complete the repeatedString function below.
def repeatedString(s, n):
	# quota - count of 'a'
    cnt = s.count('a') * (n // len(s))

	# for remainder
    cnt += s[:n % len(s)].count('a')

    return cnt
