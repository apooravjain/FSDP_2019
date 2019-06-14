
length=int(input("how many items "))


dict1 = {}
for item in range(length):
    str1 = input(">>").split()
    dict1[" ".join(str1[:-1])]=str1[-1]
print(dict1)
