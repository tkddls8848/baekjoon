import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
'''
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
n = int(input())
price = [[0] * n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
cost = [([INF]*n) for _ in range(n)]
for i in range(n):
    price[i] = list(map(int, input().split()))
move = [[1,0],[-1,0],[0,1],[0,-1]]


def dijkstra(node, cost, visited):
    q = []
    x, y = node[0], node[1]
    if 0 <= x < n and 0 <= y < n:
        if not visited[x][y]:
            cost[x][y] = min(cost[x][y], price[x][y])
            visited[x][y] = True
            heapq.heappush(q, [cost[x][y], x, y])
    while q:
        c, x, y = map(int, heapq.heappop(q))
        print('c',c, x, y)
        for _ in move:
            ax, ay = x + _[0], y + _[1]
            if 0 <= ax < n and 0 <= ay < n:
                if not visited[ax][ay]:
                    if cost[ax][ay] > c+price[ax][ay]:
                        heapq.heappush(q, [c+price[ax][ay], ax, ay])
                        visited[ax][ay] = True
                        cost[ax][ay] = c + price[ax][ay]
dijkstra([0,0], cost, visited)
print(cost)


