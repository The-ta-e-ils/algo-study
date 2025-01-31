def solution(plans):
    # 정렬
    plans.sort(key = lambda x : (int(x[1][0:2]),int(x[1][3:])))
    stop_list = []
    end_list = []

    for i in range(0, len(plans)-1):
        end_time = int(plans[i][1][0:2])*60 + int(plans[i][1][3:]) + int(plans[i][2]) # 해당 과목이 끝나는 time 
        start_time = int(plans[i+1][1][0:2])*60 + int(plans[i+1][1][3:]) # 해당 다음 과목이 시작하는 time

        diff_time = end_time-start_time
        print(plans[i][0], "diff_time : ", diff_time)
        # 과목이 제때 끝날 때
        if diff_time == 0:
            end_list.append(plans[i][0])
        # 과목이 제때 끝나지 못할 때
        elif diff_time > 0:
            # [과목, 남은 시간]
            stop_list.append([plans[i][0], int(plans[i][2]) - (int(plans[i+1][1][0:2])*60 + int(plans[i+1][1][3:]) - int(plans[i][1][0:2])*60 - int(plans[i][1][3:]))])
        # 과목이 일찍 끝날 때
        else:
            end_list.append(plans[i][0])
            
            # 과목이 일찍 끝나고 남는 시간
            while True:
                print(diff_time)
                print(stop_list)
                if len(stop_list) != 0:
                    stop_element = stop_list.pop()
                    stop_element[1] = stop_element[1] + diff_time
                    # diff_time을 딱 맞게 소모한거라면? => 다음 plan 가져오기
                    if stop_element[1] == 0:
                        end_list.append(stop_element[0])
                        break
                    # diff_time을 다 소모하는거라면? => 다시 stop_list에 넣기
                    elif stop_element[1] > 0:
                        stop_list.append(stop_element)
                        break
                    # diff_time을 다 소모하지 못했다면? => 다음 요소 꺼내기
                    else:
                        end_list.append(stop_element[0])
                        # 남는 시간
                        diff_time = stop_element[1]
                        print("요소 꺼낸 후 : ", diff_time)
                else:
                    break

    end_list.append(plans[-1][0])

    # 마지막까지 남아있는게 있다면 차례대로 뽑아내기
    if len(stop_list) != 0:
        for i in range(0, len(stop_list)):
            end_list.append(stop_list.pop()[0])

    return end_list