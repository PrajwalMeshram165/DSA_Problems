list = [1,2,3,4,5,6,7,1,2,3,8,8,9,9]
uniqeList =[]
duplicateist=[]
for i in list:
    if i not in uniqeList:
        uniqeList.append(i)
    elif i not in duplicateist:
        duplicateist.append(i)
print(duplicateist)