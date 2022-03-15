from itertools import combinations

n = input()
arr = list(map(int, input().split(" ")))
answer = []
for i in range(1, len(arr)+1):
    for c in combinations(arr, i):
        answer.append(sum(c))
answer = list(set(answer))
answer.append(-1)
for i in range(len(answer)):
    if i != answer[i]-1:
        break

