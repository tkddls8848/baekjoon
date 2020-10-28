from collections import deque
'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
v,e = map(int, input().split())
towardNum = [0] * (v+1) ##각 노드 당 간선 개수
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    towardNum[b] += 1

def topology_sort():
    q = deque()
    result = []
    for i in range(1, len(graph)):
        if towardNum[i] == 0:
            q.append(i)

            break

    while q:
        start = q.popleft()
        result.append(start)

        for i in graph[start]:

            towardNum[i] -= 1
            if towardNum[i] == 0:
                q.append(i)
    print(result)


topology_sort()
