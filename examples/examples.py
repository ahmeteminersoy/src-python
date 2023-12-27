def add(*args):
    total = 0
    for x in args:
        if isinstance(x, (tuple, list,)):
            for y in x:
                total += y
        else:
            total += x
        
    return total

result = add(1, (2, 3), (4, 5))
print(result)