"""
For message = "taiaiaertkixquxjnfxxdh", the output should be
cipher26(message) = "thisisencryptedmessage".

"""

message = "taiaiaertkixquxjnfxxdh"

def cipher26(message):
    def dig(x):
        return ord(x)-97
    def let(x):
        return chr(x+97)
    
    s = 0
    ans = ''
    for x in message:
        ans += let( (dig(x) - s)%26 )
        s = dig(x)
    return ans
           
print cipher26(message)
