from typing import List


def solution(citations: List[int]) -> int:
    citations.sort()
    n = len(citations)
    answer = 0

    for i in range(n):
        h = n - i
        if citations[i] >= h:
            answer = max(answer, h)
    
    return answer
