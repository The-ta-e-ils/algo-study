from collections import deque

def solution(n, edge):
    # 무방향 그래프 생성
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    
    for i in edge:
        a, b = i[0], i[1]
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    q.append(1) # 1번노드부터 시작
    visited[1] = 1 # 방문 횟수 추가
    
    while q: # q가 완전히 빌 때까지 반복
        current = q.popleft() # 방문한 노드는 큐에서 꺼내기
        
        for node in graph[current]: # node = [3,2], current node에 연결된 모든 노드 순회
            if not visited[node]: # 아직 방문하지 않은 노드라면 (0)
                visited[node] = visited[current] + 1
                q.append(node)
    # 1번노드에서 부터 여기까지 오는데 사용한 간선 개수 중 최댓값
    max_value = max(visited)
    # 1번으로부터 가장 멀리 있는 노드는 몇개?
    answer = visited.count(max_value)
    return answer