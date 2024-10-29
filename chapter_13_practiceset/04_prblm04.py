def divisible5(n):
    if (n%5==0):
        return True
    else:
        return False

s=[90,34,357,9687,954,75,60,48,239,64,3423285,2312420]
f = list(filter(divisible5,s))
print(f)