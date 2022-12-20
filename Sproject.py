# cake is of circular shape so angle is 360
# for N equal pieces
def check1(N):
	if 360 % N ==0:
		Case1 = True
	else:
		Case1 = False

	return Case1

# for N pieces of any size
def check2(N):
	if N < 360:
		Case2 = True
	else:
		Case2 = False

	return Case2

# for N pieces such that no two of them are equal
# In this we will use the concept of AP i.e.,1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26=351
def check3(N):
	if N <= 26:
		Case3 = True
	else:
		Case3 = False

	return Case3

        
N=int(input("Enter the number of ways how you want to cut the cake: "))

print("Case 1 (N number of equal pieces):", check1(N))
print("Case 2 (N pieces of any size):", check2(N))
print("Case 3 (N pieces such that no two of them are equal):", check3(N))
