from collections import deque
from typing import List


def solution(n: int, vertex: List[List[int]]) -> int:
    graph = [[] for _ in range(n + 1)]
    
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n + 1)
    distance[1] = 0
    
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    max_distance = max(distance)
    
    farthest_nodes_count = distance.count(max_distance)
    
    return farthest_nodes_count
