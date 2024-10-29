n1= int(input("Enter the first number:- "))
n2= int(input("Enter the second number:- "))
n3= int(input("Enter the third number:- "))
n4= int(input("Enter the fourth number:- "))

if(n1>n2 and n1>n3 and n1>n4):
    print("Greatest number is:- ",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("Greatest number is:- ",n2)
elif(n3>n2 and n3>n1 and n3>n4):
    print("Greatest number is:- ",n3)
elif(n4>n2 and n4>n3 and n4>n1):
    print("Greatest number is:- ",n4)

