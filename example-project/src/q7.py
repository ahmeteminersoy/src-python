import itertools

def get_multipy(l):
    lst = list(l)
    for i in range(len(lst)):
        if i >= len(lst) - 1:
            break
        if lst[i][1] == lst[1 + i][0]:
            lst[1 + i] = lst[i][0], lst[i + 1][1]
        else: # burası
            return
    return lst[-1]

result = list()
for _ in range(int(input())):
    found_invalid = False
    idx = 0
    n = int(input())
    l = [(int(x), int(y)) for _ in range(n) for x, y in [input().split()]]
    perms = list(itertools.permutations(l))
    for ky in range(len(perms)):
        if get_multipy(perms[ky]) == (1, 1):

            result.append(1)
            break
        if ky == len(perms) - 1:
            result.append(-1)
print(*result, end='\n')