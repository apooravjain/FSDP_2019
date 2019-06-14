

# To check if a string is pangram or not
input_string = input("Enter the string :")
count = 0
_list = []
_lower = input_string.lower()
for alpha in _lower:
    _list.append(alpha)

# remove duplicates
final_list = []    

for num in _list: 
 if num not in final_list: 
  final_list.append(num) 
    
for elements in final_list:
    if elements in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
if count == 26:
    print ("Pangram")
else:
    print ("Not Pangram")
    