from functools import reduce
def s(x,y):
    return x+y
l=[3,4,5,6]
newl=reduce(s,l)    
print(newl)