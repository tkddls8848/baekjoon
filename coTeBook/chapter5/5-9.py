# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9


# dfs 함수 구현
def dfs(graph, visited, n):
    # 노드 방문 표시
    visited[n] = True
    print(n, end=' ')
    # 해당 노드 연결 된 하위 노드 탐색
    for i in graph[n]:
        # 하위 노드가 방문하지 않았다면 방문하고 하위 노드 탐색
        if not visited[i]:
            dfs(graph, visited, i)


# 정의된 DFS 함수 호출
dfs(graph, visited, 1)