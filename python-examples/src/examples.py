def isprime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    if num % 3 == 0:
        return num == 3
    if num % 5 == 0:
        return num == 5
    if num % 7 == 0:
        return num == 7
    if num % 11 == 0:
        return num == 11
    for i in range(13, int(num ** 1/2), 2):
        if num % i == 0:
            return num == i
    return True
count = 0
n = int(input())
l = [i for i in range(1 ,int(n ** 1/5)) if isprime(i)]
for i in l:
    for k in range(1, i + 1):
        if  k * i ** 5 <= n:
            count+=1
print(count)
    