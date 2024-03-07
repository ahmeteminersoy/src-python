import sys

def findConsecutive(N):
    start = 1
    end = 1
    total_sum = 1
    count = 1
    
    while start <= N // 2:
        if total_sum < N:
            end += 1
            total_sum += end
        
        if total_sum > N:
            total_sum -= start
            start += 1
            
        if total_sum == N:
            count = end + 1 - start
            total_sum -= start 
            start += 1
    
    return count


lst1 = list(map(int, sys.stdin.readline().split()))
N = lst1[0]

sys.stdout.write("No one but Tadano\n" if findConsecutive(N) == 1 else str(findConsecutive(N)) + "\n")

for _ in range(lst1[1]):
    m = int(sys.stdin.readline())
    N *= m

    sys.stdout.write("No one but Tadano\n" if findConsecutive(N) == 1 else str(findConsecutive(N)) + "\n")


sys.stdout.flush()
