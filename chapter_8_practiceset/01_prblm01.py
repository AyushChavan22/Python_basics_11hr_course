def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>a):
        return c
a = 22
b = 67
c = 7
print(greatest(a,b,c))