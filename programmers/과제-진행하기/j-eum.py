from collections import deque
from datetime import datetime, timedelta

def solution(plans):
    answer = []
    
    plans.sort(key=lambda x:x[1])
    plans_q = deque(plans)
    
    hold = []
    current_time_str = plans_q[0][1]
    current_time = datetime.strptime(current_time_str, "%H:%M")
    
    while plans_q:
        next_plan_start_time_str = plans_q[0][1]
        next_plan_start_time = datetime.strptime(next_plan_start_time_str, "%H:%M")
        if current_time < next_plan_start_time and hold:
            current_plan = hold.pop()
        else:
            current_plan = plans_q.popleft()
            current_time = datetime.strptime(current_plan[1], "%H:%M")
            if not plans_q:
                answer.append(current_plan[0])
                break
        
        next_plan = plans_q[0]

        duration = int(current_plan[2])
        current_end_time = current_time + timedelta(minutes=duration)
        next_start_time = datetime.strptime(next_plan[1], "%H:%M")
        
        if current_end_time <= next_start_time:
            answer.append(current_plan[0])
            current_time = current_end_time
        else:
            diff = current_end_time - next_start_time
            diff_minutes_str = str(int(diff.total_seconds() // 60))
            current_plan[2] = diff_minutes_str
            hold.append(current_plan)
            current_time = next_start_time
    
    while hold:
        answer.append(hold.pop()[0])
        
    return answer
