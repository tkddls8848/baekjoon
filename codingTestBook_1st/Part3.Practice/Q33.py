'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

'''
n = int(input())
time = []
price = []
DP = [0]*n
for i in range(n):
    li = list(map(int, input().split()))
    time.append(li[0])
    price.append(li[1])

for i in range(n-1,-1,-1):
    duration = i + time[i]

    if duration <= n:
        print(DP[duration], price[i],i)
        DP[i] = max(DP[i], DP[duration]+price[i])

for _ in DP:
    print(_)