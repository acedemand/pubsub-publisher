import re
h = open("sub.log")
c = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
for line in h:
    result = c.findall(line)
    if  len(result) > 0 :
        for r in result:
            print(r)