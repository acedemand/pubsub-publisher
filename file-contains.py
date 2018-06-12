import uuid
import time
h = open("pub-guid.log")
for line in h:
    if line in open('sub-guid.log').read() == False:
        print("olmayan kayıt")
