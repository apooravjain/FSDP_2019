digit_letter={'letter':0,'digit':0}
user=input("enter the string:-")
for item in user:
    if item in "qwretyuioplkjhgfdsazxcvbnm ":
        digit_letter['letter']+=1
    else:
        digit_letter['digit']+=1
print(digit_letter)

    