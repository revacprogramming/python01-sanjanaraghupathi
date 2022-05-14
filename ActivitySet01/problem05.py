# Functions


def computepay(h, r):
    return

hrs = float(input("Enter Hours:"))

rate = float(input("Enter rate per hour: "))

p = computepay(hrs, rate)
if hrs>40:
    reg=rate*hrs
    otp=(hrs-40.0)*(rate*0.5)
    p=reg+otp
    
else:
    p=rate*hrs
    
print("Pay", p)