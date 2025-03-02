from collections import deque

def solution(n, vertex):
    # 그래프를 인접 리스트 형태로 변환
    graph = {i: [] for i in range(1, n+1)}
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # BFS 초기화
    queue = deque([1])
    distances = {i: -1 for i in range(1, n+1)}
    distances[1] = 0  # 시작 노드 거리 0
    
    # BFS 수행
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # 최장 거리 찾기
    max_distance = max(distances.values())
    
    # 최장 거리 노드 개수 반환
    return sum(1 for d in distances.values() if d == max_distance)
