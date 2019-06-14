str1=input("enter the number:").split()
print(str1)

pallindromic=[True if x==x[::-1] else False for x in str1]
print(any(pallindromic))