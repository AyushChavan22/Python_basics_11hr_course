word = "Donkey"
with open("file.txt" , "r") as a:
    content = a.read()

contentNew=content.replace(word,"######")

with open("file.txt", "w") as f:
    content = f.write(contentNew)

