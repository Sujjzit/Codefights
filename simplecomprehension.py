"""
For a = [4, 5, 6, 7, 8] and b = [8, 9, 10, 11, 12],
the output should be
coolPairs(a, b) = 2.

"""


def coolPairs(a, b):
    uniqueSums = {i+j for i in a for j in b if (i * j) % (i + j) == 0 }
    return len(uniqueSums)
