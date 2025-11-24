tentep = input("Enter file name: ")
tep = open(tentep,'r')
lst = []
for line in tep:
    text1 = line.split()
    for word in text1:
        if word in lst: continue
        else:
            lst.append(word.strip())
lst.sort()
print(lst)