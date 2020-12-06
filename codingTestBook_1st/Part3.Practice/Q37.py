'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n) for _ in range(n)]
distance = []
for j in range(n):
    graph[j-1][j-1] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)



