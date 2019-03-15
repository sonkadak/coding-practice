#!/bin/python3

# Complete the countingValleys function below.
def countingValleys(n, s):
    # current location
    loc = 0
    # number of vallies
    valley = 0
    
    # hike
    for i in s:
      if i == "U":
          loc += 1
      elif i == "D":
          loc -= 1
      if loc == 0:
        if i == "U":
          valley += 1

    return int(valley)
