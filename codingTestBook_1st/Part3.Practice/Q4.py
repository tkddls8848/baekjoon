n = input()
list = list(map(int, input().split()))
'''
5
3 2 1 1 9
'''
sorted(list)
answer = 1
while answer >= 0:
    tmp = answer
    for _ in list:
        if tmp >= _:
            tmp = tmp - _
    if tmp == 0:
        answer = answer + 1
    else:
        break
print(answer)


