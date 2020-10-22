INF = int(1e9)
N, M = input().split()##노드의 개수, 간선의 개수
n, m =int(N), int(M)
graph = [[INF] * (n+1) for _ in range(n+1)]
'''
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] == 0 ## 대각 행렬 0

for _ in range(m):
    a,b,c = map(int, input().split())##시작 노드, 끝 노드, 이동값
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1 , n + 1):
    for b in range(1 , n + 1):
        if not a == b:
            if graph[a][b] == INF:
                print(a,'에서',b,'사이는 끊겼다.')
            else:
                print(a, '에서', b, '사이의 최단거리는 ',graph[a][b])

