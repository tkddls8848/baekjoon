n = input()
li = list(map(int, input().split()))
tmp = 0
cnt = 0

li.sort(reverse=True)
while len(li)!=1:
    tmp += li.pop()
    tmp += li.pop()
    li.append(tmp)
    cnt += tmp
    tmp = 0
    print(li,cnt)


