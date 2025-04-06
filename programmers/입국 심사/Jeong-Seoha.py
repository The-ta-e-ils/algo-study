def solution(n, times):
# 최소 시간은 1분, 최대 시간은 가장 오래 걸리는 심사관이 n명을 처리하는 경우로 설정
    left = 1
    right = max(times) * n  
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        # 주어진 mid 분 동안 각 심사관이 처리할 수 있는 사람의 수의 합 계산
        total = sum(mid // time for time in times)
        
        if total >= n:  # mid 시간 안에 모든 사람을 처리할 수 있다면
            answer = mid  # 더 짧은 시간으로도 가능한지 탐색
            right = mid - 1
        else:           # mid 시간 안에 처리가 부족하다면
            left = mid + 1
    return answer
