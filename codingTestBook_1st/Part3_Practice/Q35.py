'''
10
'''

n = int(input())
cnt = 0
DP = [0] * 1000
DP[1] = 1

i2, i3, i5 = 0, 0, 0

for i in range(2, 1000):
    if i % 2 == 0:
        i2 += 1
        DP[i] = DP[i//2] * 2
    if i % 3 == 0:
        i3 += 1
        DP[i] = DP[i//3] * 3
    if i % 5 == 0:
        i5 += 1
        DP[i] = DP[i//5] * 5

print([_ for _ in DP if not _ == 0])