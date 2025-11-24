import re
while True:
    pass_code = input("Enter Pass Code:")
    if len(pass_code) < 8:
        print("===Mật Khẩu Không Hợp Lệ. Vui Lòng Nhập Lại===")
        continue
    else:
        break
if re.search(r"[a-zA-Z]",pass_code) and re.search(r"\d",pass_code) and re.search(r"[^a-zA-Z0-9\s]",pass_code):
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")