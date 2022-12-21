def is_leap(year):
    y=(1900,1999,2001,2002,2003,2005,2100)
    if year%4==0:
        if year in y:
            leap = False
        else:
            leap= True
        
        
    # Write your logic here
    
        
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))