# [가로, 세로] 를 리턴하라
# 가로 >= 세로
# 이건 왜 완전 탐색 문제인가요...?
def solution(brown, yellow):
    # brown == 2 * w + 2 * (h - 2)
    # yellow == (w - 2) * (h - 2)
    # w >= 3, h >= 3
    total = yellow + brown

    for h in range(3, total):
        w = total // h
        
        if total == w * h and 2 * w + 2 * h == brown + 4:
            return [w, h]
