from collections import deque


def solution(queue1, queue2):
    # 초기화
    answer = 0
    l = len(queue1)
    s1 = sum(queue1)
    s2 = sum(queue2)

    # 만약 숫자 다 합해서 짝수가 아니면 애초에 불가
    if (s1 + s2) % 2:
        return -1

    # dq1, dq2를 왔다리 갔다리
    dq1 = deque(queue1)
    dq2 = deque(queue2)

    # answer <= 3 * l 로 [1, 1], [1, 5]와 같이 무한히 반복되는 경우를 뺀다.
    while s1 != s2 and answer <= 3 * l:
        if s1 > s2:
            cur_num = dq1.popleft()
            s1 -= cur_num
            dq2.append(cur_num)
            s2 += cur_num
            answer += 1
        elif s1 < s2:
            cur_num = dq2.popleft()
            s2 -= cur_num
            dq1.append(cur_num)
            s1 += cur_num
            answer += 1

    # 3 * l 이면 이미 3바퀴를 돌았음 => 그동안 불가면 절대 불가
    return answer if answer < 3 * l else -1
