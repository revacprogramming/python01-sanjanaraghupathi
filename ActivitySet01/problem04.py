# conditional execution

hrs=input("enter hours")
h=float(hrs)
rate=float(input("enter rate per hour:"))
r2=1.5*rate
if h<=40:
    print(h*rate)
else:
    print(40*rate+(h-40)*r2)