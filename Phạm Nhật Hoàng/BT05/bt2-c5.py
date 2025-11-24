lon = None
nho = None
while True:
    nhap = input('Enter a number: ')
    if nhap == 'done':    break

    try:
        number = float(nhap)
    except:
        print('Invalid input')
        continue

    nhap = float(nhap)
    
    if nho is None or number < nho:
        nho = nhap
    if lon is None or number > lon:
        lon = nhap

print('largest: ', lon)
print('smallest: ', nho)