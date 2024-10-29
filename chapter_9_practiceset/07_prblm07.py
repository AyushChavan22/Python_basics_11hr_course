with open("log.txt", "r") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if ("python" in line):
        print(f"The word python is present in file at line {lineno}")
        break
    lineno += 1
else:
    print("No the word python is not present in file.")
