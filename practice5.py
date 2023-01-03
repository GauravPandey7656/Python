#Take an integer from the user consider it indicates the corresponding
# month of that number. Your task is to find the number of days
# in the specified month.
# Note: If the number is greater than 12 print invalid.
a=int(input("Enter the number which corresponds to month: "))
if a>12:
    print("Invalid")
else:
    if a in [1,3,5,7,8,10,12]:
        print(31)
    elif a in [4,6,9,11]:
        print(30)
    elif a==2:
        print("28 or 29")