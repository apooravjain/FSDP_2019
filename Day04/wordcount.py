#Number of line in file
with open("romeo.txt","rt") as file:
    fill=file.readlines()
    print("Number of lines:-"+str(len(fill)))

#number of characters in file
with open("romeo.txt","rt") as file:
    fill=file.read()
    count={}
    for item in fill:
        if item in count:
            count[item]+=1
        else:
            count[item]=1
print("Number of characters:-")
print(count)

#number of words in lines
with open("romeo.txt","rt") as file:
      fill=file.read().split()
      c={}
      for item in fill:
          if item in c:
              c[item]+=1
          else:
              c[item]=1
print("Number of words:-")
print(c)

#number of unique words in file
print("Number of unique words:-"+str(len(c)))   