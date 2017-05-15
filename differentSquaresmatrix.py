"""
For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
"""


def differentSquares(m):
    l=[]
    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
            if not [m[i][j],m[i+1][j],m[i][j+1],m[i+1][j+1]] in l:
                l.append([m[i][j],m[i+1][j],m[i][j+1],m[i+1][j+1]])
    return len(l)
