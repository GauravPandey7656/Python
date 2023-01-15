def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: " ))
while(True):
    ch=input("enter choice (n or y) to break or continue the code: ")
    if ch in "yY":
        choice=int(input("Enter your choice: "))
        if choice==1:
            print(add(num1,num2))
        elif choice==2:
            print(sub(num1,num2))
        elif choice==3:
            print(multiply(num1,num2))
        elif choice==4:
            print(divide(num1,num2))
        else:
            print("Invalid Input ")
    else:
        break

    