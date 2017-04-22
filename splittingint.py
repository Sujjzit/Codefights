Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.

def isLucky(n):
    return sum(map(int, list(str(n)[:(len(str(n))/2)]))) == sum(map(int, list(str(n)[(len(str(n))/2):])))
