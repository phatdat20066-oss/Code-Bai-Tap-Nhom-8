File_Name = input("Enter a file name:")
try:
    file = open(File_Name)
    for line in file:
        print(line.rstrip().upper())
except FileNotFoundError:
    print("File cannot be opened")
    quit()