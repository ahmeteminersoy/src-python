import random
import math

def getpi(n):
    k = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x ** 2 + y ** 2)
        if distance < 1:
            k += 1
        
    pi = 4 * k / n
    
    return pi
    
pi = getpi(1000)
print(pi)

pi = getpi(10000)
print(pi)

pi = getpi(100000)
print(pi)

pi = getpi(1000000)
print(pi)

pi = getpi(10000000)
print(pi)