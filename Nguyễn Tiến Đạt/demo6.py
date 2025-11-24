Name_File = input("Enter File: ")
try:
    file = open(Name_File)
except:
    print("File cannot be opened",Name_File)
    quit()
res = []
for line in file:
    char = line.split()
    for val in char:
        if val not in res:
            res.append(val)
res.sort()
print(res)
