#same code as question 6 but repeating a name 2 times

n = {}

name = input("Enter the name of the friend:- ")
lang = input("Enter the name of their favourite language:- ")
n.update({name : lang})
name = input("Enter the name of the friend:- ")
lang = input("Enter the name of their favourite language:- ")
n.update({name : lang})
name = input("Enter the name of the friend:- ")
lang = input("Enter the name of their favourite language:- ")
n.update({name : lang})
name = input("Enter the name of the friend:- ")
lang = input("Enter the name of their favourite language:- ")
n.update({name : lang})

print(n)

# the second language written would be replaced and it would be output
# eg:- if for Ayush i type spanish first and then english it would show english at output