#1:100  : odd , even


#-1

numbers= list(range(1,100))
odd= [x for x in numbers if x%2!=0]
even =[x for x in numbers if x%2==0]
print(odd)
print (even)
print('--------------------------------')




numbers_odd= list(range(1,100,2))
numbers_even= list(range(0,100,2))
odd= [x for x in numbers_odd  ]
even =[x for x in numbers_even]
print(odd)
print (even)

print('--------------------------------')

numbers= list(range(1,100))
odd=[]

even=[]
for x in numbers:
    if x % 2==0:
        even.append(x)
    
    else:
        odd.append(x)
    
print(odd)
print(even)
