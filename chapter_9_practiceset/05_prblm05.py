words = ["crap","dumbass","asses","fucking","bullshit","hell","fucked up","morons","shit","damn"]
with open("censored.txt" , "r") as a:
    content = a.read()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("censored.txt", "w") as f:
    content = f.write(content)