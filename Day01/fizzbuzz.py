n=1
while(n<100):
    if n%3==0 and n%5==0:
        print("FizzBizz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Bizz")
    else:
        print(n)
    n=n+1