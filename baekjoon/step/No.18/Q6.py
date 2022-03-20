'''
4
3 5 2 7
'''

n = int(input())
list = list(map(int, input().split()))
answer = []
for i in range(n-1):
    tmp = list[i]
    j = i
    while True:
        if j == n:
            ##print("j == n", -1)
            answer.append(-1)
            break
        tmp1 = list[j]
        if tmp1 > tmp:
            ##print("FINAL", tmp1)
            answer.append(tmp1)
            break
        j += 1
answer.append(-1)
##print(-1)

for i in answer:
    print(i, end=' ')

