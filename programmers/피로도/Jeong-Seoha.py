from itertools import permutations

def explore_dungeons(k, dungeon_order):
    # 주어진 던전 순서에서 최대 탐험 가능한 개수 계산
    fatigue = k  # 현재 남은 피로도
    count = 0  # 탐험한 던전 개수
    
    for min_fatigue, consume_fatigue in dungeon_order:
        if fatigue >= min_fatigue:  # 최소 필요 피로도를 만족하면 탐험 가능
            fatigue -= consume_fatigue  # 피로도를 소모
            count += 1  # 탐험한 던전 수 증가
        else:
            break  # 더 이상 탐험할 수 없으면 중단
    # 탐험한 던전 개수 반환
    return count  

def solution(k, dungeons):
    # 순열을 이용한 완전 탐색으로 최대 던전 탐험 개수 찾기
    max_dungeons = 0
    
    # 모든 던전 순서 경우의 수를 확인
    for dungeon_order in permutations(dungeons):
        max_dungeons = max(max_dungeons, explore_dungeons(k, dungeon_order))
    
    return max_dungeons
