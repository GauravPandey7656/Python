num=int(input("Enter a number: "))
count=0
while num>0:
    num=num//10 #Quotient
    count+=1
print("Total number of digits of given number is:",count)