N = 4
M = [3,5,7]
DP = [0] * len(M)
def money_distribute(N, M):
    arr = sorted(M, reverse=True)
    for i in range(len(arr)):
        number = N // arr[i]
        DP[i] = number
        rest = N - (arr[i] * number)
        N = rest
    if N == 0:
        print(sum(DP))
    else:
        print(-1)

money_distribute(N,M)

