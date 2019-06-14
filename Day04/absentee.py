file=open("absentee.txt",mode="at")
#enter the name and close to save the file
while True:
    fill=input("enter the name:-\n")
    file.write(fill+'\n')
    if not fill:
        break
file.close()
#read the file and display the all name
file=open("absentee.txt","rt")
file_content=file.read()
print(file_content)

file.close()    