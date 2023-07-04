

class Task:

    def with_f(self):
        even = []
        odd = []
        for x in range(1,101):
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)

        print(even)
        print(odd)





'''
    def with_w(self):
        i = 0
        while i <= 100:
            if i % 2 == 0:
                print(i, end=101)
                i+=1

           else: i % 2 /== 0:
                 print(i, end=101)
                 i+=1
                  
'''




t1=Task()
t1.with_f()
#t1.with_w()





'''
n=1
        while (n<=100):
            if (n % 2 ==0):
                print (n, 'is even.')

            else:
                print (n, 'is odd.')

        n += 1
'''
