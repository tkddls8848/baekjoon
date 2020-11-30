'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''
n = int(input())
DP = []
for i in range(n):
    DP.append(list(map(int, input().split())))


for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            from_left = 0
        else:
            from_left = DP[i-1][j-1]
        if j == i:
            from_right = 0
        else:
            from_right = DP[i-1][j]
        DP[i][j] = DP[i][j]+max(from_left,from_right)


