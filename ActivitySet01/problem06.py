# Loops & Iterators

a=[]
largest= None
smallest = None
while True:
    num = input("enter a number")
    if num == "done":
        break
    try:
        num=int(num)
        a.append(num)
    except:
        print("Invalid input")
    else:
        largest = max(a)
        smallest = min(a)
print("Maximum is",largest)
print("Minimum is",smallest)
