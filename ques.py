

def ceilingInSortedArray(n, x, arr):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans 
def floorInSortedArray(n, x, arr):
    low = 0
    high = len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high ) // 2
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return -1
def getFloorAndCeil(n, x ,arr):
    f = floorInSortedArray(n, x, arr)
    c = ceilingInSortedArray(n, x, arr)
    return (f,c)
result = getFloorAndCeil(5, 4, [2, 3, 4, 5, 6])
print (result)

