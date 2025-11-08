def binarySearch(arr:list,l:int, r:int, target:int):
    while(l<=r):
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return binarySearch(arr,l,mid-1,target)
        else: 
            return binarySearch(arr,mid+1,r,target)
    
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    target = 90
    result = binarySearch(arr,0,len(arr)-1,target)
    if result != -1 : print(f"Element found at index: {result}")
    else: print("Element not found in the array")