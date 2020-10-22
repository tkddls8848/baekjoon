import sys
import heapq
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2 
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())  # 노드 개수, 간선의 수
start = int(input())  # 시작노드
graph = [[] for i in range(n + 1)]  # 노드당 연결된 노드 정보
visited = [False] * (n + 1)  # 방문여부
distance = [INF] * (n + 1)  # 현재 파악한 최단거리 테이블 초기화
for _ in range(m):  # 모든 간선정보 입력
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    visited[start] = True
    while q:
        dist,now = graph[start][0], graph[start][1]
        if visited[start]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
    print(distance[i])




