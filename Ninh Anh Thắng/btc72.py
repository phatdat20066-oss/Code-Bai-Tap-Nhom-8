text = "Mã OTP của bạn là: 1357"
OTP = ""
for char in text:
    if char.isdigit():
        OTP += char
print(OTP)