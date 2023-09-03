from os import *
from sys import *
from collections import *
from math import *

def ceilingInSortedArray(n, x, arr):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = low + mid // 2
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans 
def floorInSortedArray(n, x, arr):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = low + high // 2
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return -1
def getFloorAndCeil(arr, n, x):
    f = floorInSortedArray(arr, n, x)
    c = ceilingInSortedArray(arr, n, x)
    return (f , c)
result = getFloorAndCeil([2, 3, 4, 5, 6] , 5, 4)
print(result)

