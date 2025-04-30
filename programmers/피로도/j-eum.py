from collections import deque


def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    # q = deque([(k, 0, [False] * n)])
    q = deque([(k, 0, 0)])

    while q:
        fatigue, cleared_count, visited = q.popleft()
        answer = max(answer, cleared_count)

        # for i in range(n):
        #     if not visited[i] and fatigue >= dungeons[i][0]:
        #         nxt_visited = visited[:]  # 리스트 복사
        #         nxt_visited[i] = True
        #         q.append((fatigue - dungeons[i][1], cleared_count + 1, nxt_visited))
        # 리스트 복사는 크기가 커질수록 성능 저하를 일으킬 수 있지만, 비트마스크는 상수 시간에 상태를 관리할 수 있다
        for i in range(n):
            if not (visited & (1 << i)) and fatigue >= dungeons[i][0]:
                q.append(
                    (fatigue - dungeons[i][1], cleared_count + 1, visited | (1 << i))
                )

    return answer
