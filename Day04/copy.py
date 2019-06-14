file=open("romeo.txt","rt")
print(file.name)

#create the file and copy the content in the file
file_copy = open("new.txt",mode="wt")
print(file_copy.name)
file_copy=file

#read the copy file
file_content=file_copy.read()
print(file_content)

#close the both files
file.close()
file_copy.close()