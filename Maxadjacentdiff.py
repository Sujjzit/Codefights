"""
For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""

def arrayMaximalAdjacentDifference(inputArray):
    result=0
    for i in range(len(inputArray)-1):
        if abs(inputArray[i+1]-inputArray[i])>result:
            result=abs(inputArray[i+1]-inputArray[i])
    return result
