"""
For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.
"""

def growingPlant(upSpeed, downSpeed, desiredHeight):

    currentHeight = 0
    dayIndex = 1

    while currentHeight + upSpeed < desiredHeight:
        currentHeight +=  upSpeed-downSpeed
        dayIndex += 1

    return dayIndex
