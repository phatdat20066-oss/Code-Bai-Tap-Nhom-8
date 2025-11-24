tentep = input("Enter the file name: ")
dem = 0
tong = 0.0

try:
    tep = open(tentep)
except:
    print(f"File cannot be opened: {tentep}")
    exit()

for dong in tep:
    if dong.startswith("X-DSPAM-Confidence:"):
        dem = dem + 1
        haicham = dong.find(':')
        phanso = dong[haicham + 1 : ]
        chuoi = phanso.strip()
        try:
            sothuc = float(chuoi)
            tong = tong + sothuc
        except:
            print(f"Skipping malformed line: {dong}") 
tep.close()

if dem > 0:
    trungbinh = tong / dem
    print(f"Average spam confidence: {trungbinh}")
else:
    print("No lines with X-DSPAM-Confidence found.")

