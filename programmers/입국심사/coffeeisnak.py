def solution(n, times):
    min_time = 1
    max_time = n * max(times)
    
    answer = max_time
    
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        
        total_people = sum(mid // time for time in times)
        
        if total_people >= n:
            answer = mid
            max_time = mid - 1
        else:
            min_time = mid + 1
    
    return answer
