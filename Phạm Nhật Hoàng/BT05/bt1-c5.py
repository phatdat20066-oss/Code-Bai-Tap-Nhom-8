n = 0
tong = 0
while True:
    nhap = input('Enter a number: ')
    if nhap == 'done':    break

    try:
        number = int(nhap)
    except:
         print('Invalid input')

    n = n + 1
    tong = tong + number
    tbc = tong / n
    
print(tong, n, tbc)
