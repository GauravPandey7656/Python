# Avoid Spaces in String Length
str=input("Enter String:")
l=len(str)
space=" "
count=0
s=0
for a in range(0,l):
    if str[a]==space:
        s+=1
    else:
        count+=1
print("Length of string without spaces is:",count)
print("Total spaces present in String is:",s)
        