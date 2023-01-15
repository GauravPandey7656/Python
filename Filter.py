#filter filter's out something from given collections

def is_even(i):
    return i%2==0
list1=[2,4,3,21,43,5,54,334,4545,65]
evenNum=list(filter(is_even,list1))
print(evenNum)

#0r
list1=[2,4,3,21,43,5,54,334,4545,65]
evenNum=list(filter(lambda i : i%2==0,list1))
print(evenNum)

# list of numbers greater than 5
list1=[2,4,3,21,43,5,54,334,4545,65]
num=list(filter(lambda i : i>5 , list1))
print(num)


# Triple the values of list
list1=[10,20,30,40,50]
num=list(map(lambda i:3*i,list1))
print(num)

# Convert uppercase into lowercase and lowercase into uppercase
list2=["a","B","c","D","e","f"]
def lower_Upper(list):
    for a in list:
        if a.islower():
            a=a.upper()
        else:
            a=a.lower()
    return a
str=list(map(lower_Upper,list2))
print(str)