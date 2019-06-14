import re
user=[]
while True:
    string=input("enter the email address")
    user.append(string)
    if not string:
        break
user=user[:-1]
print(user)
add=[]
for item in user:
    if re.findall(r'^[a-z0-9_-]+\@[a-z0-9]+\.[a-z]{2,4}$',item):
        add.append(item)
        
print("correct email address:")
print(sorted(add))