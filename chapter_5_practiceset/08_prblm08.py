#same code but language is repeated 2 times

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

# hence if language is repeated it still shows as different output
# value can be same of 2 keys and it will give 2 different output
# but if key is same it will print output only one key and updates the value

