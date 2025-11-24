#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
Hours = float(input('Enter Hours: '))
Rate = float(input('Enter Rate: '))
if (Hours > 40):
    Pay = (Hours-40)*1.5*Rate+40*Rate
else:
    Pay = Hours*Rate
print('Pay: ', Pay)