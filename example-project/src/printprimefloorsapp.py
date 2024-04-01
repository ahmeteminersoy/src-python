from isprime import isprime

if __name__ == ("__main__"):
    n = int(input("Input a number"))
    divider = 2
    while n != 1:       
        if n % divider == 0:
            print(divider, end=" ")
            n /= divider
        else:
            divider += 1