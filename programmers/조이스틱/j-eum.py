# https://school.programmers.co.kr/questions/83949
def solution(name):
    n = len(name)
    min_moves = n - 1
    moves = 0
    
    for i in range(n):
        diff = ord(name[i]) - ord("A")
        moves += min(diff, 26 - diff)
    
        # 다음번이 A인 경우 연속된 개수 찾기
        nxt = i + 1
        while nxt < n and name[nxt] == "A":
            nxt += 1
        if nxt - i > 1:
            # 오른쪽으로 진행 중 왼쪽으로 돌아가면 얼마나 걸리는지
            distance_to_left_end = i * 2 + n - nxt
            # 왼쪽으로 진행 중 오른쪽으로 돌아가면 얼마나 걸리는지
            distance_to_right_end = (n - nxt) * 2 + i
            min_moves = min(min_moves, distance_to_left_end, distance_to_right_end)
    
    return moves + min_moves
