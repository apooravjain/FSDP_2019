names = ['Mary', 'Isla', 'Sam']

#for i in range(len(names)):
#     names[i] = hash(names[i])

#print (names)


def hash_code(n):
    t = hash(n)
    return t

result=map(hash_code,names)
print(list(result))