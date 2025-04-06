def solution(plans):
    # hh:mm 형식에서 분 단위로 변환하는 함수
    def convert_time(time_str):
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes

    # 과제를 수행하고 멈춘 과제를 관리하는 함수
    def process_tasks(task_list):
        finished_tasks = []
        paused_tasks = []
        current_time = 0

        for i, (task_name, start_time, duration) in enumerate(task_list):
            start_time = convert_time(start_time)
            duration = int(duration)

            # 중단된 과제가 남아 있고, 현재 시간이 새로운 과제 시작 전이면 처리
            while paused_tasks and current_time < start_time:
                last_task = paused_tasks[-1][0]  # 마지막으로 멈춘 과제 이름
                remaining_time = paused_tasks.pop()[1]  # 남은 시간

                time_available = start_time - current_time
                if remaining_time <= time_available:
                    current_time += remaining_time
                    finished_tasks.append(last_task)  # 과제 완료 리스트에 추가
                else:
                    paused_tasks.append((last_task, remaining_time - time_available))
                    current_time = start_time
                    break

            # 새로운 과제 수행 시작
            current_time = start_time + duration

            # 다음 과제와 시간이 겹치는지 확인
            if i + 1 < len(task_list):
                next_task_start = convert_time(task_list[i + 1][1])
                if current_time > next_task_start:
                    paused_tasks.append((task_name, current_time - next_task_start))
                    current_time = next_task_start
                else:
                    finished_tasks.append(task_name)  # 과제 완료 리스트에 추가
            else:
                finished_tasks.append(task_name)  # 마지막 과제 처리

        # 남아 있는 중단된 과제 처리
        while paused_tasks:
            finished_tasks.append(paused_tasks.pop()[0])  # 남은 과제 중 이름만 추가

        return finished_tasks

    # 과제 시작 시간을 기준으로 정렬 후 처리
    plans.sort(key=lambda task: convert_time(task[1]))
    return process_tasks(plans)
