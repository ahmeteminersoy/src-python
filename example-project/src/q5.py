import math

def find_angle(num, widths):
    total_width = sum(widths)
    total_height = num 

    x_coordinates = [sum(widths[:i+1]) for i in range(num)]
    
    dist = [(x, total_height) for x in x_coordinates]
    
    angles = [math.atan(distance[1] / distance[0]) for distance in dist]
    
    return sum(angles) * 180 / math.pi

t = int(input())
for _ in range(t):
    n = int(input())
    widths = [int(x) for x in input().split()]
    angle = find_angle(n, widths)
    print(f"{angle:.2f}")
