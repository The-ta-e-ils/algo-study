from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    def bfs(a, b):
        q = deque()
        q.append((a, b))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))

        return maps[n - 1][m - 1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
