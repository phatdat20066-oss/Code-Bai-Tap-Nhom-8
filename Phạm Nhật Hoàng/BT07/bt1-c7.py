tentep = input("Enter a file name: ")
try:
    tep = open(tentep)
except:
    print(f"File cannot be opened: {tentep}")
    exit()
for dong in tep:
    dong = dong.rstrip().upper()
    print(dong)
tep.close()
