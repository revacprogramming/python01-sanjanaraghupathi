# Dictionaries

filename = "dataset/mbox-short.txt"
f = "dataset/mbox-short.txt"
c = open(f,"r")
n = 0
h = c.readlines()
for i in h:
    k = i.split()
    if i.startswith("From:"):
        print(k[1])
        n+=1
print(f"There were{n}lines in the file with From as the first word")