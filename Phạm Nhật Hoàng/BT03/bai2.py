try:
    Hours = float(input('Enter Hours: '))
    Rate = float(input('Enter Rate: '))
    if (Hours > 40):
        Pay = (Hours-40)*1.5*Rate+40*Rate
    else:
        Pay = Hours*Rate
    print('Pay:', Pay)
except:
    print('Error, please enter numeric input')
    quit()