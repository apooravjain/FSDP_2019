

user_input = input("Enter comma seperated Numbers: ").split(",")

user_list = []

for i in user_input:
    user_list.append(int(i))

# Sorting the list of integers
user_list.sort()

# leaving out 1 smallest and 1 largest value
final_list = user_list[1:-1]

# Calculating average
average = sum( final_list ) / len( final_list )

print ("Average is :", int( average ))
