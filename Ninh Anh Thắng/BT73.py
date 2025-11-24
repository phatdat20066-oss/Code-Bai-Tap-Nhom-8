file_name = input("Enter file name:")
if file_name.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
try:
    file = open(file_name)
    cnt = 0
    for char in file:
        if char.startswith("Subject"):
            cnt += 1
    print(f"There were {cnt} subject lines in {file_name}")
except:
    print("File cannot be opened:",file_name)