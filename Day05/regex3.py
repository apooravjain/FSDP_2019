import re
user=[]
while True:
    string=input("enter the number:")
    user.append(string)
    if not string:
        break
user=user[:-1]
print(user)

for item in user:
    if re.findall(r'^[456]?[0-9]+{16}',item):
        print("valid")
    else:
        print("invalid")
        