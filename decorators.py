def div(a,b):    # we can not change this function
    print(a/b)
    
def good_div(func):
    def inner_div(a,b):  # Number of parameters will be same as that of parent function and responsible for logic
        if a<b:          # this function is used to manipulate the above function which we can't change 
            a,b=b,a      # we do it by the use of decorators
        return func(a,b)
    return inner_div
a=int(input())
b=int(input())
div=good_div(div)
div(a,b)