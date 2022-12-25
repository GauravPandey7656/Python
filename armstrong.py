n=int(input("Enter a number which you want to check for armstrong: "))
temp=n
s=len(str(n))
r=0
while n>0:
    b=n%10
    r+=(b**s)
    n=n//10
if temp==r:
    print("Yes",temp,"is an armstrong number.")
else:
    print("No",temp,"is not an armstrong number.")