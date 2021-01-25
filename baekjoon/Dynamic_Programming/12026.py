N = int(input())
block = list(input())

def solution(N, block):
    DP = [2000000 for _ in range(N)]
    DP[0] = 0
    for i in range(len(block)):
        start = block[i]
        for j in range(i+1, len(block)):
            end = block[j]
            if (start == 'B' and end == 'O') or (start == 'O' and end == 'J') or (start == 'J' and end == 'B'):
                DP[j] = min(DP[i]+(j-i)*(j-i), DP[j])
    print(DP)
    if DP[-1] == 2000000:
        return -1
    else:
        return DP[-1]

print(solution(N, block))