S, d, k, h = map(int, input().split(' '))
'''
4 2 2 2
'''
DP = [[[[-1 for _ in range(S+1)] for _ in range(S+1)] for _ in range(S+1)] for _ in range(S+1)]

def solution(S, d, k, h):
    if S == 0:
        if d == 0 and k == 0 and h == 0:
            return 1
        else:
            return 0
    if d < 0 or k < 0 or h < 0:
        return 0
    if DP[S][d][k][h] != -1:
        return DP[S][d][k][h]
    DP[S][d][k][h] = 0
    for i in range(2):
        for j in range(2):
            for l in range(2):
                if i == 0 and j == 0 and l == 0:
                    continue
                print(i,j,l)
                DP[S][d][k][h] += solution(S-1, d-i, k-j, h-l)
    DP[S][d][k][h] %= 1000000007
    return DP[S][d][k][h]
print(DP)
print(solution(S,d,k,h))