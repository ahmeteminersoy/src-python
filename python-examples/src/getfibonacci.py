# This function returns the value of the nth Fibonacci number. 
def getFibonacci(n):
    if n < 1:
        return -1
    l = list()
    l.append(1)
    l.append(1)
    for i in range(n - 2):
        l.append(l[i] + l[i + 1])
    return(l[-1])
if __name__ == "__main__":
    print(getFibonacci(int(input("Enter a number: "))))