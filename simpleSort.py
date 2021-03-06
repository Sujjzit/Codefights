"""
For arr = [2, 4, 1, 5], the output should be
simpleSort(arr) = [1, 2, 4, 5].
"""

def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            j += 1
    return arr
