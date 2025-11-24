tentep = input("Enter the file name: ")
if tentep == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
soluong = 0

try:
    tep = open(tentep)
except:
    print(f"File cannot be opened: {tentep}")
    exit()

for dong in tep:
    if dong.startswith("Subject:"):
        soluong = soluong + 1
tep.close()
print(f"There were {soluong} subject lines in {tentep}")