# Tuples

filename = "dataset/mbox-short.txt"
f=open(filename,"r")
h=f.readlines()
for i in h:
    k=i.split()
    if i.startswith("From: "):
        print(k[1])
counts=dict()




