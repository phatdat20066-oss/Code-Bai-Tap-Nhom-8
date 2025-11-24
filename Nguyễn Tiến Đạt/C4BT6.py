def computepay(Hours,Rate):
    if Hours > 40:
        Pay = 40*Rate + (Hours-40)*Rate*1.5
    else:
        Pay = Hours * Rate
    return Pay
if __name__=='__main__':
    Hours = float(input("Enter Hours:"))
    Rate  = float(input("Enter Rate:"))
    print("--------------------------")
    print("Enter Hours:",Hours)
    print("Enter Rate:",Rate)
    print("Pay:",computepay(Hours,Rate))
    
