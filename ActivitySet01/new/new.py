file="dataset/mbox-short.txt"
f=open(file,"r")
z=f.readlines()
count=0
#print(z)
for i in z:
   
    if i.startswith("X-Content"):
         print(i)
         count=count+1
print(count)

    
    
