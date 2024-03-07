def count_platforms(h):
    count = 0
    for blocks in range(1, len(h) + 1):
        for idx in range(len(h) - blocks + 1):
            if isplatform(h[idx:idx + blocks]):
                count += 1
    return count

def isplatform(h):
    idx = len(h) // 2
    if len(h) % 2 == 1:
        for i in range(1, len(h) // 2 + 1):
            if h[idx - i] <= h[idx] >= h[idx + i]:
                return False
    else:
        for i in range(1, len(h) // 2):
            if h[idx - i] <= h[idx] >= h[idx + i]:
                return False
        if h[0] >= h[idx]:
            return False
    return True

a = int(input())
ehu = [int(x) for x in input().split()]
print(count_platforms(ehu))
