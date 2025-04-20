from collections import deque


def check_can_become(past, nxt):
    # 1개만 다른지 체크하는 함수
    cnt = 0
    l = len(past)

    for i in range(l):
        cnt += int(past[i] != nxt[i])

        if cnt > 1:
            return False

    return cnt == 1


def solution(begin, target, words):
    dq = deque([(begin, 0)])
    l = len(words)

    # 타겟이 words 안에 없으면 애초에 절대불가
    if target not in words:
        return 0

    # deque 형태로 하나만 다른(바꿀 수 있는 애들을 계속 추가해나감.)
    # 이 중 얻어걸리면 그대로 리턴
    # 메모리를 많이쓸 것 같아서 불안불안 ... 했으나 통과함.
    while dq:
        cur_string, cnt = dq.pop()

        if cur_string == target:
            return cnt

        for word in words:
            if word != cur_string and check_can_become(cur_string, word):
                dq.appendleft((word, cnt + 1))
