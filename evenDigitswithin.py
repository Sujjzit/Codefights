"""
For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
"""


def evenDigitsOnly(n):
    for item in str(n):
        item = int(item)
        if (item/2)*2 != item:
            return False
    return True
