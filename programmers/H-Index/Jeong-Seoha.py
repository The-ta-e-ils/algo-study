def solution(citations):
    
    # h번 이상 인용된 논문이 최소 h 이상
    count_citations = len(citations)
    
    count =  [0] * (count_citations + 1) #  논문 개수+1 크기의 배열 생성
    
    # 인용 횟수 세기
    for n in citations:
        if n >= count_citations:
            count[count_citations] += 1
        else:
            count[n] += 1
    
    # 역순 누적합
    total = 0
    for h in range(count_citations, -1, -1):  # 큰 h부터 확인
        total += count[h]  # 누적합 증가
        if total >= h:  # h번 이상 인용된 논문이 h개 이상인지 확인
            return h  # 최대 h 반환
    
    return 0
