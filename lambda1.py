def isEven(i):
    return i%2==0
list1=[3,4,10,9,18,66,13,15]

evenNum=list(filter(isEven,list1))

print(evenNum)

