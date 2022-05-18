# Files

fname = "dataset/mbox-short.txt"
fh = open(fname)
n=0
a=[]
result=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x=line.split()
    a.append(float(x[1]))
    result=result+float(x[1])
    n=n+1
average=result/n
print("Average spam confidence:",average)

