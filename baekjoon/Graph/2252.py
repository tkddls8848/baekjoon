from collections import deque

N, M = list(map(int, input().split()))
inDegree = [0 for i in range(N)]
graph = [[] for i in range(N)]
answer = []
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    inDegree[b-1] += 1

for i in range(len(inDegree)):
    if inDegree[i] == 0:
        q.append(i)
        answer.append(i+1)

while q:
    target = q.popleft()
    for i in graph[target]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)
            answer.append(i+1)

for _ in answer:
    print(_, end=' ')

