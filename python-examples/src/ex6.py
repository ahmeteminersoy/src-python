n = int(input())
m = int(input())
plist = [0] * n
for _ in range(m):
    i , k = [int(x) for x in input().split()]
    plist[i - 1] += k
total = sum(plist)
average_price = total/n


def get_dept(p, a):
    if p == a:
        return 0
    if p > a:
        return f"{int(p - a)} payee"
    else:
        return f"{int(a - p)} debtor"
for i in range(n):
    print(i + 1, get_dept(plist[i], average_price))

    

