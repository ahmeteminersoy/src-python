a = [1, 2, 3, 4, 5]
s = ['ali', 'veli', 'selami', 'ayşe', 'fatma', 'cumhur']
w = [72.4, 69.5, 84.2, 51.6, 56.2]

def foo(*x):
    return x

for x in map(foo, a, s, w):
    print(x)