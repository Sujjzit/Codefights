"""
Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
"""

def validTime(time):

    def charToInt(symbol):
        return ord(symbol) - ord('0')

    hours = charToInt(time[0]) * 10 + charToInt(time[1])
    minutes = charToInt(time[3]) * 10 + charToInt(time[4])

    if hours < 24 and minutes < 60:
        return True
    return False
