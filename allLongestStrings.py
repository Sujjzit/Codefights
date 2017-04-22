"For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"]."


def allLongestStrings(inputArray):
    maxlen=max(map(lambda x: len(x),inputArray)) 
    return filter(lambda x: len(x)==maxlen ,inputArray)
