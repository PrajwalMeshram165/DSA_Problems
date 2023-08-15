def MaxArr(arr,l):
    maxsum = -1
    ans = []
    for i in range(l):
        for j in range(i,l):
            a = sum(arr[i:j+1])
            if a > maxsum:
                maxsum = a
                ans = arr[i:j+1]
    print("maximum subarray = ",ans)
    print("maximum sum = ", maxsum)

array = [-1,8,1,-7,-1,5,1,-3]
print("array =",array)
MaxArr(array,len(array))