text = 'X-DSPAM-Confidence:0.8475'
index = text.find(":")
char = text[index + 1 : ]
val = float(char)
print(val)