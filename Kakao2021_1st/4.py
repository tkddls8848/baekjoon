n=6
s=4
a=6
b=2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]


import heapq

INF = 10**9
def solution(n, s, a, b, fares):
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in fares:
        graph[_[0]][_[1]] = _[2]
        graph[_[1]][_[0]] = _[2]

    def dijkstra(start, graph):
        DP = [INF for _ in range(n + 1)]
        q = []
        heapq.heappush(q, (0, start))
        DP[start] = 0
        while q:
            cost, pos = heapq.heappop(q)
            for i in range(len(graph[pos])):
                total = cost + graph[pos][i]
                if DP[i] > total:
                    DP[i] = total
                    heapq.heappush(q, (total, i))
        return DP
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, graph)[i] + dijkstra(i, graph)[a] + dijkstra(i, graph)[b])
    return answer



print(solution(n,s,a,b,fares))