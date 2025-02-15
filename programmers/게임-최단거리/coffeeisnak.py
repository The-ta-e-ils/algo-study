from collections import deque

def solution(maps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = len(maps)
    m = len(maps[0])
    dq = deque([(1, 1, 1)])
    dp = [[float('inf') for _ in range(m)] for _ in range(n)]
    dp[0][0] = 0
    flag = False
    
    
    while dq:
        r, c, d = dq.pop()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 1 <= nr <= n and 1 <= nc <= m and maps[nr - 1][nc - 1] and d + 1 < dp[nr - 1][nc - 1]:
                dq.appendleft((nr, nc, d + 1))
                dp[nr - 1][nc - 1] = d + 1
                if nr == n and nc == m:
                    flag = True
    
    if flag:
        return dp[n - 1][m - 1]
    else:
        return -1
