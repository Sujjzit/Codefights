"""
For n = 5, the output should be

multiplicationTable(n) = [[1, 2,  3,  4,  5 ], 
                          [2, 4,  6,  8,  10], 
                          [3, 6,  9,  12, 15], 
                          [4, 8,  12, 16, 20], 
                          [5, 10, 15, 20, 25]]
"""

def multiplicationTable(n):
    return [ range(i, n*i + 1, i) for i in xrange(1,1+n) ]
