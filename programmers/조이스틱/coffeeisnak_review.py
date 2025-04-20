def solution(name):
    answer = 0
    l = len(name)
    # 1. 세로로 움직이는 경우의 수
    for char in name:
        cur_diff = ord(char) - ord("A")
        answer += min(cur_diff, 26 - cur_diff)

    # 2. 좌우로 움직이는 경우의 수
    # 탐욕법 불가 표현 반례: "BBBBAAAABA"
    # 탐욕법: 13 (오른쪽으로 쭉 갔다가 왼쪽으로 가서 B 찍음)
    # 왼쪽먼저 가서 B 찍고 오른쪽: 12
    move_count = l - 1  # 최대 회수 (모든 자리 방문)
    name2 = 'A' + name[1:]  # 첫 자리는 이미 바꾼 것이나 마찬가지
    for right_end in range(l):
        left_end = right_end + 1
        while left_end < l and name2[left_end] == "A":  # 방문 필요없는 구간을 지나침
            left_end += 1

        # 위에서 준비된 두가지 인덱스 => r, l
        # r는 앞에서 부터 세온 친구, l는 거기서 부터 A를 최대한 뛰어서 나온 인덱스 (원순열에서 반지 형태)
        # 선택지 두가지
        # 1. 왼쪽으로 l을 먼저 방문하고 다시 오른쪽으로 출발하여 r까지 진행 (j까지 가는 부분은 중복됨)
        # 2. r까지 갔다가 왼쪽으로 l까지 감 (i까지 가는 부분이 중복됨)
        move_count = min(
            move_count, 2 * right_end + (l - left_end), 2 * (l - left_end) + right_end
        )

    answer += move_count
    return answer
