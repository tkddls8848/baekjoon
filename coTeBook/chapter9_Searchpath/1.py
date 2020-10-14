import sys
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
# 노드 개수, 간선의 수
n, m = map(int, input().split())
#시작노드
start = int(input())
#노드당 연결된 노드 정보
graph = [[] for i in range(n + 1)]
#방문여부
visited = [False] * (n + 1)
#현재 파악한 최단거리 테이블 초기화
distance = [INF] * (n + 1)
#모든 간선정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])

#방문하지 않는 노드 중 가장 최단거리가 짧은 노드 반환
def get_shortest_node():
    key = 0
    min_value = INF
    for i in range(1, n+1):
        if distance[i] <min_value and not visited[i]:
            key = i
            min_value = distance[i]
    return key

#다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_shortest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)


print(graph,visited,distance)