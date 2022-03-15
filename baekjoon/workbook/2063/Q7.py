N = int(input())
time = []
money = []
dp = []
answer = 0

for i in range(N):
    t, m = map(int, input().split())
    time.append(t)
    if i + t-1 < N:
        money.append(m)
        dp.append(m)
    else:
        money.append(0)
        dp.append(0)

for i in range(1, N):
    for j in range(0, i):
        if i-j >= time[j]:
             dp[i] = max(money[i] + dp[j], dp[i])
