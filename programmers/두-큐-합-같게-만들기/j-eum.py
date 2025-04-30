from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    for _ in range(2 * len(queue1 + queue2)):
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            t = q1.popleft()
            sum1 -= t
            q2.append(t)
            sum2 += t
            answer += 1
        else:
            t = q2.popleft()
            sum2 -= t
            q1.append(t)
            sum1 += t
            answer += 1
    
    return -1
