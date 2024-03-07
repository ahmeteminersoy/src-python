def isprime(n):
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5
    if n % 7 == 0:
        return n == 7
    if n % 11 == 0:
        return n == 11
    for i in range(13, int(n** 1/2), 2):
        if n % i == 0:
            return n == i
    return True
if __name__ == "__main__":
    for i in range(int(input("Input a number:"))):
        if isprime(i):
            print(i, end= " ")
