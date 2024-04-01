class myenumerate:
    def __init__(self, iterable, start=0):
        self.iterator = iterable.__iter__()
        self.i = start

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        return self.i - 1, self.iterator.__next__()


a = ['ali', 'veli', 'selami', 'ayşe', 'fatma']

me = myenumerate(a, 10)

for index, name in me:
    print(index, name)

for index, name in me:
    print(index, name)    