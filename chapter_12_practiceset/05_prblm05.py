n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]
with open ("tables.txt","a") as t:
    t.write(f"The table of {n} is: {table}\n")
