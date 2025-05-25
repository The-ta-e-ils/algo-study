from collections import deque
def solution(q1, q2):
    s1, s2 = sum(q1), sum(q2)
    tot = s1 + s2
    if tot % 2 != 0:
        return -1

    target = tot // 2
    dq1, dq2 = deque(q1), deque(q2)
    concat = dq1 + dq2
    t_len = len(concat)
    curr = s1
    p1, p2 = 0, len(dq1)
    m = 0

    while p1 <= p2 < t_len:
        if curr == target:
            return m
        
        if curr > target:
            curr -= concat[p1]
            p1 += 1
        else:
            curr += concat[p2]
            p2 += 1
        m += 1
        if p2 == t_len and p1 == len(dq1):
            break

    return -1