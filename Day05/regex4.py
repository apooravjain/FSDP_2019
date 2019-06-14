import re
user=[]
while True:
    string=input("enter the email address:")
    user.append(string)
    if not string:
        break
user=user[:-1]
print(user)

add=[]
for item in user:
    if re.findall(r'^[a-z]*\@[a-z]+\.[a-z]+',item):
        print("true")
        add.append(item)
    else:
        print("false , please enter the correct email address")
print(add)