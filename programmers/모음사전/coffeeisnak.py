def solution(word):
    # chars 배열은 이미 사전 순
    chars = ['A', 'E', 'I', 'O', 'U']
    
    # default_weigths = [1, 5, 25, 125, 625] (5의 거듭제곱들, 0 ~ 4승 까지)
    default_weights = [5 ** i for i in range(5)]  
    
    # weights = [781, 156, 31, 6, 1]
    # 이는 1째 자리에서 가질 수 있는 경우의 수,
    # 2째 자리에서 가질수 있는 경우의 수,
    # ...
    weights = [sum(default_weights[:j + 1]) for j in range(4, -1, -1)]
    
    answer = 0
    for i in range(len(word)):
        # 현재 문자
        cur_char = word[i]
        # 현재 위치의 weight
        cur_weight = weights[i]
        
        # 현재 문자의 인덱스 = 자신보다 사전 순으로 앞선 문자의 개수
        cur_char_idx = chars.index(cur_char)
        
        # 따라서 앞선 문자 개수 * 현재 위치의 weight를 더해줌.
        # 이는 예를 들어 AC 라면, C 입장에서 'AA..', 'AB..' 는 모두 자신보다 앞서고
        # 이들을 모두 세어서 더해주는 느낌임.
        answer += cur_char_idx * cur_weight
    
    # 따라서 위에서 세어준 각 자리의 가중치 * 인덱스에 더해서
    # len(word)를 더해주고 있음. => 좀 더 쉽게 말하면
    # len(word) - 1 + 1 을 더해줌
    # 여기서 1은 자기 자신, 혹은 'A'가 0번째가 아니고 1번째임을 고려
    # 여기서 len(word) - 1은 word가 AEIOU 라면
    # 자신보다 앞서 A, AE, AEI, AEIO 가 있음.
    # 그런데 앞서서는 사실상 매 반복마다 '자신보다 사전적으로 앞선' 것들만 더해줬음
    # 즉, 1번째 반복에서는 A가 더해지지 않았고,
    # 2번째 반복에서는 AE가 더해지지 않았음.
    # 그런데 이들이 더해져야 함. => 실제로 AEIOU보다 앞서니까. = len(word) - 1
    return answer + len(word)
