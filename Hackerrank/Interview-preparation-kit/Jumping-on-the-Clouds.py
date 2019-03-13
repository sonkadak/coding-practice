#!/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	jump = 0
    	n = 0 	# current location

	while n <= len(c)-2:
		if n == len(c)-2:
		    jump += 1
		    n += 1
		elif c[n] == 1:
		    jump += 1
		    n += 2
		elif c[n+2] == 0:
		    jump += 1
		    n += 2
		else:
		    jump += 1
		    n += 1

	return jump
