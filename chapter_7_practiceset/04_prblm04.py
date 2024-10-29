q = int(input("Enter a number to check if it is prime or not:- "))
if q==1:
    print("1 is neither a prime or a composite number.")
else:
    for i in range(2,q):
        if(q%i)== 0:
            print("The number is not prime.")
            break        
    else:
         print("The number is prime.")         
# if run from the print statement it will check each divisor and print that
# "The number is not prime." eg:- if 6 is entered it will show 2 times cuzz
# it will check for 2 and 3 as they completely divide 6. This happens due to looping
# in for.
# Hence a 'break' statement is required






