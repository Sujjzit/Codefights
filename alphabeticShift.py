"""
For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".
"""

def alphabeticShift(inputString):
    char=list(inputString)
    for i in range(len(char)):
        if char[i]=='z':
            char[i]='a'
        else:    
            number=ord(char[i])-ord('a')
            number+=1
            char[i]=chr(number+ord('a'))
        
    return ''.join(char)
