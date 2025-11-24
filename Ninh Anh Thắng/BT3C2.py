hours= float(input("Enter Hours: "))
rate= float(input("Enter Rate: "))
if hours> 40:
    overtime_hours = hours - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)
else:
    pay = hours * rate
print("Pay:", pay)