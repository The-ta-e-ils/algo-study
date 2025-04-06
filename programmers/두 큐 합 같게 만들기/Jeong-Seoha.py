from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    target = (sum1 + sum2) // 2
    
    # 합이 나누어 떨어지지 않으면 불가능
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    total_queue = q1 + q2  # 두 큐를 하나로 연결
    left, right = 0, len(q1)  # 투 포인터 (슬라이딩 윈도우)
    current_sum = sum1
    operations = 0
    max_operations = len(q1) * 3  # 최대 연산 횟수 제한
    
    while left < len(total_queue) and right < len(total_queue):
        if current_sum == target:
            return operations
        elif current_sum < target and right < len(total_queue):  # 원소 추가
            current_sum += total_queue[right]
            right += 1
        else:  # 원소 제거
            current_sum -= total_queue[left]
            left += 1
        operations += 1
        
        if operations > max_operations:  # 무한 루프 방지
            return -1
    
    return -1
