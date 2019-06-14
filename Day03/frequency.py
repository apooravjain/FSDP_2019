count={}
user=input("enter the string")
for item in user:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
print(count)
