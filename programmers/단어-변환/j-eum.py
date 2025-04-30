from collections import deque


def diff_between_words(w1, w2):
    cnt = 0
    for ch1, ch2 in zip(w1, w2):
        if ch1 != ch2:
            cnt += 1
    return cnt


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    n = len(words)
    q = deque([(begin, 0, [False] * n)])

    while q:
        current, step, visited = q.pop()
        if current == target:
            return step

        for i in range(n):
            if not visited[i] and diff_between_words(current, words[i]) == 1:
                nxt_visited = visited[:]
                nxt_visited[i] = True
                q.append((words[i], step + 1, nxt_visited))

    return answer
