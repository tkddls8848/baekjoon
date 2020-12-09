'''
7
15 11 4 8 5 2 4
'''
n = int(input())
army = list(map(int, input().split()))
DP = [1] * n

for i in range(n):
    for j in range(0,i):
        if not army[j] < army[i]:
            DP[i] = max(DP[i],DP[j]+1)

print(DP)
print(n - max(DP))