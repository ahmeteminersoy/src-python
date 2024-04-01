def getfactorial(n):
    a = 1
    for i in range(n):
        a *= i+1
    return a 
if __name__=="__main__":
    n = int(input("Enter a number: "))
    print(getfactorial(n))