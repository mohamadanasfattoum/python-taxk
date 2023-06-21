# Functions Tasks
# -1
'''
def mysum():
    x = 5
    y = 10
    print(x,y)

mysum()
print('----------')
'''
# -2
'''
def mysum(x,y):
    print(x+y)

mysum(5,10)
mysum(5,50)
print('----------')
'''
# -2 ,
'''
def mysum1(x,y):
    return x+y
    
b = mysum1(5,10)
print(b)
'''
# -3 ,-keyword
'''
def mysum1(x,y):
    return x+y
    
b = mysum1(y=4,x=6)
print(b)
'''
# -4 ,-give x and y default values of 0.
'''
def mysum1(x=0,y=0):
    return x+y
    
b = mysum1()
print(b)
'''
# -5
'''
def mysum1(x=0,y=0):
    return x+y
    
b = mysum1(7,8)
print(b)
'''
# -6 ,-7 ,-lambda
'''
mysum = lambda x,y : x+y
print(mysum(2,9))
'''
# -8
'''
Local variables are created when the function starts its execution and are lost when the function ends. Global variables, on the other hand, are created as execution of the program begins and are lost when the program is ended
'''
