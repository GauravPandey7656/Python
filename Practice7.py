#Program to Take a number as input from the user and your task is to print the sum of all factor's of a given number.
n=int(input("Enter a number:"))
sum=0
for a in range(1,n+1):
    if n%a==0:
        sum+=a
print("Sum of all Factor's of a given number:",sum)