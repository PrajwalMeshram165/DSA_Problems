def searchRSA(arr, target):
    low=0
    high=len(arr)-1
    middle=0

    while low <= high:
        middle = (low + high)//2
        if target >= arr[0]>arr[middle]:
            arr[middle]=float('inf')
        elif target < arr[0] <= arr[middle]:
            arr[middle] = -1*float('inf')


        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            low = middle + 1
        else:
            high = middle -1
    return -1


arr = [4,5,6,7,1,2,3]
target = 2

print(f"the index of {target} in the {arr} array is :",searchRSA(arr,target))
