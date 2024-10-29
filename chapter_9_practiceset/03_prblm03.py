def generatetable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}.doc", "w") as f:
        f.write(table)
for m in range(2,21):
    generatetable(m)