Name_File = input("Enter File: ")
try:
    file = open(Name_File)
except:
    print("File cannot be opened")
    quit()
cnt = 0
for line in file:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    char = line.split()
    print(char[1])
    cnt += 1
print(f"There were {cnt} lines in the file with From as the first word")
