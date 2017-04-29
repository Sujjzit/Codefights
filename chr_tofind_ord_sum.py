"""
For word = "hello", the output should be
wordPower(word) = 52.

Letters 'h', 'e', 'l' and 'o' have powers 8, 5, 12 and 15, respectively. Thus, the total power of the word is 8 + 5 + 12 + 12 + 15 = 52.

"""
def wordPower(word):
    num = {chr(n):n-96 for n in range(97,123)}
    return sum([num[ch] for ch in word])
