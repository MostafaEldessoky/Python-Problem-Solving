from typing import List

def reverseArray(a: List[int]):
    b: List[int] = [a[len(a)-1-i] for i in range(len(a))] 
    print(b)
    
arr = [1, 2, 3, 4, 5]
reverseArray(arr)