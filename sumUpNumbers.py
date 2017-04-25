"""
Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.
"""

def sumUpNumbers(inputString):
    s=0
    z=0
    for i in inputString:
        if '0'<=i and i<='9':
            s = s*10 + (ord(i)-ord('0'))
        else:
            z+=s
            s=0
    z+=s        
    return z
