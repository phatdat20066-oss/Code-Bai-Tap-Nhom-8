str = 'X-DSPAM-Confidence:0.8475'
find = str.find(':')
ketqua = str[find+1:]
print(float(ketqua))