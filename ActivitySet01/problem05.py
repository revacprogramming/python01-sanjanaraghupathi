# Functions


def computepay(h, r):
    return

hours = float(input("Enter hours:"))

rate = float(input("Enter rate per hour: "))

p = computepay(hours, rate)
if hours>40:
    reg=rate*hours
    otp=(hours-40.0)*(rate*0.5)
    p=reg+otp
    
else:
    p=rate*hours
    
print("Pay", p)