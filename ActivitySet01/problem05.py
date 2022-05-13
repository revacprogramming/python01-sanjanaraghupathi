# Functions


def computepay(h, r):
    return 'h'

hrs = input("Enter Hours:")
h=float(hrs)
rate = float(input("Enter rate per hour: "))
r2=1.5*rate
p = computepay(10, 20)
if h<=40:
    print(h*rate)
else:
    print(40*rate+(h-40)*r2)
    
print("Pay", p)