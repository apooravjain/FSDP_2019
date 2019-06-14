list_user=input("enter the list:-").split(" ")
print(list_user)
for i in list_user:
    if i==i[::-1]:
        print("true")
    else:
        print("false")