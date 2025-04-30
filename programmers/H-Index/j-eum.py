def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        t = min(i + 1, citations[i])
        answer = max(answer, t)

    return answer
