with open("log.txt", "r") as f:
    content= f.read()
if ("python" in content):
    print("The word python is present.")
else:
    print("The word python is not present.")
