"""
Example

For string1 = "aacb" and string2 = "aabc", the output should be
isSubstitutionCipher(string1, string2) = true.

Any ciphertext alphabet that starts with acb... would make this transformation possible.

For string1 = "aa" and string2 = "bc", the output should be
isSubstitutionCipher(string1, string2) = false.
"""

def isSubstitutionCipher(string1, string2):
    d1={}
    d2={}
    for a,b in zip(string1,string2):
        if a in d1 and b!=d1[a]:
            return False
        if b in d2 and a!=d2[b]:
            return False
        d1[a]=b
        d2[b]=a
    return True
    
