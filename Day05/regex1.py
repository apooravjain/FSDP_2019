import re
user_1=[]
while True:
    user=input("enter the number :")
    user_1.append(user)
    if not user :
        break
user_1=user_1[:-1]
print(user_1)
for item in user_1:
    if re.findall(r'^[.+-]?[0-9]*\.[0-9]+$',item):
        print("True")
    else:
        print("false")