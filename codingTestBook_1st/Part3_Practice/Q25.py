'''
5
2 1 2 6 2 4 3 3
'''

n = int(input())
stages = sorted(list(map(int, input().split())))
fail = []

for i in range(1, n+1):
    cnt = stages.count(i)
    length = len(stages)
    stages = stages[cnt:]

    if cnt == 0:
        fail.append([i, 0])
    else:
        fail.append([i, cnt / length])

fail = sorted(fail, key=lambda x:x[1], reverse=True)
print(fail)
