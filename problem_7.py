

def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        d1 += arr[i][i]
        d2 += arr[i][len(arr)-i-1]
    return abs(d1-d2)