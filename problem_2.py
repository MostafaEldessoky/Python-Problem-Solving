from typing import List


def hourglassSum(arr:List[List[int]]):
    max = -10000000000
    for i in range(1,5):
        for j in range(1,5):
            sum = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j+1]
            if sum > max:
                max = sum   
    print(max)
            
    
arr:List[List[int]] = [[-1, -1, 0, -9, -2, -2],[-2, -1, -6, -8, -2, -5],[-1, -1, -1, -2, -3, -4],[-1, -9, -2, -4, -4, -5],[-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]
hourglassSum(arr)