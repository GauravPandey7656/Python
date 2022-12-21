# Packing Unpacking of Tuple
tuple1=("A","B","C")
(one,two,three)=tuple1
print(one)
print(two)
print(three)

# Extra parameters then Variable
tuple1=("A","B","C","D","E")
(one,two,*three)=tuple1  # Remaining elements has been allocated to three
print(one)               # In similar way two or one can take extra values by putting asterisk(*) before them
print(two)
print(three)


# Question 1
tuple=(10,20,30,40)
(one,two,three,four)=tuple
print(one)
print(two)
print(three)
print(four)


#Question 2
tuple1=(10,20)
tuple2=(30,40)
temp=tuple1
tuple1=tuple2
tuple2=temp
print(tuple1)
print(tuple2)

# Or
tuple1=(10,20)
tuple2=(30,40)
tuple1,tuple2=tuple2,tuple1
print(tuple1)
print(tuple2)