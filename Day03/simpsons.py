
with open('simpsons_phone_book.txt', mode='rt')as file:
        file_content=file.readlines()
        print(file_content)
        
str1=[]
str2=list(file_content)
print(str2)
import re
for item in str2:
    if re.findall('r^J[a-z]*\sNeu\s\d*',item):
        str1.append(item)
print(str1)