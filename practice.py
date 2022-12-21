p=float(input("Enter first floating point number:"))
q=float(input("Enter second floating point number:"))
r=int(p*q)
s=int(r&int(p))
print(s)
if s==r:
    print("True")
else:
    print("False")