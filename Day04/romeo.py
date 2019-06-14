file=open("romeo.txt","rt")
#display the file in list form
file_content=file.readlines()
print(file_content)
file.close()



file=open("romeo.txt","rt")
fill=file.read().split()
#count the words in the file


count={}
for item in fill:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
print(count)
file.close()