#REMOVE i'th Character from string 
str=input("Enter  string: ")
i=int(input("Enter index value from which you want to remove character:"))
new_str=""
for a in range(0,len(str)):
    if a!=i:
        new_str=new_str+str[a]
print("New string After removing",i,"th character is:",new_str)
    
    