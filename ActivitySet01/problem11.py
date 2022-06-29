# Tuples

filename = "dataset/mbox-short.txt"
f=open(filename,"r")
count=0

h=f.readlines()

counts=dict()
emails=[]
for i in h:
    if i.startswith("From: "):
        emails.append(i.split()[1])
for email in emails:
    if email not in counts:
            counts[email]=1
    else:
            counts[email]+=1
            
print(email,counts[email])   
      






