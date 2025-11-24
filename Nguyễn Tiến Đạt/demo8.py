res = []
while True:
    Number = input("Enter a number: ")
    if Number == "done":
        break
    val = float(Number)
    res.append(val)
print("Maximum:",max(res))
print("Minimum:",min(res))