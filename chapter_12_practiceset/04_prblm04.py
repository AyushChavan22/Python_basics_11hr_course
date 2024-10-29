try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError as e:
    print("Infinite")
    