def pattern(number):
    for i in range(0,number):
        for j in range(1,i+1):
            print("* ",end=" ")
        print("\r")
    for i in range(number,0,-1):
        for j in range(0,i-1):
            print("* ",end=" ")
        print("\r")
        

number=int(input("enter the number :-"))
pattern(number)
    