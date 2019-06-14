import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
    
#for i in range(len(names)):
 #   names[i] = random.choice(code_names)
#print(names)
 
       
ran= map(lambda x: random.choice(code_names),names)
print(list(ran))