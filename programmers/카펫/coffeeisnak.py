# [가로, 세로] 를 리턴하라
# 가로 >= 세로
# 이건 왜 완전 탐색 문제인가요...?
def solution(brown, yellow):
    # brown == 2 * w + 2 * (h - 2)
    # yellow == (w - 2) * (h - 2)
    # w >= 3, h >= 3
    sum = (brown + 4) // 2
    pro = yellow + brown

    w = sum + int((sum ** 2 - 4 * pro) ** (0.5) + 0.1)
    w //= 2
    h = sum - w

    return [w, h]
