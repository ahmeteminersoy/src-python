import math
def getroots():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    delta = (b ** 2) - 4 * a * c
    if delta > 0:
        return (-b + math.sqrt(delta)) / 2 * a, (-b - math.sqrt(delta)) / 2 * a
    if delta == 0:
        return (-b + math.sqrt(delta)) / 2 * a, ""
result = getroots()
if result:
    x1, x2 = result
    print(x1, x2)
else:
    print("There are no roots!..")


