from functools import reduce
l = [90,34,357,9687,954,75,60,48,239,64,3423285,2312420]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))
