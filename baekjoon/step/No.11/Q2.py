n = int(input())
answer = 0
for i in range(n):
    tmp = list(str(i))
    tmp.append(str(i))
    result = sum(list(map(int, tmp)))
    if result == n:
        answer = i
        break
print(answer)