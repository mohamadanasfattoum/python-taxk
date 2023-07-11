'''
names = ['anas','ali','ahmad','omar']

length = []
for x in names:
    length.append(len(x))

print(length)


result = [len(x) for x in names]
print (result)
'''


# Game input names and length with list comprehensions
 #my game
'''
names = input('Enter names : ')
names_list = names.split(',')
length = int(input('Enter Length : '))
result2 = [x for x in names_list if len(x) >= length]
print (result2)
'''
            
