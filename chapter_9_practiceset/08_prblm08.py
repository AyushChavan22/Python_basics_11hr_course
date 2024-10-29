with open ("this.txt", "r") as f:
    content= f.read()
with open("this_2.0.txt","w") as r:
    r.write(content)