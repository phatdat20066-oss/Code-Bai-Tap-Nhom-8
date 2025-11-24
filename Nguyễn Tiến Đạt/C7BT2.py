Name_file = input("Enter the file name: ")
try:
    file = open(Name_file)
    cnt = 0
    sum_len = 0
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            number_pos = float(line[line.find(":") + 1:].strip())
            cnt += 1
            sum_len += number_pos
    if cnt > 1:
        print("Average spam confidence:", sum_len/cnt)
    else:
        print("No Average")
except:
    print("File cannot be opened:", Name_file)
    quit()
