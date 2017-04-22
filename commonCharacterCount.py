"""Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def commonCharacterCount(s1, s2):
    d=0
    s=list(set(s1))
    for x in s:
        d=d+min(s1.count(x),s2.count(x))
    return d
