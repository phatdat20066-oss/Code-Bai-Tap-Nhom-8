count = 0
res = []
while True:
    number = input("Enter a numer:")
    if number == "done":
        break
    try:
        val = float(number)
        res.append(val)
    except:
        print("Invalid Input")
        continue
    count += 1
print(sum(res),count,(sum(res)/count))