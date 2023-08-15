def maxinposition(A,n):
    minposition = A.index(min(A))
    maxposition = A.index(max(A))
    print("the maximum is at position::", maxposition+1)
    print("the minimum is at position::", minposition+1)
A=list()
n=int(input("enter the size of array::"))
print("enter the elemet::")
for i in range(int(n)):
        k=int(input(""))
        A.append(k)
maxinposition(A,n)



    
