
def translate(string):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    final_list = []

    for element in string:
        if element in consonants: 
            final_list.append(element+"o"+element)
        else:
            final_list.append(element)

    return "".join(final_list)

user_input = input("Enter string to Translate: ")

print (translate(user_input))

