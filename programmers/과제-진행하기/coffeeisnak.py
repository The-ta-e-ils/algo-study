def string_time_to_minute(time_string):
    """
    Args:
        time_string: HH:MM 형식의 시각을 나타내는 문자열

    Returns:
        시각을 분 단위로 바꾼 INT형 값을 리턴
    """
    hour, minute = s.split(":")
    return int(hour) * 60 + int(minute)


def solution(plans):
    answer = []

    # 분 단위로 숙제 시작 시각, 걸리는 시간을 바꾼 리스트를 생성 및 정렬
    min_plans = [[name, string_time_to_minute(start), int(playtime)] for name, start, playtime in plans]
    min_plans.sort(key=lambda x: x[1], reverse=True)

    # 반복문을 위한 초기 설정
    first_task = min_plans.pop()
    remain_stack = [first_task]
    cur = first_task[1]
    
    while len(min_plans) > 0:
        # 다음 과제가 아닌 미뤄둔 과제를 해야하는 경우
        if remain_stack and cur < min_plans[-1][1]:
            can_do_time = min_plans[-1][1] - cur
            
            if cur + remain_stack[-1][2] <= min_plans[-1][1]:
                task = remain_stack.pop()
                answer.append(task[0])
                cur += task[2]
            else:
                remain_stack[-1][2] -= can_do_time
                cur = min_plans[-1][1]
        # 다음 과제를 시작해야하는 경우
        else:
            next_task = min_plans.pop()
            cur = next_task[1]
            remain_stack.append(next_task)
    
    # 미뤄둔 과제를 전부 수행
    while remain_stack:
        remainder = remain_stack.pop()
        answer.append(remainder[0])
    
    return answer
