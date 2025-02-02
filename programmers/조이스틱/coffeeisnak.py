# 문제는 크게 두개
# 1. 주어진 글자수에 대해서 바꿔야 할 글자들이 있다면, 해당 위치를 좌 우로 움직여서 최소 몇번 내에 방문할 수 있는지 파악
# 2. 주어진 글자에 대해서 A에서 해당 글자까지 변화시키는 최소값들의 합.
def solution(name):
    change_count = 0
    l = len(name)

    # 1. A에서 해당 글자까지 바꾸는 최소값의 합
    for char in name:
        cur_diff = ord(char) - ord("A")
        change_count += min(cur_diff, 26 - cur_diff)
    
    # 2. 첫 위치에서 방문해야 하는 모든 위치를 방문하는 최소 값
    
    # 탐욕법이 안되는 이유
    # 원래 탐욕법을 시도했고 몇개의 테스트 케이스 제외하고 정답이라 예외처리문제인줄 알았음.
    # 반례: name이 "BBBBAAAABA" 일 때.
    # 탐욕법을 따라 이동하면 첫 자리에서 오른쪽으로 갔다가 왼쪽으로 가서 총 13
    # 근데 첫 자리에서 왼쪽으로 먼저 가서 B를 찍고 다시 돌아오면 12
    # 근본적으로 탐욕법으로 접근할 수 없음을 보여주는 반례라고 생각함. 이렇게 예외를 둬야만 탐욕법으로 풀리면 왜 탐욕법 문제인지를 모르겠어서 탐욕법을 사용하지 않음.
    
    move_count = l - 1  # 가능한 최대값

    for i in range(l):
        next_to_visit = i + 1
        while next_to_visit < l and name[next_to_visit] == "A":
            next_to_visit += 1
        
        # 두가지 선택지가 있음. (i와 next_to_visit 사이는 A밖에 없음)
        # 1. i까지 진행한 다음 왼쪽으로 진행 시작하여 next_to_visit을 방문
        # 2. next_to_visit을 왼쪽으로 먼저 방문한 다음 우측으로 진행을 시작하여 i를 방문
        # 두번 이상 방향성을 바꾸는 경우는 존재할 수 없음. => 이 문제는 결국 원순열에서 최소 방문 회수를 결정하는 문제임
        # 만약 두번 방향성을 바꾸게 된다면 전체적인 이동 경로는 (말이 되는 케이스만 보면) 일부가 끊어진 링 형태로, 양쪽이 겹치게 됨.
        # 이 때 1번만 방향을 바꾸는 형태로 해당 경로를 지나갈 수 있는 개선안이 무조건 존재하게 됨
        move_count = min(move_count, 2 * i + l - next_to_visit, 2 * (l - next_to_visit) + i)  

    return change_count + min(move_count, l - 1)

