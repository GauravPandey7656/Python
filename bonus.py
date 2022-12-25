year=int(input("Enter number of years spend in company:"))
salary=float(input("Enter curent salary:"))
if year>=10:
    bonus=(salary*10)/100
    salary=salary+bonus
    print("Net Bonus Amount is:",salary)
elif (year>=6 and year<10):
    bonus=(salary*8)/100
    salary=salary+bonus
    print("Net Bonus Amount is:",salary)
elif (year<6):
    bonus=(salary*5)/100
    salary=salary+bonus
    print("Net Bonus Amount is:",salary)
else:
    print("Invalid input")