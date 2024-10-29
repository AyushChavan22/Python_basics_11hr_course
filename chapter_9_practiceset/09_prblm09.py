with open("this.txt","r") as f:
    content1=f.read()
with open("this_2.0.txt","r") as r:
    content2=r.read()
if(content1 == content2):
    print("The two files are identical.")
else:
    print("The two files are not identical.")