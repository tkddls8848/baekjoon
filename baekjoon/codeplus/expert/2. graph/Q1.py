n, m = list(map(int, input().split(" ")))
graph = [[] for i in range(n)]
datas = [0 for i in range(n)]
history = []
from collections import deque
q = deque()
order = []
for i in range(m):
    tmp = list(map(int, input().split()))
    history.append(tmp)
    graph[tmp[1]-1].append(tmp[0])
    datas[tmp[1]-1] += 1
print(graph, datas)
for i in range(len(graph)):
    if graph[i] == []:
        q.append(i)
while q:
    tmp = q.pop()
    for h in history:
        if h[0] == tmp:
            history.remove(h)
            datas[h[1]-1] -= 1
            q.append(tmp)



