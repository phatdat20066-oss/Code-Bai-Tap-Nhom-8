Hours = float(input("Enter Hours:"))
Rate = float(input("Enter Rate:"))
print("--------------------------")
if Hours > 40:
    print("Enter Hours:",Hours)
    print("Enter Rate:",Rate)
    print("Pay:",40*Rate + (Hours-40)*Rate*1.5)
else:
    print("Enter Hours:",Hours)
    print("Enter Rate:",Rate)
    print("Pay:",Hours*Rate)