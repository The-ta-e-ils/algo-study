from collections import deque

def solution(n, edge):
    # 1. 연결 상태 저장 => 1에서 부터 가까운 순서를 보장해줘야함.
    # 그렇지 않을 경우, 분명 연결되어있는데 연결이 안되어있는 것처럼 처리될 수 있음.
    connections = dict(zip(list(range(1, n + 1)), [[] for _ in range(n)]))
    
    for s, e in edge:
        connections[s].append(e)
        connections[e].append(s)
    
    # 2. 핵심 로직?? 1에서 가까운 노드들부터 돌면서 최대값들을 가져옴.
    # 이 때 반복 종료를 위하여 visited 셋 관리
    dq = deque([1])
    visited = set([1])
    dist = [0] + [float('inf')] * (n - 1)
    
    while dq:
        cur_node = dq.pop()
        
        for n_node in connections[cur_node]:
            dist[n_node - 1] = min(dist[n_node - 1], dist[cur_node - 1] + 1)
            
            if n_node not in visited:
                dq.appendleft(n_node)
                visited.add(n_node)
    
    # 3. 마지막으로 최대값 개수를 찾아 반환
    max_dist = 0
    answer = 0
    
    for d in dist:
        if d > max_dist:
            answer = 1
            max_dist = d
        elif d == max_dist:
            answer += 1
        
    return answer
