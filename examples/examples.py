import time

start = time.time()

a = []

for i in range(10000000):
    a.append(str(i))
    
stop = time.time()

print(stop - start)             
    
start = time.time()

a = [str(i) for i in range(10000000)]
stop = time.time()

print(stop - start)            
