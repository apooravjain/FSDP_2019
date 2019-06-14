with open("romeo.txt","rt") as file:
    fill=file.readlines()
    last_line=int(len(fill))
    print(fill[last_line-1])