# Python Program to print Even Indexed words in string and aslo print total length of even words 
str=input("Enter String:")
l=len(str)
count=0
for a in range(0,l):
    if a%2==0:
        print(str[a],end=",")
        count+=1
print("/n")
print("Total length of even words is:",count)
    
                