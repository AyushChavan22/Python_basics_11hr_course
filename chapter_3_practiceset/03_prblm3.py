name1=("Ayush is a good boy")
print(name1.find("  "))
# this will show -1 as no double space is present hence we know this str
# do not contain double string

name2=("Ayush is  a  very bad boy  ")
print(name2.find("  "))
# this will show some integer as double space is present 
# hence if a string contains double space it will show some integer other than -1