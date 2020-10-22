n = 10
DP = [0] * n

def tile(n):
    DP[0] = 1
    DP[1] = 3
    for i in range(2, n):
        DP[i] = DP[i-1] + 2 * DP[i-2]
    return DP

print(tile(10))