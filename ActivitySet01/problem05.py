def computepay(h, r):

    if hrs>40:
        reg=rte*hrs
        otp=(hrs-40.0)*(rte*0.5)
        p=reg+otp
    	
    else:

        p=rte*hrs
    return p
 

hrs = float(input("Enter Hours:"))

rte = float(input("Enter rate per hour: "))

p= computepay(hrs,rte)
    
print("Pay", p)