# import heapq
# from datetime import datetime
from typing import List

def solution(tasks: List[List[str]]) -> List[str]:
    
    def time_to_minutes(time_str):
        """
        Converts time string to minute-based number
        """
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes
    
    # Sort tasks by start time
    tasks = sorted(tasks, key=lambda x: time_to_minutes(x[1]))
    
    # Init trackers
    result = [] # task names
    stack = []  # backed-up jobs
    current_time = 0
    i = 0  # iterator index over sorted tasks

    while i < len(tasks) or stack:
        # No new task OR it starts later than curr task...
        # ...AND there are pending tasks
        if stack and (i >= len(tasks) or current_time < time_to_minutes(tasks[i][1])):
            task_name, start_time, duration = stack.pop() # start the most recently put off job
        # If any of the above doesn't hit
        else:
            task_name, start_time, duration = tasks[i] # start the new task
            i += 1
            # set current time to new job's start time
            current_time = max(current_time, time_to_minutes(start_time))
        
        duration = int(duration)
        
        end_time = current_time + duration
        
        # Check if another task starts during the current task time
        # Pre-sorting makes this moot?
        while i < len(tasks) and time_to_minutes(tasks[i][1]) < end_time:
            # If a new task starts, put off current task...
            # ...with an updated playtime as the remainder of the completion time
            stack.append((task_name, start_time, end_time - time_to_minutes(tasks[i][1])))
            task_name, start_time, duration = tasks[i]
            current_time = time_to_minutes(start_time)
            end_time = current_time + int(duration)
            i += 1

        # If no more interruptions, finish current task
        result.append(task_name)
        current_time = end_time

    return result