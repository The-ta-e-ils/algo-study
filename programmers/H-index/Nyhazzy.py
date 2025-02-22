def solution(citations):
    h_index = 0
    citations.sort(reverse=True) #인용횟수 내림차순 정렬
    n = len(citations)
    
    for i, citations in enumerate(citations):
        if citations >= i+1:
            h_index = i+1
        else:
            break
    
    return h_index