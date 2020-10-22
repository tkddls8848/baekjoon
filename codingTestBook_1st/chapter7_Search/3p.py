import random

N,take = 4,6 #17
'''
dduk = [19,15,10,17]
'''
dduk = []
cnt = 0
limit_cnt=100
for _ in range(0,N):
    dduk.append(random.randint(0,20))


def cut(take, dduk, start, end, cnt):
    float_mid = (start + end) / 2
    mid = int(float_mid)
    total = 0

    if cnt < limit_cnt:
        cnt += 1
        for _ in dduk:
            differ = _ - mid
            if differ > 0:
                total += differ
        print(dduk, total, take, start,end, mid, cnt)
        if total > take:
            cut(take, dduk, mid + 1, end, cnt)
        elif total < take:
            cut(take,dduk,start,mid, cnt)
        elif total == take:
            print('answer', mid)
    elif cnt >= limit_cnt:
        print('alt answer', mid)



cut(take, dduk, 0, max(dduk), cnt)


