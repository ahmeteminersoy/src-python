_ = input()
p = [int(x) for x in input().split()]


operations = 0

while p[0] >= min(p[1:]):
    min_index = p[1:].index(min(p[1:])) + 1 
    p[min_index] += 1
    p[0] -= 1
    operations += 1

print(operations)