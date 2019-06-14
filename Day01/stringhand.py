name=input("enter the name :-")
find_position=int(name.find(" "))
print(name[find_position:]+" "+name[0:find_position])