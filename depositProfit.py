"""
For deposit = 100, rate = 20 and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.
"""

def depositProfit(deposit, rate, threshold):
    year=0
    while deposit<threshold:
        deposit=deposit+(deposit*(rate))/100
        year+=1
    return year
