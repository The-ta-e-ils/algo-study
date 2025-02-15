def solution(citations):
    answer = -1
    l = len(citations)
    sorted_cite = sorted(citations, reverse=True)
    
    # h를 l 부터 0까지 변화시키기
    for h in range(l, -1, -1):
        index = h - 1
        
        # 만약 h 이상인 논문이 0 ~ h - 1 (h개) 이상 있다면 이를 반환
        if h and sorted_cite[index] >= h:
            answer = h
            break
    
    # 한번도 안걸리는 경우 
    # 예시 => [5, 6, 7, 8] => 원하는 값 = 4
    if answer < 0:
        answer = min(sorted_cite[-1], l)
    
    return answer
