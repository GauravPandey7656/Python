# Program to check whether square root of a number is prime or not.
import math
num=int(input("Enter a number: "))
square_root=math.sqrt(num)
y=0
b=square_root-1
while b>1:
    c=square_root%b
    if c==0:
        y=1
        break
    else:
        y=0
    b=b-1
if y==1:
    print("Number is not a Prime Number")
else:
    print("Number is a Prime Number")