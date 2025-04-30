def solution(n, times):
    left = 1
    right = min(times) * n  # 최악의 경우:
    answer = right

    while left <= right:
        mid = (left + right) // 2
        people_processed = sum(mid // time for time in times)

        if people_processed >= n:
            answer = mid  # 더 짧은 시간도 가능한지 확인
            right = mid - 1
        else:
            left = mid + 1

    return answer
