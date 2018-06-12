un = set()
h = open("sub-guid.log")
for line in h:
    un.add(line)
print(len(un))