def printprimefloors(n):
    n 
    divider = 2
    while n != 1:
        if n % divider == 0:
            print(divider, end=' ')
            n //= divider
        else:
            divider += 1
    print()