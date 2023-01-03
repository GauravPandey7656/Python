# Program to Format the string 
a=10
b=5
c=15
d=20
str="a={2},b={3},c={1},d={0}"
print(str.format(a,b,c,d))
print(str.format(c,d,a,b))
# str me se dekhenge or dekhnege format me like a={2}iska mtlb h 2 index ko format me dekhenge jo ki "a" h to fir usko "a" ki value de denge.
