def rvrList(A,start,end):
    while start < end:
        A[start],A[end] = A[end],A[start]
        start += 1
        end -= 1

A = [1,2,3,4,5,6,7,8,9]
print(A)
rvrList(A,0,8 )
print("reverse list is : ")
print(A)