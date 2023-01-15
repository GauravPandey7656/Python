def add(num1,num2):
    print(num1+num2)
x=int(input("Enter a number:"))
y=int(input("Enter second number:"))
add(x,y)


#  or
#lambda function
x=lambda num1,num2 : num1+num2
print(x(3,4))


# Short Function

cars=["bmw","tesla","nano","swift desire"]
[print(x) for x in cars]


newlist=[x for x in cars if x!="Tata"]
#output You want then loop then condition
print(newlist) #print in form of list



l=[1,2,3]
if len(l)>0:
    print("Not Empty")
else:
    print("Empty")
    
    # OR
l1=[1,2,3]
if l1:
    print("Not Empty")
else:
    print("Empty")