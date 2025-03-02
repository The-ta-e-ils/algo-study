from collections import deque

def solution(maps):
    # 맵의 행(n)과 열(m) 길이
    n = len(maps)
    m = len(maps[0])
    
    # 동, 서, 남, 북 4방향 이동을 위한 벡터 (x, y) 좌표 변화값
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # BFS를 위한 deque 선언, (행, 열, 지나온 칸 수)를 저장
    # 시작점은 좌측 상단인 (0, 0), 시작 칸도 포함하므로 거리(칸 수)는 1부터 시작
    dq = deque([(0, 0, 1)])
    
    # 재방문을 막기 위해 시작점을 0으로
    maps[0][0] = 0

    # BFS 진행
    while dq:
        x, y, distance = dq.popleft()  # 현재 위치와 누적 이동 칸 수
        
        # 만약 우측 하단 도착이면, 현재까지의 칸 수를 반환
        if x == n - 1 and y == m - 1:
            return distance
        
        # 4가지 방향에 대해 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 이동하려는 위치가 맵 안에 있고, 벽이 아니라면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                dq.append((nx, ny, distance + 1))  # 이동 후 칸 수 증가
                maps[nx][ny] = 0  # 방문 처리 (중복 방문 방지)
    
    # 모든 경로 탐색 후에도 도착하지 못한 경우 -1을 반환
    return -1
