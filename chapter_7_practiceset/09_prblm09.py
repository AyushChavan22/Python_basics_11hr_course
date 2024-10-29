m = int(input("Enter the number:- "))
for i in range(1,m+1):
    if(i==1 or i==m):
        print("*" * m,end="")
    else:
        print("*", end="")
        print(" " * (m-2), end="")
        print("*", end="")
    print("")