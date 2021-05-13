from random import random
n=int(random()*1000)
print(int(n))
while n/1000>0 and n/100<=0:
    n=int(random()*1000)
    print(int(n))
a=n//100
b=(n//10)%10
c=n%10
print(int(a+b+c))
        
