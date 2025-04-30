from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    q = deque([1])
    distance[1] = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if distance[nxt] == -1:
                q.append(nxt)
                distance[nxt] = distance[cur] + 1

    max_d = max(distance)
    answer = 0
    for d in distance:
        if d == max_d:
            answer += 1

    return answer
