def count_platforms(h):
    count = 0
    for blocks in range(1, len(h) + 1):
        for idx in range(len(h) - blocks + 1):
            if isplatform(h[idx:idx + blocks]):
                count += 1
    return count
def isplatform(h):
    def issorted(lst):
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    
    _l = list()
    idx = len(h) // 2
    _l.append(h[idx])
    if len(h) % 2 == 1:
        for i in range(1, len(h) // 2 + 1):
            _l.append(h[idx - i]) 
            _l.append(h[idx + i])
    else:
        for i in range(1, len(h) // 2):
            _l.append(h[idx - i]) 
            _l.append(h[idx + i])
        _l.append(h[0])
    return issorted(_l)

a = int(input())
ehu = [int(x) for x in input().split()]
print(count_platforms(ehu))
